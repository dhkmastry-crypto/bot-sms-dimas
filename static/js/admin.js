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

function toggleSidebar(forceState) {
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('sidebarOverlay');
    const isMobile = window.innerWidth <= 992;

    if (isMobile) {
        if (typeof forceState === 'boolean') {
            if (forceState) {
                sidebar && sidebar.classList.add('mobile-open');
                overlay && overlay.classList.add('active');
                document.body.classList.add('drawer-open');
            } else {
                sidebar && sidebar.classList.remove('mobile-open');
                overlay && overlay.classList.remove('active');
                document.body.classList.remove('drawer-open');
            }
        } else {
            const isOpen = sidebar ? sidebar.classList.toggle('mobile-open') : false;
            if (isOpen) {
                overlay && overlay.classList.add('active');
                document.body.classList.add('drawer-open');
            } else {
                overlay && overlay.classList.remove('active');
                document.body.classList.remove('drawer-open');
            }
        }
    } else {
        const main = document.getElementById('mainContent');
        if (sidebar) sidebar.classList.toggle('collapsed');
        if (main) main.classList.toggle('expanded');
    }
}

// Auto close mobile drawer on nav clicks or resize
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.sidebar-nav .nav-item').forEach(item => {
        item.addEventListener('click', () => {
            if (window.innerWidth <= 992) {
                toggleSidebar(false);
            }
        });
    });
    window.addEventListener('resize', () => {
        if (window.innerWidth > 992) {
            toggleSidebar(false);
        }
    });
});

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
        loadEarningsAnalytics();
        refreshLogs();
        setInterval(loadDashboard, 8000);
        setInterval(loadEarningsAnalytics, 8000);
        setInterval(refreshLogs, 6000);
    } else if (page === 'sms-log') {
        loadSmsLog(1);
    } else if (page === 'accounts' || page === 'augestel-accounts' || page === 'accounts-augestel') {
        loadAugestelAccountsList();
    } else if (page === 'auto-add' || page === 'auto-add-augestel') {
        loadAugAddAccountSelect();
        checkAugestelAutoAddStatus();
        if (typeof augAutoAddInterval !== 'undefined' && augAutoAddInterval) clearInterval(augAutoAddInterval);
        augAutoAddInterval = setInterval(checkAugestelAutoAddStatus, 3000);
    } else if (page === 'numbers' || page === 'numbers-augestel') {
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

        const isOnline = data.stats && (data.stats.bot_running || data.stats.augestel_connected);
        const dot = indicator.querySelector('.status-dot');
        const span = indicator.querySelector('span');

        if (dot && span) {
            if (data.stats.bot_running) {
                dot.className = 'status-dot online';
                span.textContent = 'Bot Running';
            } else if (data.stats.augestel_connected) {
                dot.className = 'status-dot online';
                span.textContent = 'Augestel Ready';
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

let augestelAccountsList = [];
let selectedAugAccounts = new Set();

function isAllAugAccountsSelected() {
    return augestelAccountsList.length > 0 && selectedAugAccounts.size === augestelAccountsList.length;
}

function getSelectedAugAccountParam() {
    if (selectedAugAccounts.size === 0 || isAllAugAccountsSelected()) {
        return 'augestel_all';
    }
    if (selectedAugAccounts.size === 1) {
        return `augestel_${Array.from(selectedAugAccounts)[0]}`;
    }
    const sorted = Array.from(selectedAugAccounts).map(Number).sort((a, b) => a - b);
    return sorted.map(i => `aug_${i}`).join(',');
}

async function loadAugestelNumbersAccountOptions() {
    try {
        const res = await fetch('/api/augestel/accounts');
        const data = await res.json();
        augestelAccountsList = data.accounts || [];

        if (augestelAccountsList.length === 0) {
            augestelAccountsList = [{ email: 'Akun #1 (Default)' }];
        }

        // Initialize with all accounts by default if empty
        if (selectedAugAccounts.size === 0) {
            augestelAccountsList.forEach((_, i) => selectedAugAccounts.add(i + 1));
        }

        renderAugAccountCheckboxList();
        updateAugAccountSelectorUI();
    } catch (e) {
        console.error('Failed to load Augestel accounts for numbers:', e);
    }
}

function renderAugAccountCheckboxList() {
    const listEl = document.getElementById('augAccCheckboxList');
    if (!listEl) return;

    if (augestelAccountsList.length === 0) {
        listEl.innerHTML = '<div style="padding: 10px; color: #94a3b8; font-size: 0.8rem; text-align: center;">Tidak ada akun terdaftar</div>';
        return;
    }

    listEl.innerHTML = augestelAccountsList.map((acc, i) => {
        const idx = i + 1;
        const isChecked = selectedAugAccounts.has(idx);
        return `
            <label class="aug-acc-item" id="augAccItem_${idx}" data-email="${escapeHtml(acc.email).toLowerCase()}" data-idx="${idx}">
                <input type="checkbox" value="${idx}" ${isChecked ? 'checked' : ''} onchange="onAugAccountCheckboxToggle(${idx}, this.checked)">
                <span class="aug-acc-tag">#${idx}</span>
                <span class="aug-acc-email" title="${escapeHtml(acc.email)}">${escapeHtml(acc.email)}</span>
            </label>
        `;
    }).join('');
}

function onAugAccountCheckboxToggle(idx, isChecked) {
    idx = Number(idx);
    if (isChecked) {
        selectedAugAccounts.add(idx);
    } else {
        if (selectedAugAccounts.size <= 1) {
            showToast('Minimal 1 akun Augestel harus dipilih!', 'warning');
            const cb = document.querySelector(`#augAccItem_${idx} input[type="checkbox"]`);
            if (cb) cb.checked = true;
            return;
        }
        selectedAugAccounts.delete(idx);
    }
    updateAugAccountSelectorUI();
}

function selectAugAllAccounts(selectAll) {
    if (selectAll) {
        augestelAccountsList.forEach((_, i) => selectedAugAccounts.add(i + 1));
    } else {
        selectedAugAccounts.clear();
        selectedAugAccounts.add(1);
        showToast('Menyisakan Akun #1 saja (minimal 1 akun)', 'info');
    }
    renderAugAccountCheckboxList();
    updateAugAccountSelectorUI();
}

function toggleAugAccountDropdown(e) {
    if (e) e.stopPropagation();
    const dropdown = document.getElementById('augAccMultiDropdown');
    const chev = document.getElementById('augAccMultiChevron');
    if (!dropdown) return;

    if (dropdown.style.display === 'none' || !dropdown.style.display) {
        dropdown.style.display = 'block';
        if (chev) chev.style.transform = 'rotate(180deg)';
        const searchInput = document.getElementById('augAccSearchInput');
        if (searchInput) {
            searchInput.value = '';
            filterAugAccountOptions();
            setTimeout(() => searchInput.focus(), 50);
        }
    } else {
        dropdown.style.display = 'none';
        if (chev) chev.style.transform = 'rotate(0deg)';
    }
}

function applyAugAccountSelection() {
    if (selectedAugAccounts.size === 0) {
        showToast('Pilih minimal 1 akun Augestel!', 'warning');
        return;
    }
    const dropdown = document.getElementById('augAccMultiDropdown');
    const chev = document.getElementById('augAccMultiChevron');
    if (dropdown) dropdown.style.display = 'none';
    if (chev) chev.style.transform = 'rotate(0deg)';

    updateAugAccountSelectorUI();
    loadAugestelNumbersData(false);
}

function toggleAugAccountCardSelection(idx) {
    idx = Number(idx);
    if (selectedAugAccounts.has(idx)) {
        if (selectedAugAccounts.size <= 1) {
            showToast('Minimal 1 akun harus aktif!', 'warning');
            return;
        }
        selectedAugAccounts.delete(idx);
        showToast(`Akun #${idx} dikecualikan dari filter`, 'info');
    } else {
        selectedAugAccounts.add(idx);
        showToast(`Akun #${idx} ditambahkan ke filter`, 'success');
    }
    renderAugAccountCheckboxList();
    updateAugAccountSelectorUI();
    loadAugestelNumbersData(false);
}

function filterAugAccountOptions() {
    const q = (document.getElementById('augAccSearchInput')?.value || '').toLowerCase().trim();
    document.querySelectorAll('.aug-acc-item').forEach(item => {
        const email = item.getAttribute('data-email') || '';
        const idx = item.getAttribute('data-idx') || '';
        if (!q || email.includes(q) || idx.includes(q) || `akun #${idx}`.includes(q)) {
            item.style.display = 'flex';
        } else {
            item.style.display = 'none';
        }
    });
}

function updateAugAccountSelectorUI() {
    const hiddenInput = document.getElementById('augNumAccountSelect');
    const param = getSelectedAugAccountParam();
    if (hiddenInput) hiddenInput.value = param;

    const labelSpan = document.getElementById('augAccMultiLabel');
    const badgeSpan = document.getElementById('augAccMultiBadge');
    const countText = document.getElementById('augAccSelectedCountText');

    const totalAccounts = augestelAccountsList.length;
    const selCount = selectedAugAccounts.size;

    if (labelSpan && badgeSpan) {
        if (selCount === totalAccounts || totalAccounts === 0) {
            labelSpan.innerHTML = `<i class="fas fa-bolt" style="color: #a78bfa;"></i> <span>Semua Akun Augestel (${totalAccounts} Akun)</span>`;
            badgeSpan.textContent = 'Semua';
            badgeSpan.style.background = 'rgba(139, 92, 246, 0.25)';
            badgeSpan.style.color = '#c4b5fd';
        } else if (selCount === 1) {
            const singleIdx = Array.from(selectedAugAccounts)[0];
            const acc = augestelAccountsList[singleIdx - 1];
            const em = acc ? acc.email : `Akun #${singleIdx}`;
            labelSpan.innerHTML = `<i class="fas fa-user-check" style="color: #38bdf8;"></i> <span>Akun #${singleIdx} (${escapeHtml(em)})</span>`;
            badgeSpan.textContent = `1 Akun`;
            badgeSpan.style.background = 'rgba(56, 189, 248, 0.2)';
            badgeSpan.style.color = '#7dd3fc';
        } else {
            const sorted = Array.from(selectedAugAccounts).map(Number).sort((a,b)=>a-b);
            labelSpan.innerHTML = `<i class="fas fa-users-cog" style="color: #34d399;"></i> <span>${selCount} Akun Terpilih (#${sorted.join(', #')})</span>`;
            badgeSpan.textContent = `${selCount} Akun`;
            badgeSpan.style.background = 'rgba(16, 185, 129, 0.2)';
            badgeSpan.style.color = '#6ee7b7';
        }
    }

    if (countText) {
        countText.textContent = `${selCount} dari ${totalAccounts} akun terpilih`;
    }

    // Update breakdown cards visual active/inactive state if cards exist
    document.querySelectorAll('.account-breakdown-card.aug-acc-card-interactive').forEach(card => {
        const cIdx = Number(card.getAttribute('data-account-index'));
        const isSel = selectedAugAccounts.has(cIdx);
        if (isSel) {
            card.classList.remove('unselected');
            card.classList.add('selected');
            const badge = card.querySelector('.aug-card-select-badge');
            if (badge) {
                badge.className = 'aug-card-select-badge badge-selected';
                badge.innerHTML = '<i class="fas fa-check-circle"></i> Terpilih';
            }
        } else {
            card.classList.remove('selected');
            card.classList.add('unselected');
            const badge = card.querySelector('.aug-card-select-badge');
            if (badge) {
                badge.className = 'aug-card-select-badge badge-unselected';
                badge.innerHTML = '<i class="far fa-circle"></i> Nonaktif';
            }
        }
    });
}

// Global click listener to close dropdown when clicking outside
document.addEventListener('click', (e) => {
    const dropdown = document.getElementById('augAccMultiDropdown');
    const btn = document.getElementById('augAccMultiBtn');
    if (dropdown && dropdown.style.display === 'block') {
        if (!dropdown.contains(e.target) && !btn.contains(e.target)) {
            dropdown.style.display = 'none';
            const chev = document.getElementById('augAccMultiChevron');
            if (chev) chev.style.transform = 'rotate(0deg)';
        }
    }
});

async function loadAugestelNumbersData(forceRefresh = false) {
    const accIdx = getSelectedAugAccountParam();
    const isMultiple = accIdx === 'augestel_all' || accIdx.includes(',');
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
                <td colspan="${isMultiple ? 8 : 7}" class="text-center" style="padding: 30px;">
                    <i class="fas fa-circle-notch fa-spin" style="font-size: 1.5rem; color: #8b5cf6;"></i>
                    <div style="margin-top: 10px; font-weight: 500;">
                        ${isMultiple ? 'Memuat dan mendeteksi nomor dari akun-akun Augestel terpilih...' : (forceRefresh ? 'Menghubungkan ke API Augestel dan mendeteksi nomor realtime...' : 'Memuat data nomor akun Augestel...')}
                    </div>
                </td>
            </tr>
        `;
    }

    try {
        updateAugestelPoolStatus();
        const res = await fetch(`/api/numbers?account_index=${encodeURIComponent(accIdx)}&refresh=${forceRefresh ? '1' : '0'}`);
        const data = await res.json();

        if (!data.success) {
            showToast(data.message || 'Gagal mengambil nomor dari portal Augestel', 'error');
            if (tbody) {
                tbody.innerHTML = `<tr><td colspan="${isMultiple ? 8 : 7}" class="text-center text-danger" style="padding: 24px;"><i class="fas fa-exclamation-triangle"></i> ${escapeHtml(data.message || 'Gagal memuat nomor')}</td></tr>`;
            }
            if (statTotal) statTotal.textContent = '0';
            if (breakdownEl) breakdownEl.style.display = 'none';
            return;
        }

        allAugestelNumbersList = data.numbers || [];
        const total = data.total || allAugestelNumbersList.length;

        if (statTotal) statTotal.textContent = total.toLocaleString('id-ID');
        if (statAcc) {
            if (accIdx === 'augestel_all') {
                statAcc.textContent = `Semua Akun Augestel (${(data.accounts_breakdown || []).length} Akun)`;
            } else if (accIdx.includes(',')) {
                statAcc.textContent = `${selectedAugAccounts.size} Akun Terpilih (#${Array.from(selectedAugAccounts).map(Number).sort((a,b)=>a-b).join(', #')})`;
            } else {
                statAcc.textContent = data.email || 'Augestel Portal';
            }
        }
        if (statLast) statLast.textContent = data.cached_at || 'Baru saja';
        if (summary) {
            const accDesc = isMultiple ? ` (${selectedAugAccounts.size} Akun Terpilih)` : '';
            if (allAugestelNumbersList.length >= total) {
                summary.innerHTML = `Menampilkan total <b>${total.toLocaleString('id-ID')}</b> nomor${accDesc}`;
            } else {
                summary.innerHTML = `Menampilkan <b>${allAugestelNumbersList.length.toLocaleString('id-ID')}</b> dari total <b>${total.toLocaleString('id-ID')}</b> nomor${accDesc}`;
            }
        }

        // Render interactive breakdown cards
        if (breakdownEl) {
            if (data.accounts_breakdown && data.accounts_breakdown.length > 0) {
                breakdownEl.style.display = 'grid';
                const headerHtml = `
                    <div style="grid-column: 1 / -1; display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; padding: 4px 6px; flex-wrap: wrap; gap: 8px;">
                        <span style="font-size: 0.82rem; font-weight: 600; color: #c4b5fd;">
                            <i class="fas fa-hand-pointer" style="margin-right: 6px; color: #a78bfa;"></i> Klik kartu akun di bawah untuk filter multi-select akun secara instan:
                        </span>
                        <div style="display: flex; gap: 6px;">
                            <button type="button" class="btn btn-xs" onclick="selectAugAllAccounts(true); loadAugestelNumbersData(false);" style="background: rgba(139, 92, 246, 0.2); color: #c4b5fd; border: 1px solid rgba(139, 92, 246, 0.4); font-size: 0.72rem; padding: 2px 8px;">
                                <i class="fas fa-check-double"></i> Pilih Semua
                            </button>
                            <button type="button" class="btn btn-xs" onclick="selectAugAllAccounts(false); loadAugestelNumbersData(false);" style="background: rgba(239, 68, 68, 0.15); color: #fca5a5; border: 1px solid rgba(239, 68, 68, 0.3); font-size: 0.72rem; padding: 2px 8px;">
                                <i class="fas fa-undo"></i> Reset (Akun #1)
                            </button>
                        </div>
                    </div>
                `;

                const cardsHtml = data.accounts_breakdown.map(b => {
                    const idx = Number(b.account_index);
                    const isSel = selectedAugAccounts.has(idx);
                    return `
                        <div class="account-breakdown-card aug-acc-card-interactive ${isSel ? 'selected' : 'unselected'}" 
                             data-account-index="${idx}" 
                             onclick="toggleAugAccountCardSelection(${idx})" 
                             title="Klik untuk ${isSel ? 'mengecualikan' : 'memilih'} Akun #${idx} dari filter">
                            <span class="account-breakdown-badge" style="background: rgba(139, 92, 246, 0.2); color: #c4b5fd;">
                                <i class="fas fa-satellite-dish"></i> Akun #${idx}
                            </span>
                            <span class="account-breakdown-email" title="${escapeHtml(b.email)}">${escapeHtml(b.email)}</span>
                            <span class="account-breakdown-count" style="color: #a78bfa;">${(b.total || 0).toLocaleString('id-ID')} nomor</span>
                            <span class="aug-card-select-badge ${isSel ? 'badge-selected' : 'badge-unselected'}">
                                ${isSel ? '<i class="fas fa-check-circle"></i> Terpilih' : '<i class="far fa-circle"></i> Nonaktif'}
                            </span>
                        </div>
                    `;
                }).join('');

                breakdownEl.innerHTML = headerHtml + cardsHtml;
            } else {
                breakdownEl.style.display = 'none';
                breakdownEl.innerHTML = '';
            }
        }

        renderAugestelNumbersTable(allAugestelNumbersList, isMultiple);
        if (forceRefresh) {
            showToast(`Berhasil mendeteksi total ${total} nomor Augestel!`, 'success');
        }
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
        if (tbody) {
            tbody.innerHTML = `<tr><td colspan="${isMultiple ? 8 : 7}" class="text-center text-danger" style="padding: 24px;">Error: ${escapeHtml(e.message)}</td></tr>`;
        }
    } finally {
        if (btnRef) {
            btnRef.disabled = false;
            btnRef.innerHTML = '<i class="fas fa-sync-alt"></i> Deteksi Ulang';
        }
    }
}

// ── Multi-Select State for Augestel Numbers ──
let selectedAugNumbers = new Set();
let currentVisibleAugNumbers = [];
let lastAugCheckedIndex = null;

function renderAugestelNumbersTable(list, isAll = false) {
    const tbody = document.getElementById('augNumbersTableBody');
    const thAcc = document.getElementById('thAugAccountCol');
    if (thAcc) thAcc.style.display = isAll ? '' : 'none';

    currentVisibleAugNumbers = list || [];

    if (!tbody) return;

    if (!list || list.length === 0) {
        tbody.innerHTML = `<tr><td colspan="${isAll ? 8 : 7}" class="text-center text-muted" style="padding: 24px;">Tidak ada nomor Augestel yang ditemukan.</td></tr>`;
        updateAugSelectionUI();
        return;
    }

    tbody.innerHTML = list.map((item, idx) => {
        const isChecked = selectedAugNumbers.has(String(item.number));
        const accCol = isAll ? `<td style="text-align: center;"><span class="badge" style="background: rgba(139, 92, 246, 0.2); color: #c4b5fd; font-size:0.75rem;" title="${escapeHtml(item.account_email || '')}"><i class="fas fa-user"></i> ${item.account_index ? item.account_index.replace('aug_', '#') : '#1'}</span></td>` : '';
        return `
            <tr id="augRow_${idx}" class="${isChecked ? 'selected-aug-row' : ''}" onclick="handleAugRowClick(event, ${idx})" style="cursor: pointer;">
                <td style="text-align: center;" onclick="event.stopPropagation()">
                    <input type="checkbox" class="aug-num-checkbox" data-index="${idx}" data-number="${escapeHtml(item.number)}" ${isChecked ? 'checked' : ''} onchange="onAugNumberSelectChange(this, ${idx}, event)" style="cursor: pointer; width: 17px; height: 17px; accent-color: #8b5cf6; vertical-align: middle;">
                </td>
                <td class="text-muted mono" style="font-size: 0.82rem; text-align: center;">${idx + 1}</td>
                ${accCol}
                <td class="selectable mono" style="font-weight: 600; color: #a78bfa;" title="Klik untuk salin satu nomor" onclick="event.stopPropagation(); copyText('${escapeHtml(item.number)}')">
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

    updateAugSelectionUI();
}

function handleAugRowClick(event, idx) {
    if (['INPUT', 'BUTTON', 'A', 'I', 'SELECT'].includes(event.target.tagName)) return;
    const cb = document.querySelector(`.aug-num-checkbox[data-index="${idx}"]`);
    if (cb) {
        cb.checked = !cb.checked;
        onAugNumberSelectChange(cb, idx, event);
    }
}

function onAugNumberSelectChange(checkbox, index, event) {
    const isChecked = checkbox.checked;
    const num = checkbox.dataset.number;

    if (event && event.shiftKey && lastAugCheckedIndex !== null && lastAugCheckedIndex !== index) {
        const start = Math.min(lastAugCheckedIndex, index);
        const end = Math.max(lastAugCheckedIndex, index);
        for (let i = start; i <= end; i++) {
            const item = currentVisibleAugNumbers[i];
            if (item && item.number) {
                if (isChecked) {
                    selectedAugNumbers.add(String(item.number));
                } else {
                    selectedAugNumbers.delete(String(item.number));
                }
                const rowCb = document.querySelector(`.aug-num-checkbox[data-index="${i}"]`);
                if (rowCb) rowCb.checked = isChecked;
                const rowEl = document.getElementById(`augRow_${i}`);
                if (rowEl) {
                    if (isChecked) rowEl.classList.add('selected-aug-row');
                    else rowEl.classList.remove('selected-aug-row');
                }
            }
        }
    } else {
        if (isChecked) {
            selectedAugNumbers.add(String(num));
        } else {
            selectedAugNumbers.delete(String(num));
        }
        const rowEl = document.getElementById(`augRow_${index}`);
        if (rowEl) {
            if (isChecked) rowEl.classList.add('selected-aug-row');
            else rowEl.classList.remove('selected-aug-row');
        }
    }

    lastAugCheckedIndex = index;
    updateAugSelectionUI();
}

function toggleSelectAllAugNumbers(masterCheckbox) {
    const isChecked = masterCheckbox.checked;
    currentVisibleAugNumbers.forEach((item, i) => {
        if (item && item.number) {
            if (isChecked) {
                selectedAugNumbers.add(String(item.number));
            } else {
                selectedAugNumbers.delete(String(item.number));
            }
            const rowCb = document.querySelector(`.aug-num-checkbox[data-index="${i}"]`);
            if (rowCb) rowCb.checked = isChecked;
            const rowEl = document.getElementById(`augRow_${i}`);
            if (rowEl) {
                if (isChecked) rowEl.classList.add('selected-aug-row');
                else rowEl.classList.remove('selected-aug-row');
            }
        }
    });
    updateAugSelectionUI();
}

function selectAllFilteredAugNumbers() {
    currentVisibleAugNumbers.forEach((item, i) => {
        if (item && item.number) {
            selectedAugNumbers.add(String(item.number));
            const rowCb = document.querySelector(`.aug-num-checkbox[data-index="${i}"]`);
            if (rowCb) rowCb.checked = true;
            const rowEl = document.getElementById(`augRow_${i}`);
            if (rowEl) rowEl.classList.add('selected-aug-row');
        }
    });
    updateAugSelectionUI();
    showToast(`✅ Berhasil memilih seluruh ${currentVisibleAugNumbers.length.toLocaleString('id-ID')} nomor di tabel!`, 'success');
}

function clearAugNumberSelection() {
    selectedAugNumbers.clear();
    lastAugCheckedIndex = null;
    document.querySelectorAll('.aug-num-checkbox').forEach(cb => cb.checked = false);
    document.querySelectorAll('.selected-aug-row').forEach(row => row.classList.remove('selected-aug-row'));
    updateAugSelectionUI();
}

function updateAugSelectionUI() {
    const count = selectedAugNumbers.size;
    const toolbar = document.getElementById('augSelectedToolbar');
    const countText = document.getElementById('augSelectedCountText');
    const masterCb = document.getElementById('augSelectAllCheckbox');
    const visCountEl = document.getElementById('augTotalVisibleCount');

    if (visCountEl) visCountEl.textContent = currentVisibleAugNumbers.length.toLocaleString('id-ID');
    if (countText) countText.textContent = count.toLocaleString('id-ID');

    document.querySelectorAll('.aug-sel-num-count').forEach(el => {
        el.textContent = count.toLocaleString('id-ID');
    });

    if (toolbar) {
        if (count > 0) {
            toolbar.style.display = 'flex';
        } else {
            toolbar.style.display = 'none';
        }
    }

    if (masterCb && currentVisibleAugNumbers.length > 0) {
        let selectedVisibleCount = 0;
        currentVisibleAugNumbers.forEach(item => {
            if (item && item.number && selectedAugNumbers.has(String(item.number))) {
                selectedVisibleCount++;
            }
        });

        if (selectedVisibleCount === 0) {
            masterCb.checked = false;
            masterCb.indeterminate = false;
        } else if (selectedVisibleCount === currentVisibleAugNumbers.length) {
            masterCb.checked = true;
            masterCb.indeterminate = false;
        } else {
            masterCb.checked = false;
            masterCb.indeterminate = true;
        }
    } else if (masterCb) {
        masterCb.checked = false;
        masterCb.indeterminate = false;
    }
}

function getSelectedAugNumbersData() {
    const list = [];
    allAugestelNumbersList.forEach(item => {
        if (item && item.number && selectedAugNumbers.has(String(item.number))) {
            list.push(item);
        }
    });
    return list;
}

function copySelectedAugNumbers() {
    const list = getSelectedAugNumbersData();
    if (list.length === 0) {
        showToast('Pilih minimal 1 nomor terlebih dahulu', 'warning');
        return;
    }

    const textToCopy = list.map(item => String(item.number).trim()).join('\n');
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(textToCopy).then(() => {
            showToast(`✅ Berhasil menyalin ${list.length.toLocaleString('id-ID')} nomor ke clipboard!`, 'success');
        }).catch(() => {
            copyTextFallback(textToCopy, list.length);
        });
    } else {
        copyTextFallback(textToCopy, list.length);
    }
}

function copyTextFallback(text, count) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    try {
        document.execCommand('copy');
        showToast(`✅ Berhasil menyalin ${count.toLocaleString('id-ID')} nomor ke clipboard!`, 'success');
    } catch (e) {
        showToast('Gagal menyalin: ' + e.message, 'error');
    }
    document.body.removeChild(ta);
}

function exportSelectedAugNumbersTxt() {
    const list = getSelectedAugNumbersData();
    if (list.length === 0) {
        showToast('Pilih minimal 1 nomor terlebih dahulu', 'warning');
        return;
    }

    const lines = list.map(item => String(item.number).trim()).join('\n');
    const blob = new Blob([lines], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    const nowStr = new Date().toISOString().replace(/[-:T.]/g, '').slice(0, 14);
    a.href = url;
    a.download = `augestel_selected_${list.length}_nomor_${nowStr}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    showToast(`✅ File TXT (${list.length.toLocaleString('id-ID')} nomor) berhasil didownload!`, 'success');
}

async function exportSelectedAugNumbersExcel() {
    const list = getSelectedAugNumbersData();
    if (list.length === 0) {
        showToast('Pilih minimal 1 nomor terlebih dahulu', 'warning');
        return;
    }

    showToast(`📊 Menyiapkan export Excel untuk ${list.length.toLocaleString('id-ID')} nomor terpilih...`, 'info');

    try {
        const res = await fetch('/api/numbers/export-selected/excel', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ numbers: list })
        });

        if (!res.ok) {
            const err = await res.json().catch(() => ({}));
            showToast(err.message || 'Gagal export Excel', 'error');
            return;
        }

        const blob = await res.blob();
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        const nowStr = new Date().toISOString().replace(/[-:T.]/g, '').slice(0, 14);
        a.href = url;
        a.download = `augestel_selected_${list.length}_nomor_${nowStr}.xlsx`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);

        showToast(`✅ File Excel (${list.length.toLocaleString('id-ID')} nomor) berhasil didownload!`, 'success');
    } catch (e) {
        showToast('Error export Excel: ' + e.message, 'error');
    }
}

