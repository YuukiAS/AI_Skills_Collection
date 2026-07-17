#!/usr/bin/env python3
"""Read, recommend, and format scientific figure palette libraries."""

from __future__ import annotations

import json
import os
from collections import defaultdict
from pathlib import Path
from typing import Any


Palette = dict[str, Any]
Library = dict[str, Any]


TYPE_ALIASES = {
    "cat": "categorical",
    "seq": "sequential",
    "div": "diverging",
    "cyc": "cyclic",
    "bivs": "bivariate",
    "bivc": "bivariate",
    "bivd": "bivariate",
    "bivg": "bivariate",
}

PURPOSE_TYPES = {
    "categorical": "categorical",
    "sequential": "sequential",
    "diverging": "diverging",
    "cyclic": "cyclic",
    "heatmap": "sequential",
}

FIGURE_PURPOSE_HINTS = {
    "line": ["line"],
    "line plot": ["line"],
    "scatter": ["scatter"],
    "umap": ["umap", "single-cell", "biomedical"],
    "map": ["map", "spatial"],
    "heatmap": ["heatmap", "matrix", "density", "activation"],
    "bar": ["bar", "histogram", "distribution"],
    "bar chart": ["bar", "histogram", "distribution"],
    "histogram": ["histogram", "bar", "distribution"],
    "schematic": ["schematic", "pipeline", "codec"],
    "benchmark": ["benchmark", "multi-panel"],
    "gaussian splatting": ["gaussian splatting", "3d point cloud", "computer vision"],
    "clinical": ["clinical", "cohort", "survival"],
}

VENUE_ALIASES = {
    "cvpr": "CVPR",
    "icml": "ICML",
    "aaai": "AAAI",
    "nature": "Nature",
    "general-journal": "general-journal",
    "journal": "general-journal",
    "general journal": "general-journal",
    "clinical": "clinical",
    "computer vision": "computer-vision",
    "computer-vision": "computer-vision",
    "biomedical": "biomedical",
}


def _candidate_paths(filename: str) -> list[Path]:
    script_root = Path(__file__).resolve().parent
    return [
        script_root.parent / "palette" / filename,
        script_root.parent / "shared" / "palette" / filename,
        Path.cwd() / "palette" / filename,
        Path.cwd() / "shared" / "palette" / filename,
    ]


def _first_existing(candidates: list[Path]) -> Path:
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return candidates[0]


def _load_json(path: str | Path) -> Library:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def default_library_path() -> Path:
    env_path = os.environ.get("AI_SKILLS_PALETTE_LIBRARY")
    if env_path:
        return Path(env_path)
    return _first_existing(_candidate_paths("scientific-figure-palettes.json"))


def default_cols4all_path() -> Path:
    script_root = Path(__file__).resolve().parent
    return _first_existing(
        [
            script_root.parent / "palette" / "external" / "cols4all-palettes.json",
            script_root.parent / "shared" / "palette" / "external" / "cols4all-palettes.json",
            Path.cwd() / "palette" / "external" / "cols4all-palettes.json",
            Path.cwd() / "shared" / "palette" / "external" / "cols4all-palettes.json",
        ]
    )


def load_canonical_library(path: str | Path | None = None) -> Library:
    return _load_json(Path(path) if path else default_library_path())


def load_library(path: str | Path | None = None) -> Library:
    return load_canonical_library(path)


def load_cols4all_library(path: str | Path | None = None) -> Library:
    return _load_json(Path(path) if path else default_cols4all_path())


def load_notion_evidence(path: str | Path | None = None) -> Library:
    return _load_json(Path(path) if path else _first_existing(_candidate_paths("notion-image-palettes.json")))


def load_notion_candidates(path: str | Path | None = None) -> Library:
    return _load_json(Path(path) if path else _first_existing(_candidate_paths("notion-palette-candidates.json")))


def load_example_registry(path: str | Path | None = None) -> Library:
    return _load_json(Path(path) if path else _first_existing(_candidate_paths("figure-example-registry.json")))


