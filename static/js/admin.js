// ═══════════════════════════════════════════════════════════════
//  OTP IVA SMS - ADMIN DASHBOARD CLIENT JAVASCRIPT
// ═══════════════════════════════════════════════════════════════

let currentPage = 'dashboard';
let currentSmsPage = 1;
let autoAddInterval = null;
let logPollInterval = null;
let statusPollInterval = null;

// ────────────────────────────────────────────
//  UI UTILS & TOASTS
// ────────────────────────────────────────────

function showToast(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    
    let icon = 'info-circle';
    if (type === 'success') icon = 'check-circle';
    if (type === 'error') icon = 'exclamation-circle';
    if (type === 'warning') icon = 'exclamation-triangle';

    toast.innerHTML = `
        <div class="toast-icon"><i class="fas fa-${icon}"></i></div>
        <div class="toast-body">
            <div class="toast-msg">${message}</div>
        </div>
        <button class="toast-close" onclick="this.parentElement.remove()">
            <i class="fas fa-times"></i>
        </button>
    `;

    container.appendChild(toast);

    setTimeout(() => {
        toast.classList.add('hide');
        setTimeout(() => toast.remove(), 400);
    }, 4500);
}

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    const main = document.getElementById('mainContent');
    if (sidebar) sidebar.classList.toggle('collapsed');
    if (main) main.classList.toggle('expanded');
}

function updateClock() {
    const clockEl = document.getElementById('currentTime');
    if (clockEl) {
        const now = new Date();
        clockEl.textContent = now.toLocaleTimeString('id-ID', { hour12: false }) + ' WIB';
    }
}
setInterval(updateClock, 1000);
updateClock();

// ────────────────────────────────────────────
//  PAGE INITIALIZATION
// ────────────────────────────────────────────

function initPage(page) {
    currentPage = page;
    checkGlobalConnection();
    statusPollInterval = setInterval(checkGlobalConnection, 15000);

    if (page === 'dashboard') {
        loadDashboard();
        refreshLogs();
        setInterval(loadDashboard, 8000);
        setInterval(refreshLogs, 6000);
    } else if (page === 'sms-log') {
        loadSmsLog(1);
    } else if (page === 'accounts') {
        loadAccountsList();
    } else if (page === 'augestel-accounts') {
        loadAugestelAccountsList();
    } else if (page === 'auto-add') {
        loadAutoAddAccountsOptions();
        checkAutoAddStatus();
        autoAddInterval = setInterval(checkAutoAddStatus, 3000);
    } else if (page === 'auto-add-augestel') {
        loadAugAddAccountSelect();
        checkAugestelAutoAddStatus();
        if (typeof augAutoAddInterval !== 'undefined' && augAutoAddInterval) clearInterval(augAutoAddInterval);
        augAutoAddInterval = setInterval(checkAugestelAutoAddStatus, 3000);
    } else if (page === 'numbers') {
        initNumbersPage();
    } else if (page === 'numbers-augestel') {
        initAugestelNumbersPage();
    } else if (page === 'bot-control') {
        loadBotControl();
        refreshLogs();
        setInterval(loadBotControl, 5000);
        setInterval(refreshLogs, 4000);
    } else if (page === 'settings') {
        loadSettings();
    }
}

// ────────────────────────────────────────────
//  GLOBAL STATUS
// ────────────────────────────────────────────

async function checkGlobalConnection() {
    try {
        const res = await fetch('/api/dashboard');
        const data = await res.json();
        const indicator = document.getElementById('connectionStatus');
        if (!indicator) return;

        const isOnline = data.stats && (data.stats.bot_running || data.stats.ivasms_connected);
        const dot = indicator.querySelector('.status-dot');
        const span = indicator.querySelector('span');

        if (dot && span) {
            if (data.stats.bot_running) {
                dot.className = 'status-dot online';
                span.textContent = 'Bot Running';
            } else if (data.stats.ivasms_connected) {
                dot.className = 'status-dot online';
                span.textContent = 'IVASMS Ready';
            } else {
                dot.className = 'status-dot offline';
                span.textContent = 'Bot Offline';
            }
        }
    } catch (e) {
        const indicator = document.getElementById('connectionStatus');
        if (indicator) {
            const dot = indicator.querySelector('.status-dot');
            const span = indicator.querySelector('span');
            if (dot && span) {
                dot.className = 'status-dot offline';
                span.textContent = 'Server Offline';
            }
        }
    }
}

// ────────────────────────────────────────────
//  DASHBOARD
// ────────────────────────────────────────────

async function loadDashboard() {
    try {
        const res = await fetch('/api/dashboard');
        const data = await res.json();

        // Stats
        const statOtp = document.getElementById('statOtp');
        const statBot = document.getElementById('statBot');
        const statBotBadge = document.getElementById('statBotBadge');
        const statIvasms = document.getElementById('statIvasms');
        const statIvasmsBadge = document.getElementById('statIvasmsBadge');
        const statErrors = document.getElementById('statErrors');
        const statRevenue = document.getElementById('statRevenue');

        if (statOtp) statOtp.textContent = data.stats.otp_received || 0;
        if (statErrors) statErrors.textContent = data.stats.errors || 0;
        if (statRevenue) {
            const revVal = (data.stats.total_revenue !== undefined) ? data.stats.total_revenue : (data.stats.otp_received * 0.05);
            statRevenue.textContent = `$${parseFloat(revVal).toFixed(2)}`;
        }

        if (statBot) statBot.textContent = data.stats.bot_running ? 'Online' : 'Offline';
        if (statBotBadge) {
            statBotBadge.textContent = data.stats.bot_running ? 'Running' : 'Stopped';
            statBotBadge.className = `stat-badge ${data.stats.bot_running ? 'active' : 'inactive'}`;
        }

        if (statIvasms) statIvasms.textContent = data.stats.ivasms_connected ? 'Connected' : 'Disconnected';
        if (statIvasmsBadge) {
            statIvasmsBadge.textContent = data.stats.ivasms_connected ? 'Session OK' : 'Needs Sync';
            statIvasmsBadge.className = `stat-badge ${data.stats.ivasms_connected ? 'active' : 'inactive'}`;
        }

        const statAug = document.getElementById('statAugestel');
        const statAugBadge = document.getElementById('statAugestelBadge');
        const isAugConnected = (data.stats.augestel_connected !== undefined) ? data.stats.augestel_connected : true;
        if (statAug) statAug.textContent = isAugConnected ? 'Connected' : 'Disconnected';
        if (statAugBadge) {
            statAugBadge.textContent = isAugConnected ? 'Active' : 'Offline';
            statAugBadge.className = `stat-badge ${isAugConnected ? 'active' : 'inactive'}`;
        }

        // Render Country Leaderboard
        const countryBoard = document.getElementById('countryLeaderboard');
        if (countryBoard) {
            const cCounts = data.stats.country_counts || {};
            const cEntries = Object.entries(cCounts).sort((a, b) => b[1] - a[1]).slice(0, 5);
            if (cEntries.length === 0) {
                // Fallback default sample data jika bot baru nyala
                countryBoard.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(255,255,255,0.03); padding:6px 10px; border-radius:6px; font-size:0.85rem;">
                        <span>🇩🇪 Jerman (DE)</span><b style="color:var(--accent);">Active</b>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(255,255,255,0.03); padding:6px 10px; border-radius:6px; font-size:0.85rem;">
                        <span>🇿🇼 Zimbabwe (ZW)</span><b style="color:var(--accent);">Active</b>
                    </div>
                `;
            } else {
                countryBoard.innerHTML = cEntries.map(([cc, count], idx) => `
                    <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(255,255,255,0.03); padding:6px 10px; border-radius:6px; font-size:0.85rem;">
                        <span>#${idx+1} <b>${cc}</b></span>
                        <span style="color:var(--accent); font-weight:700;">${count} OTP</span>
                    </div>
                `).join('');
            }
        }

        // Render Platform Leaderboard
        const platBoard = document.getElementById('platformLeaderboard');
        if (platBoard) {
            const pCounts = data.stats.platform_counts || {};
            const pEntries = Object.entries(pCounts).sort((a, b) => b[1] - a[1]).slice(0, 5);
            if (pEntries.length === 0) {
                platBoard.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(255,255,255,0.03); padding:6px 10px; border-radius:6px; font-size:0.85rem;">
                        <span>🟢 WhatsApp</span><b style="color:#10b981;">Active</b>
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(255,255,255,0.03); padding:6px 10px; border-radius:6px; font-size:0.85rem;">
                        <span>🔵 Telegram</span><b style="color:#3b82f6;">Active</b>
                    </div>
                `;
            } else {
                platBoard.innerHTML = pEntries.map(([plat, count], idx) => `
                    <div style="display:flex; justify-content:space-between; align-items:center; background:rgba(255,255,255,0.03); padding:6px 10px; border-radius:6px; font-size:0.85rem;">
                        <span>#${idx+1} <b>${plat}</b></span>
                        <span style="color:#10b981; font-weight:700;">${count} OTP</span>
                    </div>
                `).join('');
            }
        }

        // Render Busy Hours Chart
        const chartBox = document.getElementById('hourlyChartContainer');
        if (chartBox) {
            const hourly = data.stats.hourly_counts || {};
            const hours = [];
            for (let i = 0; i < 24; i++) {
                const hk = `${String(i).padStart(2, '0')}:00`;
                hours.push({ hour: hk, count: hourly[hk] || 0 });
            }
            const maxVal = Math.max(...hours.map(h => h.count), 1);
            chartBox.innerHTML = hours.map(h => {
                const pct = Math.max((h.count / maxVal) * 100, 10);
                const isPeak = h.count === maxVal && maxVal > 0;
                return `
                    <div style="flex:1; display:flex; flex-direction:column; align-items:center; height:100%; justify-content:flex-end;" title="${h.hour}: ${h.count} OTP">
                        <div style="width:100%; max-width:14px; height:${pct}%; background:${isPeak ? 'linear-gradient(to top, #10b981, #06b6d4)' : 'rgba(255,255,255,0.15)'}; border-radius:3px 3px 0 0; transition:height 0.3s ease;"></div>
                    </div>
                `;
            }).join('');
        }

        // Recent Activity
        const activityList = document.getElementById('recentActivity');
        if (activityList && data.recent_logs) {
            if (data.recent_logs.length === 0) {
                activityList.innerHTML = '<div class="empty-state">No recent activity detected.</div>';
            } else {
                activityList.innerHTML = data.recent_logs.map(item => `
                    <div class="activity-item">
                        <div class="activity-badge badge-${item.type || 'info'}">
                            <i class="fas fa-${item.type === 'otp' ? 'key' : item.type === 'error' ? 'exclamation' : 'info'}"></i>
                        </div>
                        <div class="activity-content">
                            <div class="activity-msg">${escapeHtml(item.message)}</div>
                            <div class="activity-time">${item.timestamp || 'Just now'}</div>
                        </div>
                    </div>
                `).join('');
            }
        }
    } catch (e) {
        console.error('Failed to load dashboard:', e);
    }
}

