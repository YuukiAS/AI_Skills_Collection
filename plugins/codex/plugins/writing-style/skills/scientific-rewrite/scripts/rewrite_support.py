#!/usr/bin/env python3
"""Deterministic support for host-Codex scientific rewrites.

The helper is deliberately not a writer. The current host Codex session owns
document understanding, meaning cards, candidate prose, semantic self-audit,
repair, and assembly. This file provides only mechanical checks and
privacy-safe receipts for those host-authored stage artifacts.
"""

from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import re
import sys
import time
from pathlib import Path
from typing import Any


RUNTIME_SCHEMA = "SCIENTIFIC_REWRITE_HOST_CODEX_STAGE_RECEIPT_V1"
RUNTIME_NAME = "scientific-rewrite.host-codex.v1"
REPO_ROOT = Path(__file__).resolve().parents[5]
SEED_LIBRARY = Path(__file__).resolve().parents[1] / "references" / "seed-transformations.json"
SEMANTIC_FIELDS = [
    "claims",
    "evidence",
    "conditions",
    "comparators",
    "uncertainty",
    "caveats",
    "negative_findings",
    "attribution",
    "decision_logic",
]
EVIDENCE_CLASSES = {
    "project_fact",
    "literature_fact",
    "research_interpretation",
    "candidate_method",
    "still_unverified",
}
RAW_LITERAL_DUMP_PATTERNS = [
    r"保留.{0,6}精确.{0,4}项",
    r"缺失.{0,4}精确.{0,4}项",
    r"literal\s+dump",
    r"raw\s+literal",
]


@dataclasses.dataclass(frozen=True)
class RewriteUnit:
    unit_id: str
    heading: str
    text: str
    start_line: int
    end_line: int
    literal_invariants: list[dict[str, str]]
    source_span_ids: list[str]
    argument_role: str
    why_these_spans_belong_together: str


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def canonical_json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_seed_library(path: Path = SEED_LIBRARY) -> list[dict[str, Any]]:
    data = load_json(path)
    if not isinstance(data, list):
        raise RuntimeError("seed transformation library must be a JSON list")
    return data


def select_examples(
    library: list[dict[str, Any]],
    *,
    limit: int = 4,
    scene: str = "",
    discourse_function: str = "",
    rewrite_problem: str = "",
    fidelity_risk: str = "",
    register: str = "",
) -> list[dict[str, Any]]:
    if limit < 1:
        raise ValueError("limit must be positive")
    targets = {
        "scene": scene,
        "discourse_function": discourse_function,
        "rewrite_problem": rewrite_problem,
        "fidelity_risk": fidelity_risk,
        "register": register,
    }
    scored: list[tuple[int, str, dict[str, Any]]] = []
    for item in library:
        score = sum(1 for key, value in targets.items() if value and item.get(key) == value)
        scored.append((score, str(item.get("id", "")), item))
    selected: list[dict[str, Any]] = []
    seen_functions: set[str] = set()
    for _score, _item_id, item in sorted(scored, key=lambda row: (-row[0], row[1])):
        if len(selected) >= limit:
            break
        function = str(item.get("discourse_function", ""))
        if len(selected) < min(2, limit) and function in seen_functions:
            continue
        selected.append(item)
        seen_functions.add(function)
    if len(selected) < min(limit, len(library)):
        chosen = {item.get("id") for item in selected}
        for _score, _item_id, item in sorted(scored, key=lambda row: (-row[0], row[1])):
            if len(selected) >= limit:
                break
            if item.get("id") not in chosen:
                selected.append(item)
                chosen.add(item.get("id"))
    return selected


def _literal_role(text: str) -> str:
    if "/" in text or text.startswith("`") or re.match(r"^[A-Za-z0-9_.-]+\.(json|md|py|pt|ckpt|txt)$", text):
        return "relocatable-trace"
    return "inline-critical"


