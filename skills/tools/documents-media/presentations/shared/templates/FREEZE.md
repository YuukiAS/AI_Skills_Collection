# Built-in Beamer template freeze

- Template family version: `1.0`
- Shared core: `beamer-core-v1`
- Freeze date: `2026-11-27`
- Status: `FROZEN`

`course-standard/` is the standard blue Beamer template and the default built-in Beamer route. `cuhk/` is selected only when CUHK is explicitly requested.

Both templates use the same shared core for generated text, fonts, role sizes, leading, title bar, 8 mm body margins, captions, lists, formulas, tables, footer and navigation. Body pages must remain visually and geometrically identical for the same content. A one-line caption is centered; a multi-line caption is left aligned beneath its object.

The CUHK template may differ only on the first page through approved school artwork and school identity text. It must not add a school palette, logo, credit or other school-specific chrome to body pages.

Changing any frozen role, geometry, body-page parity rule, default routing rule or permitted title-page difference requires a new template-family version and a fresh same-content render/validator review.
