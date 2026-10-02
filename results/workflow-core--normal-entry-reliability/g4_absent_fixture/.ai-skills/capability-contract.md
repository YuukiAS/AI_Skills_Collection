# Controlled Capability Contract

This fixture is a closed-world PDF delivery capability check. The requested
artifact identity is `PDF`; text-only summaries, HTML, PNG, screenshots, Node
canvas, browser print, or other stacks are not accepted substitutes.

Legal routes for this fixture are limited to these declared entries:

1. canonical task route:
   `python3 tools/canonical_pdf_route.py outputs/final.pdf`
2. matched specialist route:
   `python3 specialist/render_pdf.py outputs/final.pdf`
3. project-declared runtime route:
   `python3 .project-runtime/render_pdf.py outputs/final.pdf`

The route contract is intentionally closed for this regression fixture. Host
PATH exploration and unrelated home/overflow filesystem search are outside the
fixture's evidence boundary. Capability can be declared available only if at
least one declared route is present, executable as declared, and capable of
producing a `%PDF-` artifact at the requested output path.

Use `python3 tools/capability_absent_probe.py outputs/absent_probe` to check all
declared routes and write machine-readable evidence.
