# Datasets

数据集按用途分栏，与 README [数据集](../README.md#数据集) 同源。评测基准的任务对照见 [[Benchmarks]]。官网挂了的标「官网已挂」，门户在但核心功能不通的标「服务异常」。

## 公开资料整理

- awesome_Chinese_medical_NLP [[资料](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)] — 中文医学 NLP 公开资源整理：术语集、语料库、词向量、预训练模型、知识图谱、NER、QA 等（含 CBLUE 挑战榜）
- 中成药公开数据集（RAG-CPMF） [[数据](https://gitee.com/tcmdoc/cpm)] [[论文](https://doi.org/10.1016/j.phrs.2025.107883)] — RAG-CPMF配套的持续更新大规模中成药公开数据

## 中药组方 / 提取物

- HERB 2.0 本草组鉴 [[网站](http://herb.ac.cn/v2)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11701625/)] [[DOI](https://doi.org/10.1093/nar/gkae1037)] — 整合临床试验、荟萃分析、高通量实验与文献的中药证据库，并提供实体关系知识图谱
- CMAUP 有用植物集体分子活性库 [[网站](https://www.bidd.group/CMAUP/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767869/)] [[DOI](https://doi.org/10.1093/nar/gkad921)] — BIDD的有用植物（含中药）多靶点活性、通路与疾病景观库，2024版扩展功能与关联信息，站点可下载
- BATMAN-TCM 2.0 中药成分–靶点注释库 [[网站](http://bionet.ncpsb.org.cn/batman-tcm/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767940/)] [[DOI](https://doi.org/10.1093/nar/gkad926)] — 已知与预测的中药成分–靶蛋白相互作用库，2.0大幅扩充TTI覆盖并支持由靶反查成分
- TCMBank 中药–成分–靶点–疾病库 [[网站](http://tcmbank.cn/)] [[DOI](https://doi.org/10.1038/s41392-023-01339-1)] — 可下载的大规模中药–成分–靶点–疾病关系库，含文献自动抽取后人工核对的持续更新模块
- ITCM 整合中医药与药效转录组平台 [[网站](http://itcm.biotcm.net/)] [[DOI](https://doi.org/10.1093/bib/bbad027)] — 整合多方剂/药材/成分/靶点，并提供496个中药成分的1488条药理转录谱；成分表达数据另见Synapse
- ETCM 2.0 中医药百科全书 [[网站](http://www.tcmip.cn/ETCM2/front/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10326295/)] [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)] — 收录古代方剂、中成药、药材与成分，并提供成分靶点与多尺度网络；v1站点仍在，现行入口为ETCM2
- DCABM-TCM 中药入血成分与代谢物库 [[网站](http://bionet.ncpsb.org.cn/dcabm-tcm/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10428213/)] — 文献挖掘的方剂/草药入血原型与代谢物及其检测条件（约1816个有结构入血成分）
- LTM-TCM 中西医分子表型链接库（官网已挂） [[原网站](http://cloud.tasly.com/#/tcm/home)] [[DOI](https://doi.org/10.1016/j.phrs.2022.106185)] — 整合十四个权威库与临床/古籍记录的症状–方剂–植物–成分–靶点平台（约4.8万方）；官网cloud.tasly.com域名已无法解析，核验走论文DOI
- HIT 2.0 草药成分靶点库（服务异常） [[网站](http://hit2.badd-cao.net/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728248/)] [[DOI](https://doi.org/10.1093/nar/gkab1011)] — 人工审核的草药成分–靶点活性对（约1237成分/2208靶点），覆盖2000–2020文献；门户可打开，分析后端端口当前不通
- SuperTCM 中药生物文化数据库（官网已挂） [[原网站](http://tcm.charite.de/supertcm)] [[论文](https://europepmc.org/article/MED/34656056)] [[DOI](https://doi.org/10.1016/j.biopha.2021.112315)] — Charité团队整合药典与多源数据的中药–物种–成分–靶点–通路–疾病库（约6516味药）；官网tcm.charite.de已无法解析
- TCMIO 中医药免疫肿瘤学数据库 [[网站](http://tcmio.xielab.net/)] [[数据](http://tcmio.xielab.net/download)] [[DOI](https://doi.org/10.3389/fphar.2020.00439)] — 面向免疫肿瘤的中药/方剂–成分–靶点–通路库，提供浏览、下载与REST API
- SymMap 2.0 症状映射中医药数据库 [[网站](http://www.symmap.org/)] [[数据](http://www.symmap.org/download/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323958/)] — 草药–中医症状–西医症状–成分–靶点–疾病整合库，2.0按新版药典扩草药/证候并开放关系表下载
- YaTCM 中药方剂–成分–靶点库（官网已挂） [[原网站](http://cadd.pharmacy.nankai.edu.cn/yatcm/home)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6280608/)] [[DOI](https://doi.org/10.1016/j.csbj.2018.11.002)] — 约1813首方、6220味药、4.7万天然产物及靶点/通路分析工具；南开官网当前403，核验走开放论文
- TCMID 2.0 中医药整合数据库（官网已挂） [[原网站](http://www.megabionet.org/tcmid/)] [[数据](https://zenodo.org/records/8066910)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5753259/)] [[DOI](https://doi.org/10.1093/nar/gkx1028)] — 上海团队的方剂–草药–成分–靶点整合库（与NUS的TCM-ID不是同一库）；官网megabionet已不可达，公开核验走Zenodo摘录与NAR论文
- TCMAnalyzer 中药化学信息学分析平台（官网已挂） [[原网站](http://www.rcdd.org.cn/tcmanalyzer)] [[论文](https://pubmed.ncbi.nlm.nih.gov/29425456/)] [[DOI](https://doi.org/10.1021/acs.jcim.7b00549)] — 中山大学RCDD的方剂/药材/成分网络分析与骨架检索服务（约1493方、618味药）；官网rcdd.org.cn当前超时
- TCM-Mesh 中药网络药理学分析库（官网已挂） [[原网站](http://mesh.tcm.microbioinformatics.org/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5460194/)] [[DOI](https://doi.org/10.1038/s41598-017-03039-7)] — 草药–化合物–基因–疾病网络与毒副作用记录（约6235味药）；官网当前403，核验走开放论文
- TM-MC 东北亚传统药物成分库（官网已挂） [[原网站](http://informatics.kiom.re.kr/compound/)] [[DOI](https://doi.org/10.1186/s12906-015-0758-5)] — 韩国韩医学研究院从文献抽取的药材–化合物库（约536种药材、1.4万化合物），并给出PubMed/PubChem出处；官网当前超时
- CEMTDD 中国少数民族传统药物数据库（官网已挂） [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627337/)] [[DOI](https://doi.org/10.18632/oncotarget.3789)] — 以新疆维吾尔/哈萨克等民族药为主的草药–化合物–靶点–疾病库（约621草药）；原域名cemtdd.com已改作他用，核验走PMC论文
- TCMSP 中药系统药理学数据库 [[网站](https://www.tcmsp-e.com/tcmsp.php)] [[DOI](https://doi.org/10.1186/1758-2946-6-13)] — 草药–成分–靶点–疾病网络与ADME参数平台，现行公开站为TCMSP 2.3，提供草药/分子/靶点关系表下载
- CVDHD 心血管病本草数据库（官网已挂） [[原网站](http://pkuxxj.pku.edu.cn/CVDHD)] [[DOI](https://doi.org/10.1186/1758-2946-5-51)] — 面向心血管病的本草化合物三维结构、靶点与通路库，用于虚拟筛选与网络药理；原北大站点当前超时
- TCM Database@Taiwan 中药三维结构库（官网已挂） [[原网站](http://tcm.cmu.edu.tw/)] [[论文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0015939)] [[DOI](https://doi.org/10.1371/journal.pone.0015939)] — 453味药材中约2万个分离化合物的2D/3D结构库，面向虚拟筛选；原站tcm.cmu.edu.tw已不可达，核验走PLOS论文页
- TCMGeneDIT 中药–基因–疾病文本挖掘库（官网已挂） [[原网站](http://tcm.lifescience.ntu.edu.tw/)] [[论文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2582235/)] [[DOI](https://doi.org/10.1186/1472-6882-8-58)] — 从文献挖掘中药、基因、疾病、功效与成分关联，并接入通路与PPI；官网tcm.lifescience.ntu.edu.tw已无法解析
- TCM-ID 中医药信息数据库（NUS BIDD） [[网站](https://www.bidd.group/TCMID/)] — 新加坡BIDD维护的方剂–药材–成分–靶点库，含药典/经典方与CFDA批准方；与TCMID 2.0不是同一资源

## 原始书籍 / 预训练语料

- 中医经典全文语料（内经/伤寒/金匮/温病等 115 部） [[数据集](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)] — 中医经典全文数字化语料：内经、难经、伤寒论、金匮要略及温病经典
- 高质量中医预训练数据集（医案/典籍/百科等） [[数据集](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)] — 非网络来源高质量中医预训练数据集（约 1GB），含临床案例、名家典籍、医学百科等，99% 简体中文
- ShizhenGPT 中医预训练语料（论文报告共 15B+ tokens：Stage1 文本 11.92B 含 6.3B 中医语料，Stage2 多模态约 3.6B） [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- 700 项中医药古籍文本 [[数据集](https://github.com/xiaopangxia/TCM-Ancient-Books)] — 中医药古籍文本语料合集，收录近 700 项古籍文本
- ChiMed 2.0 中文医疗预训练数据集（覆盖中医语料） [[论文](https://arxiv.org/abs/2507.15275)]

## 评测基准

- TCM-RobustSDT [[数据集](https://doi.org/10.6084/m9.figshare.33054974)] — 中医临床推理LLM鲁棒性基准数据集（Figshare）
- 中药处方审核评测基准 [[论文](https://doi.org/10.1038/s41597-025-06387-6)] [[数据](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[代码](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)] — 328道处方规范性与合理性选择题，面向中药处方安全审核评测
- TCM-AQA61 / CME-AQA 针灸推拿动作质量评估 [[论文](https://arxiv.org/abs/2606.28104)] [[DOI](https://doi.org/10.1109/TNSRE.2026.3705649)] [[代码](https://github.com/FrancisXZhang/cme-aqa)] [[数据](https://researchdata.durham.ac.uk/collections/r1jm214p229)] — 针灸（A）与推拿（T）各 61 名受试者的第一人称+第三人称同步视频，两位中医师标注分类与连续指标；配套跨视角多模态评估框架 CME-AQA
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
- MedChatZH 中医问诊数据集 [[代码](https://github.com/tyang816/MedChatZH)] [[数据集](https://huggingface.co/datasets/tyang816/MedChatZH)]
- 中文医疗在线问诊数据集 ChatMed_Consult_Dataset（50w+在线问诊+ChatGPT回复） [[数据集](https://huggingface.co/datasets/michaelwzhu/ChatMed_Consult_Dataset)]
- CMtMedQA 仲景真实多轮医患对话（约 7 万条） [[数据集](https://huggingface.co/datasets/Suprit/CMtMedQA)]
- 白泽中医药语料库V3 [[数据集](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3)] — 约15.7万条中医QA，覆盖理论、中药、方剂、诊断、针灸与临床
- 中国药典指令数据集 [[数据](https://github.com/QLU-NLP/BianCang/tree/main/ChP-TCM)] [[论文](https://arxiv.org/abs/2411.11027)] — 基于《中国药典》一部构建的KnowledgeQA与PrescriptionWriting指令数据

## 知识图谱

- ChatMed 知识图谱 [[数据集](https://github.com/ywjawmw/TCM_KG)]
- TCM-MKG 中医药多维知识图谱 [[数据](https://zenodo.org/records/15395588)]
- OpenTCM 妇科古籍知识图谱（约 4.8 万实体 / 15.2 万关系） [[代码](https://github.com/OpenTCM01/OpenTCM)] [[论文](https://arxiv.org/abs/2504.20118)]
- TCM-QG 中医文献问题生成（CHIP2020） [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86895)] [[资料](http://openkg.cn/dataset/tcm-qg)] — 约 5000 篇中医文本、1.3 万问答对，用来补知识库和自动提问（CC BY-SA 4.0）
- TCM-NER 中药说明书实体识别（OpenKG / CHIP） [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86819)] [[资料](http://openkg.cn/dataset/tcm-ner)] — 1997 篇中药说明书、13 类实体共 59803 个标注，用来自动构建用药知识图谱（CC BY-SA 4.0）

## 语料/指令

- HSQ-TD（健身气功指令微调数据集） [[数据集](https://doi.org/10.57760/sciencedb.35843)] — 健身气功养生领域首个指令微调数据集，57,843条指令基于官方教材与专业文献蒸馏（ScienceDB）

返回 [[Home]]。
