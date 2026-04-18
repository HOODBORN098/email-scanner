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

        # Remove the weird extra closing tag in threat feed
        content = re.sub(r'</div>\s*<div id="nav-auth-area"(.*?)</div>\s*</header>', '', content, flags=re.DOTALL)
        
        # Clean up any previously injected wrappers to start fresh
        content = re.sub(r'<!-- ===== MAIN CONTENT WRAPPER ===== -->\s*<div class="lg:pl-64">', '', content)
        content = re.sub(r'<!-- ===== MAIN CONTENT WRAPPER ===== -->\s*<div[^>]*>', '', content)
        
        # We also need to strip any closing div we previously injected
        # The script is right before </body>. We injected </div>\n<script>\n    document.addEventListener
        # Let's remove the </div> right before <script>    document.addEventListener('DOMContentLoaded', () => { // Active Nav Logic
        content = re.sub(r'</div>\s*(?=<script>\s*document\.addEventListener\(\'DOMContentLoaded\', \(\) => \{\s*// Active Nav Logic)', '', content)
        content = re.sub(r'</div>\s*(?=\n<script>\n\s*document\.addEventListener)', '', content)
        # Handle the one I injected via update_nav.py previously if it exists.

        # Simplify <main> tags. Remove `lg:pl-64`, `pt-20`, `lg:pt-10`, `pb-24`, `lg:pb-10`, `ml-72`, `lg:ml-72`, `pt-16`, `lg:pt-0`, `lg:pb-0`
        def clean_main_class(match):
            cls = match.group(1)
            # define items to strip
            strip_items = ['lg:pl-64', 'pt-20', 'lg:pt-10', 'pb-24', 'lg:pb-10', 'ml-72', 'lg:ml-72', 'pt-16', 'lg:pt-0', 'lg:pb-0', 'pt-24', 'pb-12']
            for item in strip_items:
                # remove exact word matches
                cls = re.sub(r'\b' + re.escape(item) + r'\b', '', cls)
            # extra cleanup spaces
            cls = re.sub(r'\s+', ' ', cls).strip()
            return f'<main class="{cls}">'
        content = re.sub(r'<main[^>]*class="([^"]*)"[^>]*>', clean_main_class, content)

        # Now: wrap main with the unified layout wrapper.
        # find `<main ` and replace with the wrapper opening
        # Also need to close the wrapper right before the script block.
        # But wait, my script block is at the very end of the body.
        # Let's just wrap `<main`...
        
        replacement = '<!-- ===== MAIN CONTENT WRAPPER ===== -->\n<div class="lg:pl-64 pt-24 lg:pt-12 pb-24 lg:pb-8 flex flex-col min-h-screen max-w-[100vw] overflow-x-hidden">\n<main'
        content = re.sub(r'<main', replacement, content, count=1)
        
        # close it just before the unified script
        unified_script_start = r'<script>\s*document\.addEventListener\(\'DOMContentLoaded\''
        content = re.sub(f'({unified_script_start})', r'</div>\n\1', content, count=1)
        
        # Note: By doing max-w-[100vw] and overflow-x-hidden, we ensure no horizontal scroll if something stretches.
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Fixed layout logic for {f}")
    except Exception as e:
        print(f"Failed {f}: {e}")
