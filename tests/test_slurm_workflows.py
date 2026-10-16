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
        self.assertTrue(context["tracked_site_id"].startswith("local-slurm-"))
        self.assertNotEqual(context["tracked_site_id"], context["local_site_id"])
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
        self.assertFalse(helper.duplicate_race_decision({}, False)["allowed"])
        self.assertFalse(helper.duplicate_race_decision({}, False)["eligible"])
        opt_in = helper.duplicate_race_decision({}, True)
        self.assertFalse(opt_in["allowed"])
        self.assertTrue(opt_in["eligible"])
        self.assertTrue(opt_in["requires_bounded_contract"])
        allowed_site = helper.duplicate_race_decision({"duplicate_race": "allowed"}, True)
        self.assertFalse(allowed_site["allowed"])
        self.assertTrue(allowed_site["eligible"])
        self.assertFalse(helper.duplicate_race_decision({"race_execution": "forbidden"}, True)["eligible"])

    def test_duplicate_race_policy_opt_in_truth_table_and_bounded_contract(self) -> None:
        helper = load_helper()
        truth_table = [
            ({"race_execution": "forbidden"}, True, False, "explicit_site_prohibition"),
            ({}, False, False, "missing_user_opt_in"),
            ({}, True, True, "no_known_prohibition_and_opt_in"),
            ({"race_execution": "UNKNOWN"}, False, False, "missing_user_opt_in"),
            ({"race_execution": "UNKNOWN"}, True, True, "no_known_prohibition_and_opt_in"),
            ({"race_execution": "disabled_by_default"}, True, True, "no_known_prohibition_and_opt_in"),
            ({"race_execution": "explicit_user_opt_in"}, True, True, "no_known_prohibition_and_opt_in"),
            ({"race_execution": "allowed"}, True, True, "explicit_allow_and_opt_in"),
            ({"race_execution": "allowed"}, False, False, "missing_user_opt_in"),
        ]
        for site_policy, user_opt_in, allowed, reason in truth_table:
            with self.subTest(site_policy=site_policy, user_opt_in=user_opt_in):
                decision = helper.duplicate_race_decision(site_policy, user_opt_in)
                self.assertFalse(decision["allowed"])
                self.assertEqual(decision["eligible"], allowed)
                self.assertEqual(decision["reason"], reason)

        workload = {
            "workload_scope_digest": "sha256:cohort-a-fold-1-seg-v2",
            "data": "cohort-a",
            "split": "fold-1",
            "model": "seg-v2",
            "endpoint": "train.py",
            "augmentation": "none",
            "loss_variant": "dice-ce",
            "checkpoint_selection": "val-dice",
            "preprocessing": "zscore-v1",
            "gpus": 1,
            "gpu_type": "h100",
            "memory_mb": 65536,
            "cpus_per_task": 8,
            "walltime_minutes": 240,
            "training_budget": "full",
        }
        candidates = [
            {
                "partition": "h100-short",
                "qos": "normal",
                "gpus": 1,
                "gpu_type": "h100",
                "memory_mb": 65536,
                "cpus_per_task": 8,
                "walltime_minutes": 240,
                "workload_contract": workload,
            },
            {
                "partition": "h100-main",
                "qos": "normal",
                "gpus": 1,
                "gpu_type": "h100",
                "memory_mb": 65536,
                "cpus_per_task": 8,
                "walltime_minutes": 240,
                "workload_contract": workload,
            },
        ]
        cancellation = {
            "winner_rule": "first_running_job",
            "cancel_loser": True,
            "running_tie_policy": "keep_lowest_job_id_cancel_other",
        }
        allowed = helper.bounded_duplicate_race_decision({}, True, candidates, workload, cancellation)
        self.assertTrue(allowed["allowed"])
        self.assertEqual(allowed["reason"], "bounded_two_route_race")

        explicit_forbidden = helper.bounded_duplicate_race_decision({"race_execution": "forbidden"}, True, candidates, workload, cancellation)
        self.assertFalse(explicit_forbidden["allowed"])
        self.assertEqual(explicit_forbidden["reason"], "explicit_site_prohibition")

        too_many = helper.bounded_duplicate_race_decision({}, True, candidates + [dict(candidates[0], partition="h100-extra")], workload, cancellation)
        self.assertFalse(too_many["allowed"])
        self.assertEqual(too_many["reason"], "requires_exactly_two_candidates")

        duplicate_route = helper.bounded_duplicate_race_decision({}, True, [candidates[0], dict(candidates[0])], workload, cancellation)
        self.assertFalse(duplicate_route["allowed"])
        self.assertEqual(duplicate_route["reason"], "duplicate_route_identity")

        missing_cancel = helper.bounded_duplicate_race_decision({}, True, candidates, workload, {"winner_rule": "first_running_job"})
        self.assertFalse(missing_cancel["allowed"])
        self.assertEqual(missing_cancel["reason"], "missing_loser_cancellation_contract")

        missing_proof = [candidates[0], {key: value for key, value in candidates[1].items() if key != "workload_contract"}]
        no_contract = helper.bounded_duplicate_race_decision({}, True, missing_proof, workload, cancellation)
        self.assertFalse(no_contract["allowed"])
        self.assertEqual(no_contract["reason"], "missing_workload_contract")

        augmentation_mismatch = [
            candidates[0],
            dict(candidates[1], workload_contract=dict(workload, augmentation="flip")),
        ]
        incompatible_science = helper.bounded_duplicate_race_decision({}, True, augmentation_mismatch, workload, cancellation)
        self.assertFalse(incompatible_science["allowed"])
        self.assertEqual(incompatible_science["reason"], "incompatible_workload_contract")

        digest_mismatch = [
            candidates[0],
            dict(candidates[1], workload_contract=dict(workload, workload_scope_digest="sha256:different")),
        ]
        stale_digest = helper.bounded_duplicate_race_decision({}, True, digest_mismatch, workload, cancellation)
        self.assertFalse(stale_digest["allowed"])
        self.assertEqual(stale_digest["reason"], "workload_scope_digest_mismatch")

        low_memory = [candidates[0], dict(candidates[1], memory_mb=32768)]
        memory_requirement = helper.bounded_duplicate_race_decision({}, True, low_memory, workload, cancellation)
        self.assertFalse(memory_requirement["allowed"])
        self.assertEqual(memory_requirement["reason"], "hard_resource_requirement_not_met")

        low_cpu = [candidates[0], dict(candidates[1], cpus_per_task=4)]
        cpu_requirement = helper.bounded_duplicate_race_decision({}, True, low_cpu, workload, cancellation)
        self.assertFalse(cpu_requirement["allowed"])
        self.assertEqual(cpu_requirement["reason"], "hard_resource_requirement_not_met")

        downgraded_gpu = [candidates[0], dict(candidates[1], gpu_type="a100")]
        hard_requirement = helper.bounded_duplicate_race_decision({}, True, downgraded_gpu, workload, cancellation)
        self.assertFalse(hard_requirement["allowed"])
        self.assertEqual(hard_requirement["reason"], "hard_resource_requirement_not_met")

        arbitrary_winner = helper.bounded_duplicate_race_decision(
            {},
            True,
            candidates,
            workload,
            dict(cancellation, winner_rule="largest_backfill_score"),
        )
        self.assertFalse(arbitrary_winner["allowed"])
        self.assertEqual(arbitrary_winner["reason"], "unsupported_winner_rule")

        keep_both = helper.bounded_duplicate_race_decision(
            {},
            True,
            candidates,
            workload,
            dict(cancellation, running_tie_policy="keep_both"),
        )
        self.assertFalse(keep_both["allowed"])
        self.assertEqual(keep_both["reason"], "unsupported_running_tie_policy")

        unknown_tie = helper.bounded_duplicate_race_decision(
            {},
            True,
            candidates,
            workload,
            dict(cancellation, running_tie_policy="do_something_site_specific"),
        )
        self.assertFalse(unknown_tie["allowed"])
        self.assertEqual(unknown_tie["reason"], "unsupported_running_tie_policy")

        flexible_workload = dict(workload, allowed_gpu_types=["h100", "a100"])
        flexible_workload.pop("gpu_type")
        flexible_candidates = [
            dict(candidates[0], workload_contract=flexible_workload),
            dict(candidates[1], gpu_type="a100", workload_contract=flexible_workload),
        ]
        flexible = helper.bounded_duplicate_race_decision({}, True, flexible_candidates, flexible_workload, cancellation)
        self.assertTrue(flexible["allowed"])

    def test_cancel_g1_exact_targets_private_policy_union_and_unknowns(self) -> None:
        helper = load_helper()
        site_a = {"cluster_id": "cluster-a", "cluster_identity_verified": True, "policy": {}}
        protected_policy = {
            "cluster_id": "cluster-a",
            "policy_version": "policy-7",
            "protected_partitions": ["premium"],
            "protected_accelerators": ["gpu-premium"],
            "scope_confirmed_by_human": True,
        }
        target = {
            "job_id": "4101",
            "cluster_id": "cluster-a",
            "state": "PENDING",
            "candidate_partitions": ["ordinary"],
            "requested_accelerators": ["gpu-standard"],
            "owner_run_id": "run-current",
            "cancel_responsibility": True,
            "facts_verified": True,
            "ownership_verified": True,
        }

        unprotected = helper.protected_cancel_decision(
            site_a,
            protected_policy,
            [target],
            "run-current",
            target_set_complete=True,
        )
        self.assertEqual(unprotected["decision"], "ALLOW_OWNED_UNPROTECTED")
        self.assertFalse(unprotected["execution_authorized"])

        protected_partition = helper.protected_cancel_decision(
            site_a,
            protected_policy,
            [dict(target, candidate_partitions=["ordinary", "premium"])],
            "run-current",
            target_set_complete=True,
        )
        self.assertEqual(protected_partition["decision"], "REQUIRE_FRESH_HUMAN")
        self.assertEqual(protected_partition["protection_matches"][0]["protected_partitions"], ["premium"])

        protected_accelerator = helper.protected_cancel_decision(
            site_a,
            protected_policy,
            [dict(target, requested_accelerators=["gpu-standard", "gpu-premium"])],
            "run-current",
            target_set_complete=True,
        )
        self.assertEqual(protected_accelerator["decision"], "REQUIRE_FRESH_HUMAN")
        self.assertEqual(protected_accelerator["protection_matches"][0]["protected_accelerators"], ["gpu-premium"])

        site_b = {"cluster_id": "cluster-b", "cluster_identity_verified": True, "policy": {}}
        empty_policy_b = {
            "cluster_id": "cluster-b",
            "policy_version": "policy-1",
            "protected_partitions": [],
            "protected_accelerators": [],
            "scope_confirmed_by_human": True,
        }
        same_partition_other_cluster = helper.protected_cancel_decision(
            site_b,
            empty_policy_b,
            [dict(target, job_id="5101", cluster_id="cluster-b", candidate_partitions=["premium"])],
            "run-current",
            target_set_complete=True,
        )
        self.assertEqual(same_partition_other_cluster["decision"], "ALLOW_OWNED_UNPROTECTED")

        array_targets = [
            dict(target, job_id="4200_1"),
            dict(target, job_id="4200_2"),
        ]
        expanded_array = helper.protected_cancel_decision(
            site_a,
            protected_policy,
            array_targets,
            "run-current",
            action="cancel_array_elements",
            target_set_complete=True,
        )
        self.assertEqual(expanded_array["decision"], "ALLOW_OWNED_UNPROTECTED")
        self.assertEqual(expanded_array["target_ids"], ["4200_1", "4200_2"])

        fail_closed_cases = [
            helper.protected_cancel_decision(site_a, protected_policy, [target], "run-current", target_set_complete=False),
            helper.protected_cancel_decision(site_a, {}, [target], "run-current", target_set_complete=True),
            helper.protected_cancel_decision(
                {"cluster_id": "cluster-a", "cluster_identity_verified": False},
                protected_policy,
                [target],
                "run-current",
                target_set_complete=True,
            ),
            helper.protected_cancel_decision(
                {"cluster_id": "cluster-a", "cluster_identity_verified": True, "policy": "UNKNOWN"},
                protected_policy,
                [target],
                "run-current",
                target_set_complete=True,
            ),
            helper.protected_cancel_decision(
                site_a,
                protected_policy,
                [{key: value for key, value in target.items() if key != "requested_accelerators"}],
                "run-current",
                target_set_complete=True,
            ),
            helper.protected_cancel_decision(
                site_a,
                protected_policy,
                [dict(target, job_id="4200_[1-4]")],
                "run-current",
                target_set_complete=True,
            ),
        ]
        for decision in fail_closed_cases:
            self.assertEqual(decision["decision"], "DENY_UNKNOWN_OR_FORBIDDEN")

        prohibited = helper.protected_cancel_decision(
            {"cluster_id": "cluster-a", "cluster_identity_verified": True, "policy": {"cancel_execution": "forbidden"}},
            protected_policy,
            [target],
            "run-current",
            target_set_complete=True,
        )
        self.assertEqual(prohibited["decision"], "DENY_UNKNOWN_OR_FORBIDDEN")
        self.assertEqual(prohibited["reason"], "explicit_site_prohibition")

        site_protected = helper.protected_cancel_decision(
            {
                "cluster_id": "cluster-a",
                "cluster_identity_verified": True,
                "policy": {"protected_partitions": ["ordinary"]},
            },
            protected_policy,
            [target],
            "run-current",
            target_set_complete=True,
        )
        self.assertEqual(site_protected["decision"], "REQUIRE_FRESH_HUMAN")

        private_fields = {
            "cancel_policy_version": "policy-7",
            "cancel_policy_confirmed": "true",
            "protected_partitions": "premium,priority",
            "protected_accelerators": "gpu-premium",
        }
        parsed_policy = skills.environment_cancel_protection_policy(private_fields, "cluster-a")
        self.assertEqual(parsed_policy["protected_partitions"], ["premium", "priority"])
        self.assertEqual(parsed_policy["protected_accelerators"], ["gpu-premium"])
        self.assertTrue(parsed_policy["scope_confirmed_by_human"])
        self.assertNotIn("protected_partitions", skills.environment_public_override_policy(private_fields))
        self.assertNotIn("protected_accelerators", skills.environment_public_override_policy(private_fields))

    def test_cancel_g2_fresh_human_representation_is_exact_and_non_authorizing(self) -> None:
        helper = load_helper()
        site = {"cluster_id": "cluster-a", "cluster_identity_verified": True, "policy": {}}
        policy = {
            "cluster_id": "cluster-a",
            "policy_version": "policy-7",
            "protected_partitions": ["premium"],
            "protected_accelerators": [],
            "scope_confirmed_by_human": True,
        }
        target = {
            "job_id": "6101",
            "cluster_id": "cluster-a",
            "state": "PENDING",
            "candidate_partitions": ["premium"],
            "requested_accelerators": [],
            "owner_run_id": "run-current",
            "cancel_responsibility": True,
            "facts_verified": True,
            "ownership_verified": True,
        }
        request = helper.cancel_confirmation_request(
            site,
            policy,
            [target],
            "run-current",
            target_set_complete=True,
        )
        self.assertIsNotNone(request)
        assert request is not None
        self.assertEqual(request["default_choice"], "retain")
        self.assertFalse(request["execution_authorized"])
        self.assertNotIn("scancel", request["message"])
        self.assertEqual(request["target_facts"][0]["partitions"], ["premium"])
        self.assertEqual(request["target_facts"][0]["accelerators"], [])

        receipt = {
            "confirmation_id": "human-channel-confirmation-1",
            "source": "independent_human_channel",
            "identity_verified": True,
            "human_identity": "user-a",
            "choice": "confirm_cancel_exact_targets",
            "single_use": True,
            "consumed": False,
            "action": "cancel_job",
            "binding_digest": request["binding_digest"],
            "target_ids": request["target_ids"],
            "policy_version": request["policy_version"],
            "issued_at": "2026-10-15T12:00:00+00:00",
            "expires_at": "2026-10-15T12:03:00+00:00",
        }
        valid = helper.validate_cancel_confirmation(
            receipt,
            site,
            policy,
            [target],
            "run-current",
            expected_human_identity="user-a",
            now="2026-10-15T12:01:00+00:00",
            target_set_complete=True,
        )
        self.assertTrue(valid["valid"])
        self.assertFalse(valid["execution_authorized"])

        for source in ("goal", "race_opt_in", "auto_review", "hook", "model_receipt", "scancel_interactive"):
            with self.subTest(source=source):
                rejected = helper.validate_cancel_confirmation(
                    dict(receipt, source=source),
                    site,
                    policy,
                    [target],
                    "run-current",
                    expected_human_identity="user-a",
                    now="2026-10-15T12:01:00+00:00",
                    target_set_complete=True,
                )
                self.assertFalse(rejected["valid"])
                self.assertEqual(rejected["reason"], "untrusted_confirmation_source")

        expired = helper.validate_cancel_confirmation(
            receipt,
            site,
            policy,
            [target],
            "run-current",
            expected_human_identity="user-a",
            now="2026-10-15T12:04:00+00:00",
            target_set_complete=True,
        )
        self.assertFalse(expired["valid"])
        self.assertEqual(expired["reason"], "confirmation_expired_or_not_yet_valid")

        changed_state = helper.validate_cancel_confirmation(
            receipt,
            site,
            policy,
            [dict(target, state="RUNNING")],
            "run-current",
            expected_human_identity="user-a",
            now="2026-10-15T12:01:00+00:00",
            target_set_complete=True,
        )
        self.assertFalse(changed_state["valid"])
        self.assertEqual(changed_state["reason"], "target_policy_or_state_changed")

        changed_policy = helper.validate_cancel_confirmation(
            receipt,
            site,
            dict(policy, policy_version="policy-8"),
            [target],
            "run-current",
            expected_human_identity="user-a",
            now="2026-10-15T12:01:00+00:00",
            target_set_complete=True,
        )
        self.assertFalse(changed_policy["valid"])
        self.assertEqual(changed_policy["reason"], "target_policy_or_state_changed")

        added_target = helper.validate_cancel_confirmation(
            receipt,
            site,
            policy,
            [target, dict(target, job_id="6102")],
            "run-current",
            expected_human_identity="user-a",
            now="2026-10-15T12:01:00+00:00",
            target_set_complete=True,
        )
        self.assertFalse(added_target["valid"])
        self.assertEqual(added_target["reason"], "target_policy_or_state_changed")

        no_cancel = helper.protected_cancel_decision(
            site,
            policy,
            [target],
            "run-current",
            action="natural_step_completion",
            target_set_complete=True,
        )
        self.assertIsNone(no_cancel["decision"])
        self.assertFalse(no_cancel["confirmation_required"])
        self.assertIsNone(
            helper.cancel_confirmation_request(
                site,
                policy,
                [target],
                "run-current",
                action="natural_step_completion",
                target_set_complete=True,
            )
        )

    def test_cancel_g4_old_jobs_indirect_actions_and_replacement_stay_closed(self) -> None:
        helper = load_helper()
        site = {"cluster_id": "cluster-a", "cluster_identity_verified": True, "policy": {}}
        policy = {
            "cluster_id": "cluster-a",
            "policy_version": "policy-1",
            "protected_partitions": [],
            "protected_accelerators": [],
            "scope_confirmed_by_human": True,
        }
        old_target = {
            "job_id": "7101",
            "cluster_id": "cluster-a",
            "state": "RUNNING",
            "partition": "ordinary",
            "allocated_accelerators": [],
            "owner_run_id": "older-run",
            "cancel_responsibility": False,
            "facts_verified": True,
            "ownership_verified": True,
        }
        for action in (
            "cancel_job",
            "cancel_job_set",
            "cancel_array_elements",
            "cancel_via_api",
            "release_allocation",
            "terminate_allocation_holder",
        ):
            with self.subTest(action=action):
                decision = helper.protected_cancel_decision(
                    site,
                    policy,
                    [old_target],
                    "run-current",
                    action=action,
                    target_set_complete=True,
                )
                self.assertEqual(decision["decision"], "REQUIRE_FRESH_HUMAN")
                self.assertFalse(decision["execution_authorized"])

        unknown_result = helper.bounded_replacement_decision(
            {"poll_interval_seconds": 300, "replacement_reason": "route_change"},
            {"state": "PENDING", "inactive_confirmed": False},
        )
        self.assertEqual(unknown_result["action"], "fail_closed")
        self.assertEqual(unknown_result["reason"], "old_job_uncertain")

    def test_cancel_g5_installed_normal_entry_loads_offline_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            override = Path(tmp) / "local-overrides.toml"
            override.write_text(
                "[sites.third-party]\n"
                "local_site_id = \"third-party\"\n"
                "cancel_policy_version = \"policy-1\"\n"
                "cancel_policy_confirmed = \"true\"\n"
                "protected_partitions = \"premium\"\n"
                "protected_accelerators = \"gpu-premium\"\n",
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
            with mock.patch.dict(os.environ, {"PATH": str(Path(tmp) / "empty-bin")}, clear=False):
                plan = skills.environment_plan_payload(args)
                skills.environment_apply_plan(args, plan)
            installed = skills.environment_target_root(args) / "slurm-workflows"
            installed_helper = load_helper(installed / "scripts" / "slurm_routing.py")
            local_data, errors = skills.parse_environment_local_override(override)
            self.assertEqual(errors, [])
            private_policy = skills.environment_cancel_protection_policy(local_data["third-party"], "third-party")
            decision = installed_helper.protected_cancel_decision(
                {"cluster_id": "third-party", "cluster_identity_verified": True, "policy": {}},
                private_policy,
                [
                    {
                        "job_id": "8101",
                        "cluster_id": "third-party",
                        "state": "PENDING",
                        "partition": "premium",
                        "requested_accelerators": ["gpu-standard"],
                        "owner_run_id": "run-current",
                        "cancel_responsibility": True,
                        "facts_verified": True,
                        "ownership_verified": True,
                    }
                ],
                "run-current",
                target_set_complete=True,
            )
            generated_reference = (installed / "references" / "_generated" / "site-profile.md").read_text(encoding="utf-8")
        self.assertEqual(decision["decision"], "REQUIRE_FRESH_HUMAN")
        self.assertFalse(decision["execution_authorized"])
        self.assertNotIn("premium", generated_reference)
        self.assertNotIn("gpu-premium", generated_reference)

    def test_cancel_normal_entry_evaluation_is_fail_closed_and_non_mutating(self) -> None:
        helper = load_helper()
        with tempfile.TemporaryDirectory() as tmp:
            override = Path(tmp) / "local-overrides.toml"
            override.write_text(
                "[sites.cluster-a]\n"
                "local_site_id = \"cluster-a\"\n"
                "cancel_policy_version = \"policy-1\"\n"
                "cancel_policy_confirmed = true\n"
                "protected_partitions = \"premium\"\n"
                "protected_accelerators = \"h100\"\n",
                encoding="utf-8",
            )
            live = {
                "local_site_id": "cluster-a",
                "fact_provenance": {"cluster_name": "LIVE_KNOWN"},
            }

            def fake_run(argv, timeout=5.0):
                self.assertEqual(argv[:4], ["scontrol", "show", "job", "-o"])
                job_id = argv[4]
                partition = "premium" if job_id == "9101" else "ordinary"
                accelerator = "h100" if job_id == "9101" else "a100"
                return (
                    0,
                    f"JobId={job_id} JobState=PENDING Partition={partition} "
                    f"UserId=tester(1000) Gres=gpu:{accelerator}:1 Dependency=(null)\n",
                    "",
                )

            with (
                mock.patch.object(helper, "discover_live_site_context", return_value=live),
                mock.patch.object(helper, "_run", side_effect=fake_run),
                mock.patch.object(helper, "_current_os_user", return_value="tester"),
            ):
                protected = helper.safe_cancel_jobs(
                    ["9101"], ["9101"], "run-current", "cluster-a", override, execute=False
                )
                allowed = helper.safe_cancel_jobs(
                    ["9102"], ["9102"], "run-current", "cluster-a", override, execute=False
                )
                old_job = helper.safe_cancel_jobs(
                    ["9102"], [], "run-current", "cluster-a", override, execute=False
                )

        self.assertEqual(protected["decision"], "REQUIRE_FRESH_HUMAN")
        self.assertFalse(protected["executed"])
        self.assertEqual(protected["human_request"]["target_ids"], ["9101"])
        self.assertEqual(allowed["decision"], "ALLOW_OWNED_UNPROTECTED")
        self.assertFalse(allowed["executed"])
        self.assertIsNone(allowed["human_request"])
        self.assertEqual(old_job["decision"], "REQUIRE_FRESH_HUMAN")
        self.assertEqual(old_job["reason"], "not_owned_by_current_run")
        self.assertFalse(old_job["executed"])

    def test_cancel_installed_safe_cancel_cli_retains_protected_target(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            override = Path(tmp) / "local-overrides.toml"
            override.write_text(
                "[sites.cluster-a]\n"
                "local_site_id = \"cluster-a\"\n"
                "cancel_policy_version = \"policy-1\"\n"
                "cancel_policy_confirmed = true\n"
                "protected_partitions = \"premium\"\n"
                "protected_accelerators = \"h100\"\n",
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
            with mock.patch.dict(os.environ, {"PATH": str(Path(tmp) / "empty-bin")}, clear=False):
                plan = skills.environment_plan_payload(args)
                skills.environment_apply_plan(args, plan)
            installed = skills.environment_target_root(args) / "slurm-workflows"
            installed_helper = load_helper(installed / "scripts" / "slurm_routing.py")
            live = {
                "local_site_id": "cluster-a",
                "fact_provenance": {"cluster_name": "LIVE_KNOWN"},
            }

            def fake_run(argv, timeout=5.0):
                self.assertEqual(argv, ["scontrol", "show", "job", "-o", "9201"])
                return (
                    0,
                    "JobId=9201 JobState=RUNNING Partition=premium "
                    "UserId=tester(1000) Gres=gpu:h100:1 Dependency=(null)\n",
                    "",
                )

            output = io.StringIO()
            with (
                mock.patch.object(installed_helper, "discover_live_site_context", return_value=live),
                mock.patch.object(installed_helper, "_run", side_effect=fake_run),
                mock.patch.object(installed_helper, "_current_os_user", return_value="tester"),
                contextlib.redirect_stdout(output),
            ):
                rc = installed_helper.main(
                    [
                        "safe-cancel",
                        "--job-id", "9201",
                        "--owned-job-id", "9201",
                        "--current-run-id", "run-current",
                        "--site-id", "cluster-a",
                        "--local-override", str(override),
                    ]
                )

        result = json.loads(output.getvalue())
        self.assertEqual(rc, 0)
        self.assertEqual(result["decision"], "REQUIRE_FRESH_HUMAN")
        self.assertFalse(result["executed"])
        self.assertEqual(result["human_request"]["default_choice"], "retain")

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
        base_family = {
            "local_site_id": "site-a",
            "capacity_family_id": "weekly-gpu",
            "timezone": "America/New_York",
            "activation_scope": {"family_id": "weekly-gpu", "accelerator_requirement": "h100"},
            "accepted_resource_contract": {"gpus": 1, "gpu_type": "h100"},
            "allowed_resource_envelope": {"gpus": 1, "gpu_type": "h100"},
            "recurrence": {"weekday": "mon", "start_time": "09:00", "duration_hours": 8},
            "minimum_useful_duration": "6h",
            "successor_lead_time": "12h",
            "site_capabilities": {"calendar_submit_verified": True},
            "auto_maintain_successor": True,
        }
        family = json.loads(json.dumps(base_family))
        invocation = {
            "mode": "persistent",
            "family_id": "weekly-gpu",
            "accelerator_requirement": "h100",
            "now": "2026-09-27T12:00:00+00:00",
        }
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
                [{"lifecycle_owned": True, "gpus": 1, "gpu_type": "h100", "requested_start": "2026-09-28T08:00:00-04:00", "end_time": "2026-09-28T18:00:00-04:00"}],
                invocation,
            )["action"],
            "keep_successor",
        )
        self.assertEqual(
            helper.capacity_reconcile(
                family,
                [],
                [
                    {"lifecycle_owned": True, "gpus": 1, "gpu_type": "h100", "requested_start": "2026-09-28T08:00:00-04:00", "end_time": "2026-09-28T18:00:00-04:00"},
                    {"lifecycle_owned": True, "gpus": 1, "gpu_type": "h100", "requested_start": "2026-09-28T08:00:00-04:00", "end_time": "2026-09-28T18:00:00-04:00"},
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
        planned = helper.capacity_reconcile(family, [], [], invocation)
        self.assertEqual(planned["action"], "plan_one_successor")
        self.assertEqual(planned["target_window"]["start"], "2026-09-28T09:00:00-04:00")

        different_occurrence = json.loads(json.dumps(family))
        different_occurrence["target_occurrence"] = {
            "start": "2026-10-05T13:00:00+00:00",
            "end": "2026-10-05T21:00:00+00:00",
        }
        same_scope_plan = helper.capacity_reconcile(different_occurrence, [], [], invocation)
        self.assertEqual(same_scope_plan["action"], "plan_one_successor")
        self.assertEqual(same_scope_plan["target_window"]["start"], "2026-10-05T13:00:00+00:00")

        changed_window_scope = json.loads(json.dumps(family))
        changed_window_scope["minimum_useful_duration"] = "7h"
        self.assertEqual(
            helper.capacity_reconcile(changed_window_scope, [], [], invocation)["action"],
            "read_only_proposal",
        )
        changed_action_scope = json.loads(json.dumps(family))
        changed_action_scope["authorized_actions"] = {"cancel_stale_successor": True}
        self.assertEqual(
            helper.capacity_reconcile(changed_action_scope, [], [], invocation)["action"],
            "read_only_proposal",
        )
        changed_timezone_scope = json.loads(json.dumps(family))
        changed_timezone_scope["timezone"] = "UTC"
        self.assertEqual(
            helper.capacity_reconcile(changed_timezone_scope, [], [], invocation)["action"],
            "read_only_proposal",
        )
        invalid_timezone_scope = json.loads(json.dumps(family))
        invalid_timezone_scope["timezone"] = "Not/AZone"
        invalid_timezone_scope["enrollment"]["scope_digest"] = helper._scope_digest(invalid_timezone_scope)
        invalid_timezone = helper.capacity_reconcile(invalid_timezone_scope, [], [], invocation)
        self.assertEqual(invalid_timezone["action"], "read_only_proposal")
        self.assertEqual(invalid_timezone["reason"], "invalid_or_unavailable_timezone")
        self.assertFalse(invalid_timezone["successor_mutation"])

        gap_family = json.loads(json.dumps(family))
        gap_family["recurrence"] = {"weekday": "sun", "start_time": "02:30", "duration_hours": 8}
        gap_family["enrollment"] = {"submit_successor": True, "max_successor": 1, "scope_digest": helper._scope_digest(gap_family)}
        gap_plan = helper.capacity_reconcile(gap_family, [], [], {**invocation, "now": "2026-03-08T06:00:00+00:00"})
        self.assertEqual(gap_plan["action"], "read_only_proposal")
        self.assertEqual(gap_plan["reason"], "nonexistent_recurrence_local_time")
        self.assertFalse(gap_plan["successor_mutation"])

        fold_family = json.loads(json.dumps(family))
        fold_family["recurrence"] = {"weekday": "sun", "start_time": "01:30", "duration_hours": 8}
        fold_family["enrollment"] = {"submit_successor": True, "max_successor": 1, "scope_digest": helper._scope_digest(fold_family)}
        fold_plan = helper.capacity_reconcile(fold_family, [], [], {**invocation, "now": "2026-11-01T04:30:00+00:00"})
        self.assertEqual(fold_plan["action"], "read_only_proposal")
        self.assertEqual(fold_plan["reason"], "ambiguous_recurrence_local_time")
        self.assertFalse(fold_plan["successor_mutation"])

        monday_invocation = dict(invocation)
        monday_invocation["now"] = "2026-09-28T14:00:00+00:00"
        active_current = {
            "state": "RUNNING",
            "gpus": 1,
            "gpu_type": "h100",
            "start_time": "2026-09-28T08:00:00-04:00",
            "end_time": "2026-09-28T18:00:00-04:00",
        }
        future_successor = {
            "lifecycle_owned": True,
            "gpus": 1,
            "gpu_type": "h100",
            "requested_start": "2026-10-05T08:00:00-04:00",
            "end_time": "2026-10-05T18:00:00-04:00",
        }
        next_plan = helper.capacity_reconcile(family, [active_current], [], monday_invocation)
        self.assertEqual(next_plan["action"], "plan_one_successor")
        self.assertEqual(next_plan["target_window"]["start"], "2026-10-05T09:00:00-04:00")
        self.assertEqual(
            helper.capacity_reconcile(family, [active_current], [future_successor], monday_invocation)["action"],
            "keep_successor",
        )
        spanning_active = dict(active_current)
        spanning_active["end_time"] = "2026-10-06T18:00:00-04:00"
        spanning_plan = helper.capacity_reconcile(family, [spanning_active], [], monday_invocation)
        self.assertEqual(spanning_plan["action"], "plan_one_successor")
        self.assertEqual(spanning_plan["target_window"]["start"], "2026-10-12T09:00:00-04:00")
        current_window_plan = helper.capacity_reconcile(family, [], [], monday_invocation)
        self.assertEqual(current_window_plan["action"], "plan_one_successor")
        self.assertEqual(current_window_plan["target_window"]["start"], "2026-09-28T09:00:00-04:00")
        explicit_recurring = json.loads(json.dumps(family))
        explicit_recurring["target_occurrence"] = {
            "start": "2026-09-28T13:00:00+00:00",
            "end": "2026-09-28T21:00:00+00:00",
        }
        explicit_next_plan = helper.capacity_reconcile(explicit_recurring, [active_current], [], monday_invocation)
        self.assertEqual(explicit_next_plan["action"], "plan_one_successor")
        self.assertEqual(explicit_next_plan["target_window"]["start"], "2026-10-05T09:00:00-04:00")
        self.assertEqual(
            helper.capacity_reconcile(explicit_recurring, [active_current], [future_successor], monday_invocation)["action"],
            "keep_successor",
        )
        dst_invocation = dict(invocation)
        dst_invocation["now"] = "2026-10-26T14:00:00+00:00"
        dst_active = {
            "state": "RUNNING",
            "gpus": 1,
            "gpu_type": "h100",
            "start_time": "2026-10-26T08:00:00-04:00",
            "end_time": "2026-10-26T18:00:00-04:00",
        }
        dst_next_plan = helper.capacity_reconcile(family, [dst_active], [], dst_invocation)
        self.assertEqual(dst_next_plan["action"], "plan_one_successor")
        self.assertEqual(dst_next_plan["target_window"]["start"], "2026-11-02T09:00:00-05:00")
        explicit_dst = json.loads(json.dumps(family))
        explicit_dst["target_occurrence"] = {
            "start": "2026-10-26T13:00:00+00:00",
            "end": "2026-10-26T21:00:00+00:00",
        }
        explicit_dst_plan = helper.capacity_reconcile(explicit_dst, [dst_active], [], dst_invocation)
        self.assertEqual(explicit_dst_plan["action"], "plan_one_successor")
        self.assertEqual(explicit_dst_plan["target_window"]["start"], "2026-11-02T09:00:00-05:00")
        one_off = json.loads(json.dumps(family))
        one_off.pop("recurrence")
        one_off["target_occurrence"] = {
            "start": "2026-09-28T09:00:00-04:00",
            "end": "2026-09-28T17:00:00-04:00",
        }
        self.assertEqual(
            helper.capacity_reconcile(one_off, [active_current], [], monday_invocation)["action"],
            "reuse_active",
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

    def test_g6_installed_normal_entry_duplicate_race_bounded_gate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            override = Path(tmp) / "local-overrides.toml"
            override.write_text(
                "[sites.third-party]\nlocal_site_id = \"third-party\"\npartition_priority = \"h100-short,h100-main\"\n",
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
            skills.environment_apply_plan(args, plan)
            installed = skills.environment_target_root(args) / "slurm-workflows"
            installed_helper = load_helper(installed / "scripts" / "slurm_routing.py")
            workload = {
                "workload_scope_digest": "sha256:installed-race-smoke",
                "data": "cohort-a",
                "split": "fold-1",
                "model": "seg-v2",
                "endpoint": "train.py",
                "augmentation": "none",
                "gpus": 1,
                "gpu_type": "h100",
                "memory_mb": 65536,
                "cpus_per_task": 8,
                "walltime_minutes": 240,
                "training_budget": "full",
            }
            candidates = [
                {
                    "partition": "h100-short",
                    "qos": "normal",
                    "gpus": 1,
                    "gpu_type": "h100",
                    "memory_mb": 65536,
                    "cpus_per_task": 8,
                    "walltime_minutes": 240,
                    "workload_contract": workload,
                },
                {
                    "partition": "h100-main",
                    "qos": "normal",
                    "gpus": 1,
                    "gpu_type": "h100",
                    "memory_mb": 65536,
                    "cpus_per_task": 8,
                    "walltime_minutes": 240,
                    "workload_contract": workload,
                },
            ]
            cancellation = {
                "winner_rule": "first_running_job",
                "cancel_loser": True,
                "running_tie_policy": "keep_lowest_job_id_cancel_other",
            }
            allowed = installed_helper.bounded_duplicate_race_decision(
                {"race_execution": "disabled_by_default"},
                True,
                candidates,
                workload,
                cancellation,
            )
            unsafe_cancellation = installed_helper.bounded_duplicate_race_decision(
                {"race_execution": "disabled_by_default"},
                True,
                candidates,
                workload,
                dict(cancellation, running_tie_policy="keep_both"),
            )
        self.assertTrue(allowed["allowed"])
        self.assertEqual(allowed["reason"], "bounded_two_route_race")
        self.assertFalse(unsafe_cancellation["allowed"])
        self.assertEqual(unsafe_cancellation["reason"], "unsupported_running_tie_policy")

    def test_g6_installed_persistent_capacity_state_normal_entry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            override = Path(tmp) / "local-overrides.toml"
            override.write_text(
                "[sites.third-party]\nlocal_site_id = \"third-party\"\npartition_priority = \"pi-fast\"\n",
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
            skills.environment_apply_plan(args, plan)
            installed = skills.environment_target_root(args) / "slurm-workflows"
            installed_helper = load_helper(installed / "scripts" / "slurm_routing.py")
            state_path = Path(tmp) / "runtime-home" / ".config" / "ai-skills" / "slurm-workflows.toml"
            family = {
                "local_site_id": "third-party",
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
            family["enrollment"] = {"submit_successor": True, "max_successor": 1, "scope_digest": installed_helper._scope_digest(family)}
            state = installed_helper.load_workflow_state(state_path)
            installed_helper.persist_capacity_family(state, family, "artifact:capacity-review")
            installed_helper.save_workflow_state(state, state_path)
            loaded_family = installed_helper.load_workflow_state(state_path)["capacity_families"]["weekly-gpu"]
            invocation = {
                "mode": "persistent",
                "family_id": "weekly-gpu",
                "accelerator_requirement": "h100",
                "now": "2026-09-28T10:00:00+00:00",
            }
            active_current = {
                "state": "RUNNING",
                "gpus": 1,
                "gpu_type": "h100",
                "start_time": "2026-09-28T08:00:00+00:00",
                "end_time": "2026-09-28T18:00:00+00:00",
            }
            future_successor = {
                "lifecycle_owned": True,
                "gpus": 1,
                "gpu_type": "h100",
                "requested_start": "2026-10-05T08:00:00+00:00",
                "end_time": "2026-10-05T18:00:00+00:00",
            }

        missing_successor = installed_helper.capacity_reconcile(loaded_family, [active_current], [], invocation)
        self.assertEqual(missing_successor["action"], "plan_one_successor")
        self.assertEqual(missing_successor["target_window"]["start"], "2026-10-05T09:00:00+00:00")
        self.assertEqual(
            installed_helper.capacity_reconcile(loaded_family, [active_current], [future_successor], invocation)["action"],
            "keep_successor",
        )
        self.assertEqual(
            installed_helper.capacity_reconcile(
                loaded_family,
                [],
                [{"lifecycle_owned": True, "gpus": 0, "gpu_type": "cpu", "requested_start": "2026-10-05T08:00:00+00:00", "end_time": "2026-10-05T18:00:00+00:00"}],
                {"mode": "batch", "family_id": "cpu-maint", "accelerator_requirement": "cpu"},
            )["action"],
            "read_only",
        )

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
                local_policy = skills.environment_public_override_policy(local_data[plan["local_site_id"]])
                route = installed_helper.route_candidates(
                    live_context,
                    {"gpus": 1, "gpu_type": "h100", "accelerator_hard": True},
                    local_policy,
                )
            reference = (installed / "references" / "_generated" / "site-profile.md").read_text(encoding="utf-8")
            manifest_text = json.dumps(manifest, sort_keys=True)
        self.assertEqual(detected_rc, 0)
        self.assertEqual(plan["local_site_id"], "privateclustersecret")
        self.assertTrue(manifest["local_site_id"].startswith("local-slurm-"))
        self.assertNotEqual(manifest["local_site_id"], plan["local_site_id"])
        self.assertTrue(plan["runtime_available"])
        self.assertEqual(doctor["diagnostics"]["missing_required_fields"], [])
        self.assertEqual(route["decision"], "route")
        self.assertEqual(route["candidates"][0]["partition"], "pi-fast")
        self.assertIn("local_override_locator: local-override:", reference)
        self.assertNotIn(str(Path(tmp)), reference)
        self.assertNotIn(str(Path(tmp)), manifest_text)
        self.assertNotIn("PrivateClusterSecret", reference)
        self.assertNotIn("privateclustersecret", reference.lower())
        self.assertNotIn("privateclustersecret", manifest_text.lower())
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
