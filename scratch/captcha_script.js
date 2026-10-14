
(function () {
    var root = document.getElementById('iprn-cap-cap3c4b0f6f');
    if (!root) { return; }

    var PURPOSE = root.getAttribute('data-purpose');
    var elNote   = document.getElementById('cap-note-cap3c4b0f6f');
    var elStatus = document.getElementById('cap-status-cap3c4b0f6f');
    var elStage  = document.getElementById('cap-stage-cap3c4b0f6f');
    var elCanvas = document.getElementById('cap-canvas-cap3c4b0f6f');
    var elDot    = document.getElementById('cap-dot-cap3c4b0f6f');
    var elStep   = document.getElementById('cap-step-cap3c4b0f6f');
    var elToken  = document.getElementById('cap-token-cap3c4b0f6f');
    var elAnswer = document.getElementById('cap-answer-cap3c4b0f6f');

    /* Ring drawn around each endpoint, in PICTURE pixels. 30 is the most the
       geometry allows: endpoints are 36px apart less up to 8px of jitter, so a
       larger ring would overlap its neighbour. The ring is only the visual; the
       tap area is REACH, resolved by nearest endpoint, so it can be generous
       without any two ever overlapping. */
    var HIT = 30;

    /* How far from an endpoint's centre a tap still counts, in PICTURE pixels. On
       a phone the picture runs at about 0.75 scale, so 24 here is an 18px radius
       under the finger, a 36px target. The nearest endpoint wins, so this only
       decides whether a tap far from every circle is ignored - and it is, because
       a tap in the middle of the threads is someone looking, not answering. */
    var REACH = 24;

    var state = { marks: [], picks: [], ends: [], hits: [], w: 1, h: 1, solved: false, busy: false };

    var MSG_FAIL     = 'Could not load the check. Press the arrow to retry.';
    var MSG_EXPIRED  = 'Your session has expired. Please reload the page and try again.';
    var MSG_CHECKING = 'Checking your answer...';
    var MSG_THANKS   = 'Thanks - you can continue.';
    var MSG_WRONG    = 'Not quite - that is not where the thread ends. Try this new puzzle.';
    var MSG_STALE    = 'That puzzle expired. Here is a fresh one.';

    /* keep: leave the picture on screen under the status line. Used while the
       answer is being checked, so the second ring is seen to take. */
    function say(msg, bad, keep) {
        elStatus.textContent = msg;
        elStatus.className = bad ? 'cap-status err' : 'cap-status';
        elStatus.style.display = '';
        if (!keep) { elStage.style.display = 'none'; }
    }

    function note(msg) {
        elNote.textContent = msg || '';
        elNote.style.display = msg ? '' : 'none';
    }

    /* The proof-of-work worker.

       Uses crypto.subtle rather than a hand-written SHA-256. An earlier draft here
       shipped its own implementation to dodge the secure-context requirement; that
       was the wrong trade. There is no JS runtime on this host, so a hand-rolled
       digest could not be executed or verified before shipping, and a single typo in
       it would not degrade the check - it would make the check IMPOSSIBLE TO PASS,
       silently, for every user of every login door. Untestable cryptography in front
       of the front door is not worth the small economic edge it was buying.

       When crypto.subtle is absent the server issues zero difficulty instead - see
       CaptchaController::difficultyFor(). Nobody is locked out by a missing API.

       LANES. digest() returns a promise per call, and awaiting them one at a time
       meant the cost was all scheduling: one hash per trip through the event loop,
       which on a phone is several seconds of "Checking your browser...". Issuing
       32 at once and waiting on the batch keeps the crypto thread fed and cuts the
       wait by most of that; the first satisfying counter in the batch is the
       answer, and any counter satisfies the server equally. */
    var WORKER_SRC = [
        'self.onmessage = function (ev) {',
        '  var enc = new TextEncoder();',
        '  var prefix = ev.data.prefix + ":";',
        '  var need = ev.data.bits;',
        '  var n = 0;',
        '  var LANES = 32;',
        '  function lead(bytes) {',
        '    var seen = 0;',
        '    for (var i = 0; i < bytes.length; i++) {',
        '      var v = bytes[i];',
        '      if (v === 0) { seen += 8; continue; }',
        '      for (var b = 7; b >= 0; b--) { if (v & (1 << b)) { return seen; } seen++; }',
        '    }',
        '    return seen;',
        '  }',
        '  function tryOne(s) {',
        '    return self.crypto.subtle.digest("SHA-256", enc.encode(prefix + s)).then(function (buf) {',
        '      return lead(new Uint8Array(buf)) >= need ? s : null;',
        '    });',
        '  }',
        '  function round() {',
        '    var jobs = [];',
        '    for (var i = 0; i < LANES; i++) { jobs.push(tryOne("" + (n + i))); }',
        '    n += LANES;',
        '    Promise.all(jobs).then(function (found) {',
        '      for (var i = 0; i < found.length; i++) {',
        '        if (found[i] !== null) { self.postMessage(found[i]); return; }',
        '      }',
        '      round();',
        '    }).catch(function () { self.postMessage({ error: 1 }); });',
        '  }',
        '  round();',
        '};'
    ].join('\n');

    var worker = null;

    function solvePow(token, bits, done, fail) {
        /* Zero difficulty: the server already decided this client should not be
           asked to spend. Hand back any non-empty value and move on. */
        if (!bits) { done('0'); return; }

        if (!(self.crypto && self.crypto.subtle)) { fail(); return; }

        try {
            if (!worker) {
                worker = new Worker(URL.createObjectURL(
                    new Blob([WORKER_SRC], { type: 'application/javascript' })
                ));
            }
        } catch (e) { fail(); return; }

        worker.onmessage = function (ev) {
            if (ev.data && ev.data.error) { fail(); return; }
            done(ev.data);
        };
        worker.onerror = function () { fail(); };
        worker.postMessage({ prefix: token, bits: bits });
    }

    function csrf() {
        var m = document.querySelector('meta[name="csrf-token"]');
        if (m) { return m.getAttribute('content'); }
        var i = document.querySelector('input[name="_token"]');
        return i ? i.value : '';
    }

    /* Resolves to { ok, status, body } for ANY response, JSON or not. A 419 from an
       expired session is an HTML page; parsing it used to throw straight into the
       generic "press the arrow" message, and the arrow cannot mint a new CSRF
       token, so the visitor was told to retry something that could never work. */
    function post(url, data) {
        return fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRF-TOKEN': csrf()
            },
            credentials: 'same-origin',
            body: JSON.stringify(data)
        }).then(function (r) {
            return r.json().then(
                function (j) { return { ok: r.ok, status: r.status, body: j }; },
                function ()  { return { ok: false, status: r.status, body: {} }; }
            );
        });
    }

    function pct(v, of) { return (v / of * 100) + '%'; }

    function paint(puzzle) {
        state.marks = puzzle.marks;
        state.ends  = puzzle.ends;
        state.w     = puzzle.width;
        state.h     = puzzle.height;
        state.picks = [];
        state.hits  = [];
        elCanvas.innerHTML = '';

        /* Never wider than the picture itself; narrower columns scale it down and
           the percent placement below follows. */
        elCanvas.style.maxWidth = puzzle.width + 'px';

        var img = new Image();
        img.src = puzzle.image;
        img.width = puzzle.width;
        img.height = puzzle.height;
        img.alt = '';
        img.draggable = false;
        elCanvas.appendChild(img);

        /* Rings in PERCENT of the box, never in pixels. The box is the picture's
           rectangle at whatever size the column gave it, so a percent of the box is
           the same point on the picture at every scale. Pixel placement was the
           phone bug: right on a desktop at 1:1, a full row off on a 0.75-scale
           phone. The rings carry no click handler - see the box listener below;
           they keep keyboard access and the "taken" highlight. */
        puzzle.ends.forEach(function (end, idx) {
            var hit = document.createElement('div');
            hit.className = 'cap-hit';
            hit.style.left   = pct(end.x - HIT / 2, puzzle.width);
            hit.style.top    = pct(end.y - HIT / 2, puzzle.height);
            hit.style.width  = pct(HIT, puzzle.width);
            hit.style.height = pct(HIT, puzzle.height);
            hit.setAttribute('role', 'button');
            hit.setAttribute('tabindex', '0');
            hit.addEventListener('keydown', function (e) {
                if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); choose(idx); }
            });
            state.hits.push(hit);
            elCanvas.appendChild(hit);
        });

        elStatus.style.display = 'none';
        elStage.style.display = '';
        advance();
    }

    function choose(idx) {
        if (state.busy) { return; }
        if (state.picks.length >= state.marks.length) { return; }
        if (state.picks.indexOf(idx) !== -1) { return; }
        note('');
        state.picks.push(idx);
        state.hits[idx].className = 'cap-hit taken';
        advance();
    }

    /* ONE listener on the box resolves every tap to the nearest endpoint, measured
       in picture pixels after undoing the CSS scale. A finger is not a cursor: on
       a phone it lands 5-10px from where the eye put it, and a 22px ring at 0.75
       scale misses often enough to feel broken. Nearest-wins also means the
       reachable area of one circle can never overlap another's, however close
       the jitter puts them. Clicks on a ring bubble here and resolve to that same
       ring, so a mouse loses nothing. */
    elCanvas.addEventListener('click', function (e) {
        if (!state.ends.length || state.solved) { return; }

        var box = elCanvas.getBoundingClientRect();
        if (!box.width || !box.height) { return; }

        var x = (e.clientX - box.left) * (state.w / box.width);
        var y = (e.clientY - box.top) * (state.h / box.height);

        var best = -1;
        var bestD = REACH * REACH;

        state.ends.forEach(function (end, idx) {
            var d = (end.x - x) * (end.x - x) + (end.y - y) * (end.y - y);
            if (d <= bestD) { bestD = d; best = idx; }
        });

        if (best !== -1) { choose(best); }
    });

    function advance() {
        var i = state.picks.length;

        if (i >= state.marks.length) {
            elAnswer.value = state.picks.join(',');
            check();
            return;
        }

        elDot.style.background = state.marks[i];
        elStep.textContent = state.marks.length > 1 ? '(' + (i + 1) + '/' + state.marks.length + ')' : '';
    }

    /* The picks go to the server the moment the answer is complete. Only its
       verdict unlocks the form: a right answer comes back with an upgraded token
       that verify() will accept, a wrong one burns the picture and a new one is
       fetched with the verdict shown above it. Anything else is the generic
       failure path. */
    function check() {
        state.busy = true;
        say(MSG_CHECKING, false, true);

        post('https://augestel.com/cap/check', {
            purpose: PURPOSE, token: elToken.value, answer: state.picks.join(',')
        }).then(function (res) {
            if (res.ok && res.body && res.body.token) {
                state.busy = false;
                elToken.value = res.body.token;
                state.solved = true;
                say(MSG_THANKS);
                return;
            }

            var why = res.body && res.body.error;

            if (res.status === 422 && (why === 'wrong' || why === 'expired')) {
                state.busy = false;
                note(why === 'wrong' ? MSG_WRONG : MSG_STALE);
                begin();
                return;
            }

            throw res;
        }).catch(failed);
    }

    function failed(res) {
        state.busy = false;
        say(res && res.status === 419 ? MSG_EXPIRED : MSG_FAIL, true);
    }

    function begin() {
        if (state.busy) { return; }
        state.busy = true;
        state.solved = false;
        state.ends = [];
        elAnswer.value = '';
        say('Preparing...');

        post('https://augestel.com/cap/start', { purpose: PURPOSE })
            .then(function (res) {
                if (!res.ok) { throw res; }

                elToken.value = res.body.token;
                say('Checking your browser...');

                solvePow(res.body.token, res.body.bits, function (pow) {
                    post('https://augestel.com/cap/puzzle', {
                        purpose: PURPOSE, token: elToken.value, pow: pow
                    }).then(function (p) {
                        if (!p.ok) { throw p; }
                        state.busy = false;
                        elToken.value = p.body.token;
                        paint(p.body);
                    }).catch(failed);
                }, function () {
                    state.busy = false;
                    say('Your browser could not complete the check.', true);
                });
            })
            .catch(failed);
    }

    document.getElementById('cap-reload-cap3c4b0f6f').addEventListener('click', begin);

    root.style.display = '';
    begin();

    /* Block submission until a puzzle has been answered. This is convenience only -
       the server verifies independently and a form posted past this check simply
       fails there. */
    var form = root.closest('form');

    if (form) {
        form.addEventListener('submit', function (e) {
            if (!state.solved) {
                e.preventDefault();
                e.stopImmediatePropagation();
                /* keep the picture: the visitor is being asked to finish it, and
                   hiding it here used to leave nothing to finish but the arrow. */
                if (!state.busy) { say('Please complete the check above.', true, true); }
            }
        }, true);
    }
})();

