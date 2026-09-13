import importlib.util,json,hashlib,pathlib
p=pathlib.Path('outputs/stages')
spec=importlib.util.spec_from_file_location('support','/overflow/htzhu/mingcheng_new/.codex-global/plugins/cache/ai-skills-candidate-053/writing-style/0.2+codex.local-20260913T044041Z-2704773/skills/scientific-rewrite/scripts/rewrite_support.py'); s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
source=pathlib.Path('inputs/01-source.wiki').read_text()
def save(name,obj): (p/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
prompt='''请把随附的中文维基 raw wikitext《混淆矩阵》片段整理成自然、连贯、可导出 PDF 的简体中文技术说明。

要求：

- 保留混淆矩阵/误差矩阵、实际类别、预测类别、猫狗示例、假阳性、假阴性、真阳性、真阴性、准确度、敏感性、F1 score、约登指数等关键概念；
- 保留 13 个动物、8 只猫、5 只狗、5/3/2/3、95/5、95%、100%、0%、97.4%、J=0 等数字和公式关系；
- 将 wikitext 表格整理成可读 Markdown 表格或等价的清晰结构；
- 清理 `{{...}}`、`<ref>`、`[[...]]`、分类、语言模板、归档链接等来源包装；
- 普通正文用简体中文；必要英文术语可以保留。

Input files available in this workspace:
- inputs/01-source.wiki

Write all outputs under: outputs'''
(p/'prompt.md').write_text(prompt)
save('route_selection.json',dict(schema=s.ROUTE_SELECTION_SCHEMA,selector_owner='writing-style',selected_route='scientific-rewrite',forced_route=False,ordinary_user_prompt=True,prompt_sha256=s.sha256_text(prompt),source_sha256=s.sha256_text(source),prompt_internal_terms=[],selection_basis='Host semantic selection: source-bound technical restructuring with explicit numerical and formula preservation.'))
anchors=s.split_source_anchors(source)
for a in anchors: print(a['source_anchor_id'],source[a['start']:a['end']][:45].replace('\n',' '))
meanings=[]
def m(i,ids,meaning,exact=[]): meanings.append(dict(meaning_id=i,kind='technical_explanation',normalized_meaning=meaning,source_anchor_ids=ids,exact_item_ids=exact))
exact=[dict(exact_item_id=f'e{i}',literal=t,category='user_protected',location_role='inline-critical') for i,t in enumerate(['13','8','5','3','2','95','95%','100%','0%','97.4%','F1 score','J=0',r'\frac{95}{95+0}',r'\frac{0}{0+5}'])]
m('definition',['src-001','src-002'],'用途：分类结果可视化，尤其监督学习；无监督学习对应名称为匹配矩阵。结构：实际与预测两个维度，类别集合相同，属于列联表。命名反映类别误认。误差矩阵为同义名称，术语出处为国家教育研究院。')
m('example',['src-003'],'测试条件：已训练的猫狗分类系统。样本总数13，猫8、狗5；行实际、列预测；猫行5和3，狗行2和3。主对角线正确，其他位置错误。',['e0','e1','e2','e3','e4'])
m('binary',['src-004'],'二分类用两行两列报告真阳性、假阴性、假阳性、真阴性；除总体正确率外还可分解错误。以猫为阳性解释各格。')
m('imbalance',['src-004'],'不平衡条件：猫95、狗5，全部预测猫。总体准确度95%；猫敏感性100%，狗识别率0%。以猫为阳性时F1超过97.4%，仍掩盖狗的完全漏识别。不是所有F1汇总方式均取该数值。',['e5','e6','e7','e8','e9','e10'])
m('youden',['src-004','src-005'],'约登指数抵消此例类别比例导致的高分假象。敏感性加特异性减一；此例95/(95+0)+0/(0+5)-1=0，恒猜猫没有有效类别区分信息。零值表示在此判别意义上无用，不把指数误写成概率。文献身份：Youden’s J statistic，Wikipedia。',['e11','e12','e13'])
m('other',['src-006'],'可依据分析目的从混淆矩阵计算其他指标，不同指标用途不同。')
contexts=[dict(source_context_item_id='wrappers',source_anchor_ids=[a['source_anchor_id'] for a in anchors],reader_relevance_decision='exclude_from_reader_facing_candidate',rationale='仅排除语言、页面分类、引用与表格的标记、日期和归档包装；技术内容由意义记录承担，术语及指数参考条目保留简洁文献身份。')]
mm=dict(schema=s.MEANING_MAP_SCHEMA,source_sha256=s.sha256_text(source),source_anchors=anchors,meanings=meanings,exact_items=exact,source_context_items=contexts,relations=[dict(from_meaning_id='example',to_meaning_id='definition',relation='illustrates'),dict(from_meaning_id='imbalance',to_meaning_id='binary',relation='limits_accuracy_interpretation'),dict(from_meaning_id='youden',to_meaning_id='imbalance',relation='same_example_comparison')]);save('meaning_map.json',mm)
bundles=[]
for bid,ids,q,shape in [('b1',['definition','example'],'矩阵如何阅读，猫狗计数如何对应？','定义段落和三列表格'),('b2',['binary'],'二分类的四种结果分别是什么？','阳性约定和三列表格'),('b3',['imbalance','youden','other'],'类别不平衡时为何高分仍会误导？','条件说明、指标比较、公式与解释')]:
 records=[m for m in meanings if m['meaning_id'] in ids]; ex=[e for e in exact if any(e['exact_item_id'] in m['exact_item_ids'] for m in records)]
 b=dict(bundle_id=bid,owned_meaning_ids=ids,reader_question=q,purpose=q,information_shape=shape,required_exact_item_ids=[e['exact_item_id'] for e in ex]);bundles.append(b)
 save('realization_packets/'+bid+'.json',dict(schema=s.REALIZATION_PACKET_SCHEMA,bundle_id=bid,audience='了解基本分类概念的中文技术读者',register='自然简体中文技术说明',purpose=q,information_shape=shape,meaning_records=records,exact_items=ex))
save('reader_plan.json',dict(schema=s.READER_PLAN_SCHEMA,bundle_order=['b1','b2','b3'],bundles=bundles,excluded_source_context_item_ids=['wrappers'],splitter='reader_question_dependencies'))