async function sendSelectedAugNumbersTelegram() {
    const list = getSelectedAugNumbersData();
    if (list.length === 0) {
        showToast('Pilih minimal 1 nomor terlebih dahulu', 'warning');
        return;
    }

    showToast(`🚀 Mengirim ${list.length.toLocaleString('id-ID')} nomor terpilih ke Telegram...`, 'info');

    try {
        const res = await fetch('/api/numbers/send-telegram-selected', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ numbers: list })
        });
        const data = await res.json();

        if (data.success) {
            if (typeof Swal !== 'undefined') {
                Swal.fire({
                    icon: 'success',
                    title: 'Terkirim ke Telegram!',
                    text: data.message || `File TXT berisi ${list.length} nomor telah dikirim ke Telegram Pemilik.`,
                    background: '#1e293b',
                    color: '#f8fafc',
                    confirmButtonColor: '#38bdf8'
                });
            } else {
                showToast(data.message, 'success');
            }
        } else {
            showToast('⚠️ ' + (data.message || 'Gagal mengirim ke Telegram'), 'warning');
        }
    } catch (e) {
        showToast('❌ Error: ' + e.message, 'error');
    }
}

async function deleteSelectedAugNumbers() {
    const list = getSelectedAugNumbersData();
    if (list.length === 0) {
        showToast('Pilih minimal 1 nomor terlebih dahulu', 'warning');
        return;
    }

    const accIdx = typeof getSelectedAugAccountParam === 'function' ? getSelectedAugAccountParam() : (document.getElementById('augNumAccountSelect')?.value || 'augestel_all');

    const confirmMsg = `Apakah Anda yakin ingin MENGHAPUS / RETURN ${list.length.toLocaleString('id-ID')} NOMOR TERPILIH?\n\n` +
        `• Nomor yang dipilih akan dihapus dari daftar akun Augestel.\n` +
        `• Cache database lokal akan otomatis diperbarui.`;

    if (!confirm(confirmMsg)) return;

    showToast(`Sedang menghapus/return ${list.length.toLocaleString('id-ID')} nomor terpilih...`, 'info');

    try {
        const res = await fetch('/api/numbers/delete-selected', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                numbers: list.map(item => String(item.number).trim()),
                account_index: accIdx
            })
        });
        const data = await res.json();

        if (data.success) {
            showToast(data.message || `Berhasil menghapus ${list.length} nomor!`, 'success');
            // Hapus dari data memori lokal
            const delSet = new Set(list.map(item => String(item.number).trim()));
            allAugestelNumbersList = allAugestelNumbersList.filter(item => !delSet.has(String(item.number).trim()));
            clearAugNumberSelection();
            filterAugestelNumbersTable();
        } else {
            showToast(data.message || 'Gagal menghapus nomor terpilih', 'error');
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    }
}

