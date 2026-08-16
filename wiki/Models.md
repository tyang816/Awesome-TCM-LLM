# Models

本页是 README [开源模型](../README.md#开源模型) 的展开版：先给选型原则，再给完整表。

## 怎么选

| 场景 | 优先看 |
| --- | --- |
| 本地推理 / 复现论文 | 开源权重 + 代码 + 配套数据 |
| 舌诊 / 四诊 | 标签含 `multimodal` 的模型（如 ShizhenGPT、TongueVLM） |
| 问诊工作流 | `agent` 或配套 GraphRAG 系统，而不是单模型 |
| 当底座继续微调 | 同系列 Base / Instruct，以及通用中文医疗模型 |
| 只做对照实验 | 通用中文医疗栏（华佗、孙思邈等） |

中医专用 63 · 其中开源权重 12 · 通用医疗 7 · HF 精选 12。

## 开源权重

| 模型 | 年 | 特色 | 链接 |
| --- | :---: | --- | --- |
| **杏核 (Xinghe)** | 2026 | — | [权重](https://huggingface.co/zsyjsld/Xinghe1.2-9B) · [数据](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2) |
| **知方丹台 (ZhiFangDanTai)** | 2025 | RAG · 图谱 | [论文](https://arxiv.org/abs/2509.05867) · [权重](https://huggingface.co/tczzx6/ZhiFangDanTai1.0) |
| **白泽 (Baize-TCM-LLM)** | 2025 | — | [权重](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model) · [数据](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3) |
| **扁仓 (BianCang)** | 2025 | — | [论文](https://arxiv.org/abs/2411.11027) · [权重](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct) · [代码](https://github.com/QLU-NLP/BianCang) |
| **仲景 (ZhongJing)** | 2025 | — | [论文](https://doi.org/10.26599/TST.2025.9010046) · [权重](https://huggingface.co/CMLM/ZhongjingGPT1_13B) · [代码](https://github.com/pariskang/CMLM-ZhongJing) |
| **ViTCM-LLM** | 2025 | 多模态 · RAG | [论文](https://doi.org/10.1109/bibm66473.2025.11357113) · [权重](https://huggingface.co/Mark-CHAE/ViTCM-LLM) · [代码](https://github.com/jw-chae/ViTCM_LLM) |
| **TCMChat** | 2025 | — | [论文](https://doi.org/10.1016/j.phrs.2024.107530) · [权重](https://huggingface.co/ZJUFanLab/TCMChat-600k) · [代码](https://github.com/ZJUFanLab/TCMChat) · [数据](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k) |
| **ShizhenGPT** | 2025 | 多模态 | [论文](https://arxiv.org/abs/2508.14706) · [权重](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni) · [代码](https://github.com/FreedomIntelligence/ShizhenGPT) |
| **ChatTCM** | 2025 | — | [权重](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain) |
| **TCMLLM / 灵丹 (Lingdan)** | 2024 | — | [论文](https://doi.org/10.1016/j.dcmed.2025.01.007) · [权重](https://huggingface.co/TCMLLM/Lingdan-13B-Base) · [代码](https://github.com/2020MEAI/TCMLLM) |
| **MedChatZH** | 2024 | — | [论文](https://doi.org/10.1016/j.compbiomed.2024.108290) · [权重](https://huggingface.co/tyang816/medchatzh) · [代码](https://github.com/tyang816/MedChatZH) · [数据](https://huggingface.co/datasets/tyang816/MedChatZH) |
| **神农大模型 (ShenNong-TCM-LLM)** | 2023 | — | [权重](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM) · [代码](https://github.com/michael-wzhu/ShenNong-TCM-LLM) · [数据](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset) |

## 论文或产品向（无公开权重）

- [*Digital Chinese Medicine*] **青囊 (QingNangTCM)** 参数高效微调的中医问答与临床推理模型，构建10万条**QnTCM_Dataset**语料 [河北北方学院] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.002)]
- [*ISCTIS 2026*] **舌面多模态融合智能诊断** 舌-面多模态特征融合+LLM驱动的中医智能诊断 [厦门理工学院] [[DOI](https://doi.org/10.1109/ISCTIS70043.2026.11572361)]
- [*Frontiers in Medicine*] **树状自反思检索中医问答** 树状组织语料+自反思检索的中医 QA 方法（Frontiers in Medicine 2026） [[DOI](https://doi.org/10.3389/fmed.2026.1752778)]
- [*JMIR Medical Informatics*] **TongueVLM** 中医舌诊多模态大模型，支持舌象描述生成与体质推理 [[论文](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- [*Chinese Medicine*] **TCMNet** LLM辅助疾病知识挖掘+PPI网络与结合预测的方剂优化策略 [浙江省中医药研究院] [[DOI](https://doi.org/10.1186/s13020-026-01360-w)]
- [*Digital Chinese Medicine*] **Qwen-TCM-Dia** 面向中医泄泻的专科微调模型（续训+CoT指令微调），覆盖症状→病机→治法→方药推理链 [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.003)]
- **Med-Shicheng（师承）** 基于天医 (Tianyi) 的轻量级名老中医经验传承框架，单模型内化5位国医大师知识系统、覆盖7类任务 [南京中医药大学等] [[论文](https://arxiv.org/abs/2603.23520)] [[代码](https://github.com/NJUCM-BJUCM-TCM-AI/Med-Shicheng)]
- [*Applied Intelligence*] **KDC-NER** 知识引导数据增强+大模型微调的中医嵌套命名实体识别框架 [江西中医药大学] [[DOI](https://doi.org/10.1007/s10489-026-07095-3)]
- [*Chinese Herbal Medicines*] **HerbWise** 面向传统草药（THM）的领域大模型，服务草药现代化与标准化 [成都中医药大学] [[DOI](https://doi.org/10.1016/j.chmed.2026.02.010)]
- [*Chinese Medicine*] **GastroTCM** 中医消化内科大模型，基于Llama3-8B微调并结合RAG与智能体框架 [[论文](https://link.springer.com/article/10.1186/s13020-025-01295-8)]
- **DongYuan** 中西医结合脾胃病诊断LLM框架，融合中医辨证与西医诊断推理 [[论文](https://arxiv.org/abs/2603.28191)]
- [*Digital Chinese Medicine*] **CMM-EmbedCluster** 基于LLM与药性理论的中药聚类框架，构建567味药性知识库 [南京中医药大学] [[DOI](https://doi.org/10.1016/j.dcmed.2026.05.010)]
- [*Expert Systems with Applications*] **针灸大模型驯化与生成评估 (Taming LLMs for Acupuncture)** 面向针灸推拿诊断的大模型驯化方法，并在语义相似度层面评估生成质量 [[DOI](https://doi.org/10.1016/j.eswa.2024.125920)]
- [*npj Digital Medicine*] **补充替代医学文献抽取语言模型** 用于补充替代医学文献数据抽取与偏倚风险评估的语言模型 [兰州大学] [[DOI](https://doi.org/10.1038/s41746-025-01457-w)]
- [*IEEE Journal of Biomedical and Health Informatics*] **草药-药物相互作用预测** LLM增强的草药-药物相互作用预测 [深圳大学] [[DOI](https://doi.org/10.1109/jbhi.2025.3558667)]
- [*Cell Discovery*] **神农Alpha** 西湖大学神农 Alpha：AI 驱动的天然药物知识智能编目、获取与翻译共享协作平台（Cell Discovery 2025） [西湖大学] [[DOI](https://doi.org/10.1038/s41421-025-00776-2)] [[网站](https://shennongalpha.westlake.edu.cn/)] [[论文](https://www.nature.com/articles/s41421-025-00776-2)] [[代码](https://github.com/shennong-program/shennongname)]
- **智明堂 (ZMT-M1)** 中医大模型及TCM-Eval动态可扩展评测基准 [北京航空航天大学] [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- [*Chinese Medicine*] **悬壶 (XuanHuGPT)** 基于参数高效微调（PEFT）的中医领域大模型 [河北北方学院] [[DOI](https://doi.org/10.1186/s13020-025-01200-3)]
- [*Expert Systems with Applications*] **岐伯 (Qibo)** 天津大学等提出的中医大模型与Qibo Benchmark，持续预训练+SFT提升辨证与问答能力 [天津大学，天津中医药大学] [[正式发表](https://doi.org/10.1016/j.eswa.2025.127672)] [[论文](https://arxiv.org/abs/2403.16056)] [[DOI](https://doi.org/10.1016/j.eswa.2025.127672)]
- **天惠 (TianHui)** 面向12类中医场景的领域LLM（DeepSeek-R1-Distill-Qwen-14B+PT/SFT），开源代码与评测脚本 [[论文](https://arxiv.org/abs/2509.19834)] [[代码](https://github.com/JYfantast/TianHui)]
- [*Information Fusion*] **天医 (Tianyi)** 南京中医药大学等提出约7B参数中医大模型，按读书—临证—跟师多阶段训练，配套TCMEval评测与真实世界验证 [南京中医药大学] [[正式发表](https://doi.org/10.1016/j.inffus.2025.103663)] [[论文](https://arxiv.org/abs/2505.13156)] [[新闻](https://blog.sciencenet.cn/blog-279293-1501581.html)]
- [*Scientific Reports*] **双通道知识注意力辨证模型** 双通道知识注意力的中医辨证NLP模型，缓解生僻字与术语抽取难题 [[DOI](https://doi.org/10.1038/s41598-025-96404-w)]
- [*JMIR Medical Informatics*] **中医方剂分类加权投票** LLM加权投票中医方剂分类方法 [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.2196/69286)]
- [*IEEE BIBM 2025*] **TCM-VisResolve (TCM-VR)** 基于Qwen2.5-VL的中医多模态大模型，支持163类22万张干药材图像识别与88万候选答案临床MCQ [中央民族大学] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356679)]
- [*APWeb-WAIM 2025*] **TCM-R1** 通过GRPO增强中医推理能力的大模型 [西南大学] [[论文](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*Computers in Biology and Medicine*] **TCM-KLLaMA** 知识图谱与大模型融合的中医方剂智能生成模型 [[DOI](https://doi.org/10.1016/j.compbiomed.2025.109887)]
- [*Chinese Medicine*] **TCM-DS** 药食同源食疗方智能推荐领域大模型 [澳门科技大学] [[DOI](https://doi.org/10.1186/s13020-025-01249-0)]
- [*arXiv*] **RACE-Align** 检索增强+CoT 式 DPO 的轻量中医对齐模型（Qwen3-1.7B），探索小模型对齐路线 [[arXiv](https://arxiv.org/abs/2506.02726)]
- [*IEEE ICIP 2025*] **MCM** 多智能体协同的中医多模态诊断框架（ICIP 2025） [上海计算机软件技术开发中心] [[代码](https://github.com/JerryMazeyu/MCM)] [[正式发表](https://doi.org/10.1109/icip55913.2025.11084334)]
- **Ladder-base (GRPO-TCM)** TCM-Ladder团队提出的首个GRPO强化学习对齐中医LLM [[论文](https://arxiv.org/abs/2510.17402)]
- **Hengqin-RA-v1** 类风湿关节炎中医诊疗大模型及配套数据集 [[论文](https://arxiv.org/abs/2501.02471)]
- [*Applied Sciences*] **Gen-SynDi** 知识引导的生成式AI框架，用于辨证与疾病诊断的双向教学 [[DOI](https://doi.org/10.3390/app15094862)]
- **DoPI** 类医生主动问诊中医大模型，引导模型+专家模型协同架构，问诊准确率84.68% [[论文](https://arxiv.org/abs/2507.04877)]
- [*IEEE BIBM 2025*] **ChatGLM-FGIDs-TCM** 知识融合的ChatGLM中医临床决策支持模型，面向功能性胃肠病（FGIDs） [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356283)]
- **BenCao（指令微调本草助手）** 基于ChatGPT自然语言指令对齐的中医多模态助手，对接舌象API与知识库，部署于GPTs Store（区别于华驼/本草） [[论文](https://arxiv.org/abs/2510.17415)]
- **大数中医 (BigDataTCM)** 河南工业大学复杂性科学研究院与阿帕斯联合研发的中医垂直领域大模型（34B），提供医疗问答、诊断支持与中医知识服务 [河南工业大学] [[代码](https://github.com/HAUT-CS/BigDataTCM)]
- [*AAAI*] **仲景（CMtMedQA 线，Yang et al.）** 与 Kang 系 ZhongJingGPT 同名不同源的中医大模型：Ziya-LLaMA-13B 全流程 CPT+SFT+RLHF，基于约 7 万条真实多轮医患对话 CMtMedQA（AAAI 2024；注意与 Tsinghua Sci Technol 的 ZhongJingGPT 无作者与工件交集） [[论文](https://doi.org/10.1609/aaai.v38i17.29907)] [[arXiv](https://arxiv.org/abs/2308.03549)]
- **中医提示工程框架** 基于提示工程框架的大语言模型中医智能理解方法 [[论文](https://arxiv.org/abs/2410.19451)]
- [*Computer Methods and Programs in Biomedicine Update*] **TCM-GPT** 面向中医领域自适应的高效预训练大模型 [[DOI](https://doi.org/10.1016/j.cmpbup.2024.100158)] [[论文](https://arxiv.org/abs/2311.01786)]
- [*IEEE BIBM*] **TCM-FTP** 面向中药处方预测的大模型微调方法 [[DOI](https://doi.org/10.1109/BIBM62325.2024.10822451)]
- **RLAIF 中医对齐** 通过AI反馈强化学习增强大语言模型的中医能力 [[论文](https://arxiv.org/abs/2411.00897)]
- [*Journal of the American Medical Informatics Association*] **LLM 腧穴定位关系抽取** 大语言模型关系抽取案例研究：腧穴定位知识 [[DOI](https://doi.org/10.1093/jamia/ocae233)]
- [*Frontiers in Artificial Intelligence*] **Evi-BERT** 中医RCT证据自动抽取的信息抽取模型开发与验证 [[DOI](https://doi.org/10.3389/frai.2024.1454945)]
- [*Scientific Reports*] **CPMI-ChatGLM** 中成药指令数据的 ChatGLM 参数高效微调模型 [[DOI](https://doi.org/10.1038/s41598-024-56874-w)]
- [*Digital Chinese Medicine*] **BSG 中医智能问答** 基于 BSG 深度学习模型的中医智能问答系统（方剂与中药实例） [[DOI](https://doi.org/10.1016/j.dcmed.2024.04.006)]
- [*Database (Oxford)*] **ACUBERT** 针灸适应证知识库的经络实体识别与分类模型 [[DOI](https://doi.org/10.1093/database/baae083)]
- **黄帝 (HuangDi)** 基于 Ziya-LLaMA-13B 的中医古籍知识问答大模型，预训练融合 22 本"十三五"中医教材与中医网站语料，古籍指令数据 SFT（图书馆论坛 2024 报道） [南京大学, 郑州大学] [[代码](https://github.com/Zlasejd/HuangDI)]
- [*IEEE BIBM*] **中医疫病防治问答模型** 基于大语言模型的中医疫病防治问答模型 [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385748)]
- [*IEEE BIBM*] **中医方剂 LLM 分类** 微调大语言模型并结合提示模板进行中医方剂分类，数据源自中成药国家医保目录等（IEEE BIBM 2023） [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385776)]
- [*IEEE Access*] **PreGenerator** 检索与生成方法结合的中医处方推荐模型 [[DOI](https://doi.org/10.1109/ACCESS.2023.3316219)]
- [*IEEE BIBM*] **LLM+GNN 中医处方推荐** 大语言模型与图神经网络结合的中医处方推荐模型 [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385489)]

## 通用中文医疗模型

- [*ACM Trans. Knowl. Discov. Data*] **本草[原名：华驼(HuaTuo)]** 基于中文医学知识的大语言模型指令微调 [哈尔滨工业大学] [[论文](https://arxiv.org/pdf/2309.04175.pdf)] [[代码](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)]
- **明医 (MING)** 中文医疗问诊大模型 MING，以稀疏 LoRA 混合专家（MING-MoE）增强医疗多任务学习能力（arXiv 2024） [上海交通大学] [[论文](https://arxiv.org/abs/2404.09027)] [[相关 MedCare](https://aclanthology.org/2024.findings-emnlp.619/)] [[代码](https://github.com/MediaBrain-SJTU/MING)]
- [*arXiv*] **扁鹊 (BianQue)** 中文领域生活空间主动健康大模型 [华南理工大学，广东省数字孪生人重点实验室] [[代码](https://github.com/scutcyr/BianQue)] [[论文](https://arxiv.org/abs/2310.15896)]
- **孙思邈 (Sunsimiao)** 孙思邈中文医疗大模型，Sunsimiao-7B 基于 Qwen2-7B 以高质量医疗数据微调，在 CMB-Exam 达 30B 量级 SOTA [华东理工大学] [[代码](https://github.com/X-D-Lab/Sunsimiao)]
- **启真医学大模型 (QiZhenGPT)** 中文医疗场景、药品知识问答、优化疾病、手术、检验等 [浙江大学] [[代码](https://github.com/CMKRG/QiZhenGPT)]
- [*EMNLP findings*] **华佗GPT** 中文医学语料训练的大型语言模型 [香港中文大学(深圳)，深圳市大数据研究院] [[DOI](https://doi.org/10.18653/v1/2023.findings-emnlp.725)] [[论文](https://aclanthology.org/2023.findings-emnlp.725/)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT)]
- **ChatMed** ChatMed 系列中文医疗大模型，含基于 50 万+ 在线问诊数据训练的 ChatMed-Consult [[代码](https://github.com/michael-wzhu/ChatMed)]

## Hugging Face 精选

- 杏核内经推理模型 [[模型](https://huggingface.co/zsyjsld/Xinghe1.2-9B)] [[GGUF](https://huggingface.co/zsyjsld/Xinghe1.2-9B-GGUF)]
- 知方丹台方剂生成模型 [[模型](https://huggingface.co/tczzx6/ZhiFangDanTai1.0)]
- 白泽中医大模型 [[模型](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model)] [[8B-16bit](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit)]
- MedChatZH [[medchatzh](https://huggingface.co/tyang816/medchatzh)]
- 仲景 [[ZhongjingGPT1_13B](https://huggingface.co/CMLM/ZhongjingGPT1_13B)] [[ZhongJing-2-1.8B](https://huggingface.co/CMLL/ZhongJing-2-1_8b)]
- TCMChat [[TCMChat-600k](https://huggingface.co/ZJUFanLab/TCMChat-600k)]
- ShizhenGPT 系列 [[7B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-LLM)] [[7B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-VL)] [[7B-Omni](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[32B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-LLM)] [[32B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-VL)]
- 神农 [[ShenNong-TCM-LLM](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]
- 灵丹 [[Lingdan-13B-Base](https://huggingface.co/TCMLLM/Lingdan-13B-Base)] [[Lingdan-13B-PR](https://huggingface.co/TCMLLM/Lingdan-13B-PR)]
- ChatTCM全参SFT版 [[模型](https://huggingface.co/SylvanL/ChatTCM-7B-SFT)]
- ChatTCM [[ChatTCM-7B-Pretrain](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)]
- 扁仓 (BianCang) 系列 [[Qwen2.5-7B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)] [[Qwen2.5-14B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-14B-Instruct)]

返回 [[Home]] · 分类法见 [[Taxonomy]]。
