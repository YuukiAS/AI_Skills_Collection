#!/usr/bin/env python3
"""Generate static discovery files for scientific figure palettes."""

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
INDEX_OUTPUT = ROOT / "palette" / "gallery-index.json"


def swatches(colors: list[str]) -> str:
    return "".join(
        f'<span class="swatch" title="{escape(color)}" style="background:{escape(color)}"></span>'
        for color in colors
    )


def index_record(item: dict, kind: str, source: str, colors: list[str] | None = None) -> dict:
    item_id = str(item.get("id") or item.get("candidate_id") or item.get("example_id") or item.get("source_id"))
    figure_types = item.get("figure_types", item.get("figure_type_tags", item.get("recommended_for", [])))
    venue_tags = item.get("venue_tags", [])
    title = str(item.get("name") or item.get("source_page_title") or item.get("source_id") or item_id)
    return {
        "id": item_id,
        "kind": kind,
        "source": source,
        "title": title,
        "colors": colors if colors is not None else item.get("colors", []),
        "type": item.get("type", ""),
        "tier": item.get("tier", ""),
        "palette_role": item.get("palette_role", ""),
        "review_status": item.get("review_status", ""),
        "snippet_eligibility": item.get("snippet_eligibility", ""),
        "raw_snippet_eligibility": item.get("raw_snippet_eligibility", item.get("snippet_eligibility", "")),
        "discovery_eligibility": item.get("discovery_eligibility", ""),
        "representative": bool(item.get("representative", False)),
        "page_group_id": item.get("page_group_id", item.get("source_page_slug", "")),
        "source_page_slug": item.get("source_page_slug", ""),
        "venue_tags": venue_tags,
        "figure_types": figure_types,
        "canonical_fallback_ids": item.get("canonical_fallback_ids", []),
        "disclaimer": item.get("disclaimer", ""),
        "search_text": " ".join(
            str(value)
            for value in [
                item_id,
                title,
                source,
                kind,
                item.get("tier", ""),
                item.get("palette_role", ""),
                item.get("source_page_slug", ""),
                *venue_tags,
                *figure_types,
            ]
        ).lower(),
    }


def card(record: dict) -> str:
    colors = record.get("colors", [])
    tags = " ".join(str(tag) for tag in [*record.get("venue_tags", []), *record.get("figure_types", [])])
    return f"""
<section class="card {escape(record['kind'])}" data-id="{escape(record['id'])}" data-kind="{escape(record['kind'])}" data-source="{escape(record['source'])}" data-tier="{escape(str(record.get('tier', '')))}" data-role="{escape(str(record.get('palette_role', '')))}" data-review="{escape(str(record.get('review_status', '')))}" data-snippet="{escape(str(record.get('raw_snippet_eligibility') or record.get('snippet_eligibility') or ''))}" data-venue="{escape(' '.join(str(tag) for tag in record.get('venue_tags', [])))}" data-figure="{escape(' '.join(str(tag) for tag in record.get('figure_types', [])))}" data-text="{escape(record.get('search_text', ''))}">
  <div class="meta">
    <h3>{escape(record['id'])}</h3>
    <span>{escape(record['source'])}</span>
    <span>{escape(record['kind'])}</span>
    {('<span>representative</span>' if record.get('representative') else '')}
  </div>
  <p><strong>{escape(record.get('title', ''))}</strong></p>
  {f'<div class="swatches">{swatches(colors)}</div>' if colors else ''}
  <p>{escape('; '.join(str(item) for item in record.get('figure_types', [])[:4]))}</p>
  <p class="small">venue={escape(', '.join(str(item) for item in record.get('venue_tags', [])) or '-')} | role={escape(str(record.get('palette_role') or '-'))}</p>
  <p class="small">review={escape(str(record.get('review_status') or '-'))} | raw={escape(str(record.get('raw_snippet_eligibility') or record.get('snippet_eligibility') or '-'))}</p>
  <p class="small">fallback={escape(', '.join(str(item) for item in record.get('canonical_fallback_ids', [])) or '-')}</p>
  {f'<p class="disclaimer">{escape(record["disclaimer"])}</p>' if record.get('disclaimer') else ''}
</section>"""


def build_index() -> list[dict]:
    records: list[dict] = []
    for palette in load_library().get("palettes", []):
        source = "canonical"
        if palette.get("tier") == "curated_external_gpl":
            source = "curated_external"
        records.append(index_record(palette, "palette", source))
    for candidate in load_notion_candidates().get("candidates", []):
        records.append(index_record(candidate, "candidate", "notion"))
    for example in load_example_registry().get("examples", []):
        records.append(index_record(example, "example", "notion", colors=[]))
    for palette in load_cols4all_library().get("palettes", [])[:120]:
        preview = {
            "id": palette.get("source_id"),
            "source_id": palette.get("source_id"),
            "name": palette.get("name", palette.get("source_id")),
            "type": palette.get("type"),
            "colors": palette.get("colors", []),
            "tier": "external_gpl_library",
            "recommended_for": ["external cols4all exploration"],
            "disclaimer": f"GPL-3 external palette; source id {palette.get('source_id', '')}",
        }
        records.append(index_record(preview, "palette", "cols4all"))
    return records


