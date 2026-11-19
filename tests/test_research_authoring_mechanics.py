from __future__ import annotations

import hashlib
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills/writing/research"
SCRIPT = SOURCE / "shared/scripts/check_research_artifact.py"
spec = importlib.util.spec_from_file_location("research_artifact", SCRIPT)
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)
NEW = ("research-notes", "research-story", "student-materials")


class ResearchArtifactChecks(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.root / "source.md"
        self.source.write_text("# Fixture\n\nx = 1\n", encoding="utf-8")
        self.target = self.root / "target.md"
        self.target.write_bytes(self.source.read_bytes())
        self.readback = self.root / "readback.md"
        self.readback.write_bytes(self.target.read_bytes())
        self.handoff = {
            "candidate_identity": {"source": {"path": "source.md", "sha256": adapter.sha256(self.source)}},
            "delivery_targets": [{"path": "target.md", "sha256": adapter.sha256(self.target), "readback": "readback.md"}],
        }

    def check(self, **kwargs):
        handoff = self.root / "handoff.json"
        handoff.write_text(json.dumps(self.handoff), encoding="utf-8")
        return adapter.check(handoff, **kwargs)

    def statuses(self, result, name):
        return [r["status"] for r in result["mechanical_results"] if r["check"] == name]

    def test_identical_markdown_and_readback_only_certify_measured_surfaces(self):
        result = self.check()
        self.assertEqual(result["exit_code"], 0)
        self.assertEqual(result["reader_review"], "未观察")
        self.assertIn("PASS", self.statuses(result, "readback"))
        self.assertEqual(self.statuses(result, "published_page"), ["未观察"])

    def test_tampered_source_and_target_are_rejected(self):
        self.source.write_text("x = 2\n")
        self.assertEqual(self.check()["exit_code"], 1)
        self.target.write_text("x = 3\n")
        self.assertIn("FAIL", self.statuses(self.check(), "files"))

    def test_unavailable_hash_and_required_readback_do_not_pass(self):
        self.handoff["candidate_identity"]["source"] = "source.md"
        self.assertEqual(self.check()["exit_code"], 1)
        self.handoff["candidate_identity"]["source"] = {"path": "source.md", "sha256": adapter.sha256(self.source)}
        self.handoff["delivery_targets"][0].pop("readback")
        self.assertEqual(self.check(required=["readback"])["exit_code"], 1)

    def test_out_of_scope_edit_fails_even_when_exact_item_survives(self):
        base = self.root / "base.md"
        base.write_text("# Fixture\n\nx = 0\n")
        self.handoff["accepted_base"] = "base.md"
        self.handoff["edit_scope"] = {"allowed_patches": [{"before": "x = 0", "after": "x = 1"}]}
        self.handoff["exact_items"] = [{"text": "x = 1", "line": 3}]
        self.assertEqual(self.check(required=["edit_scope", "exact_items"])["exit_code"], 0)
        base.write_text("# Changed\n\nx = 0\n")
        result = self.check()
        self.assertIn("FAIL", self.statuses(result, "edit_scope"))
        self.assertIn("PASS", self.statuses(result, "exact_items"))

    def test_mismatched_readback_fails(self):
        self.readback.write_text("x = 2\n")
        self.assertEqual(self.check()["exit_code"], 1)

    def test_missing_and_malformed_inputs_fail(self):
        self.target.unlink()
        self.assertEqual(self.check()["exit_code"], 1)
        handoff = self.root / "bad.json"
        handoff.write_text("[]")
        self.assertEqual(adapter.check(handoff)["exit_code"], 1)
        self.assertEqual(adapter.check(self.root / "absent.json")["exit_code"], 1)

    def test_markdown_resources_code_fences_and_invalid_text(self):
        self.target.write_text("```text\n[absent](missing.png)\n```\n")
        self.assertFalse(adapter.markdown_result(self.target)["errors"])
        for text in ["```text\n", "[absent](missing.png)\n", "bad\x00text"]:
            self.target.write_text(text)
            self.assertTrue(adapter.markdown_result(self.target)["errors"])

    def test_pdf_reuses_existing_validator_and_requests_every_page(self):
        calls = []

        class FakePDF:
            @staticmethod
            def validate_pdf(path, **kwargs):
                calls.append(kwargs)
                return {"pages": 2, "preview_paths": ["1.png", "2.png"], "errors": []}

        with patch.object(adapter.importlib.util, "module_from_spec", return_value=FakePDF), \
             patch.object(adapter.importlib.util, "spec_from_file_location") as factory:
            factory.return_value.loader.exec_module.return_value = None
            measured = adapter.pdf_result(self.target, self.source, Path("renderer"))
        self.assertEqual(calls[0]["preview_pages"], "all")
        self.assertTrue(measured["all_pages_generated"])
        self.assertNotIn("preview_paths", measured)

    def test_pdf_missing_renderer_reports_unobserved_not_pass(self):
        pdf = self.root / "target.pdf"
        pdf.write_bytes(b"%PDF-invalid")
        self.handoff["delivery_targets"] = [{"path": "target.pdf"}]
        result = self.check(renderer=self.root)
        self.assertIn("未观察", self.statuses(result, "format"))
        self.assertEqual(result["exit_code"], 1)

    def test_zip_manifest_and_student_evidence_separation(self):
        evidence = self.root / "evidence.yaml"
        evidence.write_bytes((ROOT / "shared/templates/plugin-execution-evidence.yaml").read_bytes())
        self.handoff["execution_evidence"] = "evidence.yaml"
        self.handoff["delivery_targets"] = [{"path": "bundle.zip", "audience": "student",
                                             "components": {"target.md": "target.md"}}]
        bundle = self.root / "bundle.zip"
        with zipfile.ZipFile(bundle, "w") as z:
            z.write(self.target, "target.md")
        self.assertIn("PASS", self.statuses(self.check(), "format"))
        with zipfile.ZipFile(bundle, "a") as z:
            z.write(evidence, "evidence.yaml")
        result = self.check()
        self.assertIn("FAIL", self.statuses(result, "format"))
        self.handoff["delivery_targets"][0]["components"]["evidence.yaml"] = "evidence.yaml"
        self.assertIn("FAIL", self.statuses(self.check(), "format"))

    def test_cli_returns_nonzero_for_unfulfilled_required_check(self):
        self.check()
        run = subprocess.run([sys.executable, str(SCRIPT), str(self.root / "handoff.json"), "--require", "evidence"],
                             capture_output=True, text=True)
        self.assertEqual(run.returncode, 1)
        self.assertEqual(json.loads(run.stdout)["reader_review"], "未观察")


class ResearchAuthoringSkeleton(unittest.TestCase):
    def test_candidate_keeps_historical_release_separate(self):
        config = json.loads((ROOT / "scripts/codex_marketplace_config.json").read_text())
        research = next(p for p in config["plugins"] if p["name"] == "research-writing")
        self.assertEqual((research["version"], research["releaseStatus"], research["releasedVersion"]),
                         ("0.1", "candidate", "0.2"))
        self.assertEqual(research["displayName"], "Research Authoring")

    def test_completed_entries_have_no_placeholders_and_resolving_reference_links(self):
        for name in NEW:
            for base in [SOURCE / name, ROOT / "plugins/codex/plugins/research-writing/skills" / name,
                         ROOT / "plugins/gpt/plugins/research-writing/skills" / name]:
                text = (base / "SKILL.md").read_text()
                self.assertNotIn("GPT-WRITES", text)
                for target in re.findall(r"\]\(([^)]+)\)", text):
                    self.assertTrue((base / target).is_file(), (base, target))
                self.assertEqual((base / "references/execution-evidence.yaml").read_bytes(),
                                 (ROOT / "shared/templates/plugin-execution-evidence.yaml").read_bytes())

    def test_codex_thin_entries_only_load_production_inputs(self):
        for name in NEW:
            codex = ROOT / "plugins/codex/plugins/research-writing/skills" / name
            self.assertEqual((codex / "SKILL.md").read_bytes(), (SOURCE / name / "codex-entry.md").read_bytes())
            links = re.findall(r"\]\(([^)]+)\)", (codex / "SKILL.md").read_text())
            self.assertEqual(set(links), {"references/production-contract.md", "references/handoff.template.json",
                                          "references/execution-evidence.yaml"})

    def test_old_public_artifact_names_resolve_to_renamed_entries(self):
        base = ROOT / "plugins/codex/plugins/research-writing/skills"
        for old, new in [("paper", "research-paper"), ("litcite", "research-citations")]:
            text = (base / old / "SKILL.md").read_text()
            self.assertIn(f"[{new}](../{new}/SKILL.md)", text)
            self.assertTrue((base / old / f"../{new}/SKILL.md").is_file())
            legacy_name = {"paper": "research-paper-workflow", "litcite": "literature-and-citations"}[old]
            self.assertIn(f"name: {legacy_name}\n", text)

    def test_rename_proof_hashes_and_snapshot_bytes(self):
        proof = json.loads((ROOT / "docs/design/plugin-reset-2026-11/research-authoring-rename-proof.json").read_text())
        for entry in proof["files"]:
            data = (ROOT / entry["new_path"]).read_bytes()
            if entry.get("name_before"):
                data = data.replace(f'name: {entry["name_after"]}\n'.encode(), f'name: {entry["name_before"]}\n'.encode(), 1)
                data = data.replace(f'# {entry["name_after"]}\n'.encode(), f'# {entry["name_before"]}\n'.encode(), 1)
            self.assertEqual(hashlib.sha256(data).hexdigest(), entry["before_sha256"], entry["new_path"])


if __name__ == "__main__":
    unittest.main()
