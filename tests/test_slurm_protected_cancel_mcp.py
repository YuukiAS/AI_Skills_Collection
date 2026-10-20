from __future__ import annotations

import asyncio
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

from test_slurm_protected_cancel import HOOK, SETUP, SCRIPTS, PortableFixture, load_module

MCP = load_module("slurm_protected_cancel_mcp", SCRIPTS / "slurm_protected_cancel_mcp.py")


def result_data(result):
    return json.loads(result["hookSpecificOutput"]["permissionDecisionReason"])


class TestMcpProtectedCancel(unittest.IsolatedAsyncioTestCase):
    async def invoke(self, fixture, response, command="scancel 5001", **extra):
        private, runtime = MCP.guard._load_runtime(fixture.hook)
        event = fixture.shell_event("PreToolUse", command)
        event.update(extra)
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
            self.assertEqual(observations, [False, False, True])
            self.assertEqual(result_data(result)["mutation_count"], 1)
            self.assertEqual(fixture.mutation_argvs(), [["5001"]])
            reservation = json.loads(next((fixture.private / "consumed").glob("*.json")).read_text())
            self.assertEqual(reservation["status"], "completed")
            records = {json.loads(p.read_text())["phase"]: json.loads(p.read_text()) for p in (fixture.private / "audit").glob("*.json")}
            self.assertLess(records["reserved"]["time_ns"], records["final_resolved"]["time_ns"])
            self.assertLess(records["final_resolved"]["time_ns"], records["invocation_intent"]["time_ns"])
            self.assertTrue(MCP.possible_invocation(fixture.private, fixture.shell_event("PreToolUse", "scancel 5001")))
            with self.assertRaises(FileExistsError):
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
            unrelated = {"tool_input": {"command": "printf harmless"}, "agent_id": "child"}
            self.assertEqual(await MCP.handle(unrelated, {}, private, runtime, forbidden), {})

    async def test_unsupported_selector_still_denied_without_elicitation(self):
        with tempfile.TemporaryDirectory() as temp:
            fixture = self.fixture(Path(temp))
            for index, command in enumerate(("scancel --help", "scancel -u user", "scancel 5001; true")):
                result = await self.invoke(fixture, None, command, tool_use_id="unsupported-" + str(index))
                self.assertEqual(result["hookSpecificOutput"]["permissionDecision"], "deny")
                self.assertEqual(fixture.mutation_argvs(), [])


class TestMcpInstaller(unittest.TestCase):
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
