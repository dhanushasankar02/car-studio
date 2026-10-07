import os
import math
from PIL import Image, ImageDraw

output_dir = r"f:\groww\car  studio\images"

def draw_gradient(draw, width, height, c1, c2):
    for y in range(height):
        r = int(c1[0] + (c2[0] - c1[0]) * (y / height))
        g = int(c1[1] + (c2[1] - c1[1]) * (y / height))
        b = int(c1[2] + (c2[2] - c1[2]) * (y / height))
        draw.line([(0, y), (width, y)], fill=(r, g, b))

def make_sec_img(filename, title, subtitle, icon_mode):
    w, h = 1200, 675
    img = Image.new("RGB", (w, h), (14, 18, 27))
    draw = ImageDraw.Draw(img)
    
    draw_gradient(draw, w, h, (8, 10, 15), (20, 26, 38))
    
    # Neon grid lines
    for x in range(0, w, 50):
        draw.line([(x, 0), (x, h)], fill=(255, 106, 26, 12), width=1)
    for y in range(0, h, 50):
        draw.line([(0, y), (w, y)], fill=(255, 106, 26, 12), width=1)
        
    # Glow ring
    cx, cy = 900, 337
    for r in range(260, 0, -6):
        alpha = int(25 * (1 - r/260))
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(255, 106, 26, alpha))
        
    draw.rounded_rectangle([40, 40, w-40, h-40], radius=24, outline=(40, 50, 75), width=2)
    draw.rounded_rectangle([70, 70, 320, 115], radius=20, fill=(255, 106, 26))
    draw.text((90, 84), "CAR STUDIO MASTER", fill=(255, 255, 255))
    
    draw.text((70, 150), title, fill=(248, 250, 252))
    draw.text((70, 210), subtitle, fill=(148, 163, 184))
    
    # Graphic element
    if icon_mode == "interior":
        # Seat / Interior emblem
        draw.rounded_rectangle([cx-120, cy-100, cx+120, cy+100], radius=24, fill=(24, 32, 48), outline=(255, 106, 26), width=4)
        draw.line([(cx-80, cy-40), (cx+80, cy-40)], fill=(255, 106, 26), width=4)
        draw.line([(cx-80, cy), (cx+80, cy)], fill=(0, 184, 217), width=4)
        draw.line([(cx-80, cy+40), (cx+80, cy+40)], fill=(255, 106, 26), width=4)
    elif icon_mode == "wrap":
        # Palette / Vinyl roll
        draw.ellipse([cx-90, cy-90, cx+90, cy+90], fill=(24, 32, 48), outline=(0, 184, 217), width=6)
        draw.ellipse([cx-50, cy-50, cx+50, cy+50], fill=(255, 106, 26))
    elif icon_mode == "handover":
        # Trophy / Shield seal
        pts = [(cx, cy-110), (cx+90, cy-70), (cx+90, cy+40), (cx, cy+110), (cx-90, cy+40), (cx-90, cy-70)]
        draw.polygon(pts, fill=(24, 32, 48), outline=(255, 106, 26), width=5)
        draw.ellipse([cx-40, cy-40, cx+40, cy+40], fill=(255, 106, 26))

    img.save(os.path.join(output_dir, f"{filename}.jpg"), "JPEG", quality=95)
    print(f"Generated {filename}.jpg")

make_sec_img("services_sec4_gemini", "Executive Interior Spa & Sanitization", "180°C Hot Vapor & Leather Nourishment", "interior")
make_sec_img("services_sec5_gemini", "Bespoke Vinyl Wraps & Styling", "Satin, Matte & Custom Cast Transformations", "wrap")
make_sec_img("services_sec6_gemini", "Concierge Handover & Digital Passport", "100-Point Audit & Carfax Warranty Logging", "handover")
