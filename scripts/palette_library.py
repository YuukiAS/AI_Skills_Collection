#!/usr/bin/env python3
"""Read and format the canonical scientific figure palette library."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


Palette = dict[str, Any]
Library = dict[str, Any]


PURPOSE_RECOMMENDATIONS: dict[str, list[str]] = {
    "categorical": ["okabe_ito", "Dark2", "Set2", "Paired"],
    "sequential": ["viridis", "cividis", "Blues", "YlGnBu", "OrRd"],
    "diverging": ["RdBu", "BrBG", "PuOr", "coolwarm"],
    "cyclic": ["twilight"],
    "journal": ["nature_npg", "science_aaas", "lancet"],
    "clinical": ["nejm", "lancet", "jama", "bmj", "jco"],
    "heatmap": ["viridis", "cividis", "RdBu", "BrBG"],
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


def list_palettes(
    type: str | None = None,
    family: str | None = None,
    core_only: bool = True,
    library: Library | None = None,
) -> list[Palette]:
    data = library or load_library()
    palettes = data.get("palettes", [])
    result: list[Palette] = []
    for palette in palettes:
        if core_only and not palette.get("core", False):
            continue
        if type and palette.get("type") != type:
            continue
        if family and family.lower() not in str(palette.get("family", "")).lower():
            continue
        result.append(palette)
    return result


def get_palette(id_or_alias: str, library: Library | None = None) -> Palette:
    data = library or load_library()
    needle = id_or_alias.lower()
    for palette in data.get("palettes", []):
        aliases = [str(alias).lower() for alias in palette.get("legacy_ids", [])]
        if str(palette.get("id", "")).lower() == needle or needle in aliases:
            return palette
    raise KeyError(f"Unknown palette id or alias: {id_or_alias}")


def recommend_palette(purpose: str, library: Library | None = None) -> list[Palette]:
    data = library or load_library()
    ids = PURPOSE_RECOMMENDATIONS.get(purpose)
    if ids is None:
        valid = ", ".join(sorted(PURPOSE_RECOMMENDATIONS))
        raise KeyError(f"Unknown purpose: {purpose}. Expected one of: {valid}")
    return [get_palette(palette_id, data) for palette_id in ids]


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
