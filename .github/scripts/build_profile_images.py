"""Generate responsive profile images and the share card from a real photograph.

Run with Pillow installed: python3 .github/scripts/build_profile_images.py [photo.jpg]
An optional original photo replaces images/profile.jpg after resizing to 400 px.
No retouching or generative processing is applied.
"""
from pathlib import Path
import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps

root = Path(__file__).resolve().parents[2]
images = root / 'images'
source = Path(sys.argv[1]) if len(sys.argv) > 1 else images / 'profile.jpg'
photo = ImageOps.exif_transpose(Image.open(source)).convert('RGB')
photo = ImageOps.fit(photo, (400, 400), method=Image.Resampling.LANCZOS)
if len(sys.argv) > 1:
    photo.save(images / 'profile.jpg', quality=92, optimize=True)
for size in [128, 224, 352]:
    photo.resize((size, size), Image.Resampling.LANCZOS).save(images / f'profile-{size}.webp', quality=84, method=6)

# Render type at double resolution for crisp small previews.
scale = 2
card = Image.new('RGB', (1200 * scale, 630 * scale), 'white')
portrait = photo.resize((280 * scale, 280 * scale), Image.Resampling.LANCZOS)
mask = Image.new('L', portrait.size, 0)
ImageDraw.Draw(mask).ellipse((0, 0, portrait.width, portrait.height), fill=255)
card.paste(portrait, (80 * scale, 175 * scale), mask)
font_folder = Path('/System/Library/Fonts/Supplemental')
if font_folder.exists():
    bold = font_folder / 'Arial Bold.ttf'
    regular = font_folder / 'Arial.ttf'
else:
    bold = Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
    regular = bold.with_name('DejaVuSans.ttf')
draw = ImageDraw.Draw(card)
for text, y, size, font, color in [
    ('David Kreismann', 225, 64, bold, '#292d30'),
    ('M.Sc. RCI @ TUM', 322, 36, regular, '#50575b'),
    ('Working Student @ IBM', 371, 36, regular, '#50575b'),
]:
    draw.text((420 * scale, y * scale), text, font=ImageFont.truetype(str(font), size * scale), fill=color, anchor='lt')
card.resize((1200, 630), Image.Resampling.LANCZOS).save(images / 'og-image-v2.png', optimize=True)
