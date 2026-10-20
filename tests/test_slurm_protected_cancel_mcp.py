from __future__ import annotations

import asyncio
import json
import hashlib
import io
import time
from contextlib import redirect_stdout
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

from test_slurm_protected_cancel import HOOK, SETUP, SCRIPTS, PortableFixture, load_module

MCP = load_module("slurm_protected_cancel_mcp", SCRIPTS / "slurm_protected_cancel_mcp.py")
# Tests explicitly pin the known source fixture; production only loads a guard
# after receiving the trusted Hook's expected identity.
with patch.object(MCP, "private_file_ok", return_value=True):
    MCP.load_guard(hashlib.sha256((SCRIPTS / "slurm_cancel_hook.py").read_bytes()).hexdigest())


def result_data(result):
    return json.loads(result["hookSpecificOutput"]["permissionDecisionReason"])


class TestMcpProtectedCancel(unittest.IsolatedAsyncioTestCase):
    def prepare(self, fixture, event):
        _, runtime = HOOK._load_runtime(fixture.hook)
        with redirect_stdout(io.StringIO()):
            HOOK._pre_tool_use(event, runtime, fixture.private)

    async def invoke(self, fixture, response, command="scancel 5001", **extra):
        private, runtime = MCP.guard._load_runtime(fixture.hook)
        event = fixture.shell_event("PreToolUse", command)
        event.update(extra)
        self.prepare(fixture, event)
        async def elicit(message, schema):
            self.assertEqual(schema, MCP.DECISION_SCHEMA)
            if isinstance(response, Exception):
                raise response
            return response
        return await MCP.handle(event, {"threadId": "session-1"}, private, runtime, elicit)

    def fixture(self, root, partition="protected-lab"):
        return PortableFixture(root, {"5001": {"partition": partition, "state": "PENDING"}})

    async def test_retain_has_no_reservation_and_audits_no_mutation(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self.fixture(Path(temp))
            result = await self.invoke(fixture, {"action": "accept", "content": {"decision": "retain"}})
            self.assertEqual(result_data(result)["protected_cancel"], "retained")
            self.assertEqual(fixture.mutation_argvs(), [])
            self.assertEqual(list((fixture.private / "consumed").glob("*.json")), [])
            records = [json.loads(path.read_text()) for path in (fixture.private / "audit").glob("*.json")]
            self.assertTrue(any(item["phase"] == "retained" and item["mutation_count"] == 0 for item in records))

    async def test_close_timeout_empty_other_and_malformed_never_mutate(self):
        cases = [None, {}, {"action": "cancel"}, {"action": "decline"},
                 {"action": "accept", "content": {}},
                 {"action": "accept", "content": {"decision": "Other"}},
                 {"action": "accept", "content": {"decision": "confirm", "extra": 1}},
                 asyncio.TimeoutError(), RuntimeError("disconnected")]
        for response in cases:
            with self.subTest(response=response), tempfile.TemporaryDirectory() as temp:
                fixture = self.fixture(Path(temp))
                result = await self.invoke(fixture, response)
                self.assertEqual(result_data(result)["mutation_count"], 0)
                self.assertEqual(fixture.mutation_argvs(), [])
                self.assertEqual(list((fixture.private / "consumed").glob("*.json")), [])

    async def test_single_select_has_only_two_labels_and_no_other_or_free_text(self):
        schema = MCP.DECISION_SCHEMA
        self.assertEqual(schema["required"], ["decision"])
        field = schema["properties"]["decision"]
        self.assertEqual(field["type"], "string")
        self.assertEqual(field["oneOf"], [{"const": "confirm", "title": "确认取消"}, {"const": "retain", "title": "保留 Job"}])
        self.assertNotIn("default", field)
        with tempfile.TemporaryDirectory() as temp:
            fixture = self.fixture(Path(temp))
            result = await self.invoke(fixture, {"action": "accept", "content": {"decision": "confirm"}}, MCP.PROBE_COMMAND)
            self.assertEqual(result_data(result)["protected_cancel"], "probe_completed")
            self.assertEqual(fixture.mutation_argvs(), [])
            self.assertEqual(list((fixture.private / "consumed").glob("*.json")), [])

    async def test_confirm_reserves_before_last_resolve_and_invokes_once(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self.fixture(Path(temp))
            original_resolve = MCP.guard._resolve_targets
            observations = []
            def resolve(runtime, job_ids):
                observations.append(bool(list((fixture.private / "consumed").glob("*.json"))))
                return original_resolve(runtime, job_ids)
            with patch.object(MCP.guard, "_resolve_targets", side_effect=resolve):
                result = await self.invoke(fixture, {"action": "accept", "content": {"decision": "confirm"}})
            self.assertEqual(observations, [False, False, True, True])
            self.assertEqual(result_data(result)["mutation_count"], 1)
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])
            reservation = json.loads(next((fixture.private / "consumed").glob("*.json")).read_text())
            self.assertEqual(reservation["status"], "completed")
            records = {json.loads(p.read_text())["phase"]: json.loads(p.read_text()) for p in (fixture.private / "audit").glob("*.json")}
            self.assertLess(records["reserved"]["time_ns"], records["final_resolved"]["time_ns"])
            self.assertLess(records["final_resolved"]["time_ns"], records["invocation_intent"]["time_ns"])
            self.assertTrue(MCP.possible_invocation(fixture.private, fixture.shell_event("PreToolUse", "scancel 5001")))
            with self.assertRaisesRegex(ValueError, "consumed"):
                await self.invoke(fixture, {"action": "accept", "content": {"decision": "confirm"}})
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])

    async def test_each_target_partition_owner_state_drift_prevents_cancellation(self):
        for changed in ({}, {"5001": {"partition": "general", "state": "PENDING"}},
                        {"5001": {"partition": "protected-lab", "state": "RUNNING"}},
                        {"5001": {"partition": "protected-lab", "state": "PENDING", "user": "different-owner"}}):
            with self.subTest(changed=changed), tempfile.TemporaryDirectory() as temp:
                fixture = self.fixture(Path(temp))
                private, runtime = MCP.guard._load_runtime(fixture.hook)
                async def elicit(message, schema):
                    fixture.set_jobs(changed)
                    return {"action": "accept", "content": {"decision": "confirm"}}
                event = fixture.shell_event("PreToolUse", "scancel 5001")
                self.prepare(fixture, event)
                result = await MCP.handle(event, {"threadId": "session-1"}, private, runtime, elicit)
                self.assertEqual(result_data(result)["mutation_count"], 0)
                self.assertEqual(fixture.mutation_argvs(), [])

    async def test_post_reservation_drift_is_consumed_without_retry(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self.fixture(Path(temp))
            real = MCP.guard._resolve_targets
            def resolve(runtime, job_ids):
                if list((fixture.private / "consumed").glob("*.json")):
                    return None
                return real(runtime, job_ids)
            with patch.object(MCP.guard, "_resolve_targets", side_effect=resolve):
                result = await self.invoke(fixture, {"action": "accept", "content": {"decision": "confirm"}})
            self.assertEqual(result_data(result)["reason"], "target_changed_after_reservation")
            self.assertEqual(fixture.mutation_argvs(), [])
            self.assertEqual(json.loads(next((fixture.private / "consumed").glob("*.json")).read_text())["status"], "pre_invocation_failed")

    async def test_wrong_owning_chat_and_subagent_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self.fixture(Path(temp))
            private, runtime = MCP.guard._load_runtime(fixture.hook)
            async def forbidden(*args):
                self.fail("must not elicit")
            event = fixture.shell_event("PreToolUse", "scancel 5001")
            with self.assertRaisesRegex(ValueError, "owning_thread_mismatch"):
                await MCP.handle(event, {"threadId": "different"}, private, runtime, forbidden)
            with self.assertRaisesRegex(ValueError, "not_root_interactive"):
                await MCP.handle({**event, "agent_id": "child"}, {"threadId": "session-1"}, private, runtime, forbidden)

    async def test_unprotected_and_unrelated_do_not_elicit_or_gain_restrictions(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self.fixture(Path(temp), "general")
            private, runtime = MCP.guard._load_runtime(fixture.hook)
            async def forbidden(*args):
                self.fail("must not elicit")
            event = fixture.shell_event("PreToolUse", "scancel 5001")
            self.assertEqual(await MCP.handle(event, {"threadId": "session-1"}, private, runtime, forbidden), {})
            self.assertEqual(await MCP.handle({**event, "agent_id": "child"}, {}, private, runtime, forbidden), {})
            unrelated = {"tool_input": {"command": "printf harmless"}, "agent_id": "child"}
            self.assertEqual(await MCP.handle(unrelated, {}, private, runtime, forbidden), {})

    async def test_unsupported_selector_still_denied_without_elicitation(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self.fixture(Path(temp))
            for index, command in enumerate(("scancel --help", "scancel -u user", "scancel 5001; true")):
                result = await self.invoke(fixture, None, command, tool_use_id="unsupported-" + str(index))
                self.assertEqual(result["hookSpecificOutput"]["permissionDecision"], "deny")
                self.assertEqual(fixture.mutation_argvs(), [])

    async def test_root_missing_optional_fields_and_real_guard_pending(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self.fixture(Path(temp))
            event = fixture.shell_event("PreToolUse", "scancel 5001")
            self.assertNotIn("agent_id", event)
            self.assertNotIn("agent_type", event)
            completed, result = fixture.invoke_supervisor("PreToolUse", event)
            self.assertEqual(completed.returncode, 0)
            self.assertEqual(result["hookSpecificOutput"]["permissionDecision"], "deny")
            path = HOOK._pending_path(fixture.private, HOOK._pending_identity(event))
            record = json.loads(path.read_text())
            self.assertRegex(record["nonce"], r"^[0-9a-f]{64}$")
            self.assertEqual(record["state"], "pending")
            self.assertEqual(record["job_ids"], ["5001"])
            self.assertEqual(record["operation"], HOOK.OPERATION)
            self.assertLess(record["created_at"], record["expires_at"])
            _, runtime = MCP.guard._load_runtime(fixture.hook)
            requested = []
            async def elicit(message, schema):
                requested.append(schema)
                return {"action": "accept", "content": {"decision": "retain"}}
            result = await MCP.handle(event, {"threadId": "session-1"}, fixture.private, runtime, elicit)
            self.assertEqual(len(requested), 1)
            self.assertEqual(result_data(result)["protected_cancel"], "retained")
            self.assertEqual(json.loads(path.read_text())["state"], "retained")
            self.assertEqual(fixture.mutation_argvs(), [])
            self.assertEqual(list((fixture.private / "consumed").glob("*.json")), [])

    async def test_explicit_subagent_never_creates_pending(self):
        for field in ("agent_id", "agent_type"):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temp:
                fixture = self.fixture(Path(temp))
                event = {**fixture.shell_event("PreToolUse", "scancel 5001"), field: "child"}
                completed, result = fixture.invoke_supervisor("PreToolUse", event)
                self.assertEqual(completed.returncode, 0)
                self.assertEqual(result["hookSpecificOutput"]["permissionDecision"], "deny")
                self.assertEqual(list((fixture.private / "pending").glob("*.json")), [])
                self.assertEqual(fixture.mutation_argvs(), [])

    async def test_parallel_mcp_early_arrival_waits_for_exact_command_pending(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self.fixture(Path(temp))
            event = fixture.shell_event("PreToolUse", MCP.PROBE_COMMAND)
            _, runtime = MCP.guard._load_runtime(fixture.hook)
            requested = []
            async def elicit(message, schema):
                requested.append(True)
                return {"action": "accept", "content": {"decision": "confirm"}}
            async def command_hook():
                await asyncio.sleep(0.04)
                self.prepare(fixture, event)
            with patch.object(MCP.guard, "_resolve_targets", side_effect=AssertionError("probe must not query scheduler")):
                result, _ = await asyncio.gather(
                    MCP.handle(event, {"threadId": "session-1"}, fixture.private, runtime, elicit), command_hook())
            self.assertEqual(requested, [True])
            self.assertEqual(result_data(result)["protected_cancel"], "probe_completed")
            self.assertEqual(fixture.mutation_argvs(), [])
            self.assertEqual(list((fixture.private / "consumed").glob("*.json")), [])

    async def test_missing_mismatched_expired_or_replayed_pending_never_elicits(self):
        cases = ["missing", "session_id", "turn_id", "tool_use_id", "targets", "job_ids", "owner", "operation", "expired", "consumed", "nonce"]
        for change in cases:
            with self.subTest(change=change), tempfile.TemporaryDirectory() as temp:
                fixture = self.fixture(Path(temp))
                event = fixture.shell_event("PreToolUse", "scancel 5001")
                _, runtime = MCP.guard._load_runtime(fixture.hook)
                self.prepare(fixture, event)
                path = HOOK._pending_path(fixture.private, HOOK._pending_identity(event))
                record = json.loads(path.read_text())
                if change == "missing": path.unlink()
                else:
                    if change in ("session_id", "turn_id", "tool_use_id", "owner", "operation", "nonce"): record[change] = "wrong"
                    elif change == "targets": record[change][0]["job_id"] = "5002"
                    elif change == "job_ids": record[change] = ["5002"]
                    elif change == "expired": record.update(created_at=time.time()-20, expires_at=time.time()-1)
                    else: record["state"] = "consumed"
                    path.write_text(json.dumps(record))
                async def forbidden(*args): self.fail("must not elicit without exact live pending")
                with patch.object(MCP, "PENDING_WAIT_SECONDS", 0.06):
                    started = time.monotonic()
                    with self.assertRaises(ValueError):
                        await MCP.handle(event, {"threadId": "session-1"}, fixture.private, runtime, forbidden)
                    self.assertLess(time.monotonic()-started, 0.5)
                self.assertEqual(fixture.mutation_argvs(), [])
                self.assertEqual(list((fixture.private / "consumed").glob("*.json")), [])

    async def test_malformed_or_wrong_call_identity_never_consumes_pending(self):
        for key in ("session_id", "turn_id", "tool_use_id"):
            for value in (None, "", "bad/id", "different"):
                with self.subTest(key=key, value=value), tempfile.TemporaryDirectory() as temp:
                    fixture = self.fixture(Path(temp))
                    event = fixture.shell_event("PreToolUse", MCP.PROBE_COMMAND)
                    self.prepare(fixture, event)
                    _, runtime = MCP.guard._load_runtime(fixture.hook)
                    async def forbidden(*args): self.fail("must not elicit")
                    with patch.object(MCP, "PENDING_WAIT_SECONDS", 0.01):
                        with self.assertRaises(ValueError):
                            await MCP.handle({**event, key: value}, {"threadId": "session-1"}, fixture.private, runtime, forbidden)
                    self.assertEqual(fixture.mutation_argvs(), [])
                    self.assertEqual(list((fixture.private / "consumed").glob("*.json")), [])


class TestMcpInstaller(unittest.TestCase):
    def test_tampered_guard_top_level_never_executes(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            server = fixture.private / SETUP.MCP_NAME
            server.write_bytes((SCRIPTS / SETUP.MCP_NAME).read_bytes())
            server.chmod(0o600)
            expected = {key: hashlib.sha256((fixture.private / name).read_bytes()).hexdigest()
                        for key, name in {"server_sha256": SETUP.MCP_NAME, "hook_sha256": "slurm_cancel_hook.py",
                                          "runtime_sha256": "runtime.json", "policy_sha256": "policy.json"}.items()}
            expected["sdk_version"] = "1.30.0"
            marker = fixture.root / "must-not-exist"
            fixture.hook.write_text("from pathlib import Path\nPath(" + repr(str(marker)) + ").touch()\n")
            isolated = load_module("tampered_guard_mcp_probe", server)
            self.assertFalse(marker.exists())
            with self.assertRaisesRegex(ValueError, "frozen_hook_sha256_mismatch"):
                isolated.pinned_runtime(expected)
            self.assertFalse(marker.exists())

    def test_frozen_runtime_policy_and_loaded_code_identity(self):
        for drift in ("runtime", "policy", "guard"):
            with self.subTest(drift=drift), tempfile.TemporaryDirectory() as temp:
                fixture = PortableFixture(Path(temp))
                source = (SCRIPTS / SETUP.MCP_NAME).read_bytes()
                server = fixture.private / SETUP.MCP_NAME
                server.write_bytes(source)
                server.chmod(0o600)
                def digest(name):
                    return hashlib.sha256((fixture.private / name).read_bytes()).hexdigest()
                expected = {"server_sha256": digest(SETUP.MCP_NAME), "hook_sha256": digest("slurm_cancel_hook.py"),
                            "runtime_sha256": digest("runtime.json"), "policy_sha256": digest("policy.json"), "sdk_version": "1.30.0"}
                with patch.object(MCP, "ROOT", fixture.private):
                    MCP.pinned_runtime(expected)
                    if drift == "runtime":
                        path = fixture.private / "runtime.json"
                        runtime = json.loads(path.read_text())
                        runtime.update(scancel_path=str(fixture.scontrol), scancel_path_realpath=str(fixture.scontrol))
                        path.write_text(json.dumps(runtime))
                    elif drift == "policy":
                        path = fixture.private / "policy.json"
                        path.write_text(json.dumps({"protected_cancel_partitions": ["different-protected"]}))
                        runtime_path = fixture.private / "runtime.json"
                        runtime = json.loads(runtime_path.read_text())
                        runtime["policy_sha256"] = digest("policy.json")
                        runtime_path.write_text(json.dumps(runtime))
                    else:
                        (fixture.private / "slurm_cancel_hook.py").write_text("# altered code\n")
                    with self.assertRaisesRegex(ValueError, "frozen_.*_mismatch"):
                        MCP.pinned_runtime(expected)
                    self.assertEqual(fixture.mutation_argvs(), [])

    def render(self, fixture):
        real = subprocess.run
        def run(argv, **kwargs):
            if "import importlib.metadata;from mcp.server" in " ".join(map(str, argv)):
                return subprocess.CompletedProcess(argv, 0, "1.30.0\n", "")
            return real(argv, **kwargs)
        with patch.object(SETUP.subprocess, "run", side_effect=run):
            return SETUP.render_global_contract(fixture.codex_home, SCRIPTS, fixture.scontrol, fixture.scancel,
                                               ["protected-lab"], mcp_python=Path(sys.executable))

    def test_both_handlers_same_match_guard_bytes_and_trust_unchanged(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            new = self.render(fixture)
            hooks = new["hooks"]
            self.assertNotIn("PostToolUse", hooks)
            group = hooks["PreToolUse"][0]
            self.assertEqual(group["matcher"], "^Bash$")
            self.assertEqual([h["type"] for h in group["hooks"]], ["command", "mcp_tool"])
            self.assertEqual(group["hooks"][0], fixture.rendered["hooks"]["PreToolUse"][0]["hooks"][0])
            for path, data in fixture.rendered["files"].items():
                self.assertEqual(new["files"][path], data)
            self.assertEqual(new["manifest"]["hook_current_hashes"]["pre_tool_use"], fixture.rendered["manifest"]["hook_current_hashes"]["pre_tool_use"])
            original = (fixture.codex_home / "config.toml").read_text() + '\n[[hooks.Stop]]\nmatcher="keep"\nhooks=[]\n'
            updated = SETUP.update_user_config_text(original, new)
            parsed, before = tomllib.loads(updated), tomllib.loads(original)
            self.assertEqual(parsed["hooks"]["state"], before["hooks"]["state"])
            self.assertEqual(parsed["hooks"]["Stop"], before["hooks"]["Stop"])
            self.assertEqual(parsed["permissions"], before["permissions"])
            self.assertNotIn("PostToolUse", parsed["hooks"])
            handler = parsed["hooks"]["PreToolUse"][0]["hooks"][1]
            self.assertEqual(handler["input"]["event"]["session_id"], "${session_id}")
            # Actual root events omit both optional fields. Expansion must not
            # depend on either field, and must still reach the MCP handler.
            event = fixture.shell_event("PreToolUse", MCP.PROBE_COMMAND)
            template = handler["input"]["event"]
            self.assertNotIn("agent_id", template)
            self.assertNotIn("agent_type", template)
            expanded = {key: event[value[2:-1]] for key, value in template.items()}
            self.assertEqual(expanded, event)
            self.assertNotIn("threadId", handler["input"])
            self.assertEqual(SETUP.update_user_config_text(updated, new), updated)

    def test_mcp_path_does_not_require_optional_default_mode_questions(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp))
            rendered = self.render(fixture)
            config = SETUP.update_user_config_text(fixture.original_config.replace("default_mode_request_user_input = true", "default_mode_request_user_input = false"), rendered)
            self.assertIn("default_mode_request_user_input = false", config)
            self.assertIn("mcp_tool", config)

    def test_failed_mcp_cannot_weaken_independent_command_guard(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = PortableFixture(Path(temp), {"5001": {"partition": "protected-lab", "state": "PENDING"}})
            rendered = self.render(fixture)
            # The command handler executes independently of any MCP connection.
            command = rendered["hooks"]["PreToolUse"][0]["hooks"][0]["command"]
            result = subprocess.run(command, shell=True, input=json.dumps(fixture.shell_event("PreToolUse", "scancel 5001")), capture_output=True, text=True)
            self.assertEqual(json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"], "deny")
            self.assertEqual(fixture.mutation_argvs(), [])


if __name__ == "__main__":
    unittest.main()
