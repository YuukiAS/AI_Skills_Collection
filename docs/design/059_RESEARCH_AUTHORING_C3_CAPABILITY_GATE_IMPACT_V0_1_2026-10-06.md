# 059 Research Authoring C3 Capability Gate 影响说明 v0.1

日期：2026-10-06  
状态：DRAFT_FOR_EXECUTION_READY_CRITIC_REVIEW  
Task：research-authoring--formal-production-authoring

## 1. Gate taxonomy不变

本轮不新增 G5，也不重命名 G1-G4。

继续使用：

~~~text
G1 = 自然入口与 owner boundary
G2 = 科研文档语义组织与长期增量维护
G3 = 真实 manuscript/package
G4 = ChatGPT + Codex 双表面最终生产
~~~

C2：

~~~text
ac501d988f00cb6672fec105ae5fd51a0679cae0
~~~

已经永久 G1 FAIL。

该失败进入 regression bank，不可重跑追认成 PASS。

## 2. C3开发矩阵不是新 Gate

Implementation Plan 中 DEV-01 至 DEV-10 是 C3 freeze 前的风险匹配开发回归。

它解决的是：

> 不再让 final G1 首次发现最基础的入口所有权错误。

它不承担最终发布能力证明。

因此：

~~~text
DEVELOPMENT_MATRIX_PASS
!=
G1_PASS
!=
RESEARCH_AUTHORING_0.3_COMPLETE
~~~

## 3. G1 impact

C3 final G1必须重新执行，直接绑定同一个 C3。

重点仍是自然入口/owner：

- Research Authoring report;
- Research Authoring manuscript;
- related work / revision;
- standalone formal-PDF handoff;
- neighboring near-miss;
- render-only owner。

C3开发矩阵中的相同/相近场景只能作为已知 regression。

Final G1必须使用冻结后的 final case bank和独立 review，不能复制开发 PASS结论。

## 4. G2 impact

C2 之后已经看过、用于旧 candidate 的 report final evidence全部降为 regression。

C3 pre-final packet必须重新冻结 fresh real report-family task和 pre-frozen Phase 2 scientific delta。

Two-phase contract保持不变：

~~~text
Phase 1 raw evidence -> greenfield report
-> independent Phase1 PASS
-> pre-frozen hidden delta
-> minimal dependency closure update
-> final G2 review
~~~

C3 owner-routing修复不能改变该 rubric。

## 5. G3 impact

旧 MoSAIC、CARE 或其他已经被当前 059 final evaluation实际消费的 manuscript evidence不能跨 candidate拼 PASS。

C3 pre-final需冻结 fresh real manuscript task，保持：

- scientific fidelity;
- venue/project authority;
- real package;
- buildable artifact;
- full Reviewer access.

如果某个旧任务只用于 development regression，则仍只能作为 regression。

## 6. G4 impact

G4仍复用 C3 G2 scientific baseline，不增加第四个科学内容任务。

C3 G4必须：

1. exact-C3 offline wrapper先准备；
2. pre-final Critic PASS；
3. 到 live mutation时请求一次 bounded user authorization；
4. guarded update existing PRIVATE USER skills-only wrapper；
5. ordinary frozen natural ChatGPT request；
6. fresh Chat stage完整执行和独立 review；
7. Chat PASS后才进入 Codex/research-main + renderer；
8. final artifact + renderer QA + Research Authoring scientific QA；
9. independent final G4 review。

第一次历史 G4 FAIL永久保留，只作为 regression。

## 7. Same-final-candidate rule

所有最终 PASS必须绑定：

~~~text
FINAL_CANDIDATE_COMMIT=C3
~~~

不允许：

- C2 G2 + C3 G1;
- C2 G3 + C3 G4;
- development matrix + final Gate拼接;
- wrapper来自与 C3 不同的 Research Authoring/Clear Writing snapshot。

## 8. Pre-final admission

C3只有在完整开发矩阵通过后冻结。

随后 independent Critic先审：

- C2 -> C3 diff;
- source/generated/version parity;
- complete development matrix;
- no test-specific workaround;
- offline wrapper binding.

Critic PASS后，Planner才冻结 fresh C3 final G1-G4 packet。

因此 workflow仍是：

~~~text
implementation
-> development matrix
-> C3 freeze
-> independent development Critic
-> fresh C3 pre-final packet
-> pre-final Critic
-> final G1-G4
~~~

没有新 Gate；中间两个 Critic是 admission/review，不是 capability taxonomy。

## 9. Failure semantics

如果开发矩阵失败：

- 不形成 C3;
- 不消耗 final Gate;
- 不通过改测试提示词追 PASS。

如果 C3 final Gate失败：

- 该 C3 final evidence永久记录真实 FAIL;
- 任何 product repair形成新 candidate;
- 旧 final evidence不得跨 candidate拼接。

## 10. Conclusion

~~~text
ADD_G5=NO
G1_G4_TAXONOMY_CHANGED=NO
C3_DEVELOPMENT_MATRIX=PRE_FINAL_REGRESSION_ONLY
C2_FINAL_EVIDENCE=REGRESSION_ONLY
C3_FINAL_EVIDENCE_MUST_BE_FRESH_AND_SAME_CANDIDATE=YES
~~~
