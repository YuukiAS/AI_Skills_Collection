#!/usr/bin/env python3
"""Read and format the canonical scientific figure palette library."""

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

PURPOSE_RECOMMENDATIONS: dict[str, list[str]] = {
    "categorical": ["okabe_ito", "Dark2", "Set2", "Paired"],
    "sequential": ["viridis", "cividis", "Blues", "YlGnBu", "OrRd"],
    "diverging": ["RdBu", "BrBG", "PuOr", "coolwarm"],
    "cyclic": ["twilight"],
    "journal": ["nature_npg", "science_aaas", "lancet"],
    "clinical": ["nejm", "lancet", "jama", "bmj", "jco"],
    "heatmap": ["viridis", "cividis", "RdBu", "BrBG"],
}

FIGURE_RECOMMENDATIONS: dict[str, list[str]] = {
    "line": ["okabe_ito", "cols4all_line7", "cols4all_line8", "tol_bright"],
    "scatter": ["okabe_ito", "cols4all_line7", "carto_safe"],
    "umap": ["okabe_ito", "cols4all_area7", "cols4all_friendly9"],
    "map": ["cols4all_area7", "cols4all_area8", "YlGnBu"],
    "heatmap": ["viridis", "cividis", "scico_batlow", "hcl_purple_green", "RdBu"],
    "bar": ["okabe_ito", "cols4all_friendly7", "Set2"],
    "schematic": ["okabe_ito", "cols4all_area7", "nature_npg"],
    "clinical": ["nejm", "lancet", "jama", "cols4all_friendly7"],
}


