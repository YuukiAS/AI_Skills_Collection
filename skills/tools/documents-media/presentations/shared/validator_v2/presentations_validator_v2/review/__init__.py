from ..io import DIGEST, InputError, tagged, unique_ids
from ..schemas import Finding


def coverage(scope, mandatory, candidate_commit):
    """Check structural claims. A scope record does not authenticate its reviewer."""
    target = "review_scope"
    if scope.get("verdict") not in {"PASS", "REVISE", "FAIL", "REVIEW", "NOT_VERIFIED"}:
        raise InputError("Invalid review verdict")
    supplied = {
        key: unique_ids(scope[key])
        for key in ("pages", "components", "requirements", "artifact_hashes")
    }
    for value in supplied["artifact_hashes"]:
        tagged(value, DIGEST, "artifact_hashes")
    unreviewed = unique_ids(scope["unreviewed_requirements"])
    missing = {key: sorted(expected - supplied[key]) for key, expected in mandatory.items()}
    extra = {key: sorted(supplied[key] - expected) for key, expected in mandatory.items()}
    exact_commit = scope.get("candidate_commit") == candidate_commit
    consistent = unreviewed == set(missing["requirements"])
    global_pass = scope["verdict"] == "PASS"
    if (any(extra.values()) or not consistent or not exact_commit
            or (global_pass and any(missing.values()))):
        return Finding("REVIEW_SCOPE", "FAIL", target, "Invalid or stale review coverage",
                       evidence={"missing": missing, "extra": extra,
                                 "candidate_commit_agrees": exact_commit})
    if scope["verdict"] in {"REVISE", "FAIL"}:
        return Finding("REVIEW_SCOPE", "FAIL", target, "Review requires correction")
    if not global_pass:
        return Finding("REVIEW_SCOPE", "NOT_VERIFIED", target,
                       "Exact global review coverage is unresolved", evidence={"missing": missing})
    return Finding("REVIEW_SCOPE", "PASS", target, "Global claim covers the exact review scope")
