import os
import re
import traceback

NAV_CODE = """
<!-- ===== MOBILE TOP HEADER ===== -->
<header class="lg:hidden fixed top-0 left-0 right-0 z-50 h-16 bg-white/95 backdrop-blur-xl border-b border-slate-100 flex items-center justify-between px-6 shadow-sm">
    <div class="flex items-center gap-3">
        <div class="w-8 h-8 rounded-xl bg-primary flex items-center justify-center text-white shadow-sm">
            <span class="material-symbols-outlined text-base" style="font-variation-settings: 'FILL' 1;">shield_with_heart</span>
        </div>
        <span class="text-sm font-black tracking-tighter text-primary uppercase">Clinical Sentinel</span>
    </div>
    <div id="mobile-auth-area" class="flex items-center gap-2">
        <div class="h-8 w-8 rounded-full bg-slate-100 animate-pulse"></div>
    </div>
</header>

<!-- ===== DESKTOP SIDEBAR ===== -->
<aside class="hidden lg:flex flex-col fixed left-0 top-0 h-screen w-64 bg-slate-50 dark:bg-slate-950 border-r border-slate-200/50 dark:border-slate-800/50 z-40 py-8 transition-colors">
    <div class="px-6 mb-8">
        <div class="flex items-center gap-3">
            <div class="w-9 h-9 rounded-xl bg-primary flex items-center justify-center text-white shadow-sm shadow-primary/20">
                <span class="material-symbols-outlined text-lg" style="font-variation-settings: 'FILL' 1;">shield_with_heart</span>
            </div>
            <div>
                <h1 class="text-[11px] font-black uppercase tracking-[0.2em] text-primary leading-tight">Clinical Sentinel</h1>
                <p class="text-[9px] font-bold uppercase tracking-widest text-slate-400 leading-tight">Enterprise Security</p>
            </div>
        </div>
    </div>
    <div class="px-4 mb-6">
        <button onclick="window.location.href='functional scanner.html'" class="w-full bg-primary text-white py-3 px-4 rounded-2xl font-bold text-sm flex items-center justify-center gap-2 shadow-lg shadow-primary/20 hover:bg-primary/90 transition-all active:scale-95">
            <span class="material-symbols-outlined text-[18px]">add</span> New Scan
        </button>
    </div>
    <nav class="flex-1 px-3 space-y-1" id="desktop-nav">
        <a href="dashboard.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-xl">shield_with_heart</span> Security Scan
        </a>
        <a href="functional scanner.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-xl">manage_search</span> Full Scanner
        </a>
        <a href="threat feed.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-xl">radar</span> Threat Feed
        </a>
        <a href="scan history.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-xl">history</span> Scan History
        </a>
        <a href="security vault.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-xl">lock</span> Security Vault
        </a>
        <a href="data reports.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-xl">analytics</span> Data Reports
        </a>
        <a href="settings account.html" class="nav-link flex items-center gap-3 px-4 py-3 rounded-2xl text-sm font-semibold text-slate-500 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-xl">manage_accounts</span> Account
        </a>
    </nav>
    <div class="px-3 border-t border-slate-200/50 dark:border-slate-800/50 pt-4 space-y-1">
        <a href="documentation.html" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-2xl text-xs text-slate-400 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-base">menu_book</span> Documentation
        </a>
        <a href="support.html" class="nav-link flex items-center gap-3 px-4 py-2.5 rounded-2xl text-xs text-slate-400 hover:text-primary hover:bg-slate-100 dark:hover:bg-slate-900 transition-all">
            <span class="material-symbols-outlined text-base">contact_support</span> Support
        </a>
        <div id="nav-auth-area" class="px-4 pt-3 flex items-center gap-3">
            <div class="h-8 w-8 rounded-full bg-slate-200 animate-pulse"></div>
        </div>
    </div>
</aside>

<!-- ===== MOBILE BOTTOM NAV ===== -->
<nav class="lg:hidden fixed bottom-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-xl border-t border-slate-100 shadow-[0_-4px_20px_rgba(0,0,0,0.05)] pb-safe">
    <div class="flex items-stretch h-16" id="mobile-bottom-nav">
        <a href="dashboard.html" class="nav-link flex-1 flex flex-col items-center justify-center gap-0.5 text-slate-400 hover:text-primary transition-colors">
            <span class="material-symbols-outlined text-[22px]">shield_with_heart</span>
            <span class="text-[9px] font-bold uppercase tracking-wider">Scan</span>
        </a>
        <a href="threat feed.html" class="nav-link flex-1 flex flex-col items-center justify-center gap-0.5 text-slate-400 hover:text-primary transition-colors">
            <span class="material-symbols-outlined text-[22px]">radar</span>
            <span class="text-[9px] font-bold uppercase tracking-wider">Feed</span>
        </a>
        <a href="scan history.html" class="nav-link flex-1 flex flex-col items-center justify-center gap-0.5 text-slate-400 hover:text-primary transition-colors">
            <span class="material-symbols-outlined text-[22px]">history</span>
            <span class="text-[9px] font-bold uppercase tracking-wider">History</span>
        </a>
        <a href="security vault.html" class="nav-link flex-1 flex flex-col items-center justify-center gap-0.5 text-slate-400 hover:text-primary transition-colors">
            <span class="material-symbols-outlined text-[22px]">lock</span>
            <span class="text-[9px] font-bold uppercase tracking-wider">Vault</span>
        </a>
        <a href="settings account.html" class="nav-link flex-1 flex flex-col items-center justify-center gap-0.5 text-slate-400 hover:text-primary transition-colors">
            <span class="material-symbols-outlined text-[22px]">manage_accounts</span>
            <span class="text-[9px] font-bold uppercase tracking-wider">Account</span>
        </a>
    </div>
</nav>
"""

