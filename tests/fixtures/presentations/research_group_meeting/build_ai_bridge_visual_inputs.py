#!/usr/bin/env python3
"""Build the Bridge Kit visual input manifest for the research presentation smoke.

This adapter is repository-specific. It reuses the committed four-page
research-group-meeting regression renders and writes only the Bridge Kit input
manifest. It does not call OpenAI and it does not make an academic visual PASS.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[4]
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "presentations" / "research_group_meeting"
PACKET_SOURCE = FIXTURE_ROOT / "visual_review_packet_source"
DEFAULT_TASK_KEY = "012_presentation_visual_adapter"
BRIDGE_KIT_COMMIT = "e915d04756490fafbd111eaa445295f0103b2c94"
LEGACY_TASK_KEY = "011_round_handoff"
LEGACY_EXTERNAL_VISUAL_IMPLEMENTATION_COMMIT = "ff8ff1ddb48cb9c511b3e3fecc7f0c4964adab46"
LEGACY_PAGES_TRANSPORT_COMMIT = "38d7bbc137fb8bbaa13d830bbfb1907be32066c6"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def repo_rel(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def display_path(path: Path) -> str:
    try:
        return repo_rel(path)
    except ValueError:
        return str(path)


def require_file(path: Path) -> Path:
    if not path.is_file():
        raise SystemExit(f"missing required visual input source: {path}")
    return path


def verify_source_chain(source_dir: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    evidence = load_json(require_file(source_dir / "EVIDENCE_MANIFEST.json"))
    render = load_json(require_file(source_dir / "RENDER_STATUS.json"))
    mechanical = load_json(require_file(source_dir / "MECHANICAL_VISUAL_REVIEW.json"))
    require_file(source_dir / "research_group_meeting_regression.pptx")
    require_file(source_dir / "pdf" / "research_group_meeting_regression.pdf")
    if evidence.get("status") != "GENERATED_SOURCE_ARTIFACTS_ONLY" or evidence.get("generator_may_pass") is not False:
        raise SystemExit("evidence manifest must be generated-source-only and must not claim PASS")
    if evidence.get("editable_slide_count") != 4 or len(evidence.get("slides", [])) != 4:
        raise SystemExit("evidence manifest must describe exactly four editable slides")
    if render.get("status") != "ok" or render.get("png_count") != 4 or render.get("returncode") != 0:
        raise SystemExit("render status must prove a successful real PPTX render to four PNGs")
    if mechanical.get("status") != "MECHANICAL_PASS":
        raise SystemExit("mechanical visual review must pass before OpenAI visual smoke")
    if mechanical.get("academic_visual_decision") != "NOT_ASSESSED":
        raise SystemExit("mechanical visual review must not claim academic visual PASS")
    if mechanical.get("rendered_png_count") != 4 or len(mechanical.get("slide_reviews", [])) != 4:
        raise SystemExit("mechanical visual review must cover four rendered slides")
    by_slide = {item.get("slide"): item for item in mechanical.get("slide_reviews", [])}
    for slide in evidence["slides"]:
        slide_number = slide["slide"]
        review = by_slide.get(slide_number)
        if not review:
            raise SystemExit(f"missing mechanical review for slide {slide_number}")
        if slide.get("archetype") != review.get("archetype"):
            raise SystemExit(f"archetype mismatch for slide {slide_number}")
        if slide.get("reference_ids") != review.get("reference_ids"):
            raise SystemExit(f"reference id mismatch for slide {slide_number}")
        if slide.get("expected_scientific_objects") != review.get("expected_object_contract"):
            raise SystemExit(f"expected scientific object mismatch for slide {slide_number}")
        rendered = require_file(source_dir / "rendered" / f"slide-{slide_number}.png")
        expected = require_file(source_dir / "expected_render" / f"slide-{slide_number}.png")
        if sha256(rendered) != sha256(expected):
            raise SystemExit(f"rendered slide-{slide_number}.png does not match committed expected render")
    return evidence, render, mechanical


def rubric_instructions(evidence: dict[str, Any]) -> str:
    slide_lines = []
    for slide in evidence["slides"]:
        slide_lines.append(
            "- slide_{slide}: title={title}; declared_archetype={archetype}; "
            "expected_scientific_objects={objects}; reference_ids={refs}; retrieval_intent={intent}".format(
                slide=slide["slide"],
                title=slide["title"],
                archetype=slide["archetype"],
                objects=", ".join(slide["expected_scientific_objects"]),
                refs=", ".join(slide["reference_ids"]),
                intent=slide["reference_retrieval"]["query"]["intent"],
            )
        )
    return "\n".join(
        [
            "You are reviewing four real rendered PNG pages from an editable PPTX research group meeting regression.",
            "Inspect the actual image pixels page by page. Do not infer PASS from SHA, file existence, page count, mechanical PASS, metadata, expected object text, or reference IDs.",
            "For each page, identify the primary scientific object visible in the image.",
            "For each page, judge whether the declared page archetype is visually satisfied.",
            "Check whether the main figure, medical case, experiment design, statistical model, formula, label, axis, legend, or core research object is immediately visible.",
            "Reject pages that degrade into rounded cards, tables, dashboards, generic consulting layouts, slogans, or decorative shapes replacing evidence.",
            "Check for meaningless blank space, obvious visual imbalance, clipping, unreadable labels, unreadable formulas, unreadable legends, or insufficient projection readability.",
            "Check that the evidence boundary is visually clear: synthetic, preliminary, validation-subset, generated, or missing evidence must not look like completed proof.",
            "Judge whether each page contains enough research information to support about 30-90 seconds of group-meeting discussion.",
            "Return PASS only when every page satisfies its research visual job. Return REVISE if any page needs a concrete visual fix. Return BLOCKED only if the supplied pixels cannot be assessed.",
            "For REVISE, give the smallest concrete page-specific repair recommendation.",
            "",
            "Declared page contracts:",
            *slide_lines,
        ]
    )


def build_manifest(source_dir: Path, task_key: str) -> dict[str, Any]:
    evidence, render, mechanical = verify_source_chain(source_dir)
    inputs = []
    image_shas: dict[str, str] = {}
    for slide in evidence["slides"]:
        logical_id = f"slide_{slide['slide']}"
        image_path = require_file(source_dir / "rendered" / f"slide-{slide['slide']}.png")
        image_sha = sha256(image_path)
        image_shas[logical_id] = image_sha
        inputs.append(
            {
                "description": (
                    f"Slide {slide['slide']}: {slide['title']} | archetype={slide['archetype']} | "
                    f"expected_objects={', '.join(slide['expected_scientific_objects'])}"
                ),
                "logical_id": logical_id,
                "mime_type": "image/png",
                "path": repo_rel(image_path),
                "sha256": image_sha,
            }
        )
    return {
        "external_upload_authorization": "",
        "identity_bindings": {
            "adapter_identity": task_key,
            "bridge_kit_commit": BRIDGE_KIT_COMMIT,
            "evidence_manifest_sha256": sha256(source_dir / "EVIDENCE_MANIFEST.json"),
            "legacy_external_visual_implementation_commit": LEGACY_EXTERNAL_VISUAL_IMPLEMENTATION_COMMIT,
            "legacy_pages_transport_commit": LEGACY_PAGES_TRANSPORT_COMMIT,
            "legacy_task_key": LEGACY_TASK_KEY,
            "mechanical_review_sha256": sha256(source_dir / "MECHANICAL_VISUAL_REVIEW.json"),
            "pdf_sha256": sha256(source_dir / "pdf" / "research_group_meeting_regression.pdf"),
            "pptx_sha256": sha256(source_dir / "research_group_meeting_regression.pptx"),
            "render_status_sha256": sha256(source_dir / "RENDER_STATUS.json"),
            "source_dir": repo_rel(source_dir),
            "source_mechanical_status": mechanical["status"],
            "source_academic_visual_decision": mechanical["academic_visual_decision"],
            "source_render_status": render["status"],
            "input_png_sha256_by_slide": image_shas,
        },
        "inputs": inputs,
        "privacy_policy": "PUBLIC_SAFE_ONLY",
        "prompt_version": "ai-bridge.visual-review.v1",
        "review_kind": "research-presentation-four-page-smoke",
        "rubric": {
            "instructions": rubric_instructions(evidence),
            "source_contracts": [
                "skills/tools/documents-media/presentations/research-presentations/SKILL.md",
                "skills/tools/documents-media/presentations/shared/visual-qa.md",
                "skills/tools/documents-media/presentations/shared/references/RESEARCH_SLIDE_ARCHETYPES.md",
            ],
        },
        "schema": "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1",
        "task_key": task_key,
        "workflow_type": "generic",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, default=PACKET_SOURCE)
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "results" / DEFAULT_TASK_KEY / "visual_review" / "visual_inputs.json",
    )
    parser.add_argument("--task-key", default=DEFAULT_TASK_KEY)
    parser.add_argument("--copy-latest", action="store_true", help="Also copy the manifest to visual_inputs.latest.json")
    args = parser.parse_args()
    source_dir = args.source_dir.resolve()
    output = args.output if args.output.is_absolute() else (REPO_ROOT / args.output)
    manifest = build_manifest(source_dir, args.task_key)
    write_json(output, manifest)
    if args.copy_latest:
        latest = output.with_name("visual_inputs.latest.json")
        shutil.copy2(output, latest)
    print(json.dumps({"output": display_path(output), "input_count": len(manifest["inputs"]), "task_key": args.task_key}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
