import glob, re

RTL_BTN_CSS = """
/* ==========================================================================
   RTL / LTR TOGGLE BUTTON STYLING (DARK MODE & LIGHT MODE COMPATIBLE)
   ========================================================================== */
#rtlBtn, #mobileRtlBtn {
    background: var(--card-bg) !important;
    border: 1px solid var(--border-light) !important;
    color: var(--text-primary) !important;
    font-size: 0.92rem !important;
    font-weight: 600 !important;
    font-family: inherit !important;
    padding: 0.5rem 1rem !important;
    border-radius: 50px !important;
    cursor: pointer !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
    transition: var(--transition-smooth) !important;
    box-shadow: var(--shadow-sm) !important;
}

#rtlBtn i, #mobileRtlBtn i {
    color: var(--accent) !important;
    font-size: 0.95rem !important;
}

#rtlBtn:hover, #mobileRtlBtn:hover {
    border-color: var(--accent) !important;
    background: rgba(255, 106, 26, 0.12) !important;
    color: var(--accent) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 16px var(--accent-glow) !important;
}

body.dark-mode #rtlBtn, body.dark-mode #mobileRtlBtn {
    background: var(--card-bg) !important;
    border-color: var(--border-light) !important;
    color: var(--text-primary) !important;
}

body.dark-mode #rtlBtn i, body.dark-mode #mobileRtlBtn i {
    color: var(--accent) !important;
}
"""

DESKTOP_RTL_BTN_HTML = """                <button class="action-btn" id="rtlBtn" aria-label="Toggle Layout Direction">
                    <i class="fas fa-right-left" id="rtlIcon"></i>
                    <span id="rtlLabel">RTL</span>
                </button>"""

MOBILE_RTL_BTN_HTML = """            <button class="action-btn" id="mobileRtlBtn">
                <i class="fas fa-right-left" id="mobileRtlIcon"></i>
                <span id="mobileRtlLabel">RTL Layout</span>
            </button>"""

JS_RTL_HANDLER = """
            // --- RTL / LTR TOGGLE HANDLER ---
            const rtlBtn = document.getElementById('rtlBtn');
            const mobileRtlBtn = document.getElementById('mobileRtlBtn');
            const rtlLabel = document.getElementById('rtlLabel');
            const mobileRtlLabel = document.getElementById('mobileRtlLabel');

            function updateRTLUI(isRtl) {
                const dir = isRtl ? 'rtl' : 'ltr';
                document.body.setAttribute('dir', dir);
                document.documentElement.setAttribute('dir', dir);
                if (rtlLabel) rtlLabel.textContent = isRtl ? 'LTR' : 'RTL';
                if (mobileRtlLabel) mobileRtlLabel.textContent = isRtl ? 'LTR Layout' : 'RTL Layout';
                localStorage.setItem('carstudio_rtl', dir);
            }

            function toggleRTL() {
                const isRtl = (document.body.getAttribute('dir') || 'ltr') === 'ltr';
                updateRTLUI(isRtl);
            }

            const savedRtl = localStorage.getItem('carstudio_rtl');
            if (savedRtl === 'rtl') {
                updateRTLUI(true);
            } else {
                updateRTLUI(false);
            }

            if (rtlBtn) rtlBtn.addEventListener('click', toggleRTL);
            if (mobileRtlBtn) mobileRtlBtn.addEventListener('click', toggleRTL);
"""

for path in sorted(glob.glob('*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. CSS Injection before </style>
    if 'RTL / LTR TOGGLE BUTTON STYLING' not in content:
        content = content.replace('</style>', f'\n{RTL_BTN_CSS}\n</style>')

    # 2. HTML Injection in desktop nav-actions
    if 'id="rtlBtn"' not in content:
        # Insert after darkModeBtn button
        content = re.sub(
            r'(<button class="action-btn" id="darkModeBtn"[^>]*>.*?</button>)',
            r'\1\n' + DESKTOP_RTL_BTN_HTML,
            content,
            flags=re.DOTALL
        )

    # 3. HTML Injection in mobile-actions
    if 'id="mobileRtlBtn"' not in content:
        # Insert before mobileDarkBtn or mobileLoginModalBtn
        if 'id="mobileDarkBtn"' in content:
            content = re.sub(
                r'(<button class="action-btn" id="mobileDarkBtn"[^>]*>.*?</button>)',
                r'\1\n' + MOBILE_RTL_BTN_HTML,
                content,
                flags=re.DOTALL
            )
        elif '<div class="mobile-actions">' in content:
            content = content.replace('<div class="mobile-actions">', '<div class="mobile-actions">\n' + MOBILE_RTL_BTN_HTML)

    # 4. JS Handler Injection before </body>
    if 'RTL / LTR TOGGLE HANDLER' not in content:
        if 'updateRTLUI' in content:
            # Replace existing updateRTLUI logic with full toggle handler
            content = re.sub(
                r'function updateRTLUI\(isRtl\)\s*\{.*?\}(\s*if\s*\(rtlBtn\).*?;\s*)?',
                '',
                content,
                flags=re.DOTALL
            )
        content = content.replace('</script>', f'{JS_RTL_HANDLER}\n    </script>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Added RTL/LTR Toggle Button to {path}")
