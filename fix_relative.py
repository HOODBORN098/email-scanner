import os
import re

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
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        def add_relative(m):
            cls = m.group(1)
            if 'relative' not in cls:
                cls += ' relative'
            if 'w-full' not in cls and 'max-w' not in cls:
                cls += ' w-full'
            return f'<main class="{cls.strip()}">'
            
        content = re.sub(r'<main[^>]*class="([^"]*)"[^>]*>', add_relative, content)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed relative positioning for {f}")
    except Exception as e:
        print(f"Failed {f}: {e}")
