# Built-in Beamer template freeze

- Template family version: `1.0`
- Shared core: `beamer-core-v1`
- Freeze date: `2026-11-27`
- Status: `FROZEN`

`course-standard/` is the standard blue Beamer template and the default built-in Beamer route. `cuhk/` is selected only when CUHK is explicitly requested.

Both templates use the same shared core for generated text, fonts, role sizes, leading, 8 mm body margins, layout grid, caption alignment, list spacing, formula sizing and table geometry. For the same content, these style metrics and content geometry must remain aligned. A one-line caption is centered; a multi-line caption is left aligned beneath its object.

The CUHK school template retains its own appearance while its styles align with `course-standard`: the original purple palette, title-bar treatment, school logo and school-information footer remain on the applicable pages. Appearance parity with `course-standard` is not required.

Changing any frozen role, geometry, style-alignment rule, default routing rule or template-specific appearance boundary requires a new template-family version and a fresh same-content render/validator review.
