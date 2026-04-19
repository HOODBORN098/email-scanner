import os
import re

# The correct, clean sidebar HTML to inject into every file
CORRECT_SIDEBAR = '''    <div class="px-6 mb-8">
        <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-primary flex items-center justify-center text-white shadow-md shadow-primary/20">
                <span class="material-symbols-outlined">shield_with_heart</span>
            </div>
            <div>
                <h1 class="text-[11px] font-black uppercase tracking-[0.2em] text-primary leading-tight">Clinical Sentinel</h1>
                <p class="text-[9px] font-bold uppercase tracking-widest text-slate-400 leading-tight">Enterprise Security</p>
            </div>
        </div>
    </div>
    <div class="px-4 mb-6">
        <button onclick="window.location.href=\'functional scanner.html\'" class="w-full bg-primary text-white py-3 px-4 rounded-2xl font-bold text-sm flex items-center justify-center gap-2 shadow-lg shadow-primary/20 hover:bg-primary/90 transition-all active:scale-95">
            <span class="material-symbols-outlined text-[20px]">add</span>
            <span data-i18n="nav_new_scan">New Scan</span>
        </button>
    </div>
    <nav class="flex-1 px-3 space-y-1" id="desktop-nav">
        <a href="dashboard.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined">shield_with_heart</span>
            <span data-i18n="nav_security_scan">Security Scan</span>
        </a>
        <a href="functional scanner.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined">manage_search</span>
            <span data-i18n="nav_full_scanner">Full Scanner</span>
        </a>
        <a href="threat feed.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined">radar</span>
            <span data-i18n="nav_threat_feed">Threat Feed</span>
        </a>
        <a href="scan history.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined">history</span>
            <span data-i18n="nav_scan_history">Scan History</span>
        </a>
        <a href="security vault.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined">lock</span>
            <span data-i18n="nav_security_vault">Security Vault</span>
        </a>
        <a href="data reports.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined">analytics</span>
            <span data-i18n="nav_data_reports">Data Reports</span>
        </a>
        <a href="settings account.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined">manage_accounts</span>
            <span data-i18n="nav_account">Account</span>
        </a>
    </nav>
    <div class="px-3 border-t border-slate-300 dark:border-slate-800/50 pt-4 space-y-1">
        <a href="documentation.html" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-2xl text-xs text-slate-400 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-[18px]">menu_book</span>
            <span data-i18n="nav_documentation">Documentation</span>
        </a>
        <a href="support.html" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-2xl text-xs text-slate-400 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-[18px]">contact_support</span>
            <span data-i18n="nav_support">Support</span>
        </a>
        <div id="nav-auth-area" class="px-4 pt-3 flex items-center gap-3">
            <div class="h-8 w-8 rounded-full bg-slate-200 animate-pulse"></div>
        </div>
    </div>
</aside>'''

CORRECT_MOBILE_BOTTOM_NAV = '''<nav class="lg:hidden fixed bottom-0 left-0 right-0 z-50 bg-slate-50/95 backdrop-blur-xl border-t border-slate-300 shadow-[0_-4px_20px_rgba(0,0,0,0.05)] pb-safe">
    <div class="flex items-stretch h-16" id="mobile-bottom-nav">
        <a href="dashboard.html" class="nav-link flex-1 flex flex-col items-center justify-center gap-0.5 text-slate-400 hover:text-primary transition-colors">
            <span class="material-symbols-outlined text-[22px]">shield_with_heart</span>
            <span class="text-[9px] font-bold uppercase tracking-wider" data-i18n="nav_security_scan">Scan</span>
        </a>
        <a href="threat feed.html" class="nav-link flex-1 flex flex-col items-center justify-center gap-0.5 text-slate-400 hover:text-primary transition-colors">
            <span class="material-symbols-outlined text-[22px]">radar</span>
            <span class="text-[9px] font-bold uppercase tracking-wider" data-i18n="nav_threat_feed">Feed</span>
        </a>
        <a href="security vault.html" class="nav-link flex-1 flex flex-col items-center justify-center gap-0.5 text-slate-400 hover:text-primary transition-colors relative">
            <div class="absolute -top-6 left-1/2 -translate-x-1/2 w-12 h-12 bg-primary rounded-full flex items-center justify-center text-white shadow-lg shadow-primary/20 border-4 border-slate-100">
                <span class="material-symbols-outlined">lock</span>
            </div>
            <span class="text-[9px] font-bold uppercase tracking-wider mt-5" data-i18n="nav_security_vault">Vault</span>
        </a>
        <a href="settings account.html" class="nav-link flex-1 flex flex-col items-center justify-center gap-0.5 text-slate-400 hover:text-primary transition-colors">
            <span class="material-symbols-outlined text-[22px]">manage_accounts</span>
            <span class="text-[9px] font-bold uppercase tracking-wider" data-i18n="nav_account">Account</span>
        </a>
    </div>
</nav>'''

