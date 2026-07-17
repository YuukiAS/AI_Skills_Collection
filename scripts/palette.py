#!/usr/bin/env python3
"""CLI for scientific figure palettes, presets, and examples."""

from __future__ import annotations

import argparse
import json
import sys

from palette_library import (
    find_examples,
    format_palette,
    get_palette,
    get_preset,
    list_palettes,
    list_presets,
    palette_to_snippet,
    recommend_palettes,
    recommend_presets,
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
    print(palette_to_snippet(palette, args.target, allow_experimental=args.allow_experimental), end="")
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
    return parser


def main(argv: list[str] | None = None) -> int:
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
