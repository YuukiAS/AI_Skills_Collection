from __future__ import annotations

import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import pwd
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "skills/tools/hpc/slurm-workflows/scripts"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SETUP = load_module("setup_protected_cancel", SCRIPTS / "setup_protected_cancel.py")
HOOK = load_module("slurm_cancel_hook", SCRIPTS / "slurm_cancel_hook.py")


def executable(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    path.chmod(0o700)
    return path


class PortableFixture:
    def __init__(self, root: Path, jobs=None, python_path=None, scripts=SCRIPTS) -> None:
        self.root = root
        self.project = root / "project"
        self.project.mkdir()
        self.codex_home = root / "codex-home"
        self.codex_home.mkdir(mode=0o700)
        self.original_config = (
            '[features]\ndefault_mode_request_user_input = true\nhooks = true\n\n'
            '[permissions.keep-me]\nextends = ":workspace"\n\n'
            '[hooks.state]\n\n[hooks.state."unrelated:stop:0:0"]\n'
            'trusted_hash = "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"\n'
        )
        (self.codex_home / "config.toml").write_text(self.original_config, encoding="utf-8")
        self.state = root / "scheduler-state.json"
        self.set_jobs(jobs or {})
        self.mutations = root / "mutations.jsonl"
        user = pwd.getpwuid(os.geteuid()).pw_name
        self.scontrol = executable(
            root / "fake-host/scontrol",
            "#!/usr/bin/python3\nimport json,sys\n"
            "state=json.load(open({!r},encoding='utf-8'))\n".format(str(self.state))
            + "job=sys.argv[-1]; record=state.get(job)\n"
            + "if record is None: raise SystemExit(1)\n"
            + "user={!r}\n".format(user)
            + "print(' '.join([f'JobId={job}',f\"JobState={record['state']}\",f\"Partition={record['partition']}\",f\"UserId={record.get('user',user)}(1000)\",f\"ArrayJobId={record.get('array_job_id','(null)')}\",f\"HetJobId={record.get('het_job_id','(null)')}\"]))\n",
        )
        self.scancel = executable(
            root / "fake-host/scancel",
            "#!/usr/bin/python3\nimport json,sys\n"
            "with open({!r},'a',encoding='utf-8') as stream: stream.write(json.dumps(sys.argv[1:])+'\\n')\n".format(str(self.mutations)),
        )
        self.rendered = SETUP.render_global_contract(
            self.codex_home, scripts, self.scontrol, self.scancel, ["protected-lab"], hook_python=python_path
        )
        SETUP.write_rendered(self.rendered, self.codex_home, install=True)
        self.private = self.codex_home / SETUP.PRIVATE_DIR
        self.hook = self.private / SETUP.HOOK_NAME
        self.supervisor = self.private / SETUP.SUPERVISOR_NAME

    def set_jobs(self, jobs) -> None:
        self.state.write_text(json.dumps(jobs) + "\n", encoding="utf-8")

    def mutation_argvs(self):
        if not self.mutations.exists():
            return []
        return [json.loads(line) for line in self.mutations.read_text(encoding="utf-8").splitlines()]

    def shell_event(self, event_name: str, command: str):
        return {
            "hook_event_name": event_name, "tool_name": "Bash",
            "tool_input": {"command": command}, "cwd": str(self.project),
            "session_id": "session-1", "turn_id": "turn-1", "tool_use_id": "tool-{}".format(event_name),
        }

    def invoke_supervisor(self, event_name: str, event):
        completed = subprocess.run(
            [str(self.supervisor), event_name], input=json.dumps(event), text=True,
            capture_output=True, check=False, timeout=12,
        )
        payload = json.loads(completed.stdout) if completed.stdout.strip() else None
        return completed, payload

    def pre(self, command: str):
        return self.invoke_supervisor("PreToolUse", self.shell_event("PreToolUse", command))

    def permission(self, command: str):
        return self.invoke_supervisor("PermissionRequest", self.shell_event("PermissionRequest", command))

    def post(self, question, response, **extra):
        event = {
            "hook_event_name": "PostToolUse", "tool_name": "request_user_input",
            "tool_input": {"questions": [question]}, "tool_response": response,
            "cwd": str(self.project), "session_id": "session-1", "turn_id": "turn-2",
            "tool_use_id": "tool-answer-1",
        }
        event.update(extra)
        return self.invoke_supervisor("PostToolUse", event)


def denial_reason(payload, event_name="PreToolUse"):
    output = payload["hookSpecificOutput"]
    if event_name == "PreToolUse":
        return output["permissionDecisionReason"]
    return output["decision"]["message"]


def protected_question(payload, event_name="PreToolUse"):
    reason = denial_reason(payload, event_name)
    marker = reason.find("{")
    assert marker >= 0, reason
    return json.loads(reason[marker:])["request_user_input"]["questions"][0]


class TestStaleSessionScopeIsolation(unittest.TestCase):
    def test_private_guard_interpreter_failure_cannot_break_unrelated_bash(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            private_python = executable(root / 'fake-host/hook-python',
                '#!/bin/sh\nexec /usr/bin/python3 "$@"\n')
            fixture = PortableFixture(root, python_path=private_python)
            declaration = fixture.rendered['hooks']['PreToolUse'][0]['hooks'][0]['command']
            private_python.write_text('#!/bin/sh\nexit 127\n')
            for command in ('git status --short', 'ls', 'python --version', 'printf harmless', 'scancel 12345'):
                result = subprocess.run(declaration, shell=True,
                    input=json.dumps(fixture.shell_event('PreToolUse', command)),
                    capture_output=True, text=True, timeout=15)
                self.assertEqual(result.returncode, 0)
                payload = json.loads(result.stdout)
                if command.startswith('scancel'):
                    self.assertEqual(payload['hookSpecificOutput']['permissionDecision'], 'deny')
                else:
                    self.assertEqual(payload, {})
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_stale_declaration_isolates_unrelated_bash_before_mutable_checks(self):
        unrelated = ('git status --short', 'ls', 'python --version', 'printf harmless')
        protected = ('scancel 12345', '/usr/bin/scancel 12345', 'scancel --help',
                     'true && scancel 12345', 'python -c "scancel 12345"',
                     r's\cancel 12345', "s'cancel' 12345",
                     HOOK.PROBE_COMMAND)
        for damaged in ('slurm_cancel_supervisor.sh', 'slurm_cancel_hook.py', 'runtime.json', 'policy.json'):
            with self.subTest(damaged=damaged), tempfile.TemporaryDirectory() as temp:
                fixture = PortableFixture(Path(temp))
                # Capture the session-owned declaration, then change the
                # installed runtime beneath it without regenerating identity.
                declarations = {event: fixture.rendered['hooks'][event][0]['hooks'][0]['command']
                                for event in ('PreToolUse', 'PermissionRequest')}
                path = fixture.private / damaged
                path.write_text(path.read_text() + '\n# updated runtime identity\n')
                for event, declaration in declarations.items():
                    for command in unrelated + protected:
                        with self.subTest(event=event, command=command):
                            result = subprocess.run(declaration, shell=True,
                                input=json.dumps(fixture.shell_event(event, command)),
                                capture_output=True, text=True, timeout=15)
                            self.assertEqual(result.returncode, 0, result.stderr)
                            payload = json.loads(result.stdout)
                            if command in unrelated:
                                self.assertEqual(payload, {})
                                self.assertNotIn('SLURM_CANCEL_DENIED', result.stdout)
                            else:
                                output = payload['hookSpecificOutput']
                                decision = (output['permissionDecision'] if event == 'PreToolUse'
                                            else output['decision']['behavior'])
                                self.assertEqual(decision, 'deny')
                            self.assertEqual(fixture.mutation_argvs(), [])

    def test_non_bash_never_enters_stale_runtime(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            declaration = fixture.rendered['hooks']['PreToolUse'][0]['hooks'][0]['command']
            fixture.supervisor.unlink()
            event = fixture.shell_event('PreToolUse', 'scancel 12345')
            event['tool_name'] = 'Read'
            result = subprocess.run(declaration, shell=True, input=json.dumps(event),
                                    capture_output=True, text=True, timeout=15)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout), {})
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_prefilter_startup_failure_still_blocks_possible_cancellation(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            tools = {name: Path('/usr/bin') / name for name in ('bash','env','timeout')}
            _, runtime = HOOK._load_runtime(fixture.hook)
            declaration = SETUP._scope_prefilter_command('exit 0', 'PreToolUse',
                fixture.root / 'missing-python', runtime['environment'], tools)
            result = subprocess.run(declaration, shell=True,
                input=json.dumps(fixture.shell_event('PreToolUse', 'scancel 12345')),
                capture_output=True, text=True, timeout=15)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout)['hookSpecificOutput']['permissionDecision'], 'deny')
            self.assertEqual(fixture.mutation_argvs(), [])


