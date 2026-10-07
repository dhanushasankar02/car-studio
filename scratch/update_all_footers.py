import glob, re

# The unified 4-column footer CSS block
UNIFIED_FOOTER_CSS = """
/* ==========================================================================
   UNIFIED SITE-WIDE FOOTER STYLING (MATCHING EXACT CAR STUDIO DESIGN)
   ========================================================================== */
.footer {
    background: #080a0f !important;
    color: #f8fafc !important;
    padding: 4.5rem 2rem 2rem !important;
    border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
    margin-top: auto !important;
}

body:not(.dark-mode) .footer {
    background: #0f172a !important;
    color: #f8fafc !important;
}

.footer-container {
    max-width: 1400px !important;
    margin: 0 auto !important;
    display: grid !important;
    grid-template-columns: 2fr 1fr 1fr 1.5fr !important;
    gap: 3.5rem !important;
    margin-bottom: 3.5rem !important;
}

.footer-brand {
    display: flex !important;
    flex-direction: column !important;
    gap: 1.2rem !important;
}

.footer-desc {
    color: #94a3b8 !important;
    font-size: 0.95rem !important;
    line-height: 1.6 !important;
    margin-top: 0.5rem !important;
    margin-bottom: 1rem !important;
    max-width: 380px !important;
}

.social-links {
    display: flex !important;
    gap: 0.8rem !important;
}

.social-btn {
    width: 40px !important;
    height: 40px !important;
    border-radius: 50% !important;
    background: rgba(255, 255, 255, 0.06) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    color: #f8fafc !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-decoration: none !important;
    transition: var(--transition-smooth) !important;
}

.social-btn i {
    color: #f8fafc !important;
}

.social-btn:hover {
    background: var(--accent) !important;
    border-color: var(--accent) !important;
    color: #ffffff !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 4px 15px var(--accent-glow) !important;
}

.social-btn:hover i {
    color: #ffffff !important;
}

.footer-col h4 {
    font-family: var(--font-heading) !important;
    font-size: 1.15rem !important;
    font-weight: 700 !important;
    color: #ffffff !important;
    margin-bottom: 1.5rem !important;
}

.footer-links {
    list-style: none !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 0.8rem !important;
}

.footer-link {
    color: #94a3b8 !important;
    text-decoration: none !important;
    font-size: 0.95rem !important;
    transition: var(--transition-smooth) !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 8px !important;
}

.footer-link i {
    font-size: 0.75rem !important;
    color: var(--accent) !important;
}

.footer-link:hover {
    color: var(--accent) !important;
    transform: translateX(4px) !important;
}

body[dir="rtl"] .footer-link:hover {
    transform: translateX(-4px) !important;
}

.newsletter-form {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.8rem !important;
}

.newsletter-input {
    width: 100% !important;
    padding: 0.85rem 1.2rem !important;
    border-radius: 50px !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    background: rgba(255, 255, 255, 0.06) !important;
    color: #ffffff !important;
    outline: none !important;
    font-family: inherit !important;
    font-size: 0.9rem !important;
}

.newsletter-btn {
    background: var(--accent) !important;
    color: #ffffff !important;
    font-weight: 700 !important;
    border: none !important;
    padding: 0.85rem 1.5rem !important;
    border-radius: 50px !important;
    cursor: pointer !important;
    transition: var(--transition-smooth) !important;
    box-shadow: 0 4px 15px var(--accent-glow) !important;
}

.newsletter-btn:hover {
    background: var(--accent-hover) !important;
}

.footer-bottom {
    max-width: 1400px !important;
    margin: 0 auto !important;
    border-top: 1px solid rgba(255, 255, 255, 0.08) !important;
    padding-top: 1.8rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    flex-wrap: wrap !important;
    gap: 1rem !important;
    color: #94a3b8 !important;
    font-size: 0.9rem !important;
}

@media (max-width: 1024px) {
    .footer-container {
        grid-template-columns: 1fr 1fr !important;
        gap: 2.5rem !important;
    }
}

@media (max-width: 650px) {
    .footer-container {
        grid-template-columns: 1fr !important;
        gap: 2rem !important;
    }
    .footer-bottom {
        flex-direction: column !important;
        text-align: center !important;
    }
}
"""

