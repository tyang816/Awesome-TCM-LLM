# Benchmarks

把「可下载的评测集」和「评测论文」分开，避免和模型论文混在一起。

## 评测集

- **TCM-RobustSDT** — 中医临床推理LLM鲁棒性基准数据集（Figshare） [[数据集](https://doi.org/10.6084/m9.figshare.33054974)]
- **中药处方审核评测基准** — 328道处方规范性与合理性选择题，面向中药处方安全审核评测 [[论文](https://doi.org/10.1038/s41597-025-06387-6)] [[数据](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[代码](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)]
- **TCM-AQA61 / CME-AQA 针灸推拿动作质量评估** — 针灸（A）与推拿（T）各 61 名受试者的第一人称+第三人称同步视频，两位中医师标注分类与连续指标；配套跨视角多模态评估框架 CME-AQA [[论文](https://arxiv.org/abs/2606.28104)] [[DOI](https://doi.org/10.1109/TNSRE.2026.3705649)] [[代码](https://github.com/FrancisXZhang/cme-aqa)] [[数据](https://researchdata.durham.ac.uk/collections/r1jm214p229)]
- **LingLan（灵兰秘典）大规模多任务中医评测基准 (2026)** [[数据集](https://github.com/TCMAI-BJTU/LingLan)] [[论文](https://arxiv.org/abs/2602.01779)]
- **ZhongJing-OMNI 中医多模态评测（含舌诊）** [[数据集](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]
- **TCMEval-SDT 辨证思维评测（专家标注病案）** — 中医辨证思维评测基准，含 300 例证候诊断案例（来源网络、古籍与医院病案），元数据遵循 FAIR 原则（Scientific Data 2025） [[DOI](https://doi.org/10.1038/s41597-025-04772-9)] [[论文](https://www.nature.com/articles/s41597-025-04772-9)] [[代码](https://github.com/zhuyan166/TCMEval)]
- **TCMBench 中医药大模型全面评测基准** — 面向中医领域的综合性大模型评测基准 TCMBench（arXiv 2024） [[数据集](https://github.com/ywjawmw/TCMBench)] [[论文](https://arxiv.org/abs/2406.01126)]
- **TCM-Vision-Benchmark 中医视觉评测（药材识别/望诊等，约 7k 题）** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Vision-Benchmark)]
- **标准化舌象病理标注数据集** — 6719张标准化舌象、20类病理多标签公开数据集，含检测基线 [[论文](https://arxiv.org/abs/2507.18288)] [[数据](https://doi.org/10.5061/dryad.1c59zw48r)] [[代码](https://github.com/btbuIntelliSense/Intelligent-tongue-diagnosis-detection-dataset)]
- **TCM-Text-Exams 近年中医执业/考研真题文本基准** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams)]
- **TCM-Ladder 中医多模态问答评测基准 (NeurIPS 2025)** — 中医多模态问答评测基准 TCM-Ladder，面向真实世界任务综合评估中医多模态大模型（arXiv 2025） [[数据集](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[榜单](https://tcmladder.com)] [[论文](https://arxiv.org/abs/2505.24063)]
- **TCM-Eval 动态可扩展中医评测基准** [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- **TCM-BEST4SDT 辨证论治病例评测基准** [[数据集](https://github.com/DYJG-research/TCM-BEST4SDT)] [[论文](https://arxiv.org/abs/2512.02816)]
- **TCM-5CEval 五维中医深度评测** [[论文](https://arxiv.org/abs/2511.13169)]
- **TCM-3CEval 核心知识·经典理解·临床决策三轴评测** [[论文](https://arxiv.org/abs/2503.07041)]
- **医疗大模型中文考试评估** [[数据集](https://github.com/jingnant/Medical-LLMs-Chinese-Exam)]
- **MTCMB 中医多任务评测基准（知识/推理/安全）** — 中医多任务评测基准 MTCMB 数据，覆盖知识、推理与安全维度，12 子集约 7100 样本（arXiv 2025） [[数据集](https://github.com/Wayyuanyuan/MTCMB)] [[论文](https://arxiv.org/abs/2506.01252)]
- **HWTCMBench 中医能力评测集** [[数据集](https://huggingface.co/datasets/Monor/hwtcm)]
- **PromptCBLUE 中文医疗NLP指令化评测** — 把CBLUE的16项中文医疗NLP任务改写成生成式指令，CCKS-2023评测任务，中文医疗LLM早期统一榜之一 [[代码](https://github.com/michael-wzhu/PromptCBLUE)]
- **CMExam 中文执业医师考试评测集** — 源自国家医学考试的中文医考题（约6.8万），带多维标注，常被中文医疗/中医LLM当知识回忆对照 [[论文](https://arxiv.org/abs/2306.03030)] [[代码](https://github.com/williamliujl/CMExam)]
- **CMB 中文综合医学评测（Exam + Clin）** — 中大深圳FreedomIntelligence的中文医疗综合基准：CMB-Exam约28万题+CMB-Clin复杂病案，中医论文里最常见的西医/综合对照榜 [[论文](https://arxiv.org/abs/2308.08833)] [[正式发表](https://aclanthology.org/2024.naacl-long.343/)] [[代码](https://github.com/FreedomIntelligence/CMB)] [[数据集](https://huggingface.co/datasets/FreedomIntelligence/CMB)]
- **TCM-SD 中医辨证评测基准** — 首个大规模公开中医辨证文本基准（54152 条真实病历、148 证，CC BY-NC-SA 4.0）；仓库写明完整数据在 TCM_SD_with_knowledge，天池 dataId=139034 [[论文](https://arxiv.org/abs/2203.10839)] [[正式发表](https://aclanthology.org/2022.ccl-1.80/)] [[代码](https://github.com/Borororo/ZY-BERT)] [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=139034)]
- **IMCS-21 智能医疗问诊对话** — 约4116场儿科在线问诊，带实体/意图/症状/报告标注，后接入CBLUE四任务 [[DOI](https://doi.org/10.1093/bioinformatics/btac817)] [[代码](https://github.com/lemuria-wchen/imcs21)] [[CBLUE任务](https://github.com/lemuria-wchen/imcs21-cblue)]
- **CBLUE 中文生物医学语言理解评测** — 中文生物医学NLU总榜（NER/关系/诊断归一化/分类等），PromptCBLUE的源任务集；天池有提交入口 [[论文](https://aclanthology.org/2022.acl-long.544/)] [[代码](https://github.com/CBLUEbenchmark/CBLUE)]

## 评测与评估论文

- [*Future Internet (MDPI)*] **RAG+LoRA 中医执照考试推理架构** RAG+LoRA生成式架构，构建台湾中医师执照考试11,476题（2005–2025）数据集，准确率61.0%→89.0%+（Future Internet） [Chung Shan Medical University Hospital，Chung Shan Medical University] [[DOI](https://doi.org/10.3390/fi18060280)]
- [*Frontiers in Plant Science*] **药用植物多模态大模型评测** 多模态LLM药用植物识别系统评测 [绍兴文理学院] [[DOI](https://doi.org/10.3389/fpls.2026.1765281)]
- [*arXiv*] **灵兰秘典 (LingLan)** 大规模多任务中医评测基准，覆盖 5 大域、13 子任务、25624 实例 [北京交通大学等] [[论文](https://arxiv.org/abs/2602.01779)] [[代码](https://github.com/TCMAI-BJTU/LingLan)] [[网站](http://tcmnlp.com)]
- [*Journal of Evidence-Based Medicine*] **中医考题大/轻量模型对比** 大规模与轻量级LLM中医考题系统对比 [河南大学第一附属医院] [[DOI](https://doi.org/10.1111/jebm.70118)]
- [*Expert Systems with Applications*] **中医端到端临床支持基准** 面向端到端临床支持全链路的中医LLM评测基准 [华东师范大学] [[DOI](https://doi.org/10.1016/j.eswa.2026.132267)]
- [*Journal of Traditional Chinese Medical Sciences*] **中医智能预问诊临床评估** LLM智能预问诊系统三甲医院临床评估，采用医-AI-患三元模式 [北京中医医院] [[DOI](https://doi.org/10.1016/j.jtcms.2026.06.002)]
- [*Frontiers in Medicine*] **中医教育AI导师评估** 跨认知层级的多模态LLM中医教育评估 [北京中医药大学] [[DOI](https://doi.org/10.3389/fmed.2026.1893231)]
- [*Scientific Reports*] **中医执业考试三模型评估** Gemini等3个LLM在中医国家执业医师考试上的系统评估 [上海交通大学] [[DOI](https://doi.org/10.1038/s41598-026-49200-z)]
- [*arXiv*] **TongueDx2** 舌诊深度学习设计空间系统消融研究（20+模型版本），含5109图像/976专家标注 [[论文](https://arxiv.org/abs/2607.28148)]
- [*Frontiers in Artificial Intelligence*] **TCMI-F-6D** 中医信息学跨学科基础能力六维基准 [安徽中医药大学] [[DOI](https://doi.org/10.3389/frai.2026.1780967)] [[代码](https://github.com/123adf-dev/TCMI-F-6D-Benchmark)]
- [*ICIC 2026*] **TCMBenchEval** 基于真实临床医案的LLM中医评测基准 [汕头大学] [[DOI](https://doi.org/10.1007/978-981-92-3498-1_1)]
- **Med-Bench-Arena** 面向医学与中医药LLM/Agent的开源评测平台，支持HF/vLLM/LiteLLM、多模态与中医特色指标（ZhongJing团队） [[代码](https://github.com/pariskang/Med-Bench-Arena)]
- [*arXiv*] **MMIR-TCM** 记忆增强的多模态舌诊与临床决策框架，提出 MedTCM 数据集与 TDEU 评测指标 [[论文](https://arxiv.org/abs/2607.01814)]
- [*Pattern Recognition*] **ATCMD-Bench** 首个Agentic中医诊断基准，通过多智能体模拟问诊评估LLM诊疗能力 [华南理工大学] [[DOI](https://doi.org/10.1016/j.patcog.2026.113679)]
- [*Expert Systems with Applications*] **针灸大模型驯化与生成评估 (Taming LLMs for Acupuncture)** 面向针灸推拿诊断的大模型驯化方法，并在语义相似度层面评估生成质量 [[DOI](https://doi.org/10.1016/j.eswa.2024.125920)]
- [*JMIR Medical Informatics*] **辨证思维评测 (Syndrome Differentiation Thinking)** 评估并提升大语言模型中医辨证思维能力的方法开发研究 [[DOI](https://doi.org/10.2196/75103)]
- [*UbiComp Companion 2025*] **中医大模型误导信息检测评测** 3000+中医考题×4种范式的安全性评测框架，覆盖错误选项、误导与捏造检测 [清华大学] [[DOI](https://doi.org/10.1145/3714394.3756275)]
- [*JMIR Formative Research*] **中医卒中LLM评测** 中医卒中领域LLM定量基准研究 [成都中医药大学] [[DOI](https://doi.org/10.2196/81545)]
- [*Frontiers in Pharmacology*] **中医临床指南遵循评估** LLM遵循中医临床实践指南的内容分析评估 [兰州大学] [[DOI](https://doi.org/10.3389/fphar.2025.1649041)]
- [*JMIR Formative Research*] **中医临床决策5-LLM对比** 5个LLM中医临床决策能力对比研究 [南京中医药大学] [[DOI](https://doi.org/10.2196/80167)]
- [*NeurIPS 2025*] **TCM-Ladder** 首个中医多模态问答评测基准，涵盖52000+题目 [[论文](https://arxiv.org/abs/2505.24063)] [[代码](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[榜单](https://tcmladder.com)]
- [*WISE 2025*] **TCM-Eval (WISE 2025)** 天津国际生物医药联合研究院提出的多维中医评测框架；与智明堂TCM-Eval（arXiv 2511.07148）同名但为不同工作 [天津国际生物医药联合研究院] [[DOI](https://doi.org/10.1007/978-981-95-7251-9_15)]
- [*arXiv*] **TCM-BEST4SDT** 面向辨证论治的病例评测基准（知识/伦理/安全/SDT） [[DOI](https://doi.org/10.6084/m9.figshare.30615956)] [[论文](https://arxiv.org/abs/2512.02816)] [[代码](https://github.com/DYJG-research/TCM-BEST4SDT)]
- [*arXiv*] **TCM-5CEval** 在 TCM-3CEval 基础上扩展本草与非药物疗法的五维深度评测 [[论文](https://arxiv.org/abs/2511.13169)]
- [*Communications Medicine*] **TCM-3CEval** 中医大模型三轴评测（核心知识、经典理解、临床决策） [[论文](https://arxiv.org/abs/2503.07041)] [[正式发表](https://doi.org/10.1038/s43856-026-01631-5)]
- [*npj Digital Medicine*] **TCM LLM针灸诊疗能力评估** 7个通用LLM与执业针灸师对照的真实病例评估（辨证/选穴/针法/方药），高影响力临床测评研究 [[DOI](https://doi.org/10.1038/s41746-025-01845-2)]
- [*arXiv*] **New Snow Tablets（新雪片）** 揭示通用与中医专用LLM依赖药名猜测成分的系统缺陷 [[论文](https://arxiv.org/abs/2504.03786)]
- [*Scientific Data*] **MTCMB** 中医多任务评测基准，12子集约7100样本，覆盖知识/推理/方剂/安全 [[论文](https://arxiv.org/abs/2506.01252)] [[代码](https://github.com/Wayyuanyuan/MTCMB)] [[正式发表](https://doi.org/10.1038/s41597-026-07967-w)]
- [*Preprints.org（预印本）*] **GPT 台湾中医执业考试评估** GPT-3.5/GPT-4/GPT-4o 在台湾中医执业考试中的表现与可靠性分析（预印本） [[DOI](https://doi.org/10.20944/preprints202501.1787.v1)]
- [*IJCNN 2025*] **From Metaphor to Mechanism** LLM解码中医隐喻/取象语言并映射现代医学概念 [Shandong Normal University,Jinan,China，China Pharmaceutical University,Nanjing,China，The University of Tokyo,Tokyo,Japan，Universiti Tunku Abdul Rahman,Perak,Malaysia] [[论文](https://arxiv.org/abs/2503.02760)] [[正式发表](https://doi.org/10.1109/ijcnn64981.2025.11228098)]
- [*南京中医药大学学报*] **中医标准化评估基准** 覆盖13个学科共29506道题的中医测评基准，系统评测3个通用模型与5个中文医疗模型 [成都中医药大学] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1383)]
- [*arXiv*] **TCMD** 面向大模型评测的中医执业考试选择题集（论文报告约 2851 训 / 600 测）；独立打开论文页未见官方 GitHub 或 Hugging Face 下载 [[论文](https://arxiv.org/abs/2406.04941)]
- [*Journal of Translational Medicine*] **LLM 中医语言文化偏差研究** 比较不同国家大模型的中医表现，论证本土化模型的必要性 [Zhujiang Hospital，Southern Medical University，Shanghai Jiao Tong University，Shanghai First People's Hospital] [[DOI](https://doi.org/10.1186/s12967-024-05128-4)]
- [*Research Square（预印本）*] **GPT-4 中医研究生考试评估** GPT-4 与国产主流大模型在中医研究生考试数据集上的表现评估（预印本） [China Academy of Chinese Medical Science，中国中医科学院，北京中医药大学，Changchun University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.21203/rs.3.rs-4392855/v1)]
- [*J Integr Complement Med*] **GPT vs ERNIE 中医文化背景对比研究** 以文化背景为框架对比 GPT 与 ERNIE 在中医任务上的表现（J Integr Complement Med 2024） [北京大学，College of Engineering, Boston University, Boston, MA, USA.] [[DOI](https://doi.org/10.1089/jicm.2024.0902)]
- [*arXiv*] **ChatGPT 中医知识理解探究** ChatGPT 对中医知识理解能力的评测 [[论文](https://arxiv.org/abs/2403.09164)]
- [*Chinese Medicine and Culture*] **ChatGPT 中医交互可行性研究** 以 ChatGPT 为例探讨交互式AI应用于中医的可行性与挑战 [上海中医药大学] [[DOI](https://doi.org/10.1097/MC9.0000000000000103)]
- **中医新冠文献 LLM 命名实体识别** 大语言模型用于中医新冠文献命名实体识别的比较研究（预印本） [[DOI](https://doi.org/10.2196/preprints.54346)]
- [*JMIR Medical Education*] **ChatGPT 针灸教育研究** ChatGPT 作为针灸学习工具的对照研究 [Seoul National University Hospital] [[DOI](https://doi.org/10.2196/47427)]

## 阅读提示

- 名称相近不一定是同一套：例如存在多个 **TCM-Eval**。
- 考试类（执业医师 / 考研）测的是知识回忆，不等于临床辨证能力。
- 多模态基准（TCM-Ladder、舌象集）需要看输入模态是否与模型匹配。

返回 [[Home]] · 模型见 [[Models]]。
