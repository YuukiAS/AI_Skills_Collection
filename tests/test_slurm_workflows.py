from __future__ import annotations

import argparse
import contextlib
import io
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


def install_fake_slurm(bindir: Path, cluster_name: str = "PrivateClusterSecret") -> None:
    write_executable(
        bindir / "sinfo",
        "#!/bin/sh\nprintf 'pi-fast*|up|8:00:00|2|64|512000|gpu:h100:4|(null)|idle|100\\nshared-gpu|up|4:00:00|4|32|256000|gpu:a100:2|(null)|mix|50\\n'\n",
    )
    write_executable(
        bindir / "scontrol",
        f"#!/bin/sh\nif [ \"$2\" = config ]; then printf 'ClusterName={cluster_name}\\nSelectType=select/cons_tres\\nPrivateData=jobs\\nControllerHost=private-controller\\n'; exit 0; fi\nif [ \"$2\" = partition ]; then exit 0; fi\nexit 1\n",
    )


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
        intent = {"project": "p", "entrypoint": "train.py", "workload_class": "fit", "scale_signature": "n1", "accelerator_requirement": "h100"}
        contract = helper.resolve_resource_contract(
            intent,
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

        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(tmp) / "slurm-workflows.toml"
            state = helper.load_workflow_state(state_path)
            helper.persist_accepted_workload_contract(state, intent, contract["resources"], "artifact:contract-review")
            helper.save_workflow_state(state, state_path)
            first_load = helper.load_workflow_state(state_path)
            second_load = helper.load_workflow_state(state_path)
            self.assertEqual(first_load, second_load)
            reused = helper.resolve_resource_contract(intent, {}, second_load["accepted_workload_contracts"], {"memory_mb": 32000})
            self.assertEqual(reused["source"], "user_local_contract")
            self.assertEqual(reused["resources"]["memory_mb"], 64000)
            self.assertEqual(second_load["evidence_locators"]["p|train.py|fit|n1|h100"], "artifact:contract-review")

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
            "recurrence": {"weekday": "mon", "start_time": "09:00", "duration_hours": 8},
            "minimum_useful_duration": "6h",
            "successor_lead_time": "12h",
            "site_capabilities": {"calendar_submit_verified": True},
            "auto_maintain_successor": True,
        }
        invocation = {
            "mode": "persistent",
            "family_id": "weekly-gpu",
            "accelerator_requirement": "h100",
            "now": "2026-09-27T12:00:00+00:00",
        }
        self.assertEqual(
            helper.capacity_reconcile(
                family,
                [{"state": "RUNNING", "gpus": 1, "gpu_type": "h100", "start_time": "2026-09-27T11:00:00+00:00", "end_time": "2026-09-29T00:00:00+00:00"}],
                [],
                invocation,
            )["action"],
            "reuse_active",
        )
        self.assertEqual(
            helper.capacity_reconcile(
                family,
                [{"state": "RUNNING", "gpus": 1, "gpu_type": "h100", "start_time": "2026-09-27T11:00:00+00:00", "end_time": "2026-09-28T12:00:00+00:00"}],
                [],
                invocation,
            )["action"],
            "read_only_proposal",
        )
        self.assertEqual(
            helper.capacity_reconcile(
                family,
                [],
                [{"lifecycle_owned": True, "gpus": 1, "gpu_type": "h100", "requested_start": "2026-09-28T08:00:00+00:00", "end_time": "2026-09-28T18:00:00+00:00"}],
                invocation,
            )["action"],
            "keep_successor",
        )
        self.assertEqual(
            helper.capacity_reconcile(
                family,
                [],
                [
                    {"lifecycle_owned": True, "gpus": 1, "gpu_type": "h100", "requested_start": "2026-09-28T08:00:00+00:00", "end_time": "2026-09-28T18:00:00+00:00"},
                    {"lifecycle_owned": True, "gpus": 1, "gpu_type": "h100", "requested_start": "2026-09-28T08:00:00+00:00", "end_time": "2026-09-28T18:00:00+00:00"},
                ],
                invocation,
            )["reason"],
            "multiple_lifecycle_successors",
        )
        self.assertEqual(
            helper.capacity_reconcile(family, [], [], invocation)["action"],
            "read_only_proposal",
        )
        family["enrollment"] = {"submit_successor": True, "max_successor": 1}
        self.assertEqual(
            helper.capacity_reconcile(family, [], [], invocation)["action"],
            "read_only_proposal",
        )
        family["enrollment"] = {"submit_successor": True, "max_successor": 1, "scope_digest": "wrong"}
        self.assertEqual(
            helper.capacity_reconcile(family, [], [], invocation)["action"],
            "read_only_proposal",
        )
        family["enrollment"] = {"submit_successor": True, "max_successor": 1, "scope_digest": helper._scope_digest(family)}
        unverified = dict(family)
        unverified["site_capabilities"] = {"calendar_submit_verified": False}
        self.assertEqual(
            helper.capacity_reconcile(unverified, [], [], invocation)["reason"],
            "calendar_submit_unverified",
        )
        self.assertEqual(
            helper.capacity_reconcile(family, [], [], invocation)["action"],
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
            installed = skills.environment_target_root(args) / "slurm-workflows"
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

    def test_g6_true_normal_entry_detect_plan_apply_doctor_installed_live_route(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            bindir = Path(tmp) / "bin"
            bindir.mkdir()
            install_fake_slurm(bindir)
            project = Path(tmp) / "project"
            override = Path(tmp) / "private" / "local-overrides.toml"
            override.parent.mkdir()
            override.write_text(
                "[sites.privateclustersecret]\npartition_priority = \"pi-fast\"\naccelerator_priority = \"h100,a100\"\n",
                encoding="utf-8",
            )
            args = argparse.Namespace(
                site=None,
                target="repo",
                project=str(project),
                hostname="ordinary-login",
                path=str(project),
                local_override=str(override),
                dry_run=False,
                json=True,
                submit_smoke_job=False,
            )
            with mock.patch.dict(os.environ, {"PATH": str(bindir), "USER": "tester"}):
                with contextlib.redirect_stdout(io.StringIO()):
                    detected_rc = skills.command_environment_detect(
                        argparse.Namespace(site=None, hostname="ordinary-login", path=str(project), local_override=str(override), json=True)
                    )
                plan = skills.environment_plan_payload(args)
                manifest = skills.environment_apply_plan(args, plan)
                doctor = skills.environment_doctor_payload(args)
                installed = skills.environment_target_root(args) / "slurm-workflows"
                installed_helper = load_helper(installed / "scripts" / "slurm_routing.py")
                live_context = installed_helper.discover_live_site_context(local_site_id=manifest["local_site_id"])
                local_data, _errors = skills.parse_environment_local_override(override)
                local_policy = skills.environment_public_override_policy(local_data[manifest["local_site_id"]])
                route = installed_helper.route_candidates(
                    live_context,
                    {"gpus": 1, "gpu_type": "h100", "accelerator_hard": True},
                    local_policy,
                )
            reference = (installed / "references" / "_generated" / "site-profile.md").read_text(encoding="utf-8")
            manifest_text = json.dumps(manifest, sort_keys=True)
        self.assertEqual(detected_rc, 0)
        self.assertEqual(plan["local_site_id"], "privateclustersecret")
        self.assertTrue(plan["runtime_available"])
        self.assertEqual(doctor["diagnostics"]["missing_required_fields"], [])
        self.assertEqual(route["decision"], "route")
        self.assertEqual(route["candidates"][0]["partition"], "pi-fast")
        self.assertIn("local_override_locator: local-override:", reference)
        self.assertNotIn(str(Path(tmp)), reference)
        self.assertNotIn(str(Path(tmp)), manifest_text)
        self.assertNotIn("PrivateClusterSecret", reference)
        self.assertNotIn("private-controller", reference)

    def test_g6_known_profile_keeps_distinct_local_site_id(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            override = Path(tmp) / "local-overrides.toml"
            override.write_text(
                "[sites.unc-longleaf]\nlocal_site_id = \"private-lab-site\"\npartition_priority = \"pi-fast\"\n",
                encoding="utf-8",
            )
            args = argparse.Namespace(
                site="unc-longleaf",
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
            reference = (
                skills.environment_target_root(args) / "slurm-workflows" / "references" / "_generated" / "site-profile.md"
            ).read_text(encoding="utf-8")
        self.assertEqual(plan["requested_site_id"], "unc-longleaf")
        self.assertEqual(plan["local_site_id"], "private-lab-site")
        self.assertEqual(plan["policy_overlay_id"], "unc-longleaf")
        self.assertEqual(manifest["local_site_id"], "private-lab-site")
        self.assertEqual(manifest["policy_overlay_id"], "unc-longleaf")
        self.assertIn("local_site_id: private-lab-site", reference)
        self.assertIn("policy_overlay_id: unc-longleaf", reference)

    def test_legacy_race_defaults_and_site_aware_doctor(self) -> None:
        fresh = skills.environment_blank_site_override("fresh-site")
        self.assertIn('race_after_minutes = ""', fresh)
        self.assertIn('race_cancel_policy = ""', fresh)
        self.assertNotIn('race_after_minutes = "60"', fresh)
        self.assertNotIn("cancel_after_first_validated_output", fresh)
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            override = Path(tmp) / "local-overrides.toml"
            override.write_text("[sites.unc-longleaf]\naccount = \"\"\n", encoding="utf-8")
            args = argparse.Namespace(
                site="unc-longleaf",
                target="repo",
                project=str(project),
                hostname=None,
                path=None,
                local_override=str(override),
                submit_smoke_job=False,
                json=True,
            )
            diagnostics = skills.environment_doctor_payload(args)["diagnostics"]
        self.assertEqual(diagnostics["missing_required_fields"], ["account"])
        self.assertNotIn("partition", diagnostics["missing_required_fields"])
        self.assertNotIn("qos", diagnostics["missing_required_fields"])
        self.assertNotIn("scratch_root", diagnostics["missing_required_fields"])
        self.assertNotIn("module_init", diagnostics["missing_required_fields"])

    def test_g6_no_profile_can_attach_optional_public_overlay(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            override = Path(tmp) / "local-overrides.toml"
            override.write_text(
                "[sites.third-party]\npolicy_overlay_id = \"unc-longleaf\"\naccelerator_priority = \"h100,a100\"\n",
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
            reference = (
                skills.environment_target_root(args) / "slurm-workflows" / "references" / "_generated" / "site-profile.md"
            ).read_text(encoding="utf-8")
        self.assertEqual(plan["local_site_id"], "third-party")
        self.assertEqual(plan["policy_overlay_id"], "unc-longleaf")
        self.assertEqual(manifest["local_site_id"], "third-party")
        self.assertEqual(manifest["policy_overlay_id"], "unc-longleaf")
        self.assertIn("local_site_id: third-party", reference)
        self.assertIn("policy_overlay_id: unc-longleaf", reference)


if __name__ == "__main__":
    unittest.main()
