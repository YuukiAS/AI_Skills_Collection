#!/usr/bin/env python3
"""Deterministic helpers for the scientific-rewrite skill."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIBRARY = ROOT / "references" / "seed-transformations.json"

NUMBER_RE = re.compile(r"(?<![\w.])[-+]?\d+(?:\.\d+)?(?:%|‰)?(?![\w.])")
DATE_RE = re.compile(r"\b(?:20\d{2}|19\d{2})(?:[-/年](?:0?[1-9]|1[0-2]))?(?:[-/月](?:0?[1-9]|[12]\d|3[01]))?日?\b")
UNIT_RE = re.compile(r"(?<![A-Za-z])\d+(?:\.\d+)?\s?(?:ms|s|min|h|GB|MB|KB|B|mm|cm|m|kg|g|mg|μm|um|%|℃|°C)\b")
CITATION_RE = re.compile(r"(?:\[[0-9,\-\s]+\]|\([A-Z][A-Za-z-]+(?: et al\.)?,\s*(?:19|20)\d{2}\)|doi:\s*10\.\S+)", re.IGNORECASE)
CODE_RE = re.compile(r"`[^`]+`")
PATH_RE = re.compile(r"(?:^|(?<=\s))(?:[./~]?[\w.-]+/[\w./-]+)(?=$|\s|[，。；,;)])")
FORMULA_RE = re.compile(r"(\$\$.*?\$\$|\$[^$\n]+\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))", re.DOTALL)
FORMAL_NAME_RE = re.compile(r"\b[A-Z][A-Za-z0-9]*(?:[-_][A-Za-z0-9]+|[A-Z][A-Za-z0-9]*)+\b")


@dataclass(frozen=True)
class RewriteUnit:
    unit_id: str
    heading: str
    start_line: int
    end_line: int
    text: str
    literal_invariants: list[dict[str, str]]


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def unique_spans(kind: str, matches: Iterable[str]) -> list[dict[str, str]]:
    seen: set[str] = set()
    spans: list[dict[str, str]] = []
    for raw in matches:
        text = raw.strip()
        if not text or text in seen:
            continue
        seen.add(text)
        spans.append({"kind": kind, "text": text})
    return spans


def extract_literal_invariants(text: str) -> list[dict[str, str]]:
    spans: list[dict[str, str]] = []
    spans.extend(unique_spans("formula", (m.group(0) for m in FORMULA_RE.finditer(text))))
    spans.extend(unique_spans("code", (m.group(0) for m in CODE_RE.finditer(text))))
    spans.extend(unique_spans("citation", (m.group(0) for m in CITATION_RE.finditer(text))))
    spans.extend(unique_spans("date", (m.group(0) for m in DATE_RE.finditer(text))))
    spans.extend(unique_spans("unit", (m.group(0) for m in UNIT_RE.finditer(text))))
    spans.extend(unique_spans("number", (m.group(0) for m in NUMBER_RE.finditer(text))))
    spans.extend(unique_spans("path", (m.group(0) for m in PATH_RE.finditer(text))))
    spans.extend(unique_spans("formal_name", (m.group(0) for m in FORMAL_NAME_RE.finditer(text))))
    return spans


def split_markdown_units(text: str) -> list[RewriteUnit]:
    lines = text.splitlines()
    starts: list[tuple[int, str]] = []
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if match:
            starts.append((index, match.group(2)))
    if not starts:
        stripped = text.strip()
        return [
            RewriteUnit(
                unit_id="unit-001",
                heading="document",
                start_line=1,
                end_line=max(1, len(lines)),
                text=stripped,
                literal_invariants=extract_literal_invariants(stripped),
            )
        ]

    units: list[RewriteUnit] = []
    for pos, (start, heading) in enumerate(starts):
        end = starts[pos + 1][0] if pos + 1 < len(starts) else len(lines)
        unit_text = "\n".join(lines[start:end]).strip()
        units.append(
            RewriteUnit(
                unit_id=f"unit-{pos + 1:03d}",
                heading=heading,
                start_line=start + 1,
                end_line=end,
                text=unit_text,
                literal_invariants=extract_literal_invariants(unit_text),
            )
        )
    return units


def load_seed_library(path: Path = DEFAULT_LIBRARY) -> list[dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("seed transformation library must be a JSON list")
    return data


def _score_example(example: dict[str, str], filters: dict[str, str]) -> tuple[int, int, str]:
    score = 0
    for key, value in filters.items():
        if not value:
            continue
        candidate = str(example.get(key, ""))
        if candidate == value:
            score += 3
        elif value in candidate or candidate in value:
            score += 1
    high_risk_penalty = 0 if example.get("fidelity_risk") == filters.get("fidelity_risk") else 1
    return (-score, high_risk_penalty, example.get("id", ""))


def select_examples(library: list[dict[str, str]], limit: int = 5, **filters: str) -> list[dict[str, str]]:
    if limit < 1:
        raise ValueError("limit must be positive")
    ranked = sorted(library, key=lambda item: _score_example(item, filters))
    selected: list[dict[str, str]] = []
    seen_functions: set[str] = set()
    for item in ranked:
        function = item.get("discourse_function", "")
        if function in seen_functions and len(selected) < min(3, limit):
            continue
        selected.append(item)
        seen_functions.add(function)
        if len(selected) == limit:
            break
    if len(selected) < min(limit, len(ranked)):
        selected_ids = {item.get("id") for item in selected}
        for item in ranked:
            if item.get("id") not in selected_ids:
                selected.append(item)
                if len(selected) == limit:
                    break
    return selected


def verify_exact(source: str, candidate: str, ledger: list[dict[str, str]] | None = None) -> dict[str, object]:
    invariants = ledger if ledger is not None else extract_literal_invariants(source)
    missing = []
    for invariant in invariants:
        text = invariant["text"]
        if text not in candidate:
            missing.append(invariant)
    return {
        "ok": not missing,
        "checked_count": len(invariants),
        "missing": missing,
    }


def command_prepare(args: argparse.Namespace) -> None:
    text = load_text(Path(args.source))
    units = split_markdown_units(text)
    print(json.dumps({"units": [asdict(unit) for unit in units]}, ensure_ascii=False, indent=2))


def command_select_examples(args: argparse.Namespace) -> None:
    library = load_seed_library(Path(args.library))
    selected = select_examples(
        library,
        limit=args.limit,
        scene=args.scene,
        discourse_function=args.discourse_function,
        rewrite_problem=args.rewrite_problem,
        fidelity_risk=args.fidelity_risk,
        register=args.register,
    )
    print(json.dumps({"examples": selected}, ensure_ascii=False, indent=2))


def command_verify_exact(args: argparse.Namespace) -> None:
    source = load_text(Path(args.source))
    candidate = load_text(Path(args.candidate))
    ledger = None
    if args.ledger:
        ledger = json.loads(Path(args.ledger).read_text(encoding="utf-8"))
    report = verify_exact(source, candidate, ledger)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if not report["ok"]:
        raise SystemExit(1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare")
    prepare.add_argument("--source", required=True)
    prepare.set_defaults(func=command_prepare)

    select = subparsers.add_parser("select-examples")
    select.add_argument("--library", default=str(DEFAULT_LIBRARY))
    select.add_argument("--scene", default="")
    select.add_argument("--discourse-function", default="")
    select.add_argument("--rewrite-problem", default="")
    select.add_argument("--fidelity-risk", default="")
    select.add_argument("--register", default="")
    select.add_argument("--limit", type=int, default=5)
    select.set_defaults(func=command_select_examples)

    verify = subparsers.add_parser("verify-exact")
    verify.add_argument("--source", required=True)
    verify.add_argument("--candidate", required=True)
    verify.add_argument("--ledger")
    verify.set_defaults(func=command_verify_exact)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
