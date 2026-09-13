import importlib.util,re,json
from pathlib import Path
p=Path('/overflow/htzhu/mingcheng_new/.codex-global/plugins/cache/ai-skills-candidate-053/writing-style/0.2+codex.local-20260913T044513Z-2716369/skills/scientific-rewrite/scripts/rewrite_support.py')
spec=importlib.util.spec_from_file_location('support',p); m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
s=Path('inputs/01-source.md').read_text(); d=Path('outputs/.work')
def save(n,o):m.write_json(d/n,o)
prompt='请把随附的《南瓜书》第 5 章神经网络材料重组为面向中文技术读者的长文说明。保留神经元模型、感知机、多层网络、误分类点集合、损失函数、梯度更新、误差逆传播、局部极小/全局最小、常见神经网络和深度学习起源等主线；保留关键公式、变量含义、条件、推导关系、章节引用和文献归因；允许重新组织段落和小节，降低阅读跳跃感，但不能把推导步骤、限制条件或负面/不确定表述删掉；普通正文用自然简体中文，公式必须是可渲染 Markdown/LaTeX；不要写成摘要列表、审稿意见、流程日志或“根据给定材料”的说明。'
(d/'prompt.md').write_text(prompt)
save('route_selection.json',m.classify_writing_style_route(prompt,s))
anchors=m.split_source_anchors(s)
sections=[('# 第5章','定位与神经元','神经网络与线性回归、对数几率回归、决策树同属机器学习，处理分类回归；算力支持其表现，深层网络构成深度学习。深度与效果的理论判断须与训练问题相连。5.1不另做模型展开；阈读yù而非阀fá；图5.1的M-P归于McCulloch和Pitts。'),('### 5.2.1','感知机边界与学习','依[1]按模型、策略、算法连接式(5.1)(5.2)。n维特征和权重、阈值、阶跃0/1输出；超平面偏置b=-theta。T有N样本，正类非负、负类严格负定义线性可分，否则不可分。在线性可分前提下寻找完全正确分隔。M为误分类样本集合，分两类错误得到非负乘积和损失。无错误则零；误差数量和距平面距离影响损失，距离参见6.1.2。固定M求导，扩充-1哑节点合并阈值，逐点随机梯度下降、学习率eta、初始化和重算M直到为空；初始化及抽样使解不唯一。'),('### 5.2.2','隐层与异或','图5.5四个二元输入通过两个隐节点的方向差与0.5阈值，再合并输出；保留(0,1)逐步代入和结果。'),('## 5.3','误差逆传播','式(5.10)依式(5.12)链式推导；输出阈值梯度等于g，更新为负eta g。平方误差、sigmoid导数和负阈值链式因子逐步展开。式(5.13)从所有输出回传经beta、b、alpha到v，导数负e x，更新正eta e x；式(5.15)的e定义从同一推导取得。式(5.14)阈值gamma有负号，导数为e、更新负eta e。所有链式中间步保留，定义输入/隐层/输出变量及样本k、l输出个数。'),('## 5.4','优化的限制','图5.10展示局部极小与全局最小；局部改善不能等同于全局保证，模拟退火、遗传算法、启发式需要另查专业资料系统学习。'),('## 5.5','其他网络','5.5网络已较不常见，5.6卷积与循环网络更常见。RBF式(5.18)为q项rho线性组合；经5.19从d维到q维，中心固定后等同3.2线性回归，可加偏置b。Boltzmann为带隐变量无向图；式(5.20)边与节点能量相加，负权重状态乘积及负阈值状态乘积，边求和i<j，保留全式。受限Boltzmann Machine即RBM只保留跨层边；5.22给定h显层各变量条件独立；5.23给定v隐层各变量条件独立。'),('## 5.6','深度学习与特征','5.6宏观解释而不展开经典网络，系统学习需其他书籍。深层网络属机器学习子集。1989卷积网络[2]，1986BP[3]；早期算力下支持向量机等非神经网络表现更好，神经网络瓶颈；2012Hinton及学生AlexNet在ImageNet明显领先第二名夺冠，学术工业关注；2015 LeCun Bengio Hinton与深度学习概念归因。人工根蒂色泽特征转向量再分类、效果依赖特征工程；图片转向量和输出分类约束使网络学习特征，二分类通常用对数几率回归输出。保留人工工程到对数几率回归、卷积特征学习到对数几率回归的比较。'),('## 参考文献','文献','保留[1]李航2012清华大学出版社；[2]全部七位作者、论文名、Neural computation卷期页及1989；[3]三位作者、论文名、nature卷期页及1986。')]
starts=[s.index(x[0]) for x in sections]+[len(s)]
exact=[]
for i,match in enumerate(re.finditer(r'\$\$.*?\$\$',s,re.S),1):
 literal=match.group(0);exact.append(dict(exact_item_id=f'f{i}',category='formula',literal=literal,sha256=m.sha256_text(literal),location_role='inline-critical',pos=match.start()))
meanings=[];bundles=[]
for i,(_,title,note) in enumerate(sections):
 mid=f'm{i+1}';bid=f'b{i+1}';ids=[a['source_anchor_id'] for a in anchors if starts[i]<=a['start']<starts[i+1]]; fs=[e['exact_item_id'] for e in exact if starts[i]<=e['pos']<starts[i+1]]
 meanings.append(dict(meaning_id=mid,kind='technical_explanation',normalized_meaning=note,source_anchor_ids=ids,exact_item_ids=fs))
 bundles.append(dict(bundle_id=bid,purpose=title,reader_question=title+'如何理解？',owned_meaning_ids=[mid],required_exact_item_ids=fs,dependencies=[] if i==0 else [f'b{i}'],information_shape='连贯解释与逐步公式推导'))
context=[dict(source_context_item_id='c1',source_anchor_ids=[a['source_anchor_id'] for a in anchors if a['start']<starts[0]],reader_relevance_decision='exclude_from_reader_facing_candidate',rationale='组队学习时间和配套课程导航不参与技术论证；独立长文不保留课程通知。')]
relations=[dict(from_meaning_id='m2',to_meaning_id='m3',kind='extends'),dict(from_meaning_id='m3',to_meaning_id='m4',kind='requires_learning'),dict(from_meaning_id='m5',to_meaning_id='m4',kind='limits_optimization_claim'),dict(from_meaning_id='m6',to_meaning_id='m7',kind='context')]
mm=dict(schema=m.MEANING_MAP_SCHEMA,source_sha256=m.sha256_text(s),source_anchors=anchors,meanings=meanings,exact_items=exact,source_context_items=context,relations=relations)
save('meaning_map.json',mm)
plan=dict(schema=m.READER_PLAN_SCHEMA,bundles=bundles,bundle_order=[b['bundle_id'] for b in bundles],excluded_source_context_item_ids=['c1'],splitter='semantic_dependencies');save('reader_plan.json',plan)
for b,meaning in zip(bundles,meanings):
 save('realization_packets/'+b['bundle_id']+'.json',dict(schema=m.REALIZATION_PACKET_SCHEMA,bundle_id=b['bundle_id'],audience='中文技术读者',register='自然简体中文技术长文',purpose=b['purpose'],meaning_records=[meaning],relation_records=relations,exact_items=[{k:v for k,v in e.items() if k!='pos'} for e in exact if e['exact_item_id'] in b['required_exact_item_ids']],information_shape=b['information_shape']))
print('语义计划及公式写作包已保存。')
