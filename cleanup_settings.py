import codecs
import re

with codecs.open('settings account.html', 'r', 'utf-8') as f:
    content = f.read()

# No, let's just delete the exact block of SideNavBar Shell
old_sidebar_pattern = r'<!-- SideNavBar Shell -->\s*<aside class="hidden lg:flex h-screen w-72 fixed left-0 top-0.+?</aside>'
content = re.sub(old_sidebar_pattern, '', content, flags=re.DOTALL)

old_bottom_nav_pattern = r'<!-- BottomNavBar \(Mobile Only\) -->\s*<nav class="md:hidden fixed bottom-0 left-0 right-0.+?</nav>'
content = re.sub(old_bottom_nav_pattern, '', content, flags=re.DOTALL)

# There's an extra </nav> at the bottom.
content = re.sub(r'</nav>\s*(?=<script>\s*const logout =)', '', content, flags=re.DOTALL)

# Also remove <!-- TopNavBar Shell -->
content = content.replace('<!-- TopNavBar Shell -->', '')

with codecs.open('settings account.html', 'w', 'utf-8') as f:
    f.write(content)
