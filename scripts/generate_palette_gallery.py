#!/usr/bin/env python3
"""Generate a static HTML gallery for scientific figure palettes and examples."""

from __future__ import annotations

from html import escape
import json
from pathlib import Path

from palette_library import (
    load_cols4all_library,
    load_example_registry,
    load_library,
    load_notion_candidates,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "palette" / "gallery.html"


def swatches(colors: list[str]) -> str:
    return "".join(
        f'<span class="swatch" title="{escape(color)}" style="background:{escape(color)}"></span>'
        for color in colors
    )


def palette_card(palette: dict, section_class: str = "") -> str:
    disclaimer = palette.get("disclaimer", "")
    return f"""
<section class="card {escape(section_class)}" data-tier="{escape(str(palette.get('tier', '')))}" data-review="{escape(str(palette.get('review_status', '')))}" data-snippet="{escape(str(palette.get('snippet_eligibility', '')))}" data-venue="{escape(' '.join(str(tag) for tag in palette.get('venue_tags', [])))}">
  <div class="meta">
    <h3>{escape(str(palette.get('id') or palette.get('candidate_id') or palette.get('source_id')))}</h3>
    <span>{escape(str(palette.get('type', '')))}</span>
    <span>{len(palette.get('colors', []))} colors</span>
    <span>{escape(str(palette.get('tier', palette.get('series', ''))))}</span>
  </div>
  <div class="swatches">{swatches(palette.get('colors', []))}</div>
  <p><strong>{escape(str(palette.get('name') or palette.get('source_page_title') or palette.get('source_id')))}</strong></p>
  <p>{escape('; '.join(str(item) for item in palette.get('recommended_for', palette.get('figure_types', []))[:3]))}</p>
  <p class="small">review={escape(str(palette.get('review_status', '-')))} | recommendation={escape(str(palette.get('recommendation_status', '-')))} | snippet={escape(str(palette.get('snippet_eligibility', '-')))}</p>
  <p class="small">fallback={escape(', '.join(str(item) for item in palette.get('canonical_fallback_ids', [])))}</p>
  <p class="small">source asset committed={escape(str(palette.get('source_asset_committed', '-')))}</p>
  {f'<p class="disclaimer">{escape(disclaimer)}</p>' if disclaimer else ''}
</section>"""


def example_card(example: dict) -> str:
    return f"""
<section class="card example" data-venue="{escape(' '.join(str(tag) for tag in example.get('venue_tags', [])))}">
  <div class="meta">
    <h3>{escape(example['example_id'])}</h3>
    <span>{escape(example.get('source_page_slug', ''))}</span>
  </div>
  <p><strong>{escape(example.get('source_page_title', ''))}</strong></p>
  <p>{escape('; '.join(str(item) for item in example.get('figure_type_tags', [])[:4]))}</p>
  <p class="small">candidate={escape(', '.join(example.get('linked_candidate_ids', [])) or '-')}</p>
  <p class="small">fallback={escape(', '.join(example.get('canonical_fallback_ids', [])))}</p>
  <p class="small">source asset committed={escape(str(example.get('source_asset_committed')))}</p>
</section>"""


def section(title: str, note: str, cards: list[str]) -> str:
    return f"""
  <h2 class="section">{escape(title)}</h2>
  <p class="note">{escape(note)}</p>
  <div class="grid">
    {''.join(cards)}
  </div>"""


def main() -> int:
    library = load_library()
    canonical = library.get("palettes", [])
    core_cards = [palette_card(palette, "core") for palette in canonical if palette.get("tier") == "core_publication"]
    journal_cards = [palette_card(palette, "journal") for palette in canonical if palette.get("tier") == "journal_inspired_nonofficial"]
    curated_cards = [palette_card(palette, "external") for palette in canonical if palette.get("tier") == "curated_external_gpl"]

    notion_candidates = load_notion_candidates().get("candidates", [])
    notion_transcribed = [palette_card(candidate, "notion") for candidate in notion_candidates if candidate.get("tier") == "image_derived_transcribed"]
    notion_unreviewed = [palette_card(candidate, "notion") for candidate in notion_candidates if candidate.get("tier") != "image_derived_transcribed"]

    examples = [example_card(example) for example in load_example_registry().get("examples", [])]

    cols4all_cards = []
    for palette in load_cols4all_library().get("palettes", [])[:120]:
        item = {
            "id": palette.get("source_id"),
            "name": palette.get("name", palette.get("source_id")),
            "type": palette.get("type"),
            "colors": palette.get("colors", []),
            "tier": "external_gpl_library",
            "review_status": "-",
            "recommendation_status": "explicit_external",
            "snippet_eligibility": "-",
            "disclaimer": f"GPL-3 external palette; source id {palette.get('source_id', '')}",
        }
        cols4all_cards.append(palette_card(item, "cols4all"))

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Scientific Figure Palettes</title>
  <style>
    :root {{ color-scheme: light; --bg: #f8fafc; --fg: #0f172a; --muted: #475569; --card: #fff; --border: #cbd5e1; }}
    body {{ margin: 0; background: var(--bg); color: var(--fg); font-family: Arial, Helvetica, sans-serif; line-height: 1.45; }}
    main {{ max-width: 1180px; margin: 0 auto; padding: 32px 20px 48px; }}
    h1 {{ font-size: 28px; margin: 0 0 8px; }}
    .lead, .note {{ color: var(--muted); }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; margin-bottom: 28px; }}
    h2.section {{ font-size: 20px; margin: 30px 0 8px; }}
    .card {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 14px; }}
    .meta {{ display: flex; align-items: center; flex-wrap: wrap; gap: 8px; margin-bottom: 10px; }}
    .meta h3 {{ font-size: 15px; margin: 0; margin-right: auto; }}
    .meta span, .small {{ color: var(--muted); font-size: 12px; }}
    .swatches {{ display: grid; grid-auto-flow: column; grid-auto-columns: 1fr; height: 32px; border-radius: 6px; overflow: hidden; border: 1px solid var(--border); }}
    .swatch {{ display: block; min-width: 10px; }}
    p {{ margin: 10px 0 0; font-size: 13px; }}
    .disclaimer {{ color: #9a3412; }}
  </style>
</head>
<body>
<main>
  <h1>Scientific Figure Palettes</h1>
  <p class="lead">Canonical palettes, Notion image-level candidates, figure examples, and external GPL library preview.</p>
  {section('Core Publication', 'Default publication-ready canonical palettes.', core_cards)}
  {section('Journal-Inspired Non-Official', 'Contextual style references, not official publisher branding.', journal_cards)}
  {section('Curated External GPL', 'Non-core curated cols4all candidates with GPL-3 provenance.', curated_cards)}
  {section('Notion Transcribed Candidates', 'Image-level candidates with visible HEX transcription; still unreviewed and gated for snippets.', notion_transcribed)}
  {section('Notion Unreviewed / Inspiration', 'Picker-derived or figure-sampled candidates remain inspiration-only and snippet-blocked.', notion_unreviewed)}
  {section('Figure Examples', 'Example routing records for layouts and figure styles. Source images are not redistributed.', examples)}
  {section('cols4all Large Library', 'First 120 exported GPL-3 cols4all palettes. Use the CLI for the full library.', cols4all_cards)}
</main>
</body>
</html>
"""
    html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
