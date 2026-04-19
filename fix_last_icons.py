import os, re

pattern = re.compile(
    r'(<span[^>]*?absolute[^>]*?left-0[^>]*?>)\s*\n?\s*alternate_email\s*\n?\s*(</span>)',
    re.DOTALL
)
replacement = r'\1\n                            <span class="material-symbols-outlined text-outline">alternate_email</span>\n                        \2'

for f in ['forgot-password.html', 'signup.html']:
    if not os.path.exists(f):
        print("Not found: " + f)
        continue
    content = open(f, 'r', encoding='utf-8').read()
    new = pattern.sub(replacement, content)
    if new != content:
        open(f, 'w', encoding='utf-8').write(new)
        print("Fixed: " + f)
    else:
        # Fallback: direct string replace
        new = content.replace(
            '>alternate_email<',
            '><span class="material-symbols-outlined text-outline">alternate_email</span><'
        )
        if new != content:
            open(f, 'w', encoding='utf-8').write(new)
            print("Fixed (fallback): " + f)
        else:
            print("No change needed: " + f)
