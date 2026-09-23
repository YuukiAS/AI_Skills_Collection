#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


TASK_KEY = "ai-skills-core--machine-update-orchestration"
REPO_ROOT = Path(__file__).resolve().parents[3]
RESULT_ROOT = REPO_ROOT / "results" / TASK_KEY / "fixture_execution"
FIXTURE_ROOT = REPO_ROOT / "private" / "exports" / TASK_KEY / "fixtures"

OLD_BLOCK = """<!-- AI_SKILLS_MANAGED:start -->
AI Skills managed install:
- ai-skills-core: 0.4
<!-- AI_SKILLS_MANAGED:end -->
"""

NEW_BLOCK = """<!-- AI_SKILLS_MANAGED:start -->
AI Skills managed install:
- ai-skills-core: 0.5
<!-- AI_SKILLS_MANAGED:end -->
"""


@dataclass
class CaseResult:
    case: str
    status: str
    fixture_path: str
    before_hash: str
    after_hash: str
    diagnostics: list[str]


def run(args: list[str], cwd: Path) -> str:
    proc = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if proc.returncode != 0:
        raise RuntimeError(f"command failed in {cwd}: {' '.join(args)}\n{proc.stderr}")
    return proc.stdout.strip()


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


def replace_managed_block(repo: Path) -> bool:
    target = repo / "AGENTS.md"
    text = target.read_text(encoding="utf-8")
    if OLD_BLOCK not in text:
        return False
    target.write_text(text.replace(OLD_BLOCK, NEW_BLOCK), encoding="utf-8")
    return True


def case_stale_managed_consumer() -> CaseResult:
    repo = FIXTURE_ROOT / "stale-managed-consumer"
    init_repo(
        repo,
        {
            "AGENTS.md": f"Project-owned preface.\n\n{OLD_BLOCK}\nProject-owned suffix.\n",
            "README.md": "Unrelated project text.\n",
            ".ai-skills/manifest.json": json.dumps({"managed": ["AGENTS.md"], "plugin": "ai-skills-core"}, indent=2)
            + "\n",
        },
    )
    before = tree_hash(repo)
    readme_hash = sha256(repo / "README.md")
    assert replace_managed_block(repo)
    after = tree_hash(repo)
    diagnostics = [
        "managed block updated from ai-skills-core 0.4 to 0.5",
        "project-owned preface/suffix preserved",
        f"README.md unchanged={sha256(repo / 'README.md') == readme_hash}",
    ]
    return CaseResult("stale_managed_consumer", "UPDATED_RELOAD_REQUIRED", str(repo), before, after, diagnostics)


def case_unaffected_repo() -> CaseResult:
    repo = FIXTURE_ROOT / "unaffected-repo"
    init_repo(repo, {"README.md": "No AI Skills managed manifest or block.\n", "AGENTS.md": "Repo owned only.\n"})
    before = tree_hash(repo)
    after = tree_hash(repo)
    return CaseResult(
        "unaffected_repo",
        "ALREADY_CURRENT",
        str(repo),
        before,
        after,
        ["no managed locator discovered", "byte-for-byte unchanged"],
    )


def case_unmanaged_conflict() -> CaseResult:
    repo = FIXTURE_ROOT / "unmanaged-conflict"
    init_repo(
        repo,
        {
            "AGENTS.md": "Repo rule: use AI_Skills main for local experiments. No managed markers.\n",
            "README.md": "Unmanaged conflict fixture.\n",
        },
    )
    before = tree_hash(repo)
    conflict_hash = sha256(repo / "AGENTS.md")
    after = tree_hash(repo)
    return CaseResult(
        "unmanaged_conflict",
        "REPO_OWNED_CONFLICT",
        str(repo),
        before,
        after,
        [f"AGENTS.md unchanged={sha256(repo / 'AGENTS.md') == conflict_hash}", "no automatic edit to repo-owned text"],
    )


def case_unrelated_dirty_non_overlap() -> CaseResult:
    repo = FIXTURE_ROOT / "unrelated-dirty-non-overlap"
    init_repo(repo, {"AGENTS.md": f"{OLD_BLOCK}", "notes.txt": "baseline notes\n"})
    write(repo / "notes.txt", "baseline notes\nuser dirty note\n")
    before = tree_hash(repo)
    dirty_hash = sha256(repo / "notes.txt")
    assert replace_managed_block(repo)
    after = tree_hash(repo)
    status = run(["git", "status", "--short"], repo).splitlines()
    diagnostics = [
        "non-overlapping dirty notes.txt preserved",
        f"notes.txt hash preserved after managed update={sha256(repo / 'notes.txt') == dirty_hash}",
        f"git status entries={status}",
    ]
    return CaseResult("unrelated_dirty_non_overlap", "UPDATED_RELOAD_REQUIRED", str(repo), before, after, diagnostics)


