from __future__ import annotations

import argparse
import json
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import skills  # noqa: E402


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

    def test_research_main_installs_renderer_but_marketplace_research_writing_does_not(self) -> None:
        profile = json.loads((REPO_ROOT / "profiles/research-main.json").read_text(encoding="utf-8"))
        self.assertIn("skills/writing/research/research-authoring-core", profile["skills"])
        self.assertIn("skills/tools/documents-media/render-chinese-math-pdf", profile["skills"])

        data = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        research = next(plugin for plugin in data["plugins"] if plugin["name"] == "research-writing")
        serialized = json.dumps(research)
        self.assertNotIn("skills/tools/documents-media/render-chinese-math-pdf", serialized)

    def test_codex_research_writing_installs_research_authoring_core(self) -> None:
        profile = json.loads((REPO_ROOT / "profiles/codex-research-writing.json").read_text(encoding="utf-8"))
        self.assertIn("skills/writing/research/research-authoring-core", profile["skills"])

    def test_research_writing_uses_core_coordinator_for_document_routes(self) -> None:
        data = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        research = next(plugin for plugin in data["plugins"] if plugin["name"] == "research-writing")
        self.assertEqual(research["version"], "0.3")

        route_by_artifact = {entry["artifact_id"]: entry for entry in research["skills"]}
        for artifact_id in ("report", "paper", "litcite"):
            route = route_by_artifact[artifact_id]
            self.assertEqual(route["type"], "aggregate")
            self.assertEqual(route["routing_mode"], "coordinator-first")
            self.assertEqual(route["coordinator_artifact_id"], "core")
            self.assertIn(
                {"source": "skills/writing/research/research-authoring-core", "artifact_id": "core"},
                route["source_skills"],
            )

    def test_research_authoring_core_defines_document_and_support_boundaries(self) -> None:
        text = read_skill("skills/writing/research/research-authoring-core")
        self.assertIn("document-producing", text)
        self.assertIn("support-only", text)
        self.assertIn("incremental authoring contract", text)
        self.assertIn("minimal dependency closure", text)
        self.assertIn("presentations", text)
        self.assertIn("render-only", text)

    def test_research_reporting_formal_pdf_handoff_fails_closed_without_companion(self) -> None:
        text = read_skill("skills/writing/research/research-reporting")
        self.assertIn("skills/tools/documents-media/render-chinese-math-pdf", text)
        self.assertIn("fail closed", text)
        self.assertIn("markdown-only research authoring requests remain markdown-only", text)
        self.assertIn("formal pdf", text)

    def test_research_writing_report_aggregate_blocks_standalone_pdf_rendering(self) -> None:
        data = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        research = next(plugin for plugin in data["plugins"] if plugin["name"] == "research-writing")
        route_by_artifact = {entry["artifact_id"]: entry for entry in research["skills"]}

        report = route_by_artifact["report"]
        notes = "\n".join(report["workflow_notes"]).lower()

        self.assertEqual(report["routing_mode"], "coordinator-first")
        self.assertEqual(report["coordinator_artifact_id"], "core")
        self.assertIn("standalone or skills-only surfaces", notes)
        self.assertIn("approved renderer companion is absent", notes)
        self.assertIn("stop after stable markdown/latex scientific source", notes)
        self.assertIn("complete downstream production handoff", notes)
        self.assertIn("local/preview/qa compile", notes)
        self.assertIn("xelatex", notes)
        self.assertIn("latexmk", notes)
        self.assertIn("pandoc-to-pdf", notes)
        self.assertIn("pdf creation/open/render", notes)
        self.assertIn("page rasterization", notes)
        self.assertIn("page visual inspection", notes)
        self.assertIn("pdf-derived text/font/page qa", notes)
        self.assertIn("pdftotext", notes)
        self.assertIn("pdfinfo", notes)
        self.assertIn("pdffonts", notes)
        self.assertIn("generic runtime, file, or compute capability is not a substitute", notes)
        self.assertIn("render-chinese-math-pdf", notes)
        self.assertIn("markdown/latex source authoring", notes)
        self.assertIn("source-only semantic/fidelity qa", notes)
        self.assertIn("full codex/downstream renderer handoff remain allowed", notes)
        self.assertIn("layout correctness that requires compile/render stays pending", notes)

        paper_notes = "\n".join(route_by_artifact["paper"]["workflow_notes"]).lower()
        litcite_notes = "\n".join(route_by_artifact["litcite"]["workflow_notes"]).lower()
        self.assertNotIn("pdftotext", paper_notes)
        self.assertNotIn("pdftotext", litcite_notes)
        self.assertNotIn("generic runtime, file, or compute capability", paper_notes)
        self.assertNotIn("generic runtime, file, or compute capability", litcite_notes)

    def test_research_main_agents_notes_route_report_pdf_through_reporting_first(self) -> None:
        profile = json.loads((REPO_ROOT / "profiles/research-main.json").read_text(encoding="utf-8"))
        notes = "\n".join(profile.get("routing_notes", [])).lower()
        self.assertIn("research-reporting", notes)
        self.assertIn("render-chinese-math-pdf", notes)
        self.assertLess(notes.index("research-reporting"), notes.index("render-chinese-math-pdf"))

        with tempfile.TemporaryDirectory() as tmp:
            args = argparse.Namespace(
                profile=["research-main"],
                domain=[],
                category=[],
                skill=[],
                target="repo",
                project=tmp,
                mode="copy",
                dry_run=False,
                json=True,
                write_agents_md=True,
                prune_managed=False,
            )
            skills.install_result(args)
            agents = (Path(tmp) / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("## Profile Routing Notes", agents)
        self.assertIn("first read and apply `research-reporting`", agents)
        self.assertIn("then use `render-chinese-math-pdf`", agents)
        self.assertLess(
            agents.index("first read and apply `research-reporting`"),
            agents.index("then use `render-chinese-math-pdf`"),
        )

    def test_research_writing_aggregate_keeps_internal_paper_boundaries(self) -> None:
        data = json.loads((REPO_ROOT / "scripts/codex_marketplace_config.json").read_text(encoding="utf-8"))
        research = next(plugin for plugin in data["plugins"] if plugin["name"] == "research-writing")
        paper = next(skill for skill in research["skills"] if skill.get("name") == "research-paper-workflow")
        self.assertIn("literature-and-citations", paper["description"])
        self.assertEqual(
            {entry["source"] for entry in paper["source_skills"]},
            {
                "skills/writing/research/research-authoring-core",
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
                "skills/writing/research/research-authoring-core",
                "skills/writing/research/literature-review",
                "skills/writing/research/citation-verification",
                "skills/science/discovery/citation-management",
                "skills/science/discovery/research-lookup",
                "skills/science/discovery/pyzotero",
            },
        )

    def test_scientific_writing_routes_non_prose_work_to_neighbors(self) -> None:
        text = read_skill("skills/writing/research/scientific-writing")
        self.assertIn("research-authoring-core", text)
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

        self.assertIn("research-authoring-core", literature_review)
        self.assertIn("research-authoring-core", research_lookup)
        self.assertIn("research-authoring-core", citation_verification)
        self.assertIn("research-authoring-core", citation_management)

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