CORRECT_MOBILE_HEADER_ICON = '<span class="material-symbols-outlined">shield_with_heart</span>'

# --- Regex patterns to match broken sidebar content -------------------------
# These patterns match the broken text-icon + nested-span pattern anywhere it appears

# Broken nav button (add icon + double-nested New Scan)
broken_btn = re.compile(
    r'(<button[^>]*?functional scanner\.html[^>]*?>)\s*\n?\s*add\s*<span data-i18n="nav_new_scan">(<span data-i18n="nav_new_scan">)?New Scan(</span>)?</span></button>',
    re.DOTALL
)
fixed_btn = r'\1\n            <span class="material-symbols-outlined text-[20px]">add</span>\n            <span data-i18n="nav_new_scan">New Scan</span>\n        </button>'

# Broken mobile header icon
broken_mobile_icon = re.compile(r'(<div[^>]*?rounded-xl bg-primary[^>]*?w-8 h-8[^>]*?>)\s*\n?\s*shield_with_heart\s*\n?\s*</div>', re.DOTALL)
fixed_mobile_icon = r'\1\n            <span class="material-symbols-outlined">shield_with_heart</span>\n        </div>'

# Broken sidebar logo icon
broken_sidebar_logo = re.compile(r'(<div[^>]*?w-9 h-9[^>]*?rounded-xl bg-primary[^>]*?>)\s*\n?\s*shield_with_heart\s*\n?\s*</div>', re.DOTALL)
fixed_sidebar_logo = r'\1\n                <span class="material-symbols-outlined">shield_with_heart</span>\n            </div>'

