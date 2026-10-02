import unittest
from pathlib import Path

from scripts.audit_maintenance_board_issue_metadata import audit_issues, collect_tracking_map


def issue(number=1, labels=None, state="OPEN", state_reason=None, status="TODO", area="web-development", resolution=""):
    return {
        "number": number,
        "title": f"Issue {number}",
        "state": state,
        "stateReason": state_reason,
        "labels": labels or ["maintenance-track", "kind:enhancement", "scope:plugin", "area:web-development"],
        "project": {"Status": status, "Area": area, "Resolution commit": resolution},
    }


class MaintenanceBoardIssueMetadataAuditTests(unittest.TestCase):
    def test_valid_plugin_issue_passes(self):
        result = audit_issues([issue()], {1: [{"source": "docs/plugin-todos/web-development.md"}]})
        self.assertTrue(result["ok"], result["violations"])

    def test_missing_kind_fails(self):
        result = audit_issues([issue(labels=["maintenance-track", "scope:plugin", "area:web-development"])], {1: [{"source": "docs/plugin-todos/web-development.md"}]})
        self.assertFalse(result["ok"])
        self.assertEqual(result["violations"][0]["code"], "kind-count")

    def test_multiple_kind_fails(self):
        labels = ["maintenance-track", "kind:enhancement", "kind:regression", "scope:plugin", "area:web-development"]
        result = audit_issues([issue(labels=labels)], {1: [{"source": "docs/plugin-todos/web-development.md"}]})
        self.assertIn("kind-count", {v["code"] for v in result["violations"]})

    def test_area_mismatch_fails(self):
        result = audit_issues([issue(labels=["maintenance-track", "kind:enhancement", "scope:plugin", "area:presentations"])], {1: [{"source": "docs/plugin-todos/web-development.md"}]})
        self.assertIn("area-mismatch", {v["code"] for v in result["violations"]})

    def test_triage_and_lifecycle_labels_fail(self):
        labels = ["maintenance-track", "triage:needed", "status:todo", "kind:enhancement", "scope:plugin", "area:web-development"]
        result = audit_issues([issue(labels=labels)], {1: [{"source": "docs/plugin-todos/web-development.md"}]})
        self.assertIn("triage-leak", {v["code"] for v in result["violations"]})
        self.assertIn("lifecycle-label", {v["code"] for v in result["violations"]})

    def test_completed_close_requires_done_and_resolution_commit(self):
        result = audit_issues([issue(state="CLOSED", state_reason="COMPLETED", status="TODO")], {1: [{"source": "docs/plugin-todos/web-development.md"}]})
        codes = {v["code"] for v in result["violations"]}
        self.assertIn("completed-not-done", codes)
        self.assertIn("completed-missing-resolution", codes)

    def test_non_completion_close_must_not_be_done(self):
        result = audit_issues([issue(state="CLOSED", state_reason="NOT_PLANNED", status="DONE", resolution="abc123")], {1: [{"source": "docs/plugin-todos/web-development.md"}]})
        self.assertIn("not-planned-false-done", {v["code"] for v in result["violations"]})

    def test_plugin_issue_requires_source_backlink(self):
        result = audit_issues([issue()], {})
        self.assertIn("missing-source-backlink", {v["code"] for v in result["violations"]})

    def test_cross_repo_non_todo_backed_issue_can_pass(self):
        labels = ["maintenance-track", "kind:governance", "scope:cross-repo", "area:workflow-core", "integration:bridge-kit"]
        result = audit_issues([issue(labels=labels, area="workflow-core")], {})
        self.assertTrue(result["ok"], result["violations"])

    def test_collect_tracking_map_reads_plugin_and_skill_todos(self):
        root = Path(self.id()).parent if False else None
        self.assertIsNotNone(collect_tracking_map(Path.cwd()))


class MaintenanceBoardStaticContractTests(unittest.TestCase):
    def test_issue_forms_do_not_target_project_or_maintenance_track(self):
        for rel in [
            ".github/ISSUE_TEMPLATE/existing_capability_failure.yml",
            ".github/ISSUE_TEMPLATE/new_capability.yml",
        ]:
            text = Path(rel).read_text(encoding="utf-8")
            self.assertNotIn("projects:", text)
            self.assertNotIn("maintenance-track", text)
        self.assertIn("kind:new-capability", Path(".github/ISSUE_TEMPLATE/new_capability.yml").read_text(encoding="utf-8"))

    def test_issue_template_config_keeps_blank_route(self):
        text = Path(".github/ISSUE_TEMPLATE/config.yml").read_text(encoding="utf-8")
        self.assertEqual(text.strip(), "blank_issues_enabled: true\ncontact_links: []")

    def test_intake_action_is_bounded(self):
        text = Path(".github/workflows/maintenance-board-intake.yml").read_text(encoding="utf-8")
        self.assertIn("issues:\n    types: [opened]", text)
        self.assertIn("permissions:\n  issues: write", text)
        self.assertNotIn("actions/checkout", text)
        self.assertNotIn("secrets.", text)
        self.assertNotIn("maintenance-track\"\n                  \"--add-label", text)
        self.assertIn("--add-label", text)
        self.assertIn("triage:needed", text)


if __name__ == "__main__":
    unittest.main()
