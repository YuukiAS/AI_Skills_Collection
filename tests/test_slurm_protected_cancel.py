from __future__ import annotations

import hashlib
import importlib.util
import json
import os
from pathlib import Path
import pwd
import shutil
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
        self.root = root
        self.project = root / "project"
        self.project.mkdir()
        self.private = self.project / ".codex/slurm-protected-cancel-private"
        self.private.mkdir(parents=True, mode=0o700)
        self.consumed = self.private / "consumed"
        self.consumed.mkdir(mode=0o700)
        self.hook = self.private / "slurm-cancel-hook"
        self.hook.write_bytes((SCRIPTS / "slurm_cancel_hook.py").read_bytes())
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
            "if record is None:\n"
            "    raise SystemExit(1)\n"
            f"user = {user!r}\n"
            "print(' '.join([\n"
            "    f'JobId={job}', f\"JobState={record['state']}\",\n"
            "    f\"Partition={record['partition']}\", f'UserId={user}(1000)',\n"
            "    f\"ArrayJobId={record.get('array_job_id', '(null)')}\",\n"
            "    f\"HetJobId={record.get('het_job_id', '(null)')}\",\n"
            "]))\n",
        )
        self.scancel = executable(
            root / "fake-host/scancel",
            "#!/usr/bin/python3\n"
            "import json, sys\n"
            f"with open({str(self.mutations)!r}, 'a', encoding='utf-8') as stream:\n"
            "    stream.write(json.dumps(sys.argv[1:]) + '\\n')\n",
        )
        runtime = {
            "schema_version": 2,
            "project_root": str(self.project),
            "hook_path": str(self.hook),
            "hook_sha256": hashlib.sha256(self.hook.read_bytes()).hexdigest(),
            "scontrol_path": str(self.scontrol),
            "scontrol_path_realpath": str(self.scontrol.resolve()),
            "scontrol_invocation_path": str(self.scontrol),
            "scancel_path": str(self.scancel),
            "scancel_path_realpath": str(self.scancel.resolve()),
            "scancel_invocation_path": str(self.scancel),
            "site_id": "fixture",
            "local_override": str(root / "unused.toml"),
            "protected_cancel_partitions": ["htzhulab"],
            "operation": "ordinary_cancel",
        }
        self.runtime = self.private / "runtime.json"
        self.runtime.write_text(json.dumps(runtime) + "\n", encoding="utf-8")
        self.runtime.chmod(0o600)

    def set_jobs(self, jobs: dict[str, dict[str, str]]) -> None:
        self.state.write_text(json.dumps(jobs) + "\n", encoding="utf-8")

    def mutation_argvs(self) -> list[list[str]]:
        if not self.mutations.exists():
            return []
        return [json.loads(line) for line in self.mutations.read_text(encoding="utf-8").splitlines()]

    def invoke(self, event: dict[str, object]) -> tuple[int, dict[str, object]]:
        completed = subprocess.run(
            [sys.executable, str(self.hook)],
            input=json.dumps(event),
            cwd=self.project,
            text=True,
            capture_output=True,
            check=False,
            timeout=10,
        )
        return completed.returncode, json.loads(completed.stdout)

    def pre(self, command: str) -> tuple[int, dict[str, object]]:
        return self.invoke(
            {
                "hook_event_name": "PreToolUse",
                "tool_name": "Bash",
                "tool_input": {"command": command},
                "cwd": str(self.project),
                "session_id": "session-1",
                "turn_id": "turn-1",
                "tool_use_id": "tool-pre-1",
            }
        )

    def post(self, question: dict[str, object], answer: object, *, tool_use_id: str = "tool-answer-1") -> tuple[int, dict[str, object]]:
        return self.invoke(
            {
                "hook_event_name": "PostToolUse",
                "tool_name": "request_user_input",
                "tool_input": {"questions": [question]},
                "tool_response": answer,
                "cwd": str(self.project),
                "session_id": "session-1",
                "turn_id": "turn-2",
                "tool_use_id": tool_use_id,
            }
        )


