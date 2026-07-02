# Citation Cleanup

AI-generated drafts may contain citation handles or placeholder characters that
are not valid Markdown, LaTeX, or bibliography syntax. Common examples include:

- `turn12search3`, `turn4view0`, or similar chat-local source handles.
- Bracketed placeholders such as `[cite: ...]`.
- Private-use Unicode marker characters copied from a chat renderer.
- Broken BibTeX keys created by automated rewrite passes.

## Rules

- Do not invent bibliography entries to satisfy placeholders.
- If the original source list exists, map placeholders to real citations and
  keep the mapping auditable.
- If the original source cannot be recovered, remove only the non-renderable
  placeholder syntax and state that citation resolution remains incomplete.
- Keep real DOI, arXiv, PMID, URL, BibTeX key, and path strings intact.
- For LaTeX documents, prefer valid `\cite{key}` or plain prose over malformed
  citation markup.

## Render-Oriented Cleanup

When a citation token blocks compilation, inspect the generated `.tex` around
the first error. Fix the smallest source span that converts an invalid token
into either a valid citation command or neutral prose. Then rerun the full PDF
QA checklist.
