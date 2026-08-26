from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import resolve_reviewed_handoff_visual_target as resolver  # noqa: E402


IMPLEMENTATION_COMMIT = "a" * 40


def write_json(path: Path, data: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def manifest_path(task_key: str) -> Path:
    return Path("results") / task_key / "visual_review" / "visual_inputs.json"


def evidence_path(task_key: str) -> Path:
    return Path("results") / task_key / "visual_review" / "VISUAL_REVIEW.json"


def manifest_data(task_key: str, implementation_commit: str = IMPLEMENTATION_COMMIT) -> dict[str, object]:
    return {
        "schema": "AI_BRIDGE_VISUAL_INPUT_MANIFEST_V1",
        "task_key": task_key,
        "workflow_type": "reviewed_handoff",
        "identity_bindings": {
            "task_key": task_key,
            "implementation_commit": implementation_commit,
        },
        "inputs": [],
    }


def write_current(
    root: Path,
    task_key: str,
    *,
    state: str = "READY_FOR_GPT_REVIEW",
    implementation_commit: str = IMPLEMENTATION_COMMIT,
    visual_review_required: bool = True,
) -> None:
    write_json(
        root / "automation" / "reviewed_handoff" / "tasks" / task_key / "CURRENT.json",
        {
            "schema": "AI_BRIDGE_REVIEWED_CURRENT_V1",
            "task_key": task_key,
            "state": state,
            "implementation_commit": implementation_commit,
            "visual_review_required": visual_review_required,
            "visual_review_manifest_path": manifest_path(task_key).as_posix(),
            "visual_review_evidence_path": evidence_path(task_key).as_posix(),
        },
    )


def write_manifest(root: Path, task_key: str, data: dict[str, object] | None = None) -> None:
    write_json(root / manifest_path(task_key), data or manifest_data(task_key))


def write_fresh_evidence(root: Path, task_key: str, implementation_commit: str = IMPLEMENTATION_COMMIT) -> None:
    manifest_bytes = (root / manifest_path(task_key)).read_bytes()
    write_json(
        root / evidence_path(task_key),
        {
            "input_manifest": {
                "manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
                "identity_bindings": {
                    "task_key": task_key,
                    "implementation_commit": implementation_commit,
                },
            }
        },
    )


class ReviewedHandoffVisualTargetTests(unittest.TestCase):
    def test_no_visual_review_task_is_noop(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current(root, "task_a", visual_review_required=False)
            self.assertIsNone(resolver.resolve_visual_target(root))

    def test_single_pending_task_returns_task_local_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current(root, "task_a")
            write_manifest(root, "task_a")

            target = resolver.resolve_visual_target(root)

            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.task_key, "task_a")
            self.assertEqual(target.manifest_path, "results/task_a/visual_review/visual_inputs.json")
            self.assertEqual(target.evidence_path, "results/task_a/visual_review/VISUAL_REVIEW.json")

    def test_fresh_evidence_noops(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current(root, "task_a")
            write_manifest(root, "task_a")
            write_fresh_evidence(root, "task_a")

            self.assertIsNone(resolver.resolve_visual_target(root))

    def test_stale_evidence_is_pending(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current(root, "task_a")
            write_manifest(root, "task_a")
            write_json(
                root / evidence_path("task_a"),
                {
                    "input_manifest": {
                        "manifest_sha256": "stale",
                        "identity_bindings": {
                            "task_key": "task_a",
                            "implementation_commit": IMPLEMENTATION_COMMIT,
                        },
                    }
                },
            )

            target = resolver.resolve_visual_target(root)

            self.assertIsNotNone(target)
            assert target is not None
            self.assertEqual(target.task_key, "task_a")

    def test_manifest_task_key_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current(root, "task_a")
            bad_manifest = manifest_data("other_task")
            write_manifest(root, "task_a", bad_manifest)

            with self.assertRaisesRegex(resolver.ResolutionError, "task_key does not match"):
                resolver.resolve_visual_target(root)

    def test_manifest_implementation_commit_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current(root, "task_a")
            write_manifest(root, "task_a", manifest_data("task_a", implementation_commit="b" * 40))

            with self.assertRaisesRegex(resolver.ResolutionError, "implementation_commit does not match"):
                resolver.resolve_visual_target(root)

    def test_two_pending_tasks_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for task_key in ("task_a", "task_b"):
                write_current(root, task_key)
                write_manifest(root, task_key)

            with self.assertRaisesRegex(resolver.ResolutionError, "multiple pending"):
                resolver.resolve_visual_target(root)

    def test_non_ready_visual_task_is_not_a_push_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_current(root, "task_a", state="WAITING_FOR_CI")
            write_manifest(root, "task_a")

            self.assertIsNone(resolver.resolve_visual_target(root))

    def test_github_env_marks_noop_and_selected_states(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            env_file = root / "env.txt"
            resolver.write_github_env(env_file, None)
            self.assertEqual(env_file.read_text(encoding="utf-8"), "AI_BRIDGE_VISUAL_REVIEW_SKIP=1\n")

            target = resolver.VisualTarget(
                task_key="task_a",
                manifest_path="results/task_a/visual_review/visual_inputs.json",
                evidence_path="results/task_a/visual_review/VISUAL_REVIEW.json",
                implementation_commit=IMPLEMENTATION_COMMIT,
            )
            resolver.write_github_env(env_file, target)
            text = env_file.read_text(encoding="utf-8")
            self.assertIn("AI_BRIDGE_VISUAL_REVIEW_SKIP=0\n", text)
            self.assertIn("AI_BRIDGE_VISUAL_REVIEW_TASK_KEY=task_a\n", text)
            self.assertIn("AI_BRIDGE_VISUAL_REVIEW_MANIFEST=results/task_a/visual_review/visual_inputs.json\n", text)
            self.assertIn("AI_BRIDGE_VISUAL_REVIEW_OUTPUT=results/task_a/visual_review/VISUAL_REVIEW.json\n", text)


class VisualReviewWorkflowTests(unittest.TestCase):
    def test_dispatch_inputs_are_preserved_and_pin_is_current(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/ai-bridge-visual-review.yml").read_text(encoding="utf-8")
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("github.event.inputs.manifest", workflow)
        self.assertIn("github.event.inputs.output", workflow)
        self.assertIn("647f63c49ccea828a0ac76a6e9adce026531c906", workflow)

    def test_push_path_uses_resolver_not_repository_level_vars(self) -> None:
        workflow = (REPO_ROOT / ".github/workflows/ai-bridge-visual-review.yml").read_text(encoding="utf-8")
        self.assertIn("scripts/resolve_reviewed_handoff_visual_target.py", workflow)
        self.assertIn("--github-env", workflow)
        self.assertNotIn("vars.AI_BRIDGE_VISUAL_REVIEW_MANIFEST", workflow)
        self.assertNotIn("vars.AI_BRIDGE_VISUAL_REVIEW_OUTPUT", workflow)
        self.assertIn("no task-local visual review pending", workflow)


if __name__ == "__main__":
    unittest.main()
