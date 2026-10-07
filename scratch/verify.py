import os, re

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('Services HTML Size:', len(content), 'bytes')

imgs = set(re.findall(r'images/[a-zA-Z0-9_.-]+', content))
print('Images referenced:', len(imgs), imgs)
missing = [i for i in imgs if not os.path.exists(i)]
print('Missing images:', missing)

framers = re.findall(r'data-framer-section="([^"]+)"', content)
print('Framer sections:', len(framers), framers)
print('Navbar present:', 'id="navbar"' in content)
print('Footer present:', 'id="footer"' in content)
