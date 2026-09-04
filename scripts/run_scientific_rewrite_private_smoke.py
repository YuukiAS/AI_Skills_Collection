#!/usr/bin/env python3
"""Validate one private 050 host-Codex style-smoke package.

The host Codex session writes the private stage artifacts and final candidate
outside tracked Git. This script verifies that package through the generated
writing-style helper and writes only privacy-safe metadata to the repository.
It does not generate prose, encrypt output, read API keys, or call OpenAI.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_HELPER = (
    REPO_ROOT
    / "plugins/codex/plugins/writing-style/skills/scientific-rewrite/scripts/rewrite_support.py"
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_runtime() -> Any:
    spec = importlib.util.spec_from_file_location("scientific_rewrite_support", RUNTIME_HELPER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load runtime helper: {RUNTIME_HELPER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def repo_path(raw: str) -> Path:
    path = Path(raw)
    if path.is_absolute():
        raise ValueError(f"Repository path must be relative: {raw}")
    return REPO_ROOT / path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, help="Repository-relative 050 smoke manifest/evidence input.")
    parser.add_argument("--plaintext", required=True, help="Private plaintext source segment path.")
    parser.add_argument("--stage-dir", required=True, help="Private host-authored stage directory.")
    parser.add_argument("--candidate", required=True, help="Private final candidate path.")
    parser.add_argument("--result", required=True, help="Repository-relative privacy-safe result JSON.")
    parser.add_argument("--receipt", required=True, help="Repository-relative privacy-safe stage receipt JSON.")
    args = parser.parse_args()

    manifest_path = repo_path(args.manifest)
    result_path = repo_path(args.result)
    receipt_path = repo_path(args.receipt)
    plaintext_path = Path(args.plaintext)
    stage_dir = Path(args.stage_dir)
    candidate_path = Path(args.candidate)

    manifest = load_json(manifest_path)
    if manifest.get("schema") != "AI_SKILLS_050_STYLE_SMOKE_INPUT_V1":
        raise RuntimeError("Unexpected 050 style-smoke manifest schema")
    if manifest.get("task_key") != "050_writing_style_host_codex_runtime":
        raise RuntimeError("Manifest is not for task 050")

    source = plaintext_path.read_text(encoding="utf-8")
    expected_source_sha = manifest["source"]["segment_sha256"]
    actual_source_sha = sha256_text(source)
    if actual_source_sha != expected_source_sha:
        raise RuntimeError("Source segment SHA-256 does not match manifest")

    runtime = load_runtime()
    runtime_result = runtime.validate_host_stage_package(source, stage_dir, candidate_path=candidate_path)
    write_json(receipt_path, runtime_result["receipt"])

    candidate = runtime_result["candidate"]
    result = {
        "schema": "AI_SKILLS_050_PRIVATE_STYLE_SMOKE_PUBLIC_RESULT_V1",
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "task_key": manifest["task_key"],
        "smoke_id": manifest["smoke_id"],
        "role": manifest["role"],
        "line_ranges": manifest["source"]["line_ranges"],
        "full_private_source_sha256": manifest["source"]["full_private_source_sha256"],
        "source_segment_sha256": actual_source_sha,
        "source_plaintext_size_bytes": len(source.encode("utf-8")),
        "implementation_commit": manifest["implementation_commit"],
        "production_entrypoint": manifest["production_entrypoint"],
        "host_codex_generation": True,
        "openai_generation_call_count": 0,
        "paid_review_call_count": 0,
        "requires_openai_api_key": False,
        "private_plaintext_committed": False,
        "private_stage_dir": str(stage_dir),
        "private_candidate_path": str(candidate_path),
        "candidate_sha256": sha256_text(candidate),
        "candidate_size_bytes": len(candidate.encode("utf-8")),
        "stage_receipt": {
            "path": args.receipt,
            "sha256": sha256_file(receipt_path),
            "schema": runtime_result["receipt"]["schema"],
            "runtime": runtime_result["receipt"]["runtime"],
            "unit_count": runtime_result["receipt"]["unit_count"],
            "stage_count": runtime_result["receipt"]["stage_count"],
            "dataflow_ok": runtime_result["receipt"]["dataflow_validation"]["ok"],
            "exact_ok": runtime_result["receipt"]["exact_verification"]["ok"],
            "literal_count": runtime_result["receipt"]["exact_verification"]["literal_count"],
        },
    }
    write_json(result_path, result)


if __name__ == "__main__":
    main()
