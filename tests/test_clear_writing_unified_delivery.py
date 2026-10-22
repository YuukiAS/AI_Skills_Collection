"""Static ownership/parity contracts, not model-quality acceptance."""

from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_clear_writing_chatgpt_wrapper as builder


class ClearWritingUnifiedDeliveryTests(unittest.TestCase):
    def source(self, route: str) -> str:
        return (ROOT / f"skills/writing/core/{route}/SKILL.md").read_text(encoding="utf-8")

    def test_response_workflow_starts_before_drafting_and_repairs_actual_candidate(self) -> None:
        text = self.source("response-clarity")
        workflow = text.split("## Workflow\n", 1)[1].split("## Red Flags", 1)[0]
        stages = ["Read the latest user question", "Separate the evidence pool",
                  "Arrange reader questions and dependencies", "Generate the complete answer",
                  "Re-read the original question", "Actually repair the complete candidate",
                  "Deliver that revised answer"]
        positions = [workflow.index(stage) for stage in stages]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("original question, not just its first screen", workflow)
        self.assertIn("full proof", workflow)
        self.assertIn("not independent review", workflow)
        self.assertNotIn("Identify the domain owner and the known result.", workflow)

    def test_preserved_depth_and_exact_output_are_not_length_rules(self) -> None:
        text = self.source("response-clarity")
        for marker in ("do not enforce fixed counts", "formulas", "uncertainty",
                       "Do not guess a scientific meaning", "keep the machine content exact",
                       "explicitly requested detailed audit", "not as\nsource consensus"):
            self.assertIn(" ".join(marker.split()), " ".join(text.split()))

    def test_final_delivery_ownership_and_reachable_projection(self) -> None:
        files, receipt = builder.build_payload(ROOT, "0.6")
        relative = "writing-fidelity/references/final-delivery.md"
        path = f"{builder.ROUTE_ROOT}/{relative}"
        source = ROOT / f"skills/writing/core/{relative}"
        self.assertEqual(files[path], source.read_bytes())
        self.assertIn(path, receipt["file_allowlist"])
        self.assertIn("references/final-delivery.md", self.source("writing-fidelity"))
        self.assertIn("../writing-fidelity/references/final-delivery.md", self.source("chinese-prose"))
        self.assertIn("../writing-fidelity/references/final-delivery.md", self.source("scientific-rewrite"))
        self.assertEqual(sum(Path(name).name == "SKILL.md" for name in files), 1)
        self.assertEqual(len(receipt["transforms"]), 2)

    def test_delivery_requires_full_content_review_before_write_and_saved_artifact_review(self) -> None:
        text = (ROOT / "skills/writing/core/writing-fidelity/references/final-delivery.md").read_text()
        for marker in ("Read the complete source", "Generate one complete readable candidate",
                       "actually repair it", "Substantive\nrepairs invalidate",
                       "Never generate a different, unchecked body", "expected source version",
                       "non-overwriting create", "parent matches the bound branch head",
                       "not\na strict concurrent-transaction lock", "Local success is not GitHub success",
                       "read the\nentire saved text as a reader", "matching\nbytes do not make it a final document"):
            self.assertIn(" ".join(marker.split()), " ".join(text.split()))
        for status in ("TARGET_SOURCE_INCOMPLETE", "TARGET_IDENTITY_DRIFT", "ARTIFACT_NOT_WRITTEN",
                       "ARTIFACT_FINALIZATION_UNVERIFIED", "ARTIFACT_FINALIZED"):
            self.assertIn(status, text)

    def test_wrapper_delegates_instead_of_owning_another_editor(self) -> None:
        text = (ROOT / builder.WRAPPER).read_text()
        self.assertIn("references/routes/writing-fidelity/references/final-delivery.md", text)
        self.assertIn("does not maintain a second version", text)
        self.assertNotIn("Separate the evidence pool", text)
        self.assertNotIn("For each authorized GitHub edit:", text)
        self.assertIn("cannot execute the required helper", text)

    def test_heavy_rewrite_remains_full_pipeline_and_uses_shared_delivery_only_afterward(self) -> None:
        text = self.source("scientific-rewrite")
        for stage in ("source anchors", "Meaning Map", "Reader Plan", "REALIZE_MEANING",
                      "assembly", "semantic fidelity audit", "structured targeted repair",
                      "re-verification", "validate-host-stage"):
            self.assertIn(stage, text)
        self.assertIn("do not replace any heavy stage above", text)
        self.assertIn("without reintroducing raw-source drafting", text)


if __name__ == "__main__":
    unittest.main()