SCRIPT_CODE = """
<script>
    document.addEventListener('DOMContentLoaded', () => {
        // Active Nav Logic
        const currentPath = window.location.pathname.split('/').pop() || 'dashboard.html';
        const navLinks = document.querySelectorAll('.nav-link');
        const exactMatch = Array.from(navLinks).find(link => link.getAttribute('href') === currentPath);
        
        navLinks.forEach(link => {
            if (link.getAttribute('href') === currentPath || (!exactMatch && currentPath === '' && link.getAttribute('href') === 'dashboard.html')) {
                if (link.closest('#desktop-nav')) {
                    link.classList.remove('text-slate-500', 'hover:bg-slate-100', 'dark:hover:bg-slate-900');
                    link.classList.add('font-bold', 'text-primary', 'bg-blue-50', 'dark:bg-blue-900/20');
                    const icon = link.querySelector('.material-symbols-outlined');
                    if (icon) icon.style.fontVariationSettings = "'FILL' 1";
                } else if (link.closest('#mobile-bottom-nav')) {
                    link.classList.remove('text-slate-400');
                    link.classList.add('text-primary');
                    const icon = link.querySelector('.material-symbols-outlined');
                    if (icon) icon.style.fontVariationSettings = "'FILL' 1";
                } else {
                     link.classList.remove('text-slate-400', 'text-slate-500');
                     link.classList.add('text-primary', 'font-bold', 'bg-blue-50');
                }
            }
        });

        // Unified Auth Logic
        const isLoggedIn = localStorage.getItem('cs_logged_in');
        const loggedInHTML = `<div class="h-8 w-8 rounded-full bg-primary flex items-center justify-center text-white text-xs font-bold shadow-sm shadow-primary/30">U</div>`;
        const loggedOutHTML = `<a href="login.html" class="text-[10px] font-bold bg-primary text-white px-3 py-1.5 rounded-full uppercase tracking-widest">Log In</a>`;

        const sidebarAuth = document.getElementById('nav-auth-area');
        const mobileAuth = document.getElementById('mobile-auth-area');
        
        if (sidebarAuth) sidebarAuth.innerHTML = isLoggedIn ? loggedInHTML : loggedOutHTML;
        if (mobileAuth) mobileAuth.innerHTML = isLoggedIn ? loggedInHTML : loggedOutHTML;
    });
</script>
"""

def inject_nav(html_content, filename):
    # 1. Clean existing navigations
    for tag in ['<!-- TopNavBar -->.*?</nav>', '<!-- SideNavBar -->.*?</aside>', 
                '<!-- SideNavBar \(Shared Component\) -->.*?</aside>', '<!-- Sidebar Shell.*?-->.*?</aside>',
                '<!-- Top Navigation -->.*?</header>', '<nav class="fixed top-0.*?</nav>',
                '<!-- Sidebar Navigation Shell -->.*?</aside>']:
        html_content = re.sub(tag, '', html_content, flags=re.DOTALL)
        
    for tag in ['<!-- ===== MOBILE TOP HEADER ===== -->.*?</header>', '<!-- ===== DESKTOP SIDEBAR ===== -->.*?</aside>', 
                '<!-- ===== MOBILE BOTTOM NAV ===== -->.*?</nav>', '<!-- SideNavBar \(Hidden on Mobile.*?</aside>']:
        html_content = re.sub(tag, '', html_content, flags=re.DOTALL)

    # 2. Add padding to main tag directly instead of wrapper wrapper div
    def add_main_padding(m):
        cls = m.group(1) or ""
        if 'lg:pl-64' not in cls:
            # We add it plus desktop and mobile top/bottom padding
            cls = f"lg:pl-64 pt-20 lg:pt-10 pb-24 lg:pb-10 {cls}"
        return f'<main class="{cls.strip()}">'

    html_content = re.sub(r'<main[^>]*class="([^"]*)"[^>]*>', add_main_padding, html_content)
    # Support.html fixes
    if filename == "support.html":
        html_content = html_content.replace('pt-32 pb-20', '')
    if filename == "documentation.html":
        html_content = html_content.replace('pt-32 px-10 pb-20', 'px-10')

    # Remove dynamic script blocks that conflict
    html_content = re.sub(r'<script>\s*// --- Dynamic Auth UI ---.*?</script>', '', html_content, flags=re.DOTALL)

    # 3. Inject new nav right after <body>
    def repl_body(m):
        return m.group(0) + f'\n{NAV_CODE}\n'
    html_content = re.sub(r'(<body[^>]*>)', repl_body, html_content, count=1)
    
    # 4. Inject script before </body>
    def repl_end(m):
        return f'\n{SCRIPT_CODE}\n{m.group(0)}'
    html_content = re.sub(r'</body>', repl_end, html_content, count=1)
    
    return html_content

files = [
    "dashboard.html",
    "functional scanner.html",
    "scan history.html",
    "security vault.html",
    "threat feed.html",
    "data reports.html",
    "settings account.html",
    "support.html",
    "documentation.html"
]

for f in files:
    try:
        if not os.path.exists(f): continue
        with open(f, 'r', encoding='utf-8') as file: content = file.read()
        new_content = inject_nav(content, f)
        
        # specific manual cleanup for lingering old DOM
        new_content = re.sub(r'<div class="flex flex-1 max-w-\[1440px\] mx-auto w-full">\s*(<main)', r'\1', new_content)
        new_content = re.sub(r'</main>\s*</div>\s*<!-- Footer -->', '</main>\n<!-- Footer -->', new_content)
        
        with open(f, 'w', encoding='utf-8') as file: file.write(new_content)
        print(f"Success: {f}")
    except Exception as e:
        print(f"Error: {e}")
