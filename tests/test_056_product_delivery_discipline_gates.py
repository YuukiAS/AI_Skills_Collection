from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RESULT_ROOT = REPO_ROOT / "results/056_product_delivery_discipline"
R1_REPLAY_ROOT = RESULT_ROOT / "replay_evidence"
R2_INPUT_ROOT = RESULT_ROOT / "replay_inputs_unbiased"
R2_REPLAY_ROOT = RESULT_ROOT / "replay_evidence_unbiased"
ADJUDICATION_ROOT = RESULT_ROOT / "replay_adjudication"
PRODUCTION_CANDIDATE_COMMIT = "33c30bbe0dd528031a23d379905cd00d6b65bc1f"
BRIDGE_CANDIDATE_COMMIT = "96a8ea1b58ebe6f9b7c5c46c43995666251911fe"
FROZEN_RUBRIC_SHA256 = "516ed142f55200840e54cda01a08793b51d2e666bc4bc4f8e62e5feb03170269"


FORBIDDEN_NEUTRAL_INPUT_PATTERNS = re.compile(
    r"\bG[1-8]\b|Source Discovery|expected|The correct behavior is|"
    r"stale_install|should-not-change|\bPASS\b|\bFAIL\b|rubric|FROZEN|"
    r"diagnosis_first|adds_duplicate_policy",
    re.IGNORECASE,
)