def load_publication_presets(path: str | Path | None = None) -> Library:
    return _load_json(Path(path) if path else _first_existing(_candidate_paths("publication-figure-presets.json")))


def _normalise_cols4all_palette(palette: Palette) -> Palette:
    source_id = str(palette.get("source_id", ""))
    public_id = source_id.replace(".", "_").replace("-", "_")
    if not public_id.startswith("cols4all_"):
        public_id = f"cols4all_{public_id}"
    return {
        "id": public_id,
        "legacy_ids": [source_id, str(palette.get("id", ""))],
        "name": str(palette.get("name") or source_id),
        "family": f"cols4all/{palette.get('series', '')}",
        "type": TYPE_ALIASES.get(str(palette.get("type")), str(palette.get("type"))),
        "colors": palette.get("colors", []),
        "recommended_for": ["external cols4all exploration"],
        "avoid_for": ["default recommendation unless cols4all/all is requested"],
        "colorblind_safe": {"source": "cols4all c4a_scores", "cbfriendly": palette.get("scores", {}).get("cbfriendly")},
        "provenance_status": palette.get("provenance_status", "copied_from_cols4all_runtime_export"),
        "origins": [{"name": "cols4all", "url": "https://github.com/cols4all/cols4all-R", "usage": "GPL-3 runtime export"}],
        "stability": "external",
        "core": False,
        "tier": "external_gpl_library",
        "recommendation_status": "explicit_external",
        "license": palette.get("license", "GPL-3"),
        "source": "cols4all",
        "source_id": source_id,
        "scores": palette.get("scores", {}),
    }


def _normalise_notion_candidate(candidate: Palette) -> Palette:
    return {
        "id": candidate["candidate_id"],
        "legacy_ids": candidate.get("legacy_ids", []),
        "name": f"{candidate.get('source_page_title', '')} / image {candidate.get('image_index')}",
        "family": "notion/image-derived",
        "type": candidate.get("type", "categorical"),
        "colors": candidate.get("colors", []),
        "recommended_for": candidate.get("figure_types", []),
        "avoid_for": ["default publication palette before manual review"],
        "colorblind_safe": {"source": "not_scored", "status": "needs_manual_review"},
        "provenance_status": "image_derived_unreviewed",
        "origins": [
            {
                "name": "Notion Skills Collection Type=Palette",
                "url": "derived metadata only; source image not redistributed",
                "usage": candidate.get("palette_role", "style_candidate"),
            }
        ],
        "stability": "experimental",
        "core": False,
        "tier": candidate.get("tier"),
        "recommendation_status": candidate.get("recommendation_status"),
        "snippet_eligibility": candidate.get("snippet_eligibility"),
        "review_status": candidate.get("review_status"),
        "palette_role": candidate.get("palette_role"),
        "source": "notion",
        "source_page_slug": candidate.get("source_page_slug"),
        "source_page_title": candidate.get("source_page_title"),
        "source_image_basename": candidate.get("source_image_basename"),
        "source_asset_committed": candidate.get("source_asset_committed"),
        "venue_tags": candidate.get("venue_tags", []),
        "canonical_fallback_ids": candidate.get("canonical_fallback_ids", []),
        "disclaimer": candidate.get("disclaimer", ""),
        "extraction_method": candidate.get("extraction_method", ""),
        "color_source": candidate.get("color_source", ""),
        "asset_kind": candidate.get("asset_kind", ""),
        "derivation_method": candidate.get("derivation_method", ""),
        "source_fidelity": candidate.get("source_fidelity", ""),
        "discovery_eligibility": candidate.get("discovery_eligibility", ""),
        "raw_snippet_eligibility": candidate.get("raw_snippet_eligibility", ""),
        "style_guidance_eligibility": candidate.get("style_guidance_eligibility", ""),
        "publication_status": candidate.get("publication_status", ""),
        "page_group_id": candidate.get("page_group_id", ""),
        "variant_rank": candidate.get("variant_rank"),
        "representative": candidate.get("representative", False),
    }


