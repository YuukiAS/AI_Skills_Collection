import unittest

from scripts.audit_skill_runtime_text import audit


class SkillRuntimeTextAuditTests(unittest.TestCase):
    def test_runtime_text_audit_passes(self):
        self.assertEqual(audit(), [])


if __name__ == "__main__":
    unittest.main()