function refreshDashboard() {
    loadDashboard();
    refreshLogs();
    showToast('Dashboard refreshed', 'info');
}

// ────────────────────────────────────────────
//  LOG TERMINAL
// ────────────────────────────────────────────

async function refreshLogs() {
    try {
        const res = await fetch('/api/logs/tail?n=40');
        const data = await res.json();
        
        const terminals = [
            document.getElementById('logTerminal'),
            document.getElementById('logTerminalBot')
        ];

        terminals.forEach(term => {
            if (!term) return;
            if (!data.lines || data.lines.length === 0) {
                term.innerHTML = '<div class="log-line text-muted">No log output yet...</div>';
                return;
            }

            term.innerHTML = data.lines.map(line => {
                let cls = 'log-line';
                if (line.includes('ERROR') || line.includes('error')) cls += ' log-error';
                else if (line.includes('WARNING') || line.includes('warn')) cls += ' log-warn';
                else if (line.includes('New OTP') || line.includes('Forwarded')) cls += ' log-success';
                return `<div class="${cls}">${escapeHtml(line)}</div>`;
            }).join('');

            const autoScrollCheckbox = document.getElementById('autoScroll');
            if (!autoScrollCheckbox || autoScrollCheckbox.checked) {
                term.scrollTop = term.scrollHeight;
            }
        });
    } catch (e) {
        console.error('Error fetching logs:', e);
    }
}

// ────────────────────────────────────────────
//  SMS LOG
// ────────────────────────────────────────────

let allSmsEntries = [];

async function loadSmsLog(page = 1) {
    currentSmsPage = page;
    const tbody = document.getElementById('smsTableBody');
    if (!tbody) return;

    tbody.innerHTML = '<tr><td colspan="3" class="text-center"><i class="fas fa-circle-notch fa-spin"></i> Loading entries...</td></tr>';

    try {
        const res = await fetch(`/api/sms-log?page=${page}&per_page=20`);
        const data = await res.json();

        allSmsEntries = data.entries || [];
        renderSmsTable(allSmsEntries);
        renderPagination(data.total_pages, data.page);
    } catch (e) {
        tbody.innerHTML = `<tr><td colspan="3" class="text-center text-danger">Gagal memuat log SMS: ${e.message}</td></tr>`;
    }
}

function renderSmsTable(entries) {
    const tbody = document.getElementById('smsTableBody');
    if (!tbody) return;

    if (entries.length === 0) {
        tbody.innerHTML = '<tr><td colspan="3" class="text-center text-muted">Tidak ada SMS tercatat.</td></tr>';
        return;
    }

    tbody.innerHTML = entries.map(item => {
        let typeBadge = `<span class="badge badge-info">${item.type}</span>`;
        if (item.type === 'otp') typeBadge = `<span class="badge badge-success">OTP</span>`;
        if (item.type === 'error') typeBadge = `<span class="badge badge-danger">ERROR</span>`;

        return `
            <tr>
                <td class="mono text-muted">${escapeHtml(item.timestamp || '-')}</td>
                <td>${typeBadge}</td>
                <td class="selectable">${formatSmsMessage(item.message)}</td>
            </tr>
        `;
    }).join('');
}

function formatSmsMessage(msg) {
    const escaped = escapeHtml(msg);
    // Highlight codes if found
    return escaped.replace(/(\b\d{4,8}\b)/g, '<mark class="code-highlight" title="Click to copy" onclick="copyText(\'$1\')">$1</mark>');
}

function filterSmsLog() {
    const query = (document.getElementById('smsSearch')?.value || '').toLowerCase();
    if (!query) {
        renderSmsTable(allSmsEntries);
        return;
    }

    const filtered = allSmsEntries.filter(e => 
        (e.message && e.message.toLowerCase().includes(query)) ||
        (e.timestamp && e.timestamp.toLowerCase().includes(query)) ||
        (e.type && e.type.toLowerCase().includes(query))
    );
    renderSmsTable(filtered);
}

function renderPagination(totalPages, page) {
    const pagContainer = document.getElementById('smsPagination');
    if (!pagContainer) return;

    if (!totalPages || totalPages <= 1) {
        pagContainer.innerHTML = '';
        return;
    }

    let html = '';
    if (page > 1) {
        html += `<button class="page-btn" onclick="loadSmsLog(${page - 1})"><i class="fas fa-chevron-left"></i> Prev</button>`;
    }
    html += `<span class="page-info">Halaman ${page} dari ${totalPages}</span>`;
    if (page < totalPages) {
        html += `<button class="page-btn" onclick="loadSmsLog(${page + 1})">Next <i class="fas fa-chevron-right"></i></button>`;
    }

    pagContainer.innerHTML = html;
}

function copyText(text) {
    navigator.clipboard.writeText(text).then(() => {
        showToast(`Disalin: ${text}`, 'success');
    }).catch(() => {
        showToast('Gagal menyalin', 'error');
    });
}

// ────────────────────────────────────────────
//  AUTO-ADD NUMBERS
// ────────────────────────────────────────────

async function loadAutoAddAccountsOptions() {
    const select = document.getElementById('addAccountSelect');
    if (!select) return;

    try {
        const res = await fetch('/api/accounts');
        const data = await res.json();
        const accounts = data.accounts || [];

        if (accounts.length === 0) {
            select.innerHTML = '<option value="1">Akun #1 (Default)</option>';
            return;
        }

        const currentVal = select.value;
        let html = '';
        if (accounts.length > 1) {
            html += `<option value="all">⚡ SEMUA AKUN SEKALIGUS (Parallel ${accounts.length} Akun)</option>`;
        }
        html += accounts.map((acc, i) => {
            const idx = i + 1;
            return `<option value="${idx}">Akun #${idx} (${escapeHtml(acc.email)})</option>`;
        }).join('');

        select.innerHTML = html;

        if (currentVal) {
            select.value = currentVal;
        }
    } catch (e) {
        console.error('Failed to load accounts for auto-add:', e);
    }
}

async function startAutoAdd() {
    const rangeName = document.getElementById('addRangeName')?.value.trim();
    const maxAdd = parseInt(document.getElementById('addMaxAdd')?.value || '0', 10);
    const delay = parseInt(document.getElementById('addDelay')?.value || '60', 10);
    const rawAccVal = document.getElementById('addAccountSelect')?.value || '1';
    const workers = parseInt(document.getElementById('addWorkers')?.value || '4', 10);

    if (!rangeName) {
        showToast('Harap masukkan Range Name!', 'warning');
        return;
    }

    const btnStart = document.getElementById('btnStartAdd');
    const btnStop = document.getElementById('btnStopAdd');
    if (btnStart) btnStart.disabled = true;

    try {
        const res = await fetch('/api/auto-add/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                account_index: rawAccVal,
                workers: workers,
                range_name: rangeName,
                max_add: maxAdd,
                delay: delay
            })
        });
        const data = await res.json();

        if (data.success) {
            showToast(data.message, 'success');
            if (btnStart) btnStart.style.display = 'none';
            if (btnStop) btnStop.style.display = 'inline-flex';
            checkAutoAddStatus();
        } else {
            showToast(data.message, 'error');
            if (btnStart) btnStart.disabled = false;
        }
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
        if (btnStart) btnStart.disabled = false;
    }
}

async function stopAutoAdd() {
    const btnStop = document.getElementById('btnStopAdd');
    if (btnStop) btnStop.disabled = true;

    try {
        const res = await fetch('/api/auto-add/stop', { method: 'POST' });
        const data = await res.json();
        showToast(data.message, 'info');
        checkAutoAddStatus();
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
    } finally {
        if (btnStop) btnStop.disabled = false;
    }
}

async function checkAutoAddStatus() {
    try {
        const res = await fetch('/api/auto-add/status');
        const state = await res.json();

        const btnStart = document.getElementById('btnStartAdd');
        const btnStop = document.getElementById('btnStopAdd');
        const badge = document.getElementById('autoAddStatus');
        const statAdded = document.getElementById('addStatAdded');
        const statFailed = document.getElementById('addStatFailed');
        const statSkipped = document.getElementById('addStatSkipped');
        const statTotal = document.getElementById('addStatTotal');
        const bar = document.getElementById('addProgressBar');
        const msg = document.getElementById('addLastMessage');
        const accSelect = document.getElementById('addAccountSelect');
        const runningInfo = document.getElementById('addRunningAccountInfo');
        const runningText = document.getElementById('addRunningAccountText');

        if (state.running) {
            if (btnStart) { btnStart.style.display = 'none'; btnStart.disabled = false; }
            if (btnStop) { btnStop.style.display = 'inline-flex'; }
            if (badge) { badge.textContent = 'Running'; badge.className = 'status-badge active'; }
            if (accSelect) { accSelect.disabled = true; }
            if (runningInfo && state.account_email) {
                runningInfo.style.display = 'block';
                if (runningText) {
                    const workerBadge = state.workers ? ` <span class="badge badge-info" style="font-size:0.75rem;"><i class="fas fa-bolt"></i> ${state.workers} Workers</span>` : '';
                    runningText.innerHTML = `Sedang berjalan menggunakan: <b>${escapeHtml(state.account_email)}</b>${workerBadge}`;
                }
            }
        } else {
            if (btnStart) { btnStart.style.display = 'inline-flex'; btnStart.disabled = false; }
            if (btnStop) { btnStop.style.display = 'none'; }
            if (badge) { badge.textContent = 'Idle'; badge.className = 'status-badge'; }
            if (accSelect) { accSelect.disabled = false; }
            if (runningInfo) { runningInfo.style.display = 'none'; }
        }

        if (statAdded) statAdded.textContent = state.added || 0;
        if (statFailed) statFailed.textContent = state.failed || 0;
        if (statSkipped) statSkipped.textContent = state.skipped || 0;
        if (statTotal) statTotal.textContent = state.total_found || 0;

        if (msg && state.last_message) {
            msg.innerHTML = `<i class="fas fa-terminal"></i> ${escapeHtml(state.last_message)}`;
        }

        if (bar) {
            const target = state.max_add > 0 ? state.max_add : state.total_found;
            if (target > 0) {
                const pct = Math.min(100, Math.round(((state.added + state.skipped) / target) * 100));
                bar.style.width = `${pct}%`;
            } else {
                bar.style.width = state.running ? '50%' : '0%';
            }
        }
    } catch (e) {
        console.error('Failed to get auto-add status:', e);
    }
}

