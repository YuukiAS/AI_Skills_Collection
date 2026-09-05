from __future__ import annotations

import importlib.util
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / "skills/writing/core/scientific-rewrite"
HELPER_PATH = SKILL_ROOT / "scripts/rewrite_support.py"
CLEAN_REPLAY_DISALLOWED_INPUT_PATTERNS = [
    r"PLAN\.md",
    r"REQUEST\.md",
    r"CURRENT\.json",
    r"RESULT\.md",
    r"STYLE_REJECT",
    r"ROUND3_PROCESS_DIAGNOSIS",
    r"ROUND4_CLEAN_REPLAY_AND_OBSERVABILITY_CONTRACT",
    r"previous",
    r"candidate",
    r"manifest",
    r"checkpoint-",
    r"method-comparison-",
    r"next-experiment",
    r"expected",
    r"vocabulary",
]


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


def local_chinese_context(candidate: str, span: dict) -> str:
    before = candidate[max(0, int(span["start"]) - 36) : int(span["start"])]
    after = candidate[int(span["end"]) : min(len(candidate), int(span["end"]) + 36)]
    for local in (after, before):
        match = re.search(r"[\u4e00-\u9fff]{2,}", local)
        if match:
            return match.group(0)
    return "局部中文解释"


def reader_pass_shell(helper, candidate: str, classifications: dict[str, list[dict]], *, pre_candidate: str | None = None) -> dict:
    pre = pre_candidate if pre_candidate is not None else candidate
    return {
        "schema": "SCIENTIFIC_REWRITE_CHINESE_READER_PASS_V1",
        "source_visible": False,
        "pre_candidate_sha256": helper.sha256_text(pre),
        "final_candidate_sha256": helper.sha256_text(candidate),
        "candidate_sha256": helper.sha256_text(pre),
        "decision": "PASS",
        "answerability": {
            "decision": "PASS",
            "reader_questions_answered": True,
        },
        "reader_effort": {
            "decision": "PASS",
            "minimum_reader_inference_burden": True,
            "not_compression_metric": True,
        },
        "english_span_classification": classifications,
        "information_shape_check": {"decision": "PASS"},
        "formula_context_check": {"decision": "PASS"},
        "epistemic_boundary_check": {"decision": "PASS"},
    }


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
        "reader_questions": ["当前证据支持什么判断，下一步怎样验证？"],
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
    reader_plan = {
        "schema": "SCIENTIFIC_REWRITE_HOST_READER_PLAN_V1",
        "document_map_sha256": document_map_sha,
        "reader_questions": [
            {
                "id": "rq-001",
                "question": "当前证据支持什么判断，下一步怎样验证？",
                "purpose": "让读者先理解问题、证据和边界。",
            }
        ],
        "bundle_order": [f"bundle-{index:03d}" for index, _unit in enumerate(units, start=1)],
        "bundles": [
            {
                "bundle_id": f"bundle-{index:03d}",
                "reader_question": "这个单元回答当前证据、限制或下一步判断中的哪一部分？",
                "unit_ids": [unit.unit_id],
                "source_span_ids": unit.source_span_ids,
                "information_shape": "prose",
                "reader_effort_action": "保持为连贯解释；本 fixture 不需要改变信息形态。",
                "expansion_policy": "same",
            }
            for index, unit in enumerate(units, start=1)
        ],
        "english_span_policy": {
            "exact_identity": ["FedFisher", "FedLPA"],
            "useful_recognition": [],
            "ordinary_reasoning": ["reader effort"],
        },
    }
    write_json(stage_dir / "reader_plan.json", reader_plan)
    write_json(stage_dir / "argument_units.json", {"schema": "SCIENTIFIC_REWRITE_ARGUMENT_UNITS_V1", "units": public_units})
    write_json(stage_dir / "selected_transformations.json", selected)
    write_json(stage_dir / "fidelity_ledger.json", {"schema": "SCIENTIFIC_REWRITE_FIDELITY_LEDGER_V1", "literal_invariants": all_literals})
    (stage_dir / "semantic_audits").mkdir(exist_ok=True)
    for audit in unit_audits:
        write_json(
            stage_dir / "semantic_audits" / f"{audit['unit_id']}.json",
            {
                "schema": "SCIENTIFIC_REWRITE_UNIT_SEMANTIC_AUDIT_V1",
                "unit_id": audit["unit_id"],
                "decision": audit["decision"],
                "candidate_unit_sha256": audit["candidate_unit_sha256"],
                "findings": audit["findings"],
            },
        )
    write_json(
        stage_dir / "self_audit.json",
        {
            "schema": "SCIENTIFIC_REWRITE_HOST_SELF_AUDIT_V1",
            "decision": decision,
            "final_candidate_sha256": helper.sha256_text(final_candidate),
            "unit_audits": unit_audits,
        },
    )
    write_json(
        stage_dir / "final_assembly.json",
        {
            "schema": "SCIENTIFIC_REWRITE_FINAL_ASSEMBLY_V1",
            "assembled_candidate_sha256": helper.sha256_text(final_candidate),
            "final_candidate_sha256": helper.sha256_text(final_candidate),
            "source_unit_order": [unit.unit_id for unit in units],
            "planned_reader_order": [unit.unit_id for unit in units],
            "reader_order_unit_ids": [unit.unit_id for unit in units],
            "reader_plan_consumed": True,
            "strategy": "按读者问题组织；本 fixture 不需要改变源顺序。",
            "information_shape_decisions": [
                {
                    "unit_id": unit.unit_id,
                    "shape": "prose",
                    "effect_on_final": "保持为连贯解释。",
                }
                for unit in units
            ],
        },
    )
    (stage_dir / "assembled_candidate_before_chinese_pass.md").write_text(final_candidate, encoding="utf-8")
    latin_inventory = helper.enumerate_latin_spans(final_candidate)
    write_json(stage_dir / "latin_span_inventory.json", latin_inventory)
    exact_literal_shas = {item["sha256"] for item in all_literals}
    exact_classifications = []
    useful_classifications = []
    for span in latin_inventory["spans"]:
        if span["text_sha256"] in exact_literal_shas:
            exact_classifications.append(
                {
                    "occurrence_id": span["occurrence_id"],
                    "reason": "测试 fixture 中该英文是源文精确身份。",
                    "identity_category": "formal_name",
                }
            )
        else:
            useful_classifications.append(
                {
                    "occurrence_id": span["occurrence_id"],
                    "reason": "测试 fixture 中该英文仅作为首用识别桥。",
                    "chinese_context": local_chinese_context(final_candidate, span),
                }
            )
    write_json(
        stage_dir / "chinese_reader_pass.json",
        reader_pass_shell(
            helper,
            final_candidate,
            {
                "exact_identity": exact_classifications,
                "useful_recognition": useful_classifications,
                "ordinary_reasoning": [],
            },
        )
        | {"decision": decision},
    )
    write_json(
        stage_dir / "post_chinese_self_audit.json",
        {
            "schema": "SCIENTIFIC_REWRITE_POST_CHINESE_SELF_AUDIT_V1",
            "final_candidate_sha256": helper.sha256_text(final_candidate),
            "exact_verification_decision": decision,
            "semantic_verification_decision": decision,
            "reader_effort_decision": decision,
        },
    )
    (stage_dir / "final_candidate.md").write_text(final_candidate, encoding="utf-8")
    return stage_dir


