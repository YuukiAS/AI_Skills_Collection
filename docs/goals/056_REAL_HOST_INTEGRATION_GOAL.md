# 056 Real Host Integration Goal — r1

Historical task: `056_product_delivery_discipline`  
Base execution package: v0.5  
Stage: `REAL_HOST_INTEGRATION_AUTHORIZATION_REVIEW`

This Goal covers only the final pre-release real-host G1 integration gate.

## Frozen identities

AI production candidate:
`33c30bbe0dd528031a23d379905cd00d6b65bc1f`

AI reviewed evidence HEAD:
`b4adf85bafe29b20de2c2fbeb95668150642f5ae`

Bridge candidate:
`96a8ea1b58ebe6f9b7c5c46c43995666251911fe` / 0.8.5

Exact target:
- host `c0824.ll.unc.edu`
- user `aereinh`
- CODEX_HOME `/overflow/htzhu/mingcheng_new/.codex`

Current normal Bridge remains:
- executable `/overflow/htzhu/mingcheng_new/.local/bin/ai-bridge`
- root `/overflow/htzhu/mingcheng_new/GPT_Codex_AI_Bridge_Kit`
- HEAD `cb77b1cc5a1fce097a38066d2db452291e359852`
- version 0.8.2

## Positive outcome

Temporarily apply the exact 0.8.5 candidate Host desired state to this exact real CODEX_HOME using the reviewed candidate source, prove the final live G1 behavior in fresh Default and Plan sessions, record evidence, then restore the exact pre-smoke Host state because permanent 0.8.5 install/release is outside this stage.

PASS requires:
1. exact Host/CODEX_HOME identity unchanged;
2. only Bridge-managed Host surface changed;
3. candidate host validate PASS;
4. Default genuine HUMAN_ONLY => one plain-text question and no dependent execution before answer;
5. explicit reply resumes same Goal once and post-action closure runs;
6. agent-resolvable work does not falsely ask user;
7. Plan-mode native request_user_input remains available/blocking;
8. no unexpected Host/repo/provider/credential scope;
9. pre-smoke Host state safely restored.

Expected temporary delta:
- default_mode_request_user_input true -> false
- 0.8.5 managed Host AGENTS block configured
- Bridge rules reconciled
- unrelated existing config preserved

Recovery uses only the existing candidate backup manifest at:
`/overflow/htzhu/mingcheng_new/.codex/ai-bridge-kit/backups/<UTC timestamp>/manifest.json`

Evidence goes only to:
`results/056_product_delivery_discipline/real_host_smoke/`

This Goal does not authorize release/main integration, permanent candidate installation, product-repo write, paid API/Terra, Persistent Run work, new provider/account/credential purpose, broader execpolicy, arbitrary CODEX_HOME, or production-source repair.

If real smoke reveals a source defect:
`SOURCE_DEFECT_DISCOVERED=YES`
and return Planner/Critic after safe restoration.

Overall 056 remains NOT ACHIEVED until later release/integration closure.