def canonical_palettes(core_only: bool = False, library: Library | None = None) -> list[Palette]:
    data = library or load_canonical_library()
    palettes = list(data.get("palettes", []))
    if core_only:
        palettes = [palette for palette in palettes if palette.get("core") is True]
    for palette in palettes:
        palette.setdefault("source", "canonical")
        palette.setdefault("tier", "core_publication" if palette.get("core") else "curated")
        palette.setdefault("recommendation_status", "default" if palette.get("core") else "explicit_only")
    return palettes


def notion_palettes() -> list[Palette]:
    return [_normalise_notion_candidate(candidate) for candidate in load_notion_candidates().get("candidates", [])]


def cols4all_palettes() -> list[Palette]:
    return [_normalise_cols4all_palette(palette) for palette in load_cols4all_library().get("palettes", [])]


def load_source_palettes(source: str = "canonical", core_only: bool = False) -> list[Palette]:
    palettes: list[Palette] = []
    if source in {"canonical", "all"}:
        palettes.extend(canonical_palettes(core_only=core_only))
    if source in {"notion", "all"}:
        palettes.extend(notion_palettes())
    if source in {"cols4all", "all"}:
        palettes.extend(cols4all_palettes())
    return palettes


def list_palettes(
    type: str | None = None,
    family: str | None = None,
    core_only: bool = False,
    library: Library | None = None,
    source: str = "canonical",
    tier: str | None = None,
    review_status: str | None = None,
    recommendation_status: str | None = None,
) -> list[Palette]:
    palettes = canonical_palettes(core_only=core_only, library=library) if source == "canonical" else load_source_palettes(source, core_only)
    result: list[Palette] = []
    for palette in palettes:
        if type and palette.get("type") != type:
            continue
        if family and family.lower() not in str(palette.get("family", "")).lower():
            continue
        if tier and palette.get("tier") != tier:
            continue
        if review_status and palette.get("review_status") != review_status:
            continue
        if recommendation_status and palette.get("recommendation_status") != recommendation_status:
            continue
        result.append(palette)
    return result


def resolve_palette(id_or_alias: str, source: str = "canonical", library: Library | None = None) -> Palette:
    needle = id_or_alias.lower()
    palettes = canonical_palettes(library=library) if source == "canonical" else load_source_palettes(source)
    matches: list[Palette] = []
    ambiguous_candidates: list[str] = []
    for palette in palettes:
        aliases = [str(alias).lower() for alias in palette.get("legacy_ids", [])]
        pid = str(palette.get("id", "")).lower()
        if pid == needle or needle in aliases:
            matches.append(palette)
        if palette.get("source") == "notion" and needle == f"notion_{palette.get('source_page_slug', '')}".lower():
            ambiguous_candidates.append(str(palette["id"]))
    if len(matches) > 1 and all(match.get("source") == "notion" for match in matches):
        raise KeyError(
            f"Ambiguous Notion page alias {id_or_alias}; use one of: {', '.join(sorted(str(match['id']) for match in matches))}"
        )
    if matches:
        return matches[0]
    if ambiguous_candidates:
        if len(ambiguous_candidates) == 1:
            return resolve_palette(ambiguous_candidates[0], source=source)
        raise KeyError(
            f"Ambiguous Notion page alias {id_or_alias}; use one of: {', '.join(sorted(ambiguous_candidates))}"
        )
    raise KeyError(f"Unknown palette id or alias: {id_or_alias}")


def get_palette(id_or_alias: str, library: Library | None = None, source: str = "canonical") -> Palette:
    return resolve_palette(id_or_alias, source=source, library=library)


def _text_match(values: list[str], hints: list[str]) -> bool:
    haystack = " ".join(str(value).lower() for value in values)
    return any(hint.lower() in haystack for hint in hints)


