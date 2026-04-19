import os
import re

def extract_strings():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    all_strings = set()
    content_regex = re.compile(r'>\s*([^<>\n\r\t&]+)\s*<')

    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            matches = content_regex.finditer(content)
            for match in matches:
                text = match.group(1).strip()
                if len(text) > 2:
                    all_strings.add(text)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    sorted_strings = sorted(list(all_strings))
    with open('all_strings.txt', 'w', encoding='utf-8') as f:
        for s in sorted_strings:
            f.write(s + '\n')
    print(f"Extracted {len(sorted_strings)} unique strings.")

if __name__ == "__main__":
    extract_strings()
