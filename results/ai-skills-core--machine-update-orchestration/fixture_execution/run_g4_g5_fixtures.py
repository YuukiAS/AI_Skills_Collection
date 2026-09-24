#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


TASK_KEY = "ai-skills-core--machine-update-orchestration"
REPO_ROOT = Path(__file__).resolve().parents[3]
RESULT_ROOT = REPO_ROOT / "results" / TASK_KEY / "fixture_execution"
FIXTURE_ROOT = REPO_ROOT / "private" / "exports" / TASK_KEY / "fixtures"
TASK_PATH = RESULT_ROOT / "candidate_g4_g5_task.md"
MANIFEST_PATH = RESULT_ROOT / "candidate_g4_g5_manifest.json"
OUTPUT_NAME = "g4_g5_candidate_result.json"
CODEX_CLI = REPO_ROOT / ".local-runtime" / "codex" / "0.153.4" / "bin" / "codex"
ISOLATED_CODEX_HOME = FIXTURE_ROOT / "isolated-codex-home"
MARKETPLACE_ROOT = FIXTURE_ROOT / "isolated-marketplaces"
LEGACY_MARKETPLACE = MARKETPLACE_ROOT / "legacy-main"
BROKEN_RELEASE_MARKETPLACE = MARKETPLACE_ROOT / "missing-release-source"
MARKETPLACE_NAME = "yuukias-ai-skills"

OLD_BLOCK = """<!-- AI_SKILLS_MANAGED:start -->
AI Skills managed install:
- ai-skills-core: 0.4
<!-- AI_SKILLS_MANAGED:end -->
"""


@dataclass
class CaseFixture:
    case: str
    fixture_path: Path
    before_hash: str
    watched_hashes: dict[str, str]


