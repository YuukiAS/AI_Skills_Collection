#!/usr/bin/env python3
"""Validate the scientific figure palette library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PALETTE_DIR = ROOT / "palette"
CANONICAL = PALETTE_DIR / "scientific-figure-palettes.json"
SCHEMA = PALETTE_DIR / "scientific-figure-palettes.schema.json"
LEGACY = PALETTE_DIR / "palettes.json"

REQUIRED_IDS = {
    "okabe_ito",
    "nature_npg",
    "science_aaas",
    "nejm",
    "lancet",
    "jama",
    "bmj",
    "jco",
    "Dark2",
    "Set2",
    "Paired",
    "Blues",
    "YlGnBu",
    "OrRd",
    "RdBu",
    "BrBG",
    "PuOr",
    "viridis",
    "plasma",
    "inferno",
    "magma",
    "cividis",
    "coolwarm",
    "twilight",
}

REQUIRED_FIELDS = {
    "id",
    "legacy_ids",
    "name",
    "family",
    "type",
    "colors",
    "recommended_for",
    "avoid_for",
    "colorblind_safe",
    "provenance_status",
    "origins",
    "stability",
}

HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - error formatting path
        raise AssertionError(f"{path} is not valid JSON: {exc}") from exc


def origin_names(palette: dict) -> set[str]:
    return {str(origin.get("name", "")).lower() for origin in palette.get("origins", [])}


def main() -> int:
    errors: list[str] = []

    schema = load_json(SCHEMA)
    if not isinstance(schema, dict) or schema.get("type") != "object":
        errors.append("schema must be a JSON object schema")

    canonical = load_json(CANONICAL)
    legacy = load_json(LEGACY)

    if not isinstance(canonical, dict):
        errors.append("canonical file must be a JSON object")
        canonical = {}
    if not isinstance(legacy, dict):
        errors.append("legacy palettes.json must be a JSON object")
        legacy = {}

    palettes = canonical.get("palettes", [])
    if not isinstance(palettes, list) or not palettes:
        errors.append("canonical palettes must be a non-empty list")
        palettes = []

    ids: set[str] = set()
    legacy_aliases: dict[str, str] = {}
    by_id: dict[str, dict] = {}

    for idx, palette in enumerate(palettes):
        if not isinstance(palette, dict):
            errors.append(f"palette #{idx} is not an object")
            continue

        pid = palette.get("id")
        if not isinstance(pid, str) or not pid:
            errors.append(f"palette #{idx} has invalid id")
            continue
        if pid in ids:
            errors.append(f"duplicate palette id: {pid}")
        ids.add(pid)
        by_id[pid] = palette

        missing = sorted(REQUIRED_FIELDS - set(palette))
        if missing:
            errors.append(f"{pid} missing required fields: {', '.join(missing)}")

        colors = palette.get("colors")
        if not isinstance(colors, list) or not colors:
            errors.append(f"{pid} colors must be a non-empty list")
        else:
            bad_colors = [c for c in colors if not isinstance(c, str) or not HEX.match(c)]
            if bad_colors:
                errors.append(f"{pid} has invalid hex colors: {bad_colors[:3]}")

        aliases = palette.get("legacy_ids", [])
        if not isinstance(aliases, list):
            errors.append(f"{pid} legacy_ids must be a list")
        else:
            for alias in aliases:
                if not isinstance(alias, str) or not alias:
                    errors.append(f"{pid} has invalid legacy alias: {alias!r}")
                    continue
                if alias in ids:
                    errors.append(f"{pid} legacy alias conflicts with palette id: {alias}")
                previous = legacy_aliases.get(alias)
                if previous and previous != pid:
                    errors.append(f"legacy alias {alias} used by both {previous} and {pid}")
                legacy_aliases[alias] = pid

        origins = palette.get("origins", [])
        if not isinstance(origins, list) or not origins:
            errors.append(f"{pid} origins must be a non-empty list")
        else:
            for origin in origins:
                if not isinstance(origin, dict) or not origin.get("url") or not origin.get("usage"):
                    errors.append(f"{pid} has incomplete origin metadata")

    missing_ids = sorted(REQUIRED_IDS - ids)
    if missing_ids:
        errors.append(f"missing required core palettes: {', '.join(missing_ids)}")

    journal_ids = {"nature_npg", "science_aaas", "nejm", "lancet", "jama", "bmj", "jco"}
    for pid in sorted(journal_ids):
        palette = by_id.get(pid)
        if not palette:
            continue
        disclaimer = str(palette.get("disclaimer", "")).lower()
        if palette.get("is_official_branding") is not False or "not official" not in disclaimer:
            errors.append(f"{pid} must carry a non-official journal-inspired disclaimer")
        if "ggsci" not in origin_names(palette):
            errors.append(f"{pid} must reference the verified ggsci source")

    source_checks = {
        "okabe_ito": "color universal design",
        "Dark2": "colorbrewer",
        "Set2": "colorbrewer",
        "Paired": "colorbrewer",
        "Blues": "colorbrewer",
        "YlGnBu": "colorbrewer",
        "OrRd": "colorbrewer",
        "RdBu": "colorbrewer",
        "BrBG": "colorbrewer",
        "PuOr": "colorbrewer",
        "viridis": "matplotlib",
        "plasma": "matplotlib",
        "inferno": "matplotlib",
        "magma": "matplotlib",
        "cividis": "matplotlib",
        "coolwarm": "matplotlib",
        "twilight": "matplotlib",
    }
    for pid, expected in source_checks.items():
        palette = by_id.get(pid)
        if palette and not any(expected in name for name in origin_names(palette)):
            errors.append(f"{pid} must reference {expected} in origins")

    external_sources = canonical.get("external_sources", [])
    source_names = {str(source.get("name", "")).lower() for source in external_sources if isinstance(source, dict)}
    for expected in {"colorbrewer", "matplotlib", "material color utilities", "ggsci", "color universal design (cud)"}:
        if expected not in source_names:
            errors.append(f"external_sources missing {expected}")

    legacy_palettes = legacy.get("palettes", [])
    if not isinstance(legacy_palettes, list) or not legacy_palettes:
        errors.append("palette/palettes.json must preserve a non-empty palettes list")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: validated {len(palettes)} canonical palettes and {len(legacy_palettes)} legacy palettes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
