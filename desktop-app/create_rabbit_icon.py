#!/usr/bin/env python3
"""Generate a cute rabbit icon for the desktop app"""
from PIL import Image, ImageDraw
import math

SIZE = 1024
img = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

cx, cy = SIZE // 2, SIZE // 2

# === Background rounded square (Muddy blue gradient) ===
margin = 80
draw.rounded_rectangle(
    [margin, margin, SIZE - margin, SIZE - margin],
    radius=200,
    fill=(58, 97, 130, 255)
)

# === Rabbit ears ===
# Left ear (outer)
left_ear_x = cx - 130
draw.ellipse(
    [left_ear_x - 65, 180, left_ear_x + 65, 460],
    fill=(245, 245, 250, 255)
)
# Left ear inner
draw.ellipse(
    [left_ear_x - 35, 210, left_ear_x + 35, 420],
    fill=(255, 200, 215, 255)
)

# Right ear (outer)
right_ear_x = cx + 130
draw.ellipse(
    [right_ear_x - 65, 180, right_ear_x + 65, 460],
    fill=(245, 245, 250, 255)
)
# Right ear inner
draw.ellipse(
    [right_ear_x - 35, 210, right_ear_x + 35, 420],
    fill=(255, 200, 215, 255)
)

# === Rabbit head (big circle) ===
head_radius = 210
head_top = 350
draw.ellipse(
    [cx - head_radius, head_top, cx + head_radius, head_top + head_radius * 2],
    fill=(250, 250, 255, 255)
)

# === Blush cheeks ===
blush_y = head_top + 320
# Left blush
draw.ellipse(
    [cx - 170, blush_y, cx - 100, blush_y + 45],
    fill=(255, 180, 195, 200)
)
# Right blush
draw.ellipse(
    [cx + 100, blush_y, cx + 170, blush_y + 45],
    fill=(255, 180, 195, 200)
)

# === Eyes ===
eye_y = head_top + 180
eye_offset = 85
eye_size = 22

# Left eye
draw.ellipse(
    [cx - eye_offset - eye_size, eye_y - eye_size,
     cx - eye_offset + eye_size, eye_y + eye_size],
    fill=(45, 55, 70, 255)
)
# Left eye highlight
draw.ellipse(
    [cx - eye_offset - 8, eye_y - 12,
     cx - eye_offset + 8, eye_y - 2],
    fill=(255, 255, 255, 255)
)

# Right eye
draw.ellipse(
    [cx + eye_offset - eye_size, eye_y - eye_size,
     cx + eye_offset + eye_size, eye_y + eye_size],
    fill=(45, 55, 70, 255)
)
# Right eye highlight
draw.ellipse(
    [cx + eye_offset - 8, eye_y - 12,
     cx + eye_offset + 8, eye_y - 2],
    fill=(255, 255, 255, 255)
)

# === Nose (small pink triangle/heart) ===
nose_y = head_top + 250
nose_size = 18
draw.polygon(
    [(cx, nose_y + nose_size),
     (cx - nose_size, nose_y - nose_size // 2),
     (cx + nose_size, nose_y - nose_size // 2)],
    fill=(255, 150, 175, 255)
)

# === Mouth (small Y shape) ===
mouth_y = nose_y + nose_size + 5
draw.arc(
    [cx - 30, mouth_y, cx, mouth_y + 35],
    0, 180,
    fill=(180, 190, 200, 255),
    width=4
)
draw.arc(
    [cx, mouth_y, cx + 30, mouth_y + 35],
    0, 180,
    fill=(180, 190, 200, 255),
    width=4
)

# === Save ===
img.save('/Users/shixueming/WorkBuddy/2026-07-27-20-15-51/desktop-app/icon_1024.png')
print("Rabbit icon generated: icon_1024.png")