PLUGIN_CASES = {
    "workflow_core": {
        "plugin": "workflow-core",
        "version": "0.3",
        "inputs": ["workflow_core_task.md", "workflow_core_scenarios.json"],
        "adjudication": "workflow_core_adjudication.md",
        "gates": ["G2", "G3", "G4", "G5", "G7", "Source Discovery"],
    },
    "web_development": {
        "plugin": "web-development",
        "version": "0.2",
        "inputs": ["web_development_task.md", "web_development_scenario.json"],
        "adjudication": "web_development_adjudication.md",
        "gates": ["G6"],
    },
    "ai_skills_core": {
        "plugin": "ai-skills-core",
        "version": "0.4",
        "inputs": ["ai_skills_core_task.md", "ai_skills_core_scenario.json"],
        "adjudication": "ai_skills_core_adjudication.md",
        "gates": ["G8"],
    },
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_sha256s(path: Path) -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, name = line.split("  ", 1)
        entries[name] = digest
    return entries


class ProductDeliveryDisciplineEvidenceRepairTests(unittest.TestCase):
    def test_production_candidate_identity_and_versions_remain_fixed(self) -> None:
        manifest = read_json(RESULT_ROOT / "evidence_manifest.json")

        self.assertEqual(
            manifest["production_candidate_identity"]["ai_skills_candidate_commit"],
            PRODUCTION_CANDIDATE_COMMIT,
        )
        self.assertEqual(
            manifest["production_candidate_identity"]["bridge_candidate_commit"],
            BRIDGE_CANDIDATE_COMMIT,
        )
        self.assertFalse(manifest["production_candidate_identity"]["production_source_changed_after_candidate"])
        self.assertFalse(manifest["production_candidate_identity"]["version_changed_in_evidence_repair"])

    def test_r1_manifest_is_retained_as_provenance_not_unbiased_semantic_pass(self) -> None:
        r1 = read_json(R1_REPLAY_ROOT / "manifest.json")

        self.assertEqual(r1["production_candidate_commit"], PRODUCTION_CANDIDATE_COMMIT)
        self.assertEqual(r1["evidence_layer"], "R1 leading-oracle provenance")
        self.assertEqual(r1["semantic_pass_status"], "superseded_for_unbiased_G2_G8_semantic_PASS")
        self.assertIn("actual consumption", r1["note"])
        self.assertIn("R2 unbiased", r1["note"])

    def test_neutral_candidate_visible_inputs_do_not_leak_gate_oracle_terms(self) -> None:
        for meta in PLUGIN_CASES.values():
            for name in meta["inputs"]:
                text = (R2_INPUT_ROOT / name).read_text(encoding="utf-8")
                self.assertIsNone(FORBIDDEN_NEUTRAL_INPUT_PATTERNS.search(text), name)
                self.assertNotIn("FROZEN_G2_G8_RUBRIC", text)
                self.assertNotIn("replay_adjudication", text)

    def test_unbiased_replay_receipts_prove_installed_candidate_consumption(self) -> None:
        for key, meta in PLUGIN_CASES.items():
            with self.subTest(plugin=key):
                run = read_json(R2_REPLAY_ROOT / key / "candidate_replay_run.json")
                add = read_json(R2_REPLAY_ROOT / key / "plugin-add.json")

                self.assertEqual(run["candidate_commit"], PRODUCTION_CANDIDATE_COMMIT)
                self.assertEqual(run["plugin_id"], f"{meta['plugin']}@ai-skills-candidate")
                self.assertEqual(run["runtime_version"], "codex-cli 0.153.4")
                self.assertTrue(run["actual_consumption"]["proven"])
                self.assertGreaterEqual(run["actual_consumption"]["line_index"], 1)
                self.assertIn("item.", run["actual_consumption"]["event_type"])
                self.assertEqual(add["pluginId"], f"{meta['plugin']}@ai-skills-candidate")
                self.assertEqual(add["marketplaceName"], "ai-skills-candidate")
                self.assertEqual(add["version"], meta["version"])
                self.assertEqual(add["installedPath"], run["installed_path"])

    def test_frozen_rubric_hash_is_stable_before_and_after_replay(self) -> None:
        rubric = ADJUDICATION_ROOT / "FROZEN_G2_G8_RUBRIC.md"
        self.assertEqual(sha256(rubric), FROZEN_RUBRIC_SHA256)
        self.assertIn(FROZEN_RUBRIC_SHA256, (ADJUDICATION_ROOT / "FROZEN_G2_G8_RUBRIC.sha256").read_text())
        self.assertIn(FROZEN_RUBRIC_SHA256, (ADJUDICATION_ROOT / "FROZEN_G2_G8_RUBRIC.post_replay.sha256").read_text())

    def test_raw_stdout_stderr_response_exist_and_hashes_match(self) -> None:
        for key in PLUGIN_CASES:
            with self.subTest(plugin=key):
                directory = R2_REPLAY_ROOT / key
                expected = [
                    "candidate_replay_run.json",
                    "plugin-add.json",
                    "child.stdout.jsonl",
                    "child.stderr",
                    "response.md",
                    "raw_evidence_manifest.json",
                ]
                hashes = parse_sha256s(directory / "SHA256SUMS")
                for name in expected:
                    artifact = directory / name
                    self.assertTrue(artifact.is_file(), artifact)
                    if name != "child.stderr":
                        self.assertGreater(artifact.stat().st_size, 0, artifact)
                    self.assertEqual(hashes[name], sha256(artifact), artifact)

    def test_adjudication_binds_rubric_raw_output_and_exact_candidate(self) -> None:
        for key, meta in PLUGIN_CASES.items():
            with self.subTest(plugin=key):
                response_hash = sha256(R2_REPLAY_ROOT / key / "response.md")
                text = (ADJUDICATION_ROOT / meta["adjudication"]).read_text(encoding="utf-8")

                self.assertIn(PRODUCTION_CANDIDATE_COMMIT, text)
                self.assertIn(FROZEN_RUBRIC_SHA256, text)
                self.assertIn(response_hash, text)
                self.assertIn("SOURCE_DEFECT_DISCOVERED=NO", text)
                self.assertIn("PASS", text)
                for gate in meta["gates"]:
                    self.assertIn(gate, text)

    def test_evidence_manifest_distinguishes_raw_candidate_output_from_adjudication(self) -> None:
        manifest = read_json(RESULT_ROOT / "evidence_manifest.json")
        unbiased = read_json(R2_REPLAY_ROOT / "manifest.json")

        self.assertFalse(manifest["source_defect_discovered"])
        self.assertEqual(
            manifest["r1_oracle_led_evidence"]["status"],
            "provenance_actual_consumption_only_superseded_for_unbiased_semantic_PASS",
        )
        self.assertEqual(unbiased["old_r1_evidence_status"], manifest["r1_oracle_led_evidence"]["status"])
        for run in unbiased["runs"]:
            self.assertTrue(run["raw_output_dir"].startswith("replay_evidence_unbiased/"))
            self.assertTrue(run["adjudication"].startswith("replay_adjudication/"))
            self.assertNotEqual(run["raw_output_dir"], run["adjudication"])
            self.assertTrue(run["pass"])
            self.assertFalse(run["source_defect_discovered"])

    def test_result_records_locator_typo_correction_and_pending_host_boundary(self) -> None:
        text = (RESULT_ROOT / "RESULT.md").read_text(encoding="utf-8")

        self.assertIn("RESULT_LOCATOR_CORRECTED=YES", text)
        self.assertIn("9f1c0d32abf49e674bcc7cab0e7287ed714a1199", text)
        self.assertIn("SOURCE_DEFECT_DISCOVERED=NO", text)
        self.assertIn("real Host", text)
        self.assertNotIn("9f1c0d33d716d484743c2880fe4e32d2a4941ef8, containing", text)


if __name__ == "__main__":
    unittest.main()