class ScientificRewriteTests(unittest.TestCase):
    def validate_clean_plugin_replay_run(
        self,
        run: dict,
        *,
        expected_plugin: str,
        expected_task_sha256: str,
        expected_source_sha256: str,
    ) -> dict:
        if run.get("plugin") != expected_plugin:
            raise RuntimeError("clean replay plugin id mismatch")
        if run.get("status") != "completed" or run.get("exit_code") != 0:
            raise RuntimeError("clean replay did not complete successfully")
        if not run.get("plugin_check", {}).get("installed"):
            raise RuntimeError("clean replay plugin was not installed")
        child_argv = [str(item) for item in run.get("child_argv", [])]
        if "--ephemeral" not in child_argv:
            raise RuntimeError("clean replay child must be ephemeral")
        if "--disable" not in child_argv or "memories" not in child_argv:
            raise RuntimeError("clean replay child must disable memories")
        joined_argv = "\n".join(child_argv)
        if "sandbox_workspace_write.network_access=false" not in joined_argv:
            raise RuntimeError("clean replay child must disable network access")
        write_isolation = run.get("write_isolation", {})
        if write_isolation.get("status") != "passed" or write_isolation.get("canary_changed") is not False:
            raise RuntimeError("clean replay write isolation did not pass")

        inputs = run.get("inputs")
        if not isinstance(inputs, list) or len(inputs) != 2:
            raise RuntimeError("clean replay must stage exactly TASK + SOURCE")
        roles = [str(item.get("role")) for item in inputs]
        if roles != ["task", "input"]:
            raise RuntimeError("clean replay staged roles must be task,input")
        shas = [str(item.get("sha256")) for item in inputs]
        if shas != [expected_task_sha256, expected_source_sha256]:
            raise RuntimeError("clean replay staged SHA256 values mismatch")

        staged_names = [Path(str(item.get("staged_path", item.get("basename", "")))).name for item in inputs]
        staged_names.extend(str(item.get("basename", "")) for item in inputs)
        for name in staged_names:
            for pattern in CLEAN_REPLAY_DISALLOWED_INPUT_PATTERNS:
                if re.search(pattern, name, flags=re.IGNORECASE):
                    raise RuntimeError(f"clean replay staged disallowed input metadata: {name}")
        return {
            "ok": True,
            "plugin": expected_plugin,
            "run_id": run.get("run_id"),
            "staged_file_count": len(inputs),
            "staged_roles": roles,
            "staged_basenames": [str(item.get("basename")) for item in inputs],
            "task_sha256": expected_task_sha256,
            "source_sha256": expected_source_sha256,
            "ephemeral": True,
            "memories_disabled": True,
            "network_disabled": True,
            "write_isolation_status": write_isolation.get("status"),
            "strict_read_isolation": run.get("filesystem_read_scope", {}).get("strict_read_isolation"),
        }

    def clean_replay_run(self, helper, **overrides):
        task_sha = helper.sha256_text("clean task")
        source_sha = helper.sha256_text("private source")
        run = {
            "plugin": "writing-style@yuukias-ai-skills",
            "run_id": "20260904T000000Z-test",
            "status": "completed",
            "exit_code": 0,
            "plugin_check": {"checked": True, "installed": True},
            "child_argv": [
                "codex",
                "exec",
                "-c",
                "sandbox_workspace_write.network_access=false",
                "--disable",
                "memories",
                "--ephemeral",
            ],
            "write_isolation": {"status": "passed", "canary_changed": False},
            "filesystem_read_scope": {"strict_read_isolation": False},
            "inputs": [
                {
                    "role": "task",
                    "basename": "CLEAN_PRODUCTION_REPLAY_TASK.md",
                    "sha256": task_sha,
                    "staged_path": "/run/inputs/01_task_CLEAN_PRODUCTION_REPLAY_TASK.md",
                },
                {
                    "role": "input",
                    "basename": "050-clean-A-source.md",
                    "sha256": source_sha,
                    "staged_path": "/run/inputs/02_input_050-clean-A-source.md",
                },
            ],
        }
        run.update(overrides)
        return run, task_sha, source_sha

    def test_clean_plugin_replay_contract_accepts_only_task_and_source(self) -> None:
        helper = load_helper()
        run, task_sha, source_sha = self.clean_replay_run(helper)
        result = self.validate_clean_plugin_replay_run(
            run,
            expected_plugin="writing-style@yuukias-ai-skills",
            expected_task_sha256=task_sha,
            expected_source_sha256=source_sha,
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["staged_file_count"], 2)
        self.assertEqual(result["staged_roles"], ["task", "input"])
        self.assertTrue(result["ephemeral"])
        self.assertTrue(result["memories_disabled"])
        self.assertTrue(result["network_disabled"])

    def test_clean_plugin_replay_contract_rejects_extra_or_role_metadata_inputs(self) -> None:
        helper = load_helper()
        run, task_sha, source_sha = self.clean_replay_run(helper)
        run["inputs"].append(
            {
                "role": "metadata",
                "basename": "checkpoint-method-comparison-manifest.json",
                "sha256": helper.sha256_text("role metadata"),
                "staged_path": "/run/inputs/03_checkpoint-method-comparison-manifest.json",
            }
        )
        with self.assertRaisesRegex(RuntimeError, "exactly TASK \\+ SOURCE"):
            self.validate_clean_plugin_replay_run(
                run,
                expected_plugin="writing-style@yuukias-ai-skills",
                expected_task_sha256=task_sha,
                expected_source_sha256=source_sha,
            )
        run, task_sha, source_sha = self.clean_replay_run(helper)
        run["inputs"][1]["basename"] = "050-clean-A-source-next-experiment.md"
        with self.assertRaisesRegex(RuntimeError, "disallowed input metadata"):
            self.validate_clean_plugin_replay_run(
                run,
                expected_plugin="writing-style@yuukias-ai-skills",
                expected_task_sha256=task_sha,
                expected_source_sha256=source_sha,
            )

    def test_clean_plugin_replay_contract_rejects_previous_candidate_and_rejection_analysis(self) -> None:
        helper = load_helper()
        for basename in ["previous_candidate.md", "STYLE_REJECT_ANALYSIS_2026-09-04.md"]:
            run, task_sha, source_sha = self.clean_replay_run(helper)
            run["inputs"][1]["basename"] = basename
            with self.assertRaisesRegex(RuntimeError, "disallowed input metadata"):
                self.validate_clean_plugin_replay_run(
                    run,
                    expected_plugin="writing-style@yuukias-ai-skills",
                    expected_task_sha256=task_sha,
                    expected_source_sha256=source_sha,
                )

    def test_clean_plugin_replay_contract_requires_ephemeral_memoryless_networkless_child(self) -> None:
        helper = load_helper()
        run, task_sha, source_sha = self.clean_replay_run(helper)
        run["child_argv"] = ["codex", "exec", "--ephemeral"]
        with self.assertRaisesRegex(RuntimeError, "disable memories"):
            self.validate_clean_plugin_replay_run(
                run,
                expected_plugin="writing-style@yuukias-ai-skills",
                expected_task_sha256=task_sha,
                expected_source_sha256=source_sha,
            )
        run, task_sha, source_sha = self.clean_replay_run(helper)
        run["child_argv"] = ["codex", "exec", "--disable", "memories", "--ephemeral"]
        with self.assertRaisesRegex(RuntimeError, "disable network"):
            self.validate_clean_plugin_replay_run(
                run,
                expected_plugin="writing-style@yuukias-ai-skills",
                expected_task_sha256=task_sha,
                expected_source_sha256=source_sha,
            )

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
        self.assertIn("renv", all_invariants)
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
            "# 结果\n\nCARE 在 2026-08-28 的 Dice=0.81，检查点路径见 /tmp/run/checkpoint.pt。\n\n"
            "下一步比较 FedFisher 和 FedLPA；如果汇总差距（pooled gap）表示的整体差距下降就是 GO，否则 STOP。"
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
        self.assertTrue(receipt["reader_plan"]["ok"])
        self.assertTrue(receipt["global_assembly"]["ok"])
        self.assertTrue(receipt["chinese_reader_pass"]["ok"])
        self.assertTrue(receipt["exact_verification"]["ok"])
        serialized = json.dumps(receipt, ensure_ascii=False)
        self.assertNotIn(source, serialized)
        self.assertNotIn("candidate_text", serialized)

    def test_reader_plan_is_required_and_consumed_by_global_assembly(self) -> None:
        helper = load_helper()
        source = "## 问题\n\n第一段定义问题。\n\n## 结论\n\n第二段给出结论。"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            (stage_dir / "reader_plan.json").unlink()
            with self.assertRaisesRegex(RuntimeError, "reader_plan.json"):
                helper.validate_host_stage_package(source, stage_dir)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            final_assembly = json.loads((stage_dir / "final_assembly.json").read_text(encoding="utf-8"))
            final_assembly["reader_order_unit_ids"] = list(reversed(final_assembly["reader_order_unit_ids"]))
            write_json(stage_dir / "final_assembly.json", final_assembly)
            with self.assertRaisesRegex(RuntimeError, "reader_plan bundle order"):
                helper.validate_host_stage_package(source, stage_dir)

    def test_chinese_reader_pass_is_candidate_only_and_checks_reader_effort(self) -> None:
        helper = load_helper()
        source = "这段说明一个科学判断。"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            chinese_pass = json.loads((stage_dir / "chinese_reader_pass.json").read_text(encoding="utf-8"))
            chinese_pass["source_visible"] = True
            write_json(stage_dir / "chinese_reader_pass.json", chinese_pass)
            with self.assertRaisesRegex(RuntimeError, "candidate-only"):
                helper.validate_host_stage_package(source, stage_dir)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            chinese_pass = json.loads((stage_dir / "chinese_reader_pass.json").read_text(encoding="utf-8"))
            chinese_pass["reader_effort"]["not_compression_metric"] = False
            write_json(stage_dir / "chinese_reader_pass.json", chinese_pass)
            with self.assertRaisesRegex(RuntimeError, "compression"):
                helper.validate_host_stage_package(source, stage_dir)

    def test_latin_span_inventory_ignores_protected_formula_code_paths_and_citations(self) -> None:
        helper = load_helper()
        text = (
            "正文保留 FedFisher 和 reader effort。`code_token` 不算，"
            "$L = pooled gap$ 不算，/tmp/run/output.txt 不算，[12] 不算。"
        )
        inventory = helper.enumerate_latin_spans(text)
        spans = [item["text"] for item in inventory["spans"]]
        self.assertIn("FedFisher", spans)
        self.assertIn("reader effort", spans)
        self.assertNotIn("code_token", spans)
        self.assertNotIn("pooled gap", spans)
        self.assertNotIn("tmp", spans)

    def test_chinese_reader_pass_requires_complete_latin_occurrence_coverage(self) -> None:
        helper = load_helper()
        source = "FedFisher 和 FedLPA 是正式方法名。"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            chinese_pass = json.loads((stage_dir / "chinese_reader_pass.json").read_text(encoding="utf-8"))
            chinese_pass["english_span_classification"]["exact_identity"].pop()
            write_json(stage_dir / "chinese_reader_pass.json", chinese_pass)
            with self.assertRaisesRegex(RuntimeError, "omitted Latin occurrences"):
                helper.validate_host_stage_package(source, stage_dir)

    def test_chinese_reader_pass_rejects_unresolved_ordinary_reasoning(self) -> None:
        helper = load_helper()
        source = "reader effort 是普通解释语言，不应残留。"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            chinese_pass = json.loads((stage_dir / "chinese_reader_pass.json").read_text(encoding="utf-8"))
            first = chinese_pass["english_span_classification"]["useful_recognition"].pop(0)
            chinese_pass["english_span_classification"]["ordinary_reasoning"].append(
                {"occurrence_id": first["occurrence_id"], "reason": "普通组织语言仍未中文化。"}
            )
            write_json(stage_dir / "chinese_reader_pass.json", chinese_pass)
            with self.assertRaisesRegex(RuntimeError, "ordinary_reasoning"):
                helper.validate_host_stage_package(source, stage_dir)

    def test_exact_identity_rejects_arbitrary_authority_but_accepts_protected_name(self) -> None:
        helper = load_helper()
        candidate = "这个段落仍然把 reader effort 当作英文身份。"
        inventory = helper.enumerate_latin_spans(candidate)
        classifications = {
            "exact_identity": [
                {
                    "occurrence_id": inventory["spans"][0]["occurrence_id"],
                    "reason": "不能因为主机声称这是技术术语就保留。",
                    "identity_authority": "host says this is a technical term",
                }
            ],
            "useful_recognition": [],
            "ordinary_reasoning": [],
        }
        with self.assertRaisesRegex(RuntimeError, "deterministic identity support"):
            helper.validate_chinese_reader_pass(
                reader_pass_shell(helper, candidate, classifications),
                candidate,
                latin_inventory=inventory,
                literal_invariants=[],
            )

        candidate = "正式方法 FedFisher 保持英文名。"
        inventory = helper.enumerate_latin_spans(candidate)
        literals = helper.extract_literal_invariants("正式方法 FedFisher 保持英文名。")
        classifications = {
            "exact_identity": [
                {
                    "occurrence_id": inventory["spans"][0]["occurrence_id"],
                    "reason": "FedFisher 是源文保护的正式方法名。",
                    "identity_category": "algorithm/model name",
                }
            ],
            "useful_recognition": [],
            "ordinary_reasoning": [],
        }
        result = helper.validate_chinese_reader_pass(
            reader_pass_shell(helper, candidate, classifications),
            candidate,
            latin_inventory=inventory,
            literal_invariants=literals,
        )
        self.assertEqual(result["exact_identity_count"], 1)

    def test_useful_recognition_requires_present_local_chinese_context(self) -> None:
        helper = load_helper()
        candidate = "第一次说明局部漂移（local drift）表示客户端更新方向偏离共享模型。"
        inventory = helper.enumerate_latin_spans(candidate)
        classifications = {
            "exact_identity": [],
            "useful_recognition": [
                {
                    "occurrence_id": inventory["spans"][0]["occurrence_id"],
                    "reason": "首用英文帮助识别论文常用术语。",
                    "chinese_context": "并不存在的中文解释",
                }
            ],
            "ordinary_reasoning": [],
        }
        with self.assertRaisesRegex(RuntimeError, "local Chinese context"):
            helper.validate_chinese_reader_pass(
                reader_pass_shell(helper, candidate, classifications),
                candidate,
                latin_inventory=inventory,
                literal_invariants=[],
            )

        classifications["useful_recognition"][0]["chinese_context"] = "局部漂移"
        result = helper.validate_chinese_reader_pass(
            reader_pass_shell(helper, candidate, classifications),
            candidate,
            latin_inventory=inventory,
            literal_invariants=[],
        )
        self.assertEqual(result["useful_recognition_first_use_count"], 1)

        weak_candidate = "在严格一次通信条件下，global-vs-personalized estimand 会改变。"
        weak_inventory = helper.enumerate_latin_spans(weak_candidate)
        weak_classifications = {
            "exact_identity": [],
            "useful_recognition": [
                {
                    "occurrence_id": weak_inventory["spans"][0]["occurrence_id"],
                    "reason": "附近有中文但没有解释这个英文项。",
                    "chinese_context": "严格一次通信",
                }
            ],
            "ordinary_reasoning": [],
        }
        with self.assertRaisesRegex(RuntimeError, "local Chinese context"):
            helper.validate_chinese_reader_pass(
                reader_pass_shell(helper, weak_candidate, weak_classifications),
                weak_candidate,
                latin_inventory=weak_inventory,
                literal_invariants=[],
            )

    def test_useful_recognition_first_use_boundary_rejects_repeated_non_identity_english(self) -> None:
        helper = load_helper()
        candidate = "第一次说明局部漂移（local drift）表示偏离共享模型；后文又直接写 local drift 增大。"
        inventory = helper.enumerate_latin_spans(candidate)
        classifications = {
            "exact_identity": [],
            "useful_recognition": [
                {
                    "occurrence_id": span["occurrence_id"],
                    "reason": "错误地把同一非身份英文反复当作有用识别。",
                    "chinese_context": "局部漂移",
                }
                for span in inventory["spans"]
            ],
            "ordinary_reasoning": [],
        }
        with self.assertRaisesRegex(RuntimeError, "repeats non-identity English"):
            helper.validate_chinese_reader_pass(
                reader_pass_shell(helper, candidate, classifications),
                candidate,
                latin_inventory=inventory,
                literal_invariants=[],
            )

        fixed_candidate = "第一次说明局部漂移（local drift）表示偏离共享模型；后文改用局部漂移增大。"
        fixed_inventory = helper.enumerate_latin_spans(fixed_candidate)
        fixed_classifications = {
            "exact_identity": [],
            "useful_recognition": [
                {
                    "occurrence_id": fixed_inventory["spans"][0]["occurrence_id"],
                    "reason": "首用保留英文用于识别，后文使用中文。",
                    "chinese_context": "局部漂移",
                }
            ],
            "ordinary_reasoning": [],
        }
        result = helper.validate_chinese_reader_pass(
            reader_pass_shell(helper, fixed_candidate, fixed_classifications),
            fixed_candidate,
            latin_inventory=fixed_inventory,
            literal_invariants=[],
        )
        self.assertEqual(result["repeated_non_identity_english_violation_count"], 0)

    def test_ordinary_reasoning_repair_requires_post_pass_removal(self) -> None:
        helper = load_helper()
        pre_candidate = "这个段落仍用 reader effort 支撑中文句子。"
        final_candidate = "这个段落改成中文说明读者阅读负担。"
        inventory = helper.enumerate_latin_spans(pre_candidate)
        classifications = {
            "exact_identity": [],
            "useful_recognition": [],
            "ordinary_reasoning": [
                {
                    "occurrence_id": inventory["spans"][0]["occurrence_id"],
                    "reason": "普通推理语言必须中文化。",
                }
            ],
        }
        result = helper.validate_chinese_reader_pass(
            reader_pass_shell(helper, final_candidate, classifications, pre_candidate=pre_candidate),
            final_candidate,
            latin_inventory=inventory,
            literal_invariants=[],
        )
        self.assertEqual(result["ordinary_reasoning_repaired_count"], 1)
        self.assertTrue(result["candidate_changed_by_chinese_pass"])

        with self.assertRaisesRegex(RuntimeError, "ordinary_reasoning Latin occurrence remains unresolved"):
            helper.validate_chinese_reader_pass(
                reader_pass_shell(helper, pre_candidate, classifications),
                pre_candidate,
                latin_inventory=inventory,
                literal_invariants=[],
            )

    def test_noop_chinese_pass_requires_legitimate_surviving_latin(self) -> None:
        helper = load_helper()
        candidate = "正式方法 FedFisher 仍保留英文名。"
        inventory = helper.enumerate_latin_spans(candidate)
        classifications = {
            "exact_identity": [
                {
                    "occurrence_id": inventory["spans"][0]["occurrence_id"],
                    "reason": "FedFisher 是源文保护的正式方法名。",
                    "identity_category": "algorithm/model name",
                }
            ],
            "useful_recognition": [],
            "ordinary_reasoning": [],
        }
        result = helper.validate_chinese_reader_pass(
            reader_pass_shell(helper, candidate, classifications),
            candidate,
            latin_inventory=inventory,
            literal_invariants=helper.extract_literal_invariants(candidate),
        )
        self.assertFalse(result["candidate_changed_by_chinese_pass"])

        bad_candidate = "这个段落仍然保留 reader effort。"
        bad_inventory = helper.enumerate_latin_spans(bad_candidate)
        bad_classifications = {
            "exact_identity": [],
            "useful_recognition": [],
            "ordinary_reasoning": [
                {
                    "occurrence_id": bad_inventory["spans"][0]["occurrence_id"],
                    "reason": "普通推理语言未修。",
                }
            ],
        }
        with self.assertRaisesRegex(RuntimeError, "ordinary_reasoning Latin occurrence remains unresolved"):
            helper.validate_chinese_reader_pass(
                reader_pass_shell(helper, bad_candidate, bad_classifications),
                bad_candidate,
                latin_inventory=bad_inventory,
                literal_invariants=[],
            )

    def test_natural_english_inline_code_cannot_escape_reader_pass(self) -> None:
        helper = load_helper()
        candidate = "这一设置改变了 `global-vs-personalized estimand`，因此需要中文说明。"
        inventory = helper.enumerate_latin_spans(candidate)
        self.assertEqual([span["text"] for span in inventory["spans"]], ["global-vs-personalized estimand"])
        self.assertNotIn(
            "global-vs-personalized estimand",
            [item["text"] for item in helper.extract_literal_invariants(candidate)],
        )
        classifications = {
            "exact_identity": [],
            "useful_recognition": [],
            "ordinary_reasoning": [
                {
                    "occurrence_id": inventory["spans"][0]["occurrence_id"],
                    "reason": "反引号中的自然英文短语仍是读者可见推理语言。",
                }
            ],
        }
        with self.assertRaisesRegex(RuntimeError, "ordinary_reasoning Latin occurrence remains unresolved"):
            helper.validate_chinese_reader_pass(
                reader_pass_shell(helper, candidate, classifications),
                candidate,
                latin_inventory=inventory,
                literal_invariants=[],
            )

    def test_host_stage_rejects_non_deterministic_literal_ledger_entries(self) -> None:
        helper = load_helper()
        source = "正式方法 FedFisher 保持英文名。"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            ledger = json.loads((stage_dir / "fidelity_ledger.json").read_text(encoding="utf-8"))
            ledger["literal_invariants"].append(
                {
                    "text": "reader effort",
                    "sha256": helper.sha256_text("reader effort"),
                    "role": "inline-critical",
                }
            )
            write_json(stage_dir / "fidelity_ledger.json", ledger)
            with self.assertRaisesRegex(RuntimeError, "non-deterministic source identities"):
                helper.validate_host_stage_package(source, stage_dir)

    def test_final_candidate_cannot_add_unclassified_latin_after_chinese_pass(self) -> None:
        helper = load_helper()
        source = "FedFisher 是正式方法名。"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = make_stage_package(helper, root, source)
            final_candidate = (stage_dir / "final_candidate.md").read_text(encoding="utf-8") + "\n\nextra workflow language"
            (stage_dir / "final_candidate.md").write_text(final_candidate, encoding="utf-8")
            self_audit = json.loads((stage_dir / "self_audit.json").read_text(encoding="utf-8"))
            self_audit["final_candidate_sha256"] = helper.sha256_text(final_candidate)
            write_json(stage_dir / "self_audit.json", self_audit)
            final_assembly = json.loads((stage_dir / "final_assembly.json").read_text(encoding="utf-8"))
            final_assembly["final_candidate_sha256"] = helper.sha256_text(final_candidate)
            write_json(stage_dir / "final_assembly.json", final_assembly)
            post = json.loads((stage_dir / "post_chinese_self_audit.json").read_text(encoding="utf-8"))
            post["final_candidate_sha256"] = helper.sha256_text(final_candidate)
            write_json(stage_dir / "post_chinese_self_audit.json", post)
            chinese_pass = json.loads((stage_dir / "chinese_reader_pass.json").read_text(encoding="utf-8"))
            chinese_pass["candidate_sha256"] = helper.sha256_text(final_candidate)
            chinese_pass["final_candidate_sha256"] = helper.sha256_text(final_candidate)
            write_json(stage_dir / "chinese_reader_pass.json", chinese_pass)
            with self.assertRaisesRegex(RuntimeError, "unclassified Latin spans"):
                helper.validate_host_stage_package(source, stage_dir)

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
            reader_plan = json.loads((stage_dir / "reader_plan.json").read_text(encoding="utf-8"))
            reader_plan["bundle_order"] = ["bundle-002", "bundle-001"]
            reader_plan["bundles"] = [
                {
                    "bundle_id": "bundle-001",
                    "reader_question": "问题和结论共同说明什么？",
                    "unit_ids": ["unit-001"],
                    "source_span_ids": ["span-001", "span-003"],
                    "information_shape": "short_list",
                    "reader_effort_action": "把非连续的问题和结论合在同一个读者问题下。",
                    "expansion_policy": "list",
                },
                {
                    "bundle_id": "bundle-002",
                    "reader_question": "限制条件是什么？",
                    "unit_ids": ["unit-002"],
                    "source_span_ids": ["span-002"],
                    "information_shape": "prose",
                    "reader_effort_action": "保留为短段说明。",
                    "expansion_policy": "same",
                },
            ]
            write_json(stage_dir / "reader_plan.json", reader_plan)
            final_assembly = json.loads((stage_dir / "final_assembly.json").read_text(encoding="utf-8"))
            final_assembly["source_unit_order"] = ["unit-001", "unit-002"]
            final_assembly["planned_reader_order"] = ["unit-002", "unit-001"]
            final_assembly["reader_order_unit_ids"] = ["unit-002", "unit-001"]
            write_json(stage_dir / "final_assembly.json", final_assembly)
            result = helper.validate_host_stage_package(source, stage_dir)
        self.assertTrue(result["receipt"]["argument_coverage"]["ok"])
        self.assertEqual(result["receipt"]["reader_plan"]["non_contiguous_bundle_count"], 1)
        self.assertEqual(result["receipt"]["reader_plan"]["information_shape_counts"]["short_list"], 1)
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
        self.assertIn("host-Codex heavy Chinese scientific rewrites", plugin["description"])
        self.assertIn("without changing scientific claims", plugin["description"])
        self.assertNotIn("research-structure decisions", plugin["description"])
        self.assertIn(
            "Rewrite this Chinese scientific report with reader-facing structure while preserving the same evidence graph.",
            plugin["defaultPrompt"],
        )
        sources = {entry["source"]: entry["artifact_id"] for entry in plugin["skills"]}
        self.assertEqual(sources["skills/writing/core/scientific-rewrite"], "scientific-rewrite")
        profile = json.loads((REPO_ROOT / "profiles/codex-writing-style.json").read_text(encoding="utf-8"))
        self.assertIn("host-Codex heavy Chinese scientific rewrites", profile["description"])
        self.assertIn("skills/writing/core/scientific-rewrite", profile["skills"])

    def test_companion_style_skills_define_heavy_rewrite_boundaries(self) -> None:
        chinese = (REPO_ROOT / "skills/writing/core/chinese-prose/SKILL.md").read_text(encoding="utf-8")
        fidelity = (REPO_ROOT / "skills/writing/core/writing-fidelity/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Reader Plan", chinese)
        self.assertIn("公式拆解", chinese)
        self.assertIn("不是候选稿更短", chinese)
        self.assertIn("reader-question bundles", fidelity)
        self.assertIn("non-contiguous source spans", fidelity)
        self.assertIn("not source order or compression", fidelity)

    def test_response_schema_name_is_bounded_and_stable(self) -> None:
        helper = load_helper()
        name = helper.response_schema_name("very long stage name " * 20)
        self.assertLessEqual(len(name), 64)
        self.assertEqual(name, helper.response_schema_name("very long stage name " * 20))


if __name__ == "__main__":
    unittest.main()
