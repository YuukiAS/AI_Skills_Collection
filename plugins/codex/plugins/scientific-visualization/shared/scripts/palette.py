#!/usr/bin/env python3
"""CLI for scientific figure palettes, presets, and examples."""

from __future__ import annotations

import argparse
import json
import sys

from palette_library import (
    compare_items,
    discover_context,
    explain_item,
    find_examples,
    format_palette,
    get_palette,
    get_preset,
    list_palettes,
    list_presets,
    palette_to_snippet,
    recommend_palettes,
    recommend_presets,
    search_notion_candidates,
    search_notion_pages,
    style_guidance,
)


SOURCE_CHOICES = ["canonical", "cols4all", "notion", "all"]
STYLE_CHOICES = ["core", "journal", "notion", "cols4all", "all"]
TARGET_CHOICES = ["matplotlib", "seaborn", "plotly", "latex"]


def _print_palette_row(palette: dict, explain: bool = False) -> None:
    print(
        f"{palette['id']}\t{palette.get('type', '')}\t{len(palette.get('colors', []))}\t"
        f"{palette.get('tier', '')}\t{palette.get('recommendation_status', '')}"
    )
    if explain:
        print(
            f"  source={palette.get('source', 'canonical')} review={palette.get('review_status', '-')}"
            f" snippet={palette.get('snippet_eligibility', '-')}"
        )
        if palette.get("disclaimer"):
            print(f"  disclaimer={palette['disclaimer']}")


def command_list(args: argparse.Namespace) -> int:
    source = args.source
    if source == "canonical" and args.tier and args.tier.startswith("image_derived"):
        source = "all"
    palettes = list_palettes(
        type=args.type,
        core_only=not args.all and source == "canonical" and not args.tier,
        source=source,
        tier=args.tier,
        review_status=args.review_status,
        recommendation_status=args.recommendation_status,
    )
    for palette in palettes:
        _print_palette_row(palette, explain=args.explain)
    return 0


def command_get(args: argparse.Namespace) -> int:
    source = "all" if args.source == "canonical" and args.id_or_alias.startswith("notion_") else args.source
    palette = get_palette(args.id_or_alias, source=source)
    print(format_palette(palette, args.format))
    return 0


def command_snippet(args: argparse.Namespace) -> int:
    source = "all" if args.source == "canonical" and args.id_or_alias.startswith("notion_") else args.source
    palette = get_palette(args.id_or_alias, source=source)
    print(
        palette_to_snippet(palette, args.target, allow_experimental=args.allow_experimental, kind=args.kind),
        end="",
    )
    return 0


def command_recommend(args: argparse.Namespace) -> int:
    palettes = recommend_palettes(
        purpose=args.purpose,
        figure_type=args.figure_type,
        paper_venue=args.paper_venue,
        style_source=args.style_source,
        source=args.source,
        include_experimental=args.style_source in {"notion", "all"},
    )
    for palette in palettes:
        _print_palette_row(palette, explain=args.explain)
    return 0


def command_preset_list(args: argparse.Namespace) -> int:
    for preset in list_presets():
        print(f"{preset['id']}\t{', '.join(preset.get('venue_tags', []))}\t{preset.get('name', '')}")
    return 0


def command_preset_get(args: argparse.Namespace) -> int:
    print(json.dumps(get_preset(args.id), ensure_ascii=False, indent=2))
    return 0


def command_preset_recommend(args: argparse.Namespace) -> int:
    for preset in recommend_presets(paper_venue=args.paper_venue, figure_type=args.figure_type):
        print(f"{preset['id']}\t{', '.join(preset.get('figure_type_tags', [])[:3])}\t{preset.get('disclaimer', '')}")
    return 0


def command_example(args: argparse.Namespace) -> int:
    examples = find_examples(
        figure_type=args.figure_type,
        style_source=args.style_source,
        page=args.page,
        paper_venue=args.paper_venue,
    )
    for example in examples:
        print(
            f"{example['example_id']}\t{example.get('source_page_slug', '')}\t"
            f"{', '.join(example.get('linked_candidate_ids', [])) or '-'}\t"
            f"{', '.join(example.get('canonical_fallback_ids', []))}"
        )
        if args.explain:
            print(f"  figure_types={'; '.join(example.get('figure_type_tags', []))}")
            print(f"  source_asset_committed={example.get('source_asset_committed')}")
            if example.get("style_notes"):
                print(f"  notes={example['style_notes']}")
    return 0


def _compact_palette(palette: dict) -> dict:
    return {
        "id": palette.get("id"),
        "type": palette.get("type"),
        "colors": palette.get("colors", []),
        "tier": palette.get("tier"),
        "source": palette.get("source", "canonical"),
        "review_status": palette.get("review_status"),
        "discovery_eligibility": palette.get("discovery_eligibility"),
        "raw_snippet_eligibility": palette.get("raw_snippet_eligibility", palette.get("snippet_eligibility")),
        "canonical_fallback_ids": palette.get("canonical_fallback_ids", []),
        "disclaimer": palette.get("disclaimer", ""),
    }