def extract_literal_invariants(text: str) -> list[dict[str, str]]:
    atomic_specs = [
        r"`[^`\n]+`",
        r"(\$\$[\s\S]*?\$\$|\$[^$\n]+\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))",
        r"(?:^|\s)(/[^\s，。；；,]+)",
        r"(?:^|\s)([A-Za-z0-9_.-]+/[A-Za-z0-9_./-]+)",
        r"\[[0-9,\-\s]+\]",
        r"\b[A-Za-z][A-Za-z0-9_]*=[0-9.]+\b",
        r"([𝑅𝑈𝑀𝜃𝑘𝑗𝑧𝑤𝐹𝐻𝐿ℓ𝑔𝑝𝑦𝑥𝐷𝛥𝑖∇⊤∣∑∫∥][^\n。；]*[=≈≤≥≪∑∫∥][^\n。；]*)",
    ]
    nested_specs = [
        r"\b\d{4}-\d{2}-\d{2}\b",
        r"\b\d+(?:\.\d+)?%?\b",
        r"\b[A-Z](?:&[A-Z][a-z]?)+\b",
        r"\b(?:[A-Z]{2,}[A-Za-z0-9-]*|[A-Za-z]+[A-Z][A-Za-z0-9-]*|[A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+)\b",
    ]
    seen: set[str] = set()
    literals: list[dict[str, str]] = []
    protected_spans: list[tuple[int, int]] = []

    def add_match(match: re.Match[str], *, protect: bool) -> None:
        group_index = 1 if match.lastindex else 0
        value = match.group(group_index).strip()
        start, end = match.span(group_index)
        if not value or value in seen:
            return
        if _span_overlaps((start, end), protected_spans):
            return
        seen.add(value)
        literals.append({"text": value, "sha256": sha256_text(value), "role": _literal_role(value)})
        if protect:
            protected_spans.append((start, end))

    for pattern in atomic_specs:
        for match in re.finditer(pattern, text):
            add_match(match, protect=True)
    for pattern in nested_specs:
        for match in re.finditer(pattern, text):
            add_match(match, protect=False)
    return literals


def _span_overlaps(span: tuple[int, int], protected_spans: list[tuple[int, int]]) -> bool:
    start, end = span
    return any(start < protected_end and end > protected_start for protected_start, protected_end in protected_spans)


def split_markdown_units(text: str, *, max_paragraphs_per_unit: int = 4) -> list[RewriteUnit]:
    lines = text.splitlines()
    blocks: list[tuple[str, int, int]] = []
    start: int | None = None
    current: list[str] = []
    for index, line in enumerate(lines, start=1):
        if line.strip():
            if start is None:
                start = index
            current.append(line)
        elif current:
            blocks.append(("\n".join(current).strip(), start or index, index - 1))
            start = None
            current = []
    if current:
        blocks.append(("\n".join(current).strip(), start or len(lines), len(lines)))

    units: list[RewriteUnit] = []
    group: list[tuple[str, int, int]] = []

    def flush() -> None:
        if not group:
            return
        unit_index = len(units) + 1
        unit_text = "\n\n".join(item[0] for item in group)
        heading = next((item[0] for item in group if item[0].lstrip().startswith("#")), "")
        start_line = group[0][1]
        end_line = group[-1][2]
        units.append(
            RewriteUnit(
                unit_id=f"unit-{unit_index:03d}",
                heading=heading,
                text=unit_text,
                start_line=start_line,
                end_line=end_line,
                literal_invariants=extract_literal_invariants(unit_text),
                source_span_ids=[f"span-{unit_index:03d}"],
                argument_role=_guess_argument_role(unit_text),
                why_these_spans_belong_together="bounded contiguous argument unit",
            )
        )
        group.clear()

    for block in blocks:
        is_heading = block[0].lstrip().startswith("#")
        if is_heading and group:
            flush()
        group.append(block)
        paragraph_count = sum(1 for item in group if not item[0].lstrip().startswith("#"))
        char_count = sum(len(item[0]) for item in group)
        if paragraph_count >= max_paragraphs_per_unit or char_count > 2800:
            flush()
    flush()
    return units


def _guess_argument_role(text: str) -> str:
    lowered = text.lower()
    if any(token in text for token in ["下一步", "GO", "STOP", "决策", "实验"]):
        return "decision-or-next-experiment"
    if any(token in text for token in ["比较", "vs", "基线", "方法", "机制"]):
        return "comparison"
    if any(token in text for token in ["结果", "证据", "指标", "观察到"]):
        return "evidence-or-result"
    if "uncertain" in lowered or "不确定" in text:
        return "uncertainty"
    return "scientific-explanation"


