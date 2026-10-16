#!/usr/bin/env python3
"""Completion gate for existing research deck revisions."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import deck_quality_loop


SCHEMA = "RESEARCH_PRESENTATION_EXISTING_DECK_REVISION_PACKET_V1"
SUMMARY_SCHEMA = "RESEARCH_PRESENTATION_EXISTING_DECK_REVISION_GATE_V1"
REPO_ROOT = Path(__file__).resolve().parents[6]
PASS_STATUSES = {"PASS", "OK", "COMPLETED", "NOT_APPLICABLE"}
ISSUE_STATUSES = {"REVISE", "BLOCKED", "FAIL", "MISSING", "UNKNOWN"}
REQUIRED_ENTRY_FIELDS = {
    "reviewer_seen_baseline",
    "accepted_element_ledger",
    "targeted_feedback",
    "rerender",
    "high_resolution_problem_pages",
}
RENDERED_QA_CHECKS = {
    "node_width_and_wrap",
    "connector_endpoint_clearance",
    "arrow_readability",
    "crowding_unused_space",
    "figure_internal_text",
    "caption_panel_pairing",
    "source_footer_safe_zone",
}
FIRST_USE_TYPES = {"method", "acronym", "dataset", "domain_term", "estimand"}


class GateError(RuntimeError):
    """Raised for invalid packet input."""


def _read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise GateError(f"missing revision packet: {path}") from exc
    except json.JSONDecodeError as exc:
        raise GateError(f"invalid JSON in revision packet: {exc}") from exc
    if not isinstance(data, dict):
        raise GateError("revision packet must be a JSON object")
    return data


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def _status(value: Any) -> str:
    return str(value or "").strip().upper()


def _truthy(value: Any) -> bool:
    return value is True or str(value).strip().lower() in {"true", "yes", "1", "pass", "completed"}


def _add(findings: list[dict[str, Any]], *, gate: str, decision: str, finding_id: str, summary: str, evidence: Any = None) -> None:
    finding: dict[str, Any] = {
        "gate": gate,
        "decision": decision,
        "finding_id": finding_id,
        "summary": summary,
    }
    if evidence is not None:
        finding["evidence"] = evidence
    findings.append(finding)


def _field_present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, (list, dict, str)):
        return bool(value)
    return True


def _artifact_path(root: Path, value: Any) -> Path | None:
    if not isinstance(value, str) or not value.strip():
        return None
    path = Path(value)
    return path if path.is_absolute() else root / path


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _check_file_binding(
    record: dict[str, Any],
    *,
    root: Path,
    gate: str,
    finding_prefix: str,
    findings: list[dict[str, Any]],
) -> Path | None:
    path = _artifact_path(root, record.get("path"))
    expected = str(record.get("sha256") or "").lower()
    if path is None or not path.is_file():
        _add(findings, gate=gate, decision="BLOCKED", finding_id=f"{finding_prefix}_missing", summary=f"bound artifact does not exist: {record.get('path')}")
        return None
    if len(expected) != 64 or _file_sha256(path) != expected:
        _add(findings, gate=gate, decision="BLOCKED", finding_id=f"{finding_prefix}_sha256_mismatch", summary=f"bound artifact hash is missing or stale: {record.get('path')}")
        return None
    return path


def _check_artifact_identity(packet: dict[str, Any], findings: list[dict[str, Any]], root: Path) -> None:
    identity = packet.get("deck_identity") or {}
    if not isinstance(identity, dict):
        _add(findings, gate="exact_artifact_identity", decision="BLOCKED", finding_id="deck_identity_invalid", summary="deck_identity must be an object")
        return
    candidate = str(identity.get("candidate_commit") or "")
    if not candidate:
        _add(findings, gate="exact_artifact_identity", decision="BLOCKED", finding_id="candidate_commit_missing", summary="exact candidate commit is required")
    source = _check_file_binding(
        {"path": identity.get("source_path"), "sha256": identity.get("source_sha256")},
        root=root, gate="exact_artifact_identity", finding_prefix="source", findings=findings,
    )
    pdf = _check_file_binding(
        {"path": identity.get("pdf_path"), "sha256": identity.get("pdf_sha256")},
        root=root, gate="exact_artifact_identity", finding_prefix="final_pdf", findings=findings,
    )
    page_images = identity.get("page_images") or []
    page_count = identity.get("page_count")
    if not isinstance(page_images, list) or not page_images or page_count != len(page_images):
        _add(findings, gate="exact_artifact_identity", decision="BLOCKED", finding_id="page_image_set_incomplete", summary="page_images must bind every rendered page and match page_count")
    else:
        expected_pages = list(range(1, len(page_images) + 1))
        actual_pages = [row.get("page") for row in page_images if isinstance(row, dict)]
        if actual_pages != expected_pages:
            _add(findings, gate="exact_artifact_identity", decision="BLOCKED", finding_id="page_image_order_invalid", summary="page_images must contain one ordered row for every page")
        for row in page_images:
            if isinstance(row, dict):
                _check_file_binding(row, root=root, gate="exact_artifact_identity", finding_prefix=f"page_{row.get('page')}", findings=findings)
    contact = identity.get("contact_sheet") or {}
    if not isinstance(contact, dict):
        contact = {}
    _check_file_binding(contact, root=root, gate="exact_artifact_identity", finding_prefix="contact_sheet", findings=findings)

    revision = packet.get("revision_entry") or packet.get("revision_context") or {}
    if isinstance(revision, dict):
        baseline = revision.get("reviewer_seen_baseline") or {}
        rerender = revision.get("rerender") or {}
        if isinstance(baseline, dict):
            _check_file_binding(baseline, root=root, gate="exact_artifact_identity", finding_prefix="reviewer_seen_baseline", findings=findings)
        if isinstance(rerender, dict):
            rendered_path = _check_file_binding(rerender, root=root, gate="exact_artifact_identity", finding_prefix="rerender", findings=findings)
            if rendered_path and pdf and rendered_path.resolve() != pdf.resolve():
                _add(findings, gate="exact_artifact_identity", decision="BLOCKED", finding_id="rerender_final_pdf_mismatch", summary="rerender evidence must bind the exact final PDF")

    review = packet.get("independent_visual_review") or packet.get("visual_review") or {}
    if not isinstance(review, dict):
        return
    if str(review.get("candidate_commit") or "") != candidate:
        _add(findings, gate="independent_visual_review", decision="BLOCKED", finding_id="review_candidate_stale", summary="independent review is not bound to the exact candidate commit")
    if str(review.get("artifact_sha256") or "").lower() != str(identity.get("pdf_sha256") or "").lower():
        _add(findings, gate="independent_visual_review", decision="BLOCKED", finding_id="review_artifact_stale", summary="independent review is not bound to the exact final PDF")
    trace = {"path": review.get("reviewer_trace_path"), "sha256": review.get("reviewer_trace_sha256")}
    _check_file_binding(trace, root=root, gate="independent_visual_review", finding_prefix="reviewer_trace", findings=findings)
    if not review.get("reviewer_run_id"):
        _add(findings, gate="independent_visual_review", decision="BLOCKED", finding_id="reviewer_run_id_missing", summary="independent review requires a durable reviewer run identity")
    rows = review.get("page_reviews") or []
    if not isinstance(rows, list) or len(rows) != len(page_images):
        _add(findings, gate="independent_visual_review", decision="BLOCKED", finding_id="page_review_rows_incomplete", summary="independent review must contain one row for every rendered page")
    else:
        image_hashes = {row.get("page"): row.get("sha256") for row in page_images if isinstance(row, dict)}
        for index, row in enumerate(rows, start=1):
            if not isinstance(row, dict) or row.get("page") != index or row.get("image_sha256") != image_hashes.get(index) or _status(row.get("decision")) != "PASS":
                _add(findings, gate="independent_visual_review", decision="BLOCKED", finding_id=f"page_review_{index}_invalid", summary="page review row is missing, stale, or not PASS")
    contact_review = review.get("contact_sheet_review") or {}
    if not isinstance(contact_review, dict) or contact_review.get("sha256") != contact.get("sha256") or _status(contact_review.get("decision")) != "PASS":
        _add(findings, gate="independent_visual_review", decision="BLOCKED", finding_id="contact_sheet_review_invalid", summary="contact-sheet review is missing, stale, or not PASS")


def _check_entry_packet(packet: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    revision = packet.get("revision_entry") or packet.get("revision_context") or {}
    if not isinstance(revision, dict):
        _add(
            findings,
            gate="existing_deck_revision_entry",
            decision="BLOCKED",
            finding_id="revision_entry_invalid",
            summary="revision entry context must be an object",
        )
        return

    for field in sorted(REQUIRED_ENTRY_FIELDS):
        if not _field_present(revision.get(field)):
            _add(
                findings,
                gate="existing_deck_revision_entry",
                decision="BLOCKED",
                finding_id=f"missing_{field}",
                summary=f"existing-deck revision packet is missing {field}",
            )

    rerender = revision.get("rerender") if isinstance(revision.get("rerender"), dict) else {}
    if rerender and _status(rerender.get("status")) not in PASS_STATUSES:
        _add(
            findings,
            gate="existing_deck_revision_entry",
            decision="BLOCKED",
            finding_id="rerender_unavailable",
            summary="revised deck was not rerendered before completion",
            evidence=rerender,
        )

    accepted = revision.get("accepted_element_ledger", [])
    for item in _as_list(accepted):
        if not isinstance(item, dict):
            continue
        if _status(item.get("regression_status")) in ISSUE_STATUSES:
            _add(
                findings,
                gate="accepted_element_regression",
                decision="REVISE",
                finding_id=str(item.get("id") or item.get("element_id") or "accepted_element_regression"),
                summary="accepted slide/component changed outside the targeted revision scope",
                evidence=item,
            )


def _check_first_use(packet: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    records = packet.get("first_use_checks") or packet.get("first_use_inventory") or []
    if not isinstance(records, list):
        _add(
            findings,
            gate="first_use_dependency_order",
            decision="BLOCKED",
            finding_id="first_use_inventory_invalid",
            summary="first-use inventory must be a list",
        )
        return

    for record in records:
        if not isinstance(record, dict):
            continue
        term_type = str(record.get("type") or record.get("term_type") or "").strip().lower()
        if term_type not in FIRST_USE_TYPES:
            continue
        if record.get("central_object") is False or record.get("becomes_central_object") is False:
            continue
        status = _status(record.get("status"))
        first_page = record.get("first_central_use_page")
        explanation_page = record.get("explanation_page")
        explanation_status = _status(record.get("explanation_status") or record.get("status"))
        if status in ISSUE_STATUSES or explanation_status in ISSUE_STATUSES:
            _add(
                findings,
                gate="first_use_dependency_order",
                decision="REVISE",
                finding_id=str(record.get("id") or record.get("term") or f"{term_type}_first_use"),
                summary=f"{term_type} becomes central before adequate audience explanation",
                evidence=record,
            )
            continue
        try:
            if explanation_page is None or int(explanation_page) > int(first_page):
                _add(
                    findings,
                    gate="first_use_dependency_order",
                    decision="REVISE",
                    finding_id=str(record.get("id") or record.get("term") or f"{term_type}_first_use"),
                    summary=f"{term_type} explanation is missing or appears after first central use",
                    evidence=record,
                )
        except (TypeError, ValueError):
            _add(
                findings,
                gate="first_use_dependency_order",
                decision="BLOCKED",
                finding_id=str(record.get("id") or record.get("term") or f"{term_type}_first_use_page_invalid"),
                summary=f"{term_type} first-use pages must be numeric when the term becomes central",
                evidence=record,
            )


def _check_rendered_scientific_qa(packet: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    qa = packet.get("rendered_scientific_object_qa") or packet.get("rendered_qa_checks") or {}
    if not isinstance(qa, dict):
        _add(
            findings,
            gate="rendered_scientific_object_qa",
            decision="BLOCKED",
            finding_id="rendered_qa_invalid",
            summary="rendered scientific-object QA must be an object keyed by check id",
        )
        return

    missing = sorted(RENDERED_QA_CHECKS - set(qa))
    for check in missing:
        _add(
            findings,
            gate="rendered_scientific_object_qa",
            decision="BLOCKED",
            finding_id=f"missing_{check}",
            summary=f"rendered scientific-object QA missing {check}",
        )

    for check, record in qa.items():
        if check not in RENDERED_QA_CHECKS:
            continue
        status = _status(record.get("status") if isinstance(record, dict) else record)
        if status in ISSUE_STATUSES or status not in PASS_STATUSES:
            finding_id = check
            if isinstance(record, dict) and record.get("id"):
                finding_id = str(record["id"])
            _add(
                findings,
                gate="rendered_scientific_object_qa",
                decision="REVISE" if status != "BLOCKED" else "BLOCKED",
                finding_id=finding_id,
                summary=f"rendered scientific-object QA failed {check}",
                evidence=record,
            )


def _check_english_final_pass(packet: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    final_pass = packet.get("english_final_pass") or {}
    if not isinstance(final_pass, dict) or not final_pass:
        _add(
            findings,
            gate="english_final_pass",
            decision="BLOCKED",
            finding_id="english_final_pass_missing",
            summary="English scientific-prose final pass is missing after scientific structure/facts freeze",
        )
        return
    if not _truthy(final_pass.get("scientific_structure_frozen")):
        _add(
            findings,
            gate="english_final_pass",
            decision="BLOCKED",
            finding_id="scientific_structure_not_frozen",
            summary="English final pass cannot close before scientific structure/formula/claim/citation freeze",
            evidence=final_pass,
        )
    if _status(final_pass.get("status")) not in PASS_STATUSES or not _truthy(final_pass.get("completed_after_structure_frozen")):
        _add(
            findings,
            gate="english_final_pass",
            decision="REVISE",
            finding_id="english_final_pass_not_completed",
            summary="English scientific-prose final pass was not completed after the freeze point",
            evidence=final_pass,
        )
    if not _truthy(final_pass.get("rerender_after_pass")):
        _add(
            findings,
            gate="english_final_pass",
            decision="REVISE",
            finding_id="english_final_pass_not_rerendered",
            summary="deck was not rerendered after the English final pass",
            evidence=final_pass,
        )


def _check_independent_review(packet: dict[str, Any], findings: list[dict[str, Any]]) -> None:
    review = packet.get("independent_visual_review") or packet.get("visual_review") or {}
    if not isinstance(review, dict) or not review:
        _add(
            findings,
            gate="independent_visual_review",
            decision="BLOCKED",
            finding_id="independent_visual_review_missing",
            summary="existing-deck revision cannot self-declare final PASS without independent visual review",
        )
        return
    if review.get("independent") is not True and str(review.get("reviewer_role") or "").lower() != "independent":
        _add(
            findings,
            gate="independent_visual_review",
            decision="BLOCKED",
            finding_id="independent_visual_review_not_independent",
            summary="visual review evidence must be from an independent reviewer",
            evidence=review,
        )
    decision = _status(review.get("decision") or review.get("overall_decision"))
    if decision in {"REVISE", "BLOCKED", "FAIL"}:
        _add(
            findings,
            gate="independent_visual_review",
            decision="REVISE" if decision == "REVISE" else "BLOCKED",
            finding_id="independent_visual_review_decision",
            summary=f"independent visual reviewer returned {decision}",
            evidence=review,
        )
    elif decision != "PASS":
        _add(
            findings,
            gate="independent_visual_review",
            decision="BLOCKED",
            finding_id="independent_visual_review_decision_missing",
            summary="independent visual review must explicitly return PASS, REVISE, or BLOCKED",
            evidence=review,
        )


def evaluate(packet: dict[str, Any], *, root: Path = REPO_ROOT) -> dict[str, Any]:
    if packet.get("schema") != SCHEMA:
        raise GateError(f"revision packet schema must be {SCHEMA}")
    findings: list[dict[str, Any]] = []
    _check_artifact_identity(packet, findings, root)
    _check_entry_packet(packet, findings)
    _check_first_use(packet, findings)
    _check_rendered_scientific_qa(packet, findings)
    _check_english_final_pass(packet, findings)
    _check_independent_review(packet, findings)

    if any(finding["decision"] == "BLOCKED" for finding in findings):
        decision = "BLOCKED"
    elif findings:
        decision = "REVISE"
    else:
        decision = "PASS_REVIEWED"

    return {
        "schema": SUMMARY_SCHEMA,
        "packet_schema": packet["schema"],
        "packet_sha256": deck_quality_loop.stable_sha(packet),
        "revision_entrypoint": "research-presentations existing-deck revision production gate",
        "completion_gate": "CLOSED" if decision == "PASS_REVIEWED" else "NOT_CLOSED",
        "final_decision": decision,
        "required_gates": [
            "reviewer_seen_baseline",
            "exact_artifact_identity",
            "accepted_element_ledger",
            "targeted_feedback",
            "rerender",
            "high_resolution_problem_pages",
            "first_use_dependency_order",
            "rendered_scientific_object_qa",
            "english_final_pass_after_scientific_freeze",
            "independent_visual_review",
        ],
        "findings": findings,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision-packet", type=Path, required=True)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args(argv)

    try:
        summary = evaluate(_read_json(args.revision_packet))
    except GateError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    text = json.dumps(summary, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
    print(text, end="")
    return 0 if summary["final_decision"] == "PASS_REVIEWED" else 2


if __name__ == "__main__":
    raise SystemExit(main())