def _venue_match(palette: Palette, paper_venue: str | None) -> bool:
    if not paper_venue:
        return True
    target = VENUE_ALIASES.get(paper_venue.lower(), paper_venue)
    return target.lower() in {str(tag).lower() for tag in palette.get("venue_tags", [])}


def _context_hints(figure_type: str | None = None, purpose: str | None = None, domain: str | None = None) -> list[str]:
    hints: list[str] = []
    if figure_type:
        hints.extend(FIGURE_PURPOSE_HINTS.get(figure_type.lower(), [figure_type]))
    if purpose:
        hints.extend(FIGURE_PURPOSE_HINTS.get(purpose.lower(), [purpose]))
    if domain:
        hints.extend(FIGURE_PURPOSE_HINTS.get(domain.lower(), [domain]))
    return [str(hint).lower() for hint in hints if hint]


def _limit_by_page(items: list[dict[str, Any]], limit_per_page: int = 3) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in items:
        grouped[str(item.get("page_group_id") or item.get("source_page_slug") or "ungrouped")].append(item)
    limited: list[dict[str, Any]] = []
    for group_items in grouped.values():
        ordered = sorted(
            group_items,
            key=lambda item: (
                not bool(item.get("representative")),
                int(item.get("variant_rank") or item.get("image_index") or 999),
                str(item.get("candidate_id") or item.get("example_id") or item.get("id")),
            ),
        )
        limited.extend(ordered[:limit_per_page])
    return limited


def _page_summary(page: dict[str, Any]) -> dict[str, Any]:
    return {
        "slug": page.get("slug"),
        "page_title": page.get("page_title"),
        "image_count": page.get("image_count"),
        "has_visible_hex_or_rgb": page.get("has_visible_hex_or_rgb"),
        "figure_uses": page.get("figure_uses", []),
        "notes": page.get("notes", ""),
        "source_asset_committed": page.get("source_asset_committed"),
        "source_locator_status": page.get("source_locator_status"),
    }


def recommend_palettes(
    purpose: str | None = None,
    figure_type: str | None = None,
    paper_venue: str | None = None,
    style_source: str = "core",
    source: str = "canonical",
    include_experimental: bool = False,
) -> list[Palette]:
    source = "all" if style_source in {"all", "notion", "cols4all", "journal"} else source
    palettes = load_source_palettes(source=source, core_only=False)
    result: list[tuple[int, Palette]] = []
    purpose_type = PURPOSE_TYPES.get(purpose or "")
    figure_hints = FIGURE_PURPOSE_HINTS.get((figure_type or "").lower(), [figure_type] if figure_type else [])
    for palette in palettes:
        tier = str(palette.get("tier", ""))
        palette_source = palette.get("source")
        if palette.get("recommendation_status") == "blocked":
            continue
        if style_source == "core" and tier != "core_publication":
            continue
        if style_source == "journal" and tier not in {"core_publication", "journal_inspired_nonofficial"}:
            continue
        if style_source == "notion" and palette_source != "notion":
            continue
        if style_source == "cols4all" and palette_source != "cols4all":
            continue
        if palette_source == "notion" and style_source not in {"notion", "all"}:
            continue
        if palette_source == "notion" and not include_experimental and not (paper_venue or figure_type):
            continue
        if palette_source == "notion" and palette.get("recommendation_status") == "inspiration_only" and style_source != "all":
            continue
        if purpose_type and palette.get("type") != purpose_type and purpose != "heatmap":
            continue
        if figure_hints and not _text_match(palette.get("recommended_for", []), figure_hints):
            continue
        if not _venue_match(palette, paper_venue):
            continue
        score = 0
        if tier == "core_publication":
            score += 100
        elif tier == "journal_inspired_nonofficial":
            score += 70
        elif palette_source == "notion":
            score += 60
        elif tier == "curated_external_gpl":
            score += 50
        if paper_venue and _venue_match(palette, paper_venue):
            score += 20
        if figure_hints and _text_match(palette.get("recommended_for", []), figure_hints):
            score += 20
        result.append((score, palette))
    result.sort(key=lambda item: (-item[0], str(item[1].get("id", ""))))
    if not result and style_source == "core":
        return _safe_fallback_palettes(purpose=purpose, figure_type=figure_type)
    return [palette for _, palette in result[:12]]


