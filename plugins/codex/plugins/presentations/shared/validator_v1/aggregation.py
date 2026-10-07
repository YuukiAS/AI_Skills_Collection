"""Page-level aggregation for deterministic and rendered findings."""

from __future__ import annotations

from typing import Any


def aggregate_page_result(packet: dict[str, Any], review_row: dict[str, Any], deterministic_findings: list[dict[str, Any]]) -> dict[str, Any]:
    issue_classes = sorted(
        {
            *(review_row.get("issue_classes") or []),
            *(
                f.get("finding_class")
                for f in deterministic_findings
                if f.get("status") == "REVISE" and f.get("finding_class") and f.get("deterministic_role") == "HARD_FAIL"
            ),
        }
    )
    verdict = "REVISE" if issue_classes or review_row.get("overall_visual_verdict") != "PASS" else "PASS"
    positive = list(review_row.get("positive_visible_evidence") or [])
    pass_fallthrough = int(verdict == "PASS" and not positive)
    if pass_fallthrough:
        verdict = "REVISE"
        issue_classes.append("PASS_FALLTHROUGH")
    return {
        "artifact_id": packet["artifact_id"],
        "physical_page": packet["physical_page"],
        "page_png_sha256": packet["page_png_sha256"],
        "stable_targets": packet.get("stable_targets", []),
        "component_targets": packet.get("component_targets", []),
        "applicable_guard_ids": [g.get("guard_id") for g in packet.get("guards", [])],
        "verdict": verdict,
        "issue_classes": sorted(set(issue_classes)),
        "positive_visible_evidence": positive,
        "negative_visible_evidence": list(review_row.get("negative_visible_evidence") or []),
        "substantive_observation": review_row.get("substantive_observation", ""),
        "pass_fallthrough": pass_fallthrough,
    }
