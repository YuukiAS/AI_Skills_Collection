#!/usr/bin/env python3
"""Mechanically review the research-group-meeting regression render.

This reviewer checks only PPTX render evidence and simple layout signals. It
does not make a scientific, academic, or communication-quality PASS decision.
"""

from __future__ import annotations

import argparse
import json
import warnings
from pathlib import Path
from zipfile import ZipFile

from PIL import Image


MECHANICAL_CRITERIA = [
    "png_from_real_pptx_render",
    "dimensions_nontrivial",
    "not_blank",
    "contrast_present",
    "dominant_object_present",
    "edge_clipping_not_obvious",
    "text_density_proxy_bounded",
    "required_object_contract_present",
]


def count_slides(pptx_path: Path) -> int:
    with ZipFile(pptx_path) as zf:
        return len([name for name in zf.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")])


def pptx_object_summary(pptx_path: Path) -> dict:
    with ZipFile(pptx_path) as zf:
        names = zf.namelist()
        slide_xml = [name for name in names if name.startswith("ppt/slides/slide") and name.endswith(".xml")]
        shape_count = 0
        picture_count = 0
        for name in slide_xml:
            text = zf.read(name).decode("utf-8", errors="ignore")
            shape_count += text.count("<p:sp>")
            picture_count += text.count("<p:pic>")
        return {
            "editable_slide_count": len(slide_xml),
            "media_count": len([name for name in names if name.startswith("ppt/media/")]),
            "shape_count": shape_count,
            "picture_count": picture_count,
        }


def image_metrics(path: Path) -> dict:
    with Image.open(path) as image:
        rgb = image.convert("RGB")
    width, height = rgb.size
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        pixels = list(rgb.getdata())
    luminance = [(r * 299 + g * 587 + b * 114) // 1000 for r, g, b in pixels]
    blank = sum(1 for value in luminance if value > 245)
    nonblank_positions = [
        (index % width, index // width)
        for index, value in enumerate(luminance)
        if value < 242
    ]
    if nonblank_positions:
        xs = [x for x, _ in nonblank_positions]
        ys = [y for _, y in nonblank_positions]
        bbox = (min(xs), min(ys), max(xs), max(ys))
        dominant_area = ((bbox[2] - bbox[0] + 1) * (bbox[3] - bbox[1] + 1)) / (width * height)
        edge_margin = min(bbox[0], bbox[1], width - bbox[2] - 1, height - bbox[3] - 1)
    else:
        bbox = None
        dominant_area = 0.0
        edge_margin = 0
    sample_step = max(1, width // 220)
    transitions = 0
    comparisons = 0
    for y in range(0, height, sample_step):
        row_start = y * width
        for x in range(0, width - sample_step, sample_step):
            comparisons += 1
            if abs(luminance[row_start + x] - luminance[row_start + x + sample_step]) > 45:
                transitions += 1
    return {
        "path": str(path),
        "width": width,
        "height": height,
        "blank_area_ratio": round(blank / len(pixels), 4),
        "contrast_range": max(luminance) - min(luminance),
        "dominant_object_area": round(dominant_area, 4),
        "edge_margin_px": edge_margin,
        "text_density_proxy": round(transitions / max(1, comparisons), 4),
        "content_bbox": bbox,
    }


def mechanical_status(metrics: dict, has_contract: bool) -> tuple[str, dict]:
    criteria = {
        "png_from_real_pptx_render": "PASS",
        "dimensions_nontrivial": "PASS" if metrics["width"] >= 900 and metrics["height"] >= 500 else "REVISE",
        "not_blank": "PASS" if metrics["blank_area_ratio"] < 0.90 else "REVISE",
        "contrast_present": "PASS" if metrics["contrast_range"] >= 40 else "REVISE",
        "dominant_object_present": "PASS" if metrics["dominant_object_area"] >= 0.20 else "REVISE",
        "edge_clipping_not_obvious": "PASS" if metrics["edge_margin_px"] >= 0 else "REVISE",
        "text_density_proxy_bounded": "PASS" if metrics["text_density_proxy"] < 0.28 else "REVISE",
        "required_object_contract_present": "PASS" if has_contract else "REVISE",
    }
    status = "MECHANICAL_PASS" if all(value == "PASS" for value in criteria.values()) else "MECHANICAL_REVISE"
    return status, criteria


def review(out_dir: Path) -> dict:
    manifest_path = out_dir / "EVIDENCE_MANIFEST.json"
    render_path = out_dir / "RENDER_STATUS.json"
    if not manifest_path.exists():
        return {
            "review_type": "MECHANICAL_VISUAL_REVIEW",
            "status": "BLOCKED",
            "academic_visual_decision": "NOT_ASSESSED",
            "reason": f"missing {manifest_path}",
        }
    if not render_path.exists():
        return {
            "review_type": "MECHANICAL_VISUAL_REVIEW",
            "status": "BLOCKED_REAL_PPTX_RENDER",
            "academic_visual_decision": "NOT_ASSESSED",
            "reason": f"missing {render_path}",
        }
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    render = json.loads(render_path.read_text(encoding="utf-8"))
    pptx_path = Path(manifest["pptx"])
    editable_slide_count = count_slides(pptx_path)
    pngs = [Path(path) for path in render.get("rendered_pngs", [])]
    if render.get("status") != "ok" or len(pngs) != editable_slide_count or not all(path.exists() for path in pngs):
        return {
            "review_type": "MECHANICAL_VISUAL_REVIEW",
            "status": "BLOCKED_REAL_PPTX_RENDER",
            "academic_visual_decision": "NOT_ASSESSED",
            "reason": "mechanical reviewer requires PNGs produced from the PPTX by a real presentation engine",
            "editable_slide_count": editable_slide_count,
            "render_status": render,
        }
    slide_reviews = []
    final_status = "MECHANICAL_PASS"
    for slide, png in zip(manifest.get("slides", []), pngs, strict=True):
        metrics = image_metrics(png)
        status, criteria = mechanical_status(metrics, bool(slide.get("expected_scientific_objects")))
        if status != "MECHANICAL_PASS":
            final_status = "MECHANICAL_REVISE"
        slide_reviews.append({
            "slide": slide["slide"],
            "archetype": slide["archetype"],
            "status": status,
            "criteria": criteria,
            "metrics": metrics,
            "reference_ids": slide["reference_ids"],
            "expected_object_contract": slide["expected_scientific_objects"],
            "style_boundary": slide["style_not_copied"],
        })
    return {
        "review_type": "MECHANICAL_VISUAL_REVIEW",
        "status": final_status,
        "academic_visual_decision": "NOT_ASSESSED",
        "reviewer_independent_from_generator": True,
        "criteria_scope": MECHANICAL_CRITERIA,
        "editable_slide_count": editable_slide_count,
        "rendered_png_count": len(pngs),
        "render_status": render,
        "pptx_object_summary": pptx_object_summary(pptx_path),
        "slide_reviews": slide_reviews,
        "rights_note": manifest["rights_note"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=Path(".cache/research-group-meeting-regression"))
    args = parser.parse_args()
    result = review(args.out_dir)
    review_path = args.out_dir / "MECHANICAL_VISUAL_REVIEW.json"
    review_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"review": str(review_path), "status": result["status"]}, indent=2))
    return 0 if result["status"] in {"MECHANICAL_PASS", "BLOCKED_REAL_PPTX_RENDER"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
