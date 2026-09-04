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


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def make_stage_package(helper, root: Path, source: str, *, decision: str = "PASS") -> Path:
    stage_dir = root / "stage"
    stage_dir.mkdir()
    units = helper.split_markdown_units(source)
    document_map = {
        "schema": "SCIENTIFIC_REWRITE_HOST_DOCUMENT_MAP_V1",
        "source_sha256": helper.sha256_text(source),
        "audience": "中文科研读者",
        "document_purpose": "解释当前证据、限制和下一步实验判断。",
        "core_research_question": "当前证据支持什么判断，下一步怎样验证？",
    }
    write_json(stage_dir / "document_map.json", document_map)
    document_map_sha = helper.sha256_bytes((stage_dir / "document_map.json").read_bytes())

    candidate_units: list[str] = []
    public_units = []
    selected = {"schema": "SCIENTIFIC_REWRITE_SELECTED_TRANSFORMATIONS_V1", "by_unit": {}}
    unit_audits = []
    all_literals = []
    for unit in units:
        propositions = helper.proposition_inventory(unit)
        unit_source_sha = helper.sha256_text(unit.text)
        public_units.append(
            {
                "unit_id": unit.unit_id,
                "source_span_ids": unit.source_span_ids,
                "source_unit_sha256": unit_source_sha,
                "start_line": unit.start_line,
                "end_line": unit.end_line,
                "argument_role": unit.argument_role,
            }
        )
        card = {
            "schema": "SCIENTIFIC_REWRITE_HOST_MEANING_CARD_V1",
            "unit_id": unit.unit_id,
            "document_map_sha256": document_map_sha,
            "source_unit_sha256": unit_source_sha,
            "reader_job": "先理解问题和证据，再判断下一步。",
            "plain_meaning": "该段说明证据边界和实验判断。",
            "reader_takeaway": "保留事实后降低读者解码成本。",
            "rewrite_problem": "workflow-language",
            "discourse_function": unit.argument_role,
            "claims": [
                {
                    "normalized_meaning": "该单元的核心含义来自原文命题。",
                    "evidence_class": "research_interpretation",
                    "source_proposition_ids": [item["proposition_id"] for item in propositions],
                    "source_span_ids": unit.source_span_ids,
                }
            ],
            "evidence": [],
            "conditions": [],
            "comparators": [],
            "uncertainty": [],
            "caveats": [],
            "negative_findings": [],
            "attribution": [],
            "decision_logic": [],
            "terminology": [],
        }
        write_json(stage_dir / "meaning_cards" / f"{unit.unit_id}.json", card)
        selected["by_unit"][unit.unit_id] = ["workflow-label-to-relation", "trace-to-appendix"]
        candidate_unit = unit.text
        (stage_dir / "candidate_units").mkdir(exist_ok=True)
        (stage_dir / "candidate_units" / f"{unit.unit_id}.md").write_text(candidate_unit, encoding="utf-8")
        candidate_units.append(candidate_unit)
        unit_audits.append(
            {
                "unit_id": unit.unit_id,
                "decision": decision,
                "candidate_unit_sha256": helper.sha256_text(candidate_unit),
                "findings": [] if decision == "PASS" else [{"severity": "critical"}],
            }
        )
        all_literals.extend(unit.literal_invariants)

    final_candidate = "\n\n".join(candidate_units)
    write_json(stage_dir / "argument_units.json", {"schema": "SCIENTIFIC_REWRITE_ARGUMENT_UNITS_V1", "units": public_units})
    write_json(stage_dir / "selected_transformations.json", selected)
    write_json(stage_dir / "fidelity_ledger.json", {"schema": "SCIENTIFIC_REWRITE_FIDELITY_LEDGER_V1", "literal_invariants": all_literals})
    write_json(
        stage_dir / "self_audit.json",
        {
            "schema": "SCIENTIFIC_REWRITE_HOST_SELF_AUDIT_V1",
            "decision": decision,
            "final_candidate_sha256": helper.sha256_text(final_candidate),
            "global_assembly": {
                "reader_order_unit_ids": [unit.unit_id for unit in units],
                "strategy": "按读者问题组织；本 fixture 不需要改变源顺序。",
            },
            "unit_audits": unit_audits,
        },
    )
    (stage_dir / "final_candidate.md").write_text(final_candidate, encoding="utf-8")
    return stage_dir


