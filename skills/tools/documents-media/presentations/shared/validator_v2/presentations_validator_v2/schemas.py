from dataclasses import asdict, dataclass, field
from typing import Any, Literal

Check = Literal["PASS", "FAIL", "REVIEW", "NOT_VERIFIED"]


@dataclass(frozen=True)
class Finding:
    detector: str
    status: Check
    target: str
    message: str
    mandatory: bool = True
    evidence: dict[str, Any] = field(default_factory=dict)


def report(rows: list[Finding], **identity: Any) -> dict:
    if not rows:
        rows = [Finding("INPUT", "NOT_VERIFIED", "artifact", "No checks ran")]
    mandatory = {row.status for row in rows if row.mandatory}
    if "FAIL" in mandatory:
        verdict = "DETERMINISTIC_FAIL"
    elif "NOT_VERIFIED" in mandatory:
        verdict = "DETERMINISTIC_INCOMPLETE"
    elif any(row.status == "REVIEW" for row in rows):
        verdict = "DETERMINISTIC_NO_FAIL_REVIEW_REQUIRED"
    else:
        verdict = "DETERMINISTIC_PASS"
    return {"state": verdict, **identity, "rows": [asdict(row) for row in rows]}
