#!/usr/bin/env python3
"""Prepare anonymous comparative visual-review inputs for task 021."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import subprocess
import urllib.request
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw


SHARED = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[6]
REFERENCE_INDEX = SHARED / "references" / "research_slide_reference_index.csv"
COMPOSITION_INDEX = SHARED / "references" / "research_slide_composition_index.json"
TASK_KEY = "021_research_presentation_comparative_reference_calibrated_visual_review"
VISIBLE_TASK_KEY = "021_visual_comparison"
RESULT_ROOT = REPO_ROOT / "results" / TASK_KEY / "visual_review"
CACHE_ROOT = REPO_ROOT / ".cache" / "research-presentation-comparative-review" / "021"
SOURCE_CACHE = REPO_ROOT / ".cache" / "research-presentation-reference-library" / "sources"

CASES = {
    "statistical": {
        "page_job_contract": "estimator/equation comparative review",
        "request_id": "statistical_estimator_cluster_robust_variance",
        "candidate_manifest": "docs/audits/research_presentation_candidate_search/generated/statistical_estimator_cluster_robust_variance/candidate_manifest.json",
        "reference_ids": ["RRL-028", "RRL-014"],
        "rubric_focus": "For this estimator/equation page job, judge whether the equation is a mature scientific object with clear composition, direct annotation, projection-scale typography, and non-generic academic language.",
    },
    "medical": {
        "page_job_contract": "medical-image comparison comparative review",
        "request_id": "medical_image_lesion_overlay_comparison",
        "candidate_manifest": "docs/audits/research_presentation_candidate_search/generated/medical_image_lesion_overlay_comparison/candidate_manifest.json",
        "reference_ids": ["RRL-022", "RRL-013"],
        "rubric_focus": "For this medical-image comparison page job, judge whether image pixels are the visual center, whether panel correspondence and legend are natural, and whether annotation supports rather than overwhelms the images.",
    },
}

FORBIDDEN_VISIBLE_TERMS = [
    "RRL-",
    "SRC-",
    "candidate",
    "reference",
    "generated",
    "gold",
    "baseline",
    "reference_faithful",
    "alternative_composition",
    "controlled_wildcard",
    "MIT",
    "CMU",
    "SFU",
    "Columbia",
    "Harvard",
    "Gelman",
    "Kumar",
    "Abhishek",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_reference_rows() -> dict[str, dict[str, str]]:
    with REFERENCE_INDEX.open(newline="", encoding="utf-8") as fh:
        return {row["reference_id"]: row for row in csv.DictReader(fh)}


def load_composition_records() -> dict[str, dict[str, Any]]:
    records = json.loads(COMPOSITION_INDEX.read_text(encoding="utf-8"))["records"]
    return {record["reference_id"]: record for record in records}


def ensure_source_pdf(row: dict[str, str]) -> Path:
    SOURCE_CACHE.mkdir(parents=True, exist_ok=True)
    target = SOURCE_CACHE / row["local_cache_file"]
    if not target.exists():
        with urllib.request.urlopen(row["source_url"], timeout=120) as response:
            target.write_bytes(response.read())
    digest = sha256(target)
    if digest != row["source_file_sha256"]:
        raise RuntimeError(f"{row['reference_id']}: source PDF SHA mismatch: {digest} != {row['source_file_sha256']}")
    return target


def render_reference(row: dict[str, str], output_dir: Path) -> Path:
    source_pdf = ensure_source_pdf(row)
    output_dir.mkdir(parents=True, exist_ok=True)
    prefix = output_dir / row["reference_id"].lower()
    page = str(row["actual_page_number"])
    subprocess.run(["pdftoppm", "-f", page, "-l", page, "-r", "140", "-png", str(source_pdf), str(prefix)], check=True)
    rendered = output_dir / f"{prefix.name}-{page}.png"
    digest = sha256(rendered)
    if digest != row["rendered_page_sha256"]:
        raise RuntimeError(f"{row['reference_id']}: canonical rendered page SHA mismatch: {digest} != {row['rendered_page_sha256']}")
    return anonymize_reference_render(rendered)


def anonymize_reference_render(rendered: Path) -> Path:
    image = Image.open(rendered).convert("RGB")
    draw = ImageDraw.Draw(image)
    width, height = image.size
    draw.rectangle((0, int(height * 0.92), int(width * 0.08), height), fill=(255, 255, 255))
    draw.rectangle((int(width * 0.84), int(height * 0.84), width, height), fill=(255, 255, 255))
    draw.rectangle((int(width * 0.82), 0, width, int(height * 0.10)), fill=(255, 255, 255))
    anonymized = rendered.with_name(f"{rendered.stem}-anonymous.png")
    image.save(anonymized)
    return anonymized


def anonymous_order(case_key: str, entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    def key(entry: dict[str, Any]) -> str:
        seed = f"{case_key}:{entry['stable_identity']}:{entry['sha256']}"
        return hashlib.sha256(seed.encode("utf-8")).hexdigest()

    return sorted(entries, key=key)


def comparative_rubric(case_key: str, page_job_contract: str, focus: str) -> str:
    return (
        f"You are reviewing anonymous visual items for one shared page job: {page_job_contract}.\n"
        "Inspect the actual pixels for every anonymous item before judging. Do not infer quality from file names, order, metadata, or SHA values.\n"
        "You are intentionally not told which items are produced by a generator and which come from mature public research slides. Do not guess provenance; judge only visible quality.\n"
        "First review each item independently. For each anonymous item, identify the primary scientific object and assess composition maturity, balance, whitespace, typography hierarchy, scientific-object prominence, equation/figure/image treatment, annotation/caption/legend integration, visual specificity versus generic template, natural academic language, AI-template or fixture fingerprints, and projection readability.\n"
        f"{focus}\n"
        "Then give relative tiers or ordering across the anonymous items. Explicitly explain the visual gaps between stronger and weaker items.\n"
        "Mark which anonymous items appear to reach mature research-group-meeting or strong conference-talk level, and which are merely technically readable.\n"
        "Do not treat the best item in this set as automatically good enough. It is valid to conclude that no anonymous item reaches the mature talk-quality bar.\n"
        "Return PASS if the comparative evidence is assessable and sufficiently detailed for downstream Planner use. Return REVISE only if the input package or rubric prevents a valid comparative judgment. Return BLOCKED only if the pixels cannot be assessed.\n"
        f"Case key for engineering trace only: {case_key}."
    )


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def prepare_case(case_key: str) -> dict[str, str]:
    spec = CASES[case_key]
    out_dir = RESULT_ROOT / case_key
    runtime_dir = CACHE_ROOT / case_key
    if runtime_dir.exists():
        shutil.rmtree(runtime_dir)
    runtime_dir.mkdir(parents=True, exist_ok=True)
    candidate_manifest = json.loads((REPO_ROOT / spec["candidate_manifest"]).read_text(encoding="utf-8"))
    references = load_reference_rows()
    compositions = load_composition_records()
    entries: list[dict[str, Any]] = []

    for candidate in candidate_manifest["candidates"]:
        preview = REPO_ROOT / candidate["preview_artifact"]["path"]
        entries.append({
            "stable_identity": candidate["candidate_id"],
            "item_class": "candidate",
            "candidate_id": candidate["candidate_id"],
            "candidate_strategy": candidate["strategy"],
            "source_reference_ids": candidate["source_reference_ids"],
            "source_composition_families": candidate["source_composition_families"],
            "source_path": str(preview.relative_to(REPO_ROOT)),
            "sha256": sha256(preview),
            "source_file_sha256": None,
            "canonical_rendered_page_sha256": None,
            "actual_page_number": None,
            "materialization_method": "copied committed 020 candidate preview to anonymous runtime filename",
            "rights_note": "owned deterministic candidate preview",
            "runtime_source": preview,
        })

    reference_render_dir = runtime_dir / "_materialized_reference_pages"
    for reference_id in spec["reference_ids"]:
        if reference_id not in references:
            raise RuntimeError(f"{case_key}: missing reference row {reference_id}")
        if reference_id not in compositions:
            raise RuntimeError(f"{case_key}: missing composition record {reference_id}")
        row = references[reference_id]
        rendered = render_reference(row, reference_render_dir)
        entries.append({
            "stable_identity": reference_id,
            "item_class": "reference",
            "reference_id": reference_id,
            "source_id": row["source_id"],
            "actual_page_number": int(row["actual_page_number"]),
            "source_file_sha256": row["source_file_sha256"],
            "canonical_rendered_page_sha256": row["rendered_page_sha256"],
            "source_url": row["source_url"],
            "local_cache_file": row["local_cache_file"],
            "page_function": row["page_function"],
            "scientific_object": row["scientific_object"],
            "sha256": sha256(rendered),
            "materialization_method": "download/verify public PDF, render inspected page with pdftoppm -r 140, and mask corner provenance marks before Terra input",
            "rights_note": row["rights_note"],
            "runtime_source": rendered,
        })

    ordered = anonymous_order(case_key, entries)
    inputs = []
    identity_items = []
    item_sha = {}
    for index, entry in enumerate(ordered):
        anonymous_id = f"item_{chr(ord('A') + index)}"
        anonymous_path = runtime_dir / f"{anonymous_id}.png"
        shutil.copyfile(entry["runtime_source"], anonymous_path)
        digest = sha256(anonymous_path)
        item_sha[anonymous_id] = digest
        inputs.append({
            "logical_id": anonymous_id,
            "mime_type": "image/png",
            "path": str(anonymous_path.relative_to(REPO_ROOT)),
            "sha256": digest,
            "description": f"Anonymous {anonymous_id} for {spec['page_job_contract']}. Judge only visible pixels and shared page-job fit.",
        })
        decoded = {key: value for key, value in entry.items() if key != "runtime_source"}
        decoded["anonymous_id"] = anonymous_id
        decoded["review_input_path"] = str(anonymous_path.relative_to(REPO_ROOT))
        decoded["review_input_sha256"] = digest
        identity_items.append(decoded)

    rubric = comparative_rubric(case_key, spec["page_job_contract"], spec["rubric_focus"])
    visible_manifest = {
        "schema": "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1",
        "task_key": VISIBLE_TASK_KEY,
        "workflow_type": "comparative-calibrated",
        "review_kind": f"comparative-calibrated-{case_key}",
        "prompt_version": "ai-bridge.visual-review.v1",
        "privacy_policy": "PUBLIC_SAFE_ONLY",
        "external_upload_authorization": "",
        "identity_bindings": {
            "adapter_identity": f"{VISIBLE_TASK_KEY}:{case_key}",
            "case_key": case_key,
            "page_job_contract": spec["page_job_contract"],
            "item_sha256_by_anonymous_id": item_sha,
        },
        "inputs": inputs,
        "rubric": {
            "instructions": rubric,
            "source_contracts": [],
        },
    }
    visible_text = json.dumps(visible_manifest, sort_keys=True)
    for forbidden in FORBIDDEN_VISIBLE_TERMS:
        if forbidden in visible_text:
            raise RuntimeError(f"{case_key}: Terra-visible manifest leaks forbidden term {forbidden}")
    manifest_sha = hashlib.sha256(visible_text.encode("utf-8")).hexdigest()
    visible_manifest["identity_bindings"]["immutable_review_identity_sha256"] = manifest_sha

    identity_map = {
        "schema": "RESEARCH_PRESENTATION_COMPARATIVE_REVIEW_IDENTITY_MAP_V1",
        "task_key": TASK_KEY,
        "case_key": case_key,
        "page_job_contract": spec["page_job_contract"],
        "review_identity_sha256": manifest_sha,
        "candidate_manifest": spec["candidate_manifest"],
        "reference_ids": spec["reference_ids"],
        "items": identity_items,
    }
    identity_meta = {
        "schema": "RESEARCH_PRESENTATION_COMPARATIVE_REVIEW_IDENTITY_V1",
        "task_key": TASK_KEY,
        "case_key": case_key,
        "review_identity_sha256": manifest_sha,
        "visual_inputs_sha256": hashlib.sha256(json.dumps(visible_manifest, sort_keys=True).encode("utf-8")).hexdigest(),
        "review_input_sha256_by_anonymous_id": item_sha,
        "rubric_sha256": hashlib.sha256(rubric.encode("utf-8")).hexdigest(),
        "anonymous_item_count": len(inputs),
        "candidate_count": 3,
        "reference_count": len(spec["reference_ids"]),
    }
    write_json(out_dir / "visual_inputs.json", visible_manifest)
    write_json(out_dir / "review_identity_map.json", identity_map)
    write_json(out_dir / "review_identity.json", identity_meta)
    return {
        "case_key": case_key,
        "manifest": str((out_dir / "visual_inputs.json").relative_to(REPO_ROOT)),
        "identity_map": str((out_dir / "review_identity_map.json").relative_to(REPO_ROOT)),
        "identity": str((out_dir / "review_identity.json").relative_to(REPO_ROOT)),
        "runtime_dir": str(runtime_dir.relative_to(REPO_ROOT)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=sorted(CASES), action="append")
    args = parser.parse_args()
    cases = args.case or sorted(CASES)
    outputs = [prepare_case(case_key) for case_key in cases]
    print(json.dumps({"prepared": outputs}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