class ScientificRewriteTests(unittest.TestCase):
    def test_skill_contract_routes_heavy_chinese_scientific_rewrite_to_host_codex(self) -> None:
        text = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Meaning Card", text)
        self.assertIn("Fidelity Ledger", text)
        self.assertIn("current host Codex session performs", text)
        self.assertIn("validate-host-stage", text)
        self.assertNotIn("OPENAI_API_KEY", text)
        self.assertNotIn("OPENAI_TEXT_TRANSFORM_API_KEY", text)
        self.assertNotIn("--driver openai-responses", text)

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
        selected = helper.select_examples(
            helper.load_seed_library(),
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

    def test_helper_has_no_external_generation_surface(self) -> None:
        helper_source = HELPER_PATH.read_text(encoding="utf-8")
        self.assertNotIn("api.openai.com", helper_source)
        self.assertNotIn("urllib.request", helper_source)
        self.assertNotIn("call_openai_text", helper_source)
        self.assertNotIn("openai-responses", helper_source)
        self.assertNotIn("restore_exact_literals", helper_source)
        helper = load_helper()
        with self.assertRaisesRegex(RuntimeError, "does not let the helper generate"):
            helper.run_multistage("CARE 在 2026-08-28 的 Dice=0.81。")

    def test_generic_runtime_has_no_task_specific_phrase_repair(self) -> None:
        helper_source = HELPER_PATH.read_text(encoding="utf-8")
        for token in ["provenance", "estimand", "resource contract", "controlled-drift", "CARE", "ODAL", "FedFisher"]:
            self.assertNotIn(token, helper_source)

    def test_structural_rewrite_authorization_is_shared_with_writing_fidelity(self) -> None:
        scientific = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        fidelity = (REPO_ROOT / "skills/writing/core/writing-fidelity/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("STRUCTURAL_REWRITE_AUTHORIZED_BY_TASK", scientific)
        self.assertIn("STRUCTURAL_REWRITE_AUTHORIZED_BY_TASK", fidelity)
        self.assertIn("content/evidence graph", scientific)
        self.assertIn("content/evidence graph", fidelity)

    def test_exact_verifier_detects_literal_invariant_drift(self) -> None:
        helper = load_helper()
        source = (
            "方法 `run_eval.py` 在 2026-08-28 使用 3 个 seed，Dice=0.81，见 [12]、"
            "/tmp/run/config.json 和 Dataset501_CAREMyoPS/splits_final.json；"
            "FedFisher 保留 𝜃̂ 𝐹𝐹 ≈ arg min ∑。"
        )
        ok_candidate = (
            "在 2026-08-28，方法 `run_eval.py` 使用 3 个 seed；Dice=0.81，配置见 "
            "/tmp/run/config.json，划分见 Dataset501_CAREMyoPS/splits_final.json，引用仍为 [12]。"
            "FedFisher 的公式标识仍是 𝜃̂ 𝐹𝐹 ≈ arg min ∑。"
        )
        bad_candidate = "该方法使用多个 seed；Dice 约为 0.8，引用见文末。"
        self.assertTrue(helper.verify_exact(source, ok_candidate)["ok"])
        bad_report = helper.verify_exact(source, bad_candidate)
        self.assertFalse(bad_report["ok"], bad_report)
        self.assertGreaterEqual(len(bad_report["missing"]), 7)

    def test_complete_formulas_are_atomic_and_nested_numbers_are_not_literals(self) -> None:
        helper = load_helper()
        source = "目标函数为 $$L = 1/2 \\sum_i (y_i - f(x_i))^2$$，随后比较 3 个 seed。"
        literals = helper.extract_literal_invariants(source)
        texts = [item["text"] for item in literals]
        self.assertIn("$$L = 1/2 \\sum_i (y_i - f(x_i))^2$$", texts)
        self.assertNotIn("1", texts)
        self.assertNotIn("2", texts)
        self.assertIn("3", texts)
        report = helper.verify_exact(source, "目标函数为 $$L = \\sum_i (y_i - f(x_i))^2$$，随后比较 3 个 seed。")
        self.assertFalse(report["ok"])

    def test_prepare_splits_markdown_by_sections_and_keeps_invariants(self) -> None:
        helper = load_helper()
        text = "# 报告\n\n## 方法\n\n使用 `renv` 和 5 个 seed。\n\n## 结果\n\nDice=0.81，见 [3]。"
        units = helper.split_markdown_units(text)
        self.assertGreaterEqual(len(units), 2)
        self.assertTrue(all(unit.source_span_ids for unit in units))
        all_invariants = [span["text"] for unit in units for span in unit.literal_invariants]
        self.assertIn("`renv`", all_invariants)
        self.assertIn("5", all_invariants)
        self.assertIn("[3]", all_invariants)

    def test_long_unheaded_source_does_not_collapse_to_one_unit(self) -> None:
        helper = load_helper()
        source = "\n\n".join(
            f"第{index}段说明同一份长篇科研报告中的证据、限制、比较和下一步实验条件。" * 30
            for index in range(1, 7)
        )
        self.assertGreater(len(helper.split_markdown_units(source)), 1)

    def test_literal_roles_allow_trace_appendix_but_keep_inline_critical_in_core(self) -> None:
        helper = load_helper()
        source = "Dice=0.81，checkpoint 路径是 /tmp/run/checkpoint.pt。"
        ledger = helper.extract_literal_invariants(source)
        roles = {item["text"]: item["role"] for item in ledger}
        self.assertEqual(roles["Dice=0.81"], "inline-critical")
        self.assertEqual(roles["/tmp/run/checkpoint.pt"], "relocatable-trace")
        candidate = "Dice=0.81。\n\n## Technical / Evidence Appendix\n\n/tmp/run/checkpoint.pt"
        report = helper.verify_exact(source, candidate, ledger, reader_core="Dice=0.81。")
        self.assertTrue(report["ok"], report)

    def test_inline_critical_in_appendix_only_fails(self) -> None:
        helper = load_helper()
        source = "主实验 Dice=0.81，checkpoint 路径是 /tmp/run/checkpoint.pt。"
        ledger = helper.extract_literal_invariants(source)
        candidate = (
            "主实验结果支持一个有边界的判断。\n\n"
            "## Technical / Evidence Appendix\n\n"
            "Dice=0.81\n\n/tmp/run/checkpoint.pt"
        )
        report = helper.verify_exact(source, candidate, ledger, reader_core=helper.reader_facing_core(candidate))
        self.assertFalse(report["ok"])
        self.assertEqual([item["text"] for item in report["missing_inline_core"]], ["Dice=0.81"])

    def test_raw_literal_dump_is_never_a_valid_exact_repair(self) -> None:
        helper = load_helper()
        source = "主实验 Dice=0.81。"
        candidate = "主实验有结果。\n\n保留原文精确项：Dice=0.81"
        report = helper.verify_exact(source, candidate)
        self.assertFalse(report["ok"])
        self.assertTrue(report["raw_literal_dump"])

    def test_reader_review_packet_is_candidate_only(self) -> None:
        helper = load_helper()
        packet = helper.reader_review_packet("候选文本", "统计/ML/医学影像研究者")
        self.assertFalse(packet["source_visible"])
        self.assertEqual(packet["candidate_text"], "候选文本")
        self.assertNotIn("source_text", json.dumps(packet, ensure_ascii=False))

    def test_meaning_card_omitted_proposition_bindings_fail_closed(self) -> None:
        helper = load_helper()
        unit = helper.split_markdown_units(
            "# 结果\n\nCARE 在 2026-08-28 的 Dice=0.81。下一步比较 FedFisher 和 FedLPA。"
        )[0]
        props = helper.proposition_inventory(unit)
        with self.assertRaisesRegex(RuntimeError, "source_proposition_ids"):
            helper.normalize_meaning_card(
                {
                    "unit_id": unit.unit_id,
                    "reader_job": "解释当前证据和下一步判断",
                    "plain_meaning": "先说明结论。",
                    "claims": [{"normalized_meaning": "漏写绑定。", "evidence_class": "research_interpretation", "source_span_ids": unit.source_span_ids}],
                    "evidence": [],
                    "conditions": [],
                    "comparators": [],
                    "uncertainty": [],
                    "caveats": [],
                    "negative_findings": [],
                    "attribution": [],
                    "decision_logic": [],
                    "relation_to_previous": "承接前文",
                    "relation_to_next": "引出后文",
                    "rewrite_problem": "workflow-language",
                    "discourse_function": "result-interpretation",
                    "reader_takeaway": "读者理解判断。",
                },
                unit,
                props,
            )

    def test_meaning_card_source_copy_fallback_fails_closed(self) -> None:
        helper = load_helper()
        unit = helper.split_markdown_units("这个段落直接说明实验条件、比较对象和结论边界，不能被复制成语义理解。")[0]
        props = helper.proposition_inventory(unit)
        with self.assertRaisesRegex(RuntimeError, "copied source prose"):
            helper.normalize_meaning_card(
                {
                    "unit_id": unit.unit_id,
                    "reader_job": "解释证据边界",
                    "plain_meaning": unit.text,
                    "reader_takeaway": "读者理解结论边界。",
                    "rewrite_problem": "workflow-language",
                    "discourse_function": "result-interpretation",
                    "claims": [
                        {
                            "normalized_meaning": unit.text,
                            "evidence_class": "research_interpretation",
                            "source_proposition_ids": [item["proposition_id"] for item in props],
                            "source_span_ids": unit.source_span_ids,
                        }
                    ],
                    "evidence": [],
                    "conditions": [],
                    "comparators": [],
                    "uncertainty": [],
                    "caveats": [],
                    "negative_findings": [],
                    "attribution": [],
                    "decision_logic": [],
                },
                unit,
                props,
            )

    def test_proposition_inventory_contains_hashes_not_source_excerpts(self) -> None:
        helper = load_helper()
        unit = helper.split_markdown_units("这一段有一个需要保留的科学判断。")[0]
        props = helper.proposition_inventory(unit)
        serialized = json.dumps(props, ensure_ascii=False)
        self.assertIn("source_text_sha256", serialized)
        self.assertNotIn("source_excerpt", serialized)
        self.assertNotIn("这一段有一个需要保留的科学判断", serialized)

    def test_host_stage_package_validation_receipt_is_privacy_safe(self) -> None:
        helper = load_helper()
        source = (
            "# 结果\n\nCARE 在 2026-08-28 的 Dice=0.81，checkpoint 见 /tmp/run/checkpoint.pt。\n\n"
            "下一步比较 FedFisher 和 FedLPA；如果 pooled gap 下降就是 GO，否则 STOP。"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            result = helper.validate_host_stage_package(source, stage_dir, candidate_path=stage_dir / "final_candidate.md")
        receipt = result["receipt"]
        self.assertEqual(receipt["schema"], helper.RUNTIME_SCHEMA)
        self.assertEqual(receipt["driver"], "host-codex")
        self.assertEqual(receipt["model_call_count"], 0)
        self.assertEqual(receipt["external_api_call_count"], 0)
        self.assertFalse(receipt["requires_openai_api_key"])
        self.assertTrue(receipt["dataflow_validation"]["ok"])
        self.assertTrue(receipt["argument_coverage"]["ok"])
        self.assertTrue(receipt["global_assembly"]["ok"])
        self.assertTrue(receipt["exact_verification"]["ok"])
        serialized = json.dumps(receipt, ensure_ascii=False)
        self.assertNotIn(source, serialized)
        self.assertNotIn("candidate_text", serialized)

    def test_host_stage_package_rejects_decorative_or_unresolved_files(self) -> None:
        helper = load_helper()
        source = "CARE 在 2026-08-28 的 Dice=0.81。"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source, decision="REVISE")
            with self.assertRaisesRegex(RuntimeError, "unresolved"):
                helper.validate_host_stage_package(source, stage_dir)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            (stage_dir / "meaning_cards" / "unit-001.json").unlink()
            with self.assertRaisesRegex(RuntimeError, "missing meaning card"):
                helper.validate_host_stage_package(source, stage_dir)

    def test_argument_plan_can_bind_non_contiguous_spans_and_reorder_reader_logic(self) -> None:
        helper = load_helper()
        source = "## 问题\n\n第一段定义问题。\n\n## 限制\n\n第二段给出限制。\n\n## 结论\n\n第三段给出结论。"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            argument_units = json.loads((stage_dir / "argument_units.json").read_text(encoding="utf-8"))
            argument_units["units"][0]["source_span_ids"] = ["span-001", "span-003"]
            argument_units["units"][1]["source_span_ids"] = ["span-002"]
            argument_units["units"] = argument_units["units"][:2]
            write_json(stage_dir / "argument_units.json", argument_units)
            self_audit = json.loads((stage_dir / "self_audit.json").read_text(encoding="utf-8"))
            self_audit["global_assembly"]["reader_order_unit_ids"] = ["unit-002", "unit-001"]
            write_json(stage_dir / "self_audit.json", self_audit)
            result = helper.validate_host_stage_package(source, stage_dir)
        self.assertTrue(result["receipt"]["argument_coverage"]["ok"])
        self.assertTrue(result["receipt"]["global_assembly"]["reordered_from_source_order"])

    def test_argument_plan_omitted_or_duplicate_source_spans_fail(self) -> None:
        helper = load_helper()
        source = "## 问题\n\n第一段定义问题。\n\n## 限制\n\n第二段给出限制。"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            argument_units = json.loads((stage_dir / "argument_units.json").read_text(encoding="utf-8"))
            argument_units["units"][0]["source_span_ids"] = ["span-001", "span-002"]
            argument_units["units"][1]["source_span_ids"] = ["span-001"]
            write_json(stage_dir / "argument_units.json", argument_units)
            with self.assertRaisesRegex(RuntimeError, "duplicates source spans"):
                helper.validate_host_stage_package(source, stage_dir)

    def test_semantic_audit_status_aliases_are_canonicalized_conservatively(self) -> None:
        helper = load_helper()
        unit = helper.split_markdown_units("CARE 在 2026-08-28 的 Dice=0.81。")[0]
        props = helper.proposition_inventory(unit)
        review = helper.normalize_semantic_audit(
            {
                "decision": "REVISE",
                "findings": [
                    {
                        "status": "missing",
                        "proposition_id": props[0]["proposition_id"],
                        "source_span_ids": unit.source_span_ids,
                        "severity": "critical",
                    }
                ],
            },
            unit,
            props,
        )
        self.assertEqual(review["findings"][0]["status"], "omitted")
        self.assertEqual(review["critical_violation_count"], 1)

    def test_private_smoke_runner_has_no_api_or_text_transform_dependency(self) -> None:
        runner = (REPO_ROOT / "scripts/run_scientific_rewrite_private_smoke.py").read_text(encoding="utf-8")
        self.assertIn("validate_host_stage_package", runner)
        self.assertNotIn("OPENAI_API_KEY", runner)
        self.assertNotIn("OPENAI_REVIEW_API_KEY", runner)
        self.assertNotIn("text-transform", runner)
        self.assertNotIn("run_multistage", runner)

    def test_writing_style_marketplace_exposes_scientific_rewrite_inside_existing_plugin(self) -> None:
        data = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        plugin = next(item for item in data["plugins"] if item["name"] == "writing-style")
        self.assertEqual(plugin["version"], "0.1")
        sources = {entry["source"]: entry["artifact_id"] for entry in plugin["skills"]}
        self.assertEqual(sources["skills/writing/core/scientific-rewrite"], "scientific-rewrite")
        profile = json.loads((REPO_ROOT / "profiles/codex-writing-style.json").read_text(encoding="utf-8"))
        self.assertIn("skills/writing/core/scientific-rewrite", profile["skills"])

    def test_response_schema_name_is_bounded_and_stable(self) -> None:
        helper = load_helper()
        name = helper.response_schema_name("very long stage name " * 20)
        self.assertLessEqual(len(name), 64)
        self.assertEqual(name, helper.response_schema_name("very long stage name " * 20))


if __name__ == "__main__":
    unittest.main()
