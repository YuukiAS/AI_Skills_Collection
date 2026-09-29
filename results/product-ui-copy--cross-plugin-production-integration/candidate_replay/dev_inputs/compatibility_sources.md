# Product UI Copy Compatibility Source Bundle

Task key: `product-ui-copy--cross-plugin-production-integration`

These snippets are repo-safe read-only inputs for development replay. They are
not consumer repo modifications.

## Source Locators

- Lucerna: `/home/yuukias/code/Lucerna @ 3b7b349d6bc0460acccf98a4b607fddc40336eda`
- Mica for ChatGPT: `/tmp/product-ui-copy-mica-readonly @ e49416f874f633aedc7521734ee5b0f441aae970`
- SeminarArc: `/home/yuukias/code/SeminarArc @ b51f6909ff31fdeb0089be0e4c7a46f55107ee9f`
- Rendered fixture: `results/product-ui-copy--cross-plugin-production-integration/rendered_acceptance/product-ui-copy-fixture.html`

## Generic Product UI Copy Fixture

Surface: browser extension settings and mobile destructive action.

Visible copy examples:

- "同步只在你确认后开始"
- "检查可同步项目"
- "先保持本机使用"
- "检查结果只用于本次同步预览。你可以在确认前移除任何项目。"
- "是否删除这条公开回复？"
- "删除后，其他人将无法再看到这条回复。我们会保留系统记录，用于安全审计。"
- "已保存"
- "你的更改已同步到这台设备。"

Protected meaning:

- Upload starts only after user confirmation.
- The local inspection result is only a preview before confirmation.
- Deleting a public reply removes public visibility but keeps audit records.
- Already clear saved-state copy may remain unchanged.

## Lucerna Desktop / Native-WebView Case

Lucerna is a Tauri desktop utility with macOS menu-bar and Windows system-tray
entry points. Its compact panel is the main product surface.

Relevant source snippets from `docs/PLATFORM_UI.md` and `docs/PRODUCT.md`:

```text
macOS menu bar
Lucerna icon     ↓ 3.2M ↑ 240K
click -> compact panel

Windows:
System tray icon -> click -> Lucerna compact panel

Compact panel purpose:
Resources
Codex                54% left
OpenAI API           $24.60 left
GitHub Actions       1,327 min
VPS bandwidth        20% left

Health
UNC Bridge           Healthy
Longleaf             Healthy

Network · macOS
↓ 3.2 MB/s           ↑ 240 KB/s
Today 18.4 GB
```

Product copy constraints:

- Do not imply widget-level real-time behavior for WidgetKit snapshots.
- Do not claim a health check is full business health when only TCP or partial
  availability is verified.
- Keep desktop/WebView evidence boundaries explicit.

## Mica Browser Extension Popup Case

Mica is a browser extension for ChatGPT long-thread usability and diagnostics.

Relevant source snippets from `extension/popup/popup.ts`,
`extension/popup/popup.css`, `dist/mica-dev/manifest.json`, and `README.md`:

```text
manifest name: Mica for ChatGPT
default_popup: popup/index.html
host permissions: https://chatgpt.com/* and https://chat.openai.com/*

status names:
Active
Native virtualization
Native only
Degraded
Disabled

popup actions:
Start diagnostics
Stop diagnostics
Copy report
Reset
Run composer check
Stop composer check
Copy composer report

status text examples:
Open a ChatGPT conversation.
No diagnostics report available.
Report copied to clipboard.
Clipboard copy failed.
Open a supported ChatGPT page.
Recording · N samples · N events
Captured · stale clear yes/no · send classification
```

Product copy constraints:

- The extension must not suggest that diagnostics upload chat content.
- It may say diagnostics are local and privacy-safe when the source supports
  that.
- Unknown authorization, deletion, payment, or tool-permission prompts must not
  be auto-dismissed.

## SeminarArc Compose UI Positive Case

SeminarArc is an Android/Compose seminar capture and reconstruction app.

Relevant source snippets from `design/UI_SPEC.md` and `design/USER_FLOW.md`:

```text
Seminar list:
Create seminar
Open seminar
All / Draft / Completed / Favorites

Live capture:
Mark Moment
Capture Slide
End Seminar
Add Question
Quick Note
Pause / Resume recording

Research Reconstruction:
Select photos or key slides
Run local OCR
Edit OCR text
Mark / unmark key slide
Search OCR text
Retry or cancel processing task

States:
PENDING
RUNNING
SUCCEEDED
FAILED
CANCELLED
```

Product copy constraints:

- UI work should respect the project-local Android/Compose implementation
  owner; generic product-interface coordination must not become platform code
  authority.
- Deleting a seminar requires a serious confirmation that names the seminar and
  lists deleted asset kinds.
- Future cloud, AI summary, transcription, Notion, formula OCR, and reference
  lookup capabilities must not appear enabled before they exist.

## SeminarArc Room / WorkManager Negative Case

Relevant source paths:

```text
app/src/main/java/com/yuukias/seminararc/data/local/AppDatabase.kt
app/src/main/java/com/yuukias/seminararc/data/local/dao/ReconstructionDao.kt
app/src/main/java/com/yuukias/seminararc/media/processing/ProcessingWorker.kt
app/src/main/java/com/yuukias/seminararc/media/processing/WorkManagerProcessingWorkScheduler.kt
app/src/main/java/com/yuukias/seminararc/media/clip/WorkManagerClipWorkScheduler.kt
```

Negative request:

```text
Migrate processing retry semantics across Room and WorkManager while keeping UI
unchanged.
```

Expected boundary:

- This is data/background processing work when UI is explicitly unchanged.
- It should not activate product-interface design or copy work.