# Broken nav links (icon text + double-nested span)
nav_link_fixes = [
    # Pattern: icon_name<span data-i18n="key"><span data-i18n="key">Text</span></span></a>
    (re.compile(r'shield_with_heart<span data-i18n="nav_security_scan">(<span data-i18n="nav_security_scan">)?Security Scan(</span>)?</span></a>', re.DOTALL),
     '<span class="material-symbols-outlined">shield_with_heart</span>\n            <span data-i18n="nav_security_scan">Security Scan</span>\n        </a>'),
    (re.compile(r'manage_search<span data-i18n="nav_full_scanner">(<span data-i18n="nav_full_scanner">)?Full Scanner(</span>)?</span></a>', re.DOTALL),
     '<span class="material-symbols-outlined">manage_search</span>\n            <span data-i18n="nav_full_scanner">Full Scanner</span>\n        </a>'),
    (re.compile(r'radar(<\/span\s*>)?<span data-i18n="nav_threat_feed">(<span data-i18n="nav_threat_feed">)?Threat Feed(</span>)?</a>', re.DOTALL),
     '<span class="material-symbols-outlined">radar</span>\n            <span data-i18n="nav_threat_feed">Threat Feed</span>\n        </a>'),
    (re.compile(r'history<span data-i18n="nav_scan_history">(<span data-i18n="nav_scan_history">)?Scan History(</span>)?</span></a>', re.DOTALL),
     '<span class="material-symbols-outlined">history</span>\n            <span data-i18n="nav_scan_history">Scan History</span>\n        </a>'),
    (re.compile(r'lock<span data-i18n="nav_security_vault">(<span data-i18n="nav_security_vault">)?Security Vault(</span>)?</span></a>', re.DOTALL),
     '<span class="material-symbols-outlined">lock</span>\n            <span data-i18n="nav_security_vault">Security Vault</span>\n        </a>'),
    (re.compile(r'analytics<span data-i18n="nav_data_reports">(<span data-i18n="nav_data_reports">)?Data Reports(</span>)?</span></a>', re.DOTALL),
     '<span class="material-symbols-outlined">analytics</span>\n            <span data-i18n="nav_data_reports">Data Reports</span>\n        </a>'),
    (re.compile(r'manage_accounts<span data-i18n="nav_account">(<span data-i18n="nav_account">)?Account(</span>)?</span></a>', re.DOTALL),
     '<span class="material-symbols-outlined">manage_accounts</span>\n            <span data-i18n="nav_account">Account</span>\n        </a>'),
    # Footer links
    (re.compile(r'menu_book<span data-i18n="nav_documentation">(<span data-i18n="nav_documentation">)?Documentation(</span>)?</span></a>', re.DOTALL),
     '<span class="material-symbols-outlined text-[18px]">menu_book</span>\n            <span data-i18n="nav_documentation">Documentation</span>\n        </a>'),
    (re.compile(r'contact_support<span data-i18n="nav_support">(<span data-i18n="nav_support">)?Support(</span>)?</span></a>', re.DOTALL),
     '<span class="material-symbols-outlined text-[18px]">contact_support</span>\n            <span data-i18n="nav_support">Support</span>\n        </a>'),
    # Mobile bottom nav broken icons
    (re.compile(r'(<a[^>]*?dashboard\.html[^>]*?flex flex-col[^>]*?>)\s*\n?\s*shield_with_heart\s*\n?\s*Scan\s*\n?\s*</a>', re.DOTALL),
     r'\1\n            <span class="material-symbols-outlined text-[22px]">shield_with_heart</span>\n            <span class="text-[9px] font-bold uppercase tracking-wider" data-i18n="nav_security_scan">Scan</span>\n        </a>'),
    (re.compile(r'(<a[^>]*?threat feed\.html[^>]*?flex flex-col[^>]*?>)\s*\n?\s*radar\s*\n?\s*Feed\s*\n?\s*</a>', re.DOTALL),
     r'\1\n            <span class="material-symbols-outlined text-[22px]">radar</span>\n            <span class="text-[9px] font-bold uppercase tracking-wider" data-i18n="nav_threat_feed">Feed</span>\n        </a>'),
    (re.compile(r'(<a[^>]*?scan history\.html[^>]*?flex flex-col[^>]*?>)\s*\n?\s*history\s*\n?\s*History\s*\n?\s*</a>', re.DOTALL),
     r'\1\n            <span class="material-symbols-outlined text-[22px]">history</span>\n            <span class="text-[9px] font-bold uppercase tracking-wider" data-i18n="nav_scan_history">History</span>\n        </a>'),
    (re.compile(r'(<a[^>]*?security vault\.html[^>]*?flex flex-col[^>]*?>)\s*\n?\s*lock\s*\n?\s*Vault\s*\n?\s*</a>', re.DOTALL),
     r'\1\n            <span class="material-symbols-outlined text-[22px]">lock</span>\n            <span class="text-[9px] font-bold uppercase tracking-wider" data-i18n="nav_security_vault">Vault</span>\n        </a>'),
    (re.compile(r'(<a[^>]*?settings account\.html[^>]*?flex flex-col[^>]*?>)\s*\n?\s*manage_accounts\s*\n?\s*(<span data-i18n="nav_account">(<span data-i18n="nav_account">)?Account(</span>)?</span>)\s*\n?\s*</a>', re.DOTALL),
     r'\1\n            <span class="material-symbols-outlined text-[22px]">manage_accounts</span>\n            <span class="text-[9px] font-bold uppercase tracking-wider" data-i18n="nav_account">Account</span>\n        </a>'),
    # Double-nested footer doc links
    (re.compile(r'<span data-i18n="nav_documentation"><span data-i18n="nav_documentation">Documentation</span></span>', re.DOTALL),
     '<span data-i18n="nav_documentation">Documentation</span>'),
    (re.compile(r'<span data-i18n="nav_support"><span data-i18n="nav_support">Support</span></span>', re.DOTALL),
     '<span data-i18n="nav_support">Support</span>'),
]

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
fixed_count = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Fix mobile header icon
    content = broken_mobile_icon.sub(fixed_mobile_icon, content)

    # Fix sidebar logo icon
    content = broken_sidebar_logo.sub(fixed_sidebar_logo, content)

    # Fix New Scan button
    content = broken_btn.sub(fixed_btn, content)

    # Fix all nav links
    for pattern, replacement in nav_link_fixes:
        content = pattern.sub(replacement, content)

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        fixed_count += 1
        print(f"  Fixed: {file}")

print(f"\nDone. {fixed_count} files restored.")