class TestG1PortableAtomicInstallation(unittest.TestCase):
    def test_render_selects_qualified_python_and_three_global_hooks(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            manifest = fixture.rendered["manifest"]
            self.assertEqual(manifest["schema_version"], 5)
            self.assertEqual(set(fixture.rendered["hooks"]), {"PreToolUse", "PermissionRequest", "PostToolUse"})
            self.assertNotEqual(manifest["python_path"], "")
            self.assertIn("supervisor_sha256", manifest)
            runtime = json.loads((fixture.private / "runtime.json").read_text(encoding="utf-8"))
            self.assertEqual(runtime["schema_version"], 5)
            self.assertEqual(runtime["hook_file"], "slurm_cancel_hook.py")
            self.assertEqual(runtime["policy_file"], "policy.json")
            self.assertNotIn("codex_home", runtime)
            self.assertEqual(set(runtime["environment"]), {"HOME", "LANG", "LC_ALL", "LOGNAME", "PATH", "USER"})

    def test_config_preserves_unrelated_state_and_binds_supervisor_hash(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            config = (fixture.codex_home / "config.toml").read_text(encoding="utf-8")
            self.assertIn("[permissions.keep-me]", config)
            self.assertIn('[hooks.state."unrelated:stop:0:0"]', config)
            self.assertIn("sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", config)
            self.assertIn(SETUP.DECLARATION_START, config)
            self.assertIn(fixture.rendered["manifest"]["supervisor_sha256"], config)
            self.assertIn("default_mode_request_user_input = true", config)
            self.assertFalse((fixture.codex_home / "rules/slurm-protected-cancel.rules").exists())
            without_declaration = SETUP._strip_block(config, SETUP.DECLARATION_START, SETUP.DECLARATION_END)
            self.assertEqual(without_declaration, fixture.original_config)

    def test_cli_reports_fresh_session_boundary_without_runtime_identity_change(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            destination = fixture.root / "rendered"
            completed = subprocess.run(
                [sys.executable, str(SCRIPTS / "setup_protected_cancel.py"),
                 "--codex-home", str(fixture.codex_home),
                 "--scontrol", str(fixture.scontrol), "--scancel", str(fixture.scancel),
                 "--protected-partition", "protected-lab", "--render-output", str(destination)],
                capture_output=True, text=True, check=True,
            )
            manifest = json.loads(completed.stdout)
            self.assertIs(manifest["fresh_session_required"], True)
            self.assertIn("fresh Codex/Desktop thread", manifest["next_action"])
            self.assertIn("hooks/list alone does not prove", manifest["next_action"])
            self.assertEqual(manifest["file_sha256"], fixture.rendered["manifest"]["file_sha256"])
            exported = json.loads((destination / "protected-cancel-render-manifest.json").read_text())
            self.assertEqual(exported, manifest)

    def test_upgrade_preserves_replay_state_and_recoverable_backup(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            marker = fixture.private / "consumed/already-used.json"
            marker.write_text('{"status":"completed"}\n', encoding="utf-8"); marker.chmod(0o600)
            original_config = (fixture.codex_home / "config.toml").read_bytes()
            rendered = SETUP.render_global_contract(
                fixture.codex_home, SCRIPTS, fixture.scontrol, fixture.scancel, ["protected-lab"]
            )
            SETUP.write_rendered(rendered, fixture.codex_home, install=True)
            self.assertEqual((fixture.private / "consumed/already-used.json").read_bytes(), marker.read_bytes())
            backups = list((fixture.private / "backups").glob("pre-v3-*"))
            self.assertEqual(len(backups), 1)
            self.assertEqual((backups[0] / "config.toml").read_bytes(), original_config)
            self.assertTrue((backups[0] / "private/runtime.json").is_file())

    def test_explicit_python_must_qualify_in_sanitized_environment(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            broken = executable(root / "broken-python", "#!/bin/sh\nexit 127\n")
            codex_home = root / "codex"; codex_home.mkdir()
            host = executable(root / "host/tool", "#!/bin/sh\nexit 0\n")
            with self.assertRaisesRegex(ValueError, "no qualified Python"):
                SETUP.render_global_contract(codex_home, SCRIPTS, host, host, ["protected-lab"], hook_python=broken)

    def test_invalid_staged_candidate_never_activates(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            scripts = root / "scripts"; shutil.copytree(SCRIPTS, scripts)
            (scripts / "slurm_cancel_hook.py").write_text("print('not-json')\n", encoding="utf-8")
            codex_home = root / "codex"; codex_home.mkdir(mode=0o700)
            original = b"[features]\ndefault_mode_request_user_input = true\nhooks = true\n"
            (codex_home / "config.toml").write_bytes(original)
            host = executable(root / "host/tool", "#!/bin/sh\nexit 0\n")
            rendered = SETUP.render_global_contract(codex_home, scripts, host, host, ["protected-lab"])
            with self.assertRaisesRegex(ValueError, "qualification failed"):
                SETUP.write_rendered(rendered, codex_home, install=True)
            self.assertEqual((codex_home / "config.toml").read_bytes(), original)
            self.assertFalse((codex_home / SETUP.PRIVATE_DIR).exists())


class TestG2FailClosedSupervisor(unittest.TestCase):
    def test_healthy_unrelated_bash_is_empty_decision(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            completed, payload = fixture.pre("printf harmless")
            self.assertEqual((completed.returncode, payload), (0, {}))

    def test_hook_hash_mismatch_returns_valid_pre_deny(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            fixture.hook.write_text("print('{}')\n", encoding="utf-8"); fixture.hook.chmod(0o600)
            completed, payload = fixture.pre("printf harmless")
            self.assertEqual(completed.returncode, 0)
            self.assertEqual(payload["hookSpecificOutput"]["permissionDecision"], "deny")
            self.assertIn("hook_runtime_failure", denial_reason(payload))

    def test_runtime_and_policy_corruption_return_event_specific_denies(self):
        for name, event in (("runtime.json", "PreToolUse"), ("policy.json", "PermissionRequest")):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temp:
                fixture = PortableFixture(Path(temp))
                (fixture.private / name).write_text("{}\n", encoding="utf-8")
                invoke = fixture.pre if event == "PreToolUse" else fixture.permission
                completed, payload = invoke("printf harmless")
                self.assertEqual(completed.returncode, 0)
                self.assertIn("hook_runtime_failure", denial_reason(payload, event))

    def test_missing_or_nonzero_interpreter_returns_valid_deny(self):
        for body in ("#!/bin/sh\nexit 127\n", "#!/bin/sh\nexit 42\n", "#!/bin/sh\nkill -TERM $$\n"):
            with self.subTest(body=body), tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                wrapper = executable(root / "python-wrapper", "#!/bin/sh\nexec /usr/bin/python3 \"$@\"\n")
                fixture = PortableFixture(root, python_path=wrapper)
                wrapper.write_text(body, encoding="utf-8"); wrapper.chmod(0o700)
                completed, payload = fixture.pre("printf harmless")
                self.assertEqual(completed.returncode, 0)
                self.assertEqual(payload["hookSpecificOutput"]["permissionDecision"], "deny")

    def test_interpreter_disappears_after_activation(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            wrapper = executable(root / "python-wrapper", "#!/bin/sh\nexec /usr/bin/python3 \"$@\"\n")
            fixture = PortableFixture(root, python_path=wrapper)
            wrapper.unlink()
            completed, payload = fixture.pre("printf harmless")
            self.assertEqual(completed.returncode, 0)
            self.assertEqual(payload["hookSpecificOutput"]["permissionDecision"], "deny")

    def test_internal_timeout_returns_valid_deny_before_host_timeout(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            wrapper = executable(root / "python-wrapper", "#!/bin/sh\nexec /usr/bin/python3 \"$@\"\n")
            fixture = PortableFixture(root, python_path=wrapper)
            wrapper.write_text("#!/bin/sh\nsleep 20\n", encoding="utf-8"); wrapper.chmod(0o700)
            text = fixture.supervisor.read_text(encoding="utf-8").replace(
                ' --kill-after=1 8 "$ENV"', ' --kill-after=1 0.2 "$ENV"', 1
            )
            fixture.supervisor.write_text(text, encoding="utf-8"); fixture.supervisor.chmod(0o700)
            completed, payload = fixture.pre("printf harmless")
            self.assertEqual(completed.returncode, 0)
            self.assertEqual(payload["hookSpecificOutput"]["permissionDecision"], "deny")

    def test_malformed_hook_output_returns_valid_deny(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            old_hook = hashlib.sha256(fixture.hook.read_bytes()).hexdigest()
            fixture.hook.write_text("print('not-json')\n", encoding="utf-8"); fixture.hook.chmod(0o600)
            new_hook = hashlib.sha256(fixture.hook.read_bytes()).hexdigest()
            runtime_path = fixture.private / "runtime.json"
            runtime = json.loads(runtime_path.read_text(encoding="utf-8")); runtime["hook_sha256"] = new_hook
            old_runtime = hashlib.sha256(runtime_path.read_bytes()).hexdigest()
            runtime_path.write_text(json.dumps(runtime, indent=2, sort_keys=True) + "\n", encoding="utf-8"); runtime_path.chmod(0o600)
            new_runtime = hashlib.sha256(runtime_path.read_bytes()).hexdigest()
            supervisor = fixture.supervisor.read_text(encoding="utf-8").replace(old_hook, new_hook).replace(old_runtime, new_runtime)
            fixture.supervisor.write_text(supervisor, encoding="utf-8"); fixture.supervisor.chmod(0o700)
            completed, payload = fixture.pre("printf harmless")
            self.assertEqual(completed.returncode, 0)
            self.assertEqual(payload["hookSpecificOutput"]["permissionDecision"], "deny")

    def test_outer_declaration_catches_missing_or_corrupt_supervisor(self):
        for mutation in ("missing", "corrupt"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temp:
                fixture = PortableFixture(Path(temp))
                command = fixture.rendered["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
                if mutation == "missing": fixture.supervisor.unlink()
                else: fixture.supervisor.write_text("#!/bin/sh\nprintf bad\n", encoding="utf-8"); fixture.supervisor.chmod(0o700)
                completed = subprocess.run(command, shell=True, input=json.dumps(fixture.shell_event("PreToolUse", "scancel 12345")), text=True, capture_output=True, check=False)
                payload = json.loads(completed.stdout)
                self.assertEqual(completed.returncode, 0)
                self.assertEqual(payload["hookSpecificOutput"]["permissionDecision"], "deny")


class TestG3ProtectedCancelSemantics(unittest.TestCase):
    def test_unprotected_exact_target_is_not_intercepted(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp), {"9101": {"partition": "general", "state": "PENDING"}})
            for invoke in (fixture.pre, fixture.permission):
                completed, payload = invoke("scancel 9101")
                self.assertEqual((completed.returncode, payload), (0, {}))
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_protected_target_denies_with_exact_native_question(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp), {"9101": {"partition": "protected-lab", "state": "PENDING"}})
            for event, invoke in (("PreToolUse", fixture.pre), ("PermissionRequest", fixture.permission)):
                completed, payload = invoke("scancel 9101")
                self.assertEqual(completed.returncode, 0)
                question = protected_question(payload, event)
                self.assertEqual(question["id"], "slurm-protected-cancel:9101")
                self.assertEqual([item["label"] for item in question["options"]], ["确认取消", "保留 Job"])
                self.assertEqual(set(question), {"id", "header", "question", "options"})
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_canonical_and_platform_normalized_question_shapes(self):
        targets = [{"job_id": "5001", "partition": "protected-lab"}]
        question = HOOK._question_for_targets(targets)
        self.assertEqual(set(question), {"id", "header", "question", "options"})
        self.assertEqual(HOOK._targets_from_question(question), targets)
        normalized = {**question, "isOther": True, "isSecret": False}
        self.assertEqual(HOOK._targets_from_question(normalized), targets)
        self.assertEqual(normalized["isOther"], True)  # Parsing must not mutate input.
        invalid = [
            {**normalized, "isOther": False},
            {**normalized, "isSecret": True},
            {**normalized, "isOther": 1},
            {**normalized, "isSecret": 0},
            {**normalized, "unexpected": "field"},
            {**question, "unexpected": "field"},
            {**question, "isOther": True},
            {**question, "question": "different question"},
            {**question, "id": "different-id"},
            {**question, "options": list(reversed(question["options"]))},
        ]
        for changed in invalid:
            with self.subTest(question=changed):
                self.assertIsNone(HOOK._targets_from_question(changed))

    def test_retain_is_explicit_without_cancellation_reservation(self):
        for normalized in (False, True):
            with self.subTest(normalized=normalized), tempfile.TemporaryDirectory() as temp:
                fixture = PortableFixture(Path(temp), {"5001": {"partition": "protected-lab", "state": "PENDING"}})
                _, first = fixture.pre("scancel 5001")
                question = protected_question(first)
                if normalized:
                    question.update(isOther=True, isSecret=False)
                _, retained = fixture.post(question, {"answers": {question["id"]: {"answers": ["保留 Job"]}}})
                self.assertEqual(retained, {"protected_cancel": "retained", "reason": "user_retained", "mutation_count": 0})
                self.assertEqual(fixture.mutation_argvs(), [])
                self.assertEqual(list((fixture.private / "consumed").glob("*.json")), [])

    def test_other_free_text_empty_or_malformed_answers_never_reserve(self):
        answers = (["Other"], ["任意自由输入"], ["确认取消", "Other"], [], None, "确认取消")
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp), {"5001": {"partition": "protected-lab", "state": "PENDING"}})
            _, first = fixture.pre("scancel 5001")
            question = {**protected_question(first), "isOther": True, "isSecret": False}
            for answer in answers:
                with self.subTest(answer=answer):
                    _, denied = fixture.post(question, {"answers": {question["id"]: {"answers": answer}}})
                    self.assertEqual(denied["protected_cancel"], "denied")
                    self.assertEqual(denied["mutation_count"], 0)
                    self.assertEqual(fixture.mutation_argvs(), [])
                    self.assertEqual(list((fixture.private / "consumed").glob("*.json")), [])

    def test_normalized_confirmation_executes_once_and_replay_is_denied(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp), {"5001": {"partition": "protected-lab", "state": "PENDING"}})
            _, first = fixture.pre("scancel 5001")
            question = {**protected_question(first), "isOther": True, "isSecret": False}
            answer = {"answers": {question["id"]: {"answers": ["确认取消"]}}}
            _, confirmed = fixture.post(question, answer)
            self.assertEqual(confirmed["protected_cancel"], "executed")
            _, replay = fixture.post(question, answer)
            self.assertEqual(replay["reason"], "replayed_or_duplicate_confirmation")
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])

    def test_reservation_precedes_final_resolution_and_one_exact_cancel(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp), {"5001": {"partition": "protected-lab", "state": "PENDING"}})
            _, first = fixture.pre("scancel 5001")
            question = protected_question(first)
            private, runtime = HOOK._load_runtime(fixture.hook)
            observed = []
            original_resolve, original_run = HOOK._resolve_targets, subprocess.run

            def resolve(runtime, job_ids):
                reservations = list((private / "consumed").glob("*.json"))
                observed.append(("resolve", bool(reservations)))
                return original_resolve(runtime, job_ids)

            def run(argv, **kwargs):
                if argv[0] == str(fixture.scancel):
                    reservations = list((private / "consumed").glob("*.json"))
                    self.assertEqual(len(reservations), 1)
                    self.assertEqual(json.loads(reservations[0].read_text())["status"], "reserved")
                    self.assertEqual(observed[-1], ("resolve", True))
                    self.assertEqual(argv, [str(fixture.scancel), "5001"])
                    observed.append(("cancel", True))
                return original_run(argv, **kwargs)

            event = {
                "tool_name": "request_user_input", "cwd": str(fixture.project),
                "session_id": "session-1", "turn_id": "turn-2", "tool_use_id": "tool-answer-1",
                "tool_input": {"questions": [question]},
                "tool_response": {"answers": {question["id"]: {"answers": ["确认取消"]}}},
            }
            with patch.object(HOOK, "_resolve_targets", side_effect=resolve), \
                    patch.object(HOOK.subprocess, "run", side_effect=run), redirect_stdout(io.StringIO()) as output:
                HOOK._post_tool_use(event, private, runtime)
            self.assertEqual(json.loads(output.getvalue())["protected_cancel"], "executed")
            self.assertEqual(observed, [("resolve", False), ("resolve", True), ("cancel", True)])
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])

    def test_target_drift_after_reservation_consumes_without_cancel(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp), {"5001": {"partition": "protected-lab", "state": "PENDING"}})
            _, first = fixture.pre("scancel 5001")
            question = protected_question(first)
            private, runtime = HOOK._load_runtime(fixture.hook)
            current = [{"job_id": "5001", "partition": "protected-lab", "state": "PENDING"}]
            event = {
                "tool_name": "request_user_input", "cwd": str(fixture.project),
                "session_id": "session-1", "turn_id": "turn-2", "tool_use_id": "tool-answer-1",
                "tool_input": {"questions": [question]},
                "tool_response": {"answers": {question["id"]: {"answers": ["确认取消"]}}},
            }
            with patch.object(HOOK, "_resolve_targets", side_effect=[current, None]), redirect_stdout(io.StringIO()) as output:
                HOOK._post_tool_use(event, private, runtime)
            self.assertEqual(json.loads(output.getvalue())["reason"], "target_changed_after_reservation")
            self.assertEqual(fixture.mutation_argvs(), [])
            reservation = next((private / "consumed").glob("*.json"))
            self.assertEqual(json.loads(reservation.read_text())["status"], "pre_invocation_failed")
            _, replay = fixture.post(question, event["tool_response"])
            self.assertEqual(replay["reason"], "replayed_or_duplicate_confirmation")

    def test_retain_and_non_confirmation_never_mutate(self):
        responses = [
            {"answers": {}},
            {"answers": {"slurm-protected-cancel:5001": {"answers": ["保留 Job"]}}},
            {"answers": {"slurm-protected-cancel:5001": {"answers": ["Other"]}}},
        ]
        for response in responses:
            with self.subTest(response=response), tempfile.TemporaryDirectory() as temp:
                fixture = PortableFixture(Path(temp), {"5001": {"partition": "protected-lab", "state": "PENDING"}})
                _, first = fixture.pre("scancel 5001")
                fixture.post(protected_question(first), response)
                self.assertEqual(fixture.mutation_argvs(), [])

    def test_fresh_confirmation_mutates_once_and_replay_is_zero(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp), {"5001": {"partition": "protected-lab", "state": "PENDING"}})
            _, first = fixture.pre("scancel 5001")
            question = protected_question(first)
            answer = {"answers": {question["id"]: {"answers": ["确认取消"]}}}
            _, confirmed = fixture.post(question, answer)
            self.assertEqual(confirmed["protected_cancel"], "executed")
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])
            _, replay = fixture.post(question, answer)
            self.assertEqual(replay["reason"], "replayed_or_duplicate_confirmation")
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])
            reservation = next((fixture.private / "consumed").glob("*.json"))
            self.assertEqual(json.loads(reservation.read_text())["status"], "completed")

    def test_target_partition_owner_or_state_change_fails_closed(self):
        changed = [
            {}, {"5001": {"partition": "general", "state": "PENDING"}},
            {"5001": {"partition": "protected-lab", "state": "COMPLETED"}},
            {"5001": {"partition": "protected-lab", "state": "PENDING", "user": "someone-else"}},
        ]
        for jobs in changed:
            with self.subTest(jobs=jobs), tempfile.TemporaryDirectory() as temp:
                fixture = PortableFixture(Path(temp), {"5001": {"partition": "protected-lab", "state": "PENDING"}})
                _, first = fixture.pre("scancel 5001"); question = protected_question(first)
                fixture.set_jobs(jobs)
                fixture.post(question, {"answers": {question["id"]: {"answers": ["确认取消"]}}})
                self.assertEqual(fixture.mutation_argvs(), [])

    def test_multi_target_binds_exact_set(self):
        jobs = {"1001": {"partition": "general", "state": "PENDING"}, "1002": {"partition": "protected-lab", "state": "RUNNING"}}
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp), jobs)
            _, first = fixture.pre("scancel 1001 1002"); question = protected_question(first)
            fixture.post(question, {"answers": {question["id"]: {"answers": ["确认取消"]}}})
            self.assertEqual(fixture.mutation_argvs(), [["1001", "1002"]])

    def test_unsupported_options_selectors_executables_and_compounds_deny(self):
        commands = (
            "scancel --help", "scancel --signal=KILL 1", "scancel 123_[1-4]", "scancel 123.batch",
            "/tmp/scancel 123", "scancel", "printf x; scancel 123", "true && scancel 123",
        )
        for command in commands:
            with self.subTest(command=command), tempfile.TemporaryDirectory() as temp:
                fixture = PortableFixture(Path(temp), {"123": {"partition": "general", "state": "PENDING"}})
                _, payload = fixture.pre(command)
                self.assertEqual(payload["hookSpecificOutput"]["permissionDecision"], "deny")
                self.assertEqual(fixture.mutation_argvs(), [])

    def test_same_global_runtime_works_from_four_unrelated_cwds(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp); fixture = PortableFixture(root, {"9101": {"partition": "protected-lab", "state": "PENDING"}})
            for index in range(4):
                cwd = root / "repo-{}".format(index); cwd.mkdir()
                event = fixture.shell_event("PreToolUse", "scancel 9101"); event["cwd"] = str(cwd)
                event["tool_use_id"] += "-cwd-" + str(index)
                _, payload = fixture.invoke_supervisor("PreToolUse", event)
                self.assertIn("NEEDS_INTERACTIVE_CHAT_CONFIRMATION", denial_reason(payload))

    def test_headless_confirmation_never_mutates(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp), {"5001": {"partition": "protected-lab", "state": "PENDING"}})
            _, first = fixture.pre("scancel 5001"); question = protected_question(first)
            answer = {"answers": {question["id"]: {"answers": ["确认取消"]}}}
            _, result = fixture.post(question, answer, agent_id="subagent-1")
            self.assertEqual(result["reason"], "not_root_interactive_session")
            self.assertEqual(fixture.mutation_argvs(), [])

    def test_no_wrapper_path_interception_or_routing_change(self):
        combined = (SCRIPTS / "setup_protected_cancel.py").read_text() + (SCRIPTS / "slurm_cancel_hook.py").read_text()
        for forbidden in ("automation-bin", "PATH prepend", "ai-slurm-scancel", 'default_permissions = "slurm-'):
            self.assertNotIn(forbidden, combined)
        rules = SETUP._rules_text([Path("/fake/scancel")])
        self.assertIn('decision="prompt"', rules)


if __name__ == "__main__":
    unittest.main()