def proposition_inventory(unit: RewriteUnit) -> list[dict[str, Any]]:
    chunks = [part.strip() for part in re.split(r"(?<=[。！？；;])\s*", unit.text) if part.strip()]
    if not chunks:
        chunks = [unit.text.strip()]
    props: list[dict[str, Any]] = []
    for index, chunk in enumerate(chunks, start=1):
        props.append(
            {
                "proposition_id": f"{unit.unit_id}-prop-{index:03d}",
                "kind": _guess_argument_role(chunk),
                "source_span_ids": unit.source_span_ids,
                "source_text_sha256": sha256_text(chunk),
                "required": True,
            }
        )
    return props


def verify_exact(
    source: str,
    candidate: str,
    ledger: list[dict[str, str]] | None = None,
    *,
    reader_core: str | None = None,
) -> dict[str, Any]:
    invariants = ledger if ledger is not None else extract_literal_invariants(source)
    if _contains_raw_literal_dump(candidate):
        return {
            "schema": "SCIENTIFIC_REWRITE_EXACT_VERIFICATION_V1",
            "ok": False,
            "literal_count": len(invariants),
            "missing": [],
            "missing_inline_core": [],
            "raw_literal_dump": True,
        }
    missing: list[dict[str, str]] = []
    missing_inline_core: list[dict[str, str]] = []
    core = candidate if reader_core is None else reader_core
    for item in invariants:
        literal = item["text"]
        if literal not in candidate:
            missing.append(item)
        if item.get("role") == "inline-critical" and literal not in core:
            missing_inline_core.append(item)
    return {
        "schema": "SCIENTIFIC_REWRITE_EXACT_VERIFICATION_V1",
        "ok": not missing and not missing_inline_core,
        "literal_count": len(invariants),
        "missing": missing,
        "missing_inline_core": missing_inline_core,
        "raw_literal_dump": False,
    }


def _contains_raw_literal_dump(text: str) -> bool:
    return any(re.search(pattern, text, re.I) for pattern in RAW_LITERAL_DUMP_PATTERNS)


def reader_facing_core(candidate: str) -> str:
    lines = candidate.splitlines()
    kept: list[str] = []
    in_appendix = False
    appendix_heading = re.compile(r"^\s{0,3}#{1,6}\s+.*(?:technical|trace|appendix|evidence appendix|附录|技术细节|证据附录|复现|路径|文件身份)", re.I)
    any_heading = re.compile(r"^\s{0,3}#{1,6}\s+")
    for line in lines:
        if appendix_heading.search(line):
            in_appendix = True
            continue
        if in_appendix and any_heading.search(line) and not appendix_heading.search(line):
            in_appendix = False
        if not in_appendix:
            kept.append(line)
    return "\n".join(kept)


def reader_review_packet(candidate: str, audience: str) -> dict[str, Any]:
    return {
        "schema": "SCIENTIFIC_REWRITE_CANDIDATE_ONLY_READER_PACKET_V1",
        "source_visible": False,
        "audience": audience,
        "candidate_text": candidate,
        "reader_questions": [
            "What question is this passage trying to answer?",
            "What evidence is already available?",
            "What remains uncertain?",
            "What comparison or experiment resolves it?",
            "What result means GO or STOP?",
        ],
    }


def normalize_reader_review(raw: dict[str, Any], unit_ids: set[str] | None = None) -> dict[str, Any]:
    findings = raw.get("findings") or []
    questions = []
    for item in raw.get("questions") or []:
        answerable = item.get("answerable")
        if isinstance(answerable, str):
            answerable = answerable.strip().lower() in {"true", "yes", "pass", "answerable"}
        questions.append(
            {
                "answerable": bool(answerable),
                "inferred_answer": item.get("inferred_answer") or "未明确回答。",
            }
        )
    if unit_ids is not None:
        for finding in findings:
            unit_id = finding.get("unit_id")
            if unit_id and unit_id not in unit_ids:
                raise RuntimeError(f"reader finding references unknown unit: {unit_id}")
    decision = "PASS" if str(raw.get("decision", "")).upper() == "PASS" and not findings and all(q["answerable"] for q in questions) else "REVISE"
    return {"decision": decision, "questions": questions, "findings": findings}


