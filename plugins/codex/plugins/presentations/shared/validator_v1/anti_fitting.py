"""AST/static anti-answer-fitting scan for generic validator production code."""

from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Any


FORBIDDEN_LITERAL_PATTERNS = [
    re.compile(r"\bSTAT5060\b"),
    re.compile(r"\bT01-[A-Z0-9-]+\b"),
    re.compile(r"\bV\d{2}\b"),
    re.compile(r"\bfeedback[_-]?id\b", re.I),
    re.compile(r"\bexpected[_-]?(pass|fail|revise|verdict)\b", re.I),
    re.compile(r"\bpage[_-]?results\b", re.I),
    re.compile(r"\bfresh[-_]page[-_]review\b", re.I),
]


class _Visitor(ast.NodeVisitor):
    def __init__(self, path: Path) -> None:
        self.path = path
        self.findings: list[dict[str, Any]] = []

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            self._check_text("import", alias.name, node.lineno)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        self._check_text("import", node.module or "", node.lineno)

    def visit_Constant(self, node: ast.Constant) -> None:
        if isinstance(node.value, str):
            self._check_text("literal", node.value, node.lineno)

    def _check_text(self, kind: str, text: str, line: int) -> None:
        for pattern in FORBIDDEN_LITERAL_PATTERNS:
            if pattern.search(text):
                self.findings.append({"path": str(self.path), "line": line, "kind": kind, "pattern": pattern.pattern, "text": text[:180]})


def scan_paths_for_answer_fitting(paths: list[Path]) -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    scanned = 0
    for root in paths:
        candidates = [root] if root.is_file() else sorted(root.rglob("*.py"))
        for path in candidates:
            if "__pycache__" in path.parts or path.name.startswith("test_"):
                continue
            scanned += 1
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            visitor = _Visitor(path)
            visitor.visit(tree)
            findings.extend(visitor.findings)
    return {
        "scanned_files": scanned,
        "finding_count": len(findings),
        "findings": findings,
        "AST_ANTI_FITTING": "PASS" if not findings else "FAIL",
        "GENERIC_CORE_PROJECT_SPECIFIC_BRANCHES": len(findings),
    }