def recommend_palette(purpose: str, library: Library | None = None, source: str = "canonical") -> list[Palette]:
    return recommend_palettes(purpose=purpose, source=source, style_source="core" if source == "canonical" else "all")


def recommend_for_figure(figure_type: str, source: str = "all") -> list[Palette]:
    style_source = "all" if source == "all" else source
    return recommend_palettes(figure_type=figure_type, source=source, style_source=style_source)


def list_presets() -> list[dict[str, Any]]:
    return list(load_publication_presets().get("presets", []))


def get_preset(preset_id: str) -> dict[str, Any]:
    for preset in list_presets():
        if preset.get("id") == preset_id:
            return preset
    raise KeyError(f"Unknown preset id: {preset_id}")


def recommend_presets(paper_venue: str | None = None, figure_type: str | None = None) -> list[dict[str, Any]]:
    result = []
    hints = _context_hints(figure_type=figure_type)
    venue = VENUE_ALIASES.get((paper_venue or "").lower(), paper_venue or "")
    for preset in list_presets():
        venue_values = preset.get("venue_tags", []) + preset.get("venue_aliases", [])
        figure_values = preset.get("figure_type_tags", []) + preset.get("figure_type_aliases", [])
        if venue and venue.lower() not in {str(tag).lower() for tag in venue_values}:
            continue
        if hints and not _text_match(figure_values, hints):
            continue
        result.append(preset)
    return result


def find_examples(
    figure_type: str | None = None,
    style_source: str | None = None,
    page: str | None = None,
    paper_venue: str | None = None,
    limit_per_page: int | None = None,
    representative_first: bool = True,
) -> list[dict[str, Any]]:
    examples = list(load_example_registry().get("examples", []))
    hints = _context_hints(figure_type=figure_type)
    venue = VENUE_ALIASES.get((paper_venue or "").lower(), paper_venue or "")
    result = []
    for example in examples:
        if page and example.get("source_page_slug") != page:
            continue
        if style_source and style_source not in {"notion", "all"}:
            continue
        if hints and not _text_match(example.get("figure_type_tags", []), hints):
            continue
        if venue and venue.lower() not in {str(tag).lower() for tag in example.get("venue_tags", [])}:
            continue
        result.append(example)
    if representative_first:
        result.sort(
            key=lambda item: (
                not bool(item.get("representative")),
                int(item.get("discovery_rank") or item.get("variant_rank") or 999),
                str(item.get("example_id")),
            )
        )
    if limit_per_page:
        result = _limit_by_page(result, limit_per_page=limit_per_page)
    return result


def search_notion_pages(
    paper_venue: str | None = None,
    figure_type: str | None = None,
    query: str | None = None,
) -> list[dict[str, Any]]:
    hints = _context_hints(figure_type=figure_type, domain=query)
    venue = VENUE_ALIASES.get((paper_venue or "").lower(), paper_venue or "")
    result = []
    for page in load_notion_evidence().get("pages", []):
        values = [
            page.get("slug", ""),
            page.get("page_title", ""),
            page.get("notes", ""),
            *page.get("figure_uses", []),
        ]
        if venue and venue.lower() not in " ".join(str(value).lower() for value in values):
            continue
        if hints and not _text_match([str(value) for value in values], hints):
            continue
        result.append(_page_summary(page))
    return result


