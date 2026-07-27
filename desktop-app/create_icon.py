from PIL import Image, ImageDraw, ImageFilter
import math

size = 1024

# Background: Morandi blue (#5B7B92)
img = Image.new('RGBA', (size, size), (91, 123, 146, 255))
draw = ImageDraw.Draw(img)

# Draw a large circle with lighter Morandi blue (#A8C0CE)
center = size // 2
draw.ellipse([center-330, center-330, center+330, center+330], fill=(168, 192, 206, 255))

# Draw wave lines (representing 湛蓝 / deep blue waves)
for i, y_off in enumerate([-60, -10, 40, 90]):
    pts = []
    for x in range(center - 280, center + 281, 2):
        y = center + y_off + 30 * math.sin((x - center) * 0.016 + i * 0.5)
        pts.append((x, y))
    alpha = 200 - i * 30
    width = 8 - i
    for j in range(len(pts) - 1):
        draw.line([pts[j], pts[j+1]], fill=(255, 255, 255, alpha), width=max(width, 3))

# Add subtle inner shadow on the circle edge
for r in range(330, 310, -1):
    alpha = int((330 - r) * 25)
    draw.ellipse([center-r, center-r, center+r, center+r], outline=(91, 123, 146, alpha), width=1)

# Slight blur for smoothness
img = img.filter(ImageFilter.GaussianBlur(radius=0.5))

img.save('/Users/shixueming/WorkBuddy/2026-07-27-20-15-51/desktop-app/icon_1024.png')
print('Icon generated: icon_1024.png')
