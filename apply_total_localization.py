import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# Massive mapping for all dashboard and scanner elements
text_map = {
    # Dashboard Hero
    "Deep Inspection": "dash_title",
    "Advanced heuristic analysis for mission-critical mail protection.": "dash_subtitle",
    "Engine Status": "dash_engine_status",
    "Optimal Security": "dash_optimal_security",
    
    # Dashboard Cards
    "Heuristic Health": "dash_heuristic_health",
    "HEURISTIC HEALTH": "dash_heuristic_health",
    "Active Threats": "dash_active_threats",
    "ACTIVE THREATS": "dash_active_threats",
    "Sensor Load": "dash_sensor_load",
    "SENSOR LOAD": "dash_sensor_load",
    "Honeypot Nodes": "dash_honeypot_nodes",
    "HONEYPOT NODES": "dash_honeypot_nodes",
    "ACTIVE": "dash_active",
    "NORMAL": "dash_normal",
    "12 nodes synchronized globally": "dash_nodes_sync",
    "No anomalies detected in last 24h": "dash_no_anomalies",
    
    # Scanner / Tabs
    "RAW INPUT": "tab_raw",
    "CARGA DE ARCHIVO": "tab_file",
    "EMAIL SOURCE CODE": "label_email_source",
    "Execute Scan": "btn_execute",
    "Clear": "btn_clear",
    "Awaiting Input": "status_awaiting",
    "System ready for raw payload analysis. Paste email source to begin diagnostic evaluation.": "status_ready",
    
    # Documentation
    "Master the Clinical Sentinel.": "doc_hero_title",
    "Knowledge Base": "doc_kb",
    "Get Started": "doc_get_started",
    "API Specs": "doc_api_specs",
    
    # Status
    "System Status: Operational": "status_operational",
    "SYSTEM LIVE": "status_live",
    "All Systems Optimal": "status_all_optimal",
    "Threats Blocked": "status_blocked",
    "Last verified 2 hours ago by Sentinel Core Team.": "last_verified",
    
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
    "Paste raw email headers and body here...": "placeholder_headers",
    "Paste full email headers here for forensic analysis...": "placeholder_headers",
    "Your Name": "sup_placeholder_name",
    "vane@clinical.secure": "sup_placeholder_email",
    "Describe the behavior of the sentinel scanner...": "sup_placeholder_details",
    "••••••••••••": "placeholder_pwd",
    "you@clinical.secure": "placeholder_email"
}

def clean_html(content):
    # Wipe previous span wraps (even the ones without attributes) to avoid nesting
    content = re.sub(r'<span[^>]*>(.*?)</span>', r'\1', content)
    # Wipe old placeholder/value tags
    content = re.sub(r' data-i18n-placeholder="[^"]+"', '', content)
    content = re.sub(r' data-i18n-value="[^"]+"', '', content)
    return content

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean old tags (aggressive reset)
    content = clean_html(content)

    # 1. Tag text nodes
    sorted_texts = sorted(text_map.keys(), key=len, reverse=True)
    for text in sorted_texts:
        key = text_map[text]
        # Match strictly between tags e.g. >Text<
        # This prevents matching "Security" inside "Security Scan"
        pattern = rf'>\s*{re.escape(text)}\s*<'
        replacement = f'><span data-i18n="{key}">{text}</span><'
        content = re.sub(pattern, replacement, content)

    # 2. Tag placeholders
    for text, key in placeholder_map.items():
        pattern = rf'placeholder="{re.escape(text)}"'
        replacement = f'placeholder="{text}" data-i18n-placeholder="{key}"'
        content = content.replace(pattern, replacement)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Applied AGGRESSIVE 100% localization tagging to {len(html_files)} files.")