def run(
    args: list[str],
    cwd: Path,
    *,
    check: bool = True,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(
        args,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        env=env,
    )
    if check and proc.returncode != 0:
        raise RuntimeError(f"command failed in {cwd}: {' '.join(args)}\n{proc.stderr}")
    return proc


def isolated_codex_env() -> dict[str, str]:
    env = os.environ.copy()
    env["CODEX_HOME"] = str(ISOLATED_CODEX_HOME)
    return env


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def tree_hash(root: Path) -> str:
    h = hashlib.sha256()
    for path in sorted(p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts):
        h.update(path.relative_to(root).as_posix().encode("utf-8"))
        h.update(b"\0")
        h.update(sha256(path).encode("ascii"))
        h.update(b"\0")
    return h.hexdigest()


def init_repo(path: Path, files: dict[str, str]) -> None:
    path.mkdir(parents=True, exist_ok=True)
    for name, text in files.items():
        write(path / name, text)
    run(["git", "init", "-q"], path)
    run(["git", "add", "."], path)
    run(
        [
            "git",
            "-c",
            "user.name=Fixture Runner",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-q",
            "-m",
            "baseline fixture",
        ],
        path,
    )


def write_marketplace(root: Path, *, ref_label: str) -> None:
    write(
        root / ".agents" / "plugins" / "marketplace.json",
        json.dumps(
            {
                "name": MARKETPLACE_NAME,
                "interface": {"displayName": f"Fixture AI Skills {ref_label}"},
                "plugins": [],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
    )


def setup_isolated_marketplace() -> dict[str, Any]:
    if not CODEX_CLI.is_file():
        raise RuntimeError(f"missing pinned codex CLI: {CODEX_CLI}")

    ISOLATED_CODEX_HOME.mkdir(parents=True, exist_ok=True)
    write_marketplace(LEGACY_MARKETPLACE, ref_label="main")

    add = run(
        [str(CODEX_CLI), "plugin", "marketplace", "add", str(LEGACY_MARKETPLACE), "--json"],
        REPO_ROOT,
        env=isolated_codex_env(),
    )
    listed = run(
        [str(CODEX_CLI), "plugin", "marketplace", "list", "--json"],
        REPO_ROOT,
        env=isolated_codex_env(),
    )
    return {
        "seed_add_stdout": add.stdout,
        "seed_add_stderr": add.stderr,
        "seed_list_stdout": listed.stdout,
        "seed_list_stderr": listed.stderr,
    }


def setup_fixtures() -> list[CaseFixture]:
    if FIXTURE_ROOT.exists():
        shutil.rmtree(FIXTURE_ROOT)
    FIXTURE_ROOT.mkdir(parents=True, exist_ok=True)

    fixtures: list[CaseFixture] = []

    def add(case: str, rel: str, files: dict[str, str], watched: list[str]) -> Path:
        repo = FIXTURE_ROOT / rel
        init_repo(repo, files)
        fixtures.append(
            CaseFixture(
                case=case,
                fixture_path=repo,
                before_hash=tree_hash(repo),
                watched_hashes={name: sha256(repo / name) for name in watched},
            )
        )
        return repo

    add(
        "stale_managed_consumer",
        "stale-managed-consumer",
        {
            "AGENTS.md": f"Project-owned preface.\n\n{OLD_BLOCK}\nProject-owned suffix.\n",
            "README.md": "Unrelated project text.\n",
            ".ai-skills/manifest.json": json.dumps({"managed": ["AGENTS.md"], "plugin": "ai-skills-core"}, indent=2)
            + "\n",
        },
        ["AGENTS.md", "README.md"],
    )

    add(
        "unaffected_repo",
        "unaffected-repo",
        {"README.md": "No AI Skills managed manifest or block.\n", "AGENTS.md": "Repo owned only.\n"},
        ["AGENTS.md", "README.md"],
    )

    add(
        "unmanaged_conflict",
        "unmanaged-conflict",
        {
            "AGENTS.md": "Repo rule: use AI_Skills main for local experiments. No managed markers.\n",
            "README.md": "Unmanaged conflict fixture.\n",
        },
        ["AGENTS.md"],
    )

    dirty = add(
        "unrelated_dirty_non_overlap",
        "unrelated-dirty-non-overlap",
        {"AGENTS.md": f"{OLD_BLOCK}", "notes.txt": "baseline notes\n"},
        ["AGENTS.md", "notes.txt"],
    )
    write(dirty / "notes.txt", "baseline notes\nuser dirty note\n")
    fixtures[-1].before_hash = tree_hash(dirty)
    fixtures[-1].watched_hashes["notes.txt"] = sha256(dirty / "notes.txt")

    overlap = add(
        "overlapping_dirty_human_gate",
        "overlapping-dirty-human-gate",
        {"AGENTS.md": f"{OLD_BLOCK}\nUser local notes: baseline.\n"},
        ["AGENTS.md"],
    )
    write(overlap / "AGENTS.md", f"{OLD_BLOCK}\nUser local notes: unsaved user change.\n")
    fixtures[-1].before_hash = tree_hash(overlap)
    fixtures[-1].watched_hashes["AGENTS.md"] = sha256(overlap / "AGENTS.md")

    add(
        "failure_restoration_and_rerun",
        "failure-restoration-rerun",
        {
            "AGENTS.md": f"{OLD_BLOCK}",
            "marketplace-source.json": json.dumps(
                {
                    "name": "yuukias-ai-skills",
                    "source": "https://github.com/YuukiAS/AI_Skills_Collection.git",
                    "ref": "main",
                    "sparse": [".agents/plugins", "plugins/codex/plugins"],
                },
                indent=2,
            )
            + "\n",
            "README.md": "Should not change.\n",
        },
        ["AGENTS.md", "marketplace-source.json", "README.md"],
    )

    return fixtures


def write_task_and_manifest(
    fixtures: list[CaseFixture],
    candidate_commit: str,
    marketplace_setup: dict[str, Any],
) -> None:
    manifest = {
        "task_key": TASK_KEY,
        "candidate_commit": candidate_commit,
        "fixture_root": str(FIXTURE_ROOT),
        "output_name": OUTPUT_NAME,
        "isolated_codex_home": str(ISOLATED_CODEX_HOME),
        "codex_cli": str(CODEX_CLI),
        "marketplace": {
            "name": MARKETPLACE_NAME,
            "initial_legacy_source": str(LEGACY_MARKETPLACE),
            "replacement_source_for_failure_injection": str(BROKEN_RELEASE_MARKETPLACE),
            "restore_source": str(LEGACY_MARKETPLACE),
            "official_command_boundary": "Use only `codex plugin marketplace list/remove/add --json` with the isolated CODEX_HOME.",
            "setup_evidence": marketplace_setup,
        },
        "cases": [
            {
                "case": item.case,
                "fixture_path": str(item.fixture_path),
                "scenario": {
                    "stale_managed_consumer": "contains an AI_Skills managed block pinned to ai-skills-core 0.4 and project-owned surrounding text",
                    "unaffected_repo": "contains no AI_Skills managed manifest or managed block",
                    "unmanaged_conflict": "contains repo-owned AI_Skills-looking text without managed markers",
                    "unrelated_dirty_non_overlap": "contains a stale managed block plus unrelated dirty notes.txt",
                    "overlapping_dirty_human_gate": "contains stale managed content with overlapping user dirty work in the same file",
                    "failure_restoration_and_rerun": "contains a stale managed block and an isolated legacy Marketplace source that must be restored after injected replacement failure",
                }[item.case],
                "before_hash": item.before_hash,
                "watched_hashes": item.watched_hashes,
            }
            for item in fixtures
        ],
        "status_vocabulary": [
            "UPDATED_RELOAD_REQUIRED",
            "ALREADY_CURRENT",
            "REPO_OWNED_CONFLICT",
            "HUMAN_ONLY",
            "PARTIAL_UPDATE",
        ],
        "owner_path_boundary": "Select the canonical AI Skills Maintainer owner path from the candidate plugin; the harness does not prescribe the path.",
    }
    write(MANIFEST_PATH, json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    write(
        TASK_PATH,
        f"""# Candidate Replay Task: G4/G5 Machine Update Fixture Execution

Use AI Skills Maintainer.

This is release-critical candidate-direct evidence for task `{TASK_KEY}`. Read
the attached manifest and operate only on the task-owned fixture repositories
listed there. Do not use unrelated real projects.

For every case, select the production owner path from the candidate plugin
itself. The fixture harness owns setup and invariant checks only; the semantic
action and returned state must come from this candidate run.

Required output: write JSON to `outputs/{OUTPUT_NAME}` with:

```json
{{
  "candidate_commit": "{candidate_commit}",
  "candidate_plugin": "ai-skills-core@ai-skills-candidate",
  "owner_path_consumed": "...",
  "marketplace_commands": [
    {{
      "argv": ["...", "plugin", "marketplace", "list", "--json"],
      "codex_home": "...",
      "returncode": 0
    }}
  ],
  "cases": [
    {{
      "case": "stale_managed_consumer",
      "status": "...",
      "failure_injection_point": null,
      "diagnostics": ["..."],
      "human_gate_count": 0
    }}
  ]
}}
```

Case requirements:

- For managed consumer fixtures, use the AI_Skills managed markers/manifest to
  decide whether a candidate-owned update is allowed. Preserve project-owned
  text and unrelated dirty files.
- For repo-owned apparent conflicts without managed ownership, preserve bytes
  and classify using the Maintainer conflict contract.
- For overlapping user-owned dirty work, emit exactly one bounded Human Gate
  and leave the overlapping user file unchanged.
- For the failure/restoration case, perform one safe managed consumer step
  first. Then use the manifest's isolated temporary `CODEX_HOME`, pinned
  `codex_cli`, and official `codex plugin marketplace` commands to exercise
  the legacy-source replacement path. Inject the bounded failure by attempting
  to add the provided missing replacement source after removing the legacy
  source. Restore the exact legacy source through the same official command
  family, run fresh discovery once, and report whether it converged without a
  second mutation.
- Select each case's returned status from the manifest vocabulary based on the
  actual candidate/owner behavior. Do not treat this task prompt as an answer
  key for the case outcomes.

Do not call paid APIs, do not mutate Marketplace/Host/global Codex state, and
do not change Git refs. The fixture repos themselves are writable for this
candidate replay.
""",
    )


def run_candidate(candidate_commit: str) -> dict[str, Any]:
    cmd = [
        sys.executable,
        "scripts/candidate_plugin_replay.py",
        "replay",
        "--plugin",
        "ai-skills-core",
        "--candidate-commit",
        candidate_commit,
        "--task",
        str(TASK_PATH.relative_to(REPO_ROOT)),
        "--input",
        str(MANIFEST_PATH.relative_to(REPO_ROOT)),
        "--writable-dir",
        str(FIXTURE_ROOT.relative_to(REPO_ROOT)),
    ]
    proc = run(cmd, REPO_ROOT)
    replay_result = json.loads(proc.stdout)
    run_dir = Path(replay_result["stdout_path"]).parent
    output_path = run_dir / "workspace" / "outputs" / OUTPUT_NAME
    if not output_path.is_file():
        raise RuntimeError(f"candidate did not write required output: {output_path}")
    candidate_result = json.loads(output_path.read_text(encoding="utf-8"))
    return {"replay": replay_result, "candidate": candidate_result, "output_path": str(output_path)}


def case_map(candidate_result: dict[str, Any]) -> dict[str, dict[str, Any]]:
    cases = candidate_result.get("cases")
    if not isinstance(cases, list):
        raise RuntimeError("candidate result missing cases list")
    mapped: dict[str, dict[str, Any]] = {}
    for item in cases:
        if not isinstance(item, dict) or not isinstance(item.get("case"), str):
            raise RuntimeError("candidate result case entry is invalid")
        mapped[item["case"]] = item
    return mapped


def assert_case_status(cases: dict[str, dict[str, Any]], case: str, expected: str) -> dict[str, Any]:
    if case not in cases:
        raise AssertionError(f"candidate omitted case {case}")
    actual = cases[case].get("status")
    if actual != expected:
        raise AssertionError(f"{case}: expected {expected}, got {actual}")
    return cases[case]


def assert_marketplace_command_evidence(candidate_result: dict[str, Any]) -> list[dict[str, Any]]:
    commands = candidate_result.get("marketplace_commands")
    if not isinstance(commands, list) or not commands:
        raise AssertionError("candidate did not record official Marketplace command evidence")
    normalized: list[str] = []
    for item in commands:
        if not isinstance(item, dict):
            raise AssertionError("marketplace command evidence entry is not an object")
        argv = item.get("argv")
        if isinstance(argv, list):
            normalized.append(" ".join(str(part) for part in argv))
        elif isinstance(argv, str):
            normalized.append(argv)
        else:
            raise AssertionError("marketplace command evidence entry lacks argv")
        if str(item.get("codex_home")) != str(ISOLATED_CODEX_HOME):
            raise AssertionError("marketplace command did not bind the isolated CODEX_HOME")

    required = [
        "plugin marketplace list",
        "plugin marketplace remove",
        "plugin marketplace add",
    ]
    for needle in required:
        if not any(needle in command for command in normalized):
            raise AssertionError(f"candidate did not record official Marketplace command: {needle}")
    return commands


def assert_isolated_marketplace_restored() -> dict[str, Any]:
    proc = run(
        [str(CODEX_CLI), "plugin", "marketplace", "list", "--json"],
        REPO_ROOT,
        env=isolated_codex_env(),
    )
    listing = json.loads(proc.stdout)
    marketplaces = listing.get("marketplaces")
    if not isinstance(marketplaces, list):
        raise AssertionError("isolated Marketplace list output is invalid")
    matches = [item for item in marketplaces if item.get("name") == MARKETPLACE_NAME]
    if len(matches) != 1:
        raise AssertionError(f"expected exactly one restored marketplace named {MARKETPLACE_NAME}, got {len(matches)}")
    source = matches[0].get("marketplaceSource", {})
    if source.get("sourceType") != "local" or str(source.get("source")) != str(LEGACY_MARKETPLACE):
        raise AssertionError("legacy Marketplace source was not restored through official isolated Codex state")
    return {
        "list_stdout": proc.stdout,
        "list_stderr": proc.stderr,
        "restored_entry": matches[0],
    }


def validate(candidate_commit: str, fixtures: list[CaseFixture], run_result: dict[str, Any]) -> dict[str, Any]:
    candidate_result = run_result["candidate"]
    if candidate_result.get("candidate_commit") != candidate_commit:
        raise AssertionError("candidate result did not bind the requested candidate commit")
    owner_path = candidate_result.get("owner_path_consumed")
    if not isinstance(owner_path, str):
        raise AssertionError("candidate result did not record AI Skills Maintainer owner path")
    managed_owner_path = candidate_result.get("managed_consumer_owner_path_consumed")
    owner_path_ok = (
        "AI Skills Maintainer" in owner_path
        or (
            "ai-skills-candidate/ai-skills-core/0.5/skills/orchestrator/SKILL.md" in owner_path
            and (
                "ai-skills-candidate/ai-skills-core/0.5/skills/proj/SKILL.md" in owner_path
                or (
                    isinstance(managed_owner_path, str)
                    and "ai-skills-candidate/ai-skills-core/0.5/skills/proj/SKILL.md" in managed_owner_path
                )
            )
        )
    )
    if not owner_path_ok:
        raise AssertionError("candidate result did not record the candidate Maintainer owner path")

    fixtures_by_case = {item.case: item for item in fixtures}
    cases = case_map(candidate_result)

    assert_case_status(cases, "stale_managed_consumer", "UPDATED_RELOAD_REQUIRED")
    stale_repo = fixtures_by_case["stale_managed_consumer"].fixture_path
    if fixtures_by_case["stale_managed_consumer"].watched_hashes["AGENTS.md"] == sha256(stale_repo / "AGENTS.md"):
        raise AssertionError("stale managed consumer AGENTS.md was not updated by candidate")
    if fixtures_by_case["stale_managed_consumer"].watched_hashes["README.md"] != sha256(stale_repo / "README.md"):
        raise AssertionError("stale managed consumer README.md changed")

    assert_case_status(cases, "unaffected_repo", "ALREADY_CURRENT")
    if tree_hash(fixtures_by_case["unaffected_repo"].fixture_path) != fixtures_by_case["unaffected_repo"].before_hash:
        raise AssertionError("unaffected repo changed")

    assert_case_status(cases, "unmanaged_conflict", "REPO_OWNED_CONFLICT")
    conflict_repo = fixtures_by_case["unmanaged_conflict"].fixture_path
    if fixtures_by_case["unmanaged_conflict"].watched_hashes["AGENTS.md"] != sha256(conflict_repo / "AGENTS.md"):
        raise AssertionError("unmanaged conflict file changed")

    assert_case_status(cases, "unrelated_dirty_non_overlap", "UPDATED_RELOAD_REQUIRED")
    dirty_repo = fixtures_by_case["unrelated_dirty_non_overlap"].fixture_path
    if fixtures_by_case["unrelated_dirty_non_overlap"].watched_hashes["notes.txt"] != sha256(dirty_repo / "notes.txt"):
        raise AssertionError("dirty non-overlap file changed")
    if fixtures_by_case["unrelated_dirty_non_overlap"].watched_hashes["AGENTS.md"] == sha256(dirty_repo / "AGENTS.md"):
        raise AssertionError("dirty non-overlap managed block was not updated")

    overlap = assert_case_status(cases, "overlapping_dirty_human_gate", "HUMAN_ONLY")
    overlap_repo = fixtures_by_case["overlapping_dirty_human_gate"].fixture_path
    if fixtures_by_case["overlapping_dirty_human_gate"].watched_hashes["AGENTS.md"] != sha256(overlap_repo / "AGENTS.md"):
        raise AssertionError("dirty overlap AGENTS.md changed")
    if overlap.get("human_gate_count") != 1:
        raise AssertionError("dirty overlap did not report exactly one Human Gate")

    failure = assert_case_status(cases, "failure_restoration_and_rerun", "PARTIAL_UPDATE")
    marketplace_commands = assert_marketplace_command_evidence(candidate_result)
    marketplace_restoration = assert_isolated_marketplace_restored()
    failure_repo = fixtures_by_case["failure_restoration_and_rerun"].fixture_path
    if fixtures_by_case["failure_restoration_and_rerun"].watched_hashes["AGENTS.md"] == sha256(failure_repo / "AGENTS.md"):
        raise AssertionError("failure case safe managed update was not retained")
    if fixtures_by_case["failure_restoration_and_rerun"].watched_hashes["marketplace-source.json"] != sha256(
        failure_repo / "marketplace-source.json"
    ):
        raise AssertionError("failure case marketplace source was not restored exactly")
    if fixtures_by_case["failure_restoration_and_rerun"].watched_hashes["README.md"] != sha256(failure_repo / "README.md"):
        raise AssertionError("failure case unrelated README changed")
    if failure.get("failure_injection_point") in {None, ""}:
        raise AssertionError("failure case did not record failure injection point")
    rerun = failure.get("rerun")
    nested_converged = (
        isinstance(rerun, dict)
        and (rerun.get("managed_consumer_converged") is True or rerun.get("converged") is True)
        and rerun.get("mutation_count") == 0
    )
    if (
        failure.get("rerun_converged") is not True
        and failure.get("rerun_converged_without_second_mutation") is not True
        and not nested_converged
    ):
        raise AssertionError("failure case did not report fresh-discovery rerun convergence")

    summaries = []
    for item in fixtures:
        case = cases[item.case]
        summaries.append(
            {
                "case": item.case,
                "status": case["status"],
                "fixture_path": str(item.fixture_path),
                "before_hash": item.before_hash,
                "after_hash": tree_hash(item.fixture_path),
                "watched_hashes_before": item.watched_hashes,
                "watched_hashes_after": {
                    rel: sha256(item.fixture_path / rel)
                    for rel in item.watched_hashes
                    if (item.fixture_path / rel).is_file()
                },
                "diagnostics": case.get("diagnostics", []),
                "failure_injection_point": case.get("failure_injection_point"),
                "human_gate_count": case.get("human_gate_count", 0),
                "rerun": case.get("rerun"),
            }
        )

    return {
        "task_key": TASK_KEY,
        "candidate_commit": candidate_commit,
        "candidate_plugin": candidate_result.get("candidate_plugin"),
        "owner_path_consumed": owner_path,
        "replay_run": run_result["replay"],
        "candidate_output_path": run_result["output_path"],
        "fixture_root": str(FIXTURE_ROOT),
        "isolated_codex_home": str(ISOLATED_CODEX_HOME),
        "marketplace_recovery": {
            "name": MARKETPLACE_NAME,
            "legacy_source": str(LEGACY_MARKETPLACE),
            "replacement_failure_source": str(BROKEN_RELEASE_MARKETPLACE),
            "commands_recorded_by_candidate": marketplace_commands,
            "post_run_official_list": marketplace_restoration,
        },
        "case_count": len(summaries),
        "cases": summaries,
        "summary": {
            "managed_update": "PASS",
            "unmanaged_preservation": "PASS",
            "dirty_non_overlap": "PASS",
            "dirty_overlap_human_gate": "PASS",
            "failure_restoration": "PASS",
            "rerun_convergence": "PASS",
        },
        "notes": [
            "Harness created/reset fixtures, captured hashes, invoked the committed candidate replay, and asserted invariants.",
            "Semantic states and fixture mutations came from the candidate child run, not from harness-side business logic.",
        ],
    }


def write_evidence(payload: dict[str, Any]) -> None:
    write(RESULT_ROOT / "g4_g5_fixture_evidence.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    lines = [
        "# G4/G5 Fixture Evidence",
        "",
        f"Task key: `{TASK_KEY}`",
        f"Candidate commit: `{payload['candidate_commit']}`",
        f"Candidate/plugin/owner path consumed: `{payload['owner_path_consumed']}`",
        f"Fixture root: `{FIXTURE_ROOT}`",
        f"Isolated CODEX_HOME: `{payload['isolated_codex_home']}`",
        f"Candidate output: `{payload['candidate_output_path']}`",
        f"Marketplace recovery source restored: `{payload['marketplace_recovery']['legacy_source']}`",
        "",
        "| Case | Status | Before hash | After hash | Failure injection | Diagnostics |",
        "|---|---|---|---|---|---|",
    ]
    for case in payload["cases"]:
        diagnostics = "<br>".join(str(item) for item in case.get("diagnostics", []))
        failure = case.get("failure_injection_point") or ""
        lines.append(
            f"| `{case['case']}` | `{case['status']}` | `{case['before_hash']}` | "
            f"`{case['after_hash']}` | `{failure}` | {diagnostics} |"
        )
    lines.extend(
        [
            "",
            "All fixture repositories are task-owned local repositories under `private/exports/`.",
            "Marketplace failure/recovery used an isolated temporary Codex identity and official `codex plugin marketplace` commands.",
            "The harness owns setup, failure injection fixtures, hashing, invariant assertions and evidence collation only.",
            "Actual semantic statuses and mutations were produced by the committed candidate through candidate plugin replay.",
        ]
    )
    write(RESULT_ROOT / "G4_G5_FIXTURE_EVIDENCE.md", "\n".join(lines) + "\n")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run G4/G5 fixtures through committed candidate plugin replay.")
    parser.add_argument("--candidate-commit", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    fixtures = setup_fixtures()
    marketplace_setup = setup_isolated_marketplace()
    write_task_and_manifest(fixtures, args.candidate_commit, marketplace_setup)
    run_result = run_candidate(args.candidate_commit)
    payload = validate(args.candidate_commit, fixtures, run_result)
    write_evidence(payload)
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
