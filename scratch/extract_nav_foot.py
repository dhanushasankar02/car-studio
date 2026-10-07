import re

with open(r'f:\groww\car  studio\index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Extract Navbar CSS & HTML
head_css = index_html.split('<style>')[1].split('</style>')[0]

# Extract Header & Mobile Panel HTML
header_html = re.search(r'(<header class="navbar" id="navbar">.*?</div\s*>\s*</div\s*>)', index_html, re.DOTALL).group(1)

# Extract Footer HTML
footer_html = re.search(r'(<footer class="footer" id="footer">.*?</footer>)', index_html, re.DOTALL).group(1)

# Extract Login Modal HTML
login_modal_html = re.search(r'(<div class="modal-overlay" id="loginModal">.*?</div>\s*</div>)', index_html, re.DOTALL).group(1)

# Extract JS script from index.html
js_content = index_html.split('<script>')[1].split('</script>')[0]

print("Header extracted length:", len(header_html))
print("Footer extracted length:", len(footer_html))
print("Login Modal extracted length:", len(login_modal_html))