// ────────────────────────────────────────────
//  MY NUMBERS & EXPORT (IVASMS PORTAL)
// ────────────────────────────────────────────

let allNumbersList = [];

async function initNumbersPage() {
    await loadNumbersAccountOptions();
    await loadNumbersData(false);
}

async function loadNumbersAccountOptions() {
    const select = document.getElementById('numAccountSelect');
    if (!select) return;

    try {
        const res = await fetch('/api/accounts');
        const data = await res.json();
        const accounts = data.accounts || [];

        if (accounts.length === 0) {
            select.innerHTML = '<option value="1">Akun #1 (Default)</option>';
            return;
        }

        const currentVal = select.value;
        let html = '';
        if (accounts.length > 1) {
            html += `<option value="all">⚡ SEMUA AKUN (Total Gabungan ${accounts.length} Akun)</option>`;
        }
        html += accounts.map((acc, i) => {
            const idx = i + 1;
            return `<option value="${idx}">Akun #${idx} (${escapeHtml(acc.email)})</option>`;
        }).join('');
        select.innerHTML = html;

        if (currentVal && (currentVal === 'all' || accounts[parseInt(currentVal, 10) - 1])) {
            select.value = currentVal;
        }
    } catch (e) {
        console.error('Failed to load accounts for numbers:', e);
    }
}

async function loadNumbersData(forceRefresh = false) {
    const select = document.getElementById('numAccountSelect');
    const accIdx = select ? select.value : '1';
    const isAll = accIdx === 'all';
    const tbody = document.getElementById('numbersTableBody');
    const statTotal = document.getElementById('numStatTotal');
    const statAcc = document.getElementById('numStatAccount');
    const statLast = document.getElementById('numStatLastCheck');
    const summary = document.getElementById('numCountSummary');
    const btnRef = document.getElementById('btnRefreshNumbers');
    const breakdownEl = document.getElementById('numAccountsBreakdown');

    if (btnRef) {
        btnRef.disabled = true;
        btnRef.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Mendeteksi...';
    }

    if (tbody) {
        tbody.innerHTML = `
            <tr>
                <td colspan="${isAll ? 8 : 7}" class="text-center" style="padding: 30px;">
                    <i class="fas fa-circle-notch fa-spin" style="font-size: 1.5rem; color: var(--primary);"></i>
                    <div style="margin-top: 10px; font-weight: 500;">
                        ${isAll ? 'Membuka portal ivasms.com & mendeteksi nomor dari seluruh akun terdaftar...' : (forceRefresh ? 'Membuka portal ivasms.com & mendeteksi nomor realtime...' : 'Memuat data nomor akun...')}
                    </div>
                </td>
            </tr>
        `;
    }

    try {
        const res = await fetch(`/api/numbers?account_index=${accIdx}&refresh=${forceRefresh ? '1' : '0'}`);
        const data = await res.json();

        if (!data.success) {
            showToast(data.message || 'Gagal mengambil nomor dari portal', 'error');
            if (tbody) {
                tbody.innerHTML = `<tr><td colspan="${isAll ? 8 : 7}" class="text-center text-danger" style="padding: 24px;"><i class="fas fa-exclamation-triangle"></i> ${escapeHtml(data.message || 'Gagal memuat nomor')}</td></tr>`;
            }
            if (statTotal) statTotal.textContent = '0';
            if (breakdownEl) breakdownEl.style.display = 'none';
            return;
        }

        allNumbersList = data.numbers || [];
        const total = data.total || allNumbersList.length;

        if (statTotal) statTotal.textContent = total.toLocaleString('id-ID');
        if (statAcc) {
            statAcc.textContent = isAll ? `Semua Akun (${(data.accounts_breakdown || []).length} Akun)` : `Akun #${data.account_index} (${data.email})`;
        }
        if (statLast) statLast.textContent = data.cached_at || 'Baru saja';
        if (summary) summary.innerHTML = `Menampilkan <b>${allNumbersList.length}</b> dari total <b>${total}</b> nomor${isAll ? ' (Semua Akun)' : ''}`;

        // Render breakdown cards jika memilih semua akun
        if (breakdownEl) {
            if (isAll && data.accounts_breakdown && data.accounts_breakdown.length > 0) {
                breakdownEl.style.display = 'grid';
                breakdownEl.innerHTML = data.accounts_breakdown.map(b => `
                    <div class="account-breakdown-card">
                        <span class="account-breakdown-badge"><i class="fas fa-user-circle"></i> Akun #${b.account_index}</span>
                        <span class="account-breakdown-email" title="${escapeHtml(b.email)}">${escapeHtml(b.email)}</span>
                        <span class="account-breakdown-count">${(b.total || 0).toLocaleString('id-ID')} nomor</span>
                    </div>
                `).join('');
            } else {
                breakdownEl.style.display = 'none';
                breakdownEl.innerHTML = '';
            }
        }

        renderNumbersTable(allNumbersList, isAll);
        if (forceRefresh) {
            showToast(`Berhasil mendeteksi total ${total} nomor!`, 'success');
        }
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
        if (tbody) {
            tbody.innerHTML = `<tr><td colspan="${isAll ? 8 : 7}" class="text-center text-danger" style="padding: 24px;">Error: ${escapeHtml(e.message)}</td></tr>`;
        }
    } finally {
        if (btnRef) {
            btnRef.disabled = false;
            btnRef.innerHTML = '<i class="fas fa-sync-alt"></i> Deteksi Ulang';
        }
    }
}

function renderNumbersTable(list, isAll = false) {
    const tbody = document.getElementById('numbersTableBody');
    const thAcc = document.getElementById('thAccountCol');
    if (thAcc) thAcc.style.display = isAll ? '' : 'none';

    if (!tbody) return;

    if (!list || list.length === 0) {
        tbody.innerHTML = `<tr><td colspan="${isAll ? 8 : 7}" class="text-center text-muted" style="padding: 24px;">Tidak ada nomor yang ditemukan.</td></tr>`;
        return;
    }

    tbody.innerHTML = list.map((item, idx) => {
        const accCol = isAll ? `<td style="text-align: center;"><span class="badge badge-secondary" style="font-size:0.75rem;" title="${escapeHtml(item.account_email || '')}"><i class="fas fa-user"></i> #${item.account_index || 1}</span></td>` : '';
        return `
            <tr>
                <td class="text-muted mono" style="font-size: 0.82rem; text-align: center;">${idx + 1}</td>
                ${accCol}
                <td class="selectable mono" style="font-weight: 600; color: var(--cyan);" title="Klik untuk salin" onclick="copyText('${escapeHtml(item.number)}')">
                    <i class="fas fa-phone-alt" style="font-size: 0.72rem; opacity: 0.65; margin-right: 6px;"></i>
                    <span>${escapeHtml(item.number)}</span>
                </td>
                <td><span class="badge badge-info" style="font-weight: 500;">${escapeHtml(item.range || '-')}</span></td>
                <td class="mono">${escapeHtml(item.rate || '-')}</td>
                <td class="mono">${escapeHtml(item.limit_range || '-')}</td>
                <td class="mono">${escapeHtml(item.sid_limit || '-')}</td>
                <td class="mono">${escapeHtml(item.sid_did_limit || '-')}</td>
            </tr>
        `;
    }).join('');
}

function filterNumbersTable() {
    const query = (document.getElementById('numSearchInput')?.value || '').toLowerCase().trim();
    const summary = document.getElementById('numCountSummary');
    const select = document.getElementById('numAccountSelect');
    const isAll = select && select.value === 'all';

    if (!query) {
        renderNumbersTable(allNumbersList, isAll);
        if (summary) summary.innerHTML = `Menampilkan <b>${allNumbersList.length}</b> nomor`;
        return;
    }

    const filtered = allNumbersList.filter(item => {
        return (item.number && item.number.toLowerCase().includes(query)) ||
               (item.range && item.range.toLowerCase().includes(query)) ||
               (item.account_email && item.account_email.toLowerCase().includes(query)) ||
               (item.id && item.id.includes(query));
    });

    renderNumbersTable(filtered, isAll);
    if (summary) summary.innerHTML = `Ditemukan <b>${filtered.length}</b> hasil dari <b>${allNumbersList.length}</b> nomor`;
}

function downloadNumbersExport(format) {
    const select = document.getElementById('numAccountSelect');
    const accIdx = select ? select.value : '1';
    const isAll = accIdx === 'all';

    if (allNumbersList.length === 0) {
        showToast('Tidak ada data nomor untuk diexport. Lakukan deteksi terlebih dahulu!', 'warning');
        return;
    }

    const label = isAll ? 'TOTAL (Semua Akun)' : (accIdx === 'augestel' ? 'Augestel Portal' : `Akun #${accIdx}`);
    showToast(`Menyiapkan export ${format.toUpperCase()} ${label}...`, 'info');
    const downloadUrl = `/api/numbers/export/${format}?account_index=${accIdx}`;
    window.location.href = downloadUrl;
}

async function deleteAllNumbersCurrentAccount() {
    const select = document.getElementById('numAccountSelect');
    const accIdx = select ? select.value : '1';

    let accLabel = `Akun #${accIdx}`;
    if (accIdx === 'all') accLabel = 'SEMUA AKUN IVASMS';
    else if (accIdx === 'augestel') accLabel = 'Akun AUGESTEL';

    const confirmMsg = `PERINGATAN: Apakah Anda yakin ingin MENGHAPUS / MENGEMBALIKAN SEMUA NOMOR untuk ${accLabel}?\n\nSemua nomor yang terikat pada akun ini akan dihapus/dilepas dari portal.`;
    if (!confirm(confirmMsg)) return;

    const btn = document.getElementById('btnDeleteAllNumbers');
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Menghapus...';
    }

    try {
        const res = await fetch('/api/numbers/delete-all', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ account_index: accIdx })
        });
        const data = await res.json();
        if (data.success) {
            showToast(data.message || 'Semua nomor berhasil dihapus / dikembalikan!', 'success');
            await loadNumbersData(true);
        } else {
            showToast(data.message || 'Gagal menghapus nomor!', 'error');
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-trash-alt"></i> Delete All Numbers';
        }
    }
}


