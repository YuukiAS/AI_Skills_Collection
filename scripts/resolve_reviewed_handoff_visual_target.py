#!/usr/bin/env python3
"""Resolve a pending task-local Reviewed Handoff visual-review target."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ELIGIBLE_STATES = {"READY_FOR_GPT_REVIEW"}
TASKS_DIR = Path("automation/reviewed_handoff/tasks")


class ResolutionError(Exception):
    """Raised when task-local visual target resolution must fail closed."""


@dataclass(frozen=True)
class VisualTarget:
    task_key: str
    manifest_path: str
    evidence_path: str
    implementation_commit: str


def _load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ResolutionError(f"{_display(path)} is not valid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ResolutionError(f"{_display(path)} must contain a JSON object")
    return data


def _display(path: Path) -> str:
    return path.as_posix()


def _repo_relative(value: Any, *, field: str, current_path: Path) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise ResolutionError(f"{_display(current_path)} missing non-empty {field}")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise ResolutionError(f"{_display(current_path)} {field} must be repository-relative without '..': {value}")
    return path


def _require_evidence_path(task_key: str, evidence_path: Path, *, current_path: Path) -> None:
    allowed_root = Path("results") / task_key / "visual_review"
    if evidence_path.suffix != ".json":
        raise ResolutionError(f"{_display(current_path)} visual_review_evidence_path must be a JSON file")
    try:
        evidence_path.relative_to(allowed_root)
    except ValueError as exc:
        raise ResolutionError(
            f"{_display(current_path)} visual_review_evidence_path must be under "
            f"{allowed_root.as_posix()}/"
        ) from exc


def _manifest_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _fresh_evidence(evidence_abs: Path, *, manifest_sha256: str, task_key: str, implementation_commit: str) -> bool:
    if not evidence_abs.exists():
        return False
    try:
        evidence = json.loads(evidence_abs.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False
    if not isinstance(evidence, dict):
        return False

    input_manifest = evidence.get("input_manifest")
    if not isinstance(input_manifest, dict):
        return False
    if input_manifest.get("manifest_sha256") != manifest_sha256:
        return False

    bindings = input_manifest.get("identity_bindings")
    if not isinstance(bindings, dict):
        return False
    return bindings.get("task_key") == task_key and bindings.get("implementation_commit") == implementation_commit


def _validate_manifest(
    *,
    root: Path,
    current_path: Path,
    task_key: str,
    implementation_commit: str,
    manifest_path: Path,
) -> dict[str, Any]:
    manifest_abs = root / manifest_path
    if not manifest_abs.is_file():
        raise ResolutionError(f"{_display(current_path)} manifest does not exist: {manifest_path.as_posix()}")
    manifest = _load_json(manifest_abs)
    if manifest.get("task_key") != task_key:
        raise ResolutionError(
            f"{manifest_path.as_posix()} task_key does not match CURRENT task_key {task_key!r}"
        )
    if manifest.get("workflow_type") != "reviewed_handoff":
        raise ResolutionError(f"{manifest_path.as_posix()} workflow_type must be reviewed_handoff")
    bindings = manifest.get("identity_bindings")
    if not isinstance(bindings, dict):
        raise ResolutionError(f"{manifest_path.as_posix()} missing identity_bindings object")
    if bindings.get("task_key") != task_key:
        raise ResolutionError(
            f"{manifest_path.as_posix()} identity_bindings.task_key does not match CURRENT task_key {task_key!r}"
        )
    if bindings.get("implementation_commit") != implementation_commit:
        raise ResolutionError(
            f"{manifest_path.as_posix()} identity_bindings.implementation_commit does not match CURRENT "
            f"implementation_commit {implementation_commit!r}"
        )
    return manifest


def resolve_visual_target(root: Path) -> VisualTarget | None:
    root = root.resolve()
    tasks_root = root / TASKS_DIR
    if not tasks_root.exists():
        return None

    eligible: list[VisualTarget] = []
    for current_path in sorted(tasks_root.glob("*/CURRENT.json")):
        current = _load_json(current_path)
        if current.get("visual_review_required") is not True:
            continue
        state = current.get("state")
        if state not in ELIGIBLE_STATES:
            continue

        task_key = current.get("task_key")
        if not isinstance(task_key, str) or not task_key:
            raise ResolutionError(f"{_display(current_path)} missing task_key")
        if task_key != current_path.parent.name:
            raise ResolutionError(f"{_display(current_path)} task_key does not match directory name")

        implementation_commit = current.get("implementation_commit")
        if not isinstance(implementation_commit, str) or not implementation_commit:
            raise ResolutionError(f"{_display(current_path)} missing implementation_commit for visual review")

        manifest_path = _repo_relative(
            current.get("visual_review_manifest_path"),
            field="visual_review_manifest_path",
            current_path=current_path,
        )
        evidence_path = _repo_relative(
            current.get("visual_review_evidence_path"),
            field="visual_review_evidence_path",
            current_path=current_path,
        )
        _require_evidence_path(task_key, evidence_path, current_path=current_path)

        _validate_manifest(
            root=root,
            current_path=current_path,
            task_key=task_key,
            implementation_commit=implementation_commit,
            manifest_path=manifest_path,
        )
        manifest_hash = _manifest_sha256(root / manifest_path)
        if _fresh_evidence(
            root / evidence_path,
            manifest_sha256=manifest_hash,
            task_key=task_key,
            implementation_commit=implementation_commit,
        ):
            continue

        eligible.append(
            VisualTarget(
                task_key=task_key,
                manifest_path=manifest_path.as_posix(),
                evidence_path=evidence_path.as_posix(),
                implementation_commit=implementation_commit,
            )
        )

    if len(eligible) > 1:
        task_keys = ", ".join(target.task_key for target in eligible)
        raise ResolutionError(f"multiple pending task-local visual reviews: {task_keys}")
    return eligible[0] if eligible else None


def _result_payload(target: VisualTarget | None) -> dict[str, Any]:
    if target is None:
        return {
            "status": "none",
            "eligible_count": 0,
            "message": "no task-local Reviewed Handoff visual review pending",
        }
    return {
        "status": "selected",
        "eligible_count": 1,
        "task_key": target.task_key,
        "manifest": target.manifest_path,
        "output": target.evidence_path,
        "implementation_commit": target.implementation_commit,
    }


def write_github_env(path: Path, target: VisualTarget | None) -> None:
    lines: list[str]
    if target is None:
        lines = ["AI_BRIDGE_VISUAL_REVIEW_SKIP=1"]
    else:
        lines = [
            "AI_BRIDGE_VISUAL_REVIEW_SKIP=0",
            f"AI_BRIDGE_VISUAL_REVIEW_TASK_KEY={target.task_key}",
            f"AI_BRIDGE_VISUAL_REVIEW_MANIFEST={target.manifest_path}",
            f"AI_BRIDGE_VISUAL_REVIEW_OUTPUT={target.evidence_path}",
        ]
    with path.open("a", encoding="utf-8") as handle:
        for line in lines:
            handle.write(f"{line}\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, default=Path("."), help="repository checkout root")
    parser.add_argument("--github-env", type=Path, help="append resolved GitHub Actions env vars to this file")
    args = parser.parse_args(argv)

    try:
        target = resolve_visual_target(args.target)
    except ResolutionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    payload = _result_payload(target)
    print(json.dumps(payload, indent=2, sort_keys=True))
    if args.github_env:
        write_github_env(args.github_env, target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