def options(records: list[dict], field: str) -> str:
    values: set[str] = set()
    for record in records:
        value = record.get(field)
        if isinstance(value, list):
            values.update(str(item) for item in value if item)
        elif value:
            values.add(str(value))
    return "\n".join(f'<option value="{escape(value)}">{escape(value)}</option>' for value in sorted(values))


def main() -> int:
    records = build_index()
    INDEX_OUTPUT.write_text(json.dumps({"version": "1.0.0", "items": records}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cards = "\n".join(card(record) for record in records)
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Scientific Figure Palette Discovery</title>
  <style>
    :root {{ color-scheme: light; --bg: #f8fafc; --fg: #0f172a; --muted: #475569; --card: #fff; --border: #cbd5e1; --accent: #0e7490; }}
    body {{ margin: 0; background: var(--bg); color: var(--fg); font-family: Arial, Helvetica, sans-serif; line-height: 1.45; }}
    main {{ max-width: 1240px; margin: 0 auto; padding: 28px 20px 48px; }}
    h1 {{ font-size: 28px; margin: 0 0 8px; }}
    .lead, .small {{ color: var(--muted); }}
    .controls {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 10px; margin: 18px 0 22px; }}
    input, select {{ width: 100%; box-sizing: border-box; border: 1px solid var(--border); border-radius: 6px; padding: 8px; background: #fff; color: var(--fg); }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; }}
    .card {{ background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 14px; }}
    .card[hidden] {{ display: none; }}
    .meta {{ display: flex; align-items: center; flex-wrap: wrap; gap: 8px; margin-bottom: 8px; }}
    .meta h3 {{ font-size: 15px; margin: 0; margin-right: auto; }}
    .meta span {{ color: var(--accent); font-size: 12px; font-weight: 700; }}
    .swatches {{ display: grid; grid-auto-flow: column; grid-auto-columns: 1fr; height: 32px; border-radius: 6px; overflow: hidden; border: 1px solid var(--border); margin-top: 10px; }}
    .swatch {{ display: block; min-width: 10px; }}
    p {{ margin: 10px 0 0; font-size: 13px; }}
    .disclaimer {{ color: #9a3412; }}
  </style>
</head>
<body>
<main>
  <h1>Scientific Figure Palette Discovery</h1>
  <p class="lead">Search canonical palettes, contextual Notion candidates, figure examples, and external GPL palette previews. Notion entries are non-official and unreviewed unless explicitly marked otherwise.</p>
  <div class="controls">
    <input id="q" type="search" placeholder="Search id, venue, figure type, page">
    <select id="source"><option value="">All sources</option>{options(records, 'source')}</select>
    <select id="kind"><option value="">All kinds</option>{options(records, 'kind')}</select>
    <select id="venue"><option value="">All venues</option>{options(records, 'venue_tags')}</select>
    <select id="figure"><option value="">All figure types</option>{options(records, 'figure_types')}</select>
    <select id="role"><option value="">All roles</option>{options(records, 'palette_role')}</select>
    <select id="review"><option value="">All review states</option>{options(records, 'review_status')}</select>
    <select id="snippet"><option value="">All snippet states</option>{options(records, 'raw_snippet_eligibility')}</select>
  </div>
  <p class="small" id="count"></p>
  <div class="grid" id="cards">
    {cards}
  </div>
</main>
<script>
const fields = ["q", "source", "kind", "venue", "figure", "role", "review", "snippet"];
const cards = [...document.querySelectorAll(".card")];
function paramsToControls() {{
  const params = new URLSearchParams(location.search);
  for (const id of fields) {{
    if (params.has(id)) document.getElementById(id).value = params.get(id);
  }}
}}
function matches(card, id, value) {{
  if (!value) return true;
  const lower = value.toLowerCase();
  if (id === "q") return card.dataset.text.includes(lower);
  if (id === "venue") return card.dataset.venue.toLowerCase().includes(lower);
  if (id === "figure") return card.dataset.figure.toLowerCase().includes(lower);
  if (id === "snippet") return card.dataset.snippet === value;
  return (card.dataset[id] || "") === value;
}}
function applyFilters() {{
  let shown = 0;
  const params = new URLSearchParams();
  for (const card of cards) {{
    const visible = fields.every(id => {{
      const value = document.getElementById(id).value;
      if (value) params.set(id, value);
      return matches(card, id, value);
    }});
    card.hidden = !visible;
    if (visible) shown += 1;
  }}
  history.replaceState(null, "", `${{location.pathname}}${{params.toString() ? "?" + params : ""}}`);
  document.getElementById("count").textContent = `${{shown}} of ${{cards.length}} records shown`;
}}
paramsToControls();
for (const id of fields) document.getElementById(id).addEventListener("input", applyFilters);
applyFilters();
</script>
</body>
</html>
"""
    html = "\n".join(line.rstrip() for line in html.splitlines()) + "\n"
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUTPUT}")
    print(f"wrote {INDEX_OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
