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
COLS4ALL = PALETTE_DIR / "external" / "cols4all-palettes.json"
COLS4ALL_SCHEMA = PALETTE_DIR / "external" / "cols4all-palettes.schema.json"
COLS4ALL_EVALUATION = PALETTE_DIR / "cols4all-evaluation.json"
NOTION_IMAGES = PALETTE_DIR / "notion-image-palettes.json"
NOTION_CANDIDATES = PALETTE_DIR / "notion-palette-candidates.json"
FIGURE_EXAMPLES = PALETTE_DIR / "figure-example-registry.json"
NOTION_REVIEW_QUEUE = PALETTE_DIR / "notion-review-queue.json"
PUBLICATION_PRESETS = PALETTE_DIR / "publication-figure-presets.json"
THIRD_PARTY_NOTICES = PALETTE_DIR / "THIRD_PARTY_NOTICES.md"

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
LOCAL_PATH_PATTERNS = ("C:\\Users\\", "/Users/", "/home/")


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
    cols4all = load_json(COLS4ALL) if COLS4ALL.exists() else None
    cols4all_schema = load_json(COLS4ALL_SCHEMA) if COLS4ALL_SCHEMA.exists() else None
    cols4all_evaluation = load_json(COLS4ALL_EVALUATION) if COLS4ALL_EVALUATION.exists() else None
    notion_images = load_json(NOTION_IMAGES) if NOTION_IMAGES.exists() else None
    notion_candidates = load_json(NOTION_CANDIDATES) if NOTION_CANDIDATES.exists() else None
    figure_examples = load_json(FIGURE_EXAMPLES) if FIGURE_EXAMPLES.exists() else None
    notion_review_queue = load_json(NOTION_REVIEW_QUEUE) if NOTION_REVIEW_QUEUE.exists() else None
    publication_presets = load_json(PUBLICATION_PRESETS) if PUBLICATION_PRESETS.exists() else None

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
    for expected in {"colorbrewer", "matplotlib", "material color utilities", "ggsci", "color universal design (cud)", "cols4all"}:
        if expected not in source_names:
            errors.append(f"external_sources missing {expected}")
    for source in external_sources:
        if isinstance(source, dict) and "local_path" in source:
            errors.append("external_sources must not store local_path")

    curated_cols4all_ids = {
        "cols4all_area7",
        "cols4all_area8",
        "cols4all_area9",
        "cols4all_line7",
        "cols4all_line8",
        "cols4all_line9",
        "cols4all_friendly5",
        "cols4all_friendly7",
        "cols4all_friendly9",
        "cols4all_friendly11",
        "cols4all_friendly13",
        "tol_bright",
        "carto_safe",
        "scico_batlow",
        "hcl_purple_green",
    }
    for pid in sorted(curated_cols4all_ids):
        palette = by_id.get(pid)
        if not palette:
            errors.append(f"missing curated cols4all palette: {pid}")
            continue
        if palette.get("core") is not False:
            errors.append(f"{pid} must remain non-core")
        if palette.get("license") != "GPL-3":
            errors.append(f"{pid} must keep GPL-3 license metadata")
        if "cols4all" not in origin_names(palette):
            errors.append(f"{pid} must reference cols4all in origins")

    core_publication = [palette for palette in palettes if palette.get("tier") == "core_publication"]
    journal_nonofficial = [palette for palette in palettes if palette.get("tier") == "journal_inspired_nonofficial"]
    curated_gpl = [palette for palette in palettes if palette.get("tier") == "curated_external_gpl"]
    if len(palettes) != 39:
        errors.append(f"canonical palette count must remain 39, found {len(palettes)}")
    if len(core_publication) != 17:
        errors.append(f"core_publication palette count must be 17, found {len(core_publication)}")
    if len(journal_nonofficial) != 7:
        errors.append(f"journal_inspired_nonofficial palette count must be 7, found {len(journal_nonofficial)}")
    if len(curated_gpl) != 15:
        errors.append(f"curated_external_gpl palette count must be 15, found {len(curated_gpl)}")
    for palette in journal_nonofficial:
        if palette.get("core") is not False:
            errors.append(f"{palette.get('id')} journal-inspired palette must be non-core")
        if palette.get("is_official_branding") is not False:
            errors.append(f"{palette.get('id')} must be marked non-official branding")

    legacy_palettes = legacy.get("palettes", [])
    if not isinstance(legacy_palettes, list) or not legacy_palettes:
        errors.append("palette/palettes.json must preserve a non-empty palettes list")

    if not isinstance(cols4all_schema, dict) or cols4all_schema.get("title") != "AI Skills cols4all External Palette Library":
        errors.append("cols4all external schema missing or invalid")

    if not isinstance(cols4all, dict):
        errors.append("cols4all external palette file missing or invalid")
    else:
        if cols4all.get("license") != "GPL-3":
            errors.append("cols4all external library must be marked GPL-3")
        if not cols4all.get("source_commit"):
            errors.append("cols4all external library must record source_commit")
        external_palettes = cols4all.get("palettes", [])
        if not isinstance(external_palettes, list) or len(external_palettes) < 600:
            errors.append("cols4all external library must contain the bulk runtime export")
        for idx, palette in enumerate(external_palettes[:20]):
            if palette.get("license") != "GPL-3":
                errors.append(f"cols4all palette #{idx} missing GPL-3 license")
            if not palette.get("colors"):
                errors.append(f"cols4all palette #{idx} missing colors")

    if not isinstance(cols4all_evaluation, dict):
        errors.append("cols4all evaluation file missing or invalid")
    else:
        evaluated = cols4all_evaluation.get("palettes", [])
        if not isinstance(evaluated, list) or len(evaluated) < len(palettes):
            errors.append("cols4all evaluation must cover canonical palettes")
        evaluation_errors = [item for item in evaluated if isinstance(item, dict) and item.get("error")]
        if evaluation_errors:
            errors.append(f"cols4all evaluation contains errors: {evaluation_errors[:3]}")

    if not isinstance(notion_images, dict):
        errors.append("notion image palette file missing or invalid")
    else:
        notion_text = NOTION_IMAGES.read_text(encoding="utf-8")
        for pattern in LOCAL_PATH_PATTERNS:
            if pattern in notion_text:
                errors.append(f"notion image palette file must not contain local path pattern {pattern}")
        if '"mtime"' in notion_text:
            errors.append("notion image palette file must not contain mtime fields")
        pages = notion_images.get("pages", [])
        if not isinstance(pages, list) or len(pages) != 8:
            errors.append("notion image palette file must record all 8 palette pages")
        slugs = {str(page.get("slug")) for page in pages if isinstance(page, dict)}
        for expected in {
            "cvpr25",
            "aaai",
            "journal_reviewer_9",
            "icml_clean",
            "nature_inspiration",
            "nature_same_palette",
            "python_bar_distribution",
            "old_palettes_typical_figures",
        }:
            if expected not in slugs:
                errors.append(f"notion image palette file missing page {expected}")
        for page in pages:
            if not isinstance(page, dict):
                continue
            slug = str(page.get("slug"))
            images = page.get("images", [])
            if not isinstance(images, list):
                errors.append(f"notion page {slug} images must be a list")
                continue
            if page.get("has_visible_hex_or_rgb") in {"yes", "mixed"} and images:
                manual = [
                    image
                    for image in images
                    if isinstance(image, dict)
                    and image.get("color_source") == "visible_hex_manual_transcription"
                    and image.get("visible_hex_colors")
                ]
                if not manual:
                    errors.append(f"notion page {slug} has visible HEX/RGB but no transcribed visible_hex_colors")
            for image in images:
                if not isinstance(image, dict):
                    continue
                primary = image.get("primary_colors", [])
                if image.get("color_source") == "visible_hex_manual_transcription" and primary != image.get("visible_hex_colors"):
                    errors.append(f"notion image {image.get('candidate_id')} primary_colors must use visible_hex_colors")
                if primary:
                    bad_primary = [c for c in primary if not isinstance(c, str) or not HEX.match(c)]
                    if bad_primary:
                        errors.append(f"notion image {image.get('candidate_id')} has invalid primary colors: {bad_primary[:3]}")
                if "file" in image or "mtime" in image:
                    errors.append(f"notion image {image.get('candidate_id')} must not keep file or mtime")

    candidate_ids: set[str] = set()
    if not isinstance(notion_candidates, dict):
        errors.append("notion candidate file missing or invalid")
    else:
        candidates = notion_candidates.get("candidates", [])
        if not isinstance(candidates, list) or len(candidates) != 50:
            errors.append("notion candidate file must contain 50 image-level candidates")
            candidates = []
        for candidate in candidates:
            if not isinstance(candidate, dict):
                errors.append("notion candidate entry must be an object")
                continue
            cid = candidate.get("candidate_id")
            if not isinstance(cid, str) or not cid:
                errors.append("notion candidate missing candidate_id")
                continue
            if cid in candidate_ids:
                errors.append(f"duplicate notion candidate id: {cid}")
            candidate_ids.add(cid)
            if candidate.get("review_status") != "unreviewed":
                errors.append(f"{cid} must remain unreviewed")
            colors = candidate.get("colors", [])
            if not isinstance(colors, list) or not colors:
                errors.append(f"{cid} must contain colors")
            else:
                bad_colors = [c for c in colors if not isinstance(c, str) or not HEX.match(c)]
                if bad_colors:
                    errors.append(f"{cid} has invalid colors: {bad_colors[:3]}")
            if candidate.get("color_source") == "visible_hex_manual_transcription":
                if candidate.get("colors") != candidate.get("source_evidence", {}).get("visible_hex_colors"):
                    errors.append(f"{cid} colors must match visible_hex_colors evidence")
                if len(candidate.get("colors", [])) > 12:
                    if candidate.get("palette_role") != "composite" or candidate.get("snippet_eligibility") != "blocked":
                        errors.append(f"{cid} large transcribed color card must be composite and snippet-blocked")
                elif candidate.get("snippet_eligibility") != "requires_allow_experimental":
                    errors.append(f"{cid} transcribed candidate must require experimental snippet gate")
            elif candidate.get("snippet_eligibility") != "blocked":
                errors.append(f"{cid} non-transcribed candidate must be snippet-blocked")
            if not candidate.get("canonical_fallback_ids"):
                errors.append(f"{cid} missing canonical_fallback_ids")

    example_ids: set[str] = set()
    if not isinstance(figure_examples, dict):
        errors.append("figure example registry missing or invalid")
    else:
        examples = figure_examples.get("examples", [])
        if not isinstance(examples, list) or len(examples) < 51:
            errors.append("figure example registry must contain image examples and old-page example")
            examples = []
        for example in examples:
            if not isinstance(example, dict):
                continue
            example_id = example.get("example_id")
            if not isinstance(example_id, str) or not example_id:
                errors.append("figure example missing example_id")
                continue
            if example_id in example_ids:
                errors.append(f"duplicate example id: {example_id}")
            example_ids.add(example_id)
            for cid in example.get("linked_candidate_ids", []):
                if cid not in candidate_ids:
                    errors.append(f"example {example_id} references unknown candidate {cid}")

    if not isinstance(notion_review_queue, dict):
        errors.append("notion review queue missing or invalid")
    else:
        queue_ids = {entry.get("candidate_id") for entry in notion_review_queue.get("entries", []) if isinstance(entry, dict)}
        if candidate_ids and queue_ids != candidate_ids:
            errors.append("notion review queue must cover every candidate exactly")

    if not isinstance(publication_presets, dict):
        errors.append("publication presets missing or invalid")
    else:
        if publication_presets.get("version") != "2.0.0":
            errors.append("publication presets must be version 2.0.0")
        for preset in publication_presets.get("presets", []):
            if not isinstance(preset, dict):
                continue
            preset_id = preset.get("id", "<unknown>")
            for palette_id in preset.get("canonical_palette_ids", {}).values():
                if palette_id not in ids:
                    errors.append(f"preset {preset_id} references unknown canonical palette {palette_id}")
            for candidate_id in preset.get("style_candidate_ids", []):
                if candidate_id not in candidate_ids:
                    errors.append(f"preset {preset_id} references unknown candidate {candidate_id}")
            for example_id in preset.get("example_refs", []):
                if example_id not in example_ids:
                    errors.append(f"preset {preset_id} references unknown example {example_id}")
            if not preset.get("disclaimer"):
                errors.append(f"preset {preset_id} missing disclaimer")

    if not THIRD_PARTY_NOTICES.exists():
        errors.append("palette/THIRD_PARTY_NOTICES.md must exist")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: validated {len(palettes)} canonical palettes and {len(legacy_palettes)} legacy palettes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