function filterAugestelNumbersTable() {
    const query = (document.getElementById('augNumSearchInput')?.value || '').toLowerCase().trim();
    const summary = document.getElementById('augNumCountSummary');
    const accIdx = getSelectedAugAccountParam();
    const isMultiple = accIdx === 'augestel_all' || accIdx.includes(',');

    if (!query) {
        renderAugestelNumbersTable(allAugestelNumbersList, isMultiple);
        if (summary) summary.innerHTML = `Menampilkan <b>${allAugestelNumbersList.length.toLocaleString('id-ID')}</b> nomor`;
        return;
    }

    const filtered = allAugestelNumbersList.filter(item => {
        return (item.number && item.number.toLowerCase().includes(query)) ||
               (item.range && item.range.toLowerCase().includes(query)) ||
               (item.account_email && item.account_email.toLowerCase().includes(query)) ||
               (item.id && item.id.includes(query));
    });

    renderAugestelNumbersTable(filtered, isMultiple);
    if (summary) summary.innerHTML = `Ditemukan <b>${filtered.length.toLocaleString('id-ID')}</b> hasil dari <b>${allAugestelNumbersList.length.toLocaleString('id-ID')}</b> nomor`;
}

function downloadAugestelNumbersExport(format) {
    const accIdx = getSelectedAugAccountParam();
    const isAll = accIdx === 'augestel_all';

    if (allAugestelNumbersList.length === 0) {
        showToast('Tidak ada data nomor Augestel untuk diexport. Lakukan deteksi terlebih dahulu!', 'warning');
        return;
    }

    const label = isAll ? 'SEMUA AKUN AUGESTEL' : `${selectedAugAccounts.size} Akun Terpilih (#${Array.from(selectedAugAccounts).map(Number).sort((a,b)=>a-b).join(', #')})`;
    const countLabel = allAugestelNumbersList.length ? `(${allAugestelNumbersList.length.toLocaleString('id-ID')} nomor)` : '';
    showToast(`Menyiapkan export ${format.toUpperCase()} ${label} ${countLabel}...`, 'info');
    const downloadUrl = `/api/numbers/export/${format}?account_index=${encodeURIComponent(accIdx)}`;
    window.location.href = downloadUrl;
}

async function sendAugestelNumbersToTelegram() {
    const btn = document.getElementById('btnSendAugTxtTelegram');
    if (btn) btn.disabled = true;

    const accIdx = getSelectedAugAccountParam();
    const label = accIdx === 'augestel_all' ? 'seluruh akun' : `${selectedAugAccounts.size} akun terpilih`;
    showToast(`🚀 Sedang mengekspor nomor ${label} & mengirimkan file .txt ke Telegram...`, 'info');

    try {
        const res = await fetch('/api/numbers/send-telegram', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ account_index: accIdx })
        });
        const data = await res.json();

        if (data.success) {
            showToast(`✅ Berhasil! File TXT (${(data.total_numbers || 0).toLocaleString('id-ID')} nomor) telah terkirim ke Telegram.`, 'success');
        } else {
            showToast('⚠️ ' + (data.message || 'Gagal mengirim file ke Telegram'), 'warning');
        }
    } catch (e) {
        showToast('❌ Terjadi kesalahan: ' + e.message, 'error');
    } finally {
        if (btn) btn.disabled = false;
    }
}

async function updateAugestelPoolStatus() {
    const badge = document.getElementById('augPoolStatusBadge');
    const text = document.getElementById('augPoolStatusText');
    if (!badge || !text) return;

    try {
        const res = await fetch('/api/augestel/pool/status');
        const data = await res.json();
        if (data.success && data.status) {
            const statuses = Object.values(data.status);
            const loggedInCount = statuses.filter(s => s.logged_in).length;
            const totalCount = statuses.length || 7;

            if (loggedInCount === totalCount && totalCount > 0) {
                badge.style.background = 'rgba(16, 185, 129, 0.15)';
                badge.style.color = '#34d399';
                badge.style.border = '1px solid rgba(16, 185, 129, 0.3)';
                text.textContent = `Browser Pool: ${loggedInCount}/${totalCount} Akun Standby di RAM (24/7)`;
            } else if (loggedInCount > 0) {
                badge.style.background = 'rgba(59, 130, 246, 0.15)';
                badge.style.color = '#60a5fa';
                badge.style.border = '1px solid rgba(59, 130, 246, 0.3)';
                text.textContent = `Browser Pool: ${loggedInCount}/${totalCount} Standby (Menyiapkan Sisa Akun...)`;
            } else {
                badge.style.background = 'rgba(245, 158, 11, 0.15)';
                badge.style.color = '#fbbf24';
                badge.style.border = '1px solid rgba(245, 158, 11, 0.3)';
                text.textContent = `Browser Pool: Menyiapkan Sesi (${totalCount} Akun)...`;
            }
        }
    } catch (e) {
        // silent
    }
}

