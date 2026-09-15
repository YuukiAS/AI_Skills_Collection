from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
HELPER_PATH = REPO_ROOT / "skills/writing/core/scientific-rewrite/scripts/rewrite_support.py"
GENERATED_HELPER_PATH = (
    REPO_ROOT / "plugins/codex/plugins/writing-style/skills/scientific-rewrite/scripts/rewrite_support.py"
)


def load_helper():
    spec = importlib.util.spec_from_file_location("scientific_rewrite_support", HELPER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


def load_helper_from(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    previous = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec.loader.exec_module(module)
    finally:
        sys.dont_write_bytecode = previous
    return module


helper = load_helper()


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_valid_stage(root: Path) -> tuple[str, Path, dict]:
    source = (
        "FedFisher 在 MMs 数据集上取得 Dice=0.81，但这个结论只覆盖一次通信的设置 [12]。\n\n"
        "CARE 的初步结果来自同一批公开切分，但报告里没有把通信轮数、客户端数量和后处理写在同一个地方。\n\n"
        "公式 $L=L_{seg}+0.2L_{reg}$ 只用于 FedFisher 的消融实验，CARE 没有使用这个正则项。\n\n"
        "复现实验脚本位于 `scripts/run_fedfisher.sh`，配置文件是 `configs/mm_fedfisher.yaml`。"
    )
    prompt = "把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢。"
    anchors = helper.split_source_anchors(source)
    exact_items = helper.extract_exact_items(source)
    exact_ids = [item["exact_item_id"] for item in exact_items]
    route_selection = helper.classify_writing_style_route(prompt, source)
    meaning_map = {
        "schema": helper.MEANING_MAP_SCHEMA,
        "source_sha256": helper.sha256_text(source),
        "source_anchors": anchors,
        "exact_items": exact_items,
        "meanings": [
            {
                "meaning_id": "m-001",
                "kind": "result_with_scope",
                "normalized_meaning": "现有结果说明 FedFisher 在 MMs 上达到 Dice=0.81，证据边界限定为一次通信设置。",
                "source_anchor_ids": ["src-001"],
                "exact_item_ids": [item["exact_item_id"] for item in exact_items if item["literal"] in {"FedFisher", "MMs", "Dice=0.81", "[12]", "0.81", "12"}],
            },
            {
                "meaning_id": "m-002",
                "kind": "condition_alignment",
                "normalized_meaning": "CARE 结果需要和通信轮数、客户端数量、后处理条件一起呈现，避免训练预算比较被误读。",
                "source_anchor_ids": ["src-002"],
                "exact_item_ids": [item["exact_item_id"] for item in exact_items if item["literal"] == "CARE"],
            },
            {
                "meaning_id": "m-003",
                "kind": "formula_scope",
                "normalized_meaning": "损失公式只属于 FedFisher 消融实验，不能写成 CARE 也使用了该正则项。",
                "source_anchor_ids": ["src-003"],
                "exact_item_ids": [item["exact_item_id"] for item in exact_items if item["literal"] in {"$L=L_{seg}+0.2L_{reg}$", "0.2"}],
            },
            {
                "meaning_id": "m-004",
                "kind": "reproduction_trace",
                "normalized_meaning": "脚本和配置路径应保留为复现实验信息，而不是替代主要科学结论。",
                "source_anchor_ids": ["src-004"],
                "exact_item_ids": [item["exact_item_id"] for item in exact_items if item["literal"] in {"scripts/run_fedfisher.sh", "configs/mm_fedfisher.yaml"}],
            },
        ],
        "relations": [
            {
                "from_meaning_id": "m-001",
                "to_meaning_id": "m-002",
                "relation": "sets_comparison_context",
            }
        ],
    }
    reader_plan = {
        "schema": helper.READER_PLAN_SCHEMA,
        "bundle_order": ["bundle-001"],
        "bundles": [
            {
                "bundle_id": "bundle-001",
                "reader_question_id": "rq-001",
                "owned_meaning_ids": ["m-001", "m-002", "m-003", "m-004"],
                "required_exact_item_ids": exact_ids,
                "information_shape": "cohesive_prose",
                "reader_dispositions": [
                    {
                        "meaning_id": "m-001",
                        "disposition": "CORE_INLINE",
                        "source_role": "scoped result",
                        "reader_reason": "读者需要先知道结果和证据边界。",
                    },
                    {
                        "meaning_id": "m-002",
                        "disposition": "SUPPORT_INLINE",
                        "source_role": "comparison condition",
                        "reader_reason": "读者需要理解 CARE 比较的条件约束。",
                    },
                    {
                        "meaning_id": "m-003",
                        "disposition": "STRUCTURED",
                        "source_role": "formula scope",
                        "reader_reason": "公式必须靠近它限定的实验，避免误归因。",
                    },
                    {
                        "meaning_id": "m-004",
                        "disposition": "RELOCATE",
                        "source_role": "reproducibility detail",
                        "reader_reason": "脚本和配置应放入复现实验说明，而不是替代科学结论。",
                    },
                ],
            }
        ],
    }
    realization_packet = {
        "schema": helper.REALIZATION_PACKET_SCHEMA,
        "bundle_id": "bundle-001",
        "audience": "中文科研读者",
        "meaning_records": [
            {"meaning_id": "m-001", "meaning": "报告 FedFisher 在 MMs 上的 Dice=0.81 结果和一次通信限制。"},
            {"meaning_id": "m-002", "meaning": "说明 CARE 比较必须对齐通信轮数、客户端数量和后处理。"},
            {"meaning_id": "m-003", "meaning": "说明 $L=L_{seg}+0.2L_{reg}$ 只属于 FedFisher 消融实验。"},
            {"meaning_id": "m-004", "meaning": "把 scripts/run_fedfisher.sh 和 configs/mm_fedfisher.yaml 放到复现实验说明。"},
        ],
        "required_exact_items": exact_items,
        "information_shape": "cohesive_prose",
        "modality_preservation": {
            "preserve_completion_status": True,
            "preserve_subject_voice": True,
            "preserve_temporal_status": True,
            "preserve_epistemic_status": True,
        },
    }
    final_candidate = (
        "现有证据只支持一个范围很窄的判断：FedFisher 在 MMs 数据集、一次通信设置下达到 "
        "Dice=0.81 [12]。CARE 的比较需要把通信轮数、客户端数量和后处理放在同一段说明。"
        "公式 $L=L_{seg}+0.2L_{reg}$ 只用于 FedFisher 消融实验，不能写成 CARE 使用了同一个正则项。"
        "复现实验脚本是 `scripts/run_fedfisher.sh`，配置文件是 `configs/mm_fedfisher.yaml`。"
    )
    assembly_packet = {
        "schema": helper.ASSEMBLY_PACKET_SCHEMA,
        "reader_plan_sha256": helper.sha256_text(helper.canonical_json(reader_plan)),
        "realized_bundle_sha256s": {"bundle-001": helper.sha256_text(final_candidate)},
        "whole_document_finish": {
            "document_purpose": "解释现有 FedFisher/CARE 结果的可比性和复现边界。",
            "reader_entry": "先给范围化结论，再解释比较条件、公式和复现信息。",
            "section_order_rationale": "单段短文按结论、限制、公式、复现实验顺序组织。",
            "transition_plan": "用条件和归属连接结果、公式与复现信息。",
            "voice_constraints": "保持完成态报告口吻，不写成执行计划。",
            "technical_detail_placement": "脚本和配置放在末尾复现实验说明。",
        },
    }
    semantic_audit = {
        "schema": helper.SEMANTIC_AUDIT_SCHEMA,
        "decision": "PASS",
        "findings": [{"finding_type": "wording", "status": "resolved", "severity": "low"}],
        "reader_disposition_decision": "PASS",
        "reader_disposition_covered_meaning_ids": ["m-001", "m-002", "m-003", "m-004"],
        "reader_disposition_findings": [
            {
                "meaning_id": "m-004",
                "status": "resolved",
                "severity": "low",
                "finding_type": "relocated_reproduction_detail",
            }
        ],
    }
    stage_dir = root / "stage"
    write_json(stage_dir / "route_selection.json", route_selection)
    write_json(stage_dir / "meaning_map.json", meaning_map)
    write_json(stage_dir / "reader_plan.json", reader_plan)
    write_json(stage_dir / "realization_packets/bundle-001.json", realization_packet)
    write_json(stage_dir / "assembly_packet.json", assembly_packet)
    write_json(stage_dir / "semantic_audit.json", semantic_audit)
    (stage_dir / "final_candidate.md").write_text(final_candidate + "\n", encoding="utf-8")
    (root / "prompt.md").write_text(prompt + "\n", encoding="utf-8")
    return source, stage_dir, meaning_map


class ScientificRewriteHeavyRouteTests(unittest.TestCase):
    def test_stage_package_validates_v2_receipt_without_paid_generation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source, stage_dir, _ = build_valid_stage(Path(tmp))
            receipt_path = Path(tmp) / "receipt.json"
            prompt = (Path(tmp) / "prompt.md").read_text(encoding="utf-8").strip()
            receipt = helper.validate_stage_package(source, stage_dir, receipt_path=receipt_path, prompt=prompt)

            self.assertTrue(receipt_path.exists())
            self.assertEqual(receipt["schema"], helper.RUNTIME_SCHEMA)
            self.assertEqual(receipt["runtime"], helper.RUNTIME_NAME)
            self.assertEqual(receipt["route_selection"]["selector_owner"], "writing-style")
            self.assertEqual(receipt["route_selection"]["selected_route"], "scientific-rewrite")
            self.assertTrue(receipt["route_selection"]["ordinary_user_prompt"])
            self.assertTrue(receipt["host_codex_owned_generation"])
            self.assertEqual(receipt["external_api_call_count"], 0)
            self.assertFalse(receipt["requires_openai_api_key"])
            self.assertFalse(receipt["paid_generation_used"])
            self.assertFalse(receipt["source_copy_fallback_used"])
            self.assertFalse(receipt["fixed_size_splitter_used"])
            self.assertFalse(receipt["seed_templates_used_for_realization"])
            self.assertFalse(receipt["private_plaintext_committed"])

    def test_validate_host_stage_cli_writes_route_bound_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, stage_dir, _ = build_valid_stage(root)
            source_path = root / "source.md"
            source_path.write_text(source, encoding="utf-8")
            receipt_path = root / "receipt.json"

            subprocess.run(
                [
                    sys.executable,
                    str(HELPER_PATH),
                    "validate-host-stage",
                    "--source",
                    str(source_path),
                    "--stage-dir",
                    str(stage_dir),
                    "--prompt",
                    str(root / "prompt.md"),
                    "--receipt",
                    str(receipt_path),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            self.assertEqual(receipt["route_selection"]["selected_route"], "scientific-rewrite")

    def test_missing_semantic_extraction_and_direct_source_copy_fail(self) -> None:
        source = "这是第一段。\n\n这是第二段。"
        anchors = helper.split_source_anchors(source)
        payload = {
            "schema": helper.MEANING_MAP_SCHEMA,
            "source_sha256": helper.sha256_text(source),
            "source_anchors": anchors,
            "meanings": [],
        }
        with self.assertRaisesRegex(helper.ValidationError, "requires host-authored meanings"):
            helper.validate_meaning_map(payload, source)

        payload["meanings"] = [
            {
                "meaning_id": "m-001",
                "kind": "claim",
                "normalized_meaning": "这是第一段。",
                "source_anchor_ids": ["src-001"],
                "exact_item_ids": [],
            },
            {
                "meaning_id": "m-002",
                "kind": "claim",
                "normalized_meaning": "第二段说明另一个信息点。",
                "source_anchor_ids": ["src-002"],
                "exact_item_ids": [],
            },
        ]
        with self.assertRaisesRegex(helper.ValidationError, "direct source-copy fallback"):
            helper.validate_meaning_map(payload, source)

    def test_realization_repair_and_assembly_reject_raw_source_leakage(self) -> None:
        realization = {
            "schema": helper.REALIZATION_PACKET_SCHEMA,
            "bundle_id": "bundle-001",
            "meaning_records": [{"meaning_id": "m-001", "source_quote": "原文句子"}],
            "modality_preservation": {
                "preserve_completion_status": True,
                "preserve_subject_voice": True,
                "preserve_temporal_status": True,
                "preserve_epistemic_status": True,
            },
        }
        repair = {
            "schema": helper.REPAIR_PACKET_SCHEMA,
            "bundle_id": "bundle-001",
            "affected_meaning_ids": ["m-001"],
            "required_semantic_correction": "SOURCE: 原文修正",
        }
        assembly = {
            "schema": helper.ASSEMBLY_PACKET_SCHEMA,
            "reader_plan_sha256": "abc",
            "realized_bundle_sha256s": {"bundle-001": "def"},
            "source_text": "原始全文",
            "whole_document_finish": {
                "document_purpose": "purpose",
                "reader_entry": "entry",
                "section_order_rationale": "order",
                "transition_plan": "transitions",
                "voice_constraints": "voice",
                "technical_detail_placement": "appendix",
            },
        }

        with self.assertRaisesRegex(helper.ValidationError, "forbidden raw-source"):
            helper.validate_realization_packet(realization)
        with self.assertRaisesRegex(helper.ValidationError, "source-copy fallback"):
            helper.validate_repair_packet(repair)
        with self.assertRaisesRegex(helper.ValidationError, "forbidden raw-source"):
            helper.validate_assembly_packet(assembly)

    def test_reader_plan_rejects_fixed_splitter_and_omitted_meanings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source, stage_dir, meaning_map = build_valid_stage(Path(tmp))
            helper.validate_meaning_map(meaning_map, source)
            reader_plan = json.loads((stage_dir / "reader_plan.json").read_text(encoding="utf-8"))

            reader_plan["splitter"] = "fixed_chars"
            with self.assertRaisesRegex(helper.ValidationError, "fixed-size splitter"):
                helper.validate_reader_plan(reader_plan, meaning_map)

            reader_plan.pop("splitter")
            reader_plan["bundles"][0]["owned_meaning_ids"] = ["m-001"]
            reader_plan["bundles"][0]["reader_dispositions"] = [
                item for item in reader_plan["bundles"][0]["reader_dispositions"] if item["meaning_id"] == "m-001"
            ]
            with self.assertRaisesRegex(helper.ValidationError, "omits meanings"):
                helper.validate_reader_plan(reader_plan, meaning_map)

    def test_reader_plan_requires_reader_dispositions_for_all_meanings(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source, stage_dir, meaning_map = build_valid_stage(Path(tmp))
            helper.validate_meaning_map(meaning_map, source)
            reader_plan = json.loads((stage_dir / "reader_plan.json").read_text(encoding="utf-8"))

            reader_plan["bundles"][0].pop("reader_dispositions")
            with self.assertRaisesRegex(helper.ValidationError, "lacks reader dispositions"):
                helper.validate_reader_plan(reader_plan, meaning_map)

            reader_plan = json.loads((stage_dir / "reader_plan.json").read_text(encoding="utf-8"))
            reader_plan["bundles"][0]["reader_dispositions"] = reader_plan["bundles"][0]["reader_dispositions"][:-1]
            with self.assertRaisesRegex(helper.ValidationError, "omits reader dispositions"):
                helper.validate_reader_plan(reader_plan, meaning_map)

    def test_source_future_work_disposition_requires_modality_record(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source, stage_dir, meaning_map = build_valid_stage(Path(tmp))
            helper.validate_meaning_map(meaning_map, source)
            reader_plan = json.loads((stage_dir / "reader_plan.json").read_text(encoding="utf-8"))
            reader_plan["bundles"][0]["reader_dispositions"][0] = {
                "meaning_id": "m-001",
                "disposition": "SOURCE_FUTURE_WORK",
                "source_role": "author future work",
                "reader_reason": "读者需要知道 source 作者尚未完成的下一步。",
            }

            with self.assertRaisesRegex(helper.ValidationError, "requires modality record"):
                helper.validate_reader_plan(reader_plan, meaning_map)

    def test_reader_relevance_accounts_irrelevant_source_metadata_without_reader_leakage(self) -> None:
        source = (
            "页面包装：English title = Neural message passing；附带别名 = Pas de message neuronal；"
            "language links = 12；archive oldid = 4321。\n\n"
            "GraphSAGE 通过邻域采样学习节点表示；在 PyTorch Geometric 中可用 "
            "`torch_geometric.nn.SAGEConv` 复现，并常用 ogbn-products 数据集评测。"
        )
        prompt = "把这份中文技术资料重写成独立中文说明，保留算法名、数据集和 API，但网页元数据不要写进正文。"
        anchors = helper.split_source_anchors(source)
        exact_items = helper.extract_exact_items(source)
        exact_items.append(
            {
                "exact_item_id": f"exact-{len(exact_items) + 1:03d}",
                "literal": "ogbn-products",
                "sha256": helper.sha256_text("ogbn-products"),
                "category": "dataset",
                "location_role": "inline-critical",
            }
        )
        required_exact_ids = [
            item["exact_item_id"]
            for item in exact_items
            if item["literal"] in {"GraphSAGE", "PyTorch", "torch_geometric.nn.SAGEConv", "ogbn-products"}
        ]
        meaning_map = {
            "schema": helper.MEANING_MAP_SCHEMA,
            "source_sha256": helper.sha256_text(source),
            "source_anchors": anchors,
            "exact_items": exact_items,
            "source_context_items": [
                {
                    "source_context_item_id": "ctx-001",
                    "source_anchor_ids": ["src-001"],
                    "context_kind": "source_wrapper_metadata",
                    "reader_relevance_decision": "exclude_from_reader_facing_candidate",
                    "rationale": "language links, archive ids, and incidental alternate labels do not help a standalone Chinese technical reader understand or reproduce the method.",
                }
            ],
            "meanings": [
                {
                    "meaning_id": "m-001",
                    "kind": "technical_identity_and_reproduction",
                    "normalized_meaning": "GraphSAGE is the method identity; PyTorch Geometric SAGEConv and ogbn-products are reproduction and evaluation identities that must remain reader-facing.",
                    "source_anchor_ids": ["src-002"],
                    "exact_item_ids": required_exact_ids,
                }
            ],
        }
        reader_plan = {
            "schema": helper.READER_PLAN_SCHEMA,
            "bundle_order": ["bundle-001"],
            "excluded_source_context_item_ids": ["ctx-001"],
            "bundles": [
                {
                    "bundle_id": "bundle-001",
                    "reader_question_id": "rq-001",
                    "owned_meaning_ids": ["m-001"],
                    "required_exact_item_ids": required_exact_ids,
                    "information_shape": "cohesive_prose",
                    "reader_dispositions": [
                        {
                            "meaning_id": "m-001",
                            "disposition": "CORE_INLINE",
                            "source_role": "method reproduction identity",
                            "reader_reason": "读者需要保留方法、API 和数据集身份，才能理解与复现。",
                        }
                    ],
                }
            ],
        }
        final_candidate = (
            "GraphSAGE 通过邻域采样学习节点表示；在 PyTorch Geometric 中可用 "
            "`torch_geometric.nn.SAGEConv` 复现，常见评测数据集是 ogbn-products。"
        )
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            stage_dir = root / "stage"
            write_json(stage_dir / "route_selection.json", {
                "schema": helper.ROUTE_SELECTION_SCHEMA,
                "selector_owner": "writing-style",
                "selected_route": "scientific-rewrite",
                "forced_route": False,
                "ordinary_user_prompt": True,
                "prompt_sha256": helper.sha256_text(prompt),
                "source_sha256": helper.sha256_text(source),
                "prompt_internal_terms": [],
            })
            write_json(stage_dir / "meaning_map.json", meaning_map)
            write_json(stage_dir / "reader_plan.json", reader_plan)
            write_json(stage_dir / "realization_packets/bundle-001.json", {
                "schema": helper.REALIZATION_PACKET_SCHEMA,
                "bundle_id": "bundle-001",
                "meaning_records": [
                    {
                        "meaning_id": "m-001",
                        "meaning": "保留 GraphSAGE、PyTorch Geometric、SAGEConv 和 ogbn-products 作为方法、API 与数据集身份。",
                    }
                ],
                "required_exact_items": [item for item in exact_items if item["exact_item_id"] in required_exact_ids],
                "information_shape": "cohesive_prose",
                "modality_preservation": {
                    "preserve_completion_status": True,
                    "preserve_subject_voice": True,
                    "preserve_temporal_status": True,
                    "preserve_epistemic_status": True,
                },
            })
            write_json(stage_dir / "assembly_packet.json", {
                "schema": helper.ASSEMBLY_PACKET_SCHEMA,
                "reader_plan_sha256": helper.sha256_text(helper.canonical_json(reader_plan)),
                "realized_bundle_sha256s": {"bundle-001": helper.sha256_text(final_candidate)},
                "whole_document_finish": {
                    "document_purpose": "把技术条目整理成可复现的中文说明。",
                    "reader_entry": "直接进入方法、API 与数据集身份。",
                    "section_order_rationale": "短说明先方法，再实现接口，再评测数据。",
                    "transition_plan": "用复现关系连接方法和 API。",
                    "voice_constraints": "不写网页包装和内部审计痕迹。",
                    "technical_detail_placement": "API 和数据集放在正文同一句中。",
                },
            })
            write_json(stage_dir / "semantic_audit.json", {
                "schema": helper.SEMANTIC_AUDIT_SCHEMA,
                "decision": "PASS",
                "findings": [],
                "reader_disposition_decision": "PASS",
                "reader_disposition_covered_meaning_ids": ["m-001"],
                "reader_disposition_findings": [],
            })
            (stage_dir / "final_candidate.md").write_text(final_candidate + "\n", encoding="utf-8")

            receipt = helper.validate_stage_package(source, stage_dir, prompt=prompt)

        self.assertEqual(receipt["meaning_map"]["source_context_item_count"], 1)
        self.assertEqual(receipt["reader_plan"]["excluded_source_context_item_count"], 1)
        self.assertNotIn("Pas de message", final_candidate)
        self.assertIn("GraphSAGE", final_candidate)
        self.assertIn("ogbn-products", final_candidate)

    def test_reader_relevance_cannot_hide_inline_critical_identity_as_metadata(self) -> None:
        source = "GraphSAGE 是 Hamilton et al. 提出的图表示学习方法，不是网页语言标签。"
        anchors = helper.split_source_anchors(source)
        exact_items = helper.extract_exact_items(source)
        graph_sage = next(item for item in exact_items if item["literal"] == "GraphSAGE")
        meaning_map = {
            "schema": helper.MEANING_MAP_SCHEMA,
            "source_sha256": helper.sha256_text(source),
            "source_anchors": anchors,
            "exact_items": exact_items,
            "source_context_items": [
                {
                    "source_context_item_id": "ctx-001",
                    "source_anchor_ids": ["src-001"],
                    "context_kind": "source_wrapper_metadata",
                    "reader_relevance_decision": "exclude_from_reader_facing_candidate",
                    "rationale": "incorrectly tries to hide a method identity as metadata",
                    "exact_item_ids": [graph_sage["exact_item_id"]],
                }
            ],
            "meanings": [
                {
                    "meaning_id": "m-001",
                    "kind": "method_identity",
                    "normalized_meaning": "GraphSAGE is the method identity and must remain reader-facing.",
                    "source_anchor_ids": ["src-001"],
                    "exact_item_ids": [graph_sage["exact_item_id"]],
                }
            ],
        }

        with self.assertRaisesRegex(helper.ValidationError, "reader relevance cannot exclude inline-critical exact items"):
            helper.validate_meaning_map(meaning_map, source)

    def test_realization_requires_modality_preservation(self) -> None:
        payload = {
            "schema": helper.REALIZATION_PACKET_SCHEMA,
            "bundle_id": "bundle-001",
            "meaning_records": [{"meaning_id": "m-001", "meaning": "保留未来工作的主体和未完成状态。"}],
        }
        with self.assertRaisesRegex(helper.ValidationError, "requires modality_preservation"):
            helper.validate_realization_packet(payload)

        payload["modality_preservation"] = {"preserve_completion_status": True}
        with self.assertRaisesRegex(helper.ValidationError, "modality preservation missing"):
            helper.validate_realization_packet(payload)

    def test_assembly_requires_whole_document_finish_contract(self) -> None:
        payload = {
            "schema": helper.ASSEMBLY_PACKET_SCHEMA,
            "reader_plan_sha256": "abc",
            "realized_bundle_sha256s": {"bundle-001": "def"},
        }
        with self.assertRaisesRegex(helper.ValidationError, "requires whole_document_finish"):
            helper.validate_assembly_packet(payload)

    def test_semantic_audit_requires_reader_disposition_audit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _, stage_dir, _ = build_valid_stage(Path(tmp))
            reader_plan = json.loads((stage_dir / "reader_plan.json").read_text(encoding="utf-8"))
            semantic_audit = {
                "schema": helper.SEMANTIC_AUDIT_SCHEMA,
                "decision": "PASS",
                "findings": [],
            }
            with self.assertRaisesRegex(helper.ValidationError, "reader disposition decision"):
                helper.validate_semantic_audit(semantic_audit, reader_plan=reader_plan)

            semantic_audit["reader_disposition_decision"] = "PASS"
            semantic_audit["reader_disposition_covered_meaning_ids"] = ["m-001"]
            semantic_audit["reader_disposition_findings"] = []
            with self.assertRaisesRegex(helper.ValidationError, "omits meanings"):
                helper.validate_semantic_audit(semantic_audit, reader_plan=reader_plan)

    def test_route_selection_requires_ordinary_unforced_heavy_route(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source, stage_dir, _ = build_valid_stage(Path(tmp))
            route_selection = json.loads((stage_dir / "route_selection.json").read_text(encoding="utf-8"))
            prompt = (Path(tmp) / "prompt.md").read_text(encoding="utf-8").strip()
            result = helper.validate_route_selection(route_selection, source, prompt=prompt)
            self.assertEqual(result["selected_route"], "scientific-rewrite")

            route_selection["forced_route"] = True
            with self.assertRaisesRegex(helper.ValidationError, "forced"):
                helper.validate_route_selection(route_selection, source, prompt=prompt)

    def test_route_classifier_keeps_writing_style_routes_distinct(self) -> None:
        long_cn = "把这份较长科研报告重新组织成自然中文，数字、公式、引用、比较条件和限制都不能丢。"
        long_source = (
            "FedFisher 在 MMs 数据集上取得 Dice=0.81，但这个结论只覆盖一次通信的设置 [12]。\n\n"
            "CARE 的初步结果来自同一批公开切分，但报告里没有把通信轮数、客户端数量和后处理写在同一个地方。\n\n"
            "公式 $L=L_{seg}+0.2L_{reg}$ 只用于 FedFisher 的消融实验，CARE 没有使用这个正则项。\n\n"
            "复现实验脚本位于 `scripts/run_fedfisher.sh`，配置文件是 `configs/mm_fedfisher.yaml`。\n\n"
            "这些信息需要重排成读者能先理解结论、再理解限制和复现实验条件的科学说明。"
        )
        self.assertEqual(helper.classify_writing_style_route(long_cn, long_source)["selected_route"], "scientific-rewrite")
        self.assertEqual(helper.classify_writing_style_route("把这两句中文润色一下。", "这是一句中文。")["selected_route"], "chinese-prose")
        self.assertEqual(
            helper.classify_writing_style_route("只检查数字、公式和引用有没有变化。", long_source)["selected_route"],
            "writing-fidelity",
        )
        english = "Polish this Results paragraph. The proposed method improves Dice while retaining uncertainty."
        self.assertEqual(helper.classify_writing_style_route("Polish this English scientific prose.", english)["selected_route"], "scientific-prose")

    def test_ordinary_latin_span_is_not_promoted_to_exact_item(self) -> None:
        text = "reader effort 和 scientific gap 这里只是普通英文说明，不应自动逐字保留。"
        exact_items = helper.extract_exact_items(text)
        self.assertNotIn("reader effort", {item["literal"] for item in exact_items})
        self.assertNotIn("scientific gap", {item["literal"] for item in exact_items})

        with self.assertRaisesRegex(helper.ValidationError, "ordinary Latin"):
            helper.validate_exact_item(
                {
                    "exact_item_id": "exact-999",
                    "literal": "reader effort",
                    "sha256": helper.sha256_text("reader effort"),
                    "category": "ordinary_latin",
                }
            )

    def test_internal_workflow_trace_is_not_reader_facing_exact_identity(self) -> None:
        text = (
            "复现实验脚本位于 `scripts/run_fedfisher.sh`，配置文件是 `configs/mm_fedfisher.yaml`。\n"
            "内部验收记录位于 results/051_writing_style_rebuild/RESULT.md，"
            "implementation commit 为 ee8dd6edda2a2e4dd8f3210504225a56432b11a0，"
            "状态写在 automation/reviewed_handoff/tasks/051_writing_style_rebuild/CURRENT.json。"
        )
        literals = {item["literal"] for item in helper.extract_exact_items(text)}

        self.assertIn("scripts/run_fedfisher.sh", literals)
        self.assertIn("configs/mm_fedfisher.yaml", literals)
        self.assertNotIn("results/051_writing_style_rebuild/RESULT.md", literals)
        self.assertNotIn("automation/reviewed_handoff/tasks/051_writing_style_rebuild/CURRENT.json", literals)
        self.assertNotIn("ee8dd6edda2a2e4dd8f3210504225a56432b11a0", literals)

    def test_reader_facing_internal_workflow_leakage_fails_stage_validation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source, stage_dir, _ = build_valid_stage(Path(tmp))
            candidate = (
                (stage_dir / "final_candidate.md").read_text(encoding="utf-8")
                + "\n本轮满足收口条件，GitHub Actions run 通过，commit "
                "ee8dd6edda2a2e4dd8f3210504225a56432b11a0 已记录在 "
                "results/051_writing_style_rebuild/RESULT.md。"
            )
            (stage_dir / "final_candidate.md").write_text(candidate + "\n", encoding="utf-8")
            prompt = (Path(tmp) / "prompt.md").read_text(encoding="utf-8").strip()

            with self.assertRaisesRegex(helper.ValidationError, "reader-facing internal workflow leakage"):
                helper.validate_stage_package(source, stage_dir, prompt=prompt)

    def test_reader_facing_internal_frame_allows_scientific_reproduction_paths(self) -> None:
        candidate = (
            "FedFisher 在 MMs 数据集、一次通信设置下达到 Dice=0.81 [12]。"
            "复现实验脚本是 `scripts/run_fedfisher.sh`，配置文件是 `configs/mm_fedfisher.yaml`。"
        )
        result = helper.validate_reader_facing_internal_frame(candidate)
        self.assertTrue(result["ok"])

    def test_source_process_framing_fails_standalone_reader_candidate(self) -> None:
        candidate = (
            "Bloom filter 用 $m$ 位数组和 $k$ 个哈希函数表示集合。"
            "原文同时指出，这种结构可能产生假阳性，但不会产生假阴性。"
        )

        with self.assertRaisesRegex(helper.ValidationError, "source-process framing"):
            helper.validate_standalone_reader_frame(candidate)

    def test_source_process_frame_allows_attribution_and_explicit_comparison(self) -> None:
        attributed = "Smith et al. [12] reported that Bloom filters may produce false positives."
        self.assertTrue(helper.validate_standalone_reader_frame(attributed)["ok"])

        comparison = "原文指出 A；改写稿误写成 B。"
        result = helper.validate_standalone_reader_frame(comparison, task_context="source comparison")
        self.assertTrue(result["ok"])

    def test_stage_validation_rejects_source_process_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source, stage_dir, _ = build_valid_stage(Path(tmp))
            candidate = (
                (stage_dir / "final_candidate.md").read_text(encoding="utf-8")
                + "\n原文指出，上述公式只用于 FedFisher 消融实验。"
            )
            (stage_dir / "final_candidate.md").write_text(candidate + "\n", encoding="utf-8")
            prompt = (Path(tmp) / "prompt.md").read_text(encoding="utf-8").strip()

            with self.assertRaisesRegex(helper.ValidationError, "source-process framing"):
                helper.validate_stage_package(source, stage_dir, prompt=prompt)

    def test_structural_rewrite_allows_reordering_but_rejects_semantic_drift(self) -> None:
        protected = [
            "claim",
            "evidence",
            "number",
            "formula",
            "citation",
            "comparator",
            "condition",
            "scope",
            "uncertainty",
            "caveat",
            "attribution",
            "conclusion_strength",
        ]
        result = helper.validate_structural_fidelity(
            {
                "mode": "STRUCTURAL_REWRITE",
                "protected_authority": protected,
                "structure_changed": True,
                "semantic_drifts": [],
            }
        )
        self.assertTrue(result["structure_changed"])

        with self.assertRaisesRegex(helper.ValidationError, "must not protect source structure"):
            helper.validate_structural_fidelity(
                {
                    "mode": "STRUCTURAL_REWRITE",
                    "protected_authority": protected + ["source_heading"],
                    "structure_changed": False,
                    "semantic_drifts": [],
                }
            )
        with self.assertRaisesRegex(helper.ValidationError, "semantic authority drift"):
            helper.validate_structural_fidelity(
                {
                    "mode": "STRUCTURAL_REWRITE",
                    "protected_authority": protected,
                    "structure_changed": True,
                    "semantic_drifts": [{"finding_type": "changed_comparator", "status": "unresolved"}],
                }
            )

    def test_writing_style_surface_keeps_existing_scientific_prose_route(self) -> None:
        config = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        profile = json.loads((REPO_ROOT / "profiles/codex-writing-style.json").read_text(encoding="utf-8"))
        writing_style = next(plugin for plugin in config["plugins"] if plugin["name"] == "writing-style")
        skill_sources = [entry["source"] for entry in writing_style["skills"]]

        self.assertIn("skills/writing/core/scientific-prose", skill_sources)
        self.assertIn("skills/writing/core/scientific-rewrite", skill_sources)
        self.assertIn("skills/writing/core/chinese-prose", skill_sources)
        self.assertIn("skills/writing/core/scientific-prose", profile["skills"])
        self.assertIn("skills/writing/core/scientific-rewrite", profile["skills"])

    def test_routing_text_sends_structural_scientific_rewrite_to_heavy_route(self) -> None:
        scientific = (REPO_ROOT / "skills/writing/core/scientific-rewrite/SKILL.md").read_text(encoding="utf-8")
        chinese = (REPO_ROOT / "skills/writing/core/chinese-prose/SKILL.md").read_text(encoding="utf-8")
        fidelity = (REPO_ROOT / "skills/writing/core/writing-fidelity/SKILL.md").read_text(encoding="utf-8")

        self.assertIn("existing Chinese or Chinese-dominant scientific/technical material", scientific)
        self.assertIn("asks to reorganize", scientific)
        self.assertIn("facts, numbers, formulas, citations, comparisons, conditions, limitations, paths", scientific)
        self.assertIn("does not need to name this\nskill or any internal route", scientific)
        self.assertIn("不要把本 skill 当主路线；应交给 `scientific-rewrite`", chinese)
        self.assertIn("hand off 给 `scientific-rewrite`", chinese)
        self.assertIn(
            "source-faithful structural scientific/technical rewrites to scientific-rewrite",
            fidelity,
        )
        self.assertIn("instead of making `chinese-prose` the main route", fidelity)

    def test_generated_plugin_payload_contains_heavy_route_helper(self) -> None:
        plugin_json = json.loads(
            (REPO_ROOT / "plugins/codex/plugins/writing-style/.codex-plugin/plugin.json").read_text(encoding="utf-8")
        )
        generated_skill = REPO_ROOT / "plugins/codex/plugins/writing-style/skills/scientific-rewrite/SKILL.md"
        generated_helper = load_helper_from(GENERATED_HELPER_PATH, "generated_scientific_rewrite_support")

        self.assertEqual(plugin_json["version"], "0.3")
        self.assertTrue(generated_skill.exists())
        self.assertTrue(GENERATED_HELPER_PATH.exists())
        self.assertEqual(generated_helper.RUNTIME_SCHEMA, helper.RUNTIME_SCHEMA)
        self.assertEqual(generated_helper.RUNTIME_NAME, helper.RUNTIME_NAME)
        self.assertEqual(generated_helper.ROUTE_SELECTION_SCHEMA, helper.ROUTE_SELECTION_SCHEMA)


if __name__ == "__main__":
    unittest.main()