def protected_question(payload: dict[str, object]) -> dict[str, object]:
    output = payload["hookSpecificOutput"]
    assert isinstance(output, dict)
    reason = output["permissionDecisionReason"]
    assert isinstance(reason, str) and reason.startswith("NEEDS_INTERACTIVE_CHAT_CONFIRMATION ")
    request = json.loads(reason.split(" ", 1)[1])
    return request["request_user_input"]["questions"][0]


class TestHostHook(unittest.TestCase):
    def test_nonprotected_host_cancel_runs_once_and_rewrites_original_input(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), {"9101": {"partition": "a100-gpu", "state": "PENDING"}})
            code, payload = fixture.pre("scancel 9101")
            self.assertEqual(code, 0)
            output = payload["hookSpecificOutput"]
            self.assertEqual(output["permissionDecision"], "allow")
            self.assertEqual(
                output["updatedInput"],
                {"command": "printf '%s\\n' 'SCANCEL_COMPLETED_BY_HOST_HOOK jobs=9101'"},
            )
            self.assertEqual(fixture.mutation_argvs(), [["9101"]])

    def test_protected_first_attempt_is_zero_mutation_and_exact_native_question(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), {"9101": {"partition": "htzhulab", "state": "PENDING"}})
            code, payload = fixture.pre("scancel 9101")
            self.assertEqual(code, 0)
            output = payload["hookSpecificOutput"]
            self.assertEqual(output["permissionDecision"], "deny")
            question = protected_question(payload)
            self.assertEqual(question["header"], "取消受保护作业")
            self.assertEqual(question["question"], "Job 9101 当前位于受保护分区 htzhulab。确认取消这个 Job 吗？")
            self.assertEqual([option["label"] for option in question["options"]], ["确认取消", "保留 Job"])
            self.assertFalse(question["isOther"])
            self.assertFalse(question["isSecret"])
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_explicit_confirmation_executes_once_and_replay_is_zero(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), {"5001": {"partition": "htzhulab", "state": "PENDING"}})
            _, first = fixture.pre("scancel 5001")
            question = protected_question(first)
            answer = {"answers": {question["id"]: {"answers": ["确认取消"]}}}
            _, confirmed = fixture.post(question, answer)
            self.assertEqual(confirmed["protected_cancel"], "executed")
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])
            _, replay = fixture.post(question, answer)
            self.assertEqual(replay["reason"], "replayed_or_duplicate_confirmation")
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])

    def test_retain_empty_timeout_other_and_free_text_never_cancel(self) -> None:
        answers = {
            "retain": lambda q: {"answers": {q["id"]: {"answers": ["保留 Job"]}}},
            "empty": lambda q: {"answers": {}},
            "timeout": lambda q: {"answers": {}},
            "other": lambda q: {"answers": {q["id"]: {"answers": ["Other"]}}},
            "free_text": lambda q: {"answers": {q["id"]: {"answers": ["请取消"]}}},
        }
        for name, response in answers.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temp:
                fixture = HostHookFixture(Path(temp), {"5001": {"partition": "htzhulab", "state": "PENDING"}})
                _, first = fixture.pre("scancel 5001")
                question = protected_question(first)
                _, result = fixture.post(question, response(question))
                self.assertEqual(result["reason"], "not_explicit_confirmation")
                self.assertEqual(fixture.mutation_argvs(), [])

    def test_target_disappears_or_partition_changes_before_confirmation(self) -> None:
        for jobs in ({}, {"5001": {"partition": "a100-gpu", "state": "PENDING"}}):
            with self.subTest(jobs=jobs), tempfile.TemporaryDirectory() as temp:
                fixture = HostHookFixture(Path(temp), {"5001": {"partition": "htzhulab", "state": "PENDING"}})
                _, first = fixture.pre("scancel 5001")
                question = protected_question(first)
                fixture.set_jobs(jobs)
                answer = {"answers": {question["id"]: {"answers": ["确认取消"]}}}
                _, result = fixture.post(question, answer)
                self.assertIn(result["reason"], {"target_resolution_failed", "target_or_partition_changed"})
                self.assertEqual(fixture.mutation_argvs(), [])

    def test_multi_target_confirmation_binds_and_executes_the_exact_set_once(self) -> None:
        jobs = {
            "1001": {"partition": "a100-gpu", "state": "PENDING"},
            "1002": {"partition": "htzhulab", "state": "PENDING"},
        }
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), jobs)
            _, first = fixture.pre("scancel 1001 1002")
            question = protected_question(first)
            self.assertIn("1001 [a100-gpu], 1002 [htzhulab]", question["question"])
            answer = {"answers": {question["id"]: {"answers": ["确认取消"]}}}
            _, result = fixture.post(question, answer)
            self.assertEqual(result["protected_cancel"], "executed")
            self.assertEqual(fixture.mutation_argvs(), [["1001", "1002"]])

    def test_nonexact_options_unknown_executable_and_array_parent_fail_closed(self) -> None:
        bad_commands = (
            "scancel --signal=KILL 1",
            "scancel 123_[1-4]",
            "scancel 123.batch",
            "/tmp/scancel 123",
            "scancel",
        )
        for command in bad_commands:
            with self.subTest(command=command), tempfile.TemporaryDirectory() as temp:
                fixture = HostHookFixture(Path(temp), {"123": {"partition": "a100-gpu", "state": "PENDING"}})
                _, result = fixture.pre(command)
                self.assertEqual(result["hookSpecificOutput"]["permissionDecision"], "deny")
                self.assertEqual(fixture.mutation_argvs(), [])
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(
                Path(temp), {"123": {"partition": "htzhulab", "state": "PENDING", "array_job_id": "123"}}
            )
            _, result = fixture.pre("scancel 123")
            self.assertIn("target_resolution_failed", result["hookSpecificOutput"]["permissionDecisionReason"])
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_exact_array_element_is_supported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(
                Path(temp), {"123_4": {"partition": "htzhulab", "state": "PENDING", "array_job_id": "123"}}
            )
            _, result = fixture.pre("scancel 123_4")
            self.assertEqual(result["hookSpecificOutput"]["permissionDecision"], "deny")
            self.assertEqual(protected_question(result)["question"], "Job 123_4 当前位于受保护分区 htzhulab。确认取消这个 Job 吗？")
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_malformed_hook_input_never_mutates(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            fixture = HostHookFixture(Path(temp), {"1": {"partition": "a100-gpu", "state": "PENDING"}})
            completed = subprocess.run(
                [sys.executable, str(fixture.hook)],
                input="not-json",
                cwd=fixture.project,
                text=True,
                capture_output=True,
                check=False,
            )
            payload = json.loads(completed.stdout)
            self.assertEqual(payload["hookSpecificOutput"]["permissionDecision"], "deny")
            self.assertEqual(fixture.mutation_argvs(), [])


class TestSetupContract(unittest.TestCase):
    def test_render_has_only_pre_and_post_hooks_and_independent_denies(self) -> None:
        setup = load_module("setup_protected_cancel_v3", SCRIPTS / "setup_protected_cancel.py")
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            project = root / "project"
            project.mkdir()
            host = root / "host"
            scontrol = executable(host / "scontrol", "#!/bin/sh\nexit 0\n")
            scancel_real = executable(host / "scancel-real", "#!/bin/sh\nexit 0\n")
            scancel_link = host / "scancel"
            scancel_link.symlink_to(scancel_real.name)
            rendered = setup.render_contract(
                project,
                SCRIPTS,
                scontrol,
                scancel_link,
                "longleaf",
                root / "local-overrides.toml",
                ["htzhulab"],
            )
            files = rendered["files"]
            self.assertNotIn(".codex/automation-bin/scancel", files)
            self.assertNotIn(".codex/hooks/slurm-protected-cancel-session", files)
            self.assertNotIn(".codex/slurm-protected-cancel-private/capability.key", files)
            self.assertNotIn(".codex/slurm-protected-cancel-private/bin/slurm-protected-cancel-binder", files)
            hooks = json.loads(files[".codex/hooks.json"])
            self.assertEqual(set(hooks["hooks"]), {"PreToolUse", "PostToolUse"})
            self.assertEqual(hooks["hooks"]["PreToolUse"][0]["matcher"], "^(Bash|shell_command|exec_command)$")
            config = tomllib.loads(files[".codex/config.toml"].decode())
            filesystem = config["permissions"]["slurm-chat-guard"]["filesystem"]
            self.assertEqual(filesystem[":workspace_roots"][".codex"], "deny")
            self.assertEqual(filesystem[str(scancel_link.absolute())], "deny")
            self.assertEqual(filesystem[str(scancel_real.resolve())], "deny")
            self.assertNotIn(".codex/automation-bin", filesystem[":workspace_roots"])
            rules = files[".codex/rules/slurm-protected-cancel.rules"].decode()
            self.assertIn('pattern=["scancel"]', rules)
            self.assertIn(json.dumps(str(scancel_link.absolute())), rules)
            self.assertIn(json.dumps(str(scancel_real.resolve())), rules)

    def test_install_removes_obsolete_wrapper_capability_and_session_files(self) -> None:
        setup = load_module("setup_protected_cancel_install", SCRIPTS / "setup_protected_cancel.py")
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            project = root / "project"
            project.mkdir()
            for relative in setup.OBSOLETE_RELS:
                path = project / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("obsolete", encoding="utf-8")
            scontrol = executable(root / "host/scontrol", "#!/bin/sh\nexit 0\n")
            scancel = executable(root / "host/scancel", "#!/bin/sh\nexit 0\n")
            rendered = setup.render_contract(
                project, SCRIPTS, scontrol, scancel, "longleaf", root / "local.toml", ["htzhulab"]
            )
            setup.write_rendered(rendered, project, install=True)
            for relative in setup.OBSOLETE_RELS:
                self.assertFalse((project / relative).exists(), relative)
            self.assertTrue((project / setup.HOOK_REL).is_file())

    def test_filesystem_deny_blocks_absolute_and_python_child_when_hook_is_missing_or_broken(self) -> None:
        codex = shutil.which("codex")
        self.assertIsNotNone(codex)
        setup = load_module("setup_protected_cancel_sandbox", SCRIPTS / "setup_protected_cancel.py")
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            project = root / "project"
            project.mkdir()
            scontrol = executable(root / "fake-host/scontrol", "#!/bin/sh\nexit 1\n")
            marker = root / "fallback-called"
            scancel = executable(root / "fake-host/scancel", f"#!/bin/sh\nprintf called > {marker}\n")
            rendered = setup.render_contract(
                project, SCRIPTS, scontrol, scancel, "fixture", root / "local.toml", ["htzhulab"]
            )
            setup.write_rendered(rendered, project, install=True)
            profile = (
                'permissions.slurm-chat-guard={extends=":workspace",filesystem={'
                + json.dumps(str(scancel))
                + '="deny",":workspace_roots"={".codex"="deny"}}}'
            )

            def sandbox(*command: str) -> subprocess.CompletedProcess[str]:
                return subprocess.run(
                    [
                        str(codex),
                        "-c",
                        'default_permissions="slurm-chat-guard"',
                        "-c",
                        profile,
                        "sandbox",
                        "-P",
                        "slurm-chat-guard",
                        "-C",
                        str(project),
                        *command,
                    ],
                    text=True,
                    capture_output=True,
                    check=False,
                    timeout=30,
                )

            direct = sandbox(str(scancel), "9101")
            self.assertNotEqual(direct.returncode, 0)
            self.assertFalse(marker.exists())

            probe = project / "python-child-probe.py"
            probe.write_text(
                "import subprocess, sys\n"
                "try:\n"
                f"    result = subprocess.run([{str(scancel)!r}, '9101'], check=False)\n"
                "except PermissionError:\n"
                "    raise SystemExit(0)\n"
                "raise SystemExit(0 if result.returncode != 0 else 1)\n",
                encoding="utf-8",
            )
            child = sandbox("/usr/bin/python3", str(probe))
            self.assertEqual(child.returncode, 0, child.stderr)
            self.assertFalse(marker.exists())

            hook_path = project / setup.HOOK_REL
            hook_path.write_text("malformed hook", encoding="utf-8")
            hook_path.chmod(0o700)
            broken = sandbox(str(scancel), "9101")
            self.assertNotEqual(broken.returncode, 0)
            self.assertFalse(marker.exists())
            hook_path.unlink()
            missing = sandbox(str(scancel), "9101")
            self.assertNotEqual(missing.returncode, 0)
            self.assertFalse(marker.exists())


if __name__ == "__main__":
    unittest.main()
