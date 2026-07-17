#!/usr/bin/env python3
"""Read, recommend, and format scientific figure palette libraries."""

from __future__ import annotations

import json
import os
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
    "scatter": ["scatter"],
    "umap": ["umap", "single-cell", "biomedical"],
    "map": ["map", "spatial"],
    "heatmap": ["heatmap", "matrix", "density", "activation"],
    "bar": ["bar", "histogram", "distribution"],
    "histogram": ["histogram", "bar", "distribution"],
    "schematic": ["schematic", "pipeline", "codec"],
    "clinical": ["clinical", "cohort", "survival"],
}

VENUE_ALIASES = {
    "cvpr": "CVPR",
    "icml": "ICML",
    "aaai": "AAAI",
    "nature": "Nature",
    "general-journal": "general-journal",
    "journal": "general-journal",
    "clinical": "clinical",
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
    hints = FIGURE_PURPOSE_HINTS.get((figure_type or "").lower(), [figure_type] if figure_type else [])
    venue = VENUE_ALIASES.get((paper_venue or "").lower(), paper_venue or "")
    for preset in list_presets():
        if venue and venue.lower() not in {str(tag).lower() for tag in preset.get("venue_tags", [])}:
            continue
        if hints and not _text_match(preset.get("figure_type_tags", []), hints):
            continue
        result.append(preset)
    return result


def find_examples(
    figure_type: str | None = None,
    style_source: str | None = None,
    page: str | None = None,
    paper_venue: str | None = None,
) -> list[dict[str, Any]]:
    examples = list(load_example_registry().get("examples", []))
    hints = FIGURE_PURPOSE_HINTS.get((figure_type or "").lower(), [figure_type] if figure_type else [])
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
    return result


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


def palette_to_snippet(palette: Palette, target: str, allow_experimental: bool = False) -> str:
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
