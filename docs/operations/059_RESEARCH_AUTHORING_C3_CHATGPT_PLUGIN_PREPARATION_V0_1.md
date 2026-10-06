# 059 Research Authoring C3 ChatGPT Plugin 提前准备方案 v0.1

日期：2026-10-06  
状态：OFFLINE_PREPARATION_ONLY / NO_LIVE_MUTATION  
Task：research-authoring--formal-production-authoring

## 1. Purpose

C3开发矩阵通过后，在新的 pre-final packet冻结以前就准备好 exact-C3 ChatGPT skills-only wrapper。

目标是让后续 G4 只剩：

~~~text
user bounded authorization
-> guarded live update
-> fresh ChatGPT G4 run
~~~

而不是临时再组包。

## 2. Canonical payload

Wrapper name保持：

research-authoring

Wrapper composition必须来自 exact：

~~~text
C3_FINAL_CANDIDATE_COMMIT=<C3>
~~~

Research Authoring payload：

plugins/codex/plugins/research-writing/** @ C3

Clear Writing support from the same C3：

- skills/writing/core/writing-fidelity/**
- skills/writing/core/chinese-prose/**
- skills/writing/core/scientific-prose/**

不得从不同 commit混包。

## 3. Wrapper identity

Future live target：

~~~text
scope=USER
discoverability=PRIVATE
skills-only=YES
MCP=NO
connector=NO
renderer-runtime=NO
database/watcher/state=NO
~~~

The wrapper distributes authoring instructions only.

It does not bundle render-chinese-math-pdf runtime. This is necessary to preserve the standalone Research Authoring boundary.

## 4. Offline files

After C3 freeze, prepare under：

private/exports/research-authoring--formal-production-authoring/c3_wrapper/

At least：

~~~text
WRAPPER_COMPOSITION.md
FILE_HASH_MANIFEST.json
LIVE_UPDATE_INPUT_TEMPLATE.md
research-authoring-wrapper-<distribution-version>-c3-<shortsha>.tar.gz
wrapper_candidate/
~~~

FILE_HASH_MANIFEST must include every archived file：

- relative path;
- SHA256;
- size;
- canonical source locator;
- source commit.

The archive hash/size must also be recorded.

## 5. Distribution version

Current historical live wrapper identity must not be assumed at mutation time.

Planning expectation：

~~~text
if current live version remains 0.3.0:
    expected next distribution version = 0.3.1
~~~

Before actual mutation：

1. re-read Plugin Creator inventory;
2. identify exact existing research-authoring personal Plugin;
3. re-read current release/version;
4. if identity/version differs from expected, STOP and reconcile;
5. compute one compatible next patch;
6. use current release id as guarded-update concurrency token.

The wrapper distribution version is independent from canonical central plugin version：

~~~text
research-writing = 0.3 @ C3
wrapper distribution ~= 0.3.1 if current live remains 0.3.0
~~~

## 6. Live update input template

Prepare, but do not execute, exact future mutation input containing：

- target plugin id placeholder resolved from fresh inventory;
- expected current release id placeholder;
- wrapper version;
- full file overlay/archive identity;
- PRIVATE / USER / skills-only constraints;
- no MCP/connector;
- no renderer runtime;
- exact C3 commit;
- complete manifest hash.

If Plugin Creator overlay semantics cannot safely remove stale files from the existing live wrapper, STOP before mutation and return Planner/Critic. Do not accept a mixed old/new payload.

## 7. Future user authorization

No live mutation is authorized by this Plan or by C3 development PASS.

At the G4 boundary ask once：

> 批准把现有 PRIVATE / USER-scope skills-only research-authoring wrapper guarded-update 到 exact C3 离线包，仅用于当前 059 G4 正常入口验收；不添加 MCP/connector/renderer runtime，不公开发布，不修改其他 Plugin。

Only after that explicit authorization may Plugin Creator be called.

## 8. Acceptance before live mutation

The offline wrapper must prove：

- every Research Authoring file originates from exact C3 generated plugin;
- Clear Writing support originates from exact C3;
- no renderer runtime included;
- no old C/C2 report aggregate remains;
- archive manifest complete;
- archive hash stable;
- candidate owner/routing metadata included.

This is packaging evidence, not G4 PASS.

## 9. G4 execution boundary

After live update：

- use the frozen ordinary natural request;
- do not add command blacklist;
- complete fresh Chat stage;
- independently review Chat stage;
- only after Chat PASS hand to Codex/research-main;
- renderer then produces PDF;
- post-render Research Authoring scientific QA runs.

If Chat stage renders PDF itself, G4 FAIL.

## 10. No mutation in current package

~~~text
OFFLINE_WRAPPER_PREP_ALLOWED_AFTER_C3=YES
LIVE_PLUGIN_MUTATION_AUTHORIZED=NO
PLUGIN_CREATOR_CALL_NOW=NO
~~~
