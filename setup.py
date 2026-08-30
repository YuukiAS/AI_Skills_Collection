from __future__ import annotations

from pathlib import Path

from setuptools import find_packages, setup


ROOT = Path(__file__).resolve().parent
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()


setup(
    name="ai-skills-collection-cli",
    version=VERSION,
    description="Local command wrapper for AI_Skills_Collection.",
    packages=find_packages(include=["ai_skills_cli", "ai_skills_cli.*"]),
    python_requires=">=3.10",
    entry_points={"console_scripts": ["ai-skills=ai_skills_cli.cli:main"]},
    extras_require={"interactive": ["InquirerPy>=0.3"]},
)
