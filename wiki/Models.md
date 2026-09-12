# Models

本页是 README [开源模型](../README.md#开源模型) 的展开版：先给选型原则，再给完整表。

## 怎么选

| 场景 | 优先看 |
| --- | --- |
| 本地推理 / 复现论文 | 开源权重 + 代码 + 配套数据 |
| 中医问诊对话 | **MedChatZH**（论文 + 权重 + 代码 + 问诊数据） |
| 舌诊 / 四诊 | 标签含 `multimodal` 的模型（如 ShizhenGPT、TongueVLM） |
| 问诊工作流 | `agent` 或配套 GraphRAG 系统，而不是单模型 |
| 当底座继续微调 | 同系列 Base / Instruct，以及通用中文医疗模型 |
| 只做对照实验 | 通用中文医疗栏（华佗、孙思邈等） |

中医专用 45 · 其中开源权重 12 · 通用医疗 30 · 闭源产品 4 · 日韩 1 · HF 精选 12。

## 开源权重

| 模型 | 年 | 机构 | 特色 | 链接 |
| --- | :---: | --- | --- | --- |
| **杏核 (Xinghe)** | 2026 | — | 推理 · 古籍 | [权重](https://huggingface.co/zsyjsld/Xinghe1.2-9B) · [数据](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2) |
| **知方丹台 (ZhiFangDanTai)** | 2025 | — | RAG · 图谱 | [论文](https://arxiv.org/abs/2509.05867) · [权重](https://huggingface.co/tczzx6/ZhiFangDanTai1.0) |
| **白泽 (Baize-TCM-LLM)** | 2025 | 中国中医科学院中药研究所 | 中国中医科学院中药研究所基于Qwen3的中医问答模型系列（0.6B/8B… | [权重](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model) · [数据](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3) |
| **扁仓 (BianCang)** | 2025 | 齐鲁工业大学 | 系列中医大模型（JBHI 正式发表）；2025.12 开源 14B 版本 | [论文](https://arxiv.org/abs/2411.11027) · [权重](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct) · [代码](https://github.com/QLU-NLP/BianCang) |
| **仲景 (ZhongJing)** | 2025 | 福耀科技大学 | 专家知识引导的中医大模型 ZhongJingGPT，融合垂直领域微调策略… | [论文](https://doi.org/10.26599/TST.2025.9010046) · [权重](https://huggingface.co/CMLM/ZhongjingGPT1_13B) · [代码](https://github.com/pariskang/CMLM-ZhongJing) |
| **ViTCM-LLM** | 2025 | Tsinghua Shenzhen International Graduate School | 多模态 · RAG | [论文](https://doi.org/10.1109/bibm66473.2025.11357113) · [权重](https://huggingface.co/Mark-CHAE/ViTCM-LLM) · [代码](https://github.com/jw-chae/ViTCM_LLM) |
| **TCMChat** | 2025 | 浙江大学 | 生成式中医药大模型，经预训练+监督微调构建，配套 60 万条中药知识对话… | [论文](https://doi.org/10.1016/j.phrs.2024.107530) · [权重](https://huggingface.co/ZJUFanLab/TCMChat-600k) · [代码](https://github.com/ZJUFanLab/TCMChat) · [数据](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k) |
| **ShizhenGPT** | 2025 | 香港中文大学(深圳)等 | 多模态 | [论文](https://arxiv.org/abs/2508.14706) · [权重](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni) · [代码](https://github.com/FreedomIntelligence/ShizhenGPT) |
| **ChatTCM** | 2025 | — | 从预训练数据到模型权重完全开源的中医大模型 | [权重](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain) |
| **TCMLLM / 灵丹 (Lingdan)** | 2024 | 北京交通大学 | 中医药大模型与处方推荐 | [论文](https://doi.org/10.1016/j.dcmed.2025.01.007) · [权重](https://huggingface.co/TCMLLM/Lingdan-13B-Base) · [代码](https://github.com/2020MEAI/TCMLLM) |
| **MedChatZH** | 2024 | 华东理工大学 | 面向中医问诊对话的微调大语言模型 MedChatZH，开源问诊数据集与模… | [论文](https://doi.org/10.1016/j.compbiomed.2024.108290) · [代码](https://github.com/tyang816/MedChatZH) · [权重](https://huggingface.co/tyang816/medchatzh) · [数据](https://huggingface.co/datasets/tyang816/MedChatZH) |
| **神农大模型 (ShenNong-TCM-LLM)** | 2023 | 华东师范大学 | 首个中医药大规模语言模型"神农"，配套 ShenNong_TCM_Dat… | [权重](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM) · [代码](https://github.com/michael-wzhu/ShenNong-TCM-LLM) · [数据](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset) |

## 论文或产品向（无公开权重）

- [*Digital Chinese Medicine*] **青囊 (QingNangTCM)** 参数高效微调的中医问答与临床推理模型，构建10万条**QnTCM_Dataset**语料 [河北北方学院] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.002)]
- [*ISCTIS 2026*] **舌面多模态融合智能诊断** 舌-面多模态特征融合+LLM驱动的中医智能诊断 [厦门理工学院] [[DOI](https://doi.org/10.1109/ISCTIS70043.2026.11572361)]
- **灵丹-V2 (Lingdan-V2)** 北交大灵丹二代中医推理家族（Qwen3 4B/8B/14B，CPT+SFT+处方GRPO）；ModelScope有权重但需申请，未标可自由下载 [北京交通大学] [[代码](https://github.com/TCMAI-BJTU/Lingdan-V2)] [[ModelScope](https://modelscope.cn/models/TCMAIBJTU/Lingdan-14B-R1)]
- [*JMIR Medical Informatics*] **TongueVLM** 中医舌诊多模态大模型，支持舌象描述生成与体质推理 [[论文](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- [*Digital Chinese Medicine*] **Qwen-TCM-Dia** 面向中医泄泻的专科微调模型（续训+CoT指令微调），覆盖症状→病机→治法→方药推理链 [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.003)]
- [*arXiv*] **Med-Shicheng（师承）** 基于天医 (Tianyi) 的轻量级名老中医经验传承框架，单模型内化5位国医大师知识系统、覆盖7类任务 [南京中医药大学等] [[论文](https://arxiv.org/abs/2603.23520)] [[代码](https://github.com/NJUCM-BJUCM-TCM-AI/Med-Shicheng)]
- [*Chinese Herbal Medicines*] **HerbWise** 面向传统草药（THM）的领域大模型，服务草药现代化与标准化 [成都中医药大学] [[DOI](https://doi.org/10.1016/j.chmed.2026.02.010)]
- [*Chinese Medicine*] **GastroTCM** 中医消化内科大模型，基于Llama3-8B微调并结合RAG与智能体框架 [[论文](https://link.springer.com/article/10.1186/s13020-025-01295-8)]
- [*arXiv*] **DongYuan** 中西医结合脾胃病诊断LLM框架，融合中医辨证与西医诊断推理 [[论文](https://arxiv.org/abs/2603.28191)]
- [*Chinese Medicine*] **DFGLM-TCM** 北京中医药大学东方医院与智谱等的中医临床系统，把通用中医知识与名医经验分模块建模后多任务协同；论文已发，权重未公开 [北京中医药大学，智谱华章] [[DOI](https://doi.org/10.1186/s13020-026-01512-y)]
- [*arXiv*] **智明堂 (ZMT-M1)** 中医大模型及TCM-Eval动态可扩展评测基准 [北京航空航天大学] [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- [*Chinese Medicine*] **悬壶 (XuanHuGPT)** 基于参数高效微调（PEFT）的中医领域大模型 [河北北方学院] [[DOI](https://doi.org/10.1186/s13020-025-01200-3)]
- [*Expert Systems with Applications*] **岐伯 (Qibo)** 天津大学等提出的中医大模型与Qibo Benchmark，持续预训练+SFT提升辨证与问答能力 [天津大学，天津中医药大学] [[正式发表](https://doi.org/10.1016/j.eswa.2025.127672)] [[论文](https://arxiv.org/abs/2403.16056)] [[DOI](https://doi.org/10.1016/j.eswa.2025.127672)]
- **女娲 (Nüwa / TCM-Nvwa)** 中医 LLM 训练流水线（持续预训练 + SFT + 奖励模型 + RLAIF），底座写明 Ziya-LLaMA-13B；仓库只给部分 pretrain/TCM-QR/reward 数据，无独立开源权重。GitHub 创建于 2025-04，与 2411.00897 作者不同，不要并条 [[代码](https://github.com/synbol/TCM-Nvwa)]
- [*arXiv*] **天惠 (TianHui)** 面向12类中医场景的领域LLM（DeepSeek-R1-Distill-Qwen-14B+PT/SFT），开源代码与评测脚本 [[论文](https://arxiv.org/abs/2509.19834)] [[代码](https://github.com/JYfantast/TianHui)]
- [*Information Fusion*] **天医 (Tianyi)** 南京中医药大学等提出约7B参数中医大模型，按读书—临证—跟师多阶段训练，配套TCMEval评测与真实世界验证 [南京中医药大学] [[正式发表](https://doi.org/10.1016/j.inffus.2025.103663)] [[论文](https://arxiv.org/abs/2505.13156)] [[新闻](https://blog.sciencenet.cn/blog-279293-1501581.html)]
- [*IEEE BIBM 2025*] **TCM-VisResolve (TCM-VR)** 基于Qwen2.5-VL的中医多模态大模型，支持163类22万张干药材图像识别与88万候选答案临床MCQ [中央民族大学] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356679)]
- [*APWeb-WAIM 2025*] **TCM-R1** 通过GRPO增强中医推理能力的大模型 [西南大学] [[论文](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*Computers in Biology and Medicine*] **TCM-KLLaMA** 知识图谱与大模型融合的中医方剂智能生成模型 [[DOI](https://doi.org/10.1016/j.compbiomed.2025.109887)]
- [*Chinese Medicine*] **TCM-DS** 药食同源食疗方智能推荐领域大模型 [澳门科技大学] [[DOI](https://doi.org/10.1186/s13020-025-01249-0)]
- [*arXiv*] **RACE-Align** 检索增强+CoT 式 DPO 的轻量中医对齐模型（Qwen3-1.7B），探索小模型对齐路线 [[arXiv](https://arxiv.org/abs/2506.02726)]
- [*IEEE ICIP 2025*] **MCM** 多智能体协同的中医多模态诊断框架（ICIP 2025） [上海计算机软件技术开发中心] [[代码](https://github.com/JerryMazeyu/MCM)] [[正式发表](https://doi.org/10.1109/icip55913.2025.11084334)]
- [*arXiv*] **Ladder-base (GRPO-TCM)** TCM-Ladder团队提出的首个GRPO强化学习对齐中医LLM [[论文](https://arxiv.org/abs/2510.17402)]
- [*arXiv*] **Hengqin-RA-v1** 类风湿关节炎中医诊疗大模型及配套数据集 [[论文](https://arxiv.org/abs/2501.02471)]
- [*Applied Sciences*] **Gen-SynDi** 知识引导的生成式AI框架，用于辨证与疾病诊断的双向教学 [College of Korean Medicine, Wonkwang University, Iksan 54538, Republic of Korea，College of Korean Medicine, Woosuk University, Jeon-Ju 54987, Republic of Korea，Dongje Medical Co., Ltd., Daegu 42187, Republic of Korea，College of Medicine, Yeungnam University, Daegu 42415, Republic of Korea] [[DOI](https://doi.org/10.3390/app15094862)]
- [*arXiv*] **DoPI** 类医生主动问诊中医大模型，引导模型+专家模型协同架构，问诊准确率84.68% [[论文](https://arxiv.org/abs/2507.04877)]
- [*IEEE BIBM 2025*] **ChatGLM-FGIDs-TCM** 知识融合的ChatGLM中医临床决策支持模型，面向功能性胃肠病（FGIDs） [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356283)]
- [*arXiv*] **BenCao（指令微调本草助手）** 基于ChatGPT自然语言指令对齐的中医多模态助手，对接舌象API与知识库，部署于GPTs Store（区别于华驼/本草） [[论文](https://arxiv.org/abs/2510.17415)]
- **大数中医 (BigDataTCM)** 河南工业大学复杂性科学研究院与阿帕斯联合研发的中医垂直领域大模型（34B），提供医疗问答、诊断支持与中医知识服务 [河南工业大学] [[代码](https://github.com/HAUT-CS/BigDataTCM)]
- [*AAAI*] **仲景（CMtMedQA 线，Yang et al.）** 与 Kang 系 ZhongJingGPT 同名不同源的中医大模型：Ziya-LLaMA-13B 全流程 CPT+SFT+RLHF，基于约 7 万条真实多轮医患对话 CMtMedQA（AAAI 2024；注意与 Tsinghua Sci Technol 的 ZhongJingGPT 无作者与工件交集） [华东师范大学等] [[论文](https://doi.org/10.1609/aaai.v38i17.29907)] [[arXiv](https://arxiv.org/abs/2308.03549)]
- [*Computer Methods and Programs in Biomedicine Update*] **TCM-GPT** 面向中医领域自适应的高效预训练大模型 [[DOI](https://doi.org/10.1016/j.cmpbup.2024.100158)] [[论文](https://arxiv.org/abs/2311.01786)]
- [*Scientific Reports*] **CPMI-ChatGLM** 中成药指令数据的 ChatGLM 参数高效微调模型 [[DOI](https://doi.org/10.1038/s41598-024-56874-w)]
- **黄帝 (HuangDi)** 基于 Ziya-LLaMA-13B 的中医古籍知识问答大模型，预训练融合 22 本"十三五"中医教材与中医网站语料，古籍指令数据 SFT（图书馆论坛 2024 报道） [南京大学, 郑州大学] [[代码](https://github.com/Zlasejd/HuangDI)]

## 通用中文医疗模型

- [*arXiv*] **百川-M3 (Baichuan-M3)** 百川第三代开源医疗推理模型（235B，底座Qwen3），用SPAR分段RL与事实感知RL做主动问诊和抑幻觉；HealthBench与SCAN-bench开源前列 [百川智能] [[论文](https://arxiv.org/abs/2602.06570)] [[代码](https://github.com/baichuan-inc/Baichuan-M3-235B)] [[模型](https://huggingface.co/baichuan-inc/Baichuan-M3-235B)]
- [*arXiv*] **百川-M2 (Baichuan-M2)** 百川第二代开源医疗推理模型（32B，底座Qwen2.5-32B），用大规模验证器与多阶段RL做临床对话对齐，HealthBench开源前列 [百川智能] [[论文](https://arxiv.org/abs/2509.02208)] [[代码](https://github.com/baichuan-inc/Baichuan-M2-32B)] [[模型](https://huggingface.co/baichuan-inc/Baichuan-M2-32B)]
- [*arXiv*] **百川-M1 (Baichuan-M1)** 百川智能从零训练的开源医疗大模型（14B），约20万亿token医疗+通用数据，覆盖20+科室；常被后续中医微调当作底座 [百川智能] [[论文](https://arxiv.org/abs/2502.12671)] [[代码](https://github.com/baichuan-inc/Baichuan-M1-14B)] [[模型](https://huggingface.co/baichuan-inc/Baichuan-M1-14B-Instruct)] [[Base](https://huggingface.co/baichuan-inc/Baichuan-M1-14B-Base)]
- [*Journal of the American Medical Informatics Association*] **太一2 (Taiyi-2)** 太一二代开源生物医学模型，底座从Qwen-7B换成GLM4-9B，重做数据过滤与任务指令；官方推荐替换Taiyi-1 [大连理工大学] [[模型](https://huggingface.co/DUTIR-BioNLP/Taiyi2-chat)] [[代码](https://github.com/DUTIR-BioNLP/Taiyi-LLM)] [[DOI](https://doi.org/10.1093/jamia/ocae037)]
- [*arXiv*] **卫宁WiNGPT3** 卫宁第三代医疗推理模型（32B，底座Qwen2.5），多阶段SFT+RL与长思维链，对接WiNEX医院流程；技术报告和代码已公开，权重未核验可下载 [卫宁健康] [[论文](https://arxiv.org/abs/2505.17387)] [[代码](https://github.com/winninghealth/WiNGPT3)]
- [*ACM Trans. Knowl. Discov. Data*] **本草[原名：华驼(HuaTuo)]** 基于中文医学知识的大语言模型指令微调 [哈尔滨工业大学] [[论文](https://arxiv.org/pdf/2309.04175.pdf)] [[代码](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)]
- [*arXiv*] **明医 (MING)** 中文医疗问诊大模型 MING，以稀疏 LoRA 混合专家（MING-MoE）增强医疗多任务学习能力（arXiv 2024） [上海交通大学] [[论文](https://arxiv.org/abs/2404.09027)] [[相关 MedCare](https://aclanthology.org/2024.findings-emnlp.619/)] [[代码](https://github.com/MediaBrain-SJTU/MING)]
- [*JAMIA*] **太一 (Taiyi)** 大连理工DUTIR的中英双语生物医学大模型，底座Qwen-7B，覆盖问答、医患对话、报告生成与信息抽取等 [大连理工大学] [[DOI](https://doi.org/10.1093/jamia/ocae037)] [[代码](https://github.com/DUTIR-BioNLP/Taiyi-LLM)] [[模型](https://huggingface.co/DUTIR-BioNLP/Taiyi-LLM)]
- [*arXiv*] **华佗GPT-o1 (HuatuoGPT-o1)** 华佗系列医疗复杂推理模型，用可验证医题+医学验证器做搜索微调与强化学习；7B/72B支持中英 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2412.18925)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-o1)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-7B)]
- [*arXiv*] **华佗GPT-Vision (HuatuoGPT-Vision)** 华佗系列医学多模态模型，大规模注入医学视觉知识，常作中文医学影像/多模态对照 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2406.19280)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-Vision)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B-Qwen2.5VL)]
- [*arXiv*] **Apollo** 中大深圳FreedomIntelligence的多语种医疗LLM（含中文），配套ApolloCorpus与XMedBench [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2403.03640)] [[代码](https://github.com/FreedomIntelligence/Apollo)] [[模型](https://huggingface.co/FreedomIntelligence/Apollo-7B)]
- [*arXiv*] **麒麟-Med (Qilin-Med)** 多阶段知识注入的中文医疗LLM（CPT+SFT+DPO，底座Baichuan-7B），发布约3GB ChiMed语料，可再加RAG [[论文](https://arxiv.org/abs/2310.09089)] [[代码](https://github.com/williamliujl/Qilin-Med)] [[数据集](https://huggingface.co/datasets/williamliu/ChiMed)]
- **扁鹊-2 (BianQue-2)** 扁鹊二代开源医疗问诊模型，强化多轮追问；CMB 等中文医疗评测里的常见对照 [华南理工大学，广东省数字孪生人重点实验室] [[代码](https://github.com/scutcyr/BianQue)] [[模型](https://huggingface.co/scutcyr/BianQue-2)]
- [*arXiv*] **扁鹊 (BianQue)** 中文领域生活空间主动健康大模型 [华南理工大学，广东省数字孪生人重点实验室] [[代码](https://github.com/scutcyr/BianQue)] [[论文](https://arxiv.org/abs/2310.15896)]
- **孙思邈 (Sunsimiao)** 孙思邈中文医疗大模型，Sunsimiao-7B 基于 Qwen2-7B 以高质量医疗数据微调，在 CMB-Exam 达 30B 量级 SOTA [华东理工大学] [[代码](https://github.com/X-D-Lab/Sunsimiao)]
- **启真医学大模型 (QiZhenGPT)** 中文医疗场景、药品知识问答、优化疾病、手术、检验等 [浙江大学] [[代码](https://github.com/CMKRG/QiZhenGPT)]
- **卫宁WiNGPT2** 卫宁健康开源医疗大模型，底座Qwen，覆盖医学问答、病历理解和多轮问诊，7B/14B可下载 [卫宁健康] [[模型](https://huggingface.co/winninghealth/WiNGPT2-14B-Chat)] [[7B](https://huggingface.co/winninghealth/WiNGPT2-7B-Chat)]
- [*arXiv*] **华佗GPT-II (HuatuoGPT-II)** 中大深圳华佗系列二代，单阶段领域适配；7B/13B以Baichuan2为底座，是中文医疗评测里最常见的开源对照之一 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2311.09774)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-II)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT2-7B)]
- [*EMNLP findings*] **华佗GPT** 中文医学语料训练的大型语言模型 [香港中文大学(深圳)，深圳市大数据研究院] [[DOI](https://doi.org/10.18653/v1/2023.findings-emnlp.725)] [[论文](https://aclanthology.org/2023.findings-emnlp.725/)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT)]
- [*arXiv*] **SoulChat** 华南理工数字孪生人实验室的心理健康对话大模型，与扁鹊同系列，常作中文医疗/健康对话对照 [华南理工大学，广东省数字孪生人重点实验室] [[论文](https://arxiv.org/abs/2311.00273)] [[代码](https://github.com/scutcyr/SoulChat)] [[模型](https://huggingface.co/scutcyr/SoulChat)]
- **PULSE** 上海AI Lab OpenMEDLab的中文医疗大模型（Bloom 7B/14B），覆盖医考、报告解读、病历结构化与模拟诊疗 [上海人工智能实验室] [[代码](https://github.com/openmedlab/PULSE)] [[模型](https://huggingface.co/OpenMEDLab/PULSE-7bv5)]
- **MedicalGPT** 开源中文医疗LLM训练框架（预训练/SFT/RLHF/DPO），也被大量中医微调实验当作基线实现 [[代码](https://github.com/shibing624/MedicalGPT)]
- [*arXiv*] **IvyGPT** 基于 LLaMA 的中文医疗问答模型，用高质量医患 QA 与 RLHF 微调，CMB 论文对照列表中的开源基线 [[论文](https://arxiv.org/abs/2307.10512)] [[代码](https://github.com/Ivy0529/IvyGPT)]
- [*arXiv*] **DoctorGLM** 基于ChatGLM-6B的早期开源中文问诊模型，用多科室医患数据做LoRA/P-Tuning，常出现在2023年中文医疗对照表 [[论文](https://arxiv.org/abs/2304.01097)] [[代码](https://github.com/xionghonglin/DoctorGLM)]
- [*arXiv*] **DISC-MedLLM** 复旦DISC实验室的医疗对话大模型，底座Baichuan-13B，配套DISC-Med-SFT；知识图谱+真实问诊重构 [复旦大学] [[论文](https://arxiv.org/abs/2308.14346)] [[代码](https://github.com/FudanDISC/DISC-MedLLM)] [[模型](https://huggingface.co/Flmc/DISC-MedLLM)] [[数据集](https://huggingface.co/datasets/Flmc/DISC-Med-SFT)]
- [*arXiv*] **ClinicalGPT** 北邮等用病历、知识、医考和多轮问诊微调的临床向中文医疗模型（BLOOM-7B），CMB等对照表常见；HF有medicalai快照 [北京邮电大学] [[论文](https://arxiv.org/abs/2306.09968)] [[模型](https://huggingface.co/medicalai/ClinicalGPT-base-zh)]
- [*arXiv*] **ChiMed-GPT** 中科大等在Ziya-v2上做继续预训练+SFT+RLHF的中文医疗大模型，覆盖抽取、问答与多轮对话 [中国科学技术大学] [[论文](https://arxiv.org/abs/2311.06025)] [[代码](https://github.com/synlp/ChiMed-GPT)] [[模型](https://huggingface.co/SYNLP/ChiMed-GPT-1.0)]
- **ChatMed** ChatMed 系列中文医疗大模型，含基于 50 万+ 在线问诊数据训练的 ChatMed-Consult [[代码](https://github.com/michael-wzhu/ChatMed)]
- **ChatGLM-Med** 哈工大SCIR用中文医学知识图谱指令微调的ChatGLM-6B，与本草/华驼同源数据，CMB常用对照 [哈尔滨工业大学] [[代码](https://github.com/SCIR-HI/Med-ChatGLM)]
- **CareGPT** 开源中文医疗LLM全流程训练框架（预训练到DPO）与配套权重，常被复现中文医疗微调 [[代码](https://github.com/WangRongsheng/CareGPT)]

## 闭源中文医疗产品

- **讯飞星火医疗** 科大讯飞闭源医疗大模型（星火医疗X1/X2），落地智医助理与讯飞晓医；无公开权重，只作产业对照 [科大讯飞] [[官网](https://www.xunfeihealthcare.com/)] [[新闻](https://www.cn-healthcare.com/article/20250303/wap-content-585822.html)]
- **蚂蚁阿福 / 蚂蚁医疗大模型** 蚂蚁闭源多模态医疗大模型，先作支付宝AQ后升级为阿福，做问诊、报告与药盒识别；WAIC 2024发布，无公开权重 [蚂蚁集团] [[官网](https://www.antafu.com/)] [[新闻稿](https://www.antgroup.com/news-media/press-releases/1720166400000)]
- **腾讯混元医疗** 腾讯健康基于混元的闭源医疗大模型，覆盖问答、导诊、病历与影像；天衍实验室发布，无公开权重 [腾讯] [[官网](https://healthcare.tencent.com/)] [[新闻](https://healthcare.tencent.com/news/1603)]
- [*Sci China Life Sci*] **盘古药物分子大模型 (PanGu Drug Model)** 华为云与中科院上海药物所的闭源分子预训练模型（约17亿小分子），做属性预测/生成/优化；数智本草曾以其为底座之一 [华为云，中国科学院上海药物研究所] [[DOI](https://doi.org/10.1007/s11427-022-2239-y)] [[官网](https://www.huaweicloud.com/cases/pgyw.html)]

## 日韩汉方 / 韩医

- **KAMPO LLM** 日本VARYTEX与日本东洋医学会合作的闭源汉方医学API，用漢方専門医研修471题评测；无公开权重 [VARYTEX] [[官网](https://kampollm.varytex.co.jp/)]

## Hugging Face 精选

- **杏核内经推理模型** [[模型](https://huggingface.co/zsyjsld/Xinghe1.2-9B)] [[GGUF](https://huggingface.co/zsyjsld/Xinghe1.2-9B-GGUF)]
- **知方丹台方剂生成模型** [[模型](https://huggingface.co/tczzx6/ZhiFangDanTai1.0)]
- **白泽中医大模型** [[模型](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model)] [[8B-16bit](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit)]
- **MedChatZH** [[medchatzh](https://huggingface.co/tyang816/medchatzh)]
- **仲景** [[ZhongjingGPT1_13B](https://huggingface.co/CMLM/ZhongjingGPT1_13B)] [[ZhongJing-2-1.8B](https://huggingface.co/CMLL/ZhongJing-2-1_8b)]
- **TCMChat** [[TCMChat-600k](https://huggingface.co/ZJUFanLab/TCMChat-600k)]
- **ShizhenGPT 系列** [[7B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-LLM)] [[7B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-VL)] [[7B-Omni](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[32B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-LLM)] [[32B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-VL)]
- **神农** [[ShenNong-TCM-LLM](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]
- **灵丹** [[Lingdan-13B-Base](https://huggingface.co/TCMLLM/Lingdan-13B-Base)] [[Lingdan-13B-PR](https://huggingface.co/TCMLLM/Lingdan-13B-PR)]
- **ChatTCM全参SFT版** [[模型](https://huggingface.co/SylvanL/ChatTCM-7B-SFT)]
- **ChatTCM** [[ChatTCM-7B-Pretrain](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)]
- **扁仓 (BianCang) 系列** [[Qwen2.5-7B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)] [[Qwen2.5-14B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-14B-Instruct)]

返回 [[Home]] · 分类法见 [[Taxonomy]]。
