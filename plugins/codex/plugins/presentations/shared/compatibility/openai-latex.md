# Official LaTeX Compatibility

This repository supplies presentation intent, Beamer template choice, content structure, and QA criteria.

The official LaTeX capability should handle:

- `.tex` file implementation;
- macro/package troubleshooting;
- compilation and log repair;
- PDF generation.

Ordinary PPTX requests should not trigger LaTeX only because slides contain equations.

Presentation-specific requirements:

- Academic presentation compilation must first use the locally installed `render-chinese-math-pdf` skill. Read that skill and run its environment probe before choosing a compiler; do not guess a server-local `xelatex`, `lualatex`, or TeX Live path.
- For <private repository> work on this workstation, keep `/home/yuukias/render_resources/chinese_math_pdf` as the known local render-resource location when the probe reports it. If the probe cannot find resources, TinyTeX, packages, fonts, or PDF QA tools, report the exact missing item and wait for user installation approval instead of falling back to retired server-only paths.
- Build the canonical CUHK and course-standard Beamer templates with XeLaTeX after probing. The shared core uses `fontspec`, `xeCJK` and `unicode-math`.
- If `render-chinese-math-pdf` is not installed in the active server profile, stop and report that missing local skill instead of silently falling back to a hand-written compiler search.
- Both skins require the fixed families declared by `shared/font-policy.md`. A missing file must be repaired in the renderer's resource bundle.
