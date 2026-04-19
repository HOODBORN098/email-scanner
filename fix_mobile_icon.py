import os, re

pattern = re.compile(
    r'(<div class="w-8 h-8 rounded-xl bg-primary flex items-center justify-center text-white shadow-md">)\s*\n?\s*shield_with_heart\s*\n?\s*(</div>)',
    re.DOTALL
)
replacement = r'\1\n            <span class="material-symbols-outlined">shield_with_heart</span>\n        \2'

for f in os.listdir('.'):
    if not f.endswith('.html'):
        continue
    content = open(f, 'r', encoding='utf-8').read()
    new = pattern.sub(replacement, content)
    if new != content:
        open(f, 'w', encoding='utf-8').write(new)
        print(f'Fixed mobile header in: {f}')

print('Done.')