// ────────────────────────────────────────────
//  MY NUMBERS & EXPORT (AUGESTEL PORTAL)
// ────────────────────────────────────────────

let allAugestelNumbersList = [];

async function initAugestelNumbersPage() {
    await loadAugestelNumbersAccountOptions();
    await loadAugestelNumbersData(false);
}

async function loadAugestelNumbersAccountOptions() {
    const select = document.getElementById('augNumAccountSelect');
    if (!select) return;

    try {
        const res = await fetch('/api/augestel/accounts');
        const data = await res.json();
        const accounts = data.accounts || [];

        if (accounts.length === 0) {
            select.innerHTML = '<option value="augestel_1">Akun #1 (Default)</option>';
            return;
        }

        const currentVal = select.value;
        let html = '';
        if (accounts.length > 1) {
            html += `<option value="augestel_all">⚡ SEMUA AKUN AUGESTEL (Total Gabungan ${accounts.length} Akun)</option>`;
        }
        html += accounts.map((acc, i) => {
            const idx = i + 1;
            return `<option value="augestel_${idx}">Akun #${idx} (${escapeHtml(acc.email)})</option>`;
        }).join('');

        select.innerHTML = html;

        if (currentVal && (currentVal === 'augestel_all' || html.includes(`value="${currentVal}"`))) {
            select.value = currentVal;
        }
    } catch (e) {
        console.error('Failed to load Augestel accounts for numbers:', e);
    }
}

async function loadAugestelNumbersData(forceRefresh = false) {
    const select = document.getElementById('augNumAccountSelect');
    const accIdx = select ? select.value : 'augestel_all';
    const isAll = accIdx === 'augestel_all';
    const tbody = document.getElementById('augNumbersTableBody');
    const statTotal = document.getElementById('augNumStatTotal');
    const statAcc = document.getElementById('augNumStatAccount');
    const statLast = document.getElementById('augNumStatLastCheck');
    const summary = document.getElementById('augNumCountSummary');
    const btnRef = document.getElementById('btnRefreshAugNumbers');
    const breakdownEl = document.getElementById('augNumAccountsBreakdown');

    if (btnRef) {
        btnRef.disabled = true;
        btnRef.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Mendeteksi...';
    }

    if (tbody) {
        tbody.innerHTML = `
            <tr>
                <td colspan="${isAll ? 7 : 6}" class="text-center" style="padding: 30px;">
                    <i class="fas fa-circle-notch fa-spin" style="font-size: 1.5rem; color: #8b5cf6;"></i>
                    <div style="margin-top: 10px; font-weight: 500;">
                        ${isAll ? 'Memuat dan mendeteksi nomor dari seluruh akun Augestel terdaftar...' : (forceRefresh ? 'Menghubungkan ke API Augestel dan mendeteksi nomor realtime...' : 'Memuat data nomor akun Augestel...')}
                    </div>
                </td>
            </tr>
        `;
    }

    try {
        const res = await fetch(`/api/numbers?account_index=${accIdx}&refresh=${forceRefresh ? '1' : '0'}`);
        const data = await res.json();

        if (!data.success) {
            showToast(data.message || 'Gagal mengambil nomor dari portal Augestel', 'error');
            if (tbody) {
                tbody.innerHTML = `<tr><td colspan="${isAll ? 7 : 6}" class="text-center text-danger" style="padding: 24px;"><i class="fas fa-exclamation-triangle"></i> ${escapeHtml(data.message || 'Gagal memuat nomor')}</td></tr>`;
            }
            if (statTotal) statTotal.textContent = '0';
            if (breakdownEl) breakdownEl.style.display = 'none';
            return;
        }

        allAugestelNumbersList = data.numbers || [];
        const total = data.total || allAugestelNumbersList.length;

        if (statTotal) statTotal.textContent = total.toLocaleString('id-ID');
        if (statAcc) {
            statAcc.textContent = isAll ? `Semua Akun Augestel (${(data.accounts_breakdown || []).length} Akun)` : (data.email || 'Augestel Portal');
        }
        if (statLast) statLast.textContent = data.cached_at || 'Baru saja';
        if (summary) summary.innerHTML = `Menampilkan <b>${allAugestelNumbersList.length}</b> dari total <b>${total}</b> nomor${isAll ? ' (Semua Akun Augestel)' : ''}`;

        // Render breakdown cards jika memilih semua akun
        if (breakdownEl) {
            if (isAll && data.accounts_breakdown && data.accounts_breakdown.length > 0) {
                breakdownEl.style.display = 'grid';
                breakdownEl.innerHTML = data.accounts_breakdown.map(b => `
                    <div class="account-breakdown-card" style="border-left: 3px solid #8b5cf6;">
                        <span class="account-breakdown-badge" style="background: rgba(139, 92, 246, 0.2); color: #c4b5fd;"><i class="fas fa-satellite-dish"></i> Akun #${b.account_index}</span>
                        <span class="account-breakdown-email" title="${escapeHtml(b.email)}">${escapeHtml(b.email)}</span>
                        <span class="account-breakdown-count" style="color: #a78bfa;">${(b.total || 0).toLocaleString('id-ID')} nomor</span>
                    </div>
                `).join('');
            } else {
                breakdownEl.style.display = 'none';
                breakdownEl.innerHTML = '';
            }
        }

        renderAugestelNumbersTable(allAugestelNumbersList, isAll);
        if (forceRefresh) {
            showToast(`Berhasil mendeteksi total ${total} nomor Augestel!`, 'success');
        }
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
        if (tbody) {
            tbody.innerHTML = `<tr><td colspan="${isAll ? 7 : 6}" class="text-center text-danger" style="padding: 24px;">Error: ${escapeHtml(e.message)}</td></tr>`;
        }
    } finally {
        if (btnRef) {
            btnRef.disabled = false;
            btnRef.innerHTML = '<i class="fas fa-sync-alt"></i> Deteksi Ulang';
        }
    }
}

function renderAugestelNumbersTable(list, isAll = false) {
    const tbody = document.getElementById('augNumbersTableBody');
    const thAcc = document.getElementById('thAugAccountCol');
    if (thAcc) thAcc.style.display = isAll ? '' : 'none';

    if (!tbody) return;

    if (!list || list.length === 0) {
        tbody.innerHTML = `<tr><td colspan="${isAll ? 7 : 6}" class="text-center text-muted" style="padding: 24px;">Tidak ada nomor Augestel yang ditemukan.</td></tr>`;
        return;
    }

    tbody.innerHTML = list.map((item, idx) => {
        const accCol = isAll ? `<td style="text-align: center;"><span class="badge" style="background: rgba(139, 92, 246, 0.2); color: #c4b5fd; font-size:0.75rem;" title="${escapeHtml(item.account_email || '')}"><i class="fas fa-user"></i> ${item.account_index ? item.account_index.replace('aug_', '#') : '#1'}</span></td>` : '';
        return `
            <tr>
                <td class="text-muted mono" style="font-size: 0.82rem; text-align: center;">${idx + 1}</td>
                ${accCol}
                <td class="selectable mono" style="font-weight: 600; color: #a78bfa;" title="Klik untuk salin" onclick="copyText('${escapeHtml(item.number)}')">
                    <i class="fas fa-phone-alt" style="font-size: 0.72rem; opacity: 0.65; margin-right: 6px;"></i>
                    <span>${escapeHtml(item.number)}</span>
                </td>
                <td><span class="badge" style="background: rgba(56, 189, 248, 0.15); color: #38bdf8; font-weight: 500;">${escapeHtml(item.range || 'Augestel')}</span></td>
                <td class="mono" style="color: #10b981;">${escapeHtml(item.rate || '$0.00')}</td>
                <td class="mono">${escapeHtml(item.limit_range || '10000')}</td>
                <td><span class="badge badge-success" style="font-size: 0.75rem;">Active / Augestel</span></td>
            </tr>
        `;
    }).join('');
}

function filterAugestelNumbersTable() {
    const query = (document.getElementById('augNumSearchInput')?.value || '').toLowerCase().trim();
    const summary = document.getElementById('augNumCountSummary');
    const select = document.getElementById('augNumAccountSelect');
    const isAll = select && select.value === 'augestel_all';

    if (!query) {
        renderAugestelNumbersTable(allAugestelNumbersList, isAll);
        if (summary) summary.innerHTML = `Menampilkan <b>${allAugestelNumbersList.length}</b> nomor`;
        return;
    }

    const filtered = allAugestelNumbersList.filter(item => {
        return (item.number && item.number.toLowerCase().includes(query)) ||
               (item.range && item.range.toLowerCase().includes(query)) ||
               (item.account_email && item.account_email.toLowerCase().includes(query)) ||
               (item.id && item.id.includes(query));
    });

    renderAugestelNumbersTable(filtered, isAll);
    if (summary) summary.innerHTML = `Ditemukan <b>${filtered.length}</b> hasil dari <b>${allAugestelNumbersList.length}</b> nomor`;
}

function downloadAugestelNumbersExport(format) {
    const select = document.getElementById('augNumAccountSelect');
    const accIdx = select ? select.value : 'augestel_all';
    const isAll = accIdx === 'augestel_all';

    if (allAugestelNumbersList.length === 0) {
        showToast('Tidak ada data nomor Augestel untuk diexport. Lakukan deteksi terlebih dahulu!', 'warning');
        return;
    }

    const label = isAll ? 'SEMUA AKUN AUGESTEL' : `Akun Augestel (${accIdx.replace('aug_', '#')})`;
    showToast(`Menyiapkan export ${format.toUpperCase()} ${label}...`, 'info');
    const downloadUrl = `/api/numbers/export/${format}?account_index=${accIdx}`;
    window.location.href = downloadUrl;
}

async function deleteAllAugestelNumbers() {
    const select = document.getElementById('augNumAccountSelect');
    const accIdx = select ? select.value : 'augestel_all';

    const confirmMsg = `Apakah Anda yakin ingin MEMBERSIHKAN & MERESET CACHE NOMOR AUGESTEL?\n\nData nomor akan di-refresh langsung dari API Augestel saat deteksi ulang.`;
    if (!confirm(confirmMsg)) return;

    const btn = document.getElementById('btnDeleteAllAugNumbers');
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Mereset...';
    }

    try {
        const res = await fetch('/api/numbers/delete-all', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ account_index: accIdx })
        });
        const data = await res.json();
        if (data.success) {
            showToast(data.message || 'Cache nomor Augestel berhasil direset!', 'success');
            await loadAugestelNumbersData(true);
        } else {
            showToast(data.message || 'Gagal reset cache nomor!', 'error');
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-trash-alt"></i> Reset Cache Nomor';
        }
    }
}


