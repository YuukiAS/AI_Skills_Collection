"""Schema helpers for the validator pilot.

The core uses plain dictionaries at repository boundaries so downstream course
adapters can write JSONL evidence without importing a serialization framework.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal


Verdict = Literal["PASS", "REVISE", "BLOCKED"]
CheckStatus = Literal["PASS", "REVISE", "N/A", "BLOCKED"]


@dataclass(frozen=True)
class DetectorSpec:
    detector_id: str
    implementation_status: Literal["IMPLEMENTED", "PLANNED"]
    observable_inputs: list[str]
    finding_class: str
    positive_control: str
    negative_control: str
    production_function: str
    reuse_classification: Literal["REUSABLE_CANDIDATE", "STAT5060_SPECIFIC"]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class CheckResult:
    check_id: str
    status: CheckStatus
    finding_class: str | None = None
    evidence: str = ""
    locations: list[dict[str, Any]] = field(default_factory=list)
    positive_evidence: list[str] = field(default_factory=list)
    negative_evidence: list[str] = field(default_factory=list)
    not_applicable_reason: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def check_pass(check_id: str, evidence: str, *, positive: list[str] | None = None) -> CheckResult:
    return CheckResult(check_id=check_id, status="PASS", evidence=evidence, positive_evidence=positive or [evidence])


def check_revise(
    check_id: str,
    finding_class: str,
    evidence: str,
    *,
    locations: list[dict[str, Any]] | None = None,
    negative: list[str] | None = None,
) -> CheckResult:
    return CheckResult(
        check_id=check_id,
        status="REVISE",
        finding_class=finding_class,
        evidence=evidence,
        locations=locations or [],
        negative_evidence=negative or [evidence],
    )


def check_na(check_id: str, reason: str) -> CheckResult:
    return CheckResult(check_id=check_id, status="N/A", not_applicable_reason=reason, evidence=reason)
