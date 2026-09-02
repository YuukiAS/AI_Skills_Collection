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


def structured_stage_response(prompt: str, source: str, *, omit_writer_literals: bool = False) -> str:
    payload = json.loads(source)
    if "Map the document purpose" in prompt:
        span_ids = [span["span_id"] for span in payload["source_spans"]]
        return json.dumps(
            {
                "audience": "统计、ML 和医学影像研究者",
                "document_purpose": "把科研证据解释成可阅读的中文报告",
                "core_research_question": "自定义核心问题：当前证据能支持什么下一步判断",
                "section_roles": [{"role_id": "section-001", "source_span_ids": span_ids, "normalized_meaning": "证据解释"}],
                "major_claims": [{"claim_id": "claim-001", "source_span_ids": span_ids, "normalized_meaning": "需要保留事实边界"}],
                "major_evidence": [{"evidence_id": "evidence-001", "source_span_ids": span_ids, "normalized_meaning": "公开测试证据"}],
                "major_uncertainties": [],
                "major_negative_findings": [],
                "major_decisions": [],
                "cross_section_dependencies": [],
                "terminology_contract": [],
                "reader_core_priorities": ["先解释研究含义"],
                "trace_material_categories": ["路径和审计细节进入技术附录"],
            },
            ensure_ascii=False,
        )
    if "Segment the source into argument units" in prompt:
        return json.dumps(
            {
                "units": [
                    {
                        "unit_id": f"unit-{index:03d}",
                        "source_span_ids": [span["span_id"]],
                        "argument_role": "evidence-or-result",
                        "why_these_spans_belong_together": "single source span argument unit",
                    }
                    for index, span in enumerate(payload["source_spans"], start=1)
                ]
            },
            ensure_ascii=False,
        )
    if "Create a structured Meaning Card" in prompt:
        unit = payload["unit"]
        prop_ids = [item["proposition_id"] for item in payload["source_propositions"]]
        span_ids = unit["source_span_ids"]
        card_item = {"normalized_meaning": "自定义普通含义：先说结论，再保留技术细节", "source_span_ids": span_ids, "source_proposition_ids": prop_ids}
        return json.dumps(
            {
                "unit_id": unit["unit_id"],
                "reader_job": "理解当前证据和下一步判断",
                "plain_meaning": "自定义普通含义：先说结论，再保留技术细节",
                "claims": [card_item],
                "evidence": [],
                "conditions": [],
                "comparators": [],
                "uncertainty": [],
                "caveats": [],
                "negative_findings": [],
                "attribution": [],
                "decision_logic": [],
                "terminology": [],
                "literal_items": [],
                "relocatable_trace_items": [],
                "relation_to_previous": "承接前文",
                "relation_to_next": "引出后文",
                "rewrite_problem": "workflow-language",
                "discourse_function": "result-interpretation",
                "reader_takeaway": "读者应先理解判断含义",
            },
            ensure_ascii=False,
        )
    if "Rewrite only the current argument unit" in prompt:
        coverage = [item["proposition_id"] for item in payload["source_propositions"]]
        reader_core = "CARE 的结果需要解释。" if omit_writer_literals else payload["current_original_unit"]
        return json.dumps(
            {"reader_core": reader_core, "technical_trace": "", "source_coverage_ids": coverage, "relocated_trace_ids": []},
            ensure_ascii=False,
        )
    if "Repair only the current rewritten unit" in prompt or "Repair this unit only for reader effort" in prompt:
        unit = payload["unit"]
        coverage = sorted(
            {
                str(prop_id)
                for field in ["claims", "evidence", "conditions", "comparators", "uncertainty", "caveats", "negative_findings", "attribution", "decision_logic"]
                for item in payload.get("meaning_card", {}).get(field, [])
                for prop_id in item.get("source_proposition_ids", [])
            }
        )
        return json.dumps(
            {"reader_core": unit["text"], "technical_trace": "", "source_coverage_ids": coverage, "relocated_trace_ids": []},
            ensure_ascii=False,
        )
    if "Audit semantic preservation" in prompt or "Re-audit semantic preservation" in prompt:
        return json.dumps({"decision": "PASS", "findings": []}, ensure_ascii=False)
    if "Review only the candidate text" in prompt or "Re-review only the repaired candidate text" in prompt:
        return json.dumps(
            {
                "decision": "PASS",
                "questions": [{"answerable": True, "inferred_answer": "候选文本可回答核心读者问题。"}],
                "findings": [],
            },
            ensure_ascii=False,
        )
    if "Check final assembly coherence" in prompt:
        return json.dumps({"decision": "PASS", "findings": []}, ensure_ascii=False)
    raise AssertionError(f"unexpected prompt: {prompt[:160]}")


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
        self.assertGreaterEqual(len(units), 2)
        self.assertTrue(all(unit.source_span_ids for unit in units))
        self.assertIn("方法", "\n".join(unit.text for unit in units))
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
        self.assertIn("candidate_text", packet)
        self.assertEqual(packet["candidate_text"], "候选文本")
        self.assertIn("GO or STOP", serialized)
        self.assertNotIn("current_original_unit", serialized)

    def test_long_unheaded_source_does_not_collapse_to_one_unit(self) -> None:
        helper = load_helper()
        source = "\n\n".join(
            f"第{index}段说明同一份长篇科研报告中的证据、限制、比较和下一步实验条件。" * 30
            for index in range(1, 7)
        )
        result = helper.run_multistage(source)
        self.assertGreater(result["receipt"]["unit_count"], 1)

    def test_dataflow_validation_rejects_unused_or_dangling_model_output(self) -> None:
        helper = load_helper()
        unused = {
            "stage_records": [
                {"stage_id": "document-map", "model_call": True, "unused_output": True, "terminal_output": False, "downstream_consumers": []}
            ]
        }
        dangling = {
            "stage_records": [
                {
                    "stage_id": "document-map",
                    "model_call": True,
                    "unused_output": False,
                    "terminal_output": False,
                    "downstream_consumers": [{"stage_id": "missing-stage", "input_binding": "document_map"}],
                }
            ]
        }
        self.assertFalse(helper.validate_dataflow(unused)["ok"])
        self.assertFalse(helper.validate_dataflow(dangling)["ok"])

    def test_malformed_meaning_card_fails_closed(self) -> None:
        helper = load_helper()
        original = helper.call_openai_text

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            if "Create a structured Meaning Card" in prompt:
                return json.dumps({"unit_id": "unit-001"}, ensure_ascii=False)
            return structured_stage_response(prompt, source)

        helper.call_openai_text = fake_call
        try:
            with self.assertRaisesRegex(RuntimeError, "meaning-card"):
                helper.run_multistage("CARE 在 2026-08-28 的 Dice=0.81。", driver="openai-responses", model="test-model", api_key="test-key")
        finally:
            helper.call_openai_text = original

    def test_document_map_and_meaning_card_are_consumed_by_writer_packet(self) -> None:
        helper = load_helper()
        original = helper.call_openai_text

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            return structured_stage_response(prompt, source)

        helper.call_openai_text = fake_call
        try:
            with tempfile.TemporaryDirectory() as tmp:
                result = helper.run_multistage(
                    "CARE 在 2026-08-28 的 Dice=0.81；下一步比较 FedFisher 和 FedLPA。",
                    driver="openai-responses",
                    model="test-model",
                    api_key="test-key",
                    stage_dir=Path(tmp),
                )
                packet = result["packets"][0]
                self.assertIn("自定义核心问题", packet["compact_document_map"]["core_research_question"])
                self.assertIn("自定义普通含义", packet["meaning_card"]["plain_meaning"])
                self.assertIn("source_propositions", packet)
        finally:
            helper.call_openai_text = original

    def test_meaning_card_runtime_completes_missing_proposition_bindings(self) -> None:
        helper = load_helper()
        unit = helper.split_markdown_units(
            "# 结果\n\nCARE 在 2026-08-28 的 Dice=0.81。下一步比较 FedFisher 和 FedLPA。"
        )[0]
        props = helper.proposition_inventory(unit)
        self.assertGreaterEqual(len(props), 2)
        first_prop = props[0]["proposition_id"]
        card = helper.normalize_meaning_card(
            {
                "unit_id": unit.unit_id,
                "reader_job": "解释当前证据和下一步判断",
                "plain_meaning": "先说明结论，再保留必要技术边界。",
                "claims": [
                    {
                        "normalized_meaning": "模型只绑定了第一条命题。",
                        "source_span_ids": unit.source_span_ids,
                        "source_proposition_ids": [first_prop],
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
                "literal_items": [],
                "relocatable_trace_items": [],
                "relation_to_previous": "承接前文",
                "relation_to_next": "引出后文",
                "rewrite_problem": "workflow-language",
                "discourse_function": "result-interpretation",
                "reader_takeaway": "读者应理解判断含义",
            },
            unit,
            props,
        )
        self.assertIn("runtime_completed_missing_proposition_ids", card)
        self.assertFalse(set(prop["proposition_id"] for prop in props) - helper._collect_card_proposition_ids(card))

    def test_openai_driver_makes_observable_stage_calls(self) -> None:
        helper = load_helper()
        calls = []
        original = helper.call_openai_text

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            calls.append({"prompt": prompt, "source": source, "kwargs": kwargs})
            return structured_stage_response(prompt, source)

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
            return structured_stage_response(prompt, source, omit_writer_literals=True)

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
        self.assertTrue(any("-targeted-repair-" in item["stage_id"] for item in receipt["stage_records"]))
        self.assertTrue(any("-post-repair-audit-" in item["stage_id"] for item in receipt["stage_records"]))

    def test_openai_driver_allows_three_unit_semantic_repair_rounds(self) -> None:
        helper = load_helper()
        original = helper.call_openai_text
        semantic_audits = 0

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            nonlocal semantic_audits
            if "Audit semantic preservation" in prompt or "Re-audit semantic preservation" in prompt:
                semantic_audits += 1
                if semantic_audits < 4:
                    return json.dumps(
                        {
                            "decision": "REVISE",
                            "findings": [
                                {
                                    "proposition_id": "unit-001-prop-001",
                                    "status": "omitted",
                                    "source_span_ids": [],
                                    "candidate_evidence": "candidate still hides a decision condition",
                                    "severity": "critical",
                                    "repair_instruction": "restore the missing decision condition",
                                }
                            ],
                        },
                        ensure_ascii=False,
                    )
                return json.dumps({"decision": "PASS", "findings": []}, ensure_ascii=False)
            return structured_stage_response(prompt, source)

        helper.call_openai_text = fake_call
        try:
            result = helper.run_multistage(
                "# 决策\n\n下一轮必须同时比较 pooled、local-only、FedAvg、FedFisher 和 FedLPA；只有 pooled gap 缩小且 drift 受控才 GO，否则 STOP。",
                driver="openai-responses",
                model="test-model",
                api_key="test-key",
            )
        finally:
            helper.call_openai_text = original

        receipt = result["receipt"]
        stage_ids = [item["stage_id"] for item in receipt["stage_records"]]
        self.assertTrue(any(stage_id.endswith("-targeted-repair-3") for stage_id in stage_ids))
        self.assertTrue(any(stage_id.endswith("-post-repair-audit-3") for stage_id in stage_ids))
        self.assertGreaterEqual(semantic_audits, 4)
        self.assertTrue(receipt["dataflow_validation"]["ok"])

    def test_openai_driver_repairs_final_assembly_revise_once(self) -> None:
        helper = load_helper()
        original = helper.call_openai_text
        assembly_reviews = 0

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            nonlocal assembly_reviews
            if "Check final assembly coherence" in prompt:
                assembly_reviews += 1
                if assembly_reviews == 1:
                    return json.dumps(
                        {
                            "decision": "REVISE",
                            "findings": [
                                {
                                    "finding_id": "assembly-001",
                                    "unit_id": "",
                                    "category": "transition",
                                    "repair_instruction": "add a clearer transition between evidence and next-step decision",
                                }
                            ],
                        },
                        ensure_ascii=False,
                    )
                return json.dumps({"decision": "PASS", "findings": []}, ensure_ascii=False)
            if "Repair the assembled candidate only" in prompt:
                payload = json.loads(source)
                return json.dumps(
                    {
                        "reader_core": payload["assembled_reader_core"] + "\n\n因此，下一步判断应接在现有证据边界之后。",
                        "technical_trace": payload["assembled_technical_trace"],
                        "applied_finding_ids": ["assembly-001"],
                        "touched_unit_ids": [],
                    },
                    ensure_ascii=False,
                )
            return structured_stage_response(prompt, source)

        helper.call_openai_text = fake_call
        try:
            result = helper.run_multistage(
                "# 结果\n\nCARE 在 2026-08-28 的 Dice=0.81。\n\n## 下一步\n\n下一轮比较 FedFisher 和 FedLPA。",
                driver="openai-responses",
                model="test-model",
                api_key="test-key",
            )
        finally:
            helper.call_openai_text = original

        receipt = result["receipt"]
        stage_ids = [item["stage_id"] for item in receipt["stage_records"]]
        self.assertIn("final-assembly-targeted-repair", stage_ids)
        self.assertIn("final-assembly-coherence-rerun", stage_ids)
        self.assertEqual(assembly_reviews, 2)
        self.assertTrue(receipt["dataflow_validation"]["ok"])

    def test_openai_driver_repairs_final_assembly_three_times(self) -> None:
        helper = load_helper()
        original = helper.call_openai_text
        assembly_reviews = 0
        assembly_repairs = 0

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            nonlocal assembly_reviews, assembly_repairs
            if "Check final assembly coherence" in prompt:
                assembly_reviews += 1
                if assembly_reviews < 4:
                    return json.dumps(
                        {
                            "decision": "REVISE",
                            "findings": [
                                {
                                    "finding_id": f"assembly-{assembly_reviews:03d}",
                                    "unit_id": "",
                                    "category": "transition",
                                    "repair_instruction": "tighten the transition without changing facts",
                                }
                            ],
                        },
                        ensure_ascii=False,
                    )
                return json.dumps({"decision": "PASS", "findings": []}, ensure_ascii=False)
            if "Repair the assembled candidate only" in prompt:
                assembly_repairs += 1
                payload = json.loads(source)
                return json.dumps(
                    {
                        "reader_core": payload["assembled_reader_core"] + f"\n\n组装修复第 {assembly_repairs} 轮保持原有事实，只改衔接。",
                        "technical_trace": payload["assembled_technical_trace"],
                        "applied_finding_ids": [f"assembly-{assembly_repairs:03d}"],
                        "touched_unit_ids": [],
                    },
                    ensure_ascii=False,
                )
            return structured_stage_response(prompt, source)

        helper.call_openai_text = fake_call
        try:
            result = helper.run_multistage(
                "# 结果\n\nCARE 在 2026-08-28 的 Dice=0.81。\n\n## 下一步\n\n下一轮比较 FedFisher 和 FedLPA。",
                driver="openai-responses",
                model="test-model",
                api_key="test-key",
            )
        finally:
            helper.call_openai_text = original

        receipt = result["receipt"]
        stage_ids = [item["stage_id"] for item in receipt["stage_records"]]
        self.assertIn("final-assembly-targeted-repair-3", stage_ids)
        self.assertIn("final-assembly-coherence-rerun-3", stage_ids)
        self.assertEqual(assembly_reviews, 4)
        self.assertEqual(assembly_repairs, 3)
        self.assertTrue(receipt["dataflow_validation"]["ok"])

    def test_openai_driver_routes_unresolved_assembly_findings_to_human_gate(self) -> None:
        helper = load_helper()
        original = helper.call_openai_text
        assembly_reviews = 0
        assembly_repairs = 0

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            nonlocal assembly_reviews, assembly_repairs
            if "Check final assembly coherence" in prompt:
                assembly_reviews += 1
                return json.dumps(
                    {
                        "decision": "REVISE",
                        "findings": [
                            {
                                "finding_id": f"assembly-{assembly_reviews:03d}",
                                "unit_id": "",
                                "category": "transition",
                                "repair_instruction": "tighten the transition without changing facts",
                            }
                        ],
                    },
                    ensure_ascii=False,
                )
            if "Repair the assembled candidate only" in prompt:
                assembly_repairs += 1
                payload = json.loads(source)
                finding_ids = [item["finding_id"] for item in payload["assembly_findings"]]
                return json.dumps(
                    {
                        "reader_core": payload["assembled_reader_core"] + f"\n\n组装修复第 {assembly_repairs} 轮保持原有事实。",
                        "technical_trace": payload["assembled_technical_trace"],
                        "applied_finding_ids": finding_ids,
                        "touched_unit_ids": [],
                    },
                    ensure_ascii=False,
                )
            return structured_stage_response(prompt, source)

        helper.call_openai_text = fake_call
        try:
            result = helper.run_multistage(
                "# 结果\n\nCARE 在 2026-08-28 的 Dice=0.81。\n\n## 下一步\n\n下一轮比较 FedFisher 和 FedLPA。",
                driver="openai-responses",
                model="test-model",
                api_key="test-key",
            )
        finally:
            helper.call_openai_text = original

        receipt = result["receipt"]
        stage_ids = [item["stage_id"] for item in receipt["stage_records"]]
        self.assertIn("final-assembly-human-style-gate-adjudication", stage_ids)
        self.assertEqual(assembly_reviews, 4)
        self.assertEqual(assembly_repairs, 3)
        self.assertTrue(receipt["dataflow_validation"]["ok"])

    def test_reader_repair_gets_semantic_targeted_retry(self) -> None:
        helper = load_helper()
        original = helper.call_openai_text

        def coverage_ids(payload: dict[str, object]) -> list[str]:
            card = payload.get("meaning_card", {})
            if not isinstance(card, dict):
                return []
            return sorted(
                {
                    str(prop_id)
                    for field in [
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
                    for item in card.get(field, [])
                    for prop_id in item.get("source_proposition_ids", [])
                }
            )

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            if "Review only the candidate text" in prompt:
                return json.dumps(
                    {
                        "decision": "REVISE",
                        "questions": [{"answerable": False, "inferred_answer": "需要补清楚下一步判断。"}],
                        "findings": [
                            {
                                "finding_id": "reader-001",
                                "unit_id": "unit-001",
                                "category": "unclear_decision",
                                "repair_instruction": "make the current conclusion strength explicit",
                            }
                        ],
                    },
                    ensure_ascii=False,
                )
            if "Re-review only the repaired candidate text" in prompt:
                return json.dumps({"decision": "PASS", "questions": [{"answerable": True, "inferred_answer": "判断已清楚。"}], "findings": []}, ensure_ascii=False)
            if "Repair this unit only for reader effort" in prompt:
                payload = json.loads(source)
                return json.dumps(
                    {
                        "reader_core": payload["unit"]["text"],
                        "technical_trace": "",
                        "source_coverage_ids": coverage_ids(payload),
                        "relocated_trace_ids": [],
                    },
                    ensure_ascii=False,
                )
            if "Audit semantic preservation after reader-targeted repair" in prompt:
                payload = json.loads(source)
                prop_id = payload["meaning_card"]["claims"][0]["source_proposition_ids"][0]
                return json.dumps(
                    {"decision": "REVISE", "findings": [{"status": "omitted", "proposition_id": prop_id, "severity": "critical"}]},
                    ensure_ascii=False,
                )
            if "Repair this unit only for semantic preservation" in prompt:
                payload = json.loads(source)
                return json.dumps(
                    {
                        "reader_core": payload["unit"]["text"],
                        "technical_trace": "",
                        "source_coverage_ids": coverage_ids(payload),
                        "relocated_trace_ids": [],
                    },
                    ensure_ascii=False,
                )
            if "Re-audit semantic preservation after the reader semantic repair" in prompt:
                return json.dumps({"decision": "PASS", "findings": []}, ensure_ascii=False)
            return structured_stage_response(prompt, source)

        helper.call_openai_text = fake_call
        try:
            result = helper.run_multistage(
                "# 结论\n\nCARE 在 2026-08-28 的 Dice=0.81 只支持继续验证。\n\n## 下一步\n\n下一轮比较 FedFisher 和 FedLPA。",
                driver="openai-responses",
                model="test-model",
                api_key="test-key",
            )
        finally:
            helper.call_openai_text = original

        stage_ids = [item["stage_id"] for item in result["receipt"]["stage_records"]]
        self.assertTrue(any("reader-semantic-targeted-repair" in stage_id for stage_id in stage_ids))
        self.assertTrue(any("reader-semantic-repair-audit" in stage_id for stage_id in stage_ids))
        self.assertTrue(result["receipt"]["dataflow_validation"]["ok"])

    def test_noncritical_semantic_revision_does_not_force_hard_repair(self) -> None:
        helper = load_helper()
        original = helper.call_openai_text

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            if "Audit semantic preservation" in prompt:
                payload = json.loads(source)
                prop_id = payload["meaning_card"]["claims"][0]["source_proposition_ids"][0]
                return json.dumps(
                    {"decision": "REVISE", "findings": [{"status": "narrowed", "proposition_id": prop_id, "severity": "minor"}]},
                    ensure_ascii=False,
                )
            return structured_stage_response(prompt, source)

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

        stage_ids = [item["stage_id"] for item in result["receipt"]["stage_records"]]
        self.assertFalse(any("-targeted-repair-" in stage_id for stage_id in stage_ids))
        self.assertTrue(result["receipt"]["dataflow_validation"]["ok"])

    def test_exact_literal_restoration_runs_after_model_repair_omits_literal(self) -> None:
        helper = load_helper()
        original = helper.call_openai_text

        def fake_call(prompt: str, source: str, **kwargs: object) -> str:
            if "Rewrite only the current argument unit" in prompt or "Repair only the current rewritten unit" in prompt:
                payload = json.loads(source)
                coverage = [item["proposition_id"] for item in payload.get("source_propositions", [])]
                if not coverage:
                    coverage = sorted(
                        {
                            str(prop_id)
                            for field in [
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
                            for item in payload.get("meaning_card", {}).get(field, [])
                            for prop_id in item.get("source_proposition_ids", [])
                        }
                    )
                return json.dumps(
                    {"reader_core": "CARE 的结果需要解释。", "technical_trace": "", "source_coverage_ids": coverage, "relocated_trace_ids": []},
                    ensure_ascii=False,
                )
            return structured_stage_response(prompt, source)

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

        self.assertIn("2026-08-28", result["candidate"])
        self.assertIn("0.81", result["candidate"])
        self.assertTrue(any("-exact-literal-restoration-" in item["stage_id"] for item in result["receipt"]["stage_records"]))
        self.assertTrue(result["receipt"]["dataflow_validation"]["ok"], result["receipt"]["dataflow_validation"])

    def test_semantic_audit_status_aliases_are_canonicalized_conservatively(self) -> None:
        helper = load_helper()
        unit = helper.RewriteUnit(
            unit_id="unit-001",
            heading="# 结果",
            text="CARE 在 2026-08-28 的 Dice=0.81。",
            start_line=1,
            end_line=1,
            literal_invariants=[],
            source_span_ids=["span-001"],
            argument_role="result-interpretation",
            why_these_spans_belong_together="single result unit",
        )
        propositions = helper.proposition_inventory(unit)
        raw = {
            "decision": "REVISE",
            "findings": [
                {"status": "missing", "proposition_id": propositions[0]["proposition_id"], "severity": "critical"},
                {"status": "partially-preserved", "proposition_id": propositions[0]["proposition_id"], "severity": "minor"},
            ],
        }
        normalized = helper.normalize_semantic_audit(raw, unit, propositions)
        self.assertEqual([item["status"] for item in normalized["findings"]], ["omitted", "narrowed"])
        self.assertEqual(normalized["critical_violation_count"], 1)
        with self.assertRaisesRegex(RuntimeError, "status is invalid"):
            helper.normalize_semantic_audit({"decision": "PASS", "findings": [{"status": "unclear"}]}, unit, propositions)

    def test_response_schema_name_is_bounded_and_stable(self) -> None:
        helper = load_helper()
        stage = "u1_route_revision_and_initial_assessment-post-repair-semantic-audit"
        name = helper.response_schema_name(stage)
        self.assertLessEqual(len(name), 64)
        self.assertEqual(name, helper.response_schema_name(stage))
        self.assertRegex(name, r"^[A-Za-z0-9_-]+$")


if __name__ == "__main__":
    unittest.main()
