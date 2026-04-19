import os, re

icons = [
    'shield_with_heart','book_2','filter_list','download_for_offline',
    'folder_zip','alternate_email','shield','public','gpp_maybe',
    'history_toggle_off','filter_alt','folder_open','arrow_forward'
]

print("=== Raw icon names still in body ===")
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    content = open(f, 'r', encoding='utf-8').read()
    for icon in icons:
        # Simple check: icon name appears as text NOT preceded by material-symbols-outlined">
        occurrences = []
        for m in re.finditer(r'>(\s*)(' + re.escape(icon) + r')(\s*)<', content):
            start = m.start()
            preceding = content[max(0, start-40):start]
            if 'material-symbols-outlined' not in preceding:
                occurrences.append(m.group(2))
        if occurrences:
            print("  " + f + ": " + icon + " (" + str(len(occurrences)) + "x)")

print()
print("=== Pages missing i18n.js ===")
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    content = open(f, 'r', encoding='utf-8').read()
    if 'i18n.js' not in content:
        print("  MISSING: " + f)

print()
print("=== Pages missing language toggle button ===")
for f in sorted(os.listdir('.')):
    if not f.endswith('.html'):
        continue
    content = open(f, 'r', encoding='utf-8').read()
    if 'data-lang' not in content:
        print("  NO TOGGLE: " + f)
