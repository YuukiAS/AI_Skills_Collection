#!/usr/bin/env python3
"""Run one private 049 style-smoke sample through the staged rewrite runtime.

The caller supplies plaintext from a temporary decrypted file. This script keeps
the candidate plaintext in the caller-provided work directory, writes only the
public stage receipt and metadata to the repository, and encrypts the candidate
to the manifest's output age recipient.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_HELPER = (
    REPO_ROOT
    / "plugins/codex/plugins/writing-style/skills/scientific-rewrite/scripts/rewrite_support.py"
)
DEFAULT_MODEL = "gpt-5.6-terra"


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


def encrypt_with_age(candidate_path: Path, recipient: str, output_age: Path, workdir: Path) -> None:
    tmp_output = workdir / "candidate-output.age"
    if tmp_output.exists():
        tmp_output.unlink()
    subprocess.run(
        ["age", "-r", recipient, "-o", str(tmp_output), str(candidate_path)],
        check=True,
        cwd=str(REPO_ROOT),
    )
    output_age.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(tmp_output), str(output_age))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--plaintext", required=True)
    parser.add_argument("--output-age", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--workdir", required=True)
    parser.add_argument("--model", default=os.environ.get("OPENAI_TEXT_TRANSFORM_MODEL") or DEFAULT_MODEL)
    args = parser.parse_args()

    manifest_path = repo_path(args.manifest)
    output_age_path = repo_path(args.output_age)
    result_path = repo_path(args.result)
    receipt_path = repo_path(args.receipt)
    plaintext_path = Path(args.plaintext)
    workdir = Path(args.workdir)
    workdir.mkdir(parents=True, exist_ok=True)
    os.chmod(workdir, 0o700)

    manifest = load_json(manifest_path)
    if manifest.get("schema") != "AI_BRIDGE_TEXT_TRANSFORM_MANIFEST_V1":
        raise RuntimeError("Unexpected text transform manifest schema")
    if manifest.get("transform_kind") != "scientific-rewrite-staged-smoke":
        raise RuntimeError("Manifest is not a 049 staged style-smoke transform")
    if not manifest.get("external_upload_authorization"):
        raise RuntimeError("Missing private artifact upload authorization record")

    source = plaintext_path.read_text(encoding="utf-8")
    expected_source_sha = manifest["input"]["plaintext_sha256"]
    actual_source_sha = sha256_text(source)
    if actual_source_sha != expected_source_sha:
        raise RuntimeError("Decrypted source plaintext SHA-256 does not match manifest")

    api_key = (
        os.environ.get("OPENAI_TEXT_TRANSFORM_API_KEY", "")
        or os.environ.get("OPENAI_REVIEW_API_KEY", "")
        or os.environ.get("OPENAI_API_KEY", "")
    )
    if not api_key:
        raise RuntimeError("OpenAI API key unavailable in GitHub Actions environment")

    runtime = load_runtime()
    runtime_result = runtime.run_multistage(
        source,
        driver="openai-responses",
        model=args.model,
        api_key=api_key,
        stage_dir=None,
        smoke_role=manifest.get("smoke", {}).get("id", ""),
    )
    candidate = runtime_result["candidate"]
    candidate_path = workdir / "candidate.md"
    candidate_path.write_text(candidate, encoding="utf-8")
    write_json(receipt_path, runtime_result["receipt"])

    recipient = manifest["output"]["public_recipient"]
    encrypt_with_age(candidate_path, recipient, output_age_path, workdir)

    encrypted_input_path = repo_path(manifest["input"]["encrypted_payload_path"])
    recipient_path = repo_path(manifest["output"]["public_recipient_path"])
    result = {
        "schema": "AI_SKILLS_049_PRIVATE_STYLE_SMOKE_TRANSFORM_V1",
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "task_key": manifest["task_key"],
        "workflow_type": manifest.get("workflow_type", "reviewed_handoff"),
        "transform_kind": manifest["transform_kind"],
        "prompt_version": manifest.get("prompt_version", ""),
        "bridge_kit_commit": os.environ.get("AI_BRIDGE_KIT_COMMIT", ""),
        "model": args.model,
        "store": False,
        "plaintext_committed": False,
        "private_plaintext_committed": False,
        "input_manifest": {
            "path": args.manifest,
            "sha256": sha256_file(manifest_path),
            "external_upload_authorization_recorded": True,
            "identity_bindings": manifest.get("identity_bindings", {}),
            "privacy_policy": manifest.get("privacy_policy", ""),
        },
        "smoke": manifest.get("smoke", {}),
        "encrypted_input": {
            "path": manifest["input"]["encrypted_payload_path"],
            "sha256": sha256_file(encrypted_input_path),
        },
        "source_plaintext_sha256": actual_source_sha,
        "source_plaintext_size_bytes": len(source.encode("utf-8")),
        "runtime": {
            "name": runtime_result["receipt"]["runtime"],
            "schema": runtime_result["receipt"]["schema"],
            "driver": runtime_result["receipt"]["driver"],
            "receipt_path": args.receipt,
            "receipt_sha256": sha256_file(receipt_path),
            "unit_count": runtime_result["receipt"]["unit_count"],
            "stage_count": runtime_result["receipt"]["stage_count"],
            "model_call_count": runtime_result["receipt"]["model_call_count"],
            "whole_document_writer_call": runtime_result["receipt"]["whole_document_writer_call"],
            "max_examples_per_unit": runtime_result["receipt"]["max_examples_per_unit"],
            "full_seed_library_injected": runtime_result["receipt"]["full_seed_library_injected"],
        },
        "output_plaintext_sha256": sha256_text(candidate),
        "output_plaintext_size_bytes": len(candidate.encode("utf-8")),
        "encrypted_output": {
            "path": args.output_age,
            "sha256": sha256_file(output_age_path),
        },
        "output_public_recipient": {
            "path": manifest["output"]["public_recipient_path"],
            "sha256": sha256_file(recipient_path),
        },
    }
    write_json(result_path, result)


if __name__ == "__main__":
    main()
