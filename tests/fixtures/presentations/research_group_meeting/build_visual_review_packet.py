#!/usr/bin/env python3
"""Build an external visual-review packet for the four-slide regression.

The packet is transport evidence only. It creates real PNG/PDF/PPTX files for
an external Planner to open, but it never writes an academic visual PASS.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


REPO_ROOT = Path(__file__).resolve().parents[4]
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "presentations" / "research_group_meeting"
GENERATOR = FIXTURE_ROOT / "generate_research_group_meeting_regression.py"
REVIEWER = FIXTURE_ROOT / "review_research_group_meeting_regression.py"
EXPECTED_RENDER = FIXTURE_ROOT / "expected_render"
CORE_IMPLEMENTATION_COMMIT = "2c54c52f287be94c5919bc5886fb52804f94fc49"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(
            f"command failed ({result.returncode}): {' '.join(cmd)}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )


def require_file(path: Path) -> Path:
    if not path.exists() or not path.is_file():
        raise SystemExit(f"missing required packet source file: {path}")
    return path


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def verify_render_chain(regression_dir: Path) -> dict:
    render_path = require_file(regression_dir / "RENDER_STATUS.json")
    review_path = require_file(regression_dir / "MECHANICAL_VISUAL_REVIEW.json")
    render = json.loads(render_path.read_text(encoding="utf-8"))
    review = json.loads(review_path.read_text(encoding="utf-8"))
    if render.get("status") != "ok":
        raise SystemExit(f"real PPTX render is not available: {render}")
    if render.get("png_count") != 4:
        raise SystemExit(f"expected 4 rendered PNGs, found {render.get('png_count')}")
    if review.get("status") != "MECHANICAL_PASS":
        raise SystemExit(f"mechanical visual review did not pass: {review.get('status')}")
    if review.get("academic_visual_decision") != "NOT_ASSESSED":
        raise SystemExit("mechanical review must not claim academic visual PASS")
    return {"render": render, "review": review}


def verify_golden_pngs(regression_dir: Path, strict: bool) -> list[dict[str, object]]:
    comparisons = []
    for slide in range(1, 5):
        generated = require_file(regression_dir / "rendered" / f"slide-{slide}.png")
        expected = require_file(EXPECTED_RENDER / f"slide-{slide}.png")
        generated_sha = sha256(generated)
        expected_sha = sha256(expected)
        matches = generated_sha == expected_sha
        if strict and not matches:
            raise SystemExit(f"generated slide-{slide}.png differs from committed golden render")
        comparisons.append(
            {
                "slide": slide,
                "generated": str(generated),
                "expected": str(expected),
                "generated_sha256": generated_sha,
                "expected_sha256": expected_sha,
                "byte_matches_committed_golden": matches,
            }
        )
    return comparisons


def write_packet_manifest(packet_dir: Path, implementation_commit: str, transport_commit: str, golden_comparison: list[dict[str, object]]) -> Path:
    files = sorted(path for path in packet_dir.rglob("*") if path.is_file() and path.name != "PACKET_MANIFEST.json")
    manifest = {
        "schema": "RESEARCH_PRESENTATION_VISUAL_REVIEW_PACKET_V1",
        "implementation_commit": implementation_commit,
        "transport_commit": transport_commit,
        "review_round": 2,
        "academic_visual_decision": "NOT_ASSESSED",
        "packet_scope": "external_visual_evidence_transport",
        "golden_render_comparison": golden_comparison,
        "files": [
            {
                "path": str(path.relative_to(packet_dir)),
                "size_bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in files
        ],
    }
    manifest_path = packet_dir / "PACKET_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (packet_dir / "SHA256SUMS.txt").write_text(
        "".join(f"{item['sha256']}  {item['path']}\n" for item in manifest["files"]),
        encoding="utf-8",
    )
    return manifest_path


def write_zip(packet_dir: Path, zip_path: Path) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as archive:
        for path in sorted(packet_dir.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(packet_dir))


def assemble_packet(regression_dir: Path, packet_dir: Path, implementation_commit: str, transport_commit: str, zip_path: Path | None, strict_golden_pngs: bool) -> dict:
    verify_render_chain(regression_dir)
    golden_comparison = verify_golden_pngs(regression_dir, strict=strict_golden_pngs)
    if packet_dir.exists():
        shutil.rmtree(packet_dir)
    packet_dir.mkdir(parents=True)

    copy_file(require_file(regression_dir / "EVIDENCE_MANIFEST.json"), packet_dir / "EVIDENCE_MANIFEST.json")
    copy_file(require_file(regression_dir / "RENDER_STATUS.json"), packet_dir / "RENDER_STATUS.json")
    copy_file(require_file(regression_dir / "MECHANICAL_VISUAL_REVIEW.json"), packet_dir / "MECHANICAL_VISUAL_REVIEW.json")
    copy_file(require_file(regression_dir / "research_group_meeting_regression.pptx"), packet_dir / "research_group_meeting_regression.pptx")
    copy_file(require_file(regression_dir / "pdf" / "research_group_meeting_regression.pdf"), packet_dir / "pdf" / "research_group_meeting_regression.pdf")
    for slide in range(1, 5):
        copy_file(require_file(regression_dir / "rendered" / f"slide-{slide}.png"), packet_dir / "rendered" / f"slide-{slide}.png")
        copy_file(require_file(EXPECTED_RENDER / f"slide-{slide}.png"), packet_dir / "expected_render" / f"slide-{slide}.png")

    (packet_dir / "VISUAL_REVIEW_PACKET.md").write_text(
        "\n".join(
            [
                "# Research Presentation Visual Review Packet",
                "",
                f"implementation_commit: {implementation_commit}",
                f"transport_commit: {transport_commit}",
                "review_round: 2",
                "packet_scope: evidence transport only",
                "academic_visual_decision: NOT_ASSESSED",
                "",
                "This packet is for external academic visual review. It does not claim academic visual PASS.",
                "",
                "Required files:",
                "- rendered/slide-1.png",
                "- rendered/slide-2.png",
                "- rendered/slide-3.png",
                "- rendered/slide-4.png",
                "- pdf/research_group_meeting_regression.pdf",
                "- research_group_meeting_regression.pptx",
                "- EVIDENCE_MANIFEST.json",
                "- RENDER_STATUS.json",
                "- MECHANICAL_VISUAL_REVIEW.json",
                "- PACKET_MANIFEST.json",
                "",
                "The packet includes committed golden PNGs and regenerated rendered PNGs.",
                "PACKET_MANIFEST.json records whether their SHA-256 values match byte-for-byte.",
                "CI does not fail on renderer/font pixel drift unless --strict-golden-pngs is set.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    manifest_path = write_packet_manifest(packet_dir, implementation_commit, transport_commit, golden_comparison)
    if zip_path is not None:
        write_zip(packet_dir, zip_path)
    return {
        "packet_dir": str(packet_dir),
        "packet_manifest": str(manifest_path),
        "zip_path": str(zip_path) if zip_path is not None else None,
        "file_count": len([path for path in packet_dir.rglob("*") if path.is_file()]),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regression-dir", type=Path, default=Path(".cache/research-group-meeting-regression-current"))
    parser.add_argument("--packet-dir", type=Path, default=Path(".cache/research-presentation-visual-review-packet"))
    parser.add_argument("--zip-path", type=Path, default=Path(".cache/research-presentation-visual-review-packet.zip"))
    parser.add_argument("--implementation-commit", default=CORE_IMPLEMENTATION_COMMIT)
    parser.add_argument("--transport-commit", default=os.environ.get("GITHUB_SHA", "LOCAL_OR_EXTERNAL_RUNNER"))
    parser.add_argument("--skip-generate", action="store_true", help="Assemble from an existing regression directory.")
    parser.add_argument("--strict-golden-pngs", action="store_true", help="Fail if regenerated PNG bytes differ from committed golden renders.")
    args = parser.parse_args()
    if not args.skip_generate:
        run([sys.executable, str(GENERATOR), "--out-dir", str(args.regression_dir)])
        run([sys.executable, str(REVIEWER), "--out-dir", str(args.regression_dir)])
    result = assemble_packet(
        args.regression_dir,
        args.packet_dir,
        args.implementation_commit,
        args.transport_commit,
        args.zip_path,
        args.strict_golden_pngs,
    )
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
