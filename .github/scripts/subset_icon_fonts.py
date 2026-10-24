"""Optimize a built site: icon fonts, CSS, asset filenames and landing-page CSS.

Font Awesome and Academicons ship thousands of glyphs, but the site shows about
fifteen. This script scans the built HTML and JavaScript for `fa-*` and `ai-*`
class names, looks up their code points in the icon stylesheets and rewrites
each font file in place with only those glyphs. It also removes unused icon rules,
fingerprints shared assets and inlines the base CSS on the two homepages.
Run it after `jekyll build`:

    python3 .github/scripts/subset_icon_fonts.py _site
"""

import re
import sys
from pathlib import Path

from fontTools import subset

site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site")

# Class names used anywhere in the generated pages and scripts
used = set()
for path in list(site.rglob("*.html")) + list(site.rglob("*.js")):
    text = path.read_text(encoding="utf-8", errors="ignore")
    used.update(re.findall(r"\b((?:fa|ai)-[a-z0-9-]+)", text))

# Font Awesome 6: `.fa-github,.fa-alias{--fa:"<glyph>"}`
fa_css = (site / "assets/css/fontawesome.css").read_text(encoding="utf-8")
fa_codes = set()
for selectors, glyph in re.findall(r"((?:\.fa-[a-z0-9-]+,?)+)\{--fa:\"([^\"]+)\"", fa_css):
    names = {s.lstrip(".") for s in selectors.split(",")}
    if names & used:
        fa_codes.update(ord(c) for c in glyph)

# Academicons: `.ai-orcid:before {content: "\e9d9";}`
ai_css = (site / "assets/css/academicons.min.css").read_text(encoding="utf-8")
ai_codes = {
    int(code, 16)
    for name, code in re.findall(r"\.(ai-[a-z0-9-]+):before\s*\{\s*content:\s*\"\\([0-9a-f]+)\"", ai_css)
    if name in used
}

def shrink(font_path, codes):
    if not font_path.exists() or not codes:
        return
    before = font_path.stat().st_size
    options = subset.Options()
    options.flavor = {".woff2": "woff2", ".woff": "woff"}.get(font_path.suffix)
    options.layout_features = ["*"]
    font = subset.load_font(str(font_path), options)
    subsetter = subset.Subsetter(options)
    subsetter.populate(unicodes=codes)
    subsetter.subset(font)
    subset.save_font(font, str(font_path), options)
    print(f"{font_path.relative_to(site)}: {before // 1024} KB -> {font_path.stat().st_size // 1024} KB")

for name in ["fa-solid-900", "fa-brands-400", "fa-regular-400"]:
    for ext in [".woff2", ".ttf"]:
        shrink(site / "assets/webfonts" / f"{name}{ext}", fa_codes)

for ext in [".ttf", ".woff"]:
    shrink(site / "assets/fonts" / f"academicons{ext}", ai_codes)

print(f"kept {len(fa_codes)} Font Awesome and {len(ai_codes)} Academicons glyphs")

# Prefer WOFF2 for Academicons rather than downloading the larger TTF first.
from fontTools.ttLib import TTFont

academy = TTFont(site / 'assets/fonts/academicons.ttf')
academy.flavor = 'woff2'
academy.save(site / 'assets/fonts/academicons.woff2')

# Keep the shared icon helpers, but remove unused glyph selectors and aliases.
fa_rule = re.compile(r'((?:\.fa-[a-z0-9-]+,?)+)\{--fa:"([^"]+)";?\}')
def keep_fa_rule(match):
    selectors = [selector for selector in match[1].split(',') if selector.lstrip('.') in used]
    return ','.join(selectors) + '{--fa:"' + match[2] + '"}' if selectors else ''

fa_optimized = fa_rule.sub(keep_fa_rule, fa_css)
(site / 'assets/css/fontawesome.css').write_text(fa_optimized, encoding='utf-8')
ai_rule = re.compile(r'\.(ai-[a-z0-9-]+):before\s*\{[^{}]*\}')
ai_optimized = ai_rule.sub(lambda match: match[0] if match[1] in used else '', ai_css)
(site / 'assets/css/academicons.min.css').write_text(ai_optimized, encoding='utf-8')
print(f'icon CSS: {len((fa_css + ai_css).encode()):,} -> {len((fa_optimized + ai_optimized).encode()):,} bytes')

# Stable content-based filenames keep unchanged assets reusable across deployments.
import hashlib

replacements = []
for relative in ['assets/css/main.css', 'assets/css/fontawesome.css', 'assets/css/academicons.min.css', 'assets/js/main.min.js']:
    asset = site / relative
    digest = hashlib.sha256(asset.read_bytes()).hexdigest()[:12]
    fingerprinted = asset.with_name(f'{asset.stem}.{digest}{asset.suffix}')
    fingerprinted.write_bytes(asset.read_bytes())
    replacements.append(('/' + relative, '/' + str(fingerprinted.relative_to(site))))
for page in site.rglob('*.html'):
    html = page.read_text(encoding='utf-8')
    for original, versioned in replacements:
        html = re.sub(re.escape(original) + r'(?:\?v=\d+)?', versioned, html)
    page.write_text(html, encoding='utf-8')

# The two landing pages can paint without a separate render-blocking CSS request.
# Other pages keep the cacheable shared stylesheet for subsequent navigation.
main_css = (site / 'assets/css/main.css').read_text(encoding='utf-8')
for relative in ['index.html', 'de/index.html']:
    homepage = site / relative
    if homepage.exists():
        html = homepage.read_text(encoding='utf-8')
        html = re.sub(r'<link rel="stylesheet" href="[^"]*/assets/css/main\.[a-f0-9]+\.css">', lambda match: '<style>' + main_css + '</style>', html)
        homepage.write_text(html, encoding='utf-8')