// ────────────────────────────────────────────
//  BOT CONTROL
// ────────────────────────────────────────────

async function loadBotControl() {
    try {
        const res = await fetch('/api/bot/status');
        const status = await res.json();

        const icon = document.getElementById('botIcon');
        const text = document.getElementById('botStatusText');
        const desc = document.getElementById('botStatusDesc');
        const btnStart = document.getElementById('btnStartBot');
        const btnStop = document.getElementById('btnStopBot');

        if (status.running) {
            if (icon) icon.className = 'bot-icon online';
            if (text) text.textContent = 'Bot Sedang Berjalan';
            if (desc) desc.textContent = `PID: ${status.pid} • Aktif sejak ${status.started_at || 'sekarang'}`;
            if (btnStart) btnStart.disabled = true;
            if (btnStop) btnStop.disabled = false;
        } else {
            if (icon) icon.className = 'bot-icon offline';
            if (text) text.textContent = 'Bot Berhenti';
            if (desc) desc.textContent = 'Proses bot.py tidak sedang berjalan.';
            if (btnStart) btnStart.disabled = false;
            if (btnStop) btnStop.disabled = true;
        }

        // Render status akun IVASMS dari backend bot status / api accounts
        await renderBotControlAccountsStatus(status.accounts_status || null);
    } catch (e) {
        console.error('Error fetching bot status:', e);
    }
}

async function renderBotControlAccountsStatus(customResults = null) {
    const listContainer = document.getElementById('ivasmsAccountsStatusList');
    if (!listContainer) return;

    try {
        let accounts = [];
        if (customResults && Array.isArray(customResults) && customResults.length > 0) {
            accounts = customResults;
        } else {
            const res = await fetch('/api/accounts');
            const data = await res.json();
            accounts = (data.accounts || []).map((a, i) => ({
                index: i + 1,
                email: a.email,
                connected: a.connected !== undefined ? a.connected : true,
                last_check: a.last_check || 'Status Terpantau (Aktif)'
            }));
        }

        const countBadge = document.getElementById('ivasmsAccCountBadge');
        if (countBadge) {
            countBadge.textContent = `${accounts.length} Akun Terdaftar`;
        }

        if (accounts.length === 0) {
            listContainer.innerHTML = `
                <div class="text-muted" style="font-size: 0.85rem; padding: 14px; text-align: center; background: rgba(255,255,255,0.02); border-radius: 8px;">
                    Belum ada akun IVASMS terdaftar. <a href="/accounts" style="color: var(--primary); text-decoration: underline;">Kelola Akun</a> untuk menambahkan akun.
                </div>
            `;
            return;
        }

        listContainer.innerHTML = accounts.map(acc => {
            const isConn = !!acc.connected;
            const statusDot = isConn 
                ? '<div class="status-dot online" style="margin: 0; box-shadow: 0 0 8px rgba(16,185,129,0.6);"></div>' 
                : '<div class="status-dot offline" style="margin: 0; box-shadow: 0 0 8px rgba(239,68,68,0.6);"></div>';
            const badge = isConn 
                ? '<span class="badge badge-success" style="font-size: 0.72rem; padding: 4px 8px;"><i class="fas fa-check-circle"></i> Connected</span>' 
                : '<span class="badge badge-danger" style="font-size: 0.72rem; padding: 4px 8px;"><i class="fas fa-times-circle"></i> Disconnected</span>';

            return `
                <div id="accStatusCard_${acc.index}" style="background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; display: flex; align-items: center; justify-content: space-between; gap: 10px; transition: all 0.2s ease;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        ${statusDot}
                        <div>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <b style="font-size: 0.92rem; color: var(--text);">Akun #${acc.index}</b>
                                <span class="text-muted" style="font-size: 0.8rem; font-family: monospace;">(${escapeHtml(acc.email)})</span>
                            </div>
                            <div class="text-muted" style="font-size: 0.74rem; margin-top: 3px;" id="accCheckTime_${acc.index}">
                                <i class="far fa-clock"></i> ${acc.last_check ? 'Pengecekan: ' + acc.last_check : 'Status terpantau aktif'}
                            </div>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span id="accBadge_${acc.index}">${badge}</span>
                        <button class="btn-sm" style="padding: 4px 10px; font-size: 0.75rem;" onclick="checkIvasmsSingle(${acc.index})" id="btnCheckAcc_${acc.index}" title="Cek koneksi akun #${acc.index}">
                            <i class="fas fa-sync-alt"></i> Cek
                        </button>
                    </div>
                </div>
            `;
        }).join('');
    } catch (e) {
        listContainer.innerHTML = `<div class="text-danger" style="font-size: 0.8rem;">Gagal memuat status: ${e.message}</div>`;
    }
}

async function startBot() {
    const btn = document.getElementById('btnStartBot');
    if (btn) btn.disabled = true;

    try {
        const res = await fetch('/api/bot/start', { method: 'POST' });
        const data = await res.json();
        if (data.success) {
            showToast(data.message, 'success');
        } else {
            showToast(data.message, 'error');
        }
        loadBotControl();
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
        if (btn) btn.disabled = false;
    }
}

async function stopBot() {
    const btn = document.getElementById('btnStopBot');
    if (btn) btn.disabled = true;

    try {
        const res = await fetch('/api/bot/stop', { method: 'POST' });
        const data = await res.json();
        if (data.success) {
            showToast(data.message, 'success');
        } else {
            showToast(data.message, 'error');
        }
        loadBotControl();
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
        if (btn) btn.disabled = false;
    }
}

async function checkIvasmsSingle(index) {
    const btn = document.getElementById(`btnCheckAcc_${index}`);
    const originalHtml = btn ? btn.innerHTML : '';
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i>';
    }

    try {
        const res = await fetch('/api/ivasms/check', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ index: index })
        });
        const data = await res.json();
        if (data.success && data.status) {
            const accList = data.status.accounts || [];
            await renderBotControlAccountsStatus(accList);
            const thisAcc = accList.find(a => a.index === index);
            if (thisAcc && thisAcc.connected) {
                showToast(`Akun #${index} berhasil terhubung!`, 'success');
            } else {
                showToast(`Akun #${index} terputus / cookie expired!`, 'error');
            }
        } else {
            showToast(`Gagal cek akun #${index}: ${data.message || 'Error'}`, 'error');
        }
    } catch (e) {
        showToast(`Gagal cek akun #${index}: ${e.message}`, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = originalHtml;
        }
    }
}

async function checkIvasms() {
    const text = document.getElementById('ivasmsStatusText');
    const desc = document.getElementById('ivasmsStatusDesc');
    const icon = document.getElementById('ivasmsIcon');
    const btn = document.getElementById('btnCheckIvasms');

    if (text) text.textContent = 'Memeriksa Semua Akun...';
    if (desc) desc.textContent = 'Memvalidasi sesi login & cookies per akun...';
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Memeriksa...';
    }

    try {
        const res = await fetch('/api/ivasms/check', { method: 'POST' });
        const data = await res.json();

        if (data.success && data.status) {
            const accList = data.status.accounts || [];
            const allConn = accList.length > 0 && accList.every(a => a.connected);
            const anyConn = accList.some(a => a.connected);

            if (icon) icon.className = anyConn ? 'bot-icon online' : 'bot-icon offline';
            if (text) text.textContent = allConn ? 'Semua Akun Terhubung' : anyConn ? 'Sebagian Akun Terhubung' : 'Semua Akun Terputus';
            if (desc) desc.textContent = `Pengecekan selesai pada ${data.status.last_check}`;

            await renderBotControlAccountsStatus(accList);
            showToast(allConn ? 'Semua akun IVASMS berhasil terhubung!' : anyConn ? 'Sebagian akun terhubung.' : 'Semua akun terputus!', anyConn ? 'success' : 'warning');
        } else {
            showToast('Gagal memverifikasi status akun!', 'error');
        }
    } catch (e) {
        showToast(`Gagal cek IVASMS: ${e.message}`, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-sync-alt"></i> Cek Koneksi';
        }
    }
}

// ────────────────────────────────────────────
//  SETTINGS
// ────────────────────────────────────────────

async function loadSettings() {
    try {
        const res = await fetch('/api/config');
        const cfg = await res.json();

        if (document.getElementById('cfgBotToken')) document.getElementById('cfgBotToken').value = cfg.BOT_TOKEN || '';
        if (document.getElementById('cfgGroupChatId')) document.getElementById('cfgGroupChatId').value = cfg.GROUP_CHAT_ID || '';
        if (document.getElementById('cfgGroupLink')) document.getElementById('cfgGroupLink').value = cfg.GROUP_LINK || '';
        if (document.getElementById('cfgBotName')) document.getElementById('cfgBotName').value = cfg.BOT_NAME || '';
        if (document.getElementById('cfgPollInterval')) document.getElementById('cfgPollInterval').value = cfg.POLL_INTERVAL || '10';
        if (document.getElementById('cfgEmail')) document.getElementById('cfgEmail').value = cfg.IVASMS_EMAIL || '';
        if (document.getElementById('cfgPassword')) document.getElementById('cfgPassword').value = cfg.IVASMS_PASSWORD || '';
        if (document.getElementById('cfgEmail2')) document.getElementById('cfgEmail2').value = cfg.IVASMS_EMAIL_2 || '';
        if (document.getElementById('cfgPassword2')) document.getElementById('cfgPassword2').value = cfg.IVASMS_PASSWORD_2 || '';
        
        // File & Channel Links
        const fileLink = cfg.FILE_LINK || cfg.NUMBER_LINK || '';
        const channelLink = cfg.CHANNEL_LINK || cfg.GROUP_LINK || '';
        const sensorText = cfg.SENSOR_TEXT || '••••';

        if (document.getElementById('cfgFileLink')) document.getElementById('cfgFileLink').value = fileLink;
        if (document.getElementById('cfgChannelLink')) document.getElementById('cfgChannelLink').value = channelLink;
        if (document.getElementById('cfgSensorText')) document.getElementById('cfgSensorText').value = sensorText;
        if (document.getElementById('cfgNumberLink')) document.getElementById('cfgNumberLink').value = fileLink;
        if (document.getElementById('cfgOwnerLink')) document.getElementById('cfgOwnerLink').value = cfg.OWNER_LINK || '';
    } catch (e) {
        showToast('Gagal memuat konfigurasi: ' + e.message, 'error');
    }
}

