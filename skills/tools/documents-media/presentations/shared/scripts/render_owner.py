#!/usr/bin/env python3
"""Adapter for the render-chinese-math-pdf environment contract.

Presentations owns template behavior. The render-chinese-math-pdf skill owns
machine-specific resource discovery, TeX cache policy, compiler probing, and
font-resource discovery. This module consumes that skill's probe output without
reimplementing its resolver.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


SHARED = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[6]
RENDER_SKILL_ROOT = REPO_ROOT / "skills" / "tools" / "documents-media" / "render-chinese-math-pdf"
RENDER_PROBE = RENDER_SKILL_ROOT / "scripts" / "probe_pdf_render_env.py"
OWNER = "render-chinese-math-pdf"


def _rel(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def probe(root: Path = REPO_ROOT, *, resource_dir: Path | None = None) -> dict[str, Any]:
    if not RENDER_PROBE.exists():
        return {
            "schema": "PRESENTATIONS_RENDER_OWNER_PROBE_V1",
            "environment_owner": OWNER,
            "status": "blocked_missing_dependency",
            "missing_dependency": _rel(RENDER_PROBE),
            "probe": _rel(RENDER_PROBE),
            "payload": None,
        }
    cmd = [sys.executable, str(RENDER_PROBE), "--root", str(root), "--pretty"]
    if resource_dir is not None:
        cmd.extend(["--resource-dir", str(resource_dir)])
    run = subprocess.run(cmd, check=False, capture_output=True, text=True)
    try:
        payload = json.loads(run.stdout)
    except json.JSONDecodeError:
        payload = {"raw_stdout": run.stdout}
    missing = first_missing_dependency(payload)
    return {
        "schema": "PRESENTATIONS_RENDER_OWNER_PROBE_V1",
        "environment_owner": OWNER,
        "status": "ok" if run.returncode == 0 and payload.get("ready") else "blocked_missing_dependency",
        "failure_status": payload.get("failure_status"),
        "missing_dependency": missing,
        "probe": _rel(RENDER_PROBE),
        "returncode": run.returncode,
        "stderr": run.stderr,
        "payload": payload,
        "resolved_route": {
            "resource_dir": payload.get("resource_dir"),
            "default_renderer": payload.get("default_renderer"),
        },
    }


def first_missing_dependency(payload: dict[str, Any]) -> str | None:
    if not payload:
        return "render-chinese-math-pdf probe output"
    if not payload.get("resource_dir"):
        return "render resource directory"
    for group in ("commands", "latex_packages", "fonts"):
        values = payload.get(group) or {}
        for name, item in values.items():
            if not item.get("available"):
                return f"{group}.{name}"
    return None


def command_path(probe_payload: dict[str, Any], name: str) -> str | None:
    commands = ((probe_payload.get("payload") or {}).get("commands") or {})
    item = commands.get(name) or {}
    path = item.get("path")
    return str(path) if item.get("available") and path else None


def resource_dir(probe_payload: dict[str, Any]) -> Path | None:
    raw = ((probe_payload.get("payload") or {}).get("resource_dir"))
    return Path(raw) if raw else None


def tex_inputs(probe_payload: dict[str, Any], template_inputs: list[Path] | None = None) -> str:
    parts: list[str] = []
    for template_input in template_inputs or []:
        parts.append(str(template_input.resolve()) + "//")
    resource = resource_dir(probe_payload)
    if resource is not None:
        texmf = resource / "texmf"
        if texmf.exists():
            parts.append(str(texmf.resolve()) + "//")
    existing = os.environ.get("TEXINPUTS")
    if existing:
        parts.append(existing)
    else:
        parts.append("")
    return os.pathsep.join(parts)


def tex_cache_env(build_dir: Path, probe_payload: dict[str, Any], *, template_inputs: list[Path] | None = None) -> dict[str, str]:
    cache_root = build_dir / ".tex-cache"
    env = {
        "TEXMFVAR": str(cache_root / "var"),
        "TEXMFCONFIG": str(cache_root / "config"),
        "TEXMFCACHE": str(cache_root / "cache"),
        "TEXINPUTS": tex_inputs(probe_payload, template_inputs),
    }
    resource = resource_dir(probe_payload)
    if resource is not None:
        env["TEXMFHOME"] = str((resource / "texmf").resolve())
        font_dirs = [
            resource / "fonts",
            resource / "texmf" / "fonts" / "opentype",
            resource / "texmf" / "fonts" / "truetype",
        ]
        existing = os.environ.get("OSFONTDIR")
        env["OSFONTDIR"] = os.pathsep.join([str(path.resolve()) for path in font_dirs if path.exists()] + ([existing] if existing else []))
    return env


def font_dir(probe_payload: dict[str, Any], relative: str) -> Path | None:
    resource = resource_dir(probe_payload)
    if resource is None:
        return None
    path = resource / relative
    return path if path.exists() else None


def times_font_dir(probe_payload: dict[str, Any]) -> tuple[Path | None, str]:
    override = os.environ.get("AI_SKILLS_TIMES_FONT_DIR")
    if override:
        return Path(override).expanduser(), "AI_SKILLS_TIMES_FONT_DIR"
    path = font_dir(probe_payload, "fonts/times")
    if path is not None:
        return path, "render-owner resource fonts/times"
    return None, "missing"


def manifest(probe_payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema": "PRESENTATIONS_RENDER_OWNER_MANIFEST_V1",
        "environment_owner": OWNER,
        "probe": probe_payload.get("probe"),
        "status": probe_payload.get("status"),
        "failure_status": probe_payload.get("failure_status"),
        "missing_dependency": probe_payload.get("missing_dependency"),
        "resolved_route": probe_payload.get("resolved_route"),
        "private_presentations_resolver": False,
    }