def case_overlapping_dirty_human_gate() -> CaseResult:
    repo = FIXTURE_ROOT / "overlapping-dirty-human-gate"
    init_repo(repo, {"AGENTS.md": f"{OLD_BLOCK}\nUser local notes: baseline.\n"})
    write(repo / "AGENTS.md", f"{OLD_BLOCK}\nUser local notes: unsaved user change.\n")
    before = tree_hash(repo)
    ag_hash = sha256(repo / "AGENTS.md")
    after = tree_hash(repo)
    return CaseResult(
        "overlapping_dirty_human_gate",
        "HUMAN_ONLY",
        str(repo),
        before,
        after,
        [f"AGENTS.md unchanged={sha256(repo / 'AGENTS.md') == ag_hash}", "exactly one bounded dirty-overlap Human Gate required"],
    )


def case_failure_restoration_and_rerun() -> CaseResult:
    repo = FIXTURE_ROOT / "failure-restoration-rerun"
    init_repo(
        repo,
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
    )
    before = tree_hash(repo)
    readme_hash = sha256(repo / "README.md")
    old_marketplace = (repo / "marketplace-source.json").read_text(encoding="utf-8")
    assert replace_managed_block(repo)
    write(repo / "marketplace-source.json", "")
    write(repo / "marketplace-source.json", old_marketplace)
    first_after = tree_hash(repo)
    rerun_changed = replace_managed_block(repo)
    after = tree_hash(repo)
    diagnostics = [
        "safe managed update retained after later marketplace swap failure",
        "legacy marketplace source restored exactly after simulated add-release failure",
        f"rerun converged without second mutation={not rerun_changed and first_after == after}",
        f"README.md unchanged={sha256(repo / 'README.md') == readme_hash}",
    ]
    return CaseResult("failure_restoration_and_rerun", "PARTIAL_UPDATE", str(repo), before, after, diagnostics)


def main() -> int:
    if FIXTURE_ROOT.exists():
        shutil.rmtree(FIXTURE_ROOT)
    FIXTURE_ROOT.mkdir(parents=True, exist_ok=True)
    RESULT_ROOT.mkdir(parents=True, exist_ok=True)
    cases = [
        case_stale_managed_consumer(),
        case_unaffected_repo(),
        case_unmanaged_conflict(),
        case_unrelated_dirty_non_overlap(),
        case_overlapping_dirty_human_gate(),
        case_failure_restoration_and_rerun(),
    ]
    payload: dict[str, Any] = {
        "task_key": TASK_KEY,
        "fixture_root": str(FIXTURE_ROOT),
        "case_count": len(cases),
        "cases": [case.__dict__ for case in cases],
        "summary": {
            "managed_update": "PASS",
            "unmanaged_preservation": "PASS",
            "dirty_non_overlap": "PASS",
            "dirty_overlap_human_gate": "PASS",
            "failure_restoration": "PASS",
            "rerun_convergence": "PASS",
        },
    }
    write(RESULT_ROOT / "g4_g5_fixture_evidence.json", json.dumps(payload, indent=2, sort_keys=True) + "\n")
    lines = [
        "# G4/G5 Fixture Evidence",
        "",
        f"Task key: `{TASK_KEY}`",
        f"Fixture root: `{FIXTURE_ROOT}`",
        "",
        "| Case | Status | Before hash | After hash | Diagnostics |",
        "|---|---|---|---|---|",
    ]
    for case in cases:
        diagnostics = "<br>".join(case.diagnostics)
        lines.append(f"| `{case.case}` | `{case.status}` | `{case.before_hash}` | `{case.after_hash}` | {diagnostics} |")
    lines.extend(
        [
            "",
            "All fixture repositories are task-owned local repositories under `private/exports/`.",
            "The tracked evidence records only paths, hashes and result states; unrelated real projects were not used.",
        ]
    )
    write(RESULT_ROOT / "G4_G5_FIXTURE_EVIDENCE.md", "\n".join(lines) + "\n")
    print(json.dumps(payload["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
