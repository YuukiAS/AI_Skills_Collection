#!/usr/bin/env python3
"""Validate 023 deck-design-system integration artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any
from zipfile import ZipFile


REPO_ROOT = Path(__file__).resolve().parents[6]
TASK_KEY = "023_research_presentation_deck_design_system_integration"

FORBIDDEN_AUDIENCE_TERMS = [
    "RRL-",
    "SRC-",
    "candidate",
    "Reference retrieval",
    "EVIDENCE_MANIFEST",
    "Diagram contract",
    "QA",
    "repo path",
    "run ID",
    "implementation commit",
    "review target",
    "reference_faithful",
    "alternative_composition",
    "controlled_wildcard",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def resolve(path: str) -> Path:
    return REPO_ROOT / path


def pptx_text(path: Path) -> str:
    with ZipFile(path) as zf:
        return "\n".join(
            zf.read(name).decode("utf-8", errors="ignore")
            for name in sorted(zf.namelist())
            if name.startswith("ppt/slides/slide") and name.endswith(".xml")
        )


def slide_count(path: Path) -> int:
    with ZipFile(path) as zf:
        return len([name for name in zf.namelist() if name.startswith("ppt/slides/slide") and name.endswith(".xml")])


def validate_profile(path: Path) -> list[str]:
    errors: list[str] = []
    profile = load_json(path)
    if profile.get("schema") != "RESEARCH_DECK_DESIGN_PROFILE_V1":
        errors.append(f"{path}: invalid design profile schema")
    if profile.get("profile_id") != "research-deck-design-profile-v1":
        errors.append(f"{path}: invalid profile_id")
    provenance = profile.get("provenance", {})
    if provenance.get("task_key") != TASK_KEY:
        errors.append(f"{path}: profile provenance task_key mismatch")
    locked = profile.get("locked_properties", {})
    for key in ["fonts", "type_scale", "color_roles", "spacing", "annotation", "chart", "image_panel", "equation", "caption"]:
        if key not in locked:
            errors.append(f"{path}: locked_properties missing {key}")
    page_local = set(profile.get("page_local_properties", []))
    for key in ["scientific_object_bbox", "layout_family", "panel_count", "annotation_target"]:
        if key not in page_local:
            errors.append(f"{path}: page_local_properties missing {key}")
    if locked.get("equation", {}).get("decorative_card_used") is not False:
        errors.append(f"{path}: equation locked profile must reject decorative cards")
    return errors


def validate_deck_manifest(path: Path) -> list[str]:
    errors: list[str] = []
    manifest = load_json(path)
    if manifest.get("schema") != "RESEARCH_DECK_DESIGN_SYSTEM_INTEGRATION_MANIFEST_V1":
        errors.append(f"{path}: invalid deck manifest schema")
        return errors
    if manifest.get("task_key") != TASK_KEY:
        errors.append(f"{path}: task_key mismatch")
    if "engineering integration fixture" not in manifest.get("fixture_boundary", ""):
        errors.append(f"{path}: missing fixture boundary")
    deck_plan = resolve(manifest.get("deck_plan", ""))
    if not deck_plan.exists():
        errors.append(f"{path}: deck plan missing")
    else:
        plan = load_json(deck_plan)
        if plan.get("schema") != "RESEARCH_DECK_DESIGN_SYSTEM_FIXTURE_PLAN_V1":
            errors.append(f"{path}: invalid deck plan schema")
        if len(plan.get("slides", [])) != len(manifest.get("slides", [])):
            errors.append(f"{path}: deck plan slide count mismatch")
    pptx = resolve(manifest.get("pptx", ""))
    if not pptx.exists():
        errors.append(f"{path}: PPTX missing")
    else:
        if slide_count(pptx) != manifest.get("editable_slide_count"):
            errors.append(f"{path}: editable slide count mismatch")
        text = pptx_text(pptx)
        for term in FORBIDDEN_AUDIENCE_TERMS:
            if term in text:
                errors.append(f"{path}: audience-facing PPTX leaks {term}")
    slides = manifest.get("slides", [])
    if len(slides) < 4:
        errors.append(f"{path}: expected at least 4 slides")
    families = {slide.get("layout_family") for slide in slides}
    major = set(manifest.get("major_composition_families", []))
    if len(major) < 3:
        errors.append(f"{path}: expected at least 3 major composition families")
    if len({slide.get("locked_properties_sha256") for slide in slides}) != 1:
        errors.append(f"{path}: deck-wide locked profile SHA is not stable")
    primary_roles = {tuple(slide.get("primary_object_roles", [])) for slide in slides}
    if len(primary_roles) < 2:
        errors.append(f"{path}: primary scientific-object roles do not vary")
    for index, slide in enumerate(slides, start=1):
        if not slide.get("source_reference_ids"):
            errors.append(f"{path}: slide {index} missing source reference")
        if not slide.get("geometry_transfer"):
            errors.append(f"{path}: slide {index} missing geometry_transfer")
        if not slide.get("primary_bboxes"):
            errors.append(f"{path}: slide {index} missing primary_bboxes")
        if slide.get("locked_profile_id") != "research-deck-design-profile-v1":
            errors.append(f"{path}: slide {index} missing locked profile id")
        audience = "\n".join(slide.get("audience_text", []))
        for term in FORBIDDEN_AUDIENCE_TERMS:
            if term in audience:
                errors.append(f"{path}: slide {index} audience text leaks {term}")
    if len(families) < 3:
        errors.append(f"{path}: slide layout families insufficiently diverse")
    render = manifest.get("render_status", {})
    if render.get("status") != "ok":
        errors.append(f"{path}: real render not ok")
    if render.get("png_count") != len(slides):
        errors.append(f"{path}: rendered PNG count mismatch")
    for item in render.get("rendered_png", []):
        png = resolve(item.get("path", ""))
        if not png.exists() or png.stat().st_size < 10_000:
            errors.append(f"{path}: rendered PNG missing or too small {png}")
    qa = manifest.get("mechanical_qa", {})
    if qa.get("status") != "MECHANICAL_PASS":
        errors.append(f"{path}: mechanical QA did not pass")
    return errors


def validate_outputs(path: Path) -> list[str]:
    errors: list[str] = []
    outputs = load_json(path)
    if outputs.get("schema") != "RESEARCH_DECK_DESIGN_SYSTEM_INTEGRATION_OUTPUTS_V1":
        return [f"{path}: invalid outputs schema"]
    if outputs.get("task_key") != TASK_KEY:
        errors.append(f"{path}: task_key mismatch")
    profile = resolve(outputs.get("deck_design_profile", ""))
    if not profile.exists():
        errors.append(f"{path}: design profile missing")
    else:
        errors.extend(validate_profile(profile))
    decks = outputs.get("decks", [])
    if len(decks) != 2:
        errors.append(f"{path}: expected exactly two mini-decks")
    review_pack = outputs.get("review_pack_pdf", {})
    review_pack_path = resolve(review_pack.get("path", ""))
    if not review_pack_path.exists() or review_pack_path.stat().st_size < 100_000:
        errors.append(f"{path}: combined review pack PDF missing or too small")
    if len(review_pack.get("source_pdfs", [])) != 2:
        errors.append(f"{path}: combined review pack must cite two source PDFs")
    mutation = outputs.get("profile_mutation_regression", {})
    mutation_path = resolve(mutation.get("path", ""))
    if not mutation_path.exists():
        errors.append(f"{path}: profile mutation regression missing")
    else:
        mutation_result = load_json(mutation_path)
        if mutation_result.get("schema") != "RESEARCH_DECK_DESIGN_PROFILE_MUTATION_REGRESSION_V1":
            errors.append(f"{path}: invalid profile mutation regression schema")
        if mutation_result.get("status") != "PASS":
            errors.append(f"{path}: profile mutation regression did not pass")
        checks = mutation_result.get("checks", {})
        for key in ["profile_sha_changed", "native_pptx_xml_changed", "page_local_geometry_stable", "render_still_ok"]:
            if checks.get(key) is not True:
                errors.append(f"{path}: profile mutation regression check failed: {key}")
        for key in ["mutated_profile", "mutated_manifest"]:
            if not resolve(mutation_result.get(key, "")).exists():
                errors.append(f"{path}: profile mutation regression missing {key}")
    deck_keys = {deck.get("manifest", "").split("/")[-2] for deck in decks}
    if deck_keys != {"statistical_design_system_fixture", "medical_design_system_fixture"}:
        errors.append(f"{path}: unexpected deck keys {sorted(deck_keys)}")
    for deck in decks:
        manifest = resolve(deck.get("manifest", ""))
        if not manifest.exists():
            errors.append(f"{path}: deck manifest missing {manifest}")
        else:
            errors.extend(validate_deck_manifest(manifest))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outputs", default=f"results/{TASK_KEY}/generated/OUTPUTS.json")
    args = parser.parse_args()
    errors = validate_outputs(resolve(args.outputs) if not Path(args.outputs).is_absolute() else Path(args.outputs))
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("validated 2 deck-design-system integration mini-deck(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