async function saveSettings() {
    const fileLink = document.getElementById('cfgFileLink')?.value.trim() || document.getElementById('cfgNumberLink')?.value.trim();
    const channelLink = document.getElementById('cfgChannelLink')?.value.trim() || document.getElementById('cfgGroupLink')?.value.trim();
    const sensorText = document.getElementById('cfgSensorText')?.value.trim() || '••••';

    const payload = {
        BOT_TOKEN: document.getElementById('cfgBotToken')?.value.trim(),
        GROUP_CHAT_ID: document.getElementById('cfgGroupChatId')?.value.trim(),
        GROUP_LINK: channelLink,
        CHANNEL_LINK: channelLink,
        BOT_NAME: document.getElementById('cfgBotName')?.value.trim(),
        POLL_INTERVAL: parseInt(document.getElementById('cfgPollInterval')?.value || '10', 10),
        FILE_LINK: fileLink,
        NUMBER_LINK: fileLink,
        SENSOR_TEXT: sensorText,
        OWNER_LINK: document.getElementById('cfgOwnerLink')?.value.trim(),
    };

    if (document.getElementById('cfgEmail')) {
        payload.IVASMS_EMAIL = document.getElementById('cfgEmail').value.trim();
    }
    if (document.getElementById('cfgPassword')) {
        payload.IVASMS_PASSWORD = document.getElementById('cfgPassword').value.trim();
    }
    if (document.getElementById('cfgEmail2')) {
        payload.IVASMS_EMAIL_2 = document.getElementById('cfgEmail2').value.trim();
    }
    if (document.getElementById('cfgPassword2')) {
        payload.IVASMS_PASSWORD_2 = document.getElementById('cfgPassword2').value.trim();
    }

    try {
        const res = await fetch('/api/config', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();

        if (data.success) {
            showToast(data.message, 'success');
        } else {
            showToast(data.message, 'error');
        }
    } catch (e) {
        showToast('Gagal menyimpan: ' + e.message, 'error');
    }
}

function copyText(text) {
    if (!text) return;
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => {
            showToast(`Disalin: ${text}`, 'success');
        }).catch(() => {
            fallbackCopy(text);
        });
    } else {
        fallbackCopy(text);
    }
}

function fallbackCopy(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast(`Disalin: ${text}`, 'success');
}

function togglePasswordVisibility() {
    const input = document.getElementById('cfgPassword');
    const icon = document.getElementById('pwdToggleIcon');
    if (!input || !icon) return;

    if (input.type === 'password') {
        input.type = 'text';
        icon.className = 'fas fa-eye-slash';
    } else {
        input.type = 'password';
        icon.className = 'fas fa-eye';
    }
}

function togglePasswordVisibility2() {
    const input = document.getElementById('cfgPassword2');
    const icon = document.getElementById('pwdToggleIcon2');
    if (!input || !icon) return;

    if (input.type === 'password') {
        input.type = 'text';
        icon.className = 'fas fa-eye-slash';
    } else {
        input.type = 'password';
        icon.className = 'fas fa-eye';
    }
}

// ────────────────────────────────────────────
//  MENU KELOLA AKUN IVASMS (SEPARATE PAGE)
// ────────────────────────────────────────────

let currentAccounts = [];

async function loadAccountsList() {
    const container = document.getElementById('accountsListContainer');
    if (!container) return;

    try {
        const res = await fetch('/api/accounts');
        const data = await res.json();
        currentAccounts = data.accounts || [];

        if (currentAccounts.length === 0) {
            container.innerHTML = `
                <div class="text-muted" style="text-align: center; padding: 25px; border: 1px dashed var(--border); border-radius: 12px;">
                    <i class="fas fa-users-slash" style="font-size: 2rem; margin-bottom: 8px; opacity: 0.5;"></i>
                    <p>Belum ada akun IVASMS terdaftar. Silakan tambahkan akun pertama Anda.</p>
                </div>
            `;
            return;
        }

        container.innerHTML = currentAccounts.map((acc, idx) => {
            const email = escapeHtml(acc.email || '');
            const isFirst = idx === 0;
            const badgeLabel = isFirst ? 'Akun Utama' : `Akun ${idx + 1}`;
            const gradient = isFirst 
                ? 'linear-gradient(135deg, #3b82f6, #1d4ed8)' 
                : 'linear-gradient(135deg, #10b981, #059669)';

            return `
                <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 14px; padding: 18px; display: flex; align-items: center; justify-content: space-between; gap: 12px;">
                    <div style="display: flex; align-items: center; gap: 14px;">
                        <div style="width: 44px; height: 44px; border-radius: 12px; background: ${gradient}; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; color: #fff;">
                            <i class="fas fa-user-check"></i>
                        </div>
                        <div>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <b style="font-size: 1rem; color: var(--text);">Akun #${idx + 1}</b>
                                <span class="badge ${isFirst ? 'badge-info' : 'badge-success'}" style="font-size: 0.72rem;">
                                    ${badgeLabel}
                                </span>
                            </div>
                            <div class="text-muted" style="font-size: 0.85rem; margin-top: 4px;">
                                <i class="fas fa-envelope"></i> ${email}
                            </div>
                        </div>
                    </div>
                    <div style="display: flex; gap: 6px;">
                        <button class="btn btn-secondary btn-sm" onclick="editAccountSlot(${idx})" title="Edit Akun">
                            <i class="fas fa-edit"></i> Edit
                        </button>
                        <button class="btn btn-danger btn-sm" onclick="deleteAccountSlot(${idx})" title="Hapus Akun">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </div>
            `;
        }).join('');
    } catch (e) {
        container.innerHTML = `<div class="text-danger" style="padding: 10px;">Gagal memuat akun: ${e.message}</div>`;
    }
}

function editAccountSlot(index) {
    if (index >= 0 && index < currentAccounts.length) {
        const acc = currentAccounts[index];
        document.getElementById('accEditIndex').value = String(index);
        document.getElementById('accInputEmail').value = acc.email || '';
        document.getElementById('accInputPassword').value = acc.password || '';

        const title = document.getElementById('accFormModeTitle');
        if (title) {
            title.innerHTML = `<i class="fas fa-edit"></i> Edit Akun #${index + 1} (${escapeHtml(acc.email)})`;
        }
        const btnSave = document.getElementById('btnSaveAcc');
        if (btnSave) {
            btnSave.innerHTML = `<i class="fas fa-save"></i> Perbarui Akun #${index + 1}`;
        }
        const btnCancel = document.getElementById('btnCancelEdit');
        if (btnCancel) {
            btnCancel.style.display = 'inline-block';
        }
        document.getElementById('accInputEmail')?.focus();
    }
}

function resetAccForm() {
    document.getElementById('accEditIndex').value = '';
    document.getElementById('accInputEmail').value = '';
    document.getElementById('accInputPassword').value = '';

    const title = document.getElementById('accFormModeTitle');
    if (title) {
        title.innerHTML = `<i class="fas fa-plus-circle"></i> Tambah Akun Baru`;
    }
    const btnSave = document.getElementById('btnSaveAcc');
    if (btnSave) {
        btnSave.innerHTML = `<i class="fas fa-plus"></i> Simpan Akun`;
    }
    const btnCancel = document.getElementById('btnCancelEdit');
    if (btnCancel) {
        btnCancel.style.display = 'none';
    }
}

function toggleAccPasswordVisibility() {
    const input = document.getElementById('accInputPassword');
    const icon = document.getElementById('accPwdIcon');
    if (!input || !icon) return;

    if (input.type === 'password') {
        input.type = 'text';
        icon.className = 'fas fa-eye-slash';
    } else {
        input.type = 'password';
        icon.className = 'fas fa-eye';
    }
}

async function saveAccountFromMenu() {
    const editIdxVal = document.getElementById('accEditIndex')?.value;
    const email = document.getElementById('accInputEmail')?.value.trim();
    const password = document.getElementById('accInputPassword')?.value.trim();

    if (!email || !password) {
        showToast('Email dan Password akun wajib diisi!', 'warning');
        return;
    }

    const payload = {
        email: email,
        password: password
    };
    if (editIdxVal !== '' && !isNaN(parseInt(editIdxVal))) {
        payload.index = parseInt(editIdxVal, 10);
    }

    try {
        const res = await fetch('/api/accounts', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        if (data.success) {
            showToast(data.message || 'Akun berhasil disimpan!', 'success');
            resetAccForm();
            await loadAccountsList();
        } else {
            showToast(data.message || 'Gagal menyimpan akun', 'error');
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    }
}

async function deleteAccountSlot(index) {
    if (!confirm(`Apakah Anda yakin ingin menghapus Akun #${index + 1}?`)) return;

    try {
        const res = await fetch('/api/accounts/delete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ index: index })
        });
        const data = await res.json();
        if (data.success) {
            showToast('Akun berhasil dihapus!', 'success');
            resetAccForm();
            await loadAccountsList();
        } else {
            showToast(data.message || 'Gagal menghapus akun', 'error');
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    }
}

async function submitBulkAccounts() {
    const textarea = document.getElementById('accBulkInput');
    const btn = document.getElementById('btnSubmitBulk');
    const hint = document.getElementById('bulkImportHint');
    const rawText = textarea ? textarea.value.trim() : '';

    if (!rawText) {
        showToast('Teks akun bulk tidak boleh kosong!', 'warning');
        return;
    }

    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Mengimpor...';
    }

    try {
        const res = await fetch('/api/accounts/bulk-import', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: rawText })
        });
        const data = await res.json();

        if (data.success) {
            showToast(data.message, 'success');
            if (textarea) textarea.value = '';
            if (hint) hint.innerHTML = `<span class="text-success"><i class="fas fa-check-circle"></i> Berhasil import ${data.imported} akun baru (${data.total} total akun).</span>`;
            await loadAccountsList();
            if (typeof loadAutoAddAccountsOptions === 'function') {
                await loadAutoAddAccountsOptions();
            }
        } else {
            showToast(data.message || 'Gagal import akun bulk', 'error');
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-upload"></i> Proses Import Massal';
        }
    }
}

// ────────────────────────────────────────────
//  AUGESTEL ACCOUNT & CONNECTION CONTROLLER
// ────────────────────────────────────────────

let currentAugestelAccounts = [];