async function deleteAllAugestelNumbers() {
    const accIdx = getSelectedAugAccountParam();
    const isAll = accIdx === 'augestel_all';
    const accLabel = isAll ? 'SEMUA AKUN AUGESTEL' : `${selectedAugAccounts.size} AKUN TERPILIH (#${Array.from(selectedAugAccounts).map(Number).sort((a,b)=>a-b).join(', #')})`;

    const confirmMsg = `Apakah Anda yakin ingin RETURN ALL / HAPUS SEMUA NOMOR untuk ${accLabel}?\n\n` +
        `• Tindakan ini akan mengembalikan semua nomor akun terpilih langsung ke sistem via https://augestel.com/Switchfy/client/numbers menggunakan sesi browser resmi.\n` +
        `• Seluruh cache nomor akun terpilih juga akan otomatis dibersihkan.`;
    if (!confirm(confirmMsg)) return;

    const btn = document.getElementById('btnDeleteAllAugNumbers');
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Menghapus/Return All...';
    }

    showToast(`Sedang melakukan Return All Numbers untuk ${accLabel} melalui portal Augestel...`, 'info');

    try {
        const res = await fetch('/api/numbers/delete-all', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ account_index: accIdx })
        });
        const data = await res.json();
        if (data.success) {
            if (typeof Swal !== 'undefined') {
                Swal.fire({
                    icon: 'success',
                    title: 'Berhasil Return All!',
                    text: data.message || 'Semua nomor Augestel berhasil di-return ke portal.',
                    background: '#1e293b',
                    color: '#f8fafc',
                    confirmButtonColor: '#10b981'
                });
            } else {
                showToast(data.message || 'Semua nomor Augestel berhasil di-return!', 'success');
            }
            await loadAugestelNumbersData(true);
        } else {
            if (typeof Swal !== 'undefined') {
                Swal.fire({
                    icon: 'warning',
                    title: 'Perhatian: Return Nomor Belum Berhasil',
                    text: data.message || 'Gagal return semua nomor dari portal Augestel.',
                    background: '#1e293b',
                    color: '#f8fafc',
                    confirmButtonColor: '#ef4444'
                });
            } else {
                showToast(data.message || 'Gagal return semua nomor!', 'error');
            }
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-trash-alt"></i> Return All / Hapus Semua Nomor';
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

        // Render status akun IVASMS dan Augestel dari backend bot status / api accounts
        await renderBotControlAccountsStatus(status.accounts_status || null);
        await renderBotControlAugestelStatus(status.augestel_accounts_status || null);
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
        if (document.getElementById('cfgOwnerChatId')) document.getElementById('cfgOwnerChatId').value = cfg.OWNER_CHAT_ID || '';
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
        OWNER_CHAT_ID: document.getElementById('cfgOwnerChatId')?.value.trim(),
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

async function renderBotControlAugestelStatus(customResults = null) {
    const listContainer = document.getElementById('augAccountsStatusList');
    if (!listContainer) return;

    try {
        let accounts = [];
        if (customResults && Array.isArray(customResults) && customResults.length > 0) {
            accounts = customResults;
        } else {
            const res = await fetch('/api/augestel/accounts');
            const data = await res.json();
            accounts = (data.accounts || []).map((a, i) => ({
                index: i + 1,
                email: a.email,
                connected: a.connected !== undefined ? a.connected : !!a.api_key,
                balance: a.balance || '0.00',
                last_check: a.last_check || (a.api_key ? 'Status Terpantau (Aktif)' : 'Belum ada API Key')
            }));
        }

        const countBadge = document.getElementById('augAccCountBadge');
        if (countBadge) {
            countBadge.textContent = `${accounts.length} Akun Terdaftar`;
        }

        const icon = document.getElementById('augIcon');
        const text = document.getElementById('augStatusText');
        const desc = document.getElementById('augStatusDesc');

        const anyConn = accounts.some(a => a.connected || a.cookie_connected || a.is_pool_active);

        if (icon) {
            icon.className = anyConn ? 'bot-icon online' : 'bot-icon offline';
        }
        if (text) {
            text.textContent = 'Augestel Multi-Account';
        }
        if (desc) {
            const connCount = accounts.filter(a => a.connected || (a.api_connected && a.cookie_connected)).length;
            const poolCount = accounts.filter(a => a.is_pool_active || (a.cookie_status && a.cookie_status.includes('RAM')) || a.cookie_connected).length;
            if (poolCount > 0) {
                desc.innerHTML = `<span style="color: #34d399; font-weight: 600;"><i class="fas fa-desktop"></i> Browser Keep-Alive: ${poolCount}/${accounts.length} Standby di RAM (24/7)</span> • ${connCount}/${accounts.length} Full Active`;
            } else {
                desc.textContent = anyConn 
                    ? `Status semua akun terpantau (${connCount}/${accounts.length} Terhubung)` 
                    : 'Tidak ada akun yang terhubung';
            }
        }

        if (accounts.length === 0) {
            listContainer.innerHTML = `
                <div class="text-muted" style="font-size: 0.85rem; padding: 14px; text-align: center; background: rgba(255,255,255,0.02); border-radius: 8px;">
                    Belum ada akun Augestel terdaftar. <a href="/accounts" style="color: #a78bfa; text-decoration: underline;">Kelola Akun</a> untuk menambahkan akun.
                </div>
            `;
            return;
        }

        listContainer.innerHTML = accounts.map(acc => {
            const apiOk = !!acc.api_connected;
            const isPoolActive = !!acc.is_pool_active || (acc.cookie_status && acc.cookie_status.includes('RAM'));
            const cookieOk = !!acc.cookie_connected || isPoolActive;
            const fullyConnected = apiOk && cookieOk;

            const statusDot = fullyConnected 
                ? '<div class="status-dot online" style="margin: 0; box-shadow: 0 0 8px rgba(16,185,129,0.6);" title="API & Browser Keep-Alive di RAM Aktif"></div>' 
                : (apiOk || cookieOk)
                    ? '<div class="status-dot" style="margin: 0; background: #f59e0b; box-shadow: 0 0 8px rgba(245,158,11,0.6);" title="Parsial: Perlu perhatian"></div>'
                    : '<div class="status-dot offline" style="margin: 0; box-shadow: 0 0 8px rgba(239,68,68,0.6);" title="Terputus"></div>';

            const apiBadge = apiOk
                ? '<span class="badge badge-success" style="font-size: 0.7rem; padding: 3px 6px;" title="REST API Key Valid"><i class="fas fa-key"></i> API OK</span>'
                : '<span class="badge badge-danger" style="font-size: 0.7rem; padding: 3px 6px;" title="REST API Key Invalid"><i class="fas fa-times"></i> API Off</span>';

            let cookieBadge = '';
            if (isPoolActive) {
                cookieBadge = '<span class="badge" style="font-size: 0.7rem; padding: 3px 7px; background: rgba(16, 185, 129, 0.2); border: 1px solid rgba(16, 185, 129, 0.45); color: #34d399;" title="Live Browser Tab Standby di RAM 24/7 (Instan 0s)"><i class="fas fa-desktop"></i> RAM Standby</span>';
            } else if (cookieOk) {
                if (acc.has_remember) {
                    cookieBadge = '<span class="badge badge-success" style="font-size: 0.7rem; padding: 3px 6px;" title="Browser Profile & Sesi Remember Me Aktif (Jangka Panjang)"><i class="fas fa-cookie-bite"></i> Browser OK</span>';
                } else {
                    cookieBadge = '<span class="badge badge-info" style="font-size: 0.7rem; padding: 3px 6px;" title="Browser Profile Sesi Aktif (Session Cookie)"><i class="fas fa-cookie-bite"></i> Sesi OK</span>';
                }
            } else {
                cookieBadge = `<span class="badge badge-warning" style="font-size: 0.7rem; padding: 3px 6px;" title="${escapeHtml(acc.cookie_status || 'Browser Belum Login')}"><i class="fas fa-exclamation-triangle"></i> Browser Off</span>`;
            }

            const balInfo = acc.balance && acc.balance !== '0.00' ? ` • Saldo: $${acc.balance}` : '';
            const statusDetail = isPoolActive
                ? ` • <span style="color: #34d399; font-weight: 500;"><i class="fas fa-bolt"></i> Live RAM Tab Active</span>`
                : (acc.cookie_status ? ` • <span style="color: ${cookieOk ? 'var(--text-muted)' : '#f59e0b'}; font-size: 0.72rem;">${escapeHtml(acc.cookie_status)}</span>` : '');

            const loginBtn = !cookieOk
                ? `<button class="btn-sm" style="padding: 4px 8px; font-size: 0.75rem; background: rgba(245, 158, 11, 0.15); border: 1px solid rgba(245, 158, 11, 0.4); color: #fbbf24;" onclick="loginAugestelSingle(${acc.index})" id="btnLoginAug_${acc.index}" title="Login Browser Profil Akun #${acc.index}"><i class="fas fa-sign-in-alt"></i> Login RAM</button>`
                : '';

            return `
                <div id="accStatusCard_aug_${acc.index}" style="background: rgba(139, 92, 246, 0.04); border: 1px solid rgba(139, 92, 246, 0.2); border-radius: 10px; padding: 12px 14px; display: flex; align-items: center; justify-content: space-between; gap: 10px; transition: all 0.2s ease;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        ${statusDot}
                        <div>
                            <div style="display: flex; align-items: center; gap: 8px;">
                                <b style="font-size: 0.92rem; color: var(--text);">Akun #${acc.index}</b>
                                <span class="text-muted" style="font-size: 0.8rem; font-family: monospace;">(${escapeHtml(acc.email)})</span>
                            </div>
                            <div class="text-muted" style="font-size: 0.74rem; margin-top: 3px;" id="augAccCheckTime_${acc.index}">
                                <i class="far fa-clock"></i> ${acc.last_check ? 'Cek: ' + acc.last_check : 'Status terpantau'}${balInfo}${statusDetail}
                            </div>
                        </div>
                    </div>
                    <div style="display: flex; align-items: center; gap: 6px;">
                        <span id="augAccApiBadge_${acc.index}">${apiBadge}</span>
                        <span id="augAccCookieBadge_${acc.index}">${cookieBadge}</span>
                        ${loginBtn}
                        <button class="btn-sm" style="padding: 4px 10px; font-size: 0.75rem;" onclick="checkAugestelSingle(${acc.index})" id="btnCheckAugAcc_${acc.index}" title="Cek status API & Live Tab Browser Akun #${acc.index}">
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

async function checkAllAugestelAccounts() {
    const btn = document.getElementById('btnCheckAllAug');
    const orig = btn ? btn.innerHTML : '';
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Cek...';
    }
    try {
        const res = await fetch('/api/augestel/check', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({})
        });
        const data = await res.json();
        if (data.success && data.status) {
            await renderBotControlAugestelStatus(data.status.accounts || []);
            showToast('Sinkronisasi status seluruh akun Augestel dengan Browser Pool selesai!', 'success');
        } else {
            showToast('Gagal sinkron akun: ' + (data.message || 'Error'), 'error');
        }
    } catch (e) {
        showToast('Gagal sinkron akun Augestel: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = orig;
        }
    }
}

async function checkAugestelSingle(index) {
    const btn = document.getElementById(`btnCheckAugAcc_${index}`);
    const originalHtml = btn ? btn.innerHTML : '';
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i>';
    }

    try {
        const res = await fetch('/api/augestel/check', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ index: index })
        });
        const data = await res.json();
        if (data.success && data.status) {
            const accList = data.status.accounts || [];
            await renderBotControlAugestelStatus(accList);
            const thisAcc = accList.find(a => a.index === index);
            if (thisAcc) {
                const isPool = thisAcc.is_pool_active || (thisAcc.cookie_status && thisAcc.cookie_status.includes('RAM'));
                if (thisAcc.api_connected && (thisAcc.cookie_connected || isPool)) {
                    showToast(`Akun #${index}: API Key OK & Browser Live Tab Standby di RAM (24/7)!`, 'success');
                } else if (thisAcc.api_connected && !thisAcc.cookie_connected && !isPool) {
                    showToast(`Akun #${index}: API OK, Browser Live Tab belum aktif (${thisAcc.cookie_status})`, 'warning');
                } else if (!thisAcc.api_connected && (thisAcc.cookie_connected || isPool)) {
                    showToast(`Akun #${index}: Browser aktif di RAM, namun API Key belum valid!`, 'warning');
                } else {
                    showToast(`Akun #${index}: Terputus (API & Browser tidak aktif)`, 'error');
                }
            }
        } else {
            showToast(`Gagal cek akun Augestel #${index}: ${data.message || 'Error'}`, 'error');
        }
    } catch (e) {
        showToast(`Gagal cek akun Augestel #${index}: ${e.message}`, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = originalHtml;
        }
    }
}

