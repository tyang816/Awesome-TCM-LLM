# Datasets

数据集按用途分栏，与 README [数据集](../README.md#数据集) 同源。评测基准的任务对照见 [[Benchmarks]]。

## 公开资料整理

- awesome_Chinese_medical_NLP [[资料](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)] — 中文医学 NLP 公开资源整理：术语集、语料库、词向量、预训练模型、知识图谱、NER、QA 等（含 CBLUE 挑战榜）
- 中成药公开数据集（RAG-CPMF） [[数据](https://gitee.com/tcmdoc/cpm)] [[论文](https://doi.org/10.1016/j.phrs.2025.107883)] — RAG-CPMF配套的持续更新大规模中成药公开数据

## 原始书籍 / 预训练语料

- 中医经典全文语料（内经/伤寒/金匮/温病等 115 部） [[数据集](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)] — 中医经典全文数字化语料：内经、难经、伤寒论、金匮要略及温病经典
- 高质量中医预训练数据集（医案/典籍/百科等） [[数据集](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)] — 非网络来源高质量中医预训练数据集（约 1GB），含临床案例、名家典籍、医学百科等，99% 简体中文
- ShizhenGPT 中医预训练语料（论文报告共 15B+ tokens：Stage1 文本 11.92B 含 6.3B 中医语料，Stage2 多模态约 3.6B） [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- 700 项中医药古籍文本 [[数据集](https://github.com/xiaopangxia/TCM-Ancient-Books)] — 中医药古籍文本语料合集，收录近 700 项古籍文本
- ChiMed 2.0 中文医疗预训练数据集（覆盖中医语料） [[论文](https://arxiv.org/abs/2507.15275)]

## 评测基准

- TCM-RobustSDT [[数据集](https://doi.org/10.6084/m9.figshare.33054974)] — 中医临床推理LLM鲁棒性基准数据集（Figshare）
- 中药处方审核评测基准 [[论文](https://doi.org/10.1038/s41597-025-06387-6)] [[数据](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[代码](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)] — 328道处方规范性与合理性选择题，面向中药处方安全审核评测
- LingLan（灵兰秘典）大规模多任务中医评测基准 (2026) [[数据集](https://github.com/TCMAI-BJTU/LingLan)] [[论文](https://arxiv.org/abs/2602.01779)]
- ZhongJing-OMNI 中医多模态评测（含舌诊） [[数据集](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]
- TCMEval-SDT 辨证思维评测（专家标注病案） [[DOI](https://doi.org/10.1038/s41597-025-04772-9)] [[论文](https://www.nature.com/articles/s41597-025-04772-9)] [[代码](https://github.com/zhuyan166/TCMEval)] — 中医辨证思维评测基准，含 300 例证候诊断案例（来源网络、古籍与医院病案），元数据遵循 FAIR 原则（Scientific Data 2025）
- TCMBench 中医药大模型全面评测基准 [[数据集](https://github.com/ywjawmw/TCMBench)] [[论文](https://arxiv.org/abs/2406.01126)] — 面向中医领域的综合性大模型评测基准 TCMBench（arXiv 2024）
- TCM-Vision-Benchmark 中医视觉评测（药材识别/望诊等，约 7k 题） [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Vision-Benchmark)]
- 标准化舌象病理标注数据集 [[论文](https://arxiv.org/abs/2507.18288)] [[数据](https://doi.org/10.5061/dryad.1c59zw48r)] [[代码](https://github.com/btbuIntelliSense/Intelligent-tongue-diagnosis-detection-dataset)] — 6719张标准化舌象、20类病理多标签公开数据集，含检测基线
- TCM-Ladder 中医多模态问答评测基准 (NeurIPS 2025) [[数据集](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[榜单](https://tcmladder.com)] [[论文](https://arxiv.org/abs/2505.24063)] — 中医多模态问答评测基准 TCM-Ladder，面向真实世界任务综合评估中医多模态大模型（arXiv 2025）
- TCM-Eval 动态可扩展中医评测基准 [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- TCM-BEST4SDT 辨证论治病例评测基准 [[数据集](https://github.com/DYJG-research/TCM-BEST4SDT)] [[论文](https://arxiv.org/abs/2512.02816)]
- TCM-5CEval 五维中医深度评测 [[论文](https://arxiv.org/abs/2511.13169)]
- TCM-3CEval 核心知识·经典理解·临床决策三轴评测 [[论文](https://arxiv.org/abs/2503.07041)]
- MTCMB 中医多任务评测基准（知识/推理/安全） [[数据集](https://github.com/Wayyuanyuan/MTCMB)] [[论文](https://arxiv.org/abs/2506.01252)] — 中医多任务评测基准 MTCMB 数据，覆盖知识、推理与安全维度，12 子集约 7100 样本（arXiv 2025）
- HWTCMBench 中医能力评测集 [[数据集](https://huggingface.co/datasets/Monor/hwtcm)]

## 考试数据集

- TCM-Text-Exams 近年中医执业/考研真题文本基准 [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams)]
- 医疗大模型中文考试评估 [[数据集](https://github.com/jingnant/Medical-LLMs-Chinese-Exam)]

## 指令/对话数据集

- 黄帝内经SFT指令集 [[数据集](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2)] — 杏核配套约2009条内经相关指令数据，含thinking/output字段
- TCMNSCLC 非小细胞肺癌中医推理真实世界数据集 [[数据集](https://huggingface.co/datasets/zhangxinxin0428/TCMNSCLC)] [[DOI](https://doi.org/10.5281/zenodo.21027568)] — 真实世界医案全标注（辨证/治法/汤药/中成药）的中医推理数据集
- 高质量中医 SFT 数据集 [[数据集](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]
- TCMChat-dataset-600k 中药知识问答与推荐指令数据 [[数据集](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- ShizhenGPT 多模态指令微调数据（文本/视觉/语音/ECG 等，论文 Table 3 合计约 31.1 万条） [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- 中医药指令数据集 ShenNong_TCM_Dataset [[数据集](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)]
- MedChatZH 中医问诊数据集 [[数据集](https://huggingface.co/datasets/tyang816/MedChatZH)]
- 中文医疗在线问诊数据集 ChatMed_Consult_Dataset（50w+在线问诊+ChatGPT回复） [[数据集](https://huggingface.co/datasets/michaelwzhu/ChatMed_Consult_Dataset)]
- CMtMedQA 仲景真实多轮医患对话（约 7 万条） [[数据集](https://huggingface.co/datasets/Suprit/CMtMedQA)]
- 白泽中医药语料库V3 [[数据集](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3)] — 约15.7万条中医QA，覆盖理论、中药、方剂、诊断、针灸与临床
- 中国药典指令数据集 [[数据](https://github.com/QLU-NLP/BianCang/tree/main/ChP-TCM)] [[论文](https://arxiv.org/abs/2411.11027)] — 基于《中国药典》一部构建的KnowledgeQA与PrescriptionWriting指令数据

## 知识图谱

- ChatMed 知识图谱 [[数据集](https://github.com/ywjawmw/TCM_KG)]
- TCM-MKG 中医药多维知识图谱 [[数据](https://zenodo.org/records/15395588)]
- OpenTCM 妇科古籍知识图谱（约 4.8 万实体 / 15.2 万关系） [[代码](https://github.com/OpenTCM01/OpenTCM)] [[论文](https://arxiv.org/abs/2504.20118)]

## 语料/指令

- HSQ-TD（健身气功指令微调数据集） [[数据集](https://doi.org/10.57760/sciencedb.35843)] — 健身气功养生领域首个指令微调数据集，57,843条指令基于官方教材与专业文献蒸馏（ScienceDB）

返回 [[Home]]。
