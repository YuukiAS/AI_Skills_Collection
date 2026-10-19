from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import pwd
import subprocess
import sys
import tempfile
import tomllib
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "skills/tools/hpc/slurm-workflows/scripts"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def executable(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    path.chmod(0o700)
    return path


class HostHookFixture:
    def __init__(self, root: Path, jobs: dict[str, dict[str, str]]) -> None:
        self.project = root / "project"
        self.project.mkdir()
        self.codex_home = root / "codex-home"
        self.private = self.codex_home / "slurm-protected-cancel"
        self.hooks = self.private / "hooks"
        self.hooks.mkdir(parents=True, mode=0o700)
        self.private.chmod(0o700)
        self.hooks.chmod(0o700)
        (self.private / "consumed").mkdir(mode=0o700)

        source = (SCRIPTS / "slurm_cancel_hook.py").read_bytes()
        digest = hashlib.sha256(source).hexdigest()
        self.hook = self.hooks / f"slurm-protected-cancel-{digest}.py"
        self.hook.write_bytes(source)
        self.hook.chmod(0o700)

        self.state = root / "scheduler-state.json"
        self.set_jobs(jobs)
        self.mutations = root / "mutations.jsonl"
        user = pwd.getpwuid(os.geteuid()).pw_name
        self.scontrol = executable(
            root / "fake-host/scontrol",
            "#!/usr/bin/python3\n"
            "import json, sys\n"
            f"state = json.load(open({str(self.state)!r}, encoding='utf-8'))\n"
            "job = sys.argv[-1]\n"
            "record = state.get(job)\n"
            "if record is None: raise SystemExit(1)\n"
            f"user = {user!r}\n"
            "print(' '.join([f'JobId={job}', f\"JobState={record['state']}\", "
            "f\"Partition={record['partition']}\", f'UserId={user}(1000)', "
            "f\"ArrayJobId={record.get('array_job_id', '(null)')}\", "
            "f\"HetJobId={record.get('het_job_id', '(null)')}\"]))\n",
        )
        self.scancel = executable(
            root / "fake-host/scancel",
            "#!/usr/bin/python3\n"
            "import json, sys\n"
            f"with open({str(self.mutations)!r}, 'a', encoding='utf-8') as stream:\n"
            "    stream.write(json.dumps(sys.argv[1:]) + '\\n')\n",
        )
        policy = self.private / "policy.toml"
        policy.write_text('protected_cancel_partitions = ["htzhulab"]\n', encoding="utf-8")
        policy.chmod(0o600)
        runtime = {
            "schema_version": 4,
            "codex_home": str(self.codex_home),
            "hook_path": str(self.hook),
            "hook_sha256": digest,
            "policy_path": str(policy),
            "policy_sha256": hashlib.sha256(policy.read_bytes()).hexdigest(),
            "scontrol_path": str(self.scontrol),
            "scontrol_path_realpath": str(self.scontrol.resolve()),
            "scontrol_invocation_path": str(self.scontrol),
            "scancel_path": str(self.scancel),
            "scancel_path_realpath": str(self.scancel.resolve()),
            "scancel_invocation_path": str(self.scancel),
            "operation": "ordinary_cancel",
        }
        runtime_path = self.private / "runtime.json"
        runtime_path.write_text(json.dumps(runtime) + "\n", encoding="utf-8")
        runtime_path.chmod(0o600)

    def set_jobs(self, jobs: dict[str, dict[str, str]]) -> None:
        self.state.write_text(json.dumps(jobs) + "\n", encoding="utf-8")

    def mutation_argvs(self) -> list[list[str]]:
        if not self.mutations.exists():
            return []
        return [json.loads(line) for line in self.mutations.read_text(encoding="utf-8").splitlines()]

    def invoke(self, event: dict[str, object]) -> tuple[int, dict[str, object] | None, str]:
        completed = subprocess.run(
            [sys.executable, str(self.hook)],
            input=json.dumps(event),
            cwd=self.project,
            text=True,
            capture_output=True,
            check=False,
            timeout=10,
        )
        payload = json.loads(completed.stdout) if completed.stdout.strip() else None
        return completed.returncode, payload, completed.stderr

    def shell_event(self, event_name: str, command: str) -> dict[str, object]:
        return {
            "hook_event_name": event_name,
            "tool_name": "Bash",
            "tool_input": {"command": command},
            "cwd": str(self.project),
            "session_id": "session-1",
            "turn_id": "turn-1",
            "tool_use_id": f"tool-{event_name}",
        }

    def pre(self, command: str):
        return self.invoke(self.shell_event("PreToolUse", command))

    def permission(self, command: str):
        return self.invoke(self.shell_event("PermissionRequest", command))

    def post(self, question: dict[str, object], answer: object, **extra: object):
        event: dict[str, object] = {
            "hook_event_name": "PostToolUse",
            "tool_name": "request_user_input",
            "tool_input": {"questions": [question]},
            "tool_response": answer,
            "cwd": str(self.project),
            "session_id": "session-1",
            "turn_id": "turn-2",
            "tool_use_id": "tool-answer-1",
        }
        event.update(extra)
        return self.invoke(event)


def denial_reason(payload: dict[str, object], event_name: str) -> str:
    output = payload["hookSpecificOutput"]
    assert isinstance(output, dict)
    if event_name == "PreToolUse":
        return str(output["permissionDecisionReason"])
    decision = output["decision"]
    assert isinstance(decision, dict)
    return str(decision["message"])


def protected_question(payload: dict[str, object], event_name: str = "PreToolUse") -> dict[str, object]:
    reason = denial_reason(payload, event_name)
    marker = reason.find("{")
    assert marker >= 0
    return json.loads(reason[marker:])["request_user_input"]["questions"][0]


class TestGlobalHostHook(unittest.TestCase):
    def test_nonprotected_adds_no_protected_decision_or_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), {"9101": {"partition": "general", "state": "PENDING"}})
            for invoke in (fixture.pre, fixture.permission):
                code, payload, _ = invoke("scancel 9101")
                self.assertEqual((code, payload), (0, {}))
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_protected_pre_and_permission_deny_without_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), {"9101": {"partition": "htzhulab", "state": "PENDING"}})
            for name, invoke in (("PreToolUse", fixture.pre), ("PermissionRequest", fixture.permission)):
                _, payload, _ = invoke("scancel 9101")
                assert payload is not None
                output = payload["hookSpecificOutput"]
                self.assertEqual(output["hookEventName"], name)
                question = protected_question(payload, name)
                self.assertEqual(question["id"], "slurm-protected-cancel:9101")
                self.assertEqual(question["header"], "取消受保护作业")
                self.assertEqual(question["question"], "Job 9101 当前位于受保护分区 htzhulab。确认取消这个 Job 吗？")
                self.assertEqual([item["label"] for item in question["options"]], ["确认取消", "保留 Job"])
                self.assertFalse(question["isOther"])
                self.assertFalse(question["isSecret"])
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_explicit_confirmation_executes_once_and_replay_is_zero(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), {"5001": {"partition": "htzhulab", "state": "PENDING"}})
            _, first, _ = fixture.pre("scancel 5001")
            assert first is not None
            question = protected_question(first)
            answer = {"answers": {question["id"]: {"answers": ["确认取消"]}}}
            _, confirmed, _ = fixture.post(question, answer)
            self.assertEqual(confirmed["protected_cancel"], "executed")
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])
            _, replay, _ = fixture.post(question, answer)
            self.assertEqual(replay["reason"], "replayed_or_duplicate_confirmation")
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])

    def test_negative_responses_and_nonroot_events_never_cancel(self) -> None:
        cases = [
            {"answers": {}},
            {"answers": {"slurm-protected-cancel:5001": {"answers": ["保留 Job"]}}},
            {"answers": {"slurm-protected-cancel:5001": {"answers": ["Other"]}}},
            {"answers": {"slurm-protected-cancel:5001": {"answers": ["请取消"]}}},
        ]
        for response in cases:
            with self.subTest(response=response), tempfile.TemporaryDirectory() as temp:
                fixture = HostHookFixture(Path(temp), {"5001": {"partition": "htzhulab", "state": "PENDING"}})
                _, first, _ = fixture.pre("scancel 5001")
                question = protected_question(first)
                fixture.post(question, response)
                self.assertEqual(fixture.mutation_argvs(), [])
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), {"5001": {"partition": "htzhulab", "state": "PENDING"}})
            _, first, _ = fixture.pre("scancel 5001")
            question = protected_question(first)
            answer = {"answers": {question["id"]: {"answers": ["确认取消"]}}}
            fixture.post(question, answer, agent_id="subagent-1")
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_target_or_partition_change_fails_closed(self) -> None:
        for jobs in ({}, {"5001": {"partition": "general", "state": "PENDING"}}, {"5001": {"partition": "htzhulab", "state": "COMPLETED"}}):
            with self.subTest(jobs=jobs), tempfile.TemporaryDirectory() as temp:
                fixture = HostHookFixture(Path(temp), {"5001": {"partition": "htzhulab", "state": "PENDING"}})
                _, first, _ = fixture.pre("scancel 5001")
                question = protected_question(first)
                fixture.set_jobs(jobs)
                answer = {"answers": {question["id"]: {"answers": ["确认取消"]}}}
                fixture.post(question, answer)
                self.assertEqual(fixture.mutation_argvs(), [])

    def test_multi_target_authority_binds_exact_set(self) -> None:
        jobs = {
            "1001": {"partition": "general", "state": "PENDING"},
            "1002": {"partition": "htzhulab", "state": "PENDING"},
        }
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), jobs)
            _, first, _ = fixture.pre("scancel 1001 1002")
            question = protected_question(first)
            answer = {"answers": {question["id"]: {"answers": ["确认取消"]}}}
            fixture.post(question, answer)
            self.assertEqual(fixture.mutation_argvs(), [["1001", "1002"]])

    def test_unsupported_target_and_untrusted_executable_fail_closed(self) -> None:
        commands = ("scancel --signal=KILL 1", "scancel 123_[1-4]", "scancel 123.batch", "/tmp/scancel 123", "scancel")
        for command in commands:
            with self.subTest(command=command), tempfile.TemporaryDirectory() as temp:
                fixture = HostHookFixture(Path(temp), {"123": {"partition": "general", "state": "PENDING"}})
                _, payload, _ = fixture.pre(command)
                self.assertEqual(payload["hookSpecificOutput"]["permissionDecision"], "deny")
                self.assertEqual(fixture.mutation_argvs(), [])

    def test_malformed_event_and_missing_runtime_never_use_path_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fixture = HostHookFixture(root, {"9101": {"partition": "htzhulab", "state": "PENDING"}})
            fallback_log = root / "fallback-called"
            executable(root / "path-bin/scancel", f"#!/bin/sh\ntouch {fallback_log}\n")
            completed = subprocess.run(
                [sys.executable, str(fixture.hook)],
                input="not-json",
                text=True,
                capture_output=True,
                env={**os.environ, "PATH": str(root / "path-bin")},
                check=False,
            )
            self.assertNotEqual(completed.returncode, 0)
            (fixture.private / "runtime.json").unlink()
            fixture.pre("scancel 9101")
            self.assertFalse(fallback_log.exists())

    def test_same_global_hook_works_from_four_unrelated_cwds(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fixture = HostHookFixture(root, {"9101": {"partition": "htzhulab", "state": "PENDING"}})
            for index in range(4):
                cwd = root / f"repo-{index}"
                cwd.mkdir()
                event = fixture.shell_event("PreToolUse", "scancel 9101")
                event["cwd"] = str(cwd)
                _, payload, _ = fixture.invoke(event)
                self.assertIn("NEEDS_INTERACTIVE_CHAT_CONFIRMATION", denial_reason(payload, "PreToolUse"))


class TestGlobalSetup(unittest.TestCase):
    def setUp(self) -> None:
        self.setup = load_module("setup_protected_cancel", SCRIPTS / "setup_protected_cancel.py")

    def test_render_has_three_user_hooks_and_no_named_permission_profile(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            codex_home = root / "codex-home"
            fake_scontrol = executable(root / "host/scontrol", "#!/bin/sh\nexit 0\n")
            fake_scancel = executable(root / "host/scancel", "#!/bin/sh\nexit 0\n")
            rendered = self.setup.render_global_contract(codex_home, SCRIPTS, fake_scontrol, fake_scancel, ["htzhulab"])
            self.assertEqual(set(rendered["hooks"]), {"PreToolUse", "PermissionRequest", "PostToolUse"})
            manifest = rendered["manifest"]
            self.assertEqual(len(manifest["hook_keys"]), 3)
            self.assertIn("/hooks/slurm-protected-cancel-", manifest["hook_path"])
            self.assertEqual(manifest["python_path"], str(Path(sys.executable).resolve()))
            for groups in rendered["hooks"].values():
                command = groups[0]["hooks"][0]["command"]
                self.assertIn(str(Path(sys.executable).resolve()), command)
                self.assertNotIn("exec /usr/bin/python3", command)
            original = (
                'default_permissions = "slurm-chat-guard"\n'
                '[features]\ndefault_mode_request_user_input = false\nhooks = true\n\n'
                '[permissions.slurm-chat-guard]\nextends = ":workspace"\n\n'
                '[permissions.keep-me]\nextends = ":workspace"\n'
            )
            updated = self.setup.update_user_config_text(original, rendered)
            parsed = tomllib.loads(updated)
            self.assertNotIn("default_permissions", parsed)
            self.assertNotIn("slurm-chat-guard", parsed.get("permissions", {}))
            self.assertNotIn("slurm-protected-cancel-global", parsed.get("permissions", {}))
            self.assertIn("keep-me", parsed["permissions"])
            self.assertTrue(parsed["features"]["default_mode_request_user_input"])
            self.assertEqual(set(parsed["hooks"]), {"PreToolUse", "PermissionRequest", "PostToolUse"})

    def test_hash_checked_launcher_runs_with_the_frozen_compatible_python(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), {})
            digest = hashlib.sha256(fixture.hook.read_bytes()).hexdigest()
            command = self.setup._hash_checked_command(
                fixture.hook,
                digest,
                Path(sys.executable).resolve(),
            )
            completed = subprocess.run(
                command,
                shell=True,
                input=json.dumps(fixture.shell_event("PreToolUse", "printf harmless")),
                text=True,
                capture_output=True,
                check=False,
                timeout=10,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(json.loads(completed.stdout), {})

    def test_install_has_no_wrapper_shim_or_path_interception(self) -> None:
        source = (SCRIPTS / "setup_protected_cancel.py").read_text(encoding="utf-8")
        hook = (SCRIPTS / "slurm_cancel_hook.py").read_text(encoding="utf-8")
        combined = source + hook
        for forbidden in ("automation-bin", "shutil.which", "command -v scancel", "PATH prepend", "ai-slurm-scancel"):
            self.assertNotIn(forbidden, combined)
        self.assertNotIn('default_permissions = "slurm-', combined)

    def test_rules_keep_scancel_on_ordinary_prompt_boundary(self) -> None:
        rules = self.setup._rules_text([Path("/fake/scancel")])
        self.assertIn('decision="prompt"', rules)
        self.assertNotIn("forbidden", rules)


if __name__ == "__main__":
    unittest.main()
