import glob

for path in sorted(glob.glob('*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    has_desktop = 'id="rtlBtn"' in c
    has_mobile = 'id="mobileRtlBtn"' in c
    print(f"{path}: desktop rtlBtn={has_desktop}, mobileRtlBtn={has_mobile}")