def normalize_meaning_card(raw: dict[str, Any], unit: RewriteUnit, propositions: list[dict[str, Any]]) -> dict[str, Any]:
    if raw.get("unit_id") != unit.unit_id:
        raise RuntimeError("meaning-card unit_id mismatch")
    if _contains_forbidden_source_copy_key(raw):
        raise RuntimeError("meaning-card contains forbidden source-copy field")
    for key in ["reader_job", "plain_meaning", "reader_takeaway", "rewrite_problem", "discourse_function"]:
        if not str(raw.get(key, "")).strip():
            raise RuntimeError(f"meaning-card missing required field: {key}")
        if _looks_like_source_copy(str(raw.get(key, "")), unit.text):
            raise RuntimeError(f"meaning-card {key} looks like copied source prose")
    valid_props = {item["proposition_id"] for item in propositions}
    covered: set[str] = set()
    for field in SEMANTIC_FIELDS:
        for item in raw.get(field, []):
            meaning = str(item.get("normalized_meaning", "")).strip()
            if not meaning:
                raise RuntimeError("meaning-card semantic item missing normalized_meaning")
            if _looks_like_source_copy(meaning, unit.text):
                raise RuntimeError("meaning-card semantic item looks like copied source prose")
            evidence_class = str(item.get("evidence_class", "")).strip()
            if evidence_class not in EVIDENCE_CLASSES:
                raise RuntimeError(f"meaning-card semantic item has invalid evidence_class: {evidence_class}")
            prop_ids = item.get("source_proposition_ids")
            if not prop_ids:
                raise RuntimeError("meaning-card semantic item missing source_proposition_ids")
            for prop_id in prop_ids:
                if prop_id not in valid_props:
                    raise RuntimeError(f"meaning-card references unknown proposition: {prop_id}")
                covered.add(prop_id)
    missing = sorted(valid_props - covered)
    if missing:
        raise RuntimeError("meaning-card omitted source propositions: " + ", ".join(missing))
    return raw


def _contains_forbidden_source_copy_key(value: Any) -> bool:
    if isinstance(value, dict):
        for key, item in value.items():
            if str(key) in {"source_excerpt", "source_text", "original_excerpt", "copied_source_excerpt"}:
                return True
            if _contains_forbidden_source_copy_key(item):
                return True
    if isinstance(value, list):
        return any(_contains_forbidden_source_copy_key(item) for item in value)
    return False


def _looks_like_source_copy(value: str, source: str) -> bool:
    normalized_value = re.sub(r"\s+", "", value)
    normalized_source = re.sub(r"\s+", "", source)
    return len(normalized_value) >= 24 and normalized_value in normalized_source


def normalize_semantic_audit(raw: dict[str, Any], unit: RewriteUnit, propositions: list[dict[str, Any]]) -> dict[str, Any]:
    aliases = {"missing": "omitted", "partially-preserved": "narrowed", "changed": "broadened"}
    allowed = {"preserved", "narrowed", "broadened", "reversed", "invented", "omitted", "reattributed"}
    prop_ids = {item["proposition_id"] for item in propositions}
    findings = []
    critical = 0
    for finding in raw.get("findings", []):
        status = aliases.get(str(finding.get("status")), str(finding.get("status")))
        if status not in allowed:
            raise RuntimeError(f"semantic audit status is invalid: {status}")
        prop_id = finding.get("proposition_id")
        if prop_id and prop_id not in prop_ids:
            raise RuntimeError(f"semantic audit references unknown proposition: {prop_id}")
        normalized = dict(finding)
        normalized["status"] = status
        if normalized.get("severity") == "critical":
            critical += 1
        findings.append(normalized)
    decision = "PASS" if str(raw.get("decision", "")).upper() == "PASS" and critical == 0 and not findings else "REVISE"
    return {"decision": decision, "findings": findings, "critical_violation_count": critical}


def validate_dataflow(receipt: dict[str, Any]) -> dict[str, Any]:
    records = receipt.get("stage_records", [])
    stage_ids = {item.get("stage_id") for item in records}
    unused = [item.get("stage_id") for item in records if item.get("unused_output")]
    dangling: list[dict[str, str]] = []
    for item in records:
        for consumer in item.get("downstream_consumers", []):
            if consumer.get("stage_id") not in stage_ids:
                dangling.append({"from": item.get("stage_id", ""), "to": consumer.get("stage_id", "")})
    return {"ok": not unused and not dangling, "unused_outputs": unused, "dangling_consumers": dangling}


