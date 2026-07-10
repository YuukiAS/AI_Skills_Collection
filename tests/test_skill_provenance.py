from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import skills  # noqa: E402


class SkillProvenanceTests(unittest.TestCase):
    def test_external_adapted_requires_source_url_and_ref(self) -> None:
        errors = skills.validate_skill_provenance(
            Path("skills/example/SKILL.md"),
            {
                "provenance": "external-adapted",
                "source_path": ".",
                "source_imported_at": "2026-07-10",
                "source_license": "MIT",
            },
        )
        self.assertTrue(any("source_repo_url" in error for error in errors))
        self.assertTrue(any("source_ref" in error for error in errors))

    def test_external_adapted_rejects_placeholder_url(self) -> None:
        errors = skills.validate_skill_provenance(
            Path("skills/example/SKILL.md"),
            {
                "provenance": "external-adapted",
                "source_repo_url": "unknown URL",
                "source_path": ".",
                "source_ref": "abc123",
                "source_imported_at": "2026-07-10",
                "source_license": "MIT",
            },
        )
        self.assertTrue(any("placeholder" in error or "HTTP/HTTPS" in error for error in errors))

    def test_unknown_history_is_allowed_without_source_fields(self) -> None:
        errors = skills.validate_skill_provenance(Path("skills/old/SKILL.md"), {"provenance": "unknown"})
        self.assertEqual(errors, [])

    def test_user_authored_does_not_require_external_url(self) -> None:
        errors = skills.validate_skill_provenance(Path("skills/local/SKILL.md"), {"provenance": "user-authored"})
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
