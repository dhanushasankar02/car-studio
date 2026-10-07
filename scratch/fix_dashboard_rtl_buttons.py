import glob

# 1. Update dashboard.html
with open('dashboard.html', 'r', encoding='utf-8') as f:
    db_content = f.read()

if 'id="rtlBtn"' not in db_content:
    db_content = db_content.replace(
        '<button class="ctrl-btn" id="dbThemeToggle">',
        '''<button class="ctrl-btn" id="rtlBtn" style="margin-bottom: 0.5rem; justify-content: space-between;">
                <span id="rtlLabel">RTL Layout</span>
                <i class="fas fa-right-left" id="rtlIcon"></i>
            </button>\n            <button class="ctrl-btn" id="dbThemeToggle">'''
    )
    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(db_content)
    print("Added rtlBtn to dashboard.html")

# 2. Update admin-dashboard.html
with open('admin-dashboard.html', 'r', encoding='utf-8') as f:
    adm_content = f.read()

if 'id="rtlBtn"' not in adm_content:
    adm_content = adm_content.replace(
        '<button class="ctrl-btn" id="adminThemeToggle">',
        '''<button class="ctrl-btn" id="rtlBtn" style="margin-bottom: 0.5rem; justify-content: space-between;">
                <span id="rtlLabel">RTL Layout</span>
                <i class="fas fa-right-left" id="rtlIcon"></i>
            </button>\n            <button class="ctrl-btn" id="adminThemeToggle">'''
    )
    with open('admin-dashboard.html', 'w', encoding='utf-8') as f:
        f.write(adm_content)
    print("Added rtlBtn to admin-dashboard.html")
