from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import palette_library  # noqa: E402


class PaletteWorkflowTests(unittest.TestCase):
    def test_notion_candidate_count_and_no_local_paths(self) -> None:
        candidates = json.loads((REPO_ROOT / "palette/notion-palette-candidates.json").read_text(encoding="utf-8"))
        self.assertEqual(len(candidates["candidates"]), 50)
        notion_text = (REPO_ROOT / "palette/notion-image-palettes.json").read_text(encoding="utf-8")
        self.assertNotIn("C:\\Users\\", notion_text)
        self.assertNotIn('"mtime"', notion_text)

    def test_default_recommendation_excludes_notion_candidates(self) -> None:
        palettes = palette_library.recommend_palettes(figure_type="line")
        self.assertTrue(palettes)
        self.assertFalse(any(str(palette["id"]).startswith("notion_") for palette in palettes))

    def test_explicit_notion_recommendation_finds_candidates(self) -> None:
        palettes = palette_library.recommend_palettes(
            figure_type="schematic",
            paper_venue="AAAI",
            style_source="notion",
            include_experimental=True,
        )
        self.assertEqual([palette["id"] for palette in palettes], ["notion_aaai_1", "notion_aaai_2", "notion_aaai_3"])

    def test_contextual_discovery_finds_notion_without_style_source(self) -> None:
        result = palette_library.discover_context(figure_type="schematic", paper_venue="AAAI")
        self.assertTrue(result["safe_palettes"])
        self.assertFalse(any(str(palette["id"]).startswith("notion_") for palette in result["safe_palettes"]))
        self.assertEqual([candidate["id"] for candidate in result["experimental_candidates"]], ["notion_aaai_1", "notion_aaai_2", "notion_aaai_3"])
        self.assertTrue(any(preset["id"] == "aaai_schematic_clean" for preset in result["contextual_presets"]))

    def test_contextual_discovery_supports_representative_scenarios(self) -> None:
        cases = [
            ("CVPR", "Gaussian splatting", "notion_cvpr25_1"),
            ("Nature", "UMAP", "notion_nature_inspiration_1"),
            ("ICML", "line chart", "example_icml_clean_1"),
            (None, "histogram", "example_python_bar_distribution_1"),
        ]
        for venue, figure_type, expected in cases:
            result = palette_library.discover_context(figure_type=figure_type, paper_venue=venue, limit_per_page=3)
            serialized = json.dumps(result)
            self.assertIn(expected, serialized)
            page_counts: dict[str, int] = {}
            for candidate in [*result["experimental_candidates"], *result["guidance_only"]]:
                group = candidate.get("page_group_id")
                page_counts[group] = page_counts.get(group, 0) + 1
            self.assertTrue(all(count <= 3 for count in page_counts.values()))

    def test_ambiguous_page_alias_rejected(self) -> None:
        with self.assertRaisesRegex(KeyError, "Ambiguous Notion page alias"):
            palette_library.get_palette("notion_aaai", source="all")

    def test_snippet_gate(self) -> None:
        allowed = palette_library.get_palette("notion_aaai_1", source="all")
        with self.assertRaisesRegex(ValueError, "requires --allow-experimental"):
            palette_library.palette_to_snippet(allowed, "matplotlib")
        snippet = palette_library.palette_to_snippet(allowed, "matplotlib", allow_experimental=True)
        self.assertIn("Experimental Notion-derived palette", snippet)

        blocked = palette_library.get_palette("notion_icml_clean_1", source="all")
        with self.assertRaisesRegex(ValueError, "not eligible"):
            palette_library.palette_to_snippet(blocked, "matplotlib", allow_experimental=True)

    def test_preset_and_example_references_resolve(self) -> None:
        preset = palette_library.get_preset("icml_clean_layout")
        self.assertEqual(preset["example_refs"], ["example_icml_clean_3", "example_icml_clean_2", "example_icml_clean_1"])
        self.assertEqual(preset["discovery_mode"], "contextual_default")
        examples = palette_library.find_examples(figure_type="histogram", style_source="notion", page="python_bar_distribution")
        self.assertEqual(len(examples), 18)
        limited = palette_library.find_examples(figure_type="histogram", style_source="notion", page="python_bar_distribution", limit_per_page=3)
        self.assertEqual(len(limited), 3)

    def test_cli_smoke_for_required_commands(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/palette.py", "list", "--tier", "image_derived_transcribed", "--review-status", "unreviewed"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("notion_aaai_1", result.stdout)

        failed = subprocess.run(
            [sys.executable, "scripts/palette.py", "snippet", "notion_aaai_1", "--target", "matplotlib"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(failed.returncode, 0)
        self.assertIn("requires --allow-experimental", failed.stderr)

        discovered = subprocess.run(
            [sys.executable, "scripts/palette.py", "discover", "--figure-type", "schematic", "--paper-venue", "AAAI", "--explain"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("EXPERIMENTAL CANDIDATES", discovered.stdout)
        self.assertIn("notion_aaai_1", discovered.stdout)

        guidance = subprocess.run(
            [sys.executable, "scripts/palette.py", "guidance", "notion_icml_clean_1", "--target", "matplotlib"],
            cwd=REPO_ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Style guidance", guidance.stdout)

    def test_gallery_contains_candidate_ids(self) -> None:
        subprocess.run([sys.executable, "scripts/generate_palette_gallery.py"], cwd=REPO_ROOT, check=True)
        gallery = (REPO_ROOT / "palette/gallery.html").read_text(encoding="utf-8")
        index = json.loads((REPO_ROOT / "palette/gallery-index.json").read_text(encoding="utf-8"))
        self.assertIn("notion_aaai_1", gallery)
        self.assertIn("Scientific Figure Palette Discovery", gallery)
        index_ids = {item["id"] for item in index["items"]}
        self.assertIn("notion_aaai_1", index_ids)
        self.assertIn("example_python_bar_distribution_1", index_ids)

    def test_plugin_shared_payload_matches_source_files(self) -> None:
        shared_root = REPO_ROOT / "plugins/codex/plugins/scientific-visualization/shared"
        for relative in [
            "palette/notion-palette-candidates.json",
            "palette/figure-example-registry.json",
            "palette/publication-figure-presets.json",
            "scripts/palette.py",
            "scripts/palette_library.py",
        ]:
            source = (REPO_ROOT / relative).read_text(encoding="utf-8")
            generated = (shared_root / relative).read_text(encoding="utf-8")
            self.assertEqual(source, generated)


if __name__ == "__main__":
    unittest.main()
