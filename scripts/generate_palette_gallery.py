#!/usr/bin/env python3
"""Generate a static HTML gallery for canonical scientific figure palettes."""

from __future__ import annotations

from html import escape
from pathlib import Path

from palette_library import load_library


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "palette" / "gallery.html"


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
    cards = []
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
        cards.append(card)

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
  <p class="lead">Canonical palette preview generated from palette/scientific-figure-palettes.json.</p>
  <div class="grid">
    {''.join(cards)}
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
