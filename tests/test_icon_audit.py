from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import icon_audit  # noqa: E402


class IconAuditTests(unittest.TestCase):
    def test_active_source_skills_have_icon_coverage(self) -> None:
        self.assertEqual(icon_audit.active_skill_errors(), [])


if __name__ == "__main__":
    unittest.main()