def default_library_path() -> Path:
    env_path = os.environ.get("AI_SKILLS_PALETTE_LIBRARY")
    if env_path:
        return Path(env_path)

    script_root = Path(__file__).resolve().parent
    candidates = [
        script_root.parent / "palette" / "scientific-figure-palettes.json",
        script_root.parent / "shared" / "palette" / "scientific-figure-palettes.json",
        Path.cwd() / "palette" / "scientific-figure-palettes.json",
        Path.cwd() / "shared" / "palette" / "scientific-figure-palettes.json",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return candidates[0]


def load_library(path: str | Path | None = None) -> Library:
    library_path = Path(path) if path else default_library_path()
    return json.loads(library_path.read_text(encoding="utf-8"))


def default_cols4all_path() -> Path:
    script_root = Path(__file__).resolve().parent
    candidates = [
        script_root.parent / "palette" / "external" / "cols4all-palettes.json",
        script_root.parent / "shared" / "palette" / "external" / "cols4all-palettes.json",
        Path.cwd() / "palette" / "external" / "cols4all-palettes.json",
        Path.cwd() / "shared" / "palette" / "external" / "cols4all-palettes.json",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return candidates[0]


def default_notion_path() -> Path:
    script_root = Path(__file__).resolve().parent
    candidates = [
        script_root.parent / "palette" / "notion-image-palettes.json",
        script_root.parent / "shared" / "palette" / "notion-image-palettes.json",
        Path.cwd() / "palette" / "notion-image-palettes.json",
        Path.cwd() / "shared" / "palette" / "notion-image-palettes.json",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return candidates[0]


def load_cols4all_library(path: str | Path | None = None) -> Library:
    library_path = Path(path) if path else default_cols4all_path()
    return json.loads(library_path.read_text(encoding="utf-8"))


def load_notion_library(path: str | Path | None = None) -> Library:
    library_path = Path(path) if path else default_notion_path()
    return json.loads(library_path.read_text(encoding="utf-8"))


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
        "recommended_for": [
            "external cols4all exploration",
            "publication figure candidate after license/provenance review",
        ],
        "avoid_for": ["default core palette unless source=cols4all/all is requested"],
        "colorblind_safe": {
            "source": "cols4all c4a_scores",
            "cbfriendly": palette.get("scores", {}).get("cbfriendly"),
        },
        "provenance_status": palette.get("provenance_status", "copied_from_cols4all_runtime_export"),
        "origins": [
            {
                "name": "cols4all",
                "url": "https://github.com/cols4all/cols4all-R",
                "usage": "copied GPL-3 palette colors from runtime export",
            }
        ],
        "stability": "external",
        "core": False,
        "license": palette.get("license", "GPL-3"),
        "source_id": source_id,
        "scores": palette.get("scores", {}),
    }


def _normalise_notion_page(page: Palette) -> Palette:
    images = page.get("images", [])
    colors = []
    if images:
        colors = images[0].get("picker_colors", [])
    return {
        "id": f"notion_{page.get('slug', '')}",
        "legacy_ids": [str(page.get("slug", "")), str(page.get("page_title", ""))],
        "name": str(page.get("page_title", "")),
        "family": "notion/image-derived",
        "type": "categorical",
        "colors": colors,
        "recommended_for": page.get("figure_uses", []),
        "avoid_for": ["core publication palette before manual picker review"],
        "colorblind_safe": {"source": "not_scored", "status": "needs_manual_review"},
        "provenance_status": "image_derived_needs_manual_review",
        "origins": [
            {
                "name": "Notion Skills Collection Type=Palette",
                "url": "local Notion page with latest image files in Downloads",
                "usage": str(page.get("action", "")),
            }
        ],
        "stability": "experimental",
        "core": False,
        "source_page": page.get("page_title", ""),
        "has_visible_hex_or_rgb": page.get("has_visible_hex_or_rgb"),
        "image_count": page.get("image_count", 0),
        "notes": page.get("notes", ""),
    }


def load_source_palettes(source: str = "canonical", core_only: bool = True) -> list[Palette]:
    palettes: list[Palette] = []
    if source in {"canonical", "all"}:
        palettes.extend(list_palettes(core_only=core_only))
    if source in {"cols4all", "all"}:
        palettes.extend(_normalise_cols4all_palette(palette) for palette in load_cols4all_library().get("palettes", []))
    if source in {"notion", "all"}:
        palettes.extend(_normalise_notion_page(page) for page in load_notion_library().get("pages", []))
    return palettes


def list_palettes(
    type: str | None = None,
    family: str | None = None,
    core_only: bool = True,
    library: Library | None = None,
    source: str = "canonical",
) -> list[Palette]:
    if source != "canonical" and library is None:
        palettes = load_source_palettes(source=source, core_only=core_only)
    else:
        data = library or load_library()
        palettes = data.get("palettes", [])
    result: list[Palette] = []
    for palette in palettes:
        if source == "canonical" and core_only and not palette.get("core", False):
            continue
        if type and palette.get("type") != type:
            continue
        if family and family.lower() not in str(palette.get("family", "")).lower():
            continue
        result.append(palette)
    return result


def get_palette(id_or_alias: str, library: Library | None = None, source: str = "canonical") -> Palette:
    if source != "canonical" and library is None:
        needle = id_or_alias.lower()
        for palette in load_source_palettes(source=source, core_only=False):
            aliases = [str(alias).lower() for alias in palette.get("legacy_ids", [])]
            if str(palette.get("id", "")).lower() == needle or needle in aliases:
                return palette
        raise KeyError(f"Unknown palette id or alias: {id_or_alias}")

    data = library or load_library()
    needle = id_or_alias.lower()
    for palette in data.get("palettes", []):
        aliases = [str(alias).lower() for alias in palette.get("legacy_ids", [])]
        if str(palette.get("id", "")).lower() == needle or needle in aliases:
            return palette
    raise KeyError(f"Unknown palette id or alias: {id_or_alias}")


def recommend_palette(purpose: str, library: Library | None = None, source: str = "canonical") -> list[Palette]:
    data = library or load_library()
    ids = PURPOSE_RECOMMENDATIONS.get(purpose)
    if ids is None:
        valid = ", ".join(sorted(PURPOSE_RECOMMENDATIONS))
        raise KeyError(f"Unknown purpose: {purpose}. Expected one of: {valid}")
    return [get_palette(palette_id, data if source == "canonical" else None, source=source) for palette_id in ids]


def recommend_for_figure(figure_type: str, source: str = "all") -> list[Palette]:
    ids = FIGURE_RECOMMENDATIONS.get(figure_type)
    if ids is None:
        valid = ", ".join(sorted(FIGURE_RECOMMENDATIONS))
        raise KeyError(f"Unknown figure type: {figure_type}. Expected one of: {valid}")
    return [get_palette(palette_id, source=source) for palette_id in ids]


def palette_to_snippet(palette: Palette, target: str) -> str:
    palette_id = str(palette["id"])
    colors = list(palette["colors"])
    colors_repr = repr(colors)
    palette_type = str(palette.get("type", "categorical"))
    disclaimer = ""
    if palette.get("is_official_branding") is False:
        disclaimer = "# Not official journal branding; verify accessibility before submission.\n"

    if target == "matplotlib":
        if palette_type == "categorical":
            return (
                f"{disclaimer}import matplotlib.pyplot as plt\n\n"
                f"{palette_id} = {colors_repr}\n"
                f"plt.rcParams['axes.prop_cycle'] = plt.cycler(color={palette_id})\n"
            )
        return (
            f"{disclaimer}from matplotlib.colors import ListedColormap\n\n"
            f"{palette_id}_colors = {colors_repr}\n"
            f"{palette_id}_cmap = ListedColormap({palette_id}_colors, name='{palette_id}')\n"
            "# Use with: ax.imshow(data, cmap={0}_cmap)\n".format(palette_id)
        )

    if target == "seaborn":
        if palette_type == "categorical":
            return (
                f"{disclaimer}import seaborn as sns\n\n"
                f"{palette_id} = {colors_repr}\n"
                f"sns.set_palette({palette_id})\n"
            )
        return (
            f"{disclaimer}import seaborn as sns\n\n"
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
                f"{disclaimer}import plotly.express as px\n\n"
                f"{palette_id} = {colors_repr}\n"
                f"# Use with: px.scatter(df, x='x', y='y', color='group', color_discrete_sequence={palette_id})\n"
            )
        return (
            f"{disclaimer}import plotly.express as px\n\n"
            f"{palette_id}_scale = {scale!r}\n"
            f"# Use with: px.imshow(data, color_continuous_scale={palette_id}_scale)\n"
        )

    if target == "latex":
        lines = [disclaimer.rstrip()] if disclaimer else []
        for index, color in enumerate(colors, start=1):
            lines.append(f"\\definecolor{{{palette_id}{index}}}{{HTML}}{{{color.lstrip('#')}}}")
        return "\n".join(line for line in lines if line) + "\n"

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
