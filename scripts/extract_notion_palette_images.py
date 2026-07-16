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


DOWNLOADS = Path(r"C:\Users\yuukias\Downloads")
HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}")


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
        "no",
        "derive_palette_and_example",
        ["3D point cloud", "Gaussian splatting", "multi-panel computer vision figure"],
        "One latest image; bottom swatches require picker extraction.",
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


def dominant_colors(path: Path, count: int = 8) -> list[str]:
    try:
        with Image.open(path) as img:
            rgb = np.array(img.convert("RGB"))
    except Exception:
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


def build_record(plan: PagePlan, files: list[Path]) -> dict[str, Any]:
    image_records = []
    for path in files:
        image_records.append(
            {
                "file": str(path),
                "mtime": path.stat().st_mtime,
                "picker_colors": dominant_colors(path),
                "review_status": "needs_manual_review",
                "extraction_method": "opencv_kmeans_bottom_crop",
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
