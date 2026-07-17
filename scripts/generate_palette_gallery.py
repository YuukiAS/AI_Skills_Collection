#!/usr/bin/env python3
"""Generate a static HTML gallery for canonical scientific figure palettes."""

from __future__ import annotations

from html import escape
import json
from pathlib import Path

from palette_library import load_library


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "palette" / "gallery.html"
COLS4ALL = ROOT / "palette" / "external" / "cols4all-palettes.json"
NOTION_IMAGES = ROOT / "palette" / "notion-image-palettes.json"


def swatches(colors: list[str]) -> str:
    blocks = []
    for color in colors:
        blocks.append(
            f'<span class="swatch" title="{escape(color)}" '
            f'style="background:{escape(color)}"></span>'
        )
    return "".join(blocks)


def main() -> int:
    library = load_library()
    core_cards = []
    curated_cards = []
    for palette in library["palettes"]:
        disclaimer = palette.get("disclaimer", "")
        card = f"""
<section class="card">
  <div class="meta">
    <h2>{escape(palette['id'])}</h2>
    <span>{escape(palette['type'])}</span>
    <span>{len(palette['colors'])} colors</span>
    <span>{escape(palette['provenance_status'])}</span>
  </div>
  <div class="swatches">{swatches(palette['colors'])}</div>
  <p><strong>{escape(palette['name'])}</strong> · {escape(palette['family'])}</p>
  <p>{escape('; '.join(palette.get('recommended_for', [])[:3]))}</p>
  {f'<p class="disclaimer">{escape(disclaimer)}</p>' if disclaimer else ''}
</section>"""
        if palette.get("core"):
            core_cards.append(card)
        else:
            curated_cards.append(card)

    cols4all_cards = []
    if COLS4ALL.exists():
        cols4all = json.loads(COLS4ALL.read_text(encoding="utf-8"))
        for palette in cols4all.get("palettes", [])[:120]:
            disclaimer = f"GPL-3 external palette; source id {palette.get('source_id', '')}"
            cols4all_cards.append(
                f"""
<section class="card external">
  <div class="meta">
    <h2>{escape(palette['source_id'])}</h2>
    <span>{escape(palette['type'])}</span>
    <span>{len(palette['colors'])} colors</span>
    <span>{escape(palette.get('series', ''))}</span>
  </div>
  <div class="swatches">{swatches(palette['colors'])}</div>
  <p><strong>{escape(palette.get('name', palette['source_id']))}</strong></p>
  <p class="disclaimer">{escape(disclaimer)}</p>
</section>"""
            )

    notion_cards = []
    if NOTION_IMAGES.exists():
        notion = json.loads(NOTION_IMAGES.read_text(encoding="utf-8"))
        for page in notion.get("pages", []):
            first_colors = []
            if page.get("images"):
                first_colors = page["images"][0].get("primary_colors") or page["images"][0].get("visible_hex_colors") or page["images"][0].get("picker_colors", [])
            notion_cards.append(
                f"""
<section class="card image-derived">
  <div class="meta">
    <h2>{escape(page['slug'])}</h2>
    <span>{page['image_count']} images</span>
    <span>HEX/RGB: {escape(page['has_visible_hex_or_rgb'])}</span>
  </div>
  <div class="swatches">{swatches(first_colors)}</div>
  <p><strong>{escape(page['page_title'])}</strong></p>
  <p>{escape('; '.join(page.get('figure_uses', [])[:3]))}</p>
  <p class="disclaimer">{escape(page.get('action', ''))}: {escape(page.get('notes', ''))}</p>
</section>"""
            )

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Scientific Figure Palettes</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f8fafc;
      --fg: #0f172a;
      --muted: #475569;
      --card: #ffffff;
      --border: #cbd5e1;
    }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--fg);
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.45;
    }}
    main {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 32px 20px 48px;
    }}
    h1 {{
      font-size: 28px;
      margin: 0 0 8px;
    }}
    .lead {{
      margin: 0 0 24px;
      color: var(--muted);
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
      margin-bottom: 28px;
    }}
    h2.section {{
      font-size: 20px;
      margin: 30px 0 12px;
    }}
    .note {{
      color: var(--muted);
      margin: -4px 0 14px;
    }}
    .card {{
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 14px;
    }}
    .meta {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
    }}
    .meta h2 {{
      font-size: 16px;
      margin: 0;
      margin-right: auto;
    }}
    .meta span {{
      color: var(--muted);
      font-size: 12px;
    }}
    .swatches {{
      display: grid;
      grid-auto-flow: column;
      grid-auto-columns: 1fr;
      height: 32px;
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid var(--border);
    }}
    .swatch {{
      display: block;
      min-width: 10px;
    }}
    p {{
      margin: 10px 0 0;
      font-size: 13px;
    }}
    .disclaimer {{
      color: #9a3412;
    }}
  </style>
</head>
<body>
<main>
  <h1>Scientific Figure Palettes</h1>
  <p class="lead">Canonical, external cols4all, and Notion image-derived palette preview.</p>
  <h2 class="section">Core</h2>
  <div class="grid">
    {''.join(core_cards)}
  </div>
  <h2 class="section">Curated External</h2>
  <p class="note">Non-core publication candidates. GPL-3 cols4all entries keep license/provenance visible.</p>
  <div class="grid">
    {''.join(curated_cards)}
  </div>
  <h2 class="section">Notion Image-Derived</h2>
  <p class="note">Latest local Downloads images by Notion page. Picker colors are review candidates, not core palettes.</p>
  <div class="grid">
    {''.join(notion_cards)}
  </div>
  <h2 class="section">cols4all Large Library</h2>
  <p class="note">First 120 of the exported 689 GPL-3 cols4all palettes. Use CLI for the full library.</p>
  <div class="grid">
    {''.join(cols4all_cards)}
  </div>
</main>
</body>
</html>
"""
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
