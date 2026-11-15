"""Commit-aware replay for external repositories without checkout or mutation."""

from ..integrity.git import blob, identity, tree
from ..io import DIGEST, OID, EvidenceMissing, InputError, records, repo_path, sha256, tagged
from ..schemas import Finding


def replay(repo, config):
    if identity(repo) != config["repository"]:
        raise InputError("Replay repository does not match frozen identity")
    rows = []
    for entry_id, entry in records(config["locators"]).items():
        commit = tagged(entry["commit"], OID, "locator commit")
        path = repo_path(entry["path"])
        expected = entry.get("sha256")
        if expected is not None:
            tagged(expected, DIGEST, "locator sha256")
        locator = f"{commit}:{path}"
        try:
            tree(repo, commit)
            actual = sha256(blob(repo, commit, path))
        except EvidenceMissing:
            rows.append(Finding("REPLAY", "NOT_VERIFIED", entry_id,
                                "Exact historical object unavailable",
                                evidence={"locator": locator}))
            continue
        status = ("NOT_VERIFIED" if expected is None else "PASS" if actual == expected else "FAIL")
        rows.append(Finding("REPLAY", status, entry_id,
                            "Exact historical object content identity",
                            evidence={"locator": locator, "actual_sha256": actual,
                                      "expected_sha256": expected}))
    if not rows:
        raise InputError("No historical locators were declared")
    return rows