def validate_argument_coverage(source: str, units: list[dict[str, Any]]) -> dict[str, Any]:
    expected_spans = [span for unit in split_markdown_units(source) for span in unit.source_span_ids]
    owners: dict[str, list[str]] = {}
    for unit in units:
        unit_id = str(unit.get("unit_id"))
        source_span_ids = unit.get("source_span_ids") or []
        if not source_span_ids:
            raise RuntimeError(f"argument unit missing source_span_ids: {unit_id}")
        for span_id in source_span_ids:
            owners.setdefault(str(span_id), []).append(unit_id)
    missing = sorted(set(expected_spans) - set(owners))
    unknown = sorted(set(owners) - set(expected_spans))
    duplicates = {span_id: unit_ids for span_id, unit_ids in owners.items() if len(unit_ids) > 1}
    if missing:
        raise RuntimeError("argument plan omitted source spans: " + ", ".join(missing))
    if unknown:
        raise RuntimeError("argument plan references unknown source spans: " + ", ".join(unknown))
    if duplicates:
        raise RuntimeError("argument plan duplicates source spans: " + ", ".join(sorted(duplicates)))
    return {"ok": True, "source_span_count": len(expected_spans), "unit_count": len(units)}


def validate_global_assembly(self_audit: dict[str, Any], unit_ids: set[str]) -> dict[str, Any]:
    assembly = self_audit.get("global_assembly")
    if not isinstance(assembly, dict):
        raise RuntimeError("self_audit missing global_assembly evidence")
    reader_order = [str(item) for item in assembly.get("reader_order_unit_ids", [])]
    if set(reader_order) != unit_ids or len(reader_order) != len(unit_ids):
        raise RuntimeError("global_assembly reader_order_unit_ids must cover every unit exactly once")
    strategy = str(assembly.get("strategy", "")).strip()
    if not strategy:
        raise RuntimeError("global_assembly missing strategy")
    return {
        "ok": True,
        "reader_order_unit_ids": reader_order,
        "reordered_from_source_order": reader_order != sorted(unit_ids),
        "strategy": strategy,
    }


