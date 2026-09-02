from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills/writing/core/scientific-rewrite"
HELPER_PATH = SKILL_ROOT / "scripts/rewrite_support.py"


def load_helper():
    spec = importlib.util.spec_from_file_location("rewrite_support", HELPER_PATH)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


class ScientificRewriteTests(unittest.TestCase):
    def test_skill_contract_routes_heavy_chinese_scientific_rewrite(self) -> None:
        text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Meaning Card", text)
        self.assertIn("Fidelity Ledger", text)
        self.assertIn("Never borrow facts", text)
        self.assertIn("research-reporting", text)
        self.assertIn("chinese-prose", text)
        self.assertIn("scientific-prose", text)
        self.assertIn("detector", text)

    def test_seed_library_is_small_metadata_tagged_and_holdout_free(self) -> None:
        seeds = json.loads((SKILL_ROOT / "references/seed-transformations.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(seeds), 12)
        self.assertLessEqual(len(seeds), 20)
        required = {
            "scene",
            "discourse_function",
            "rewrite_problem",
            "rewrite_depth",
            "fidelity_risk",
            "register",
            "source",
            "source_revision",
            "license",
            "approval_status",
            "original_template",
            "rewrite_template",
        }
        forbidden = {"bobbio", "distributed imaging", "r_research_stack", "asteria", "care/m&ms"}
        for seed in seeds:
            self.assertTrue(required.issubset(seed), seed.get("id"))
            self.assertIn(seed["approval_status"], {"SEED", "REFERENCE", "REVIEWED_REFERENCE", "REVIEWED"})
            serialized = json.dumps(seed, ensure_ascii=False).lower()
            for token in forbidden:
                self.assertNotIn(token, serialized)

    def test_metadata_selection_returns_diverse_bounded_examples(self) -> None:
        helper = load_helper()
        library = helper.load_seed_library()
        selected = helper.select_examples(
            library,
            limit=4,
            scene="scientific-report",
            discourse_function="result-interpretation",
            rewrite_problem="workflow-language",
            fidelity_risk="high",
            register="formal-technical",
        )
        self.assertGreaterEqual(len(selected), 2)
        self.assertLessEqual(len(selected), 4)
        self.assertEqual(len({item["id"] for item in selected}), len(selected))
        self.assertGreaterEqual(len({item["discourse_function"] for item in selected[:2]}), 2)

    def test_exact_verifier_detects_literal_invariant_drift(self) -> None:
        helper = load_helper()
        source = "方法 `run_eval.py` 在 2026-08-28 使用 3 个 seed，Dice=0.81，见 [12] 和 /tmp/run/config.json。"
        ok_candidate = "在 2026-08-28，方法 `run_eval.py` 使用 3 个 seed；Dice=0.81，配置见 /tmp/run/config.json，引用仍为 [12]。"
        bad_candidate = "该方法使用多个 seed；Dice 约为 0.8，引用见文末。"
        ok_report = helper.verify_exact(source, ok_candidate)
        bad_report = helper.verify_exact(source, bad_candidate)
        self.assertTrue(ok_report["ok"], ok_report)
        self.assertFalse(bad_report["ok"], bad_report)
        self.assertGreaterEqual(len(bad_report["missing"]), 4)

    def test_prepare_splits_markdown_by_sections_and_keeps_invariants(self) -> None:
        helper = load_helper()
        text = "# 报告\n\n## 方法\n\n使用 `renv` 和 5 个 seed。\n\n## 结果\n\nDice=0.81，见 [3]。"
        units = helper.split_markdown_units(text)
        self.assertEqual([unit.heading for unit in units], ["报告", "方法", "结果"])
        all_invariants = [span["text"] for unit in units for span in unit.literal_invariants]
        self.assertIn("`renv`", all_invariants)
        self.assertIn("5", all_invariants)
        self.assertIn("[3]", all_invariants)

    def test_helper_verify_exact_reports_missing_literal(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            source = tmp_path / "source.md"
            candidate = tmp_path / "candidate.md"
            source.write_text("2026-08-28 使用 `renv`，n=3。", encoding="utf-8")
            candidate.write_text("使用环境管理，样本量为 3。", encoding="utf-8")
            helper = load_helper()
            report = helper.verify_exact(source.read_text(encoding="utf-8"), candidate.read_text(encoding="utf-8"))
            self.assertFalse(report["ok"])

    def test_writing_style_marketplace_exposes_scientific_rewrite_inside_existing_plugin(self) -> None:
        data = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        plugin = next(item for item in data["plugins"] if item["name"] == "writing-style")
        self.assertEqual(plugin["version"], "0.1")
        sources = {entry["source"]: entry["artifact_id"] for entry in plugin["skills"]}
        self.assertEqual(sources["skills/writing/core/scientific-rewrite"], "scientific-rewrite")
        self.assertEqual(data["marketplacePluginBudget"], 10)
        profile = json.loads((REPO_ROOT / "profiles/codex-writing-style.json").read_text(encoding="utf-8"))
        self.assertIn("skills/writing/core/scientific-rewrite", profile["skills"])

    def test_writing_fidelity_documents_literal_vs_semantic_split(self) -> None:
        fidelity = (REPO_ROOT / "skills/writing/core/writing-fidelity/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Literal vs Semantic Preservation", fidelity)
        self.assertIn("ordinary reader-facing headings", fidelity.lower())
        self.assertIn("preserved`, `narrowed`, `broadened`, `reversed`, `invented`", fidelity)

    def test_multistage_runtime_receipt_has_separate_responsibilities(self) -> None:
        helper = load_helper()
        source = (
            "# CARE evidence\n\n"
            "当前 checkpoint provenance audit 显示 /tmp/run/checkpoint.pt 与训练历史重叠，因此这个实验只能说明 2026-08-28 的 CARE 证据边界。\n\n"
            "## 下一步\n\n"
            "下一轮比较 pooled、local-only、FedAvg、FedFisher 和 FedLPA；如果 pooled gap 下降且 drift 可控就是 GO，否则 STOP。\n"
        )
        result = helper.run_multistage(source)
        receipt = result["receipt"]
        self.assertEqual(receipt["schema"], helper.RUNTIME_SCHEMA)
        self.assertFalse(receipt["whole_document_writer_call"])
        self.assertGreaterEqual(receipt["unit_count"], 2)
        responsibilities = "\n".join(item["responsibility"] for item in receipt["stage_records"])
        self.assertIn("document purpose", responsibilities)
        self.assertIn("Meaning Card", responsibilities)
        self.assertIn("candidate only", responsibilities.replace("-", " "))
        self.assertIn("final assembly", responsibilities)

    def test_multistage_runtime_selects_bounded_examples_not_full_library(self) -> None:
        helper = load_helper()
        source = "# 比较\n\nODAL vs FedFisher / FedLPA 的比较必须保留 Fisher、Laplace、theta_0 和 3 个 seed。"
        result = helper.run_multistage(source)
        receipt = result["receipt"]
        self.assertLessEqual(receipt["max_examples_per_unit"], 4)
        self.assertFalse(receipt["full_seed_library_injected"])
        writer_records = [item for item in receipt["stage_records"] if item["stage_id"].endswith("-writer")]
        self.assertTrue(writer_records)
        self.assertTrue(writer_records[0]["selected_example_ids"])

    def test_literal_roles_allow_trace_appendix_but_keep_inline_critical_in_core(self) -> None:
        helper = load_helper()
        source = "Dice=0.81，checkpoint 路径是 /tmp/run/checkpoint.pt。"
        ledger = helper.extract_literal_invariants(source)
        roles = {item["text"]: item["role"] for item in ledger}
        self.assertEqual(roles["0.81"], "inline-critical")
        self.assertEqual(roles["/tmp/run/checkpoint.pt"], "relocatable-trace")
        candidate = "Dice=0.81。\n\n## Technical / Evidence Appendix\n\n/tmp/run/checkpoint.pt"
        report = helper.verify_exact(source, candidate, ledger, reader_core="Dice=0.81。")
        self.assertTrue(report["ok"], report)

    def test_reader_review_packet_is_candidate_only(self) -> None:
        helper = load_helper()
        packet = helper.reader_review_packet("候选文本", "统计/ML/医学影像研究者")
        self.assertFalse(packet["source_visible"])
        serialized = json.dumps(packet, ensure_ascii=False)
        self.assertIn("GO or STOP", serialized)
        self.assertNotIn("current_original_unit", serialized)

    def test_openai_driver_makes_observable_stage_calls(self) -> None:
        helper = load_helper()
        calls = []
        original = helper.call_openai_text

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            calls.append({"prompt": prompt, "source": source, "kwargs": kwargs})
            if "Rewrite only the current argument unit" in prompt:
                payload = json.loads(source)
                return payload["current_original_unit"]
            return "stage ok"

        helper.call_openai_text = fake_call
        try:
            result = helper.run_multistage(
                "# 结果\n\nCARE 在 2026-08-28 的 Dice=0.81；下一步比较 FedFisher 和 FedLPA。",
                driver="openai-responses",
                model="test-model",
                api_key="test-key",
            )
        finally:
            helper.call_openai_text = original

        receipt = result["receipt"]
        model_stage_ids = [item["stage_id"] for item in receipt["stage_records"] if item["model_call"]]
        self.assertEqual(receipt["model_call_count"], len(calls))
        self.assertIn("document-map", model_stage_ids)
        self.assertTrue(any(stage_id.endswith("-meaning-card") for stage_id in model_stage_ids))
        self.assertTrue(any(stage_id.endswith("-writer") for stage_id in model_stage_ids))
        self.assertTrue(any(stage_id.endswith("-literal-semantic-audit") for stage_id in model_stage_ids))
        self.assertIn("candidate-only-reader-review", model_stage_ids)
        self.assertIn("final-assembly-coherence", model_stage_ids)

    def test_openai_driver_applies_targeted_repair_output(self) -> None:
        helper = load_helper()
        original = helper.call_openai_text

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            if "Rewrite only the current argument unit" in prompt:
                return "CARE 的结果需要解释。"
            if "Repair only the current rewritten unit" in prompt:
                payload = json.loads(source)
                return payload["unit"]["text"]
            return "stage ok"

        helper.call_openai_text = fake_call
        try:
            result = helper.run_multistage(
                "# 结果\n\nCARE 在 2026-08-28 的 Dice=0.81；下一步比较 FedFisher 和 FedLPA。",
                driver="openai-responses",
                model="test-model",
                api_key="test-key",
            )
        finally:
            helper.call_openai_text = original

        receipt = result["receipt"]
        self.assertIn("2026-08-28", result["candidate"])
        self.assertIn("Dice=0.81", result["candidate"])
        self.assertTrue(any(item["stage_id"].endswith("-targeted-repair") for item in receipt["stage_records"]))
        self.assertTrue(any(item["stage_id"].endswith("-post-repair-audit") for item in receipt["stage_records"]))


if __name__ == "__main__":
    unittest.main()