async function checkAugestelConnection() {
    const card = document.getElementById('augConnectionCard');
    const dot = document.getElementById('augStatusDot');
    const badge = document.getElementById('augBadge');
    const desc = document.getElementById('augStatusDesc');
    const btn = document.getElementById('btnCheckAugestel');

    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Cek...';
    }

    try {
        const res = await fetch('/api/augestel/check', { method: 'POST' });
        const data = await res.json();

        if (data.success && data.status && data.status.connected) {
            if (dot) dot.className = 'status-dot online';
            if (badge) {
                badge.className = 'badge badge-success';
                badge.innerHTML = '<i class="fas fa-check-circle"></i> Connected';
            }
            if (desc) {
                desc.innerHTML = `<i class="fas fa-check"></i> API Aktif • Saldo: $${data.status.balance || 0} • ${data.status.total_numbers || 0} Nomor`;
            }
            showToast(`Augestel Connected! Saldo: $${data.status.balance || 0}, ${data.status.total_numbers || 0} Nomor terdeteksi.`, 'success');
        } else {
            if (dot) dot.className = 'status-dot offline';
            if (badge) {
                badge.className = 'badge badge-danger';
                badge.innerHTML = '<i class="fas fa-times-circle"></i> Error';
            }
            if (desc) desc.textContent = data.message || 'Koneksi API Augestel gagal';
            showToast(`Gagal koneksi Augestel: ${data.message || 'Unknown error'}`, 'error');
        }
    } catch (e) {
        showToast('Error cek Augestel: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-satellite-dish"></i> Cek Augestel';
        }
    }
}

async function loadAugestelAccountsList() {
    const container = document.getElementById('augAccountsListContainer');
    if (!container) return;

    try {
        const res = await fetch('/api/augestel/accounts');
        const data = await res.json();
        currentAugestelAccounts = data.accounts || [];

        if (currentAugestelAccounts.length === 0) {
            container.innerHTML = `
                <div class="text-muted" style="text-align: center; padding: 25px; border: 1px dashed var(--border); border-radius: 12px;">
                    <i class="fas fa-satellite-dish" style="font-size: 2rem; margin-bottom: 8px; opacity: 0.5;"></i>
                    <p>Belum ada akun Augestel terdaftar. Silakan tambahkan akun pertama Anda.</p>
                </div>
            `;
            return;
        }

        container.innerHTML = currentAugestelAccounts.map((acc, idx) => {
            const email = escapeHtml(acc.email || '');
            const apiKey = acc.api_key || '';
            const maskedKey = apiKey ? (apiKey.length > 12 
                ? `${apiKey.substring(0, 8)}••••••••${apiKey.substring(apiKey.length - 4)}` 
                : apiKey) : 'Login Portal Aktif (Key belum di-generate)';
            const isFirst = idx === 0;

            return `
                <div style="background: rgba(255,255,255,0.03); border: 1px solid var(--border); border-radius: 14px; padding: 18px; display: flex; align-items: center; justify-content: space-between; gap: 12px;">
                    <div style="display: flex; align-items: center; gap: 14px;">
                        <div style="width: 44px; height: 44px; border-radius: 12px; background: linear-gradient(135deg, #8b5cf6, #6d28d9); display: flex; align-items: center; justify-content: center; font-size: 1.1rem; color: #fff;">
                            <i class="fas fa-satellite-dish"></i>
                        </div>
                        <div>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <b style="font-size: 1rem; color: var(--text);">Akun Augestel #${idx + 1}</b>
                                <span class="badge ${isFirst ? 'badge-info' : 'badge-success'}" style="font-size: 0.72rem;">
                                    ${isFirst ? 'Default / Utama' : `Akun #${idx + 1}`}
                                </span>
                            </div>
                            <div class="text-muted" style="font-size: 0.85rem; margin-top: 4px;">
                                <i class="fas fa-envelope"></i> ${email}
                            </div>
                            <div class="text-muted mono" style="font-size: 0.76rem; margin-top: 2px; color: var(--accent-light);">
                                <i class="fas fa-key"></i> Key: ${escapeHtml(maskedKey)}
                            </div>
                        </div>
                    </div>
                    <div style="display: flex; gap: 6px;">
                        <button class="btn btn-secondary btn-sm" onclick="editAugestelAccount(${idx})" title="Edit Akun">
                            <i class="fas fa-edit"></i> Edit
                        </button>
                        <button class="btn btn-danger btn-sm" onclick="deleteAugestelAccount(${idx})" title="Hapus Akun">
                            <i class="fas fa-trash"></i>
                        </button>
                    </div>
                </div>
            `;
        }).join('');
    } catch (e) {
        container.innerHTML = `<div class="text-danger" style="padding: 10px;">Gagal memuat akun: ${e.message}</div>`;
    }
}

function editAugestelAccount(index) {
    if (index >= 0 && index < currentAugestelAccounts.length) {
        const acc = currentAugestelAccounts[index];
        const editIdx = document.getElementById('augAccEditIndex');
        const emailEl = document.getElementById('augAccInputEmail');
        const keyEl = document.getElementById('augAccInputApiKey');
        const passEl = document.getElementById('augAccInputPassword');
        const title = document.getElementById('augAccFormModeTitle');
        const btnSave = document.getElementById('btnSaveAugAcc');
        const btnCancel = document.getElementById('btnCancelAugEdit');

        if (editIdx) editIdx.value = String(index);
        if (emailEl) emailEl.value = acc.email || '';
        if (keyEl) keyEl.value = acc.api_key || '';
        if (passEl) passEl.value = acc.password || '';

        if (title) title.innerHTML = `<i class="fas fa-edit"></i> Edit Akun Augestel #${index + 1} (${escapeHtml(acc.email)})`;
        if (btnSave) btnSave.innerHTML = `<i class="fas fa-save"></i> Perbarui Akun #${index + 1}`;
        if (btnCancel) btnCancel.style.display = 'inline-block';

        emailEl?.focus();
    }
}

function resetAugAccForm() {
    const editIdx = document.getElementById('augAccEditIndex');
    const emailEl = document.getElementById('augAccInputEmail');
    const keyEl = document.getElementById('augAccInputApiKey');
    const passEl = document.getElementById('augAccInputPassword');
    const title = document.getElementById('augAccFormModeTitle');
    const btnSave = document.getElementById('btnSaveAugAcc');
    const btnCancel = document.getElementById('btnCancelAugEdit');

    if (editIdx) editIdx.value = '';
    if (emailEl) emailEl.value = '';
    if (keyEl) keyEl.value = '';
    if (passEl) passEl.value = '';

    if (title) title.innerHTML = `<i class="fas fa-satellite-dish" style="color: #a78bfa;"></i> Tambah Akun Augestel`;
    if (btnSave) btnSave.innerHTML = `<i class="fas fa-save"></i> Simpan Akun Augestel`;
    if (btnCancel) btnCancel.style.display = 'none';
}

function toggleAugPasswordVisibility() {
    const input = document.getElementById('augAccInputPassword');
    const icon = document.getElementById('augAccPwdIcon');
    if (!input || !icon) return;

    if (input.type === 'password') {
        input.type = 'text';
        icon.className = 'fas fa-eye-slash';
    } else {
        input.type = 'password';
        icon.className = 'fas fa-eye';
    }
}

async function autoDetectAugestelKey() {
    const email = document.getElementById('augAccInputEmail')?.value.trim();
    const password = document.getElementById('augAccInputPassword')?.value.trim();
    const btn = document.getElementById('btnAutoDetectKey');
    const keyInput = document.getElementById('augAccInputApiKey');

    if (!email || !password) {
        showToast('Masukkan Email dan Password akun Augestel terlebih dahulu!', 'warning');
        return;
    }

    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Login...';
    }

    showToast('Menghubungkan ke portal Augestel (Switchfy)...', 'info');

    try {
        const res = await fetch('/api/augestel/accounts', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email: email, password: password, api_key: '' })
        });
        const data = await res.json();
        if (data.success && data.api_key) {
            if (keyInput) keyInput.value = data.api_key;
            showToast(data.message || 'Berhasil login! API Key terdeteksi otomatis.', 'success');
            await loadAugestelAccountsList();
        } else {
            showToast(data.message || 'Gagal mendeteksi API Key. Periksa email & password!', 'error');
        }
    } catch (e) {
        showToast('Error login: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-bolt" style="color: var(--accent);"></i> Cek Login';
        }
    }
}

async function saveAugestelAccount() {
    const editIdxVal = document.getElementById('augAccEditIndex')?.value;
    const email = document.getElementById('augAccInputEmail')?.value.trim();
    const apiKey = document.getElementById('augAccInputApiKey')?.value.trim();
    const password = document.getElementById('augAccInputPassword')?.value.trim();
    const btnSave = document.getElementById('btnSaveAugAcc');

    if (!email) {
        showToast('Email akun Augestel wajib diisi!', 'warning');
        return;
    }
    if (!password && !apiKey) {
        showToast('Password portal Augestel wajib diisi untuk login otomatis!', 'warning');
        return;
    }

    if (btnSave) {
        btnSave.disabled = true;
        btnSave.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Memproses Login...';
    }

    const payload = {
        email: email,
        api_key: apiKey,
        password: password
    };
    if (editIdxVal !== '' && !isNaN(parseInt(editIdxVal))) {
        payload.index = parseInt(editIdxVal, 10);
    }

    try {
        const res = await fetch('/api/augestel/accounts', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        if (data.success) {
            showToast(data.message || 'Akun Augestel berhasil disimpan!', 'success');
            resetAugAccForm();
            await loadAugestelAccountsList();
        } else {
            showToast(data.message || 'Gagal menyimpan akun Augestel', 'error');
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    } finally {
        if (btnSave) {
            btnSave.disabled = false;
            btnSave.innerHTML = '<i class="fas fa-save"></i> Login & Simpan Akun';
        }
    }
}


async function deleteAugestelAccount(index) {
    if (!confirm(`Apakah Anda yakin ingin menghapus Akun Augestel #${index + 1}?`)) return;

    try {
        const res = await fetch('/api/augestel/accounts/delete', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ index: index })
        });
        const data = await res.json();
        if (data.success) {
            showToast('Akun Augestel berhasil dihapus!', 'success');
            resetAugAccForm();
            await loadAugestelAccountsList();
        } else {
            showToast(data.message || 'Gagal menghapus akun', 'error');
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    }
}

async function runBatchLoginAugestel() {
    const btn = document.getElementById('btnBatchLoginAug');
    const originalText = btn ? btn.innerHTML : '';
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Login Berjalan...';
    }
    showToast('Memulai proses login & warmup untuk semua akun Augestel di background...', 'info');
    try {
        const res = await fetch('/api/augestel/batch-login', { method: 'POST' });
        const data = await res.json();
        if (data.success) {
            showToast(data.message || 'Proses batch login & warmup telah dimulai!', 'success');
            setTimeout(loadAugestelAccountsList, 3000);
        } else {
            showToast(data.message || 'Gagal memulai batch login', 'error');
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = originalText || '<i class="fas fa-bolt"></i> Login & Warmup Semua Akun';
        }
    }
}