def search_notion_candidates(
    paper_venue: str | None = None,
    figure_type: str | None = None,
    role: str | None = None,
    query: str | None = None,
    limit_per_page: int | None = 3,
    include_guidance_only: bool = True,
) -> list[Palette]:
    hints = _context_hints(figure_type=figure_type, domain=query)
    venue = VENUE_ALIASES.get((paper_venue or "").lower(), paper_venue or "")
    result: list[Palette] = []
    for palette in notion_palettes():
        if role and palette.get("palette_role") != role and palette.get("asset_kind") != role:
            continue
        if palette.get("discovery_eligibility") == "blocked":
            continue
        if palette.get("discovery_eligibility") == "guidance_only" and not include_guidance_only:
            continue
        values = [
            palette.get("id", ""),
            palette.get("source_page_slug", ""),
            palette.get("source_page_title", ""),
            palette.get("palette_role", ""),
            palette.get("asset_kind", ""),
            *palette.get("recommended_for", []),
            *palette.get("venue_tags", []),
        ]
        if venue and venue.lower() not in {str(tag).lower() for tag in palette.get("venue_tags", [])}:
            continue
        if hints and not _text_match([str(value) for value in values], hints):
            continue
        result.append(palette)
    result.sort(
        key=lambda item: (
            item.get("discovery_eligibility") != "contextual_default",
            not bool(item.get("representative")),
            int(item.get("variant_rank") or 999),
            str(item.get("id")),
        )
    )
    if limit_per_page:
        result = _limit_by_page(result, limit_per_page=limit_per_page)
    return result


def _safe_fallback_palettes(purpose: str | None = None, figure_type: str | None = None) -> list[Palette]:
    preferred: list[str]
    context = " ".join(str(item or "").lower() for item in [purpose, figure_type])
    if any(term in context for term in ("heatmap", "density", "matrix", "umap")):
        preferred = ["viridis", "cividis", "Blues"]
    elif any(term in context for term in ("diverging", "correlation", "residual", "difference")):
        preferred = ["RdBu", "BrBG", "PuOr"]
    else:
        preferred = ["okabe_ito", "Dark2", "Set2"]
    by_id = {palette["id"]: palette for palette in canonical_palettes(core_only=True)}
    return [by_id[pid] for pid in preferred if pid in by_id]


def discover_context(
    purpose: str | None = None,
    figure_type: str | None = None,
    paper_venue: str | None = None,
    domain: str | None = None,
    limit_per_page: int = 3,
) -> dict[str, Any]:
    safe_palettes = recommend_palettes(
        purpose=purpose,
        figure_type=figure_type,
        paper_venue=paper_venue,
        style_source="core",
        source="canonical",
        include_experimental=False,
    )
    if not safe_palettes:
        safe_palettes = _safe_fallback_palettes(purpose=purpose, figure_type=figure_type)
    contextual_presets = recommend_presets(paper_venue=paper_venue or domain, figure_type=figure_type or purpose)
    notion_pages = search_notion_pages(paper_venue=paper_venue or domain, figure_type=figure_type or purpose)
    candidates = search_notion_candidates(
        paper_venue=paper_venue or domain,
        figure_type=figure_type or purpose,
        query=domain,
        limit_per_page=limit_per_page,
        include_guidance_only=True,
    )
    experimental_candidates = [
        candidate for candidate in candidates if candidate.get("discovery_eligibility") == "contextual_default"
    ]
    guidance_only = [
        candidate for candidate in candidates if candidate.get("discovery_eligibility") == "guidance_only"
    ]
    figure_examples = find_examples(
        figure_type=figure_type or purpose,
        style_source="notion",
        paper_venue=paper_venue or domain,
        limit_per_page=limit_per_page,
    )
    warnings = [
        "Notion-derived candidates are unreviewed, non-official, and not publication-safe defaults.",
        "Use canonical safe palettes for default plotting snippets.",
    ]
    if experimental_candidates:
        warnings.append("Raw color snippets for transcribed Notion candidates still require --allow-experimental.")
    if guidance_only:
        warnings.append("Guidance-only candidates are not eligible for raw color snippets.")
    return {
        "safe_palettes": safe_palettes,
        "contextual_presets": contextual_presets,
        "notion_pages": notion_pages,
        "experimental_candidates": experimental_candidates,
        "figure_examples": figure_examples,
        "guidance_only": guidance_only,
        "warnings": warnings,
    }


