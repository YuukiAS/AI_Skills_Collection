#!/usr/bin/env python3
"""Prepare hash-bound private G5 review metadata and bundle files."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[6]
TASK_KEY = "presentations--stage1-front-door-two-template-foundation"
EXPECTED_CHAPTER1_SHA256 = "ed205507a6d2de320b77d47d41e55bb0b406aef48144bc2c55d3bbba8c77ddf7"
DEFAULT_OUT = REPO_ROOT / "results" / TASK_KEY / "g5_private_review" / "G5_REVIEW_INPUTS.json"
DEFAULT_BUNDLE = REPO_ROOT / "private" / "exports" / TASK_KEY / "g5-review-bundle"


def rel(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def file_sha(path: Path) -> str:
    import hashlib

    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_artifact(value: str) -> tuple[str, Path]:
    if ":" not in value:
        raise ValueError("--artifact must use role:path")
    role, raw_path = value.split(":", 1)
    if not role:
        raise ValueError("--artifact role cannot be empty")
    return role, Path(raw_path)


def copy_artifacts(artifacts: list[tuple[str, Path]], bundle_dir: Path) -> list[dict[str, Any]]:
    bundle_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    for role, path in artifacts:
        source = path if path.is_absolute() else REPO_ROOT / path
        if not source.is_file():
            raise FileNotFoundError(f"missing artifact for {role}: {source}")
        target = bundle_dir / f"{role}{source.suffix}"
        shutil.copy2(source, target)
        records.append(
            {
                "role": role,
                "source_path": rel(source),
                "bundle_path": rel(target),
                "sha256": file_sha(target),
            }
        )
    return records


def build_manifest(
    *,
    implementation_commit: str,
    chapter1_locator: str | None,
    course_standard_source_identity: dict[str, Any] | None,
    cuhk_source_identity: dict[str, Any] | None,
    render_identities: dict[str, Any],
    render_owner_route: dict[str, Any],
    artifact_records: list[dict[str, Any]],
) -> dict[str, Any]:
    waiting_for_course = course_standard_source_identity is None
    return {
        "schema": "PRESENTATIONS_G5_REVIEW_INPUTS_V1",
        "task_key": TASK_KEY,
        "implementation_commit": implementation_commit,
        "chapter1_expected_sha256": EXPECTED_CHAPTER1_SHA256,
        "chapter1_locator": chapter1_locator,
        "chapter1_private_pixels_committed": False,
        "course_standard_source_identity": course_standard_source_identity,
        "course_standard_dependency_status": (
            "WAITING_FOR_CANONICAL_COURSE_STANDARD_TEMPLATE" if waiting_for_course else "READY"
        ),
        "cuhk_source_identity": cuhk_source_identity,
        "candidate_artifacts": artifact_records,
        "render_identities": render_identities,
        "render_owner": {
            "environment_owner": "render-chinese-math-pdf",
            "route": render_owner_route,
        },
        "review_surface": "PRESENTATIONS_LONG_TERM_PLANNER_CHAT_PRIVATE_G5_EVIDENCE",
        "direct_private_pixel_access_required": True,
        "private_pixels_committed": False,
        "final_g5_ready": not waiting_for_course and bool(artifact_records),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--implementation-commit", required=True)
    parser.add_argument("--out-json", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--bundle-dir", type=Path, default=DEFAULT_BUNDLE)
    parser.add_argument("--chapter1-locator")
    parser.add_argument("--course-standard-source-identity-json")
    parser.add_argument("--cuhk-source-identity-json")
    parser.add_argument("--render-identities-json", default="{}")
    parser.add_argument("--render-owner-route-json", default="{}")
    parser.add_argument("--artifact", action="append", default=[], help="Candidate artifact as role:path")
    args = parser.parse_args()

    course_identity = json.loads(args.course_standard_source_identity_json) if args.course_standard_source_identity_json else None
    cuhk_identity = json.loads(args.cuhk_source_identity_json) if args.cuhk_source_identity_json else None
    render_identities = json.loads(args.render_identities_json)
    render_owner_route = json.loads(args.render_owner_route_json)
    artifact_records = copy_artifacts([parse_artifact(item) for item in args.artifact], args.bundle_dir)
    manifest = build_manifest(
        implementation_commit=args.implementation_commit,
        chapter1_locator=args.chapter1_locator,
        course_standard_source_identity=course_identity,
        cuhk_source_identity=cuhk_identity,
        render_identities=render_identities,
        render_owner_route=render_owner_route,
        artifact_records=artifact_records,
    )
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    bundle_manifest = args.bundle_dir / "G5_REVIEW_INPUTS.json"
    if args.bundle_dir.exists():
        bundle_manifest.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"status": "ok", "out_json": rel(args.out_json), "final_g5_ready": manifest["final_g5_ready"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
