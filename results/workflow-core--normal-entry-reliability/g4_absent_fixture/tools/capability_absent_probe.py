#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ROUTES = [
    {
        "name": "canonical_task_route",
        "kind": "canonical",
        "relative_command": ["python3", "tools/canonical_pdf_route.py", "outputs/final.pdf"],
        "script": ROOT / "tools" / "canonical_pdf_route.py",
    },
    {
        "name": "matched_specialist_route",
        "kind": "specialist",
        "relative_command": ["python3", "specialist/render_pdf.py", "outputs/final.pdf"],
        "script": ROOT / "specialist" / "render_pdf.py",
    },
    {
        "name": "project_declared_runtime_route",
        "kind": "project_runtime",
        "relative_command": ["python3", ".project-runtime/render_pdf.py", "outputs/final.pdf"],
        "script": ROOT / ".project-runtime" / "render_pdf.py",
    },
]


def inspect_route(route: dict[str, object]) -> dict[str, object]:
    script = route["script"]
    assert isinstance(script, Path)
    result: dict[str, object] = {
        "name": route["name"],
        "kind": route["kind"],
        "relative_command": route["relative_command"],
        "script": str(script.relative_to(ROOT)),
        "script_exists": script.exists(),
        "usable": False,
    }
    if not script.exists():
        result["reason"] = "declared route script is absent in controlled fixture"
        return result
    proc = subprocess.run(
        [sys.executable, str(script), "outputs/final.pdf"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        timeout=10,
    )
    output = ROOT / "outputs" / "final.pdf"
    result.update(
        {
            "exit_code": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "output_exists": output.exists(),
            "output_has_pdf_header": output.exists() and output.read_bytes().startswith(b"%PDF-"),
        }
    )
    result["usable"] = bool(
        proc.returncode == 0 and result["output_exists"] and result["output_has_pdf_header"]
    )
    if not result["usable"]:
        result["reason"] = "declared route did not produce a valid PDF artifact"
    return result


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: capability_absent_probe.py <output-dir>")
    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)
    routes = [inspect_route(route) for route in ROUTES]
    report = {
        "fixture_root": str(ROOT),
        "closed_world_contract": ".ai-skills/capability-contract.md",
        "declared_route_count": len(routes),
        "usable_route_count": sum(1 for route in routes if route["usable"]),
        "routes": routes,
        "capability_status": "blocked_target_not_met"
        if all(not route["usable"] for route in routes)
        else "available",
        "missing_scope": [
            "canonical_task_route",
            "matched_specialist_route",
            "project_declared_runtime_route",
        ],
    }
    (out_dir / "capability_report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
