#!/usr/bin/env python3
"""AI_Skills_Collection-specific Reviewed Handoff intake checks."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from skill_utils import ROOT


DEFAULT_HISTORY = ROOT / "docs" / "provenance" / "INTEGRATION_HISTORY.md"
DEFAULT_ADAPTER = ROOT / "docs" / "workflows" / "REVIEWED_HANDOFF_SKILL_INTAKE.md"

PROCESSED_DECISIONS = {
    "merged",
    "partially-merged",
    "reference-only",
    "reviewed-not-adopted",
    "rejected",
}
ADOPTED_DECISIONS = {"merged", "partially-merged", "reference-only"}
NON_ADOPTED_DECISIONS = {"reviewed-not-adopted", "rejected", "unresolved-asset"}
PLANNER_DECISIONS = {
    "merge into existing skill",
    "partially merge into existing skill",
    "create new skill",
    "create new top-level plugin",
    "reference-only",
    "reviewed-not-adopted",
    "unresolved-asset",
    "rejected",
}
ACTIVE_CHANGE_DECISIONS = {
    "merge into existing skill",
    "partially merge into existing skill",
    "create new skill",
    "create new top-level plugin",
}


@dataclass(frozen=True)
class Candidate:
    name: str
    source: str
    page_type: str = ""
    utilized: bool = False


@dataclass(frozen=True)
class HistoryDecision:
    decision: str
    target: str
    integration_commit: str
    source: str


def normalize_source(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"^https?://", "", value)
    value = value.removesuffix(".git")
    return value.strip("/")


def parse_history(path: Path = DEFAULT_HISTORY) -> list[HistoryDecision]:
    rows: list[HistoryDecision] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or line.startswith("|---") or "source_type" in line:
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) < 9:
            continue
        rows.append(
            HistoryDecision(
                source=parts[2],
                decision=parts[5],
                target=parts[6],
                integration_commit=parts[7],
            )
        )
    return rows


def default_phase1_candidate(candidate: Candidate) -> bool:
    return (not candidate.utilized) and candidate.page_type.strip().lower() != "research"


def history_gate(candidate: Candidate, history: list[HistoryDecision]) -> dict[str, str]:
    candidate_key = normalize_source(candidate.source or candidate.name)
    for row in history:
        row_key = normalize_source(row.source)
        if candidate_key and (candidate_key in row_key or row_key in candidate_key):
            if row.decision in PROCESSED_DECISIONS:
                return {
                    "status": "ALREADY_PROCESSED",
                    "decision": row.decision,
                    "target": row.target,
                    "integration_commit": row.integration_commit,
                }
    return {"status": "NEW_CANDIDATE"}


def utilized_writeback(decision: str) -> str:
    if decision in ADOPTED_DECISIONS:
        return "Utilized=true"
    if decision in NON_ADOPTED_DECISIONS:
        return "do-not-set-utilized-true"
    raise ValueError(f"unknown decision: {decision}")


def _list_values(plan: dict[str, object], key: str) -> list[str]:
    value = plan.get(key)
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    return []


def validate_plan(plan: dict[str, object]) -> list[str]:
    errors: list[str] = []
    decision = str(plan.get("planner_decision", "")).strip()
    if decision not in PLANNER_DECISIONS:
        errors.append("planner_decision must use the AI Skills intake decision taxonomy")

    changes_active_skill = bool(plan.get("changes_active_skill"))
    changes_plugin_exposure = bool(plan.get("changes_plugin_exposure"))
    creates_plugin = decision == "create new top-level plugin" or bool(plan.get("creates_top_level_plugin"))

    if creates_plugin and not bool(plan.get("explicit_plugin_decision")):
        errors.append("new top-level plugin requires an explicit Planner decision")

    if (changes_active_skill or changes_plugin_exposure or decision in ACTIVE_CHANGE_DECISIONS) and not bool(
        plan.get("routing_contract")
    ):
        errors.append("active skill or plugin exposure changes require a routing_contract")

    routing = plan.get("routing_contract")
    if isinstance(routing, dict):
        if len(_list_values(routing, "should_trigger")) < 5:
            errors.append("routing_contract.should_trigger must include at least 5 examples")
        if len(_list_values(routing, "should_not_trigger")) < 3:
            errors.append("routing_contract.should_not_trigger must include at least 3 examples")
        for key in ("neighbor_skills", "front_door", "reason"):
            if not routing.get(key):
                errors.append(f"routing_contract.{key} is required")

    if bool(plan.get("overlaps_existing_trigger")) and decision not in {
        "merge into existing skill",
        "partially merge into existing skill",
        "reference-only",
        "reviewed-not-adopted",
        "unresolved-asset",
        "rejected",
    }:
        errors.append("trigger overlap requires an explicit merge/conflict decision")

    return errors


def audit_generated_only(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative in (".agents/plugins/marketplace.json", "plugins/codex/plugins"):
        path = root / relative
        if path.exists():
            errors.append(f"{relative} exists and remains generated-only; do not hand-edit for intake policy")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", default=str(DEFAULT_HISTORY))
    parser.add_argument("--check-adapter-doc", action="store_true")
    args = parser.parse_args()

    history = parse_history(Path(args.history))
    print(f"history decisions loaded: {len(history)}")
    if args.check_adapter_doc and not DEFAULT_ADAPTER.exists():
        print(f"ERROR: missing adapter doc: {DEFAULT_ADAPTER.relative_to(ROOT).as_posix()}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
