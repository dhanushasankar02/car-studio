import glob, re

NAVBAR_NOWRAP_CSS = """
/* ==========================================================================
   NAVBAR ONE-LINE SINGLE HORIZONTAL ROW & NO-WRAP FIX (SITE-WIDE)
   ========================================================================== */
.navbar, .nav-container, .nav-links, .nav-actions {
    flex-wrap: nowrap !important;
}

.nav-container {
    max-width: 1440px !important;
    padding: 0.65rem 1.5rem !important;
    gap: 0.8rem !important;
}

.nav-links {
    gap: 0.25rem !important;
}

.nav-link, .dropdown-item, .action-btn, .logo-area {
    white-space: nowrap !important;
    word-break: keep-all !important;
}

.nav-link {
    font-size: 0.92rem !important;
    padding: 0.5rem 0.85rem !important;
}

.nav-actions {
    gap: 0.5rem !important;
}

.action-btn {
    padding: 0.45rem 0.85rem !important;
    font-size: 0.88rem !important;
}

@media (max-width: 1200px) {
    .nav-link {
        font-size: 0.88rem !important;
        padding: 0.45rem 0.65rem !important;
    }
    .nav-container {
        padding: 0.6rem 1rem !important;
        gap: 0.5rem !important;
    }
}
"""

def get_navbar_html(active_page):
    return f"""    <!-- ==================== STICKY GLASS NAVBAR ==================== -->
    <header class="navbar" id="navbar">
        <div class="nav-container">
            <!-- Logo Area -->
            <a href="index.html" class="logo-area" aria-label="Car Studio Home">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 100" class="logo-svg" height="58">
                    <defs>
                        <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                            <stop offset="0%" stop-color="#FF6A1A"/>
                            <stop offset="100%" stop-color="#FF3800"/>
                        </linearGradient>
                        <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                            <stop offset="0%" stop-color="#FF6A1A"/>
                            <stop offset="100%" stop-color="#FFA066"/>
                        </linearGradient>
                    </defs>
                    <g transform="translate(10, 10)">
                        <rect x="0" y="0" width="80" height="80" rx="20" fill="url(#logoGrad)"/>
                        <path d="M18 54 L62 54 L56 42 L24 42 Z" fill="#FFFFFF"/>
                        <path d="M26 42 L35 26 L45 26 L54 42 Z" fill="#FFFFFF" opacity="0.88"/>
                        <circle cx="28" cy="54" r="5" fill="#12151C"/>
                        <circle cx="52" cy="54" r="5" fill="#12151C"/>
                    </g>
                    <text x="106" y="52" font-family="'Outfit', 'Inter', sans-serif" font-weight="900" font-size="32" fill="url(#textGrad)" letter-spacing="2">CAR STUDIO</text>
                    <text x="108" y="74" font-family="'Inter', sans-serif" font-weight="700" font-size="12" fill="var(--text-secondary)" letter-spacing="3.5">DETAILED &amp; CUSTOMS</text>
                </svg>
            </a>

            <!-- Navigation Links (One Line Horizontal Order) -->
            <ul class="nav-links">
                <li class="nav-item dropdown">
                    <a href="index.html" class="nav-link {'active' if active_page in ['index', 'home1', 'home2'] else ''}">
                        Home <i class="fas fa-chevron-down chevron"></i>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="index.html" class="dropdown-item"><i class="fas fa-layer-group"></i> Home 1</a></li>
                        <li><a href="home2.html" class="dropdown-item"><i class="fas fa-desktop"></i> Home 2</a></li>
                    </ul>
                </li>
                <li class="nav-item"><a href="services.html" class="nav-link {'active' if active_page == 'services' else ''}">Services</a></li>
                <li class="nav-item"><a href="gallery.html" class="nav-link {'active' if active_page == 'gallery' else ''}">Gallery</a></li>
                <li class="nav-item"><a href="packages.html" class="nav-link {'active' if active_page == 'packages' else ''}">Packages</a></li>
                <li class="nav-item"><a href="why-choose-us.html" class="nav-link {'active' if active_page == 'why' else ''}">Why Choose Us</a></li>
                <li class="nav-item"><a href="contact.html" class="nav-link {'active' if active_page == 'contact' else ''}">Contact</a></li>
                <li class="nav-item dropdown">
                    <a href="dashboard.html" class="nav-link {'active' if active_page in ['dashboard', 'admin-dashboard'] else ''}">
                        Dashboard <i class="fas fa-chevron-down chevron"></i>
                    </a>
                    <ul class="dropdown-menu">
                        <li><a href="dashboard.html" class="dropdown-item"><i class="fas fa-user-circle"></i> User Dashboard</a></li>
                        <li><a href="admin-dashboard.html" class="dropdown-item"><i class="fas fa-shield-alt"></i> Admin Dashboard</a></li>
                    </ul>
                </li>
            </ul>

            <!-- Right Side Controls (Dark Mode -> RTL -> Login -> Menu Toggle) -->
            <div class="nav-actions">
                <button class="action-btn" id="darkModeBtn" aria-label="Toggle Theme">
                    <i class="fas fa-moon" id="themeIcon"></i>
                    <span id="themeLabel">Dark</span>
                </button>

                <button class="action-btn" id="rtlBtn" aria-label="Toggle Layout Direction">
                    <i class="fas fa-right-left" id="rtlIcon"></i>
                    <span id="rtlLabel">RTL</span>
                </button>

                <button class="action-btn btn-login" id="loginModalBtn">
                    <i class="fas fa-lock"></i>
                    <span>Login</span>
                </button>

                <button class="menu-toggle" id="mobileToggleBtn" aria-label="Open Mobile Menu">
                    <i class="fas fa-bars"></i>
                </button>
            </div>
        </div>
    </header>"""

page_active_map = {
    'index.html': 'index',
    'home2.html': 'home2',
    'services.html': 'services',
    'gallery.html': 'gallery',
    'packages.html': 'packages',
    'why-choose-us.html': 'why',
    'contact.html': 'contact',
    'dashboard.html': 'dashboard',
    'admin-dashboard.html': 'admin-dashboard',
    'navbar.html': 'index'
}

for path, page_key in page_active_map.items():
    if not glob.glob(path):
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject No-Wrap CSS
    if 'NAVBAR ONE-LINE SINGLE HORIZONTAL ROW' not in content:
        content = content.replace('</style>', f'\n{NAVBAR_NOWRAP_CSS}\n</style>')

    # 2. Replace Header Navbar HTML
    if '<header class="navbar"' in content:
        content = re.sub(r'<header class="navbar".*?</header>', get_navbar_html(page_key), content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Fixed navbar one-line order in {path}")
