#!/usr/bin/env python3
"""Extract reviewable palette records from the latest Notion palette images."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image
from scipy import ndimage


DOWNLOADS = Path(r"C:\Users\yuukias\Downloads")
HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}")

MANUAL_VISIBLE_HEX: dict[tuple[str, int], list[str]] = {
    ("cvpr25", 1): ["#BFDCE7", "#DFEDF2", "#CAC2D7", "#DDD6E5", "#D9E4C2", "#F5D8BF", "#F9EDE0"],
    ("aaai", 1): ["#D9E7FA", "#ECECEC", "#D3E7D2", "#B8C6D1", "#F8F6E8", "#66AA9E", "#FFFED3", "#F8D8D3", "#FF8400", "#7DA5DE", "#FDD2CF", "#DFD3E6"],
    ("aaai", 2): ["#F4F0DE", "#DAEEC3", "#D6E9E0", "#ACD0C0", "#86BAA3", "#E1E1E1", "#CCCCCC", "#B7B7B7", "#D2DEEC", "#97AFD3", "#6689BD", "#4A74B1"],
    ("aaai", 3): ["#FFF5D5", "#CEE1F3", "#DEEBF7", "#B4C6E7", "#FAE4D5", "#C6E0B4", "#5D9FCC", "#9A4653", "#E2DC2F", "#6FA4A6", "#4470C3", "#6EAB46"],
    ("journal_reviewer_9", 2): ["#FBF6E3", "#FAE9C8", "#E3BDAA", "#7B9097"],
    ("journal_reviewer_9", 3): ["#C6D0D4", "#737B7B", "#383F0F", "#21220A"],
    ("journal_reviewer_9", 4): ["#C7ACB0", "#8188AD", "#594958", "#272B56"],
    ("journal_reviewer_9", 5): ["#E5EDE3", "#909C87", "#954738", "#39422F"],
    ("journal_reviewer_9", 6): ["#D2AD98", "#4B7FCC", "#225295", "#041E4F"],
    ("journal_reviewer_9", 7): ["#D5DBDC", "#86A1B1", "#295C6C", "#0D334A"],
    ("journal_reviewer_9", 8): ["#DEC19C", "#8D8089", "#59434E", "#3E495B"],
    ("journal_reviewer_9", 9): ["#DFC7BA", "#9298C6", "#37507E", "#161C2E"],
    ("journal_reviewer_9", 10): ["#B3C3B5", "#81B2AA", "#579186", "#174E42"],
    ("nature_inspiration", 1): ["#3D9F3C", "#9ED17B", "#367DB0", "#9DC7DD"],
    ("nature_inspiration", 2): ["#3D9F3C", "#9ED17B", "#367DB0", "#9DC7DD", "#519D78", "#8BCF8B", "#AADCA9", "#C4E9CA", "#DDF3DE", "#F3FBF2", "#5385BD", "#9BC7DF", "#DFF3F8", "#6CBAD8", "#96C2D4", "#BAD2E1", "#D8E5F7", "#DBF1FA"],
    ("nature_inspiration", 3): ["#3D9F3C", "#9ED17B", "#367DB0", "#9DC7DD"],
    ("nature_inspiration", 4): ["#BCF4C5", "#92C2A6", "#D6F6FF", "#ACEEFE", "#6FC8CA", "#58B8D1", "#3492B2", "#04579B"],
    ("nature_inspiration", 5): ["#6CBAD8", "#96C2D4", "#BAD2E1", "#D8E5F7", "#DBF1FA"],
    ("nature_inspiration", 6): ["#519D78", "#8BCF8B", "#AADCA9", "#C4E9CA", "#DDF3DE", "#F3FBF2", "#5385BD", "#9BC7DF", "#DFF3F8"],
    ("nature_inspiration", 7): ["#99BCAC", "#90B56D", "#97C87D", "#B9DF99"],
    ("nature_inspiration", 8): ["#0E600F", "#21AD5D", "#53BD7D", "#A1E7B8", "#191A94", "#7087E4", "#72C2FF", "#BFE9FE"],
    ("nature_same_palette", 1): ["#FFD6E7", "#FFB6D5", "#F7A1C4", "#E6F3FF", "#CDEBFA", "#B3E5FC", "#9ED8F5", "#81D4FA", "#90CAF9", "#B0BEC5", "#A7C7E7", "#7FB3F0", "#4D90FE", "#E8F0F8", "#FCE4EC", "#D9F0FA", "#EDE7F6", "#C7D6E6", "#8FB7E3", "#FFD1E1", "#BDBDBD", "#D0D0D0", "#E5E5E5", "#F8BBD0", "#90A4AE", "#B3E5FC"],
    ("nature_same_palette", 2): ["#CAE5F8", "#9DCBED", "#FAEFF5", "#F2C5DA", "#E286AF"],
    ("nature_same_palette", 3): ["#5271AE", "#70ACDE", "#F5CC7D", "#FFA660", "#D85B59"],
    ("nature_same_palette", 4): ["#FEEFF4", "#FBE0E9", "#F3C2D5", "#E69EB6", "#E282A7"],
    ("nature_same_palette", 5): ["#EDF2F6", "#DCE9F2", "#C2DBEF", "#97C2E4", "#4FA1D1"],
    ("nature_same_palette", 6): ["#DAE6F4", "#9EC5E4", "#67A5CC", "#FAE1E5", "#D780AA"],
    ("nature_same_palette", 7): ["#93C2E9", "#F5CDEF", "#F1BDC1", "#888888", "#D0D0CE"],
    ("nature_same_palette", 8): ["#4F587D", "#C68DC0", "#C2E0EE", "#776B97", "#DBC8ED"],
}


@dataclass(frozen=True)
class PagePlan:
    title: str
    slug: str
    pattern: str
    has_visible_hex: str
    action: str
    figure_uses: list[str]
    notes: str


PAGE_PLANS = [
    PagePlan(
        "CVPR25优质绘图学配色",
        "cvpr25",
        "CVPR25优质绘图学配色*.jpg",
        "yes",
        "parse_visible_hex_then_example",
        ["3D point cloud", "Gaussian splatting", "multi-panel computer vision figure"],
        "One latest image with visible bottom HEX labels; use as a computer-vision figure example and experimental palette.",
    ),
    PagePlan(
        "AAAI跟着顶会学配色",
        "aaai",
        "AAAI跟着顶会学配色*.jpg",
        "yes",
        "parse_visible_hex_then_picker_check",
        ["AI schematic", "codec pipeline", "benchmark panel", "histogram", "boxplot", "scatter density"],
        "Three images with visible RGB/HEX labels; picker output is kept for verification.",
    ),
    PagePlan(
        "攒了九组顶刊审稿人都挑不出毛病的配色",
        "journal_reviewer_9",
        "攒了九组顶刊审稿人都挑不出毛病的配色*.jpg",
        "yes",
        "parse_visible_hex_then_picker_check",
        ["journal-style categorical palette", "small multiples", "line chart", "bar chart"],
        "Nine card images in the latest batch; treat as aesthetic experimental palettes.",
    ),
    PagePlan(
        "ICML的清爽绘图风格！学了就能Accept‼️",
        "icml_clean",
        "ICML的清爽绘图风格*.jpg",
        "no",
        "derive_examples_first_palette_second",
        ["ICML-style schematic", "line chart", "attention heatmap", "model comparison figure"],
        "Three figures; mostly examples. Extracted colors need manual review before promotion.",
    ),
    PagePlan(
        "Nature顶刊配色灵感🌷",
        "nature_inspiration",
        "Nature顶刊配色灵感*.jpg",
        "mixed",
        "parse_visible_hex_and_picker",
        ["UMAP", "single-cell plot", "line/scatter series", "biomedical multi-panel"],
        "Eight images; several include visible HEX labels while dense figures need picker confirmation.",
    ),
    PagePlan(
        "顶刊配色直接抄！Nature同款色板也太绝了",
        "nature_same_palette",
        "顶刊配色直接抄！Nature同款色板也太绝了*.jpg",
        "yes",
        "parse_visible_hex_then_picker_check",
        ["UMAP", "activation heatmap", "ridge plot", "histogram", "Nature-inspired figure"],
        "Eight images with visible palette cards; non-official Nature-inspired experimental source.",
    ),
    PagePlan(
        "Python绘制高颜值柱状图展示数据分布",
        "python_bar_distribution",
        "Python绘制高颜值柱状图展示数据分布*.jpg",
        "no",
        "derive_bar_palette_and_example",
        ["histogram", "bar chart", "distribution comparison", "four-level categorical bars"],
        "Eighteen variants of the same bar/distribution example; use primarily as figure examples.",
    ),
    PagePlan(
        "Palettes and Typical Figures (Old)",
        "old_palettes_typical_figures",
        "Palettes and Typical Figures*.jpg",
        "unknown",
        "cols4all_only_plus_typical_examples",
        ["legacy typical figure examples"],
        "Old page is not imported as image palette; only cols4all is fused from this page direction.",
    ),
]


def hex_color(rgb: np.ndarray) -> str:
    rgb = np.clip(np.rint(rgb), 0, 255).astype(int)
    return "#{:02X}{:02X}{:02X}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))


def load_rgb(path: Path) -> np.ndarray | None:
    try:
        with Image.open(path) as img:
            return np.array(img.convert("RGB"))
    except Exception:
        return None


def dedupe_colors(colors: list[str], min_distance: int = 24) -> list[str]:
    result: list[str] = []
    vectors: list[np.ndarray] = []
    for color in colors:
        vec = np.array([int(color[i : i + 2], 16) for i in (1, 3, 5)])
        if all(np.linalg.norm(vec - existing) >= min_distance for existing in vectors):
            result.append(color)
            vectors.append(vec)
    return result


def swatch_colors(path: Path, count: int = 12) -> list[str]:
    rgb = load_rgb(path)
    if rgb is None:
        return []

    h, w = rgb.shape[:2]
    scale = min(1.0, 900 / max(h, w))
    if scale < 1:
        with Image.fromarray(rgb) as img:
            resized = img.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
            rgb = np.array(resized)
        h, w = rgb.shape[:2]

    # Most explicit palette cards live in the lower or middle-lower image area.
    # Keep enough vertical context for card-style screenshots, but avoid titles.
    y0 = int(h * 0.28)
    work = rgb[y0:, :, :].astype(np.int16)
    maxc = work.max(axis=2)
    minc = work.min(axis=2)
    sat = maxc - minc
    mean = work.mean(axis=2)
    mask = (sat > 14) & (mean > 35) & (mean < 245)

    labels, n_labels = ndimage.label(mask)
    candidates: list[tuple[int, int, int, int, int, str]] = []
    min_area = max(18, int(h * w * 0.00006))
    max_area = int(h * w * 0.025)
    for label in range(1, n_labels + 1):
        ys, xs = np.where(labels == label)
        area = len(xs)
        if area < min_area or area > max_area:
            continue
        x_min, x_max = int(xs.min()), int(xs.max())
        y_min, y_max = int(ys.min()), int(ys.max())
        bw = x_max - x_min + 1
        bh = y_max - y_min + 1
        if bw < 5 or bh < 5:
            continue
        aspect = bw / bh
        if aspect < 0.25 or aspect > 4.0:
            continue
        component_pixels = work[ys, xs, :]
        color = hex_color(np.median(component_pixels, axis=0))
        candidates.append((y_min + y0, x_min, area, bw, bh, color))

    # Palette cards usually appear as same-row swatches. Favor components with
    # similar y positions and left-to-right order, but keep figure bars/legends
    # as fallback for pages without explicit cards.
    candidates.sort(key=lambda item: (item[0] // 24, item[1]))
    colors = dedupe_colors([item[-1] for item in candidates], min_distance=18)
    return colors[:count]


def dominant_colors(path: Path, count: int = 8) -> list[str]:
    rgb = load_rgb(path)
    if rgb is None:
        return []
    h, w = rgb.shape[:2]
    crop = rgb[int(h * 0.55) :, :, :]
    pixels = crop.reshape(-1, 3)
    mask = (pixels.max(axis=1) - pixels.min(axis=1) > 18) & (pixels.mean(axis=1) < 245) & (pixels.mean(axis=1) > 20)
    pixels = pixels[mask]
    if len(pixels) < count:
        pixels = rgb.reshape(-1, 3)
    sample = pixels[:: max(1, len(pixels) // 50000)]
    if len(sample) < count:
        return [hex_color(color) for color in sample[:count]]

    # Quantized RGB bins are deterministic and enough for a review queue; final
    # promotion still requires manual picker confirmation.
    bins = (sample // 16).astype(int)
    frequencies = Counter(tuple(row) for row in bins)
    ordered = [np.array(key) * 16 + 8 for key, _freq in frequencies.most_common(count * 3)]
    colors: list[str] = []
    for center in ordered:
        color = hex_color(center)
        if color not in colors:
            colors.append(color)
        if len(colors) == count:
            break
    return colors


def page_files(plan: PagePlan, downloads: Path) -> list[Path]:
    return sorted(downloads.glob(plan.pattern), key=lambda path: path.stat().st_mtime, reverse=True)


def image_index(path: Path) -> int | None:
    matches = re.findall(r"_(\d+)_", path.name)
    if not matches:
        return None
    return int(matches[-1])


def color_source(plan: PagePlan, visible: list[str], picker: list[str]) -> str:
    if visible and plan.has_visible_hex in {"yes", "mixed"}:
        return "visible_palette_swatch_sample"
    if visible:
        return "figure_swatch_or_bar_sample"
    if picker:
        return "dominant_picker_fallback"
    return "none"


def confidence(plan: PagePlan, visible: list[str], picker: list[str]) -> str:
    if visible and plan.has_visible_hex == "yes":
        return "high_visible_swatch"
    if visible and plan.has_visible_hex == "mixed":
        return "medium_visible_or_figure_swatch"
    if visible:
        return "medium_figure_derived"
    if picker:
        return "low_picker_only"
    return "none"


def build_record(plan: PagePlan, files: list[Path]) -> dict[str, Any]:
    image_records = []
    for path in files:
        idx = image_index(path)
        visible_hex = MANUAL_VISIBLE_HEX.get((plan.slug, idx or -1), [])
        visible = swatch_colors(path)
        picker = dominant_colors(path)
        primary = visible_hex or visible or picker
        source = "visible_hex_manual_transcription" if visible_hex else color_source(plan, visible, picker)
        conf = "high_visible_hex_transcribed" if visible_hex else confidence(plan, visible, picker)
        image_records.append(
            {
                "file": str(path),
                "image_index": idx,
                "mtime": path.stat().st_mtime,
                "visible_hex_colors": visible_hex,
                "visible_palette_colors": visible,
                "picker_colors": picker,
                "primary_colors": primary,
                "color_source": source,
                "palette_confidence": conf,
                "review_status": "needs_manual_review",
                "extraction_method": "connected_swatch_detection_plus_dominant_fallback",
            }
        )
    return {
        "page_title": plan.title,
        "slug": plan.slug,
        "source": "Notion Skills Collection Type=Palette latest local Downloads batch",
        "has_visible_hex_or_rgb": plan.has_visible_hex,
        "action": plan.action,
        "figure_uses": plan.figure_uses,
        "notes": plan.notes,
        "image_count": len(files),
        "images": image_records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--downloads", type=Path, default=DOWNLOADS)
    parser.add_argument("--out", type=Path, default=Path("palette/notion-image-palettes.json"))
    args = parser.parse_args()

    pages = [build_record(plan, page_files(plan, args.downloads)) for plan in PAGE_PLANS]
    doc = {
        "library_id": "notion-image-palettes",
        "generated_on": datetime.now(timezone.utc).isoformat(),
        "scope": "latest local Downloads images corresponding to Notion Skills Collection Type=Palette pages",
        "default_policy": {
            "core": False,
            "stability": "experimental",
            "promotion_rule": "manual review plus cols4all/accessibility scoring required before moving into curated publication palettes",
        },
        "pages": pages,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {args.out} with {sum(page['image_count'] for page in pages)} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
