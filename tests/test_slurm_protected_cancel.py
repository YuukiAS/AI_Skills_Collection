from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import stat
import sys
import tempfile
import tomllib
from types import SimpleNamespace
import unittest
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "skills/tools/hpc/slurm-workflows/scripts"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def executable(path: Path, text: str = "#!/bin/sh\nexit 99\n") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    path.chmod(0o700)
    return path


def private_json(path: Path, value: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value) + "\n", encoding="utf-8")
    path.chmod(0o600)


class GuardTests(unittest.TestCase):
    def setUp(self) -> None:
        self.routing = load_module("slurm_routing_v21", SCRIPTS / "slurm_routing.py")

    def _override(self, root: Path, partitions: str = "htzhulab") -> Path:
        path = root / "local-overrides.toml"
        path.write_text(
            '[sites.longleaf]\nprotected_cancel_partitions = "' + partitions + '"\n',
            encoding="utf-8",
        )
        return path

    @staticmethod
    def _job(job_id: str, partition: str, state: str = "PENDING") -> str:
        return (
            f"JobId={job_id} JobState={state} Partition={partition} "
            "UserId=tester(1000) ArrayJobId=(null) HetJobId=(null)\n"
        )

    def test_protected_partition_returns_exact_native_request_without_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            override = self._override(root)
            scontrol = executable(root / "host/scontrol")
            scancel = executable(root / "host/scancel")
            with (
                mock.patch.object(self.routing, "_current_os_user", return_value="tester"),
                mock.patch.object(
                    self.routing,
                    "_run_absolute",
                    return_value=(0, self._job("1234", "htzhulab"), ""),
                ) as lookup,
                mock.patch.object(self.routing.subprocess, "run") as run,
            ):
                result = self.routing.guard_cancel_jobs(
                    ["1234"], "longleaf", override, scontrol, scancel
                )

        self.assertEqual(result["status"], "NEEDS_INTERACTIVE_CHAT_CONFIRMATION")
        self.assertEqual(result["mutation_count"], 0)
        self.assertEqual(lookup.call_count, 1)
        run.assert_not_called()
        request = result["human_requests"][0]["request_user_input"]["questions"][0]
        binder = load_module("slurm_cancel_binder_contract", SCRIPTS / "slurm_cancel_binder.py")
        self.assertEqual(
            request["question"],
            "Job 1234 当前位于受保护分区 htzhulab。确认取消这个 Job 吗？",
        )
        self.assertEqual(request["id"], binder._question_id("1234", "htzhulab"))
        self.assertEqual(request["options"], binder._expected_options())
        self.assertEqual(result["metadata_trust"], "UNTRUSTED_REQUEST_METADATA")

    def test_any_protected_target_blocks_the_whole_invocation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            responses = iter(
                [
                    (0, self._job("1001", "ordinary"), ""),
                    (0, self._job("1002", "htzhulab", "RUNNING"), ""),
                ]
            )
            with (
                mock.patch.object(self.routing, "_current_os_user", return_value="tester"),
                mock.patch.object(self.routing, "_run_absolute", side_effect=lambda *_: next(responses)),
                mock.patch.object(self.routing.subprocess, "run") as run,
            ):
                result = self.routing.guard_cancel_jobs(
                    ["1001", "1002"],
                    "longleaf",
                    self._override(root),
                    executable(root / "host/scontrol"),
                    executable(root / "host/scancel"),
                )
        self.assertEqual(result["status"], "NEEDS_INTERACTIVE_CHAT_CONFIRMATION")
        self.assertEqual(result["mutation_count"], 0)
        run.assert_not_called()

    def test_unprotected_target_is_revalidated_then_cancelled_exactly_once(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scontrol = executable(root / "host/scontrol")
            scancel = executable(root / "host/scancel")
            lookup = mock.Mock(return_value=(0, self._job("2001", "ordinary"), ""))
            completed = SimpleNamespace(returncode=0, stdout="", stderr="")
            with (
                mock.patch.object(self.routing, "_current_os_user", return_value="tester"),
                mock.patch.object(self.routing, "_run_absolute", lookup),
                mock.patch.object(self.routing.subprocess, "run", return_value=completed) as run,
                mock.patch.dict(os.environ, {"SCANCEL_TEST": "must-not-pass"}, clear=False),
            ):
                result = self.routing.guard_cancel_jobs(
                    ["2001"], "longleaf", self._override(root), scontrol, scancel
                )
        self.assertEqual(result["status"], "EXECUTED_UNPROTECTED_CANCEL")
        self.assertEqual(result["mutation_count"], 1)
        self.assertEqual(lookup.call_count, 2)
        run.assert_called_once()
        args, kwargs = run.call_args
        self.assertEqual(args[0], [str(scancel), "2001"])
        self.assertNotIn("SCANCEL_TEST", kwargs["env"])

    def test_target_change_and_non_exact_selectors_fail_closed(self) -> None:
        bad_ids = ["--state=PENDING", "123_[1-4]", "123+1", "123.batch", "123,124", ""]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            override = self._override(root)
            scontrol = executable(root / "host/scontrol")
            scancel = executable(root / "host/scancel")
            for value in bad_ids:
                with self.subTest(value=value), mock.patch.object(self.routing, "_run_absolute") as lookup:
                    result = self.routing.guard_cancel_jobs([value], "longleaf", override, scontrol, scancel)
                    self.assertEqual(result["status"], "DENY_UNKNOWN_OR_FORBIDDEN")
                    lookup.assert_not_called()

            responses = iter(
                [
                    (0, self._job("3001", "ordinary"), ""),
                    (0, self._job("3001", "htzhulab"), ""),
                ]
            )
            with (
                mock.patch.object(self.routing, "_current_os_user", return_value="tester"),
                mock.patch.object(self.routing, "_run_absolute", side_effect=lambda *_: next(responses)),
                mock.patch.object(self.routing.subprocess, "run") as run,
            ):
                result = self.routing.guard_cancel_jobs(["3001"], "longleaf", override, scontrol, scancel)
            self.assertEqual(result["reason"], "target_or_state_changed")
            run.assert_not_called()

    def test_missing_unknown_or_explicitly_forbidden_policy_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            scontrol = executable(root / "host/scontrol")
            scancel = executable(root / "host/scancel")
            policies = {
                "missing": "[sites.longleaf]\n",
                "unknown": '[sites.longleaf]\nprotected_cancel_partitions = "UNKNOWN"\n',
                "forbidden": (
                    '[sites.longleaf]\nprotected_cancel_partitions = "htzhulab"\n'
                    'cancel_execution = "forbidden"\n'
                ),
            }
            for name, value in policies.items():
                with self.subTest(name=name):
                    override = root / f"{name}.toml"
                    override.write_text(value, encoding="utf-8")
                    with mock.patch.object(self.routing, "_run_absolute") as lookup:
                        result = self.routing.guard_cancel_jobs(
                            ["4001"], "longleaf", override, scontrol, scancel
                        )
                    self.assertEqual(result["status"], "DENY_UNKNOWN_OR_FORBIDDEN")
                    lookup.assert_not_called()


class BinderTests(unittest.TestCase):
    def _fixture(self, root: Path):
        project = root / "project"
        private_root = project / ".codex/slurm-protected-cancel-private"
        binder_path = private_root / "bin/slurm-protected-cancel-binder"
        binder_path.parent.mkdir(parents=True)
        private_root.chmod(0o700)
        binder_path.write_bytes((SCRIPTS / "slurm_cancel_binder.py").read_bytes())
        binder_path.chmod(0o700)
        consumed = private_root / "consumed"
        consumed.mkdir(mode=0o700)
        host = root / "host"
        scontrol = executable(host / "scontrol")
        scancel = executable(host / "scancel")
        hook_digest = "a" * 64
        runtime = {
            "schema_version": 1,
            "project_root": str(project),
            "binder_path": str(binder_path),
            "binder_sha256": hashlib.sha256(binder_path.read_bytes()).hexdigest(),
            "session_hook_sha256": hook_digest,
            "scontrol_path": str(scontrol),
            "scancel_path": str(scancel),
            "protected_cancel_partitions": ["htzhulab"],
            "operation": "ordinary_cancel",
            "active_session_id": "session-1",
        }
        capability = {
            "schema_version": 1,
            "project_root": str(project),
            "session_id": "session-1",
            "hook_version": hook_digest,
            "capability": "b" * 64,
        }
        private_json(private_root / "runtime.json", runtime)
        private_json(private_root / "capability.key", capability)
        module = load_module("slurm_cancel_binder_v21", SCRIPTS / "slurm_cancel_binder.py")
        module.__file__ = str(binder_path)
        question = {
            "id": module._question_id("5001", "htzhulab"),
            "header": "确认取消",
            "question": "Job 5001 当前位于受保护分区 htzhulab。确认取消这个 Job 吗？",
            "options": module._expected_options(),
        }
        event = {
            "hook_event_name": "PostToolUse",
            "tool_name": "request_user_input",
            "cwd": str(project),
            "session_id": "session-1",
            "turn_id": "turn-1",
            "tool_use_id": "tool-1",
            "tool_input": {"questions": [question]},
            "tool_response": {"answers": {question["id"]: {"answers": ["确认取消"]}}},
        }
        return module, event, runtime, scontrol, scancel, private_root

    @staticmethod
    def _scheduler_result(job_id: str = "5001", partition: str = "htzhulab"):
        return SimpleNamespace(
            returncode=0,
            stdout=(
                f"JobId={job_id} JobState=PENDING Partition={partition} "
                "UserId=" + os.environ.get("USER", "") + "(1000) ArrayJobId=(null) HetJobId=(null)\n"
            ),
            stderr="",
        )

    def test_exact_confirmation_executes_once_and_replay_is_denied(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            module, event, _runtime, scontrol, scancel, private_root = self._fixture(Path(tmp))
            user = module.pwd.getpwuid(os.geteuid()).pw_name
            scheduler = SimpleNamespace(
                returncode=0,
                stdout=(
                    "JobId=5001 JobState=PENDING Partition=htzhulab "
                    f"UserId={user}(1000) ArrayJobId=(null) HetJobId=(null)\n"
                ),
                stderr="",
            )
            success = SimpleNamespace(returncode=0, stdout="", stderr="")
            output = io.StringIO()
            with (
                mock.patch.object(sys, "stdin", io.StringIO(json.dumps(event))),
                contextlib.redirect_stdout(output),
                mock.patch.object(module.subprocess, "run", side_effect=[scheduler, success]) as run,
            ):
                rc = module.main()
            self.assertEqual(rc, 0)
            self.assertEqual(run.call_args_list[0].args[0], [str(scontrol), "show", "job", "-o", "5001"])
            self.assertEqual(run.call_args_list[1].args[0], [str(scancel), "5001"])
            records = list((private_root / "consumed").glob("*.json"))
            self.assertEqual(len(records), 1)
            self.assertEqual(json.loads(records[0].read_text())["status"], "executed")

            with (
                mock.patch.object(sys, "stdin", io.StringIO(json.dumps(event))),
                contextlib.redirect_stdout(io.StringIO()),
                mock.patch.object(module.subprocess, "run", return_value=scheduler) as replay_run,
            ):
                replay_rc = module.main()
            self.assertEqual(replay_rc, 23)
            replay_run.assert_called_once_with(
                [str(scontrol), "show", "job", "-o", "5001"],
                check=False,
                capture_output=True,
                text=True,
                timeout=10,
            )

    def test_non_confirmation_and_subagent_events_never_resolve_or_cancel(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            module, event, *_rest = self._fixture(Path(tmp))
            cases = [
                {"answers": {}},
                {"answers": {event["tool_input"]["questions"][0]["id"]: {"answers": ["保留 Job"]}}},
                {"answers": {event["tool_input"]["questions"][0]["id"]: {"answers": ["Other"]}}},
            ]
            for response in cases:
                with self.subTest(response=response):
                    with (
                        mock.patch.object(sys, "stdin", io.StringIO(json.dumps({**event, "tool_response": response}))),
                        contextlib.redirect_stdout(io.StringIO()),
                        mock.patch.object(module.subprocess, "run") as run,
                    ):
                        self.assertEqual(module.main(), 11)
                        run.assert_not_called()
            subagent = {**event, "agent_id": "child-1"}
            with (
                mock.patch.object(sys, "stdin", io.StringIO(json.dumps(subagent))),
                contextlib.redirect_stdout(io.StringIO()),
                mock.patch.object(module.subprocess, "run") as run,
            ):
                self.assertEqual(module.main(), 4)
                run.assert_not_called()

    def test_digest_capability_operation_and_partition_mismatches_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            module, event, runtime, _scontrol, _scancel, private_root = self._fixture(root)
            mismatch_values = [
                ("binder_sha256", "0" * 64, 14),
                ("operation", "release_allocation", 15),
                ("active_session_id", "other-session", 17),
            ]
            for key, value, expected in mismatch_values:
                with self.subTest(key=key):
                    changed = dict(runtime, **{key: value})
                    private_json(private_root / "runtime.json", changed)
                    with (
                        mock.patch.object(sys, "stdin", io.StringIO(json.dumps(event))),
                        contextlib.redirect_stdout(io.StringIO()),
                        mock.patch.object(module.subprocess, "run") as run,
                    ):
                        self.assertEqual(module.main(), expected)
                        run.assert_not_called()
            private_json(private_root / "runtime.json", runtime)
            user = module.pwd.getpwuid(os.geteuid()).pw_name
            changed_partition = SimpleNamespace(
                returncode=0,
                stdout=(
                    "JobId=5001 JobState=PENDING Partition=ordinary "
                    f"UserId={user}(1000) ArrayJobId=(null) HetJobId=(null)\n"
                ),
                stderr="",
            )
            with (
                mock.patch.object(sys, "stdin", io.StringIO(json.dumps(event))),
                contextlib.redirect_stdout(io.StringIO()),
                mock.patch.object(module.subprocess, "run", return_value=changed_partition) as run,
            ):
                self.assertEqual(module.main(), 22)
                run.assert_called_once()

    def test_group_readable_private_material_is_rejected_before_scheduler_access(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            module, event, _runtime, _scontrol, _scancel, private_root = self._fixture(Path(tmp))
            (private_root / "capability.key").chmod(0o640)
            with (
                mock.patch.object(sys, "stdin", io.StringIO(json.dumps(event))),
                contextlib.redirect_stdout(io.StringIO()),
                mock.patch.object(module.subprocess, "run") as run,
            ):
                self.assertEqual(module.main(), 12)
                run.assert_not_called()


class SessionAndSetupTests(unittest.TestCase):
    def test_session_start_and_end_create_and_remove_private_capability(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "project"
            private_root = project / ".codex/slurm-protected-cancel-private"
            private_root.mkdir(parents=True, mode=0o700)
            private_root.chmod(0o700)
            session_path = project / ".codex/hooks/slurm-protected-cancel-session"
            session_path.parent.mkdir(parents=True)
            session_path.write_bytes((SCRIPTS / "slurm_cancel_session.py").read_bytes())
            session_path.chmod(0o700)
            digest = hashlib.sha256(session_path.read_bytes()).hexdigest()
            runtime = {
                "project_root": str(project),
                "session_hook_path": str(session_path),
                "session_hook_sha256": digest,
                "active_session_id": None,
            }
            private_json(private_root / "runtime.json", runtime)
            module = load_module("slurm_cancel_session_v21", SCRIPTS / "slurm_cancel_session.py")
            module.__file__ = str(session_path)
            start = {"hook_event_name": "SessionStart", "cwd": str(project), "session_id": "session-9"}
            with mock.patch.object(sys, "stdin", io.StringIO(json.dumps(start))):
                self.assertEqual(module.main(), 0)
            capability_path = private_root / "capability.key"
            capability = json.loads(capability_path.read_text())
            self.assertRegex(capability["capability"], r"^[0-9a-f]{64}$")
            self.assertEqual(capability["session_id"], "session-9")
            self.assertEqual(capability["hook_version"], digest)
            self.assertEqual(stat.S_IMODE(capability_path.stat().st_mode), 0o600)

            end = {"hook_event_name": "SessionEnd", "cwd": str(project), "session_id": "session-9"}
            with mock.patch.object(sys, "stdin", io.StringIO(json.dumps(end))):
                self.assertEqual(module.main(), 0)
            self.assertFalse(capability_path.exists())
            self.assertIsNone(json.loads((private_root / "runtime.json").read_text())["active_session_id"])

    def test_setup_render_freezes_absolute_paths_digests_hooks_rules_and_deny(self) -> None:
        setup = load_module("setup_protected_cancel_v21", SCRIPTS / "setup_protected_cancel.py")
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project = root / "candidate"
            project.mkdir()
            scontrol = executable(root / "host/scontrol")
            scancel = executable(root / "host/scancel")
            runtime_scripts = root / "production-install/scripts"
            runtime_scripts.mkdir(parents=True)
            (runtime_scripts / "slurm_routing.py").write_text("# production locator\n", encoding="utf-8")
            rendered = setup.render_contract(
                project,
                SCRIPTS,
                scontrol,
                scancel,
                "longleaf",
                root / "local-overrides.toml",
                ["htzhulab"],
                runtime_scripts,
            )
            files = rendered["files"]
            config = tomllib.loads(files[".codex/config.toml"].decode())
            self.assertEqual(config["default_permissions"], "slurm-chat-guard")
            self.assertFalse(config["bypass_hook_trust"])
            self.assertTrue(config["features"]["default_mode_request_user_input"])
            self.assertEqual(
                config["permissions"]["slurm-chat-guard"]["filesystem"][":workspace_roots"][".codex"],
                "deny",
            )
            hooks = json.loads(files[".codex/hooks.json"])
            post = hooks["hooks"]["PostToolUse"][0]
            self.assertEqual(post["matcher"], "^request_user_input$")
            command = post["hooks"][0]["command"]
            self.assertIn(str(project / setup.PRIVATE_REL / "bin/slurm-protected-cancel-binder"), command)
            self.assertIn(rendered["manifest"]["binder_sha256"], command)
            self.assertIn("/usr/bin/sha256sum", command)
            hashes = rendered["manifest"]["hook_current_hashes"]
            self.assertEqual(set(hashes), {"post_tool_use", "session_end", "session_start"})
            self.assertTrue(all(value.startswith("sha256:") and len(value) == 71 for value in hashes.values()))
            self.assertNotEqual(hashes["session_start"], hashes["session_end"])
            self.assertEqual(
                setup._normalized_hook_hash(
                    "SessionEnd",
                    {"hooks": [{"type": "command", "command": "echo fixed", "timeout": 10}]},
                    {"type": "command", "command": "echo fixed", "timeout": 10},
                ),
                "sha256:8991b928d4f8dd22193cb0ee3be87e870876b1334c521e7c4293cd64c6f9c5e7",
            )
            runtime = json.loads(files[str(setup.PRIVATE_REL / "runtime.json")])
            self.assertEqual(runtime["project_root"], str(project))
            self.assertEqual(runtime["scontrol_path"], str(scontrol))
            self.assertEqual(runtime["scancel_path"], str(scancel))
            self.assertEqual(runtime["protected_cancel_partitions"], ["htzhulab"])
            rules = files[".codex/rules/slurm-protected-cancel.rules"].decode()
            self.assertIn('pattern=["scancel"]', rules)
            self.assertIn('pattern=["/usr/bin/scancel"]', rules)
            shim = files[".codex/automation-bin/scancel"].decode()
            self.assertIn(str(runtime_scripts / "slurm_routing.py"), shim)
            self.assertNotIn(str(SCRIPTS / "slurm_routing.py"), shim)

            render_output = root / "rendered"
            setup.write_rendered(rendered, render_output, install=False)
            self.assertTrue((render_output / "protected-cancel-render-manifest.json").is_file())
            setup.write_rendered(rendered, project, install=True)
            self.assertFalse((project / "protected-cancel-render-manifest.json").exists())
            self.assertEqual(
                stat.S_IMODE((project / setup.PRIVATE_REL / "runtime.json").stat().st_mode),
                0o600,
            )

    def test_old_terminal_receipt_entry_is_not_a_normal_cli(self) -> None:
        routing = load_module("slurm_routing_v21_cli", SCRIPTS / "slurm_routing.py")
        self.assertFalse(hasattr(routing, "validate_cancel_confirmation"))
        with self.assertRaises(SystemExit), contextlib.redirect_stderr(io.StringIO()):
            routing.build_arg_parser().parse_args(["safe-cancel"])


if __name__ == "__main__":
    unittest.main()
