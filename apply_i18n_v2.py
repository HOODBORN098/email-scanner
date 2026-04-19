import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Definitions
nav_mapping = {
    "Security Scan": "nav_security_scan",
    "Full Scanner": "nav_full_scanner",
    "Threat Feed": "nav_threat_feed",
    "Scan History": "nav_scan_history",
    "Security Vault": "nav_security_vault",
    "Data Reports": "nav_data_reports",
    "Account": "nav_account",
    "Documentation": "nav_documentation",
    "Support": "nav_support",
    "New Scan": "nav_new_scan"
}

general_mapping = {
    "Deep Inspection": "dash_title",
    "Advanced heuristic analysis for mission-critical mail protection.": "dash_subtitle",
    "Engine Status": "engine_status",
    "Optimal Security": "engine_optimal",
    "Heuristic Health": "stat_heuristic",
    "Active Threats": "stat_active_threats",
    "Sensor Load": "stat_sensor_load",
    "Honeypot Nodes": "stat_honeypot",
    "Raw Input": "tab_raw",
    "File Upload": "tab_file",
    "Execute Scan": "btn_execute",
    "Clear": "btn_clear",
    "Awaiting Input": "status_awaiting",
    "SYSTEM NOMINAL": "feed_nominal",
    "Live Attack Map": "feed_map_title",
    "Real-time vector visualization of incoming email threats.": "feed_map_desc",
    "Today's Activity": "feed_today_activity",
    "Threats Blocked": "feed_blocked"
}

# New Desktop Floating Toggle (Far Right)
desktop_toggle = """
<div class="hidden lg:flex fixed top-6 right-8 z-[100] items-center p-1 bg-slate-50/80 backdrop-blur-md rounded-full border border-slate-300 shadow-xl">
    <button onclick="updateLanguage('en')" data-lang="en" class="lang-toggle-btn px-4 py-1.5 rounded-full text-[11px] font-black tracking-widest transition-all">EN</button>
    <button onclick="updateLanguage('es')" data-lang="es" class="lang-toggle-btn px-4 py-1.5 rounded-full text-[11px] font-black tracking-widest transition-all">ES</button>
</div>
"""

# New Mobile Toggle (Right-aligned in header)
mobile_toggle = """
<div class="flex items-center p-0.5 bg-slate-200/50 dark:bg-slate-800 rounded-full border border-slate-300 ml-auto">
    <button onclick="updateLanguage('en')" data-lang="en" class="lang-toggle-btn px-3 py-1 rounded-full text-[10px] font-black tracking-widest transition-all">EN</button>
    <button onclick="updateLanguage('es')" data-lang="es" class="lang-toggle-btn px-3 py-1 rounded-full text-[10px] font-black tracking-widest transition-all">ES</button>
</div>
"""

def clean_extreme(content):
    # Remove i18n spans
    content = re.sub(r'<span data-i18n="[^"]+">(.*?)</span>', r'\1', content)
    # Remove any div with lang-toggle-btn
    content = re.sub(r'<div[^>]*>\s*(<div[^>]*>\s*)?<button onclick="updateLanguage.*?<\/div>\s*(<\/div>)?', '', content, flags=re.DOTALL)
    # Fix potential broken div tags from previous runs
    content = re.sub(r'<div\s+p-0\.5[^>]+>', '', content)
    content = content.replace('<div \n', '<div ')
    return content

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # WIPE PREVIOUS ATTEMPTS
    content = clean_extreme(content)
    content = clean_extreme(content)

    # 1. i18n Script
    if 'i18n.js' not in content:
        content = content.replace('</body>', '<script src="i18n.js"></script>\n</body>')

    # 2. Desktop Toggle: Place before closing body tag
    content = content.replace('</body>', f'{desktop_toggle}\n</body>')

    # 3. Mobile Toggle: Place inside header before mobile-auth-area
    if 'id="mobile-auth-area"' in content:
        # We use ml-auto in mobile_toggle to push it right
        content = content.replace('<div id="mobile-auth-area"', f'{mobile_toggle}\n    <div id="mobile-auth-area"')

    # 4. Add data-i18n attributes
    all_mappings = {**nav_mapping, **general_mapping}
    sorted_texts = sorted(all_mappings.keys(), key=len, reverse=True)
    for text in sorted_texts:
        key = all_mappings[text]
        content = re.sub(rf'>(?:\s*){re.escape(text)}(?:\s*)<', f'><span data-i18n="{key}">{text}</span><', content)

    # 5. UI Polish
    content = content.replace('bg-white', 'bg-slate-50')
    content = content.replace('border-slate-100', 'border-slate-300')
    content = content.replace('border-slate-200', 'border-slate-300')
    content = re.sub(r'\bbg-gradient-to-[a-zA-Z0-9-]+\b', '', content)
    content = content.replace('bg-background', 'bg-slate-100')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Relocated Toggle to Far-Right on all pages.")
