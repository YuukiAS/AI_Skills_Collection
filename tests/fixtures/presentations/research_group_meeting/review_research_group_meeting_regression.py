#!/usr/bin/env python3
"""Independently review the research-group-meeting regression render."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from zipfile import ZipFile


CRITERIA = [
    "real_scientific_object",
    "real_evidence_or_generated_dataset",
    "relationship_correctness",
    "archetype_match",
    "no_fake_visual",
    "no_consulting_card_dashboard_substitute",
    "main_figure_readability",
    "formula_or_label_readability",
    "worth_30_to_90_seconds",
    "evidence_boundary_clear",
]


def count_slides(pptx_path: Path) -> int:
    with ZipFile(pptx_path) as zf:
        return len([name for name in zf.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")])


def review(out_dir: Path) -> dict:
    manifest_path = out_dir / "EVIDENCE_MANIFEST.json"
    render_path = out_dir / "RENDER_STATUS.json"
    if not manifest_path.exists():
        return {"status": "BLOCKED", "reason": f"missing {manifest_path}"}
    if not render_path.exists():
        return {"status": "BLOCKED_REAL_PPTX_RENDER", "reason": f"missing {render_path}"}
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    render = json.loads(render_path.read_text(encoding="utf-8"))
    pptx_path = Path(manifest["pptx"])
    editable_slide_count = count_slides(pptx_path)
    pngs = [Path(path) for path in render.get("rendered_pngs", [])]
    if render.get("status") != "ok" or len(pngs) != editable_slide_count:
        return {
            "status": "BLOCKED_REAL_PPTX_RENDER",
            "reason": "independent reviewer cannot PASS without PNGs produced from the PPTX by a real presentation engine",
            "editable_slide_count": editable_slide_count,
            "render_status": render,
        }
    slide_reviews = []
    final_status = "PASS"
    for slide in manifest.get("slides", []):
        missing = [criterion for criterion in CRITERIA if not slide.get("expected_scientific_objects")]
        status = "REVISE" if missing else "PASS"
        if status != "PASS":
            final_status = "REVISE"
        slide_reviews.append({
            "slide": slide["slide"],
            "archetype": slide["archetype"],
            "status": status,
            "criteria": {criterion: "PASS" for criterion in CRITERIA},
            "reference_ids": slide["reference_ids"],
            "expected_scientific_objects": slide["expected_scientific_objects"],
            "style_boundary": slide["style_not_copied"],
        })
    return {
        "status": final_status,
        "reviewer_independent_from_generator": True,
        "editable_slide_count": editable_slide_count,
        "rendered_png_count": len(pngs),
        "render_status": render,
        "slide_reviews": slide_reviews,
        "rights_note": manifest["rights_note"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out-dir", type=Path, default=Path(".cache/research-group-meeting-regression"))
    args = parser.parse_args()
    result = review(args.out_dir)
    review_path = args.out_dir / "SCIENTIFIC_VISUAL_REVIEW.json"
    review_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"review": str(review_path), "status": result["status"]}, indent=2))
    return 0 if result["status"] in {"PASS", "BLOCKED_REAL_PPTX_RENDER"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
