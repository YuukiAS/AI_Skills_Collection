# Source Notes

This skill generalizes a prior host-local Chinese/math PDF rendering workflow
into a portable Codex skill.

Design constraints:

- Do not assume a fixed path such as a user-specific `render_resources`
  directory.
- Prefer project-local render scripts and resources when present.
- Probe TeX/Pandoc/font availability before selecting a route.
- Treat a produced PDF as incomplete until page count, text extraction, and
  glyph/font sanity checks have been performed when the relevant tools exist.
