# C3 G1 frozen case bank

Candidate: `9e88d7eda1749c09bac0ed97562909a90810ccdb`

G1 validates the ChatGPT Web / skills-only wrapper Research Authoring normal entry and near-miss boundary. It does **not** run Codex raw authoring owner competition.

## Natural positives

1. Advisor research update:
   - Natural request: "帮我把这些实验结果整理成给导师看的正式研究更新，保留证据边界和下一步。"
   - Expected route: Research Authoring report-family normal entry.
   - Expected output: stable Markdown/LaTeX source plus complete Codex production handoff.

2. Manuscript section:
   - Natural request: "根据这些方法和结果，起草一段双盲论文方法/实验部分，并准备后续 Codex production handoff。"
   - Expected route: Research Authoring core -> paper/manuscript route.
   - Expected output: source/package plus handoff, not self-rendered PDF.

3. Related-work document:
   - Natural request: "把这些论文卡片整理成 related work 小节，说明每类方法和我们工作的关系。"
   - Expected route: Research Authoring document-producing literature route.

4. Existing research document revision:
   - Natural request: "这份研究更新已经有一版草稿，请根据新增结果和导师反馈做最小必要修订，保留已经成立的结论和证据边界。"
   - Expected route: Research Authoring incremental document revision.
   - Expected output: revised stable source plus complete Codex production handoff when a final artifact is requested.

## Near misses

1. Citation verification only.
2. Paper lookup / BibTeX cleanup only.
3. Content-preserving one-sentence polish.
4. README / email writing that is not a research document.
5. Render-only finalized Markdown/LaTeX.
6. PPT / Beamer / slide deck request.
7. Ordinary research Q&A without document production.

## Pass contract

```text
CHATGPT_RESEARCH_AUTHORING_NORMAL_ENTRY=PASS_REQUIRED
NEAR_MISS_BOUNDARY=PASS_REQUIRED
RAW_CODEX_AUTHORING_OWNER_COMPETITION=NOT_IN_G1
FINAL_GATES_NOT_STARTED_IN_PACKET=YES
```