def validate_host_stage_package(source: str, stage_dir: Path, *, candidate_path: Path | None = None) -> dict[str, Any]:
    required_files = [
        "document_map.json",
        "argument_units.json",
        "fidelity_ledger.json",
        "selected_transformations.json",
        "self_audit.json",
        "final_candidate.md",
    ]
    missing_files = [name for name in required_files if not (stage_dir / name).is_file()]
    if missing_files:
        raise RuntimeError("missing host stage files: " + ", ".join(missing_files))

    document_map_path = stage_dir / "document_map.json"
    argument_units_path = stage_dir / "argument_units.json"
    selected_transformations_path = stage_dir / "selected_transformations.json"
    self_audit_path = stage_dir / "self_audit.json"
    final_candidate_path = stage_dir / "final_candidate.md"

    document_map = load_json(document_map_path)
    argument_units = load_json(stage_dir / "argument_units.json")
    fidelity_ledger = load_json(stage_dir / "fidelity_ledger.json")
    selected_transformations = load_json(stage_dir / "selected_transformations.json")
    self_audit = load_json(stage_dir / "self_audit.json")
    final_candidate = final_candidate_path.read_text(encoding="utf-8")
    if candidate_path is not None and final_candidate != candidate_path.read_text(encoding="utf-8"):
        raise RuntimeError("candidate path does not match stage final_candidate.md")

    source_sha = sha256_text(source)
    if document_map.get("source_sha256") and document_map["source_sha256"] != source_sha:
        raise RuntimeError("document_map source_sha256 does not match source")
    units = argument_units.get("units", [])
    if not units:
        raise RuntimeError("argument_units.json must contain at least one unit")
    unit_ids = {str(unit.get("unit_id")) for unit in units}
    argument_coverage = validate_argument_coverage(source, units)
    selected_by_unit = selected_transformations.get("by_unit", {})
    audit_units = {str(item.get("unit_id")): item for item in self_audit.get("unit_audits", [])}
    document_map_sha = sha256_bytes(document_map_path.read_bytes())
    candidate_unit_shas: dict[str, str] = {}
    mechanical_units = {unit.unit_id: unit for unit in split_markdown_units(source)}
    for unit in units:
        unit_id = str(unit.get("unit_id"))
        if not unit_id or unit_id == "None":
            raise RuntimeError("argument unit missing unit_id")
        unit_source_sha = str(unit.get("source_unit_sha256", ""))
        if not unit_source_sha:
            raise RuntimeError(f"argument unit missing source_unit_sha256: {unit_id}")
        card_path = stage_dir / "meaning_cards" / f"{unit_id}.json"
        candidate_unit_path = stage_dir / "candidate_units" / f"{unit_id}.md"
        if not card_path.is_file():
            raise RuntimeError(f"missing meaning card for {unit_id}")
        if not candidate_unit_path.is_file():
            raise RuntimeError(f"missing candidate unit for {unit_id}")
        card = load_json(card_path)
        if card.get("unit_id") != unit_id:
            raise RuntimeError(f"meaning card unit_id mismatch for {unit_id}")
        if card.get("source_unit_sha256") != unit_source_sha:
            raise RuntimeError(f"meaning card source hash mismatch for {unit_id}")
        if card.get("document_map_sha256") != document_map_sha:
            raise RuntimeError(f"meaning card does not bind current document map for {unit_id}")
        if unit_id in mechanical_units:
            normalize_meaning_card(card, mechanical_units[unit_id], proposition_inventory(mechanical_units[unit_id]))
        if unit_id not in selected_by_unit:
            raise RuntimeError(f"selected transformations missing unit: {unit_id}")
        candidate_unit_shas[unit_id] = sha256_bytes(candidate_unit_path.read_bytes())
        audit = audit_units.get(unit_id)
        if not audit:
            raise RuntimeError(f"self_audit missing unit audit: {unit_id}")
        if audit.get("candidate_unit_sha256") != candidate_unit_shas[unit_id]:
            raise RuntimeError(f"self_audit candidate hash mismatch for {unit_id}")
        if str(audit.get("decision", "")).upper() != "PASS":
            raise RuntimeError(f"host semantic self-audit unresolved for {unit_id}")
    if str(self_audit.get("decision", "")).upper() not in {"PASS", "REVISE"}:
        raise RuntimeError("self_audit decision must be PASS or REVISE")
    if str(self_audit.get("decision", "")).upper() != "PASS":
        raise RuntimeError("host semantic self-audit has unresolved findings")
    if self_audit.get("final_candidate_sha256") != sha256_text(final_candidate):
        raise RuntimeError("self_audit final_candidate_sha256 mismatch")
    global_assembly = validate_global_assembly(self_audit, unit_ids)

    exact = verify_exact(source, final_candidate, fidelity_ledger.get("literal_invariants"), reader_core=reader_facing_core(final_candidate))
    stage_records = _stage_records(stage_dir, document_map, units, selected_transformations, self_audit, final_candidate)
    receipt = {
        "schema": RUNTIME_SCHEMA,
        "runtime": RUNTIME_NAME,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "driver": "host-codex",
        "model_call_count": 0,
        "external_api_call_count": 0,
        "requires_openai_api_key": False,
        "whole_document_writer_call": False,
        "source_sha256": source_sha,
        "candidate_sha256": sha256_text(final_candidate),
        "unit_count": len(units),
        "stage_count": len(stage_records),
        "argument_coverage": argument_coverage,
        "global_assembly": global_assembly,
        "stage_records": stage_records,
        "exact_verification": exact,
        "private_plaintext_committed": False,
    }
    receipt["dataflow_validation"] = validate_dataflow(receipt)
    if not receipt["dataflow_validation"]["ok"]:
        raise RuntimeError("host stage dataflow validation failed")
    if not exact["ok"]:
        raise RuntimeError("exact verification failed")
    return {"candidate": final_candidate, "receipt": receipt}


