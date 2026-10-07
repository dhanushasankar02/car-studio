import os
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

output_dir = r"f:\groww\car  studio\images"
os.makedirs(output_dir, exist_ok=True)

# Colors
BG_DARK = (14, 18, 27)
BG_CARD = (20, 26, 38)
ACCENT_ORANGE = (255, 106, 26)
ACCENT_BLUE = (0, 184, 217)
TEXT_WHITE = (248, 250, 252)
TEXT_MUTED = (148, 163, 184)
BORDER_COLOR = (40, 50, 70)

def draw_gradient_background(draw, width, height, color1, color2):
    for y in range(height):
        r = int(color1[0] + (color2[0] - color1[0]) * (y / height))
        g = int(color1[1] + (color2[1] - color1[1]) * (y / height))
        b = int(color1[2] + (color2[2] - color1[2]) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def create_image(filename_base, title, subtitle, icon_type):
    width, height = 1200, 675
    img = Image.new("RGB", (width, height), BG_DARK)
    draw = ImageDraw.Draw(img)
    
    # Background gradient & grid lines
    draw_gradient_background(draw, width, height, (8, 10, 15), (20, 26, 38))
    
    # Grid pattern for futuristic tech studio feel
    for x in range(0, width, 60):
        draw.line([(x, 0), (x, height)], fill=(255, 255, 255, 8), width=1)
    for y in range(0, height, 60):
        draw.line([(0, y), (width, y)], fill=(255, 255, 255, 8), width=1)
        
    # Draw glowing accent shape/circle in background
    for r in range(250, 0, -5):
        alpha = int(20 * (1 - r / 250))
        draw.ellipse([width - 350 - r, 100 - r, width - 350 + r, 100 + r], fill=(255, 106, 26, alpha))

    # Inner decorative frame card
    pad = 40
    draw.rounded_rectangle([pad, pad, width - pad, height - pad], radius=24, outline=BORDER_COLOR, width=2)
    
    # Badge tag
    draw.rounded_rectangle([pad + 30, pad + 30, pad + 260, pad + 70], radius=50, fill=ACCENT_ORANGE)
    draw.text((pad + 50, pad + 42), "CAR STUDIO SERVICES", fill=(255, 255, 255))
    
    # Title & Subtitle text
    draw.text((pad + 30, pad + 100), title, fill=TEXT_WHITE)
    draw.text((pad + 30, pad + 170), subtitle, fill=TEXT_MUTED)
    
    # Draw central stylized icon/illustration based on icon_type
    cx, cy = width - 280, height // 2 + 30
    if icon_type == "shield":
        # Shield shape
        pts = [(cx, cy - 120), (cx + 100, cy - 80), (cx + 100, cy + 40), (cx, cy + 120), (cx - 100, cy + 40), (cx - 100, cy - 80)]
        draw.polygon(pts, fill=(30, 40, 60), outline=ACCENT_ORANGE, width=6)
        draw.polygon([(cx, cy - 80), (cx + 60, cy - 50), (cx + 60, cy + 30), (cx, cy + 80), (cx - 60, cy + 30), (cx - 60, cy - 50)], fill=ACCENT_ORANGE)
    elif icon_type == "car":
        # Car silhouette styling
        draw.rounded_rectangle([cx - 140, cy - 30, cx + 140, cy + 50], radius=15, fill=(30, 40, 60), outline=ACCENT_ORANGE, width=4)
        draw.ellipse([cx - 100, cy + 20, cx - 40, cy + 80], fill=ACCENT_ORANGE)
        draw.ellipse([cx + 40, cy + 20, cx + 100, cy + 80], fill=ACCENT_ORANGE)
        draw.polygon([(cx - 90, cy - 30), (cx - 40, cy - 80), (cx + 40, cy - 80), (cx + 90, cy - 30)], fill=(40, 50, 75), outline=ACCENT_BLUE, width=3)
    elif icon_type == "sparkle":
        # Diamond / Polish Sparkle
        for i in range(4):
            ang = i * (math.pi / 2)
            dx = int(120 * math.cos(ang))
            dy = int(120 * math.sin(ang))
            draw.line([(cx, cy), (cx + dx, cy + dy)], fill=ACCENT_ORANGE, width=8)
        draw.ellipse([cx - 40, cy - 40, cx + 40, cy + 40], fill=ACCENT_BLUE)
    elif icon_type == "workflow":
        # Process nodes
        for i in range(3):
            nx = cx - 120 + i * 120
            draw.ellipse([nx - 35, cy - 35, nx + 35, cy + 35], fill=ACCENT_ORANGE if i==1 else BG_CARD, outline=ACCENT_ORANGE, width=4)
            if i < 2:
                draw.line([(nx + 35, cy), (nx + 85, cy)], fill=TEXT_MUTED, width=4)
    elif icon_type == "calculator":
        # Calculator / Meter visual
        draw.rounded_rectangle([cx - 100, cy - 90, cx + 100, cy + 90], radius=16, fill=(30, 40, 60), outline=ACCENT_BLUE, width=4)
        draw.rectangle([cx - 80, cy - 70, cx + 80, cy - 30], fill=(10, 15, 25), outline=ACCENT_ORANGE, width=2)
        draw.ellipse([cx - 40, cy, cx + 40, cy + 60], fill=ACCENT_ORANGE)
    elif icon_type == "tech":
        # Nano molecure / grid
        for i in range(5):
            angle = i * (2 * math.pi / 5)
            nx = int(cx + 80 * math.cos(angle))
            ny = int(cy + 80 * math.sin(angle))
            draw.line([(cx, cy), (nx, ny)], fill=ACCENT_BLUE, width=3)
            draw.ellipse([nx - 18, ny - 18, nx + 18, ny + 18], fill=ACCENT_ORANGE)
        draw.ellipse([cx - 25, cy - 25, cx + 25, cy + 25], fill=TEXT_WHITE)
    elif icon_type == "check":
        # Quality check shield & checkmark
        draw.ellipse([cx - 80, cy - 80, cx + 80, cy + 80], fill=(30, 40, 60), outline=ACCENT_ORANGE, width=6)
        draw.line([(cx - 40, cy), (cx - 10, cy + 30), (cx + 45, cy - 35)], fill=ACCENT_ORANGE, width=10)

    # Save JPG file
    jpg_path = os.path.join(output_dir, f"{filename_base}.jpg")
    img.save(jpg_path, "JPEG", quality=92)

    # Generate corresponding SVG file
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080a0f"/>
      <stop offset="100%" stop-color="#141a26"/>
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff6a1a"/>
      <stop offset="100%" stop-color="#ff924d"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="675" fill="url(#bgGrad)"/>
  <rect x="40" y="40" width="1120" height="595" rx="24" fill="none" stroke="#283246" stroke-width="2"/>
  <rect x="70" y="70" width="240" height="40" rx="20" fill="url(#accentGrad)"/>
  <text x="90" y="96" fill="#ffffff" font-family="Outfit, sans-serif" font-weight="700" font-size="16">CAR STUDIO SERVICES</text>
  <text x="70" y="160" fill="#f8fafc" font-family="Outfit, sans-serif" font-weight="800" font-size="34">{title}</text>
  <text x="70" y="210" fill="#94a3b8" font-family="Inter, sans-serif" font-weight="500" font-size="20">{subtitle}</text>
  <g transform="translate(900, 340)">
    <circle cx="0" cy="0" r="110" fill="rgba(255, 106, 26, 0.15)" stroke="#ff6a1a" stroke-width="4"/>
    <path d="M-30 0 L-10 25 L40 -30" fill="none" stroke="#ff6a1a" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
  </g>
</svg>'''
    svg_path = os.path.join(output_dir, f"{filename_base}.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

# Generate 13 Service Images
images_to_create = [
    ("services_hero", "Precision Automotive Detailing", "Master-Grade Services & Surface Preservation", "car"),
    ("service_paint_protection", "Ultra Paint Protection Film (PPF)", "Self-Healing Clear Armor & Hydrophobic Coating", "shield"),
    ("service_ceramic_coating", "9H Nano Ceramic Coating", "Mirror Shine & Permanent UV/Chemical Defense", "sparkle"),
    ("service_paint_correction", "Multi-Stage Paint Correction", "100% Swirl Removal & Depth Restoration", "sparkle"),
    ("service_interior_detailing", "Interior Spa & Leather Care", "Deep Sanitization & Premium Conditioning", "car"),
    ("service_custom_wraps", "Bespoke Vinyl Color Wraps", "Custom Finish & Satin/Gloss Transformations", "shield"),
    ("service_wheel_caliper", "Wheel & Caliper Refinishing", "High-Temp Ceramic Coat & Rim Restoration", "sparkle"),
    ("service_glass_ceramic", "Hydrophobic Glass Shield", "360 Weather-Proof & Crystal Rain Optics", "shield"),
    ("services_workflow", "5-Step Precision Workflow", "Decontamination, Correction & Curing Protocol", "workflow"),
    ("services_calculator", "Custom Service Estimator", "Interactive Pricing & Personal Plan Builder", "calculator"),
    ("services_technology", "Nanotechnology & Chemical Science", "Proprietary Formulations & Infrared Curing", "tech"),
    ("services_comparison", "Service Tier Matrix", "Compare Standard vs. Studio Grade Services", "shield"),
    ("services_assurance", "Certified Quality Guarantee", "Multi-Year Warranty & Comprehensive Care", "check"),
]

for base, title, sub, icon in images_to_create:
    create_image(base, title, sub, icon)
    print(f"Created {base}.jpg and {base}.svg")
