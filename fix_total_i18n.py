import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Exact text-to-key mapping from i18n.js
text_map = {
    # Dashboard
    "Deep Inspection": "dash_title",
    "Advanced heuristic analysis for mission-critical mail protection.": "dash_subtitle",
    "Engine Status": "dash_engine_status",
    "Optimal Security": "dash_optimal_security",
    "Heuristic Health": "dash_heuristic_health",
    "HEURISTIC HEALTH": "dash_heuristic_health_caps",
    "Active Threats": "dash_active_threats",
    "ACTIVE THREATS": "dash_active_threats_caps",
    "Sensor Load": "dash_sensor_load",
    "SENSOR LOAD": "dash_sensor_load_caps",
    "Honeypot Nodes": "dash_honeypot_nodes",
    "HONEYPOT NODES": "dash_honeypot_nodes_caps",
    "ACTIVE": "dash_active",
    "NORMAL": "dash_normal",
    "12 nodes synchronized globally": "dash_nodes_sync",
    "No anomalies detected in last 24h": "dash_no_anomalies",
    
    # Scanner
    "Scanner": "scan_title",
    "Automated Intelligence": "scan_intel",
    "RAW INPUT": "tab_raw",
    "Direct Input": "tab_direct",
    "File Upload": "tab_file",
    "EMAIL SOURCE CODE": "label_email_source",
    "Header Analysis": "label_header_analysis",
    "Execute Scan": "btn_execute_scan",
    "Execute Forensic Scan": "btn_execute_forensic",
    
    # Support & Docs
    "Concierge Support": "sup_concierge",
    "How can we secure your flow?": "sup_hero_title",
    "Identity Name": "sup_label_name",
    "Secure Email": "sup_label_email",
    "Initialize Support Request": "sup_btn_init",
    "Master the Clinical Sentinel.": "doc_hero_title",
    "Knowledge Base": "doc_kb",
    "Get Started": "doc_get_started",
    
    # Nav
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

placeholder_map = {
    "Paste full email headers here for forensic analysis...": "placeholder_headers",
    "Paste raw email headers and body here...": "placeholder_source",
    "Your Name": "sup_placeholder_name",
    "vane@clinical.secure": "sup_placeholder_email",
    "Describe the behavior of the sentinel scanner...": "sup_placeholder_details",
    "••••••••••••": "placeholder_pwd"
}

# Icons that might have been stripped of their span class
icon_names = [
    "shield_with_heart", "add", "manage_search", "radar", "history", "lock", 
    "analytics", "manage_accounts", "menu_book", "contact_support", "verified", 
    "verified_user", "book_2", "upload_file", "description", "close", "monitoring", "info", "security"
]

def restore_icons(content):
    # If we find an icon name inside a <span> that doesn't have the class, restore it
    # We also look for those text names just floating in tags if they were stripped entirely
    for icon in icon_names:
        # Match <span ...>icon</span> and fix the class if missing or if it's nested
        # Also match >icon< where icon might have been left bare
        # Restore Material Symbols outlined class
        content = content.replace(f'>{icon}<', f'><span class="material-symbols-outlined">{icon}</span><')
        # Clean up double spans if they were created
        content = content.replace(f'class="material-symbols-outlined"><span class="material-symbols-outlined">{icon}</span>', f'class="material-symbols-outlined">{icon}')
    return content

def safe_clean(content):
    # Only remove spans that have data-i18n to avoid breaking icons or layout spans
    content = re.sub(r'<span data-i18n="[^"]+">(.*?)</span>', r'\1', content)
    # Also clean up any empty spans or nested spans created by previous runs
    content = re.sub(r'<span\s*>(.*?)</span>', r'\1', content)
    return content

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Safe Clean
    content = safe_clean(content)
    
    # 2. Restore Icons
    content = restore_icons(content)

    # 3. Tag Text Nodes
    # Sort by length descending
    sorted_texts = sorted(text_map.keys(), key=len, reverse=True)
    for text in sorted_texts:
        key = text_map[text]
        pattern = rf'>\s*{re.escape(text)}\s*<'
        replacement = f'><span data-i18n="{key}">{text}</span><'
        content = re.sub(pattern, replacement, content)

    # 4. Tag Placeholders
    for text, key in placeholder_map.items():
        pattern = rf'placeholder="{re.escape(text)}"'
        replacement = f'placeholder="{text}" data-i18n-placeholder="{key}"'
        content = content.replace(pattern, replacement)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Fixed recovery and applied localization to {len(html_files)} files.")
