import glob, re

for path in sorted(glob.glob('*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    css_blocks = re.findall(r'<style>(.*?)</style>', content, re.DOTALL)
    for idx, css in enumerate(css_blocks):
        open_b = css.count('{')
        close_b = css.count('}')
        diff = open_b - close_b
        if diff != 0:
            print(f"ERROR: {path} style block {idx} brace mismatch: open={open_b}, close={close_b}, diff={diff}")
        else:
            print(f"OK: {path} style block {idx} braces balanced ({open_b} pairs)")

    has_rtl_engine = 'ULTRA-PRECISION RTL & DARK MODE ICON & LAYOUT ENGINE' in content
    print(f"  -> {path}: RTL Dark Mode Engine injected: {has_rtl_engine}")