async function loginAugestelSingle(index) {
    const btn = document.getElementById(`btnLoginAug_${index}`);
    const originalHtml = btn ? btn.innerHTML : '';
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i>';
    }

    try {
        const res = await fetch('/api/augestel/login-single', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ index: index })
        });
        const data = await res.json();
        if (data.success) {
            showToast(data.message, 'success');
            // Auto re-check in 8 seconds after login completes
            setTimeout(() => checkAugestelSingle(index), 8000);
        } else {
            showToast(data.message || 'Gagal memulai login browser', 'error');
        }
    } catch (e) {
        showToast('Error login akun: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = originalHtml;
        }
    }
}

async function checkAugestelConnection() {
    const text = document.getElementById('augStatusText');
    const desc = document.getElementById('augStatusDesc');
    const btn = document.getElementById('btnCheckAugestel');

    if (text) text.textContent = 'Memeriksa Semua Akun Augestel...';
    if (desc) desc.textContent = 'Memvalidasi REST API & Browser Profile Cookies per akun...';
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Memeriksa...';
    }

    try {
        const res = await fetch('/api/augestel/check', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({})
        });
        const data = await res.json();

        if (data.success && data.status) {
            const accList = data.status.accounts || [];
            await renderBotControlAugestelStatus(accList);
            const bothCount = accList.filter(a => a.api_connected && a.cookie_connected).length;
            const apiCount = accList.filter(a => a.api_connected).length;
            const cookieCount = accList.filter(a => a.cookie_connected).length;
            showToast(`Cek Augestel selesai: API (${apiCount}/${accList.length}) • Browser (${cookieCount}/${accList.length})`, bothCount > 0 ? 'success' : 'warning');
        } else {
            showToast(`Gagal cek akun Augestel: ${data.message || 'Error'}`, 'error');
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
                    <div style="display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end;">
                        <button class="btn btn-sm" style="background: linear-gradient(135deg, #6366f1, #4f46e5); color: #fff; font-weight: 600;" onclick="showAugestelWindow(${idx + 1})" title="Buka browser di layar desktop VPS untuk login / selesaikan captcha">
                            <i class="fas fa-desktop"></i> Buka di Layar
                        </button>
                        <button class="btn btn-primary btn-sm" style="background: linear-gradient(135deg, #10b981, #059669); border: none; font-weight: 600;" onclick="openAugSimulateModal(${idx + 1}, '${email}')" title="Test Live Webhook & Kirim SMS Dummy ke Telegram">
                            <i class="fas fa-vial"></i> Test SMS
                        </button>
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
        checkWebhookStatusLive();
    } catch (e) {
        container.innerHTML = `<div class="text-danger" style="padding: 10px;">Gagal memuat akun: ${e.message}</div>`;
    }
}

let currentDesktopModalAccount = null;

