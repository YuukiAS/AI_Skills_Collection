#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import shutil
import sys
from pathlib import Path


def write_minimal_pdf(path: Path) -> None:
    payload = (
        b"%PDF-1.4\n"
        b"1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n"
        b"2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n"
        b"3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 200 120] "
        b"/Contents 4 0 R >> endobj\n"
        b"4 0 obj << /Length 44 >> stream\n"
        b"BT /F1 12 Tf 20 80 Td (probe pdf output) Tj ET\n"
        b"endstream endobj\n"
        b"trailer << /Root 1 0 R >>\n%%EOF\n"
    )
    path.write_bytes(payload)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("probe-output")
    out_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = out_dir / "minimal_probe.pdf"
    write_minimal_pdf(pdf_path)
    header_ok = pdf_path.read_bytes().startswith(b"%PDF-")
    result = {
        "default_path": {
            "xelatex": shutil.which("xelatex"),
            "typst": shutil.which("typst"),
        },
        "project_probe": {
            "minimal_pdf_writer": {
                "available": header_ok,
                "path": str(pdf_path),
                "sha256": sha256(pdf_path),
            }
        },
        "absent_contrast": {
            "definitely_missing_renderer": shutil.which("definitely-missing-ai-skills-renderer")
        },
    }
    (out_dir / "probe.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if header_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
