#!/usr/bin/env python3
"""Build the public GitHub Pages payload for external visual review.

The Pages payload is a transport layer for an already-rendered synthetic
regression PDF. It must not rebuild a parallel PDF or claim academic PASS.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


REQUIRED_SOURCE_FILES = [
    "EVIDENCE_MANIFEST.json",
    "RENDER_STATUS.json",
    "MECHANICAL_VISUAL_REVIEW.json",
    "pdf/research_group_meeting_regression.pdf",
]
PDF_NAME = "research_group_meeting_regression.pdf"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_page_count(path: Path) -> int:
    data = path.read_bytes()
    return len(re.findall(rb"/Type\s*/Page\b", data))


def require_file(path: Path) -> Path:
    if not path.is_file():
        raise SystemExit(f"missing required Pages source file: {path}")
    return path


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_source(source_dir: Path) -> tuple[Path, dict, dict, dict]:
    missing = [name for name in REQUIRED_SOURCE_FILES if not (source_dir / name).is_file()]
    if missing:
        raise SystemExit(f"visual review Pages source is missing required files: {missing}")

    evidence = load_json(source_dir / "EVIDENCE_MANIFEST.json")
    render = load_json(source_dir / "RENDER_STATUS.json")
    review = load_json(source_dir / "MECHANICAL_VISUAL_REVIEW.json")
    pdf = require_file(source_dir / "pdf" / PDF_NAME)

    if evidence.get("generator_may_pass") is not False:
        raise SystemExit("Pages source evidence must not allow generator PASS")
    if render.get("status") != "ok" or render.get("png_count") != 4:
        raise SystemExit(f"Pages source must be a successful four-page real render: {render}")
    if review.get("status") != "MECHANICAL_PASS":
        raise SystemExit(f"Pages source mechanical review did not pass: {review.get('status')}")
    if review.get("academic_visual_decision") != "NOT_ASSESSED":
        raise SystemExit("Pages source must not claim academic visual PASS")
    count = pdf_page_count(pdf)
    if count != 4:
        raise SystemExit(f"Pages PDF must contain exactly 4 pages, found {count}")
    return pdf, evidence, render, review


def copy_payload(source_dir: Path, destination: Path, implementation_commit: str, transport_commit: str) -> dict:
    pdf, _evidence, _render, _review = validate_source(source_dir)
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)

    files_to_copy = {
        "EVIDENCE_MANIFEST.json": source_dir / "EVIDENCE_MANIFEST.json",
        "RENDER_STATUS.json": source_dir / "RENDER_STATUS.json",
        "MECHANICAL_VISUAL_REVIEW.json": source_dir / "MECHANICAL_VISUAL_REVIEW.json",
        PDF_NAME: pdf,
    }
    for relative, source in files_to_copy.items():
        shutil.copy2(source, destination / relative)

    pdf_sha = sha256(destination / PDF_NAME)
    manifest = {
        "schema": "RESEARCH_PRESENTATION_GITHUB_PAGES_VISUAL_REVIEW_V1",
        "transport": "github_pages_pdf",
        "packet_scope": "synthetic_regression_visual_evidence_only",
        "implementation_commit": implementation_commit,
        "transport_commit": transport_commit,
        "academic_visual_decision": "NOT_ASSESSED",
        "pdf": {
            "path": PDF_NAME,
            "page_count": 4,
            "sha256": pdf_sha,
            "render_source": "PPTX -> LibreOffice -> PDF",
        },
        "published_files": [
            {
                "path": relative,
                "size_bytes": (destination / relative).stat().st_size,
                "sha256": sha256(destination / relative),
            }
            for relative in sorted(files_to_copy)
        ],
        "forbidden_publication_boundary": [
            ".cache reference corpus",
            "downloaded public research decks",
            "CARE/private clinical images",
            "patient data",
            "credentials",
            "private project artifacts",
        ],
    }
    manifest_path = destination / "packet_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def build_pages(source_dir: Path, pages_dir: Path, implementation_commit: str, transport_commit: str, copy_latest: bool) -> dict:
    target = pages_dir / "presentation-review" / implementation_commit
    manifest = copy_payload(source_dir, target, implementation_commit, transport_commit)
    if copy_latest:
        copy_payload(source_dir, pages_dir / "presentation-review" / "latest", implementation_commit, transport_commit)
    return {
        "pages_dir": str(pages_dir),
        "immutable_dir": str(target),
        "immutable_pdf_path": str(target / PDF_NAME),
        "implementation_commit": implementation_commit,
        "transport_commit": transport_commit,
        "pdf_sha256": manifest["pdf"]["sha256"],
        "page_count": manifest["pdf"]["page_count"],
        "latest_copied": copy_latest,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--pages-dir", type=Path, required=True)
    parser.add_argument("--implementation-commit", required=True)
    parser.add_argument("--transport-commit", required=True)
    parser.add_argument("--copy-latest", action="store_true")
    args = parser.parse_args()
    result = build_pages(
        args.source_dir,
        args.pages_dir,
        args.implementation_commit,
        args.transport_commit,
        args.copy_latest,
    )
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