def explain_item(item_id: str) -> dict[str, Any]:
    try:
        palette = get_palette(item_id, source="all")
        return {"kind": "palette", "item": palette}
    except KeyError:
        pass
    for preset in list_presets():
        if preset.get("id") == item_id:
            return {"kind": "preset", "item": preset}
    for example in load_example_registry().get("examples", []):
        if example.get("example_id") == item_id:
            return {"kind": "example", "item": example}
    for page in load_notion_evidence().get("pages", []):
        if page.get("slug") == item_id:
            return {"kind": "notion_page", "item": _page_summary(page)}
    raise KeyError(f"Unknown palette discovery item: {item_id}")


def compare_items(item_ids: list[str], paper_venue: str | None = None, figure_type: str | None = None) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item_id in item_ids:
        explained = explain_item(item_id)
        item = explained["item"]
        rows.append(
            {
                "id": item.get("id") or item.get("candidate_id") or item.get("example_id") or item.get("slug"),
                "kind": explained["kind"],
                "type": item.get("type", ""),
                "colors": len(item.get("colors", [])) if isinstance(item.get("colors"), list) else "",
                "tier": item.get("tier", ""),
                "review_status": item.get("review_status", ""),
                "discovery_eligibility": item.get("discovery_eligibility", ""),
                "raw_snippet_eligibility": item.get("raw_snippet_eligibility", item.get("snippet_eligibility", "")),
                "venue_match": _venue_match(item, paper_venue) if explained["kind"] == "palette" else "",
                "figure_match": _text_match(item.get("recommended_for", item.get("figure_type_tags", [])), _context_hints(figure_type=figure_type))
                if figure_type
                else "",
                "fallback": item.get("canonical_fallback_ids", []),
                "disclaimer": item.get("disclaimer", ""),
            }
        )
    return rows


def style_guidance(item_id: str, target: str = "json") -> dict[str, Any] | str:
    palette = get_palette(item_id, source="all")
    if palette.get("source") != "notion":
        guidance = {
            "id": palette["id"],
            "status": "canonical_or_external_palette",
            "message": "Use normal snippets for reviewed canonical palettes; keep license and disclaimer visible for non-core palettes.",
        }
    else:
        guidance = {
            "id": palette["id"],
            "source_page_slug": palette.get("source_page_slug"),
            "review_status": palette.get("review_status"),
            "source_fidelity": palette.get("source_fidelity"),
            "discovery_eligibility": palette.get("discovery_eligibility"),
            "raw_snippet_eligibility": palette.get("raw_snippet_eligibility"),
            "canonical_fallback_ids": palette.get("canonical_fallback_ids", []),
            "style_rules": [
                "Treat this as non-official visual inspiration, not as a publication-safe palette.",
                "Use canonical fallback palettes for final plots unless the user explicitly accepts experimental colors.",
                "Preserve redundant encodings such as markers, line styles, labels, or hatching.",
            ],
            "disclaimer": palette.get("disclaimer", ""),
        }
    if target == "json":
        return guidance
    lines = [
        f"# Style guidance for {guidance['id']}",
        f"# Review status: {guidance.get('review_status', '-')}",
        f"# Raw snippet eligibility: {guidance.get('raw_snippet_eligibility', '-')}",
    ]
    for fallback in guidance.get("canonical_fallback_ids", []):
        lines.append(f"# Canonical fallback: {fallback}")
    for rule in guidance.get("style_rules", []):
        lines.append(f"# {rule}")
    return "\n".join(lines) + "\n"


