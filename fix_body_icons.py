import os, re

# All icon names used as raw text in the project body (not nav)
ICON_NAMES = [
    'shield_with_heart', 'book_2', 'filter_list', 'download_for_offline',
    'folder_zip', 'lock', 'visibility', 'shield', 'public', 'gpp_maybe',
    'gpp_good', 'verified_user', 'security', 'monitoring', 'history_toggle_off',
    'filter_alt', 'search', 'close', 'check_circle', 'warning', 'error',
    'info', 'verified', 'upload_file', 'description', 'attach_file',
    'arrow_forward', 'arrow_back', 'chevron_right', 'more_vert',
    'mail', 'inbox', 'send', 'drafts', 'mark_email_read', 'report',
    'autorenew', 'sync', 'refresh', 'tune', 'settings', 'help',
    'open_in_new', 'link', 'copy_all', 'content_copy', 'delete',
    'edit', 'save', 'print', 'download', 'upload', 'cloud_upload',
    'notifications', 'notifications_none', 'person', 'group',
    'badge', 'work', 'calendar_today', 'schedule', 'timelapse',
    'bar_chart', 'pie_chart', 'show_chart', 'timeline',
    'key', 'password', 'fingerprint', 'vpn_key', 'no_encryption',
    'encrypted', 'privacy_tip', 'policy', 'bug_report', 'code',
    'terminal', 'memory', 'dns', 'router', 'hub', 'lan', 'wifi',
    'cell_tower', 'satellite_alt', 'travel_explore', 'language',
    'dark_mode', 'light_mode', 'contrast', 'palette', 'format_paint',
    'star', 'star_border', 'favorite', 'favorite_border', 'thumb_up',
    'emoji_events', 'military_tech', 'workspace_premium',
]

# Pattern: matches a bare icon name that is the ONLY text content between > and <
# i.e. >icon_name< but NOT inside a material-symbols-outlined span already
def fix_bare_icons(content, icons):
    for icon in icons:
        # Match >\s*icon_name\s*< but only when NOT already inside a material-symbols span
        # Strategy: replace ">icon_name<" with proper span, but skip if already wrapped
        pattern = re.compile(r'(?<!material-symbols-outlined">)>(\s*)(' + re.escape(icon) + r')(\s*)<', re.MULTILINE)
        def replacer(m):
            before = m.group(1)
            name = m.group(2)
            after = m.group(3)
            return f'>{before}<span class="material-symbols-outlined">{name}</span>{after}<'
        content = pattern.sub(replacer, content)
    return content

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
fixed = []

for file in html_files:
    content = open(file, 'r', encoding='utf-8').read()
    original = content
    content = fix_bare_icons(content, ICON_NAMES)
    if content != original:
        open(file, 'w', encoding='utf-8').write(content)
        fixed.append(file)
        print(f'Fixed body icons in: {file}')

print(f'\nDone. Fixed {len(fixed)} files.')
