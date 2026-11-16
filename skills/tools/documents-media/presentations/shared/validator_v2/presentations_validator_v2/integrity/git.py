from pathlib import Path
import os
import re
import subprocess

from ..io import EvidenceMissing, InputError, OID, repo_path, tagged


def git(root: Path, *args: str) -> bytes:
    process = subprocess.run(
        ["git", "--no-replace-objects", "--no-optional-locks", "-C", str(root), *args],
        capture_output=True, check=False,
        env={**{k: v for k, v in os.environ.items() if not k.startswith("GIT_")},
             "GIT_NO_LAZY_FETCH": "1", "GIT_TERMINAL_PROMPT": "0"},
    )
    if process.returncode:
        raise EvidenceMissing(f"Git {args[0]} could not resolve {' '.join(args[1:])}")
    return process.stdout


def identity(root: Path) -> str:
    origin = git(root, "config", "--local", "--get", "remote.origin.url").decode().strip()
    match = re.fullmatch(r"(?:https://github\.com/|git@github\.com:|ssh://git@github\.com/)"
                         r"([\w.-]+/[\w.-]+?)(?:\.git)?", origin)
    if not match:
        raise InputError("Repository origin has no supported repository identity")
    return match[1]


def tree(root: Path, commit: str) -> str:
    tagged(commit, OID, "commit")
    if git(root, "cat-file", "-t", commit).strip() != b"commit":
        raise InputError(f"Not a Git commit: {commit}")
    return git(root, "rev-parse", "--verify", f"{commit}^{{tree}}").decode().strip()


def blob_oid(root: Path, commit: str, path: str) -> str:
    locator = f"{tagged(commit, OID, 'commit')}:{repo_path(path)}"
    if git(root, "cat-file", "-t", locator).strip() != b"blob":
        raise InputError(f"Not a Git blob: {locator}")
    return git(root, "rev-parse", "--verify", locator).decode().strip()


def blob(root: Path, commit: str, path: str) -> bytes:
    return git(root, "cat-file", "blob", blob_oid(root, commit, path))


def changed_paths(root: Path, old: str, new: str) -> set[str]:
    data = git(root, "diff-tree", "--no-commit-id", "--name-only",
               "--no-renames", "-r", "-z", old, new, "--")
    return {path.decode() for path in data.split(b"\0") if path}
