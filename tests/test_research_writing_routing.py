from __future__ import annotations

import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_skill(rel_path: str) -> str:
    return (REPO_ROOT / rel_path / "SKILL.md").read_text(encoding="utf-8").lower()


class ResearchWritingRoutingTests(unittest.TestCase):
    def test_research_writing_marketplace_contract_stays_at_ten_plugins(self) -> None:
        data = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        self.assertEqual(data["marketplacePluginBudget"], 10)
        self.assertEqual(
            [plugin["name"] for plugin in data["plugins"]],
            [
                "workflow-core",
                "ai-skills-core",
                "writing-style",
                "research-writing",
                "presentations",
                "scientific-visualization",
                "web-development",
                "statistical-modeling",
                "bioinformatics",
                "medical-imaging",
            ],
        )

    def test_research_writing_aggregate_keeps_internal_paper_boundaries(self) -> None:
        data = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        research = next(plugin for plugin in data["plugins"] if plugin["name"] == "research-writing")
        paper = next(skill for skill in research["skills"] if skill.get("name") == "research-paper-workflow")
        self.assertIn("literature-and-citations", paper["description"])
        self.assertEqual(
            {entry["source"] for entry in paper["source_skills"]},
            {
                "skills/writing/research/scientific-writing",
                "skills/writing/research/paper-workflow-orchestrator",
                "skills/writing/research/nature-manuscript-workflow",
                "skills/writing/research/latex-paper-authoring",
                "skills/writing/research/venue-templates",
                "skills/writing/research/peer-review",
                "skills/writing/research/scholar-evaluation",
            },
        )

    def test_literature_and_citation_aggregate_keeps_lookup_verify_bibtex_split(self) -> None:
        data = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        research = next(plugin for plugin in data["plugins"] if plugin["name"] == "research-writing")
        litcite = next(skill for skill in research["skills"] if skill.get("name") == "literature-and-citations")
        self.assertIn("citation support checks", litcite["description"])
        self.assertEqual(
            {entry["source"] for entry in litcite["source_skills"]},
            {
                "skills/writing/research/literature-review",
                "skills/writing/research/citation-verification",
                "skills/science/discovery/citation-management",
                "skills/science/discovery/research-lookup",
                "skills/science/discovery/pyzotero",
            },
        )

    def test_scientific_writing_routes_non_prose_work_to_neighbors(self) -> None:
        text = read_skill("skills/writing/research/scientific-writing")
        self.assertIn("paragraph-writing skill", text)
        self.assertIn("whole-paper planning", text)
        self.assertIn("reviewer-risk critique", text)
        self.assertIn("literature discovery", text)
        self.assertIn("citation verification", text)
        self.assertIn("bibtex", text)

    def test_peer_review_and_scholar_evaluation_are_separate(self) -> None:
        peer_review = read_skill("skills/writing/research/peer-review")
        scholar_evaluation = read_skill("skills/writing/research/scholar-evaluation")
        self.assertIn("acceptance-risk", peer_review)
        self.assertIn("ordinary manuscript drafting", peer_review)
        self.assertIn("scholar-evaluation", peer_review)
        self.assertIn("quantitative scores", scholar_evaluation)
        self.assertIn("fixed dimensions", scholar_evaluation)
        self.assertIn("plain request", scholar_evaluation)

    def test_literature_review_research_lookup_and_citation_tools_have_distinct_edges(self) -> None:
        literature_review = read_skill("skills/writing/research/literature-review")
        research_lookup = read_skill("skills/science/discovery/research-lookup")
        citation_verification = read_skill("skills/writing/research/citation-verification")
        citation_management = read_skill("skills/science/discovery/citation-management")

        self.assertIn("single-paper evidence cards", literature_review)
        self.assertIn("fast lookup", literature_review)
        self.assertIn("citation-verification", literature_review)
        self.assertIn("bibtex", literature_review)

        self.assertIn("recent papers", research_lookup)
        self.assertIn("current evidence", research_lookup)
        self.assertIn("systematic reviews", research_lookup)
        self.assertIn("claim-support verdicts", research_lookup)

        self.assertIn("claim support", citation_verification)
        self.assertIn("citation-management", citation_verification)
        self.assertIn("research-lookup", citation_verification)

        self.assertIn("reference-library hygiene", citation_management)
        self.assertIn("claim support", citation_management)
        self.assertIn("literature synthesis", citation_management)
        self.assertIn("zotero operations", citation_management)
        self.assertIn("known papers or identifier-backed records", citation_management)
        self.assertIn("bibliography record resolution", citation_management)
        self.assertIn("exact-record lookup", citation_management)
        self.assertIn("find papers by topic", citation_management)
        self.assertIn("use `research-lookup`", citation_management)
        self.assertNotIn("paper discovery and search", citation_management)
        self.assertNotIn("searching for specific papers on google scholar or pubmed", citation_management)
        self.assertNotIn("search for papers on your topic", citation_management)
        self.assertNotIn("find key papers on your topic", citation_management)
        self.assertNotIn("finding and citing seminal papers", citation_management)


if __name__ == "__main__":
    unittest.main()
