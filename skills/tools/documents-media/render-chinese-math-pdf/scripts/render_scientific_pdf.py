#!/usr/bin/env python3
"""Canonical scientific Markdown/LaTeX PDF orchestration.

The default route is Markdown -> Pandoc AST/LaTeX -> XeLaTeX -> PDF.
Chromium is available only as an explicit diagnostic route.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPT_DIR.parent
DEFAULT_PROFILE_PATH = SKILL_ROOT / "profiles" / "canonical_formal_note.json"

if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import build_chinese_math_header  # noqa: E402
import probe_pdf_render_env as probe  # noqa: E402
import validate_pdf_layout as pdf_qa  # noqa: E402


MARKDOWN_EXTENSIONS = "markdown+tex_math_dollars+tex_math_single_backslash"
ROUTE_CANONICAL_MARKDOWN = "canonical-markdown"
ROUTE_DIRECT_XELATEX = "direct-xelatex"
ROUTE_CHROMIUM_DIAGNOSTIC = "chromium-diagnostic"
ROUTE_PROJECT_COMMAND = "project-command"


def run_command(args: list[str], *, cwd: Path | None = None, env: dict[str, str] | None = None, timeout: int = 180) -> dict[str, Any]:
    proc = subprocess.run(args, cwd=cwd, env=env, check=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=timeout)
    return {"args": args, "returncode": proc.returncode, "output": proc.stdout}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def math_type_name(value: Any) -> str:
    if isinstance(value, dict):
        return str(value.get("t") or value.get("c") or value)
    return str(value)


def collect_math_nodes(node: Any, result: list[dict[str, str]]) -> None:
    if isinstance(node, dict):
        if node.get("t") == "Math":
            content = node.get("c", [])
            if isinstance(content, list) and len(content) == 2:
                result.append({"mathtype": math_type_name(content[0]), "text": str(content[1])})
        for value in node.values():
            collect_math_nodes(value, result)
    elif isinstance(node, list):
        for item in node:
            collect_math_nodes(item, result)


def pandoc_ast(source: Path) -> dict[str, Any]:
    cmd = ["pandoc", str(source), "--from", MARKDOWN_EXTENSIONS, "--to", "json"]
    proc = run_command(cmd, cwd=source.parent)
    if proc["returncode"] != 0:
        raise RuntimeError("pandoc AST parse failed:\n" + proc["output"])
    return json.loads(proc["output"])


def math_signature_from_ast(ast: dict[str, Any]) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    collect_math_nodes(ast, result)
    return result


def math_signature(source: Path) -> list[dict[str, str]]:
    return math_signature_from_ast(pandoc_ast(source))


def math_anchor_tokens(math_text: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9]*|\\[A-Za-z]+|[0-9]+|[\u0370-\u03ff]+", math_text)
    cleaned: list[str] = []
    ignored = {
        "left",
        "right",
        "begin",
        "end",
        "frac",
        "sum",
        "int",
        "mathrm",
        "mathbf",
        "mathbb",
        "hat",
        "bar",
        "tilde",
        "cdot",
        "times",
    }
    for token in tokens:
        token = token.lstrip("\\")
        if token and token not in ignored and token not in cleaned:
            cleaned.append(token)
    if not cleaned:
        fallback = re.sub(r"\s+", "", math_text)
        if fallback:
            cleaned.append(fallback[:24])
    return cleaned


def generated_tex_math_survival(signature: list[dict[str, str]], tex_text: str) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    normalized_tex = re.sub(r"\s+", "", tex_text)
    for index, item in enumerate(signature):
        tokens = math_anchor_tokens(item["text"])
        matched = [token for token in tokens if token in tex_text or token in normalized_tex]
        check = {
            "index": index,
            "mathtype": item["mathtype"],
            "text": item["text"],
            "anchors": tokens,
            "matched_anchors": matched,
            "passed": bool(matched),
        }
        checks.append(check)
        if not check["passed"]:
            failures.append(check)
    return {"checks": checks, "failures": failures, "passed": not failures}


def tex_env(resource_dir: Path, work_dir: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["TEXMFHOME"] = str(resource_dir / "texmf")
    env["TEXMFVAR"] = str(work_dir / "texmf-var")
    env["TEXMFCONFIG"] = str(work_dir / "texmf-config")
    env["TEXMFCACHE"] = str(work_dir / "texmf-cache")
    env["TEXINPUTS"] = str(resource_dir / "texmf") + "//:"
    env["OSFONTDIR"] = os.pathsep.join(
        [
            str(resource_dir / "fonts"),
            str(resource_dir / "texmf" / "fonts" / "opentype" / "public" / "noto-cjk"),
        ]
    )
    for key in ["TEXMFVAR", "TEXMFCONFIG", "TEXMFCACHE"]:
        Path(env[key]).mkdir(parents=True, exist_ok=True)
    return env


def resolve_resource(args: argparse.Namespace) -> Path:
    resource = probe.find_resource(args.root, args.resource_dir, args.local_override)
    if resource is None:
        raise SystemExit("blocked_missing_dependency: chinese_math_pdf resource root not found")
    return resource


def dependency_probe(args: argparse.Namespace) -> dict[str, Any]:
    result = probe.build_probe_result(args)
    if not result["ready"]:
        raise SystemExit("blocked_missing_dependency: " + json.dumps(result, ensure_ascii=False, indent=2))
    return result


def effective_profile(profile: dict[str, Any], *, route: str, authority: str, source: Path, resource_dir: Path | None) -> dict[str, Any]:
    return {
        "profile_id": profile.get("id"),
        "authority": authority,
        "route": route,
        "engine": profile.get("engine") if route == ROUTE_CANONICAL_MARKDOWN else route,
        "source": str(source),
        "resource_dir": str(resource_dir) if resource_dir else None,
        "paper": profile.get("paper"),
        "fontsize": profile.get("fontsize"),
        "margin": profile.get("margin"),
        "linestretch": profile.get("linestretch"),
        "toc": bool(profile.get("toc")),
        "number_sections": bool(profile.get("number_sections")),
        "ordinary_prose_downscaling": bool(profile.get("ordinary_prose_downscaling")),
        "fonts": profile.get("fonts", {}),
    }


def pandoc_latex_args(source: Path, tex: Path, header: Path, profile: dict[str, Any]) -> list[str]:
    args = [
        "pandoc",
        str(source),
        "--from",
        MARKDOWN_EXTENSIONS,
        "--to",
        "latex",
        "--standalone",
        "--include-in-header",
        str(header),
        "--variable",
        f"papersize={profile['paper']}",
        "--variable",
        f"fontsize={profile['fontsize']}",
        "--variable",
        f"geometry:margin={profile['margin']}",
        "--variable",
        f"linestretch={profile['linestretch']}",
        "-o",
        str(tex),
    ]
    if profile.get("number_sections"):
        args.append("--number-sections")
    if profile.get("toc"):
        args.append("--toc")
    return args


def run_xelatex(tex: Path, output_pdf: Path, work_dir: Path, env: dict[str, str]) -> list[dict[str, Any]]:
    commands: list[dict[str, Any]] = []
    for _ in range(2):
        proc = run_command(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory", str(work_dir), str(tex)],
            cwd=tex.parent,
            env=env,
            timeout=240,
        )
        commands.append(proc)
        if proc["returncode"] != 0:
            raise RuntimeError("xelatex failed:\n" + proc["output"])
    produced = work_dir / f"{tex.stem}.pdf"
    if not produced.exists() or produced.stat().st_size == 0:
        raise RuntimeError(f"xelatex did not create a non-empty PDF: {produced}")
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(produced, output_pdf)
    return commands


def render_canonical_markdown(args: argparse.Namespace, work_dir: Path, profile: dict[str, Any]) -> dict[str, Any]:
    source = args.source.resolve()
    output = args.output.resolve()
    resource = resolve_resource(args)
    probe_result = dependency_probe(args)
    header = work_dir / "canonical-header.tex"
    generated_tex = work_dir / f"{source.stem}.generated.tex"
    header.write_text(
        build_chinese_math_header.build_header(
            argparse.Namespace(root=args.root, resource_dir=args.resource_dir, local_override=args.local_override)
        ),
        encoding="utf-8",
    )

    source_signature = math_signature(source)
    pandoc_cmd = pandoc_latex_args(source, generated_tex, header, profile)
    pandoc_proc = run_command(pandoc_cmd, cwd=source.parent)
    if pandoc_proc["returncode"] != 0:
        raise RuntimeError("pandoc LaTeX generation failed:\n" + pandoc_proc["output"])
    tex_text = generated_tex.read_text(encoding="utf-8", errors="replace")
    math_survival = generated_tex_math_survival(source_signature, tex_text)
    if not math_survival["passed"]:
        raise RuntimeError("generated LaTeX lost math anchors:\n" + json.dumps(math_survival, ensure_ascii=False, indent=2))
    xelatex_commands = run_xelatex(generated_tex, output, work_dir, tex_env(resource, work_dir))
    qa = pdf_qa.validate_pdf(output, source=source, preview_dir=args.preview_dir, preview_pages=args.preview_pages, canonical_profile=True)
    if qa["errors"]:
        raise RuntimeError("PDF QA failed:\n" + json.dumps(qa, ensure_ascii=False, indent=2))
    return {
        "route": ROUTE_CANONICAL_MARKDOWN,
        "probe": probe_result,
        "effective_profile": effective_profile(profile, route=ROUTE_CANONICAL_MARKDOWN, authority="canonical-default", source=source, resource_dir=resource),
        "source_math_signature": source_signature,
        "post_transform_math_signature": source_signature,
        "generated_tex": str(generated_tex),
        "generated_tex_math_survival": math_survival,
        "commands": {"pandoc_latex": pandoc_proc, "xelatex": xelatex_commands},
        "qa": qa,
    }


def render_direct_xelatex(args: argparse.Namespace, work_dir: Path) -> dict[str, Any]:
    source = args.source.resolve()
    output = args.output.resolve()
    resource = resolve_resource(args)
    probe_result = dependency_probe(args)
    commands = run_xelatex(source, output, work_dir, tex_env(resource, work_dir))
    qa = pdf_qa.validate_pdf(output, source=None, preview_dir=args.preview_dir, preview_pages=args.preview_pages, canonical_profile=False)
    if qa["errors"]:
        raise RuntimeError("PDF QA failed:\n" + json.dumps(qa, ensure_ascii=False, indent=2))
    profile = load_json(args.profile)
    return {
        "route": ROUTE_DIRECT_XELATEX,
        "probe": probe_result,
        "effective_profile": effective_profile(profile, route=ROUTE_DIRECT_XELATEX, authority="source-or-project", source=source, resource_dir=resource),
        "commands": {"xelatex": commands},
        "qa": qa,
    }


def render_chromium_diagnostic(args: argparse.Namespace, work_dir: Path) -> dict[str, Any]:
    source = args.source.resolve()
    output = args.output.resolve()
    script = SCRIPT_DIR / "render_markdown_pdf_chromium.py"
    cmd = [sys.executable, str(script), str(source), str(output), "--root", str(args.root or source.parent)]
    if args.resource_dir:
        cmd.extend(["--resource-dir", str(args.resource_dir)])
    proc = run_command(cmd, cwd=source.parent, timeout=240)
    if proc["returncode"] != 0:
        raise RuntimeError("Chromium diagnostic render failed:\n" + proc["output"])
    qa = pdf_qa.validate_pdf(output, source=source, preview_dir=args.preview_dir, preview_pages=args.preview_pages, canonical_profile=False)
    return {
        "route": ROUTE_CHROMIUM_DIAGNOSTIC,
        "diagnostic_only": True,
        "effective_profile": {
            "authority": "explicit-diagnostic",
            "route": ROUTE_CHROMIUM_DIAGNOSTIC,
            "source": str(source),
        },
        "commands": {"chromium_diagnostic": proc},
        "qa": qa,
    }


def render_project_command(args: argparse.Namespace, work_dir: Path) -> dict[str, Any]:
    if not args.project_command:
        raise SystemExit("project-command route requires --project-command")
    source = args.source.resolve()
    output = args.output.resolve()
    command = [part.format(source=str(source), output=str(output), work_dir=str(work_dir)) for part in shlex.split(args.project_command)]
    proc = run_command(command, cwd=source.parent, timeout=240)
    if proc["returncode"] != 0:
        raise RuntimeError("project render command failed:\n" + proc["output"])
    qa = pdf_qa.validate_pdf(output, source=source if source.suffix.lower() in {".md", ".markdown"} else None, preview_dir=args.preview_dir, preview_pages=args.preview_pages, canonical_profile=False)
    if qa["errors"]:
        raise RuntimeError("PDF QA failed:\n" + json.dumps(qa, ensure_ascii=False, indent=2))
    return {
        "route": ROUTE_PROJECT_COMMAND,
        "effective_profile": {
            "authority": "explicit-user-venue-project",
            "route": ROUTE_PROJECT_COMMAND,
            "source": str(source),
            "project_command": args.project_command,
        },
        "commands": {"project_command": proc},
        "qa": qa,
    }


def resolve_route(args: argparse.Namespace) -> str:
    if args.route != "auto":
        return args.route
    suffix = args.source.suffix.lower()
    if suffix == ".tex":
        return ROUTE_DIRECT_XELATEX
    return ROUTE_CANONICAL_MARKDOWN


def render(args: argparse.Namespace) -> dict[str, Any]:
    profile = load_json(args.profile)
    route = resolve_route(args)
    if args.work_dir:
        args.work_dir.mkdir(parents=True, exist_ok=True)
        work_context = None
        work_dir = args.work_dir.resolve()
    else:
        work_context = tempfile.TemporaryDirectory(prefix="scientific-pdf-render-")
        work_dir = Path(work_context.name)
    try:
        if route == ROUTE_CANONICAL_MARKDOWN:
            receipt = render_canonical_markdown(args, work_dir, profile)
        elif route == ROUTE_DIRECT_XELATEX:
            receipt = render_direct_xelatex(args, work_dir)
        elif route == ROUTE_CHROMIUM_DIAGNOSTIC:
            receipt = render_chromium_diagnostic(args, work_dir)
        elif route == ROUTE_PROJECT_COMMAND:
            receipt = render_project_command(args, work_dir)
        else:
            raise SystemExit(f"unknown route: {route}")
    finally:
        if work_context is not None:
            work_context.cleanup()
    receipt["status"] = "complete"
    receipt["output_pdf"] = str(args.output.resolve())
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--root", type=Path, default=None)
    parser.add_argument("--resource-dir", type=Path, default=None)
    parser.add_argument("--local-override", type=Path, default=None)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE_PATH)
    parser.add_argument("--route", choices=["auto", ROUTE_CANONICAL_MARKDOWN, ROUTE_DIRECT_XELATEX, ROUTE_CHROMIUM_DIAGNOSTIC, ROUTE_PROJECT_COMMAND], default="auto")
    parser.add_argument("--project-command")
    parser.add_argument("--work-dir", type=Path)
    parser.add_argument("--preview-dir", type=Path)
    parser.add_argument("--preview-pages", default="first", help="'first', 'all', or a comma-separated list of one-based pages.")
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    try:
        receipt = render(args)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if args.receipt:
        write_json(args.receipt, receipt)
    else:
        print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