def _stage_records(
    stage_dir: Path,
    document_map: dict[str, Any],
    units: list[dict[str, Any]],
    selected_transformations: dict[str, Any],
    self_audit: dict[str, Any],
    final_candidate: str,
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    records.append(_record("document-map", stage_dir / "document_map.json", ["argument-segmentation"]))
    records.append(_record("argument-segmentation", stage_dir / "argument_units.json", [f"{unit['unit_id']}-meaning-card" for unit in units]))
    for unit in units:
        unit_id = str(unit["unit_id"])
        records.append(_record(f"{unit_id}-meaning-card", stage_dir / "meaning_cards" / f"{unit_id}.json", [f"{unit_id}-example-selection", f"{unit_id}-writer"]))
        records.append(_record(f"{unit_id}-example-selection", stage_dir / "selected_transformations.json", [f"{unit_id}-writer"], unit_id=unit_id))
        records.append(_record(f"{unit_id}-writer", stage_dir / "candidate_units" / f"{unit_id}.md", [f"{unit_id}-semantic-self-audit"], unit_id=unit_id))
        records.append(_record(f"{unit_id}-semantic-self-audit", stage_dir / "self_audit.json", ["final-assembly"], unit_id=unit_id))
    records.append(_record("final-assembly", stage_dir / "final_candidate.md", [], terminal=True))
    return records


def _record(stage_id: str, path: Path, consumers: list[str], *, unit_id: str | None = None, terminal: bool = False) -> dict[str, Any]:
    data = path.read_bytes()
    return {
        "stage_id": stage_id,
        "unit_id": unit_id,
        "output_identity": f"{stage_id}:{sha256_bytes(data)}",
        "output_sha256": sha256_bytes(data),
        "downstream_consumers": [{"stage_id": item, "input_binding": stage_id} for item in consumers],
        "model_call": False,
        "host_codex_authored": True,
        "plaintext_committed": False,
        "terminal_output": terminal,
        "unused_output": False,
    }


def run_multistage(*_args: Any, **_kwargs: Any) -> dict[str, Any]:
    raise RuntimeError("050 host-Codex route does not let the helper generate reader-facing prose; use validate_host_stage_package")


def response_schema_name(stage: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_-]+", "_", stage).strip("_")
    digest = sha256_text(stage)[:10]
    return (safe[:50].rstrip("_") + "_" + digest)[:64]


def command_select_examples(args: argparse.Namespace) -> None:
    selected = select_examples(
        load_seed_library(),
        limit=args.limit,
        scene=args.scene,
        discourse_function=args.discourse_function,
        rewrite_problem=args.rewrite_problem,
        fidelity_risk=args.fidelity_risk,
        register=args.register,
    )
    print(json.dumps(selected, ensure_ascii=False, indent=2, sort_keys=True))


def command_verify_exact(args: argparse.Namespace) -> None:
    source = Path(args.source).read_text(encoding="utf-8")
    candidate = Path(args.candidate).read_text(encoding="utf-8")
    report = verify_exact(source, candidate)
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    if not report["ok"]:
        raise SystemExit(1)


def command_validate_host_stage(args: argparse.Namespace) -> None:
    source = Path(args.source).read_text(encoding="utf-8")
    result = validate_host_stage_package(source, Path(args.stage_dir), candidate_path=Path(args.candidate) if args.candidate else None)
    if args.receipt:
        write_json(Path(args.receipt), result["receipt"])
    print(json.dumps(result["receipt"], ensure_ascii=False, indent=2, sort_keys=True))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    select = sub.add_parser("select-examples")
    select.add_argument("--limit", type=int, default=4)
    select.add_argument("--scene", default="")
    select.add_argument("--discourse-function", default="")
    select.add_argument("--rewrite-problem", default="")
    select.add_argument("--fidelity-risk", default="")
    select.add_argument("--register", default="")
    select.set_defaults(func=command_select_examples)

    verify = sub.add_parser("verify-exact")
    verify.add_argument("--source", required=True)
    verify.add_argument("--candidate", required=True)
    verify.set_defaults(func=command_verify_exact)

    validate = sub.add_parser("validate-host-stage")
    validate.add_argument("--source", required=True)
    validate.add_argument("--stage-dir", required=True)
    validate.add_argument("--candidate")
    validate.add_argument("--receipt")
    validate.set_defaults(func=command_validate_host_stage)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
