import glob, re

RTL_DARKMODE_CSS = """
/* ==========================================================================
   ULTRA-PRECISION RTL & DARK MODE ICON & LAYOUT ENGINE (SITE-WIDE)
   ========================================================================== */
/* 1. Universal RTL Icon Horizontal Flip */
[dir="rtl"] .fa-angle-right,
[dir="rtl"] .fa-arrow-right,
[dir="rtl"] .fa-chevron-right,
[dir="rtl"] .fa-chevron-left,
[dir="rtl"] .fa-angle-double-right,
[dir="rtl"] .fa-arrow-left,
[dir="rtl"] .fa-angle-left,
[dir="rtl"] .fa-arrow-right-long,
[dir="rtl"] .fa-arrow-left-long,
[dir="rtl"] .fa-long-arrow-alt-right,
[dir="rtl"] .fa-long-arrow-alt-left,
[dir="rtl"] .fa-caret-right,
[dir="rtl"] .fa-caret-left,
[dir="rtl"] .fa-arrow-circle-right,
[dir="rtl"] .fa-arrow-circle-left,
[dir="rtl"] .fa-paper-plane,
[dir="rtl"] .fa-right-to-bracket,
[dir="rtl"] .fa-left-to-bracket,
[dir="rtl"] .fa-external-link-alt,
[dir="rtl"] .fa-arrow-up-right-from-square,
[dir="rtl"] .footer-link i.fa-chevron-right,
html[dir="rtl"] .fa-angle-right,
html[dir="rtl"] .fa-arrow-right,
html[dir="rtl"] .fa-chevron-right,
html[dir="rtl"] .fa-chevron-left,
html[dir="rtl"] .fa-angle-double-right,
html[dir="rtl"] .fa-arrow-left,
html[dir="rtl"] .fa-angle-left,
html[dir="rtl"] .footer-link i.fa-chevron-right,
body[dir="rtl"] .fa-angle-right,
body[dir="rtl"] .fa-arrow-right,
body[dir="rtl"] .fa-chevron-right,
body[dir="rtl"] .fa-chevron-left,
body[dir="rtl"] .fa-angle-double-right,
body[dir="rtl"] .fa-arrow-left,
body[dir="rtl"] .fa-angle-left,
body[dir="rtl"] .footer-link i.fa-chevron-right {
    transform: scaleX(-1) !important;
    display: inline-block !important;
}

/* 2. RTL Text Alignment & Layout Adjustments */
[dir="rtl"] {
    text-align: right;
}

[dir="rtl"] .navbar,
[dir="rtl"] .nav-container,
[dir="rtl"] .footer,
[dir="rtl"] .footer-container,
[dir="rtl"] .section-header,
[dir="rtl"] .section-title,
[dir="rtl"] .section-desc,
[dir="rtl"] .hero-text-box,
[dir="rtl"] .footer-bottom {
    text-align: right;
}

[dir="rtl"] .dropdown-menu {
    left: auto !important;
    right: 0 !important;
}

[dir="rtl"] .dropdown-item:hover,
[dir="rtl"] .footer-link:hover,
[dir="rtl"] .protocol-step-item:hover,
[dir="rtl"] .step-nav-card:hover {
    transform: translateX(-4px) !important;
}

[dir="rtl"] .mobile-panel {
    right: auto !important;
    left: -380px !important;
    border-left: none !important;
    border-right: 1px solid var(--border-light) !important;
    transition: left 0.35s cubic-bezier(0.2, 0.9, 0.4, 1.1) !important;
}

[dir="rtl"] .mobile-panel.active {
    left: 0 !important;
    right: auto !important;
}

[dir="rtl"] .modal-close,
[dir="rtl"] .close-drawer-btn,
[dir="rtl"] .modal-close-btn {
    right: auto !important;
    left: 20px !important;
}

[dir="rtl"] .step-num,
[dir="rtl"] .service-card-badge {
    right: auto !important;
    left: 1.2rem !important;
}

/* 3. RTL Icons in Dark Mode Explicit Inversion & High Contrast Fix */
body.dark-mode[dir="rtl"] i,
body.dark-mode [dir="rtl"] i,
html[dir="rtl"] body.dark-mode i,
.dark-mode[dir="rtl"] .social-btn i,
.dark-mode[dir="rtl"] .footer-link i,
.dark-mode[dir="rtl"] .action-btn i,
.dark-mode[dir="rtl"] .btn-login i,
.dark-mode[dir="rtl"] .dropdown-item i {
    opacity: 1 !important;
}

/* 4. RTL Button & Input Flex Direction & Icon Margins */
[dir="rtl"] .action-btn,
[dir="rtl"] .btn-login,
[dir="rtl"] .dropdown-item,
[dir="rtl"] .footer-link,
[dir="rtl"] .mobile-nav-link,
[dir="rtl"] .mobile-sublink {
    flex-direction: row;
}

[dir="rtl"] .action-btn i,
[dir="rtl"] .btn-login i,
[dir="rtl"] .dropdown-item i,
[dir="rtl"] .footer-link i {
    margin-right: 0;
    margin-left: 6px;
}
"""

for path in sorted(glob.glob('*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject or update CSS block before </style>
    if 'ULTRA-PRECISION RTL & DARK MODE ICON & LAYOUT ENGINE' not in content:
        content = content.replace('</style>', f'\n{RTL_DARKMODE_CSS}\n</style>')

    # 2. Update updateRTLUI in JavaScript if present to set dir on both body and html
    if 'function updateRTLUI' in content:
        content = re.sub(
            r'function updateRTLUI\(isRtl\)\s*\{[^}]*\}',
            '''function updateRTLUI(isRtl) {
                const dir = isRtl ? 'rtl' : 'ltr';
                document.body.setAttribute('dir', dir);
                document.documentElement.setAttribute('dir', dir);
                if (rtlLabel) rtlLabel.textContent = isRtl ? 'LTR' : 'RTL';
                const mobileRtlLabel = document.getElementById('mobileRtlLabel');
                if (mobileRtlLabel) mobileRtlLabel.textContent = isRtl ? 'LTR Layout' : 'RTL Layout';
                localStorage.setItem('carstudio_rtl', dir);
            }''',
            content,
            flags=re.DOTALL
        )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Applied RTL & Dark Mode Icon Engine to {path}")