def command_discover(args: argparse.Namespace) -> int:
    result = discover_context(
        purpose=args.purpose,
        figure_type=args.figure_type,
        paper_venue=args.paper_venue,
        domain=args.domain,
        limit_per_page=args.limit_per_page,
    )
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    print("SAFE PUBLICATION DEFAULTS")
    for palette in result["safe_palettes"]:
        print(f"- {palette['id']} ({palette.get('type', '')}; {len(palette.get('colors', []))} colors)")
    print("\nCONTEXTUAL PRESETS")
    for preset in result["contextual_presets"]:
        print(f"- {preset['id']}: {preset.get('name', '')}")
    print("\nNOTION PAGES")
    for page in result["notion_pages"]:
        print(f"- {page['slug']} ({page.get('image_count')} images): {'; '.join(page.get('figure_uses', [])[:3])}")
    print("\nEXPERIMENTAL CANDIDATES")
    for palette in result["experimental_candidates"]:
        print(
            f"- {palette['id']} review={palette.get('review_status')} raw={palette.get('raw_snippet_eligibility')} "
            f"fallback={', '.join(palette.get('canonical_fallback_ids', []))}"
        )
        if args.explain and palette.get("disclaimer"):
            print(f"  {palette['disclaimer']}")
    print("\nFIGURE EXAMPLES")
    for example in result["figure_examples"]:
        print(f"- {example['example_id']} page={example.get('source_page_slug')} candidate={', '.join(example.get('linked_candidate_ids', []))}")
    print("\nGUIDANCE ONLY")
    for palette in result["guidance_only"]:
        print(f"- {palette['id']} role={palette.get('palette_role')} raw={palette.get('raw_snippet_eligibility')}")
    if args.explain:
        print("\nWARNINGS")
        for warning in result["warnings"]:
            print(f"- {warning}")
    return 0


def command_notion_pages(args: argparse.Namespace) -> int:
    for page in search_notion_pages():
        print(f"{page['slug']}\t{page.get('image_count')}\t{'; '.join(page.get('figure_uses', [])[:4])}")
    return 0


def command_notion_show(args: argparse.Namespace) -> int:
    matches = search_notion_pages(query=args.page_slug)
    page = next((item for item in matches if item.get("slug") == args.page_slug), None)
    if page is None:
        raise KeyError(f"Unknown Notion page slug: {args.page_slug}")
    print(json.dumps(page, ensure_ascii=False, indent=2))
    return 0


def command_notion_search(args: argparse.Namespace) -> int:
    pages = search_notion_pages(paper_venue=args.venue, figure_type=args.figure_type, query=args.query)
    candidates = search_notion_candidates(
        paper_venue=args.venue,
        figure_type=args.figure_type,
        role=args.role,
        query=args.query,
        limit_per_page=args.limit_per_page,
    )
    if args.format == "json":
        print(json.dumps({"pages": pages, "candidates": candidates}, ensure_ascii=False, indent=2))
        return 0
    print("PAGES")
    for page in pages:
        print(f"- {page['slug']} ({page.get('image_count')} images)")
    print("CANDIDATES")
    for palette in candidates:
        print(f"- {palette['id']}\t{palette.get('palette_role')}\t{palette.get('discovery_eligibility')}\t{palette.get('raw_snippet_eligibility')}")
    return 0


def command_explain(args: argparse.Namespace) -> int:
    print(json.dumps(explain_item(args.id), ensure_ascii=False, indent=2))
    return 0


def command_compare(args: argparse.Namespace) -> int:
    rows = compare_items(args.ids, paper_venue=args.paper_venue, figure_type=args.figure_type)
    if args.format == "json":
        print(json.dumps(rows, ensure_ascii=False, indent=2))
        return 0
    for row in rows:
        print(
            f"{row['id']}\t{row['kind']}\t{row.get('tier', '')}\t"
            f"review={row.get('review_status', '')}\traw={row.get('raw_snippet_eligibility', '')}\t"
            f"fallback={', '.join(row.get('fallback', []))}"
        )
    return 0


def command_guidance(args: argparse.Namespace) -> int:
    guidance = style_guidance(args.id, target=args.target)
    if isinstance(guidance, dict):
        print(json.dumps(guidance, ensure_ascii=False, indent=2))
    else:
        print(guidance, end="")
    return 0


