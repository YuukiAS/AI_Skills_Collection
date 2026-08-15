from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import skill_intake_adapter as adapter  # noqa: E402


def valid_routing_contract() -> dict[str, object]:
    return {
        "should_trigger": [
            "Help me turn this public skill repo into the right local capability.",
            "Review this candidate workflow and decide whether it belongs in the skill library.",
            "Merge the useful review-writing parts into our existing paper review skill.",
            "Check whether this source should be reference-only instead of a new skill.",
            "Add the adopted behavior to the right front-door skill without duplicating triggers.",
        ],
        "should_not_trigger": [
            "Summarize this unrelated GitHub repository.",
            "Install this package into my Python environment.",
            "Create a Notion database for tracking tasks.",
        ],
        "neighbor_skills": ["skill-library-analysis", "ai-skills-repository-maintainer"],
        "front_door": "ai-skills-core / ai-skills-repository-maintainer",
        "reason": "Users ask for the task outcome, not for upstream repository names.",
    }


class SkillIntakeAdapterTests(unittest.TestCase):
    def test_notion_false_existing_partially_merged_is_already_processed(self) -> None:
        history = adapter.parse_history(REPO_ROOT / "docs/provenance/INTEGRATION_HISTORY.md")
        result = adapter.history_gate(
            adapter.Candidate(
                name="ICLR reviewer open source collection",
                source="https://github.com/Haoran-98/ICLR-reviewer",
                page_type="",
                utilized=False,
            ),
            history,
        )
        self.assertEqual(result["status"], "ALREADY_PROCESSED")
        self.assertEqual(result["decision"], "partially-merged")
        self.assertIn("skills/writing/research/peer-review", result["target"])
        registry = json.loads((REPO_ROOT / "registry.json").read_text(encoding="utf-8"))
        duplicate_skills = [
            item["name"]
            for item in registry["skills"]
            if "iclr-reviewer" in item["name"].lower() or "iclr-reviewer" in item["path"].lower()
        ]
        self.assertEqual(duplicate_skills, [])

    def test_already_rejected_candidate_is_not_reimported(self) -> None:
        history = [
            adapter.HistoryDecision(
                source="example/rejected-tool",
                decision="rejected",
                target="none",
                integration_commit="current-tree",
            )
        ]
        result = adapter.history_gate(
            adapter.Candidate(name="Rejected tool", source="https://github.com/example/rejected-tool"),
            history,
        )
        self.assertEqual(result["status"], "ALREADY_PROCESSED")
        self.assertEqual(result["decision"], "rejected")

    def test_new_overlapping_candidate_requires_merge_or_conflict_decision(self) -> None:
        errors = adapter.validate_plan(
            {
                "planner_decision": "create new skill",
                "changes_active_skill": True,
                "overlaps_existing_trigger": True,
                "routing_contract": valid_routing_contract(),
            }
        )
        self.assertIn("trigger overlap requires an explicit merge/conflict decision", errors)

    def test_new_active_skill_requires_should_trigger_examples(self) -> None:
        routing = valid_routing_contract()
        routing["should_trigger"] = []
        errors = adapter.validate_plan(
            {
                "planner_decision": "create new skill",
                "changes_active_skill": True,
                "routing_contract": routing,
            }
        )
        self.assertIn("routing_contract.should_trigger must include at least 5 examples", errors)

    def test_new_active_skill_requires_should_not_trigger_examples(self) -> None:
        routing = valid_routing_contract()
        routing["should_not_trigger"] = []
        errors = adapter.validate_plan(
            {
                "planner_decision": "create new skill",
                "changes_active_skill": True,
                "routing_contract": routing,
            }
        )
        self.assertIn("routing_contract.should_not_trigger must include at least 3 examples", errors)

    def test_new_plugin_requires_explicit_planner_decision(self) -> None:
        errors = adapter.validate_plan(
            {
                "planner_decision": "create new top-level plugin",
                "creates_top_level_plugin": True,
                "explicit_plugin_decision": False,
                "routing_contract": valid_routing_contract(),
            }
        )
        self.assertIn("new top-level plugin requires an explicit Planner decision", errors)

    def test_generated_marketplace_layer_is_not_adapter_source(self) -> None:
        doc = (REPO_ROOT / "docs/workflows/REVIEWED_HANDOFF_SKILL_INTAKE.md").read_text(encoding="utf-8")
        self.assertIn(".agents/plugins/marketplace.json", doc)
        self.assertIn("plugins/codex/plugins/", doc)
        for relative in (".agents/plugins/marketplace.json", "plugins/codex/plugins"):
            self.assertTrue((REPO_ROOT / relative).exists())

    def test_research_type_excluded_from_phase1_default_intake(self) -> None:
        self.assertFalse(
            adapter.default_phase1_candidate(
                adapter.Candidate(name="Research item", source="https://github.com/example/research", page_type="Research")
            )
        )
        self.assertTrue(
            adapter.default_phase1_candidate(
                adapter.Candidate(name="Empty type item", source="https://github.com/example/tool", page_type="")
            )
        )


if __name__ == "__main__":
    unittest.main()
