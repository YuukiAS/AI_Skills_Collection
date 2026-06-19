# research-communication

Active skills: 6

## Install

Complete domain install:

```bash
ai-skills install --target repo --domain research-communication --mode symlink --write-agents-md
```

Install a few skills precisely:

```bash
ai-skills install --target repo --skill science/communication/latex-posters --skill science/communication/paper-2-web --skill science/communication/pptx-posters --mode symlink --write-agents-md
```

Complete domain installs are supported. If an audit reports high description length or many active skills, treat it as a context-budget warning, not an installation error.

## Common Uses

- Install the whole domain for a project where most tasks are in this area.
- Use precise skill selectors when only one tool or workflow is needed.
- Combine with profiles when a project needs a curated cross-domain set.

## Skills

- `latex-posters` (`skills/science/communication/latex-posters`): Create professional research posters in LaTeX using beamerposter, tikzposter, or baposter. Support for conference presentations, academic posters, and scientific communication. Includes layout design, color schemes, multi-column formats, figure integration, and poster-specific best practices for visual communication.
- `paper-2-web` (`skills/science/communication/paper-2-web`): This skill should be used when converting academic papers into promotional and presentation formats including interactive websites (Paper2Web), presentation videos (Paper2Video), and conference posters (Paper2Poster).
- `pptx-posters` (`skills/science/communication/pptx-posters`): Create research posters using HTML/CSS that can be exported to PDF or PPTX. Use this skill ONLY when the user explicitly requests PowerPoint/PPTX poster format. For standard research posters, use latex-posters instead. This skill provides modern web-based poster design with responsive layouts and easy visual integration.
- `scientific-schematics` (`skills/science/communication/scientific-schematics`): Create publication-quality scientific diagrams using Nano Banana 2 AI with smart iterative refinement. Uses Gemini 3.1 Pro Preview for quality review.
- `scientific-slides` (`skills/science/communication/scientific-slides`): Build slide decks and presentations for research talks. Use this for making PowerPoint slides, conference presentations, seminar talks, research presentations, thesis defense slides, or any scientific talk. Provides slide structure, design templates, timing guidance, and visual validation. Works with PowerPoint and LaTeX Beamer.
- `scientific-visualization` (`skills/science/communication/scientific-visualization`): Meta-skill for publication-ready figures. Use when creating journal submission figures requiring multi-panel layouts, significance annotations, error bars, colorblind-safe palettes, and specific journal formatting (Nature, Science, Cell).

## Main References

- No domain references discovered yet. Add `references/source-notes.md`, checklists, or overview notes when the skill carries long-lived domain knowledge.