def add_common_recommend_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--paper-venue", help="Routing context, e.g. CVPR, ICML, AAAI, Nature, general-journal")
    parser.add_argument("--style-source", choices=STYLE_CHOICES, default="core")
    parser.add_argument("--explain", action="store_true")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List palettes")
    p_list.add_argument("--type", choices=["categorical", "sequential", "diverging", "cyclic", "bivariate"])
    p_list.add_argument("--all", action="store_true", help="Include non-core canonical palettes")
    p_list.add_argument("--source", choices=SOURCE_CHOICES, default="canonical")
    p_list.add_argument("--tier")
    p_list.add_argument("--review-status")
    p_list.add_argument("--recommendation-status")
    p_list.add_argument("--explain", action="store_true")
    p_list.set_defaults(func=command_list)

    p_get = sub.add_parser("get", help="Get one palette")
    p_get.add_argument("id_or_alias")
    p_get.add_argument("--format", choices=["json", "hex", "python", "css"], default="json")
    p_get.add_argument("--source", choices=SOURCE_CHOICES, default="canonical")
    p_get.set_defaults(func=command_get)

    p_snippet = sub.add_parser("snippet", help="Generate plotting code for one palette")
    p_snippet.add_argument("id_or_alias")
    p_snippet.add_argument("--target", choices=TARGET_CHOICES, required=True)
    p_snippet.add_argument("--source", choices=SOURCE_CHOICES, default="canonical")
    p_snippet.add_argument("--allow-experimental", action="store_true")
    p_snippet.add_argument("--kind", choices=["raw-colors", "style-tokens"], default="raw-colors")
    p_snippet.set_defaults(func=command_snippet)

    p_recommend = sub.add_parser("recommend", help="Recommend palettes for a figure purpose")
    p_recommend.add_argument("--purpose", choices=["categorical", "sequential", "diverging", "cyclic", "journal", "clinical", "heatmap"])
    p_recommend.add_argument("--figure-type", help="Concrete figure type, e.g. line, umap, heatmap, schematic")
    p_recommend.add_argument("--source", choices=SOURCE_CHOICES, default="canonical")
    add_common_recommend_args(p_recommend)
    p_recommend.set_defaults(func=command_recommend)

    p_preset = sub.add_parser("preset", help="List, get, or recommend publication figure presets")
    preset_sub = p_preset.add_subparsers(dest="preset_command", required=True)
    p_preset_list = preset_sub.add_parser("list")
    p_preset_list.set_defaults(func=command_preset_list)
    p_preset_get = preset_sub.add_parser("get")
    p_preset_get.add_argument("id")
    p_preset_get.set_defaults(func=command_preset_get)
    p_preset_rec = preset_sub.add_parser("recommend")
    p_preset_rec.add_argument("--figure-type")
    p_preset_rec.add_argument("--paper-venue")
    p_preset_rec.set_defaults(func=command_preset_recommend)

    p_example = sub.add_parser("example", help="Find figure examples")
    p_example.add_argument("--figure-type")
    p_example.add_argument("--style-source", choices=["notion", "all"], default="notion")
    p_example.add_argument("--page")
    p_example.add_argument("--paper-venue")
    p_example.add_argument("--explain", action="store_true")
    p_example.set_defaults(func=command_example)

    p_discover = sub.add_parser("discover", help="Discover safe palettes plus contextual Notion references")
    p_discover.add_argument("--purpose")
    p_discover.add_argument("--figure-type")
    p_discover.add_argument("--paper-venue")
    p_discover.add_argument("--domain")
    p_discover.add_argument("--format", choices=["text", "json"], default="text")
    p_discover.add_argument("--limit-per-page", type=int, default=3)
    p_discover.add_argument("--explain", action="store_true")
    p_discover.set_defaults(func=command_discover)

    p_notion = sub.add_parser("notion", help="Discover Notion-derived palette pages and candidates")
    notion_sub = p_notion.add_subparsers(dest="notion_command", required=True)
    p_notion_pages = notion_sub.add_parser("pages")
    p_notion_pages.set_defaults(func=command_notion_pages)
    p_notion_show = notion_sub.add_parser("show")
    p_notion_show.add_argument("page_slug")
    p_notion_show.set_defaults(func=command_notion_show)
    p_notion_search = notion_sub.add_parser("search")
    p_notion_search.add_argument("--venue")
    p_notion_search.add_argument("--figure-type")
    p_notion_search.add_argument("--role")
    p_notion_search.add_argument("--query")
    p_notion_search.add_argument("--limit-per-page", type=int, default=3)
    p_notion_search.add_argument("--format", choices=["text", "json"], default="text")
    p_notion_search.set_defaults(func=command_notion_search)

    p_explain = sub.add_parser("explain", help="Explain a palette, candidate, preset, example, or Notion page")
    p_explain.add_argument("id")
    p_explain.set_defaults(func=command_explain)

    p_compare = sub.add_parser("compare", help="Compare palette discovery items")
    p_compare.add_argument("ids", nargs="+")
    p_compare.add_argument("--paper-venue")
    p_compare.add_argument("--figure-type")
    p_compare.add_argument("--format", choices=["text", "json"], default="text")
    p_compare.set_defaults(func=command_compare)

    p_guidance = sub.add_parser("guidance", help="Emit style guidance without raw color snippets")
    p_guidance.add_argument("id")
    p_guidance.add_argument("--target", choices=[*TARGET_CHOICES, "json"], default="json")
    p_guidance.set_defaults(func=command_guidance)
    return parser


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "recommend" and not args.purpose and not args.figure_type and not args.paper_venue:
            parser.error("recommend requires --purpose, --figure-type, or --paper-venue")
        return args.func(args)
    except (KeyError, FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