async function showAugestelWindow(idx) {
    let email = '';
    let password = '';
    if (typeof currentAugestelAccounts !== 'undefined' && currentAugestelAccounts && currentAugestelAccounts[idx - 1]) {
        email = currentAugestelAccounts[idx - 1].email || '';
        password = currentAugestelAccounts[idx - 1].password || '';
    }

    // Buka modal interaktif terlebih dahulu agar user mendapat respon visual langsung
    openAugDesktopModal(idx, email, password);

    showToast(`🖥️ Membuka jendela browser Akun #${idx} di layar desktop VPS...`, 'info');
    try {
        const res = await fetch(`/api/augestel/pool/show/${idx}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        const data = await res.json();
        if (data.success) {
            showToast(`✅ ${data.message}`, 'success');
            if (data.email) email = data.email;
            if (data.password) password = data.password;
            openAugDesktopModal(idx, email, password, data.message);
        } else {
            showToast(`⚠️ ${data.message}`, 'warning');
            const statusBox = document.getElementById('desktopModalStatusBox');
            if (statusBox) {
                statusBox.className = 'text-warning';
                statusBox.style.display = 'block';
                statusBox.style.background = 'rgba(234, 179, 8, 0.1)';
                statusBox.innerHTML = `⚠️ ${escapeHtml(data.message)}`;
            }
        }
    } catch (e) {
        showToast(`❌ Error: ${e.message}`, 'error');
    }
}

function openAugDesktopModal(idx, email, password, statusMsg) {
    currentDesktopModalAccount = { idx, email, password };
    const modal = document.getElementById('augDesktopModal');
    if (!modal) return;

    const titleEl = document.getElementById('desktopModalTitle');
    if (titleEl) titleEl.textContent = `Layar Browser Akun #${idx}`;

    const emailEl = document.getElementById('desktopModalEmail');
    if (emailEl) emailEl.textContent = email || `Akun #${idx}`;

    const pwdEl = document.getElementById('desktopModalPassword');
    if (pwdEl) pwdEl.textContent = password || '(tersimpan)';

    const statusBox = document.getElementById('desktopModalStatusBox');
    if (statusBox) {
        if (statusMsg) {
            statusBox.className = 'text-success';
            statusBox.style.display = 'block';
            statusBox.style.background = 'rgba(16, 185, 129, 0.1)';
            statusBox.innerHTML = `✅ ${escapeHtml(statusMsg)}`;
        } else {
            statusBox.style.display = 'none';
        }
    }

    modal.style.display = 'flex';
}

function closeAugDesktopModal() {
    const modal = document.getElementById('augDesktopModal');
    if (modal) modal.style.display = 'none';
}

function copyDesktopModalField(field) {
    if (!currentDesktopModalAccount) return;
    const text = field === 'email' ? currentDesktopModalAccount.email : currentDesktopModalAccount.password;
    if (!text) {
        showToast('Kredensial kosong!', 'warning');
        return;
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(() => {
            showToast(`📋 ${field === 'email' ? 'Email' : 'Password'} berhasil disalin ke clipboard!`, 'success');
        }).catch(() => {
            prompt(`Salin ${field}:`, text);
        });
    } else {
        prompt(`Salin ${field}:`, text);
    }
}

async function focusAugestelDesktopWindowAction() {
    if (!currentDesktopModalAccount) return;
    const idx = currentDesktopModalAccount.idx;
    showToast(`🖥️ Memfokuskan jendela Akun #${idx} ke depan layar...`, 'info');
    try {
        const res = await fetch(`/api/augestel/pool/show/${idx}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        const data = await res.json();
        showToast(data.message, data.success ? 'success' : 'warning');
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
    }
}

async function closeAugestelDesktopWindowAction() {
    if (!currentDesktopModalAccount) return;
    const idx = currentDesktopModalAccount.idx;
    showToast(`Menutup jendela desktop Akun #${idx}...`, 'info');
    try {
        const res = await fetch(`/api/augestel/pool/close-desktop/${idx}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        const data = await res.json();
        showToast(data.message, data.success ? 'success' : 'warning');
        closeAugDesktopModal();
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
    }
}

async function syncAugestelDesktopSessionAction() {
    if (!currentDesktopModalAccount) return;
    const idx = currentDesktopModalAccount.idx;
    const btn = document.getElementById('btnSyncDesktopSession');
    if (btn) btn.disabled = true;
    showToast(`🔄 Memeriksa & menyinkronkan sesi Akun #${idx}...`, 'info');

    try {
        const res = await fetch(`/api/augestel/pool/sync-session/${idx}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        const data = await res.json();
        if (data.success && data.logged_in) {
            showToast(`🎉 ${data.message}`, 'success');
            const statusBox = document.getElementById('desktopModalStatusBox');
            if (statusBox) {
                statusBox.className = 'text-success';
                statusBox.style.display = 'block';
                statusBox.style.background = 'rgba(16, 185, 129, 0.15)';
                statusBox.innerHTML = `🎉 <b>Login Terverifikasi!</b> Cookie sesi aktif & bot telah disinkronkan.`;
            }
            if (typeof loadAugestelAccounts === 'function') loadAugestelAccounts();
        } else {
            showToast(`⚠️ ${data.message}`, 'warning');
            const statusBox = document.getElementById('desktopModalStatusBox');
            if (statusBox) {
                statusBox.className = 'text-warning';
                statusBox.style.display = 'block';
                statusBox.style.background = 'rgba(234, 179, 8, 0.15)';
                statusBox.innerHTML = `⚠️ ${escapeHtml(data.message)}`;
            }
        }
    } catch (e) {
        showToast(`Error: ${e.message}`, 'error');
    } finally {
        if (btn) btn.disabled = false;
    }
}

async function hideAugestelWindow(idx) {
    try {
        const res = await fetch(`/api/augestel/pool/hide/${idx}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        const data = await res.json();
        if (data.success) {
            showToast(`✅ ${data.message}`, 'success');
        }
    } catch (e) {
        showToast(`❌ Error: ${e.message}`, 'error');
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

async function setupAllAugestelWebhooks() {
    const btn = document.getElementById('btnSetupAllWebhooks');
    const originalText = btn ? btn.innerHTML : '';
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Menyiapkan Webhook...';
    }
    showToast('Memasang Webhook ke seluruh akun Augestel (Bypass 429 Limit)...', 'info');
    try {
        const res = await fetch('/api/augestel/webhooks/setup-all', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });

        if (res.status === 401 || res.redirected) {
            showToast('Sesi login telah berakhir. Mengarahkan ke halaman login...', 'warning');
            setTimeout(() => { window.location.href = '/login'; }, 1200);
            return;
        }

        const text = await res.text();
        let data;
        try {
            data = JSON.parse(text);
        } catch (parseErr) {
            if (text.includes('<!DOCTYPE') || text.includes('<html')) {
                showToast('Sesi login telah kedaluwarsa. Silakan login kembali.', 'warning');
                setTimeout(() => { window.location.href = '/login'; }, 1200);
                return;
            }
            throw new Error('Respon server tidak valid');
        }

        if (data.success) {
            showToast(data.message || 'Webhook berhasil dikonfigurasi ke seluruh akun Augestel!', 'success');
        } else if (data.need_login) {
            showToast(data.message || 'Sesi login telah berakhir', 'warning');
            setTimeout(() => { window.location.href = '/login'; }, 1200);
        } else {
            showToast(data.message || 'Gagal memasang webhook', 'error');
        }
    } catch (e) {
        showToast('Error: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = originalText || '<i class="fas fa-satellite-dish"></i> Pasang Webhook (Bypass Limit 429)';
        }
    }
}

function copyWebhookUrl() {
    const input = document.getElementById('webhookUrlDisplay');
    if (!input) return;
    navigator.clipboard.writeText(input.value).then(() => {
        showToast('URL Webhook berhasil disalin ke clipboard!', 'success');
    }).catch(() => {
        input.select();
        document.execCommand('copy');
        showToast('URL Webhook berhasil disalin!', 'success');
    });
}

async function checkWebhookStatusLive() {
    const btn = document.getElementById('btnCheckWebhookLive');
    if (btn) btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i>';
    try {
        const res = await fetch('/api/augestel/webhooks/status');
        const data = await res.json();
        if (data.success) {
            const countEl = document.getElementById('whTotalCount');
            const timeEl = document.getElementById('whLastTime');
            const badgeEl = document.getElementById('webhookStatusBadge');
            const guardEl = document.getElementById('whGuardianStatus');
            const listEl = document.getElementById('whGuardianAccountsList');

            if (countEl) countEl.innerText = `${data.total_received} OTP`;
            if (timeEl) timeEl.innerText = data.last_received ? `${data.last_received} (${data.last_event || 'event'})` : 'Belum ada';
            if (badgeEl) badgeEl.innerHTML = '<i class="fas fa-circle" style="font-size: 0.6rem;"></i> 200 OK - AKTIF &amp; LISTENING';

            const urlInput = document.getElementById('webhookUrlDisplay');
            if (urlInput && data.webhook_url) urlInput.value = data.webhook_url;

            const tunnelStatusEl = document.getElementById('whTunnelStatus');
            if (tunnelStatusEl && data.tunnel_url) {
                const isCf = data.tunnel_url.includes('trycloudflare.com') || data.tunnel_url.includes('cloudflare');
                tunnelStatusEl.innerHTML = isCf ? '🟢 Cloudflare Tunnel (24/7)' : '🟢 Tunnel Online';
            }

            if (guardEl) {
                if (data.guardian_enabled) {
                    guardEl.innerHTML = '<span style="color: #10b981;">🟢 Auto-Heal Aktif (24/7)</span>';
                } else {
                    guardEl.innerHTML = '<span style="color: #ef4444;">🔴 Guardian Nonaktif</span>';
                }
            }

            if (listEl && data.guardian_accounts) {
                const entries = Object.entries(data.guardian_accounts);
                if (entries.length > 0) {
                    listEl.innerHTML = entries.map(([idx, st]) => {
                        const isDeliv = st.is_delivering;
                        const isPaused = st.is_paused;
                        const recovers = st.auto_recovered_count || 0;
                        let bg = isDeliv ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)';
                        let border = isDeliv ? 'rgba(16, 185, 129, 0.4)' : 'rgba(239, 68, 68, 0.4)';
                        let color = isDeliv ? '#10b981' : '#ef4444';
                        let label = isDeliv ? 'Delivering' : (isPaused ? 'Paused' : 'OFF');
                        let recoverBadge = recovers > 0 ? `<span style="background: rgba(245, 158, 11, 0.2); color: #f59e0b; padding: 1px 5px; border-radius: 4px; font-size: 0.7rem; margin-left: 4px;" title="Jumlah otomatis dinyalakan kembali saat mati">🛡️ Healed: ${recovers}x</span>` : '';

                        return `
                            <div style="background: ${bg}; border: 1px solid ${border}; border-radius: 6px; padding: 4px 10px; font-size: 0.75rem; display: flex; align-items: center; gap: 6px;">
                                <b style="color: var(--text-main);">Akun #${idx}</b>
                                <span style="color: ${color}; font-weight: 600;">● ${label}</span>
                                ${recoverBadge}
                            </div>
                        `;
                    }).join('');
                }
            }
        }
    } catch (e) {
        console.error('Error checking webhook status:', e);
    } finally {
        if (btn) btn.innerHTML = '<i class="fas fa-sync-alt"></i> Cek Status';
    }
}

async function triggerGuardianCheckNow() {
    const btn = document.getElementById('btnGuardianCheckNow');
    const orig = btn ? btn.innerHTML : '';
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Checking...';
    }
    showToast('Memeriksa status webhook & menjalankan auto-heal jika ada yang mati...', 'info');
    try {
        const res = await fetch('/api/augestel/webhooks/guardian/check-now', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        });
        const data = await res.json();
        if (data.success) {
            let healedCount = 0;
            if (data.results) {
                Object.values(data.results).forEach(r => {
                    if (r && r.auto_healed) healedCount++;
                });
            }
            if (healedCount > 0) {
                showToast(`🛡️ Webhook Guardian: ${healedCount} akun terdeteksi mati dan BERHASIL dinyalakan kembali otomatis!`, 'success');
            } else {
                showToast('🛡️ Webhook Guardian: Semua akun sehat & aktif Delivering (tidak ada yang mati).', 'success');
            }
            await checkWebhookStatusLive();
        } else {
            showToast('Gagal check guardian: ' + (data.message || 'error'), 'error');
        }
    } catch (e) {
        showToast('Error guardian check: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = orig || '<i class="fas fa-shield-alt"></i> Auto-Heal Check';
        }
    }
}

async function sendTestWebhookPing() {
    const btn = document.getElementById('btnTestWebhookPing');
    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Mengirim Test...';
    }
    showToast('Mengirim simulasi webhook test ke server...', 'info');
    try {
        const payload = {
            event: "message.received",
            data: {
                number: "+6281299887766",
                source: "WhatsApp",
                message: "Kode verifikasi WhatsApp Anda adalah: 852-149. Jangan bagikan ke siapapun.",
                rate: 0.0150,
                status: "delivered",
                received_at: new Date().toISOString()
            }
        };
        const res = await fetch('/api/augestel/webhook', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Augestel-Event': 'message.received'
            },
            body: JSON.stringify(payload)
        });
        const data = await res.json();
        if (data.success) {
            showToast('✅ Test Webhook berhasil diterima & dikirim ke grup Telegram!', 'success');
            setTimeout(checkWebhookStatusLive, 1000);
        } else {
            showToast('Gagal mengirim test webhook: ' + (data.message || 'error'), 'error');
        }
    } catch (e) {
        showToast('Error test webhook: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-paper-plane"></i> Test Kirim Webhook';
        }
    }
}

// ────────────────────────────────────────────
//  AUTO-ADD AUGESTEL (SEPARATE NAVIGATION)
// ────────────────────────────────────────────

let augAutoAddInterval = null;

let augAddAccountsCache = [];

async function loadAugAddAccountSelect() {
    const container = document.getElementById('augAddAccountsContainer');
    const summary = document.getElementById('augAddSelectedSummary');
    if (!container) return;

    try {
        const res = await fetch('/api/augestel/accounts');
        const data = await res.json();
        const accounts = data.accounts || [];
        augAddAccountsCache = accounts;

        if (accounts.length === 0) {
            container.innerHTML = '<div class="text-danger" style="font-size: 0.85rem; padding: 8px;">Belum ada akun Augestel yang terdaftar!</div>';
            if (summary) summary.textContent = 'Tidak ada akun';
            return;
        }

        // Coba ambil jumlah nomor terkini dari API numbers jika ada
        let numbersBreakdown = {};
        try {
            const numRes = await fetch('/api/numbers?account_index=augestel_all&refresh=0');
            const numData = await numRes.json();
            if (numData.success && numData.accounts_breakdown) {
                numData.accounts_breakdown.forEach(b => {
                    numbersBreakdown[b.account_index] = b.total || 0;
                });
            }
        } catch (ex) {
            console.debug('Failed to load numbers breakdown for auto add:', ex);
        }

        let html = '';
        accounts.forEach((acc, i) => {
            const idx = i + 1;
            const currentTotal = numbersBreakdown[idx] !== undefined ? numbersBreakdown[idx] : (acc.total_numbers || 0);
            const isFull = currentTotal >= 2500;
            const badgeBg = isFull ? 'rgba(239, 68, 68, 0.2)' : (currentTotal > 0 ? 'rgba(56, 189, 248, 0.2)' : 'rgba(255, 255, 255, 0.08)');
            const badgeColor = isFull ? '#f87171' : (currentTotal > 0 ? '#38bdf8' : '#94a3b8');
            const badgeText = isFull ? `${currentTotal.toLocaleString('id-ID')}/2.500 🔒 FULL` : `${currentTotal.toLocaleString('id-ID')}/2.500`;

            // Default dicentang jika belum penuh
            const isChecked = !isFull;

            html += `
                <label class="aug-account-chk-card" style="display: flex; align-items: center; gap: 10px; padding: 9px 12px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 8px; cursor: pointer; user-select: none; transition: all 0.2s;">
                    <input type="checkbox" class="aug-acc-chk" value="${idx}" ${isChecked ? 'checked' : ''} onchange="updateAugAddSelectedSummary()" style="width: 17px; height: 17px; accent-color: #0ea5e9; cursor: pointer;">
                    <div style="flex: 1; min-width: 0;">
                        <div style="display: flex; align-items: center; justify-content: space-between; gap: 4px; margin-bottom: 2px;">
                            <span style="font-weight: 700; font-size: 0.85rem; color: #f1f5f9;">Akun #${idx}</span>
                            <span class="badge" style="font-size: 0.68rem; padding: 2px 6px; background: ${badgeBg}; color: ${badgeColor}; font-weight: 600;">
                                ${badgeText}
                            </span>
                        </div>
                        <div style="font-size: 0.74rem; color: var(--text-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;" title="${escapeHtml(acc.email)}">
                            ${escapeHtml(acc.email)}
                        </div>
                    </div>
                </label>
            `;
        });

        container.innerHTML = html;
        updateAugAddSelectedSummary();
    } catch (e) {
        console.error('Failed to load Augestel accounts for auto-add:', e);
        if (container) container.innerHTML = '<div class="text-danger" style="padding: 8px;">Gagal memuat akun Augestel.</div>';
    }
}

function selectAllAugAddAccounts(selectAll) {
    const checkboxes = document.querySelectorAll('.aug-acc-chk');
    checkboxes.forEach(cb => {
        cb.checked = !!selectAll;
    });
    updateAugAddSelectedSummary();
}

function updateAugAddSelectedSummary() {
    const checkboxes = document.querySelectorAll('.aug-acc-chk:checked');
    const summary = document.getElementById('augAddSelectedSummary');
    if (!summary) return;

    const selectedVals = Array.from(checkboxes).map(cb => parseInt(cb.value, 10)).sort((a, b) => a - b);
    if (selectedVals.length === 0) {
        summary.innerHTML = '<span class="text-danger"><i class="fas fa-exclamation-circle"></i> Tidak ada akun yang dipilih (pilih minimal 1 akun)!</span>';
    } else if (selectedVals.length === augAddAccountsCache.length) {
        summary.innerHTML = `<span style="color: #38bdf8;"><i class="fas fa-check-circle"></i> <b>Semua Akun (${selectedVals.length} akun)</b> dipilih untuk Auto-Add</span>`;
    } else {
        const labels = selectedVals.map(v => `#${v}`).join(', ');
        summary.innerHTML = `<span style="color: #38bdf8;"><i class="fas fa-check-circle"></i> <b>${selectedVals.length} Akun Dipilih:</b> Akun ${labels}</span>`;
    }
}

function setAugAddBatchCount(val) {
    const el = document.getElementById('augAddBatchCount');
    if (el) el.value = val;
}

async function startAugestelAutoAdd() {
    const rangeName = (document.getElementById('augAddRangeName')?.value || '').trim();
    const numberPrefix = (document.getElementById('augAddNumberPrefix')?.value || '').trim();
    const batchCount = parseInt(document.getElementById('augAddBatchCount')?.value || '250', 10);
    const maxAdd = parseInt(document.getElementById('augAddMaxAdd')?.value || '0', 10);
    const delay = parseInt(document.getElementById('augAddDelay')?.value || '15', 10);
    const workers = parseInt(document.getElementById('augAddWorkers')?.value || '2', 10);

    const checkedBoxes = document.querySelectorAll('.aug-acc-chk:checked');
    const selectedAccounts = Array.from(checkedBoxes).map(cb => cb.value.trim()).filter(Boolean);

    if (selectedAccounts.length === 0) {
        showToast('Pilih minimal satu akun Augestel untuk Auto-Add!', 'warning');
        return;
    }

    const accountArg = selectedAccounts.join(',');

    const btnStart = document.getElementById('btnStartAugAdd');
    const btnStop = document.getElementById('btnStopAugAdd');
    if (btnStart) btnStart.disabled = true;

    try {
        const res = await fetch('/api/augestel/auto-add/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                account_index: accountArg,
                workers: workers,
                range_name: rangeName,
                number_prefix: numberPrefix,
                batch_count: batchCount,
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
        const runningInfo = document.getElementById('augAddRunningAccountInfo');
        const runningText = document.getElementById('augAddRunningAccountText');

        // Toggle checkbox disabled state while running
        const chks = document.querySelectorAll('.aug-acc-chk');
        chks.forEach(cb => { cb.disabled = !!state.running; });

        if (state.running) {
            if (btnStart) { btnStart.style.display = 'none'; btnStart.disabled = false; }
            if (btnStop) { btnStop.style.display = 'inline-flex'; }
            if (badge) { badge.textContent = 'Running'; badge.className = 'status-badge active'; }
            if (runningInfo && state.account_email) {
                runningInfo.style.display = 'block';
                if (runningText) {
                    const workerBadge = state.workers ? ` <span class="badge badge-info" style="font-size:0.75rem;"><i class="fas fa-bolt"></i> ${state.workers} Workers</span>` : '';
                    const rangeBadge = state.range_name ? ` <span class="badge" style="background: rgba(167, 139, 250, 0.2); color: #c4b5fd; font-size:0.75rem;"><i class="fas fa-globe"></i> ${escapeHtml(state.range_name)}</span>` : '';
                    const prefixBadge = state.number_prefix ? ` <span class="badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; font-size:0.75rem;"><i class="fas fa-phone-alt"></i> ${escapeHtml(state.number_prefix)}</span>` : '';
                    runningText.innerHTML = `Sedang berjalan pada: <b>${escapeHtml(state.account_email)}</b>${workerBadge}${rangeBadge}${prefixBadge}`;
                }
            }
        } else {
            if (btnStart) { btnStart.style.display = 'inline-flex'; btnStart.disabled = false; }
            if (btnStop) { btnStop.style.display = 'none'; }
            if (badge) { badge.textContent = 'Idle'; badge.className = 'status-badge'; }
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

// ────────────────────────────────────────────
//  FITUR 1: SMART CAP BALANCER (AUTO-ADD ALL)
// ────────────────────────────────────────────
function enableSmartCapBalancerMode() {
    selectAllAugAddAccounts(true);
    const batchInput = document.getElementById('augAddBatchCount');
    const maxInput = document.getElementById('augAddMaxAdd');
    const delayInput = document.getElementById('augAddDelay');
    const workersInput = document.getElementById('augAddWorkers');

    if (batchInput) batchInput.value = '250';
    if (maxInput) maxInput.value = '0'; // 0 = Auto-Fill sampai kuota 2.500 per akun
    if (delayInput) delayInput.value = '15';
    if (workersInput) workersInput.value = '2';

    const count = (augAddAccountsCache && augAddAccountsCache.length) ? augAddAccountsCache.length : document.querySelectorAll('.aug-acc-chk').length;
    showToast(`🚀 Mode Smart Balancer AKTIF! Seluruh ${count} akun dipilih untuk diisi merata hingga batas 2.500 nomor per akun.`, 'success');
}

// ────────────────────────────────────────────
//  FITUR 2: EARNINGS & REVENUE ANALYTICS (DUAL MODE: REST API & REAL-TIME WEBHOOK)
// ────────────────────────────────────────────
let currentEarningsMode = 'api';
let _cachedEarningsPayload = null;
let _earningsSyncInterval = null;

function switchEarningsTab(tabName) {
    const vAccounts = document.getElementById('earnViewAccounts');
    const vDaily = document.getElementById('earnViewDaily');
    const vNumbers = document.getElementById('earnViewNumbers');

    const bAcc = document.getElementById('btnTabEarnAcc');
    const bDaily = document.getElementById('btnTabEarnDaily');
    const bNums = document.getElementById('btnTabEarnNums');

    const activeStyle = "background: rgba(124, 92, 252, 0.25); color: #fff; border: 1px solid var(--accent);";
    const inactiveStyle = "background: rgba(255, 255, 255, 0.05); color: var(--text-muted); border: 1px solid var(--border);";

    if (vAccounts) vAccounts.style.display = tabName === 'accounts' ? 'block' : 'none';
    if (vDaily) vDaily.style.display = tabName === 'daily' ? 'block' : 'none';
    if (vNumbers) vNumbers.style.display = tabName === 'numbers' ? 'block' : 'none';

    if (bAcc) bAcc.style.cssText = tabName === 'accounts' ? activeStyle : inactiveStyle;
    if (bDaily) bDaily.style.cssText = tabName === 'daily' ? activeStyle : inactiveStyle;
    if (bNums) bNums.style.cssText = tabName === 'numbers' ? activeStyle : inactiveStyle;
}

function setEarningsMode(mode) {
    if (mode !== 'api' && mode !== 'webhook') mode = 'api';
    currentEarningsMode = mode;

    const btnApi = document.getElementById('btnModeApi');
    const btnWb = document.getElementById('btnModeWebhook');
    const badgeEngine = document.getElementById('earnEngineBadge');
    const titleTotal = document.getElementById('earnCardTitleTotal');
    const btnSyncApi = document.getElementById('btnSyncEarningsApi');
    const accTitleBadge = document.getElementById('earnTotalAccountsBadge');

    if (mode === 'api') {
        if (btnApi) {
            btnApi.style.background = 'var(--accent)';
            btnApi.style.color = '#fff';
            btnApi.style.fontWeight = '700';
        }
        if (btnWb) {
            btnWb.style.background = 'transparent';
            btnWb.style.color = 'var(--text-muted)';
            btnWb.style.fontWeight = '600';
        }
        if (badgeEngine) {
            badgeEngine.className = 'badge badge-success';
            badgeEngine.innerHTML = '<i class="fas fa-bolt"></i> Official Augestel REST API';
        }
        if (titleTotal) {
            titleTotal.textContent = 'Total Payout (Akumulasi API)';
        }
        if (btnSyncApi) {
            btnSyncApi.style.display = 'inline-flex';
        }
        if (accTitleBadge) {
            accTitleBadge.textContent = 'Total 32 Akun Terdaftar (Data Resmi REST API)';
        }
    } else {
        if (btnApi) {
            btnApi.style.background = 'transparent';
            btnApi.style.color = 'var(--text-muted)';
            btnApi.style.fontWeight = '600';
        }
        if (btnWb) {
            btnWb.style.background = 'linear-gradient(135deg, #0284c7, #0ea5e9)';
            btnWb.style.color = '#fff';
            btnWb.style.fontWeight = '700';
        }
        if (badgeEngine) {
            badgeEngine.className = 'badge badge-info';
            badgeEngine.innerHTML = '<i class="fas fa-satellite-dish"></i> Live Webhook Stream (Real-Time)';
        }
        if (titleTotal) {
            titleTotal.textContent = 'Total Payout (Real-Time Webhook)';
        }
        if (btnSyncApi) {
            btnSyncApi.style.display = 'none';
        }
        if (accTitleBadge) {
            accTitleBadge.textContent = 'Data Real-Time Push Webhook (Auto-Recorded)';
        }
    }

    if (_cachedEarningsPayload) {
        const rate = _cachedEarningsPayload.exchange_rate || 16250;
        const d = (mode === 'webhook' ? _cachedEarningsPayload.webhook_data : _cachedEarningsPayload.api_data) || _cachedEarningsPayload.data;
        if (d) {
            renderEarningsData(d, rate, mode);
            return;
        }
    }

    loadEarningsAnalytics(mode);
}

async function triggerApiEarningsSync() {
    const btn = document.getElementById('btnSyncEarningsApi');
    const badgeSyncing = document.getElementById('earnSyncingBadge');
    const badgeProgress = document.getElementById('earnSyncProgress');

    if (btn) btn.disabled = true;
    if (badgeSyncing) badgeSyncing.style.display = 'inline-flex';
    if (badgeProgress) badgeProgress.textContent = '0%';

    try {
        const res = await fetch('/api/augestel/earnings/sync', { method: 'POST' });
        const json = await res.json();
        showNotification(json.message || "Sinkronisasi API Augestel dimulai...", "info");

        if (_earningsSyncInterval) clearInterval(_earningsSyncInterval);
        _earningsSyncInterval = setInterval(async () => {
            try {
                const sRes = await fetch('/api/augestel/earnings/sync-status');
                const sJson = await sRes.json();
                const st = sJson.sync_status || {};

                if (badgeProgress) badgeProgress.textContent = `${st.progress_pct || 0}%`;

                if (!st.is_syncing) {
                    clearInterval(_earningsSyncInterval);
                    _earningsSyncInterval = null;
                    if (badgeSyncing) badgeSyncing.style.display = 'none';
                    if (btn) btn.disabled = false;
                    showNotification(`✅ Sinkronisasi API selesai! ${st.total_synced || 32} akun berhasil dimutakhirkan.`, "success");
                    loadEarningsAnalytics('api');
                }
            } catch (err) {
                console.error('Error polling sync status:', err);
            }
        }, 1500);

    } catch (e) {
        showNotification("Gagal memicu sinkronisasi API: " + e.message, "error");
        if (btn) btn.disabled = false;
        if (badgeSyncing) badgeSyncing.style.display = 'none';
    }
}

function renderEarningsData(d, rate, mode) {
    if (!d) return;
    rate = rate || 16250;
    mode = mode || currentEarningsMode;

    const elTotalUsd = document.getElementById('earnTotalUsd');
    const elTotalIdr = document.getElementById('earnTotalIdr');
    const elTodayUsd = document.getElementById('earnTodayUsd');
    const elTodaySms = document.getElementById('earnTodaySms');
    const elYestUsd = document.getElementById('earnYesterdayUsd');
    const elYestSms = document.getElementById('earnYesterdaySms');
    const elTotalSms = document.getElementById('earnTotalSms');
    const elStatRev = document.getElementById('statRevenue');
    const elAvgRate = document.getElementById('earnAvgRate');
    const elLastSync = document.getElementById('earnLastSyncBadge');
    const elAccCount = document.getElementById('earnAccCount');

    const totalUsd = typeof d.total_revenue_usd === 'number' ? d.total_revenue_usd : parseFloat(d.total_revenue_usd || 0);
    const totalIdr = d.total_revenue_idr || Math.round(totalUsd * rate);
    const totalSms = d.total_sms || 0;

    if (elTotalUsd) elTotalUsd.textContent = `$${totalUsd.toFixed(4)}`;
    if (elTotalIdr) elTotalIdr.textContent = `≈ Rp ${totalIdr.toLocaleString('id-ID')}`;
    if (elTodayUsd) elTodayUsd.textContent = `$${(d.today_revenue_usd || 0).toFixed(4)}`;
    if (elTodaySms) elTodaySms.textContent = d.today_sms || 0;
    if (elYestUsd) elYestUsd.textContent = `$${(d.yesterday_revenue_usd || 0).toFixed(4)}`;
    if (elYestSms) elYestSms.textContent = d.yesterday_sms || 0;
    if (elTotalSms) elTotalSms.textContent = totalSms;
    if (elStatRev) elStatRev.textContent = `$${totalUsd.toFixed(2)}`;

    if (elAvgRate) {
        if (totalSms > 0) {
            const avg = totalUsd / totalSms;
            elAvgRate.textContent = `~$${avg.toFixed(4)}`;
        } else {
            elAvgRate.textContent = '~$0.0160';
        }
    }

    if (elLastSync) {
        if (mode === 'api') {
            if (d.last_api_sync) {
                elLastSync.innerHTML = `<i class="fas fa-check-circle text-success"></i> API Sync: ${escapeHtml(d.last_api_sync)}`;
            } else {
                elLastSync.innerHTML = `<i class="fas fa-clock"></i> API Sync: Standby`;
            }
        } else {
            const lastTime = d.last_event_time || d.last_updated || 'Real-Time Active';
            elLastSync.innerHTML = `<i class="fas fa-satellite-dish text-info"></i> Webhook: ${escapeHtml(lastTime)}`;
        }
    }

    // 1. Render Rincian Akun
    const accContainer = document.getElementById('earnAccountsList');
    const accs = d.by_account || {};
    const keys = Object.keys(accs);
    if (elAccCount) elAccCount.textContent = keys.length || 32;

    if (accContainer) {
        if (keys.length === 0) {
            accContainer.innerHTML = `<div class="text-muted" style="font-size: 0.82rem; grid-column: 1 / -1; padding: 10px;">Belum ada data pendapatan akun untuk mode ini.</div>`;
        } else {
            const sortedKeys = keys.sort((a,b) => {
                const na = parseInt(a);
                const nb = parseInt(b);
                if (!isNaN(na) && !isNaN(nb)) return na - nb;
                return String(a).localeCompare(String(b));
            });

            accContainer.innerHTML = sortedKeys.map(k => {
                const item = accs[k];
                const u = typeof item.usd === 'number' ? item.usd : parseFloat(item.usd || 0);
                const idrEst = item.idr || Math.round(u * rate);
                const isConn = item.api_connected !== false;
                const isNumericKey = !isNaN(parseInt(k)) && String(parseInt(k)) === String(k);
                const accLabel = isNumericKey ? `Akun #${k}` : (item.email ? `Akun ${escapeHtml(item.email)}` : escapeHtml(k));
                const badgeText = mode === 'api' ? (isConn ? 'API OK' : 'Cache') : 'Webhook';
                const badgeClass = mode === 'api' ? (isConn ? 'badge-success' : 'badge-warning') : 'badge-info';

                return `
                    <div style="background: rgba(255,255,255,0.03); border: 1px solid ${u > 0 ? 'rgba(16, 185, 129, 0.3)' : 'var(--border)'}; border-radius: 10px; padding: 12px 14px; display: flex; align-items: center; justify-content: space-between; transition: transform 0.2s;" onmouseenter="this.style.transform='translateY(-2px)'" onmouseleave="this.style.transform='translateY(0)'">
                        <div style="min-width: 0; flex: 1; padding-right: 10px;">
                            <div style="display: flex; align-items: center; gap: 6px;">
                                <span style="font-weight: 700; font-size: 0.88rem; color: #fff;">${accLabel}</span>
                                <span class="badge ${badgeClass}" style="font-size: 0.65rem; padding: 1px 6px;">${badgeText}</span>
                            </div>
                            <div class="text-muted" style="font-size: 0.75rem; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${escapeHtml(item.email || k)}">${escapeHtml(item.email || k)}</div>
                        </div>
                        <div style="text-align: right; flex-shrink: 0;">
                            <div style="font-weight: 800; font-size: 0.95rem; color: ${u > 0 ? '#10b981' : '#64748b'};">$${u.toFixed(4)}</div>
                            <div style="font-size: 0.74rem; color: #38bdf8;">${item.sms || 0} SMS <span class="text-muted">(Rp ${idrEst.toLocaleString('id-ID')})</span></div>
                        </div>
                    </div>
                `;
            }).join('');
        }
    }

    // 2. Render Riwayat Harian (Daily Breakdown Table)
    const dailyBody = document.getElementById('earnDailyTableBody');
    if (dailyBody) {
        const daily = d.daily_breakdown || [];
        if (daily.length === 0) {
            dailyBody.innerHTML = `<tr><td colspan="4" style="text-align: center; padding: 20px;" class="text-muted">Belum ada riwayat harian tercatat untuk versi ${mode === 'api' ? 'REST API' : 'Webhook'}.</td></tr>`;
        } else {
            dailyBody.innerHTML = daily.map(item => {
                const earn = typeof item.earnings === 'number' ? item.earnings : parseFloat(item.earnings || 0);
                const idr = item.earnings_idr || Math.round(earn * rate);
                return `
                    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 0.85rem;">
                        <td style="padding: 10px 12px; font-weight: 600; color: #e2e8f0;"><i class="far fa-calendar-check" style="color: #38bdf8; margin-right: 6px;"></i> ${escapeHtml(item.period)}</td>
                        <td style="padding: 10px 12px; text-align: center;"><span class="badge badge-success" style="font-weight: 700;">${item.messages || item.delivered || 0} SMS</span></td>
                        <td style="padding: 10px 12px; text-align: right; font-weight: 700; color: #10b981;">$${earn.toFixed(4)}</td>
                        <td style="padding: 10px 12px; text-align: right; font-weight: 600; color: #38bdf8;">Rp ${idr.toLocaleString('id-ID')}</td>
                    </tr>
                `;
            }).join('');
        }
    }

    // 3. Render Top Numbers Table / Recent Transactions
    const numsBody = document.getElementById('earnNumbersTableBody');
    if (numsBody) {
        const topNums = d.top_numbers || [];
        if (topNums.length > 0) {
            numsBody.innerHTML = topNums.map((tn, i) => {
                const earn = typeof tn.earnings === 'number' ? tn.earnings : parseFloat(tn.earnings || 0);
                return `
                    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 0.84rem;">
                        <td style="padding: 9px 12px; color: var(--text-muted); font-weight: 700;">#${i + 1}</td>
                        <td style="padding: 9px 12px; font-family: monospace; font-weight: 700; color: #f8fafc;"><i class="fas fa-phone-alt" style="color: #10b981; margin-right: 6px; font-size: 0.75rem;"></i> +${escapeHtml(tn.number)}</td>
                        <td style="padding: 9px 12px; color: #94a3b8; font-size: 0.78rem;">${escapeHtml(tn.range_name || '-')}</td>
                        <td style="padding: 9px 12px; color: #cbd5e1; font-size: 0.78rem; max-width: 140px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${escapeHtml(tn.account || '-')}">${escapeHtml(tn.account || '-')}</td>
                        <td style="padding: 9px 12px; text-align: center;"><span class="badge badge-info" style="font-weight: 700;">${tn.messages || 0}</span></td>
                        <td style="padding: 9px 12px; text-align: right; font-weight: 800; color: #10b981;">$${earn.toFixed(4)}</td>
                    </tr>
                `;
            }).join('');
        } else if (d.recent_transactions && d.recent_transactions.length > 0) {
            numsBody.innerHTML = d.recent_transactions.slice(0, 20).map((tx, i) => {
                const r = typeof tx.rate_usd === 'number' ? tx.rate_usd : parseFloat(tx.rate_usd || 0.016);
                return `
                    <tr style="border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 0.84rem;">
                        <td style="padding: 9px 12px; color: var(--text-muted); font-weight: 700;">#${i + 1}</td>
                        <td style="padding: 9px 12px; font-family: monospace; font-weight: 700; color: #f8fafc;"><i class="fas fa-sms" style="color: #38bdf8; margin-right: 6px; font-size: 0.75rem;"></i> ${escapeHtml(tx.phone || '-')}</td>
                        <td style="padding: 9px 12px; color: #94a3b8; font-size: 0.78rem;">${escapeHtml(tx.platform || 'SMS')} (${escapeHtml(tx.flag || '')})</td>
                        <td style="padding: 9px 12px; color: #cbd5e1; font-size: 0.78rem; max-width: 140px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;" title="${escapeHtml(tx.account || '-')}">${escapeHtml(tx.account || '-')}</td>
                        <td style="padding: 9px 12px; text-align: center;"><span class="badge badge-success" style="font-weight: 700;">1 OTP</span></td>
                        <td style="padding: 9px 12px; text-align: right; font-weight: 800; color: #10b981;">+$${r.toFixed(4)}</td>
                    </tr>
                `;
            }).join('');
        } else {
            numsBody.innerHTML = `<tr><td colspan="6" style="text-align: center; padding: 20px;" class="text-muted">Belum ada traffic pada nomor Augestel untuk versi ini.</td></tr>`;
        }
    }
}

async function loadEarningsAnalytics(mode) {
    if (!mode) mode = currentEarningsMode;
    try {
        const res = await fetch(`/api/augestel/earnings?mode=${encodeURIComponent(mode)}`);
        const json = await res.json();
        if (!json.success) return;
        _cachedEarningsPayload = json;
        const rate = json.exchange_rate || 16250;
        const activeData = (mode === 'webhook' ? json.webhook_data : json.api_data) || json.data;
        renderEarningsData(activeData, rate, mode);
    } catch (e) {
        console.error('Error loadEarningsAnalytics:', e);
    }
}

// ────────────────────────────────────────────
//  FITUR 6: LIVE SMS SIMULATOR & WEBHOOK TESTER
// ────────────────────────────────────────────
function openAugSimulateModal(targetAccountIdx, email) {
    const modal = document.getElementById('augSimulateModal');
    if (!modal) return;

    const sel = document.getElementById('simAccountSelect');
    if (sel && currentAugestelAccounts && currentAugestelAccounts.length > 0) {
        sel.innerHTML = currentAugestelAccounts.map((acc, i) => `
            <option value="${i + 1}" ${targetAccountIdx && targetAccountIdx === (i + 1) ? 'selected' : ''}>
                Akun #${i + 1} (${escapeHtml(acc.email || '')})
            </option>
        `).join('');
    } else if (sel) {
        sel.innerHTML = `<option value="${targetAccountIdx || 1}">Akun #${targetAccountIdx || 1} (${escapeHtml(email || '')})</option>`;
    }

    const resBox = document.getElementById('simResultBox');
    if (resBox) resBox.style.display = 'none';

    randomizeSimOtp();
    modal.style.display = 'flex';
}

function closeAugSimulateModal() {
    const modal = document.getElementById('augSimulateModal');
    if (modal) modal.style.display = 'none';
}

function updateSimCountryFlag() {
    const sel = document.getElementById('simCountry');
    const phoneInput = document.getElementById('simPhone');
    if (!sel || !phoneInput) return;
    const parts = sel.value.split('|');
    if (parts.length >= 3) {
        phoneInput.value = parts[2];
    }
}

function randomizeSimOtp() {
    const input = document.getElementById('simOtp');
    if (input) {
        const rand = Math.floor(100000 + Math.random() * 900000);
        input.value = String(rand);
    }
}

async function submitAugSimulateSms() {
    const btn = document.getElementById('btnSubmitAugSimulate');
    const resBox = document.getElementById('simResultBox');
    const accIdx = document.getElementById('simAccountSelect')?.value || '1';
    const countryParts = (document.getElementById('simCountry')?.value || 'ZW|🇿🇼|+263788124006').split('|');
    const platform = document.getElementById('simPlatform')?.value || 'WhatsApp';
    const phone = document.getElementById('simPhone')?.value.trim() || '+263788124006';
    const otp = document.getElementById('simOtp')?.value.trim() || '884762';
    const rate = parseFloat(document.getElementById('simRate')?.value || '0.0150');
    const rangeName = document.getElementById('simRangeName')?.value.trim() || 'Augestel Test Range';

    if (btn) {
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Mengirim & Mencatat Cuan...';
    }

    try {
        const payload = {
            account_index: parseInt(accIdx),
            phone: phone,
            platform: platform,
            otp: otp,
            rate: rate,
            range_name: rangeName,
            country_code: countryParts[0] || 'ZW',
            flag: countryParts[1] || '🇿🇼'
        };

        const res = await fetch('/api/augestel/webhook/simulate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        const data = await res.json();

        if (data.success) {
            showToast(`✅ ${data.message}`, 'success');
            if (resBox) {
                resBox.style.display = 'block';
                resBox.style.background = 'rgba(16, 185, 129, 0.15)';
                resBox.style.border = '1px solid rgba(16, 185, 129, 0.3)';
                resBox.style.color = '#10b981';
                resBox.innerHTML = `
                    <div style="font-weight: 700; margin-bottom: 4px;"><i class="fas fa-check-circle"></i> Simulasi Webhook Berhasil Terkirim!</div>
                    <div style="font-size: 0.82rem; color: var(--text-secondary); line-height: 1.6;">
                        • Akun: <b>${data.account}</b><br>
                        • Nomor & Platform: <b>${data.phone} (${platform})</b><br>
                        • OTP: <b style="color: #fff;">${data.otp}</b> | Cuan: <b style="color: #10b981;">+$${data.rate.toFixed(4)}</b><br>
                        • Telegram Status: <b>${data.telegram_sent ? 'Terkirim ke Grup (Message ID: ' + data.telegram_message_id + ')' : 'Pesan Tersimpan'}</b>
                    </div>
                `;
            }
            loadEarningsAnalytics();
        } else {
            showToast('Gagal simulasi: ' + (data.message || 'error'), 'error');
        }
    } catch (e) {
        showToast('Error simulasi: ' + e.message, 'error');
    } finally {
        if (btn) {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-paper-plane"></i> Kirim Test Webhook & Cuan Sekarang 🚀';
        }
    }
}
