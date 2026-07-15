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
- For CUHK Beamer output, prefer `xelatex` after probing because the template uses `fontspec` and Times New Roman. Use `lualatex` only if the probe and a test compile show the same template works.
- If `render-chinese-math-pdf` is not installed in the active server profile, stop and report that missing local skill instead of silently falling back to a hand-written compiler search.
- The CUHK template requires Times New Roman Regular, Bold, Italic, and Bold Italic. Do not commit these proprietary font files to the public repo; install them on the server or provide them as a private deployment asset before compiling.
