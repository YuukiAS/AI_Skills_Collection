# render-chinese-math-pdf — Long-Term TODO

This inbox keeps unresolved, reusable failures for the standalone Chinese Math PDF skill. Released fixes remain in release history rather than this active TODO.

## Open candidates

### Formal PDFs from upstream authoring routes need an explicit renderer handoff
status: NEW
tracking: UNASSIGNED
problem: An upstream authoring plugin can finish the document semantics without reliably handing formal PDF production to the canonical renderer. The route should preserve Markdown-only requests, use the renderer when a formal PDF is requested and available, and fail clearly when the required renderer is absent.
