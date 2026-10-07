import glob, re

for path in sorted(glob.glob('*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    rtl_matches = re.findall(r'\[dir=["\']rtl["\']\]', content)
    print(f"{path}: RTL selector count = {len(rtl_matches)}")
