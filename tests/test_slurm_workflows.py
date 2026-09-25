from __future__ import annotations

import argparse
import importlib.util
import json
import os
import stat
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import skills  # noqa: E402


HELPER_PATH = REPO_ROOT / "skills" / "tools" / "hpc" / "slurm-workflows" / "scripts" / "slurm_routing.py"


def load_helper(path: Path = HELPER_PATH):
    spec = importlib.util.spec_from_file_location("slurm_routing_under_test", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def write_executable(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
    path.chmod(path.stat().st_mode | stat.S_IXUSR)


class SlurmWorkflowsRoutingTests(unittest.TestCase):
    def test_g1_live_discovery_no_profile_and_unknown_facts(self) -> None:
        helper = load_helper()
        with tempfile.TemporaryDirectory() as tmp:
            bindir = Path(tmp)
            write_executable(
                bindir / "sinfo",
                "#!/bin/sh\nprintf 'pi-gpu*|up|2:00:00|2|64|512000|gpu:h100:4|(null)|idle|100\\nshared-gpu|up|1:00:00|4|32|256000|gpu:a100:2|(null)|mix|50\\n'\n",
            )
            write_executable(
                bindir / "scontrol",
                "#!/bin/sh\nif [ \"$2\" = config ]; then printf 'ClusterName=PrivateCluster\\nSelectType=select/cons_tres\\nPrivateData=jobs\\n'; exit 0; fi\nexit 1\n",
            )
            with mock.patch.dict(os.environ, {"PATH": str(bindir), "USER": "tester"}):
                context = helper.discover_live_site_context()

        self.assertTrue(context["runtime_available"])
        self.assertEqual(context["fact_provenance"]["partitions"], "LIVE_KNOWN")
        self.assertEqual(context["fact_provenance"]["associations"], "UNKNOWN")
        self.assertEqual(context["fact_provenance"]["partition_detail"], "UNKNOWN")
        self.assertTrue(context["local_site_id"].startswith("privatecluster"))
        self.assertNotIn("PrivateCluster ", json.dumps(context))

    def test_g1_generic_source_has_no_deployment_routing_constants(self) -> None:
        source_paths = [
            REPO_ROOT / "scripts" / "skills.py",
            REPO_ROOT / "skills" / "tools" / "hpc" / "slurm-workflows" / "SKILL.md",
            HELPER_PATH,
        ]
        forbidden = ["htzhulab", "volta-gpu", "longleaf", "cuhk"]
        combined = "\n".join(path.read_text(encoding="utf-8").lower() for path in source_paths)
        for value in forbidden:
            self.assertNotIn(value, combined)

    def test_g2_local_preference_orders_legal_routes_without_resource_change(self) -> None:
        helper = load_helper()
        context = {
            "partitions": [
                {"partition": "shared-new", "availability": "up", "gres": "gpu:h100:4", "features": ""},
                {"partition": "pi-fast", "availability": "up", "gres": "gpu:v100:4", "features": ""},
                {"partition": "shared-mid", "availability": "up", "gres": "gpu:a100:2", "features": ""},
            ]
        }
        contract = {"gpus": 1, "gpu_type": "v100", "accelerator_hard": False, "memory_mb": 65536}
        plan = helper.route_candidates(
            context,
            contract,
            {"partition_priority": ["pi-fast"], "accelerator_priority": ["h100", "a100", "v100"]},
        )
        self.assertEqual(plan["decision"], "route")
        self.assertEqual(plan["candidates"][0]["partition"], "pi-fast")
        self.assertEqual(plan["resource_contract"], contract)

        hard = helper.route_candidates(context, {"gpus": 1, "gpu_type": "h100", "accelerator_hard": True}, {"accelerator_priority": ["v100"]})
        self.assertEqual([item["partition"] for item in hard["candidates"]], ["shared-new"])

    def test_g3_g4_job_identity_and_duplicate_race_fail_closed(self) -> None:
        helper = load_helper()
        self.assertEqual(
            helper.widening_plan(
                {"state": "PENDING", "dependency": "afterok:123"},
                ["p1", "p2"],
                {"native_multi_partition": True, "in_place_partition_update_verified": False},
            )["action"],
            "fail_closed",
        )
        self.assertEqual(
            helper.widening_plan({"state": "PENDING"}, ["p1", "p2"], {"native_multi_partition": True})["action"],
            "native_widen",
        )
        self.assertFalse(helper.duplicate_race_decision({}, True)["allowed"])
        self.assertTrue(helper.duplicate_race_decision({"duplicate_race": "allowed"}, True)["allowed"])

    def test_g5_bounded_monitoring_replacement(self) -> None:
        helper = load_helper()
        self.assertEqual(
            helper.bounded_replacement_decision({"poll_interval_seconds": 10}, {"state": "PENDING", "inactive_confirmed": True})["reason"],
            "tight_polling",
        )
        self.assertEqual(
            helper.bounded_replacement_decision({"poll_interval_seconds": 300}, {"state": "PENDING", "inactive_confirmed": True})["reason"],
            "no_blind_resubmit",
        )
        self.assertEqual(
            helper.bounded_replacement_decision({"poll_interval_seconds": 300, "replacement_reason": "queue_window_missed"}, {"state": "PENDING", "inactive_confirmed": False})["reason"],
            "old_job_uncertain",
        )
        self.assertEqual(
            helper.bounded_replacement_decision({"poll_interval_seconds": 300, "replacement_reason": "queue_window_missed"}, {"state": "PENDING", "inactive_confirmed": True})["action"],
            "replace_pending",
        )

    def test_g7_sticky_contract_and_right_sizing_hysteresis(self) -> None:
        helper = load_helper()
        contract = helper.resolve_resource_contract(
            {"project": "p", "entrypoint": "train.py", "workload_class": "fit", "scale_signature": "n1", "accelerator_requirement": "h100"},
            {},
            {"p|train.py|fit|n1|h100": {"memory_mb": 64000, "cpus_per_task": 8, "gpus": 1, "gpu_type": "h100"}},
            {"memory_mb": 32000},
        )
        self.assertEqual(contract["source"], "user_local_contract")
        self.assertEqual(contract["resources"]["memory_mb"], 64000)
        self.assertEqual(
            helper.right_size_contract(contract["resources"], [{"comparable": False, "ambiguous": True}])["memory_decision"]["decision"],
            "keep",
        )
        oom = helper.right_size_contract(contract["resources"], [{"comparable": True, "oom": True, "max_rss_mb": 64000}])
        self.assertGreater(oom["resources"]["memory_mb"], 64000)
        low = helper.right_size_contract(
            contract["resources"],
            [
                {"comparable": True, "state": "COMPLETED", "max_rss_mb": 20000},
                {"comparable": True, "state": "COMPLETED", "max_rss_mb": 22000},
                {"comparable": True, "state": "COMPLETED", "max_rss_mb": 21000},
            ],
        )
        self.assertEqual(low["memory_decision"]["decision"], "decrease_candidate")
        self.assertEqual(low["resources"]["cpu_action"], "stable_first")
        self.assertEqual(low["resources"]["gpu_action"], "preserve_count_and_type")

    def test_g8_modes_capacity_reuse_successor_and_enrollment(self) -> None:
        helper = load_helper()
        self.assertEqual(helper.classify_workload_mode({"entrypoint": "train.py"}), "batch")
        self.assertEqual(helper.classify_workload_mode({"persistent": True}), "persistent")
        self.assertEqual(helper.classify_workload_mode({"debug": True}), "debug")
        family = {
            "local_site_id": "site-a",
            "capacity_family_id": "weekly-gpu",
            "activation_scope": {"family_id": "weekly-gpu", "accelerator_requirement": "h100"},
            "accepted_resource_contract": {"gpus": 1, "gpu_type": "h100"},
            "allowed_resource_envelope": {"gpus": 1, "gpu_type": "h100"},
            "recurrence": {"weekday": "mon"},
            "auto_maintain_successor": True,
        }
        self.assertEqual(
            helper.capacity_reconcile(family, [{"state": "RUNNING", "gpus": 1, "gpu_type": "h100"}], [], {"mode": "persistent", "family_id": "weekly-gpu", "accelerator_requirement": "h100"})["action"],
            "reuse_active",
        )
        self.assertEqual(
            helper.capacity_reconcile(family, [], [{"lifecycle_owned": True, "gpus": 1, "gpu_type": "h100"}], {"mode": "persistent", "family_id": "weekly-gpu", "accelerator_requirement": "h100"})["action"],
            "keep_successor",
        )
        self.assertEqual(
            helper.capacity_reconcile(family, [], [], {"mode": "persistent", "family_id": "weekly-gpu", "accelerator_requirement": "h100"})["action"],
            "read_only_proposal",
        )
        family["enrollment"] = {"submit_successor": True, "max_successor": 1}
        self.assertEqual(
            helper.capacity_reconcile(family, [], [], {"mode": "persistent", "family_id": "weekly-gpu", "accelerator_requirement": "h100"})["action"],
            "plan_one_successor",
        )
        self.assertEqual(
            helper.capacity_reconcile(family, [], [], {"mode": "batch", "family_id": "cpu-maint", "accelerator_requirement": "cpu"})["action"],
            "read_only",
        )

    def test_g6_no_profile_environment_apply_installed_normal_entry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            override = Path(tmp) / "local-overrides.toml"
            override.write_text(
                "[sites.third-party]\nlocal_site_id = \"third-party\"\npartition_priority = \"pi-fast\"\naccelerator_priority = \"h100,a100\"\n",
                encoding="utf-8",
            )
            args = argparse.Namespace(
                site="third-party",
                target="repo",
                project=str(project),
                hostname=None,
                path=None,
                local_override=str(override),
                dry_run=False,
                json=True,
            )
            plan = skills.environment_plan_payload(args)
            manifest = skills.environment_apply_plan(args, plan)
            installed = Path(manifest["target_root"]) / "slurm-workflows"
            helper = load_helper(installed / "scripts" / "slurm_routing.py")
            reference = (installed / "references" / "_generated" / "site-profile.md").read_text(encoding="utf-8")
            route = helper.route_candidates(
                {"partitions": [{"partition": "pi-fast", "availability": "up", "gres": "gpu:h100:1"}]},
                {"gpus": 1, "gpu_type": "h100", "accelerator_hard": True},
                {"partition_priority": ["pi-fast"]},
            )
        self.assertEqual(manifest["local_site_id"], "third-party")
        self.assertIsNone(manifest["policy_overlay_id"])
        self.assertIn("local_site_id: third-party", reference)
        self.assertIn("policy_overlay_id: none", reference)
        self.assertEqual(route["decision"], "route")


if __name__ == "__main__":
    unittest.main()