// ────────────────────────────────────────────
//  AUTO-ADD AUGESTEL (SEPARATE NAVIGATION)
// ────────────────────────────────────────────

let augAutoAddInterval = null;

async function loadAugAddAccountSelect() {
    const select = document.getElementById('augAddAccountSelect');
    if (!select) return;

    try {
        const res = await fetch('/api/augestel/accounts');
        const data = await res.json();
        const accounts = data.accounts || [];

        if (accounts.length === 0) {
            select.innerHTML = '<option value="">Belum ada akun Augestel (Tambahkan di Akun Augestel)</option>';
            return;
        }

        const currentVal = select.value;
        let html = '';
        if (accounts.length > 1) {
            html += `<option value="all">⚡ SEMUA AKUN SEKALIGUS (Parallel ${accounts.length} Akun)</option>`;
        }
        html += accounts.map((acc, i) => {
            return `<option value="${i + 1}">Akun #${i + 1} (${escapeHtml(acc.email)})</option>`;
        }).join('');

        select.innerHTML = html;
        if (currentVal) select.value = currentVal;
    } catch (e) {
        console.error('Failed to load Augestel accounts for auto-add:', e);
    }
}

async function startAugestelAutoAdd() {
    const rangeName = (document.getElementById('augAddRangeName')?.value || '').trim();
    const maxAdd = parseInt(document.getElementById('augAddMaxAdd')?.value || '0', 10);
    const delay = parseInt(document.getElementById('augAddDelay')?.value || '15', 10);
    const rawAccVal = document.getElementById('augAddAccountSelect')?.value || '1';
    const workers = parseInt(document.getElementById('augAddWorkers')?.value || '2', 10);

    const btnStart = document.getElementById('btnStartAugAdd');
    const btnStop = document.getElementById('btnStopAugAdd');
    if (btnStart) btnStart.disabled = true;

    try {
        const res = await fetch('/api/augestel/auto-add/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                account_index: rawAccVal,
                workers: workers,
                range_name: rangeName,
                max_add: maxAdd,
                delay: delay
            })
        });
        const data = await res.json();

        if (data.success) {
            showToast(data.message, 'success');
            if (btnStart) btnStart.style.display = 'none';
            if (btnStop) btnStop.style.display = 'inline-flex';
            checkAugestelAutoAddStatus();
        } else {
            showToast(data.message, 'error');
            if (btnStart) btnStart.disabled = false;
        }
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
        if (btnStart) btnStart.disabled = false;
    }
}

async function stopAugestelAutoAdd() {
    const btnStop = document.getElementById('btnStopAugAdd');
    if (btnStop) btnStop.disabled = true;

    try {
        const res = await fetch('/api/augestel/auto-add/stop', { method: 'POST' });
        const data = await res.json();
        showToast(data.message, 'info');
        checkAugestelAutoAddStatus();
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
    } finally {
        if (btnStop) btnStop.disabled = false;
    }
}

async function checkAugestelAutoAddStatus() {
    try {
        const res = await fetch('/api/augestel/auto-add/status');
        const state = await res.json();

        const btnStart = document.getElementById('btnStartAugAdd');
        const btnStop = document.getElementById('btnStopAugAdd');
        const badge = document.getElementById('augAutoAddStatus');
        const statAdded = document.getElementById('augStatAdded');
        const statFailed = document.getElementById('augStatFailed');
        const statSkipped = document.getElementById('augStatSkipped');
        const statTotal = document.getElementById('augStatTotal');
        const bar = document.getElementById('augProgressBar');
        const msg = document.getElementById('augLastMessage');
        const accSelect = document.getElementById('augAddAccountSelect');
        const runningInfo = document.getElementById('augAddRunningAccountInfo');
        const runningText = document.getElementById('augAddRunningAccountText');

        if (state.running) {
            if (btnStart) { btnStart.style.display = 'none'; btnStart.disabled = false; }
            if (btnStop) { btnStop.style.display = 'inline-flex'; }
            if (badge) { badge.textContent = 'Running'; badge.className = 'status-badge active'; }
            if (accSelect) { accSelect.disabled = true; }
            if (runningInfo && state.account_email) {
                runningInfo.style.display = 'block';
                if (runningText) {
                    const workerBadge = state.workers ? ` <span class="badge badge-info" style="font-size:0.75rem;"><i class="fas fa-bolt"></i> ${state.workers} Workers</span>` : '';
                    runningText.innerHTML = `Sedang berjalan menggunakan: <b>${escapeHtml(state.account_email)}</b>${workerBadge}`;
                }
            }
        } else {
            if (btnStart) { btnStart.style.display = 'inline-flex'; btnStart.disabled = false; }
            if (btnStop) { btnStop.style.display = 'none'; }
            if (badge) { badge.textContent = 'Idle'; badge.className = 'status-badge'; }
            if (accSelect) { accSelect.disabled = false; }
            if (runningInfo) { runningInfo.style.display = 'none'; }
        }

        if (statAdded) statAdded.textContent = state.added || 0;
        if (statFailed) statFailed.textContent = state.failed || 0;
        if (statSkipped) statSkipped.textContent = state.skipped || 0;
        if (statTotal) statTotal.textContent = state.total_found || 0;

        if (msg && state.last_message) {
            msg.innerHTML = `<i class="fas fa-terminal"></i> ${escapeHtml(state.last_message)}`;
        }

        if (bar) {
            const target = state.max_add > 0 ? state.max_add : state.total_found;
            if (target > 0) {
                const pct = Math.min(100, Math.round(((state.added + state.skipped) / target) * 100));
                bar.style.width = `${pct}%`;
            } else {
                bar.style.width = state.running ? '50%' : '0%';
            }
        }
    } catch (e) {
        console.error('Failed to get Augestel auto-add status:', e);
    }
}


// ────────────────────────────────────────────
//  HELPERS
// ────────────────────────────────────────────

function escapeHtml(str) {
    if (!str) return '';
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
}

// ────────────────────────────────────────────
//  TEST OTP FEATURES
// ────────────────────────────────────────────

async function sendQuickTestOtp() {
    const btn = document.getElementById('btnQuickTest');
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Mengirim...';
    }

    try {
        const payload = {
            country_code: "ZW",
            flag: "🇿🇼",
            platform: "WhatsApp",
            phone: "263788124006",
            otp: String(Math.floor(100000 + Math.random() * 900000)),
        };

        const res = await fetch('/api/test-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();

        if (data.success) {
            showToast(data.message, 'success');
            // Update preview di halaman jika ada
            updateLivePreview(payload);
            // Refresh logs
            setTimeout(refreshLogs, 1000);
        } else {
            showToast(data.message, 'error');
        }
    } catch (e) {
        showToast(`Gagal mengirim: ${e.message}`, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-paper-plane"></i> Kirim Test OTP Cepat';
        }
    }
}

function openCustomTestModal() {
    const modal = document.getElementById('customTestModal');
    if (modal) {
        randomizeOtp();
        modal.style.display = 'flex';
    }
}

function closeCustomTestModal() {
    const modal = document.getElementById('customTestModal');
    if (modal) modal.style.display = 'none';
}

function updateCountryFlag() {
    const val = document.getElementById('testCountry')?.value || 'ZW|🇿🇼';
    const [cc, flag] = val.split('|');
    const phoneInput = document.getElementById('testPhone');
    if (phoneInput) {
        if (cc === 'ZW') phoneInput.value = '263788124006';
        else if (cc === 'DE') phoneInput.value = '491521990635';
        else if (cc === 'ID') phoneInput.value = '6281234567890';
        else if (cc === 'US') phoneInput.value = '14155552671';
        else if (cc === 'RU') phoneInput.value = '79991234567';
        else if (cc === 'ML') phoneInput.value = '22378901234';
        else if (cc === 'FR') phoneInput.value = '33612345678';
    }
}

function randomizeOtp() {
    const otpInput = document.getElementById('testOtp');
    if (otpInput) {
        otpInput.value = String(Math.floor(100000 + Math.random() * 900000));
    }
}

async function submitCustomTestOtp() {
    const btn = document.getElementById('btnSubmitTest');
    const countryVal = document.getElementById('testCountry')?.value || 'ZW|🇿🇼';
    const [country_code, flag] = countryVal.split('|');
    const platform = document.getElementById('testPlatform')?.value || 'WhatsApp';
    const phone = document.getElementById('testPhone')?.value.trim() || '263788124006';
    const otp = document.getElementById('testOtp')?.value.trim() || '884762';

    if (!phone) {
        showToast('Nomor HP wajib diisi!', 'warning');
        return;
    }
    if (!otp) {
        showToast('Kode OTP wajib diisi!', 'warning');
        return;
    }

    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Mengirim...';
    }

    try {
        const payload = { country_code, flag, platform, phone, otp };
        const res = await fetch('/api/test-otp', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();

        if (data.success) {
            showToast(data.message, 'success');
            updateLivePreview(payload);
            closeCustomTestModal();
            setTimeout(refreshLogs, 1000);
        } else {
            showToast(data.message, 'error');
        }
    } catch (e) {
        showToast(`Gagal: ${e.message}`, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-paper-plane"></i> Kirim ke Telegram Sekarang';
        }
    }
}

function updateLivePreview(data) {
    if (document.getElementById('prevFlag')) document.getElementById('prevFlag').textContent = data.flag || '🇿🇼';
    if (document.getElementById('prevCC')) document.getElementById('prevCC').textContent = data.country_code || 'ZW';
    
    // Mask phone & prefix
    const digits = (data.phone || '').replace(/\D/g, '');
    const prefix = digits.substring(0, 6);
    if (document.getElementById('prevPrefix')) document.getElementById('prevPrefix').textContent = prefix;
    
    if (document.getElementById('prevPhone')) {
        if (digits.length >= 8) {
            document.getElementById('prevPhone').textContent = `${digits.substring(0, 4)} •••• ${digits.substring(digits.length - 4)}`;
        } else {
            document.getElementById('prevPhone').textContent = digits;
        }
    }

    // OTP
    const otp = data.otp || '884762';
    const dispOtp = (otp.length === 6 && /^\d+$/.test(otp)) ? `${otp.substring(0, 3)}-${otp.substring(3)}` : otp;
    if (document.getElementById('prevOtp')) {
        document.getElementById('prevOtp').textContent = `🔑 ${dispOtp}`;
    }
}