UNIFIED_FOOTER_HTML = """    <!-- ==================== FOOTER ==================== -->
    <footer class="footer" id="footer">
        <div class="footer-container">
            <!-- Brand Column -->
            <div class="footer-brand">
                <a href="index.html" class="logo-area" aria-label="Car Studio Footer Logo">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 100" class="logo-svg" height="58">
                        <defs>
                            <linearGradient id="logoGradFoot" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#FF6A1A"/>
                                <stop offset="100%" stop-color="#FF3800"/>
                            </linearGradient>
                            <linearGradient id="textGradFoot" x1="0%" y1="0%" x2="100%" y2="0%">
                                <stop offset="0%" stop-color="#FF6A1A"/>
                                <stop offset="100%" stop-color="#FFA066"/>
                            </linearGradient>
                        </defs>
                        <g transform="translate(10, 10)">
                            <rect x="0" y="0" width="80" height="80" rx="20" fill="url(#logoGradFoot)"/>
                            <path d="M18 54 L62 54 L56 42 L24 42 Z" fill="#FFFFFF"/>
                            <path d="M26 42 L35 26 L45 26 L54 42 Z" fill="#FFFFFF" opacity="0.88"/>
                            <circle cx="28" cy="54" r="5" fill="#12151C"/>
                            <circle cx="52" cy="54" r="5" fill="#12151C"/>
                        </g>
                        <text x="106" y="52" font-family="'Outfit', 'Inter', sans-serif" font-weight="900" font-size="32" fill="url(#textGradFoot)" letter-spacing="2">CAR STUDIO</text>
                        <text x="108" y="74" font-family="'Inter', sans-serif" font-weight="700" font-size="12" fill="var(--text-secondary)" letter-spacing="3.5">DETAILED &amp; CUSTOMS</text>
                    </svg>
                </a>
                <p class="footer-desc">
                    Premium automotive detailing, custom wrapping, ceramic coating, and precision tuning studio for luxury vehicles.
                </p>
                <div class="social-links">
                    <a href="#" class="social-btn" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                    <a href="#" class="social-btn" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                    <a href="#" class="social-btn" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                    <a href="#" class="social-btn" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
                </div>
            </div>

            <!-- Quick Links -->
            <div class="footer-col">
                <h4>Quick Links</h4>
                <ul class="footer-links">
                    <li><a href="index.html" class="footer-link"><i class="fas fa-chevron-right"></i> Home 1</a></li>
                    <li><a href="home2.html" class="footer-link"><i class="fas fa-chevron-right"></i> Home 2</a></li>
                    <li><a href="services.html" class="footer-link"><i class="fas fa-chevron-right"></i> Services</a></li>
                    <li><a href="gallery.html" class="footer-link"><i class="fas fa-chevron-right"></i> Gallery</a></li>
                    <li><a href="packages.html" class="footer-link"><i class="fas fa-chevron-right"></i> Packages</a></li>
                </ul>
            </div>

            <!-- Dashboards & Info -->
            <div class="footer-col">
                <h4>Dashboards &amp; Info</h4>
                <ul class="footer-links">
                    <li><a href="dashboard.html" class="footer-link"><i class="fas fa-chevron-right"></i> User Dashboard</a></li>
                    <li><a href="admin-dashboard.html" class="footer-link"><i class="fas fa-chevron-right"></i> Admin Dashboard</a></li>
                    <li><a href="why-choose-us.html" class="footer-link"><i class="fas fa-chevron-right"></i> Why Choose Us</a></li>
                    <li><a href="contact.html" class="footer-link"><i class="fas fa-chevron-right"></i> Contact Us</a></li>
                    <li><a href="#" class="footer-link" id="footerLoginTrigger"><i class="fas fa-chevron-right"></i> Login Portal</a></li>
                </ul>
            </div>

            <!-- Newsletter Column -->
            <div class="footer-col">
                <h4>Newsletter</h4>
                <p style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 0.8rem;">
                    Subscribe for exclusive detailing packages and car care tips.
                </p>
                <form class="newsletter-form" id="newsletterForm">
                    <input type="email" placeholder="Enter your email" class="newsletter-input" required>
                    <button type="submit" class="newsletter-btn">Subscribe</button>
                </form>
            </div>
        </div>

        <!-- Footer Bottom -->
        <div class="footer-bottom">
            <p>&copy; 2026 Car Studio. All rights reserved.</p>
            <div style="display: flex; gap: 1.5rem;">
                <a href="#" class="footer-link" style="font-size: 0.88rem;">Privacy Policy</a>
                <a href="#" class="footer-link" style="font-size: 0.88rem;">Terms of Service</a>
                <a href="#" class="footer-link" style="font-size: 0.88rem;">Cookie Preferences</a>
            </div>
        </div>
    </footer>"""

for path in sorted(glob.glob('*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject CSS before </style> if UNIFIED_FOOTER_CSS is not present
    if 'UNIFIED SITE-WIDE FOOTER STYLING' not in content:
        content = content.replace('</style>', f'\n{UNIFIED_FOOTER_CSS}\n</style>')

    # 2. Replace or add footer HTML
    if '<footer' in content:
        content = re.sub(r'<footer[^>]*>.*?</footer>', UNIFIED_FOOTER_HTML, content, flags=re.DOTALL)
    else:
        # Insert before </body> or before <div class="modal-overlay" id="loginModal">
        if '<div class="modal-overlay"' in content:
            content = content.replace('<div class="modal-overlay"', f'{UNIFIED_FOOTER_HTML}\n\n    <div class="modal-overlay"')
        elif '</body>' in content:
            content = content.replace('</body>', f'{UNIFIED_FOOTER_HTML}\n</body>')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated footer CSS and HTML in {path}")
