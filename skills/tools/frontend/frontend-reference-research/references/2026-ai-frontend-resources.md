# 2026 AI Frontend Resource Intake

Reviewed on 2026-07-13 from the private Notion `AI Resources` database plus public source checks. Keep this as a research note, not as vendored source.

## Sources And Decisions

| Source | Public status | Reusable pattern | Do not copy |
|---|---|---|---|
| Notion: `Codex前端审美补全` | Private workspace page; text and images reviewed through the Notion connector where available | Use external galleries to expand visual vocabulary, compare before/after screenshots, and translate vague words such as "premium" into concrete constraints for layout, type, spacing, motion, and QA | Private screenshots, unpublished Notion images, or creator-specific examples |
| `pulkitxm/claude-directory` | GitHub repo, MIT, archived read-only on 2026-07-08 | Use as a prompt/demo gallery for AI-generated landing pages, hero sections, shaders, design systems, WebGL/Three.js, Framer Motion, GSAP, and Tailwind experiments | Do not import generated code without review; check dependencies, accessibility, responsiveness, and archive freshness |
| Notion: `为什么AI做出来的页面太丑` | Private workspace page; one image was referenced but not committed | Convert "AI-looking" critique into a checklist: image-first references, restrained palette, meaningful hierarchy, type scale discipline, spacing rhythm, contextual brand cues, and motion that serves the task | Do not preserve social-media phrasing as a rule source; rewrite as repository-native criteria |
| Notion: `最佳前端设计 Skill 对比` | Private workspace page | Treat external skill names as benchmark labels only: motion strength, web norms/accessibility, and "less AI-flavored" taste are useful evaluation axes | Do not merge unverified third-party skill text or claim endorsement |
| Notion: `2026最强AI组合之一：Codex + Figma` | Private workspace page; principle-level evidence only | Use as a Figma-to-code handoff reminder: keep Figma inspection and node edits in the official Figma capability, pass explicit frame/node ids, extract tokens/assets deliberately, and verify rendered code against the frame | Do not copy private screenshots or imply this repository replaces official Figma tools |
| `DavidHDev/react-bits` | Public GitHub repo; 130+ animated React components; MIT + Commons Clause; supports shadcn and jsrepo install flows | Use as inspiration or optional project dependency for text effects, animated backgrounds, UI motion, and interaction polish when the project is React and the license is acceptable | Do not add it by default, do not vendor components without license review, and do not use animation that hurts accessibility or task speed |
| `dqev/reicon` | Public GitHub repo; SVG icon library with React/Vue/Svelte/JS packages and Figma workspace; MIT package with upstream icon credits | Consider for icon exploration when lucide or the existing project icon set is insufficient | Do not mix icon styles blindly; verify upstream icon licenses before embedding icons in deliverables |

## Downstream Brief Pattern

When handing work to `frontend-visual-systems` or an implementation agent, include:

- reference names and public URLs;
- access date and license or "private Notion evidence only";
- one sentence on the visual job each reference solves;
- the exact design constraints to test in screenshots;
- forbidden copying notes for private assets, whole pages, icons, and component code.
