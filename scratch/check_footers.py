import glob, re

with open('index.html', 'r', encoding='utf-8') as f:
    ref_content = f.read()

ref_match = re.search(r'<footer class="footer" id="footer">.*?</footer>', ref_content, re.DOTALL)
ref_footer = ref_match.group(0).strip() if ref_match else ""

print("Reference footer found. Length:", len(ref_footer))

for path in sorted(glob.glob('*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'<footer class="footer" id="footer">.*?</footer>', c, re.DOTALL)
    if m:
        same = (m.group(0).strip() == ref_footer)
        print(f"{path}: footer found, matches reference: {same}")
    else:
        print(f"{path}: NO standard footer matching id='footer'")
