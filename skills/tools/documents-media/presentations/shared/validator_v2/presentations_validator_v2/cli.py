"""Stable CLI for validator evidence, with machine-readable stdout or file output."""

import argparse
import json
from pathlib import Path

from . import __version__, adapters, integrity, layout
from .io import EvidenceMissing, InputError, read, read_contract, read_json, sha256
from .schemas import Finding, report


FORBIDDEN_SELECTORS = {
    "fixture_name", "fixture_id", "mutation_id", "expected_verdict",
    "bad_page_number", "human_complaint",
}


LAYOUT_INPUTS = ("contract", "pdf", "source_manifest", "object_map", "source_root")
LAYOUT_FLAGS = tuple(name.replace("_", "-") for name in LAYOUT_INPUTS)


def parser():
    result = argparse.ArgumentParser(prog="presentations_validator_v2")
    commands = result.add_subparsers(dest="command", required=True)
    for name, required, optional in (
        ("validate", ("authority-bundle", "candidate-bundle", "repo"),
         (*LAYOUT_FLAGS, "baseline-pdf")),
        ("layout", LAYOUT_FLAGS, ("baseline-pdf",)),
        ("replay", ("config", "repo"), ()),
    ):
        cmd = commands.add_parser(name)
        for flag in required:
            cmd.add_argument(f"--{flag}", type=Path, required=True)
        for flag in (*optional, "out"):
            cmd.add_argument(f"--{flag}", type=Path)
    cmd = commands.add_parser("inspect")
    cmd.add_argument("--out", type=Path)
    return result


def package_identity():
    root = Path(__file__).parent
    return sha256(b"".join(
        path.relative_to(root).as_posix().encode("utf-8") + b"\0" + read(path) + b"\0"
        for path in sorted(root.rglob("*.py"))
    ))


def inspect():
    import ast

    root = Path(__file__).parent
    callables = {key: f"{fn.__module__}.{fn.__name__}" for key, fn in layout.DETECTORS.items()}
    suspicious = []
    for path in sorted(root.rglob("*.py")):
        tree = ast.parse(read(path))
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.IfExp, ast.Match)):
                expr = node.subject if isinstance(node, ast.Match) else node.test
                for item in ast.walk(expr):
                    value = (item.id if isinstance(item, ast.Name) else
                             item.attr if isinstance(item, ast.Attribute) else
                             item.value if isinstance(item, ast.Constant) else None)
                    if isinstance(value, str) and value in FORBIDDEN_SELECTORS:
                        suspicious.append(f"{path.relative_to(root)}:{node.lineno}")
    integrity_hooks = [f"{fn.__module__}.{fn.__name__}" for fn in integrity.DETECTORS]
    return {"layout_hooks": callables, "integrity_hooks": integrity_hooks,
            "conditional_selector_hits": sorted(set(suspicious)),
            "scope": "AST scan for known forbidden selectors; not a semantic proof"}


def layout_evidence(args, pdf):
    return layout.validate(
        read_contract(args.contract), pdf, read_json(args.source_manifest),
        read_json(args.object_map), args.source_root,
        read(args.baseline_pdf) if args.baseline_pdf else None,
    )


def run(args):
    info = {"validator_version": __version__, "code_sha256": package_identity()}
    try:
        if args.command == "validate":
            rows, identity = integrity.validate(args.authority_bundle, args.candidate_bundle, args.repo)
            if any(getattr(args, name) for name in (*LAYOUT_INPUTS, "baseline_pdf")):
                if not all(getattr(args, name) for name in LAYOUT_INPUTS):
                    raise InputError("Combined validation requires all five layout inputs")
                data = read(args.pdf)
                if sha256(data) not in identity["verified_artifact_hashes"]:
                    raise InputError("Layout PDF is not a verified Git artifact in the candidate bundle")
                layout_rows, geometry = layout_evidence(args, data)
                rows.extend(layout_rows)
                identity.update(geometry)
        elif args.command == "layout":
            rows, identity = layout_evidence(args, read(args.pdf))
        elif args.command == "replay":
            config = read_json(args.config)
            identity = {"config_sha256": sha256(read(args.config))}
            rows = adapters.replay(args.repo, config)
        else:
            return {**info, **inspect()}, 0
    except EvidenceMissing as exc:
        identity = {}
        rows = [Finding("INPUT", "NOT_VERIFIED", args.command, str(exc))]
    except (InputError, ValueError, KeyError, TypeError, AttributeError, IndexError) as exc:
        identity = {}
        rows = [Finding("INPUT", "FAIL", args.command, f"Invalid evidence: {exc}")]
    result = report(rows, **info, **identity)
    code = {"DETERMINISTIC_FAIL": 1, "DETERMINISTIC_INCOMPLETE": 2}.get(result["state"], 0)
    return result, code


def main():
    args = parser().parse_args()
    result, code = run(args)
    payload = json.dumps(result, indent=2, sort_keys=True, allow_nan=False, ensure_ascii=False)
    if args.out:
        args.out.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return code
