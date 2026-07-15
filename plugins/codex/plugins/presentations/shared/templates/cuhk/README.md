# CUHK Default Template

Local source files:

- `C:\Users\humc2\Downloads\CUHK Template.zip`
- `C:\Users\humc2\Downloads\CUHK Template.pdf`

The full zip contents are committed under `beamer/source/` so the template can be reproduced without returning to the Downloads folder. The committed source includes `main.tex`, `.vscode/settings.json`, `styles/`, `assets/`, `images/`, and `bibliography.bib`.

`beamer/source/` is the canonical CUHK Beamer template. Use it for academic talks and exact template reproduction.

`design-tokens.json`, `beamer/main.tex`, and `pptx/build_reference_deck.py` are derived scaffolds for non-exact workflows only. Do not use them when the user asks for CUHK template fidelity or when generating the default academic/research deck.

Title slide lock:

- Preserve the first/title slide layout from `beamer/source/` exactly.
- Only replace metadata/content fields such as title, subtitle, author, institute, date, course label, supervisor, and ID number.
- Do not change title-slide geometry, background, logo placement, theme files, spacing, or decorative elements unless the user explicitly asks to modify the CUHK template itself.

Font requirements:

- The source theme uses `\setmainfont{Times New Roman}`, `\setsansfont{Times New Roman}`, and `\setmonofont{Times New Roman}`.
- A build host must provide Times New Roman Regular, Bold, Italic, and Bold Italic. On Windows these are usually `C:\Windows\Fonts\times.ttf`, `C:\Windows\Fonts\timesbd.ttf`, `C:\Windows\Fonts\timesi.ttf`, and `C:\Windows\Fonts\timesbi.ttf`.
- No font files were present in the CUHK zip. Do not commit Times New Roman files to this repo unless redistribution rights are explicitly confirmed.
- For private server deployment, install the fonts on the server or ship them as a private, non-versioned deployment asset and update the server font cache before compiling.
