#!/usr/bin/env python3
"""CLI for the canonical scientific figure palette library."""

from __future__ import annotations

import argparse
import sys

from palette_library import (
    format_palette,
    get_palette,
    list_palettes,
    palette_to_snippet,
    recommend_palette,
)


def command_list(args: argparse.Namespace) -> int:
    palettes = list_palettes(type=args.type, core_only=not args.all)
    for palette in palettes:
        print(
            f"{palette['id']}\t{palette['type']}\t{len(palette['colors'])}\t"
            f"{palette['family']}\t{palette['provenance_status']}"
        )
    return 0


def command_get(args: argparse.Namespace) -> int:
    palette = get_palette(args.id_or_alias)
    print(format_palette(palette, args.format))
    return 0


def command_snippet(args: argparse.Namespace) -> int:
    palette = get_palette(args.id_or_alias)
    print(palette_to_snippet(palette, args.target), end="")
    return 0


def command_recommend(args: argparse.Namespace) -> int:
    palettes = recommend_palette(args.purpose)
    for palette in palettes:
        print(
            f"{palette['id']}\t{palette['type']}\t{len(palette['colors'])}\t"
            f"{', '.join(palette['recommended_for'][:2])}"
        )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="List canonical palettes")
    p_list.add_argument("--type", choices=["categorical", "sequential", "diverging", "cyclic"])
    p_list.add_argument("--all", action="store_true", help="Include non-core palettes if present")
    p_list.set_defaults(func=command_list)

    p_get = sub.add_parser("get", help="Get one palette")
    p_get.add_argument("id_or_alias")
    p_get.add_argument("--format", choices=["json", "hex", "python", "css"], default="json")
    p_get.set_defaults(func=command_get)

    p_snippet = sub.add_parser("snippet", help="Generate plotting code for one palette")
    p_snippet.add_argument("id_or_alias")
    p_snippet.add_argument("--target", choices=["matplotlib", "seaborn", "plotly", "latex"], required=True)
    p_snippet.set_defaults(func=command_snippet)

    p_recommend = sub.add_parser("recommend", help="Recommend palettes for a figure purpose")
    p_recommend.add_argument(
        "--purpose",
        choices=["categorical", "sequential", "diverging", "cyclic", "journal", "clinical", "heatmap"],
        required=True,
    )
    p_recommend.set_defaults(func=command_recommend)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (KeyError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