def _snippet_header(palette: Palette) -> str:
    if palette.get("source") != "notion":
        if palette.get("is_official_branding") is False:
            return "# Not official journal branding; verify accessibility before submission.\n"
        return ""
    return (
        f"# Experimental Notion-derived palette: {palette['id']}\n"
        f"# Source page: {palette.get('source_page_slug')} / {palette.get('source_page_title')}\n"
        f"# Extraction: {palette.get('color_source')} via {palette.get('extraction_method')}\n"
        f"# Review status: {palette.get('review_status')}\n"
        f"# Disclaimer: {palette.get('disclaimer')}\n"
    )


def palette_to_snippet(palette: Palette, target: str, allow_experimental: bool = False, kind: str = "raw-colors") -> str:
    if kind == "style-tokens":
        return style_guidance(str(palette["id"]), target=target)  # type: ignore[return-value]
    eligibility = palette.get("snippet_eligibility")
    if eligibility == "blocked":
        raise ValueError(f"{palette['id']} is not eligible for snippets: {palette.get('palette_role')} / {palette.get('color_source')}")
    if eligibility == "requires_allow_experimental" and not allow_experimental:
        raise ValueError(f"{palette['id']} is unreviewed and requires --allow-experimental for snippets")

    palette_id = str(palette["id"])
    colors = list(palette["colors"])
    colors_repr = repr(colors)
    palette_type = str(palette.get("type", "categorical"))
    header = _snippet_header(palette)

    if target == "matplotlib":
        if palette_type == "categorical":
            return (
                f"{header}import matplotlib.pyplot as plt\n\n"
                f"{palette_id} = {colors_repr}\n"
                f"plt.rcParams['axes.prop_cycle'] = plt.cycler(color={palette_id})\n"
            )
        return (
            f"{header}from matplotlib.colors import ListedColormap\n\n"
            f"{palette_id}_colors = {colors_repr}\n"
            f"{palette_id}_cmap = ListedColormap({palette_id}_colors, name='{palette_id}')\n"
            "# Use with: ax.imshow(data, cmap={0}_cmap)\n".format(palette_id)
        )

    if target == "seaborn":
        if palette_type == "categorical":
            return f"{header}import seaborn as sns\n\n{palette_id} = {colors_repr}\nsns.set_palette({palette_id})\n"
        return (
            f"{header}import seaborn as sns\n\n"
            f"{palette_id}_colors = {colors_repr}\n"
            f"{palette_id}_cmap = sns.color_palette({palette_id}_colors, as_cmap=True)\n"
            "# Use with: sns.heatmap(data, cmap={0}_cmap)\n".format(palette_id)
        )

    if target == "plotly":
        if len(colors) == 1:
            scale = [(0, colors[0]), (1, colors[0])]
        else:
            scale = [(round(i / (len(colors) - 1), 4), color) for i, color in enumerate(colors)]
        if palette_type == "categorical":
            return (
                f"{header}import plotly.express as px\n\n"
                f"{palette_id} = {colors_repr}\n"
                f"# Use with: px.scatter(df, x='x', y='y', color='group', color_discrete_sequence={palette_id})\n"
            )
        return f"{header}import plotly.express as px\n\n{palette_id}_scale = {scale!r}\n"

    if target == "latex":
        lines = [line for line in header.rstrip().splitlines() if line]
        for index, color in enumerate(colors, start=1):
            lines.append(f"\\definecolor{{{palette_id}{index}}}{{HTML}}{{{color.lstrip('#')}}}")
        return "\n".join(lines) + "\n"

    raise KeyError(f"Unknown snippet target: {target}")


def format_palette(palette: Palette, format: str) -> str:
    if format == "json":
        return json.dumps(palette, ensure_ascii=False, indent=2)
    if format == "hex":
        return "\n".join(palette["colors"])
    if format == "python":
        return f"{palette['id']} = {palette['colors']!r}"
    if format == "css":
        return "\n".join(
            f"--palette-{palette['id']}-{index}: {color};"
            for index, color in enumerate(palette["colors"], start=1)
        )
    raise KeyError(f"Unknown output format: {format}")
