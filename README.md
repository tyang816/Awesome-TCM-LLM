# 🔥 开源中医模型、数据、论文、专利

**语言 / Language:** [中文](README.md) | [English](README_EN.md)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  ![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork) [![中文门户](https://img.shields.io/badge/中医资源-门户-blue)](https://tyang816.github.io/zh/projects/tcm/) [![Project](https://img.shields.io/badge/Project-tyang816.github.io-informational)](https://tyang816.github.io/projects/tcm/)

开源中医模型、数据、论文、专利精选，也带一点相关中文医疗。现在大概有 29 条新闻、92 个模型、47 篇综述、22 件专利、85 个数据集、157 篇方法论文。[欢迎补条目](CONTRIBUTING.md)。

[项目页](https://tyang816.github.io/projects/tcm/) · [中文项目页](https://tyang816.github.io/zh/projects/tcm/) · [Wiki](wiki/Home.md) · [主页](https://tyang816.github.io/zh/)

## 先看这里

真能下载复现的中医权重大概 12 个，都在[开源模型](#开源模型)里。新闻里医院、公司发的，多数没有公开权重，当不了实验底座。

2025 年以后，多模态、Agent 和评测明显变多；再单独训一个 7B 问答，往往不够。执业考试分数测的是回忆，不能当成辨证或临床能力——要比的话看 TCM-Ladder、LingLan、MTCMB。

| 你想做什么 | 可以先看 | 备注 |
| --- | --- | --- |
| 本机跑通一个模型 | **[扁仓 (BianCang)](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)**、**[仲景 (ZhongJing)](https://huggingface.co/CMLM/ZhongjingGPT1_13B)** | 论文、权重、代码都有 |
| 做中医问诊 | **[MedChatZH](https://github.com/tyang816/MedChatZH)** | 还有配套问诊数据 |
| 舌诊、四诊 | **[ShizhenGPT](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)** | 多模态，数据和权重都开 |
| 自己接着训 | **[ChatTCM](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)**、**[神农大模型 (ShenNong-TCM-LLM)](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)** | 预训练或指令数据是公开的 |
| 电脑比较一般 | **[杏核 (Xinghe)](https://huggingface.co/zsyjsld/Xinghe1.2-9B)** | 9B，有 GGUF |
| 做对比实验 | **[TCM-Ladder](https://arxiv.org/abs/2505.24063)**、**[灵兰秘典 (LingLan)](https://arxiv.org/abs/2602.01779)** | 任务说得比较清楚；更多在[数据集](#数据集) |
| 写相关工作 | 近两年的 scoping review | 先翻[综述](#综述)，别从单篇模型论文起 |

同名不一定是同一个东西。「仲景」至少有 ZhongJingGPT 和 AAAI 那条 CMtMedQA；TCM-Eval 也不止一套。说不清时看 [Getting Started](wiki/Getting-Started.md)。

## 开源模型

上面是起步用的。要翻全部能下的权重，或只有论文/产品、通用中文医疗底座、闭源产品和日韩汉方/韩医，点开即可。

<details>
<summary>能下载的权重，共 12 个</summary>

| 模型 | 年 | 机构 | 特色 | 链接 |
| --- | :---: | --- | --- | --- |
| **杏核 (Xinghe)** | 2026 | Xinghe-TCM | 推理 · 古籍 | [权重](https://huggingface.co/zsyjsld/Xinghe1.2-9B) · [数据](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2) |
| **知方丹台 (ZhiFangDanTai)** | 2025 | 首都师范大学 | RAG · 图谱 | [论文](https://arxiv.org/abs/2509.05867) · [权重](https://huggingface.co/tczzx6/ZhiFangDanTai1.0) · [数据](https://huggingface.co/datasets/tczzx6/ZhiFangDanTai1.0) |
| **白泽 (Baize-TCM-LLM)** | 2025 | 中国中医科学院中药研究所 | 中国中医科学院中药研究所基于Qwen3的中医问答模型系列（0.6B/8B… | [权重](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model) · [数据](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3) |
| **扁仓 (BianCang)** | 2025 | 齐鲁工业大学 | 系列中医大模型（JBHI 正式发表）；2025.12 开源 14B 版本 | [论文](https://arxiv.org/abs/2411.11027) · [权重](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct) · [代码](https://github.com/QLU-NLP/BianCang) |
| **仲景 (ZhongJing)** | 2025 | 福耀科技大学 | 专家知识引导的中医大模型 ZhongJingGPT，融合垂直领域微调策略… | [论文](https://doi.org/10.26599/TST.2025.9010046) · [权重](https://huggingface.co/CMLM/ZhongjingGPT1_13B) · [代码](https://github.com/pariskang/CMLM-ZhongJing) |
| **ViTCM-LLM** | 2025 | Tsinghua Shenzhen International Graduate School | 多模态 · RAG | [论文](https://doi.org/10.1109/bibm66473.2025.11357113) · [权重](https://huggingface.co/Mark-CHAE/ViTCM-LLM) · [代码](https://github.com/jw-chae/ViTCM_LLM) |
| **TCMChat** | 2025 | 浙江大学 | 生成式中医药大模型，经预训练+监督微调构建，配套 60 万条中药知识对话… | [论文](https://doi.org/10.1016/j.phrs.2024.107530) · [权重](https://huggingface.co/ZJUFanLab/TCMChat-600k) · [代码](https://github.com/ZJUFanLab/TCMChat) · [数据](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k) |
| **ShizhenGPT** | 2025 | 香港中文大学(深圳)等 | 多模态 | [论文](https://arxiv.org/abs/2508.14706) · [权重](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni) · [代码](https://github.com/FreedomIntelligence/ShizhenGPT) |
| **ChatTCM** | 2025 | — | HF 用户 SylvanL 开源的中医 LLM：Qwen2-7B 继续预… | [权重](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain) |
| **TCMLLM / 灵丹 (Lingdan)** | 2024 | 北京交通大学 | 中医药大模型与处方推荐 | [论文](https://doi.org/10.1016/j.dcmed.2025.01.007) · [权重](https://huggingface.co/TCMLLM/Lingdan-13B-Base) · [代码](https://github.com/2020MEAI/TCMLLM) |
| **MedChatZH** | 2024 | 华东理工大学 | 面向中医问诊对话的微调大语言模型 MedChatZH，开源问诊数据集与模… | [论文](https://doi.org/10.1016/j.compbiomed.2024.108290) · [代码](https://github.com/tyang816/MedChatZH) · [权重](https://huggingface.co/tyang816/medchatzh) · [数据](https://huggingface.co/datasets/tyang816/MedChatZH) |
| **神农大模型 (ShenNong-TCM-LLM)** | 2023 | 华东师范大学 | 首个中医药大规模语言模型"神农"，配套 ShenNong_TCM_Dat… | [权重](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM) · [代码](https://github.com/michael-wzhu/ShenNong-TCM-LLM) · [数据](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset) |

</details>

<details>
<summary>只有论文或产品、没有核验权重的（33）</summary>

<details>
<summary>2026 · 10</summary>

- [*Digital Chinese Medicine*] **青囊 (QingNangTCM)** 参数高效微调的中医问答与临床推理模型，构建10万条**QnTCM_Dataset**语料 [河北北方学院] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.002)]
- [*ISCTIS 2026*] **舌面多模态融合智能诊断** 舌-面多模态特征融合+LLM驱动的中医智能诊断 [厦门理工学院] [[DOI](https://doi.org/10.1109/ISCTIS70043.2026.11572361)]
- **灵丹-V2 (Lingdan-V2)** 北交大灵丹二代中医推理家族（Qwen3 4B/8B/14B，CPT+SFT+处方GRPO）；ModelScope有权重但需申请，未标可自由下载 [北京交通大学] [[代码](https://github.com/TCMAI-BJTU/Lingdan-V2)] [[ModelScope](https://modelscope.cn/models/TCMAIBJTU/Lingdan-14B-R1)]
- [*JMIR Medical Informatics*] **TongueVLM** 中医舌诊多模态大模型，支持舌象描述生成与体质推理。JMIR 页被拦截，OpenAlex 记录作者单位为合肥工业大学与安徽中医药大学等 [合肥工业大学，安徽中医药大学等] [[论文](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- [*Digital Chinese Medicine*] **Qwen-TCM-Dia** 面向中医泄泻的专科微调模型（续训+CoT指令微调），覆盖症状→病机→治法→方药推理链。Digital Chinese Medicine 署名首都医科大学附属北京中医医院与北京中医药大学等 [首都医科大学附属北京中医医院，北京中医药大学等] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.003)]
- [*arXiv*] **Med-Shicheng（师承）** 基于天医 (Tianyi) 的轻量级名老中医经验传承框架，单模型内化5位国医大师知识系统、覆盖7类任务 [南京中医药大学等] [[论文](https://arxiv.org/abs/2603.23520)] [[代码](https://github.com/NJUCM-BJUCM-TCM-AI/Med-Shicheng)]
- [*Chinese Herbal Medicines*] **HerbWise** 面向传统草药（THM）的领域大模型，服务草药现代化与标准化 [成都中医药大学] [[DOI](https://doi.org/10.1016/j.chmed.2026.02.010)]
- [*Chinese Medicine*] **GastroTCM** 中医消化内科大模型，基于Llama3-8B微调并结合RAG与智能体框架。Chinese Medicine 论文署名清华大学 TCM-X 与中日友好医院等 [清华大学，中日友好医院等] [[论文](https://link.springer.com/article/10.1186/s13020-025-01295-8)]
- [*arXiv*] **DongYuan** 中西医结合脾胃病诊断LLM框架，融合中医辨证与西医诊断推理。arXiv PDF 署名河北省中医院、中科院自动化所、中科闻歌与天津大学 [河北省中医院，中国科学院自动化研究所等] [[论文](https://arxiv.org/abs/2603.28191)]
- [*Chinese Medicine*] **DFGLM-TCM** 北京中医药大学东方医院与智谱等的中医临床系统，把通用中医知识与名医经验分模块建模后多任务协同；论文已发，权重未公开 [北京中医药大学，智谱华章] [[DOI](https://doi.org/10.1186/s13020-026-01512-y)]

</details>

<details>
<summary>2025 · 18</summary>

- [*arXiv*] **智明堂 (ZMT-M1)** 中医大模型及TCM-Eval动态可扩展评测基准 [北京航空航天大学] [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- [*Chinese Medicine*] **悬壶 (XuanHuGPT)** 基于参数高效微调（PEFT）的中医领域大模型 [河北北方学院] [[DOI](https://doi.org/10.1186/s13020-025-01200-3)]
- [*Expert Systems with Applications*] **岐伯 (Qibo)** 天津大学等提出的中医大模型与Qibo Benchmark，持续预训练+SFT提升辨证与问答能力 [天津大学，天津中医药大学] [[正式发表](https://doi.org/10.1016/j.eswa.2025.127672)] [[论文](https://arxiv.org/abs/2403.16056)] [[DOI](https://doi.org/10.1016/j.eswa.2025.127672)]
- **女娲 (Nüwa / TCM-Nvwa)** 中医 LLM 训练流水线（持续预训练 + SFT + 奖励模型 + RLAIF），底座写明 Ziya-LLaMA-13B；仓库只给部分 pretrain/TCM-QR/reward 数据，无独立开源权重。GitHub 创建于 2025-04，与 2411.00897 作者不同，不要并条 [[代码](https://github.com/synbol/TCM-Nvwa)]
- [*arXiv*] **天惠 (TianHui)** 面向12类中医场景的领域LLM（DeepSeek-R1-Distill-Qwen-14B+PT/SFT），开源代码与评测脚本。arXiv PDF 署名成都中医药大学智能医学院 [成都中医药大学] [[论文](https://arxiv.org/abs/2509.19834)] [[代码](https://github.com/JYfantast/TianHui)]
- [*Information Fusion*] **天医 (Tianyi)** 南京中医药大学等提出约7B参数中医大模型，按读书—临证—跟师多阶段训练，配套TCMEval评测与真实世界验证 [南京中医药大学] [[正式发表](https://doi.org/10.1016/j.inffus.2025.103663)] [[论文](https://arxiv.org/abs/2505.13156)] [[新闻](https://blog.sciencenet.cn/blog-279293-1501581.html)]
- [*IEEE BIBM 2025*] **TCM-VisResolve (TCM-VR)** 基于Qwen2.5-VL的中医多模态大模型，支持163类22万张干药材图像识别与88万候选答案临床MCQ [中央民族大学] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356679)]
- [*APWeb-WAIM 2025*] **TCM-R1** 通过GRPO增强中医推理能力的大模型 [西南大学] [[论文](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*Computers in Biology and Medicine*] **TCM-KLLaMA** 知识图谱与大模型融合的中医方剂智能生成模型。PubMed 40056842 署名浙江工商大学与西湖大学医学院附属杭州市第一人民医院 [浙江工商大学，西湖大学医学院附属杭州市第一人民医院] [[DOI](https://doi.org/10.1016/j.compbiomed.2025.109887)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/40056842)]
- [*Chinese Medicine*] **TCM-DS** 药食同源食疗方智能推荐领域大模型 [澳门科技大学] [[DOI](https://doi.org/10.1186/s13020-025-01249-0)]
- [*arXiv*] **RACE-Align** 检索增强+CoT 式 DPO 的轻量中医对齐模型（Qwen3-1.7B），探索小模型对齐路线。arXiv PDF 署名上海科技大学、河南大学与辽宁中医药大学 [上海科技大学，河南大学，辽宁中医药大学] [[arXiv](https://arxiv.org/abs/2506.02726)]
- [*IEEE ICIP 2025*] **MCM** 多智能体协同的中医多模态诊断框架（ICIP 2025） [上海计算机软件技术开发中心] [[代码](https://github.com/JerryMazeyu/MCM)] [[正式发表](https://doi.org/10.1109/icip55913.2025.11084334)]
- [*arXiv*] **Ladder-base (GRPO-TCM)** TCM-Ladder团队提出的首个GRPO强化学习对齐中医LLM。arXiv PDF 署名密苏里大学与上海中医药大学等 [密苏里大学，上海中医药大学等] [[论文](https://arxiv.org/abs/2510.17402)]
- [*arXiv*] **Hengqin-RA-v1** 类风湿关节炎中医诊疗大模型及配套数据集。arXiv/DOI 页署名中医广东省实验室与南方科技大学 [中医广东省实验室，南方科技大学] [[论文](https://arxiv.org/abs/2501.02471)]
- [*Applied Sciences*] **Gen-SynDi** 知识引导的生成式AI框架，用于辨证与疾病诊断的双向教学 [College of Korean Medicine, Wonkwang University, Iksan 54538, Republic of Korea，College of Korean Medicine, Woosuk University, Jeon-Ju 54987, Republic of Korea，Dongje Medical Co., Ltd., Daegu 42187, Republic of Korea，College of Medicine, Yeungnam University, Daegu 42415, Republic of Korea] [[DOI](https://doi.org/10.3390/app15094862)]
- [*arXiv*] **DoPI** 类医生主动问诊中医大模型，引导模型+专家模型协同架构，问诊准确率84.68%。arXiv HTML 署名天津大学、香港中文大学与中国电科 [天津大学，香港中文大学等] [[论文](https://arxiv.org/abs/2507.04877)]
- [*IEEE BIBM 2025*] **ChatGLM-FGIDs-TCM** 知识融合的ChatGLM中医临床决策支持模型，面向功能性胃肠病（FGIDs） [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356283)]
- [*arXiv*] **BenCao（指令微调本草助手）** 基于ChatGPT自然语言指令对齐的中医多模态助手，对接舌象API与知识库，部署于GPTs Store（区别于华驼/本草）。arXiv HTML 署名密苏里大学与上海中医药大学等 [密苏里大学，上海中医药大学等] [[论文](https://arxiv.org/abs/2510.17415)]

</details>

<details>
<summary>2024 · 4</summary>

- **大数中医 (BigDataTCM)** 河南工业大学复杂性科学研究院与阿帕斯联合研发的中医垂直领域大模型（34B），提供医疗问答、诊断支持与中医知识服务 [河南工业大学] [[代码](https://github.com/HAUT-CS/BigDataTCM)]
- [*AAAI*] **仲景（CMtMedQA 线，Yang et al.）** 与 Kang 系 ZhongJingGPT 同名不同源的中医大模型：Ziya-LLaMA-13B 全流程 CPT+SFT+RLHF，基于约 7 万条真实多轮医患对话 CMtMedQA（AAAI 2024；注意与 Tsinghua Sci Technol 的 ZhongJingGPT 无作者与工件交集） [华东师范大学等] [[论文](https://doi.org/10.1609/aaai.v38i17.29907)] [[arXiv](https://arxiv.org/abs/2308.03549)]
- [*Computer Methods and Programs in Biomedicine Update*] **TCM-GPT** 面向中医领域自适应的高效预训练大模型。期刊元数据署名北京邮电大学与伦敦大学学院 [北京邮电大学，伦敦大学学院] [[DOI](https://doi.org/10.1016/j.cmpbup.2024.100158)] [[论文](https://arxiv.org/abs/2311.01786)]
- [*Scientific Reports*] **CPMI-ChatGLM** 中成药指令数据的 ChatGLM 参数高效微调模型。OpenAlex/期刊单位为安徽中医药大学与中国中医科学院安徽中医药计算机应用研究所 [安徽中医药大学，中国中医科学院安徽中医药计算机应用研究所] [[DOI](https://doi.org/10.1038/s41598-024-56874-w)]

</details>

<details>
<summary>2023 · 1</summary>

- **黄帝 (HuangDi)** 基于 Ziya-LLaMA-13B 的中医古籍知识问答大模型，预训练融合 22 本"十三五"中医教材与中医网站语料，古籍指令数据 SFT（图书馆论坛 2024 报道） [南京大学, 郑州大学] [[代码](https://github.com/Zlasejd/HuangDI)]

</details>


</details>

<details>
<summary>通用中文医疗模型，常当底座或对照（30）</summary>

<details>
<summary>2026 · 1</summary>

- [*arXiv*] **百川-M3 (Baichuan-M3)** 百川第三代开源医疗推理模型（235B，底座Qwen3），用SPAR分段RL与事实感知RL做主动问诊和抑幻觉；HealthBench与SCAN-bench开源前列 [百川智能] [[论文](https://arxiv.org/abs/2602.06570)] [[代码](https://github.com/baichuan-inc/Baichuan-M3-235B)] [[模型](https://huggingface.co/baichuan-inc/Baichuan-M3-235B)]

</details>

<details>
<summary>2025 · 4</summary>

- [*arXiv*] **百川-M2 (Baichuan-M2)** 百川第二代开源医疗推理模型（32B，底座Qwen2.5-32B），用大规模验证器与多阶段RL做临床对话对齐，HealthBench开源前列 [百川智能] [[论文](https://arxiv.org/abs/2509.02208)] [[代码](https://github.com/baichuan-inc/Baichuan-M2-32B)] [[模型](https://huggingface.co/baichuan-inc/Baichuan-M2-32B)]
- [*arXiv*] **百川-M1 (Baichuan-M1)** 百川智能从零训练的开源医疗大模型（14B），约20万亿token医疗+通用数据，覆盖20+科室；常被后续中医微调当作底座 [百川智能] [[论文](https://arxiv.org/abs/2502.12671)] [[代码](https://github.com/baichuan-inc/Baichuan-M1-14B)] [[模型](https://huggingface.co/baichuan-inc/Baichuan-M1-14B-Instruct)] [[Base](https://huggingface.co/baichuan-inc/Baichuan-M1-14B-Base)]
- [*Journal of the American Medical Informatics Association*] **太一2 (Taiyi-2)** 太一二代开源生物医学模型，底座从Qwen-7B换成GLM4-9B，重做数据过滤与任务指令；官方推荐替换Taiyi-1 [大连理工大学] [[模型](https://huggingface.co/DUTIR-BioNLP/Taiyi2-chat)] [[代码](https://github.com/DUTIR-BioNLP/Taiyi-LLM)] [[DOI](https://doi.org/10.1093/jamia/ocae037)]
- [*arXiv*] **卫宁WiNGPT3** 卫宁第三代医疗推理模型（32B，底座Qwen2.5），多阶段SFT+RL与长思维链，对接WiNEX医院流程；技术报告和代码已公开，权重未核验可下载 [卫宁健康] [[论文](https://arxiv.org/abs/2505.17387)] [[代码](https://github.com/winninghealth/WiNGPT3)]

</details>

<details>
<summary>2024 · 6</summary>

- [*ACM Trans. Knowl. Discov. Data*] **本草[原名：华驼(HuaTuo)]** 基于中文医学知识的大语言模型指令微调 [哈尔滨工业大学] [[论文](https://arxiv.org/pdf/2309.04175.pdf)] [[代码](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)]
- [*arXiv*] **明医 (MING)** 中文医疗问诊大模型 MING，以稀疏 LoRA 混合专家（MING-MoE）增强医疗多任务学习能力（arXiv 2024） [上海交通大学] [[论文](https://arxiv.org/abs/2404.09027)] [[相关 MedCare](https://aclanthology.org/2024.findings-emnlp.619/)] [[代码](https://github.com/MediaBrain-SJTU/MING)]
- [*JAMIA*] **太一 (Taiyi)** 大连理工DUTIR的中英双语生物医学大模型，底座Qwen-7B，覆盖问答、医患对话、报告生成与信息抽取等 [大连理工大学] [[DOI](https://doi.org/10.1093/jamia/ocae037)] [[代码](https://github.com/DUTIR-BioNLP/Taiyi-LLM)] [[模型](https://huggingface.co/DUTIR-BioNLP/Taiyi-LLM)]
- [*arXiv*] **华佗GPT-o1 (HuatuoGPT-o1)** 华佗系列医疗复杂推理模型，用可验证医题+医学验证器做搜索微调与强化学习；7B/72B支持中英 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2412.18925)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-o1)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-7B)]
- [*arXiv*] **华佗GPT-Vision (HuatuoGPT-Vision)** 华佗系列医学多模态模型，大规模注入医学视觉知识，常作中文医学影像/多模态对照 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2406.19280)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-Vision)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B-Qwen2.5VL)]
- [*arXiv*] **Apollo** 中大深圳FreedomIntelligence的多语种医疗LLM（含中文），配套ApolloCorpus与XMedBench [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2403.03640)] [[代码](https://github.com/FreedomIntelligence/Apollo)] [[模型](https://huggingface.co/FreedomIntelligence/Apollo-7B)]

</details>

<details>
<summary>2023 · 19</summary>

- [*arXiv*] **麒麟-Med (Qilin-Med)** 多阶段知识注入的中文医疗LLM（CPT+SFT+DPO，底座Baichuan-7B），发布约3GB ChiMed语料，可再加RAG。arXiv PDF 署名北京大学、港科大（广州）等 [北京大学，香港科技大学（广州）等] [[论文](https://arxiv.org/abs/2310.09089)] [[代码](https://github.com/williamliujl/Qilin-Med)] [[数据集](https://huggingface.co/datasets/williamliu/ChiMed)]
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
- [*arXiv*] **IvyGPT** 基于 LLaMA 的中文医疗问答模型，用高质量医患 QA 与 RLHF 微调，CMB 论文对照列表中的开源基线。arXiv PDF 署名澳门理工大学 [澳门理工大学] [[论文](https://arxiv.org/abs/2307.10512)] [[代码](https://github.com/Ivy0529/IvyGPT)]
- [*arXiv*] **DoctorGLM** 基于ChatGLM-6B的早期开源中文问诊模型，用多科室医患数据做LoRA/P-Tuning，常出现在2023年中文医疗对照表。arXiv HTML 署名上海科技大学、联影智能、复旦大学华山医院等 [上海科技大学，联影智能等] [[论文](https://arxiv.org/abs/2304.01097)] [[代码](https://github.com/xionghonglin/DoctorGLM)]
- [*arXiv*] **DISC-MedLLM** 复旦DISC实验室的医疗对话大模型，底座Baichuan-13B，配套DISC-Med-SFT；知识图谱+真实问诊重构 [复旦大学] [[论文](https://arxiv.org/abs/2308.14346)] [[代码](https://github.com/FudanDISC/DISC-MedLLM)] [[模型](https://huggingface.co/Flmc/DISC-MedLLM)] [[数据集](https://huggingface.co/datasets/Flmc/DISC-Med-SFT)]
- [*arXiv*] **ClinicalGPT** 北邮等用病历、知识、医考和多轮问诊微调的临床向中文医疗模型（BLOOM-7B），CMB等对照表常见；HF有medicalai快照 [北京邮电大学] [[论文](https://arxiv.org/abs/2306.09968)] [[模型](https://huggingface.co/medicalai/ClinicalGPT-base-zh)]
- [*arXiv*] **ChiMed-GPT** 中科大等在Ziya-v2上做继续预训练+SFT+RLHF的中文医疗大模型，覆盖抽取、问答与多轮对话 [中国科学技术大学] [[论文](https://arxiv.org/abs/2311.06025)] [[代码](https://github.com/synlp/ChiMed-GPT)] [[模型](https://huggingface.co/SYNLP/ChiMed-GPT-1.0)]
- **ChatMed** ChatMed 系列中文医疗大模型，含基于 50 万+ 在线问诊数据训练的 ChatMed-Consult。GitHub README 引用 Wei Zhu / Xiaoling Wang，无独立期刊论文 [华东师范大学] [[代码](https://github.com/michael-wzhu/ChatMed)] [[模型](https://huggingface.co/michaelwzhu/ChatMed-Consult)]
- **ChatGLM-Med** 哈工大SCIR用中文医学知识图谱指令微调的ChatGLM-6B，与本草/华驼同源数据，CMB常用对照 [哈尔滨工业大学] [[代码](https://github.com/SCIR-HI/Med-ChatGLM)]
- **CareGPT** 开源中文医疗LLM全流程训练框架（预训练到DPO）与配套权重，常被复现中文医疗微调。README 写明由澳门理工大学应用科学学院完成 [澳门理工大学] [[代码](https://github.com/WangRongsheng/CareGPT)]

</details>


</details>

<details>
<summary>闭源中文医疗产品，无核验权重（4）</summary>

- **讯飞星火医疗** 科大讯飞闭源医疗大模型（星火医疗X1/X2），落地智医助理与讯飞晓医；无公开权重，只作产业对照 [科大讯飞] [[官网](https://www.xunfeihealthcare.com/)] [[新闻](https://www.cn-healthcare.com/article/20250303/wap-content-585822.html)]
- **蚂蚁阿福 / 蚂蚁医疗大模型** 蚂蚁闭源多模态医疗大模型，先作支付宝AQ后升级为阿福，做问诊、报告与药盒识别；WAIC 2024发布，无公开权重 [蚂蚁集团] [[官网](https://www.antafu.com/)] [[新闻稿](https://www.antgroup.com/news-media/press-releases/1720166400000)]
- **腾讯混元医疗** 腾讯健康基于混元的闭源医疗大模型，覆盖问答、导诊、病历与影像；天衍实验室发布，无公开权重 [腾讯] [[官网](https://healthcare.tencent.com/)] [[新闻](https://healthcare.tencent.com/news/1603)]
- [*Sci China Life Sci*] **盘古药物分子大模型 (PanGu Drug Model)** 华为云与中科院上海药物所的闭源分子预训练模型（约17亿小分子），做属性预测/生成/优化；数智本草曾以其为底座之一 [华为云，中国科学院上海药物研究所] [[DOI](https://doi.org/10.1007/s11427-022-2239-y)] [[官网](https://www.huaweicloud.com/cases/pgyw.html)]

</details>

<details>
<summary>日韩汉方 / 韩医模型与系统（1）</summary>

- **KAMPO LLM** 官网仍开：VARYTEX 与日本东洋医学会合作的闭源汉方 API；页面写明 471 题评测 Pro 97.4%、Flash 92.1%，无公开权重 [VARYTEX，日本东洋医学会] [[官网](https://kampollm.varytex.co.jp/)]

</details>

<details>
<summary>Hugging Face 上的其他尺寸和 GGUF（12）</summary>

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

</details>

## 新闻

<details>
<summary>29 条，最近有：广医·岐智2.0 · 首发首展 · 华族本草</summary>

<details>
<summary>2026 · 10</summary>

- [2026.09] 中国中医科学院广安门医院在2026服贸会展示**广医·岐智2.0**，以AI医生「安安」覆盖患者服务、临床诊疗、病房管理等六大场景 [[链接](https://app.xinhuanet.com/news/article.html?articleId=202609101de3e66a53f7474ba7d373deaaa7e122)]
- [2026.09] 2026服贸会中医药展区，北京中医药大学**首发首展**中医体质辨识体系与具身智能推拿机器人，同期还有智能诊脉设备体验 [[链接](https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202608/t20260807_4812596.html)]
- [2026.07] 贵州医科大学等在中国—东盟教育交流周发布全国首个民族药创制全域智能平台**华族本草**，以数智岐黄+Qwen为底座融汇多民族医药古籍 [[链接](https://www.gmc.edu.cn/info/1058/30267.htm)]
- [2026.07] 智慧眼携**砭石云中医**亮相WAIC 2026，以已备案砭石多模态大模型为底座，展示四诊仪与辅助诊疗系统 [[链接](http://www.eeo.com.cn/2026/0720/965556.shtml)]
- [2026.07] 安顿健康在WAIC 2026首发**七诊合参**中医机器人，集成面/红外面/舌/耳/闻/问/脉采集，底座含天回脉诊算法与中医诊疗大模型 [[链接](https://www.news.cn/finance/20260720/f6a8625c1be4412d9c311a232c7a35fa/c.html)]
- [2026.07] 上海中医药大学附属第七人民医院正式发布**岐元大模型**，采用预训练+领域微调+专家强化学习，支持生成式病历与名老中医Agent数字孪生，并亮相WAIC [[链接](https://dwgk.shutcm.edu.cn/2026/0725/c1890a175544/page.htm)]
- [2026.06] 中科闻歌通过港交所上市聆讯；报道提及与中国中医科学院合作的**大医金匮**中医大模型已通过中国信通院最高级别可信AI认证 [[链接](https://www.ncsti.gov.cn/kjdt/xwjj/202606/t20260610_249369.html)]
- [2026.04] 山东中医药大学附属医院启动山东省卫健委「人工智能＋」中医药重点场景**智汇岐黄**大模型项目 [[链接](http://ccpd.china.com.cn/2026-04/17/content_43401621.html)]
- [2026.04] 北京中医药大学牵头研发的**薪火中国药**中医药教育大模型通过国家生成式人工智能服务备案，成为国内首个获批面向公众服务的中医药领域大模型 [[链接](https://regional.chinadaily.com.cn/education/cn/2026-04/22/c_1177692.htm)]
- [2026.02] 工信部等八部门印发《中药工业高质量发展实施方案（2026—2030年）》，明确运用人工智能与知识图谱赋能经典名方与名老中医经验方研发 [[链接](https://www.gov.cn/zhengce/zhengceku/202602/content_7057174.htm)]

</details>

<details>
<summary>2025 · 14</summary>

- [2025.12] **智明堂ZMT-M1**在国家中医执业医师资格考试模拟测试中以96.26分获得该领域最佳成绩，已在全国100余间诊室试点应用 [[链接](https://m.tech.china.com/redian/2025/1229/122025_1789291.html)]
- [2025.12] 固生堂发布”中医大脑”产品及国医大师施杞教授AI数字分身，已累计发布14位顶级专家数字分身，覆盖八大中医核心专科 [[链接](https://www.jjckb.cn/20251231/693ca93b14ff4f57adc359959dc0320d/c.html)]
- [2025.12] 吉林发布**众星·长白岐黄1.0** AI原生多模态中医药大模型 [[链接](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- [2025.11] 国家卫健委等五部门印发《关于促进和规范”人工智能+医疗卫生”应用发展的实施意见》，明确支撑建设中医药诊疗大模型 [[链接](https://www.gov.cn/zhengce/zhengceku/202511/content_7047018.htm)]
- [2025.09] **智赋岐黄天功**中医AI大模型通过国家深度合成服务算法备案，应用于中医四诊仪与体质辨识 [[链接](http://zs.scbzol.com/zs/2025/0919/328624.html)]
- [2025.09] 传神语联**任度·素问**通过中国信通院可信AI中医药大模型4+级评估 [[链接](https://zhongyi.gmw.cn/2025-09/10/content_38277329.htm)]
- [2025.09] 中原药谷基层中医药振兴工程下，**伊尹中医经典大模型**在嵩县发布启用，融合中医教育与AI辅助诊疗服务县域基层 [[链接](http://www.ha.xinhuanet.com/20250918/a3da94037689422dbcd1fe57fa62ef94/c.html)]
- [2025.08] 国家超算天津中心联合天津中医药大学等发布**天河·灵枢**2.0，由针灸专科扩展至20余科；同步启动中医药智能模型评价体系 [[链接](http://tj.people.com.cn/n2/2025/0809/c375366-41317410.html)]
- [2025.08] **固生堂**正式发布十大”国医AI分身”，基于国医大师及名中医临床经验构建，辨证准确性达86%以上 [[链接](http://sz.people.com.cn/n2/2025/0801/c202846-41310443.html)]
- [2025.07] 中国中医科学院广安门医院与多家医联体单位成立**广医·岐智大模型智能体联盟**，推进跨机构智能诊疗能力辐射 [[链接](https://www.gamyy.cn/gzb/news/big/112751.html)]
- [2025.06] **中医横琴**垂类大模型正式发布 [[链接](https://www.stdaily.com/web/gdxw/2025-06/20/content_357526.html)]
- [2025.05] 中国中医科学院发布中医药大模型评测标准 [[链接](https://www.news.cn/politics/20250510/5e6a0b4978b44b69b67dbfb7282fd220/c.html)]
- [2025.04] 传神语联发布**任度·素问**中医大模型，基于全自研混合熵(moH)技术架构，支持智能问诊、辨证分析、方剂推荐 [[链接](https://www.transn.com/about_us/consult/article/1924766101036437505)]
- [2025.03] 中国中医科学院广安门医院28日正式发布**广医·岐智**中医大模型，成为国内首家本地化部署”算力+模型+应用”一体化服务的中医医院 [[链接](https://www.xinhuanet.com/tech/20250328/8b1685ad8c6f48c9bdc2add1658edac3/c.html)]

</details>

<details>
<summary>2024 · 4</summary>

- [2024.12] 招联消费金融联合中山大学、广州中医药大学深圳医院发布中医垂直大模型**仲思**，落地深圳多家社康中心智能问诊 [[链接](https://finance.sina.com.cn/jjxw/2024-12-16/doc-inczrzsp5791684.shtml)]
- [2024.09] 中科闻歌发布**大医金匮**中医大模型及中医智能健康管理平台，基于1500余本中医典籍训练 [[链接](https://36kr.com/newsflashes/2946967562099592)]
- [2024.05] 天士力与华为云联合发布**数智本草**大模型，基于盘古语言与药物分子模型，覆盖中药研发全链条；后通过信通院中医药大模型4+级评估 [[链接](https://news.pharmnet.com.cn/news/2024/05/10/591622.html)]
- [2024.03] 华东师范大学、上海中医药大学、华东理工大学、海军军医大学、临港实验室、华润江中现代中药全国重点实验室联合开发了**数智岐黄**中医药大模型。所附链接为华东师范大学对数智岐黄 2.0 的后续介绍，并非 2024.03 首发公告。 [[链接](https://pharm.ecnu.edu.cn/08/27/c43775a657447/page.htm)]

</details>

<details>
<summary>2023 · 1</summary>

- [2023.07] 南京大经中医发布**岐黄问道·大模型**，基于千万级知识图谱与临床数据，面向医疗机构开放内测 [[链接](http://js.news.cn/20230729/fa034db71a00487b819a4ad95b44673e/c.html)]

</details>


</details>

## 综述

<details>
<summary>47 篇，按年收着</summary>

<details>
<summary>2026 · 22</summary>

- [*兰州大学学报(医学版)*] **从大语言模型到智能体（兰州大学学报医学版综述）** 以「大模型→智能体」演进为主线的中医临床辅助诊疗中文系统综述，梳理研究进展、关键问题与方向（兰州大学学报(医学版) 2026;52(4):49-57） [[DOI](https://doi.org/10.13885/j.issn.2097-681X.T20260032)]
- **Agentic and Knowledge-Grounded LLMs in TCM（预注册）** 中医Agentic/知识接地LLM系统综述的OSF预注册方案（证据图谱+文本挖掘+转化就绪度），非完成版综述 [[预注册](https://doi.org/10.17605/osf.io/kq8jx)]
- [*International Journal of Pattern Recognition and Artificial Intelligence*] **中医大模型关键技术综述（IJPRAI）** 系统综述中医大模型知识组织、辅助诊断与临床决策支持关键技术（World Scientific IJPRAI正式发表） [Guangdong Provincial Hospital of Traditional Chinese Medicine，Guangdong University Of Finances and Economics，Guangdong University of Finance] [[DOI](https://doi.org/10.1142/s0218001426590263)]
- [*Journal of Traditional Chinese Medical Sciences*] **AI驱动中医诊断智能化综述（JTCMS）** 综述多模态融合与大模型在中医四诊智能化中的应用、挑战与展望（JTCMS正式发表） [暨南大学，北京中医药大学] [[DOI](https://doi.org/10.1016/j.jtcms.2026.05.002)]
- [*上海中医药杂志*] **人工智能驱动下的中医智能诊疗研究进展与挑战** 以中医辨治六步程式为骨架的全链路（四诊-辨证-处方-疗效预测）中文综述，对照监督/无监督/强化/深度学习范式（上海中医药杂志 2026;60(1)） [[DOI](https://doi.org/10.16305/j.1007-1334.2026.z20250609004)]
- [*Communications in Computer and Information Science (Springer)*] **多模态大模型驱动舌脉面诊智能化综述（Springer 书章）** 唯一以「多模态LLM×四诊感知」为题的综述性文本，覆盖舌/脉/面诊智能化（Springer CCIS 会议书章，评审强度低于期刊） [Chinese Academy of Social Sciences，Institute of Ethnology and Anthropology，University of Chinese Academy of Social Sciences] [[DOI](https://doi.org/10.1007/978-981-95-7299-1_15)]
- [*中华中医药学刊*] **人工智能赋能中医数字化诊断：现状与挑战（中华中医药学刊）** 中文短篇综述：AI在海量数据处理、辅助诊断、疾病预测的应用现状与数据质量/可解释性/理论融合三挑战（北大核心，题录级） [[DOI](https://doi.org/10.13193/j.issn.1673-7717.2026.01.004)]
- [*Integrative Medicine Research*] **Yao et al. 2026: LLM 与循证中医整合（Scoping Review）** PRISMA scoping review，纳入 12 篇（2022-11 至 2026-01），覆盖 LLM 循证中医的证据生成、合成与转化 [University of Geneva，中国医学科学院，Gansu University of Traditional Chinese Medicine，Lanzhou University] [[DOI](https://doi.org/10.1016/j.imr.2026.101349)]
- [*Journal of Pharmaceutical Analysis*] **Xu et al. 2026: 基于 LLM 的中医智能问答系统综述** 中医智能问答系统谱系综述（KG-QA→LLM-QA、RAG） [天津大学，Tianjin haihe hospital] [[DOI](https://doi.org/10.1016/j.jpha.2025.101406)]
- [*Artificial Intelligence Review*] **Wu et al. 2026: AI 在中药材中的应用综述** 中药学×AI 全栈 survey（成分、靶点、质控，含 LLM 一节） [Northeastern University，First Hospital of China Medical University，China Medical University，Liaoning University] [[DOI](https://doi.org/10.1007/s10462-026-11513-w)]
- [*Information*] **Lu et al. 2026: 深度学习中医诊断方法学质量审计** 系统综述+验证缺口分析：DL 中医疾病诊断研究的方法学质量与临床转化 [香港中文大学] [[DOI](https://doi.org/10.3390/info17060554)]
- [*ACL 2026*] **LLM-Based Multi-Agent Systems for Clinical Workflows（ACL 2026，邻近）** 工作流级多智能体综述+四层评测栈（safety/process/outcome/operations）；无TCM交集但过程评测主张方法学同构（邻近） [Sanford Health，University of Massachusetts Lowell，University of Massachusetts Amherst] [[DOI](https://doi.org/10.18653/v1/2026.acl-long.2123)]
- [*Chinese Medicine*] **Han et al. 2026: LLM 在中医中的调优与临床应用（Scoping Review）** PRISMA-ScR scoping review，纳入 27 篇（至 2025-05），聚焦 LoRA/CPT/RAG 调优配方与临床应用统计 [中国医学科学院，Jining Traditional Chinese Medicine Hospital，中国中医科学院，北京中医药大学] [[DOI](https://doi.org/10.1186/s13020-026-01346-8)]
- [*Chinese Medicine*] **Guo et al. 2026: AI 与多模态数据融合推动中医现代化** AI 全景综述（ML/DL/KG/NLP/LLM），LLM 为一节，附多尺度数据资源与平台编目 [Ningbo College of Health Sciences，Shenzhen Second People's Hospital，Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1186/s13020-025-01194-y)]
- [*Journal of Integrative Medicine*] **Deep learning in TCM（J Integr Med）** 深度学习单技术线综述：医学影像、药材物质研究、数据挖掘等应用实例（J Integr Med 2026;24(4):471-480） [天津大学] [[DOI](https://doi.org/10.1016/j.joim.2026.03.001)]
- [*OSF Preprints*] **Cong H et al. TCM×LLM 综述（OSF 预印本）** OSF 平台中医×LLM 综述预印本（未经同行评议，存档用） [[DOI](https://doi.org/10.17605/osf.io/5z367)]
- [*Science of Traditional Chinese Medicine*] **Chen et al. 2026: LLM 在中医的下一步（叙述性综述）** 叙述性前瞻：多模态、Agent 与临床落地路线 [北京中医药大学] [[DOI](https://doi.org/10.1097/st9.0000000000000109)]
- [*OSF Preprints*] **Cai R et al. TCM×LLM scoping review（OSF 预印本）** OSF 平台中医×LLM 范围综述预印本（未经同行评议，存档用） [[DOI](https://doi.org/10.17605/osf.io/2hyeq)]
- [*Pharmacological Research - Modern Chinese Medicine*] **AI in TCM: multimodal data to pharmacology and clinical decision（PRMCM 综述）** 宽口径 AI×TCM 英文综述：多模态数据整合→药理研究→临床决策支持（Pharmacol Res Mod Chin Med 2026；第三轮扫描新发现，无基准矩阵/开源编目/历史谱系） [Saveetha University] [[DOI](https://doi.org/10.1016/j.prmcm.2026.100842)]
- [*Research*] **AI in TCM: Unraveling Herbal Medicine's Mechanisms（Research）** 主张AI从相关分析范式走向重建证候辨证与方剂配伍生物逻辑的药材机制中心宽口径综述（Research 2026;9:1224） [Zhejiang Chinese Medical University] [[DOI](https://doi.org/10.34133/research.1224)]
- [*Journal of Integrative Medicine*] **AI empowers the innovation of TCM（J Integr Med 评论）** 单作者评论性综述：古籍挖掘、诊疗标准化、药物研发周期三痛点×AI（J Integr Med 2026） [上海中医药大学] [[DOI](https://doi.org/10.1016/j.joim.2026.05.004)]
- [*Chinese Medicine and Culture*] **AI and Big Data in TCM Standardization and Internationalization（Chin Med Cult）** AI/大数据助力中医标准化与国际化评论（Chin Med Cult 2026, ahead of print） [南洋理工大学] [[DOI](https://doi.org/10.1097/mc9.0000000000000203)]

</details>

<details>
<summary>2025 · 15</summary>

- [*Chinese Medicine*] **古籍知识图谱×多智能体融合综述（Chin Med）** 古籍KG构建（术语统一、数据标准化）挑战-展望型综述，首次把multi-agent写入中医古籍议题（Chin Med 2025;20:168） [北京大学] [[DOI](https://doi.org/10.1186/s13020-025-01226-7)]
- [*智能系统学报*] **医疗领域的大型语言模型综述（智能系统学报，邻近）** 中文医疗LLM通用综述（训练流程/策略/场景/挑战），与中医LLM综述圈属母子集关系（邻近） [[DOI](https://doi.org/10.11992/tis.202405003)]
- [*智能系统学报*] **医学大语言模型的研发与应用系统综述（智能系统学报，邻近）** 系统综述129个医学专用LLM（截至2024-06）+4类临床应用研究；系统检索协议方法学可比（邻近） [[DOI](https://doi.org/10.11992/tis.202410020)]
- [*中华中医药学刊*] **人工智能实现中医四诊的发展现状、问题及解决路径（中华中医药学刊）** 四诊AI客观化现状-问题-路径分析：面舌采集、电子鼻、脉象传感、四诊合参融合度低（北大核心，题录级） [[论文](https://www.sinomed.ac.cn/article.do?ui=2026106036)]
- [*AI Medicine*] **Zhang et al. 2025: 中医 LLM 短综述与展望** 短 survey+展望，TCM LLM 模型与任务速览 [Northeastern University] [[DOI](https://doi.org/10.53941/aim.2025.100003)]
- [*Journal of Evidence-Based Medicine*] **Yip et al. 2025: 中西医结合 LLM 进展与挑战** 综述：LLM 在整合医学（中西医结合）中的进展、挑战与机遇 [Hong Kong Baptist University，Guangdong-Hongkong-Macau Joint Laboratory of Collaborative Innovation for Environmental Quality] [[DOI](https://doi.org/10.1111/jebm.70031)]
- [*American Journal of Chinese Medicine*] **Wang et al. 2025: AI 驱动中医诊断模型进展** 系统综述：AI 诊断模型（四诊客观化、辨证） [清华大学，南京大学] [[DOI](https://doi.org/10.1142/S0192415X25500259)]
- [*Journal of Pharmaceutical Analysis*] **The integration of machine learning into TCM（J Pharm Anal）** 机器学习×中医整合综述：诊断客观化与机制阐释两条线（J Pharm Anal 2025;15(8):101157） [Hangzhou Normal University] [[DOI](https://doi.org/10.1016/j.jpha.2024.101157)]
- [*American Journal of Chinese Medicine*] **Shataer et al. 2025: LLM 在中医应用（State-of-the-Art Review）** 叙述性综述，扫描 TCM LLM 应用场景（诊疗、教育、翻译、科研） [Centre for Intelligent Healthcare, Coventry University, Coventry CV1 5RW, UK] [[DOI](https://doi.org/10.1142/S0192415X25500375)]
- [*Journal of Evidence-Based Medicine*] **Ren et al. 2025: 中医大语言模型（Scoping Review）** Arksey–O'Malley scoping review，纳入 29 篇（至 2024-04），覆盖知识管理、辅助诊疗与考试准确率 [成都中医药大学，中国医学科学院，Institute of Health Data Science Lanzhou University Lanzhou China，Institute of Global Health University of Geneva Geneva Switzerland] [[DOI](https://doi.org/10.1111/jebm.12658)]
- [*Pharmacological Research*] **Meng et al. 2025: 大模型+虚拟细胞助力中医变革** 综述：大模型与虚拟细胞用于中风方药现代分析 [Northeastern University，Shenyang Medical College] [[DOI](https://doi.org/10.1016/j.phrs.2025.107953)]
- [*Healthcare*] **Intelligent Question-Answering Systems in Healthcare（Healthcare，邻近）** 2018-2025医疗QA综述+CiteSpace计量，明确含中医方剂开发应用场景（邻近综述，非TCM专用） [Beijing Information Science & Technology University] [[DOI](https://doi.org/10.3390/healthcare13182269)]
- [*Journal of Evidence-Based Medicine*] **Guo et al. 2025: GPT 能否加速中医智能诊疗（综述+实证）** 综述+实证分析，讨论 GPT 适配中医诊疗的挑战与幻觉问题 [Xiyuan Hospital China Academy of Chinese Medicinal Sciences Beijing China，北京大学] [[DOI](https://doi.org/10.1111/jebm.70004)]
- [*Acupuncture and Herbal Medicine*] **Chen et al. 2025: 中医大语言模型系统综述** 系统综述，纳入 10 篇（至 2024 年中），聚焦生成任务证据 [天津大学，现代中药海河实验室，Italian National Institute of Health, Rome, Italy] [[DOI](https://doi.org/10.1097/HM9.0000000000000143)]
- [*Current Medical Science*] **AI for Spleen-Stomach Disorders in TCM（Curr Med Sci）** 单病种（脾胃病）KG+智能诊疗综述：「症状-证候-疾病-方剂」框架的知识工程化（Curr Med Sci 2025;45(6):1348-1357） [Hubei University of Chinese Medicine，Hubei Provincial Hospital of Traditional Chinese Medicine，Hospital Conde S. Januário，Union Hospital] [[DOI](https://doi.org/10.1007/s11596-025-00128-x)]

</details>

<details>
<summary>2024 · 5</summary>

- [*计算机工程与应用*] **苏尤丽 et al. 2024: 人工智能在中医诊疗领域的研究综述** 中文综述：专家系统→机器学习→深度学习三阶段中医 AI 诊疗发展与挑战 [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2312-0400)]
- [*南京中医药大学学报*] **李欣桐 et al. 2024: 中医药领域大语言模型研究进展与展望** 中文综述：中医药 LLM 研究过程、前沿技术（提示工程/RAG/RLHF）与应用前景 [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1393)]
- [*Computers in Biology and Medicine*] **Tian et al. 2024: 四诊机器学习综述** 望闻问切四诊的 ML 传感与模型综述 [Northeastern University，Ningbo University，辽宁中医药大学] [[DOI](https://doi.org/10.1016/j.compbiomed.2024.108074)]
- [*中国工程科学*] **Song et al. 2024: AI 辅助中医辨证关键问题与技术挑战** 战略研究综述：多模态数据融合、症状关联、证候量化与推理及中医药大模型关键问题 [Shanghai University of Engineering Science，Digital China Health (China)，Zhejiang Lab，中国医学科学院] [[DOI](https://doi.org/10.15302/J-SSCAE-2024.02.010)]
- [*Computer Materials & Continua*] **Qu et al. 2024: 中医知识图谱综述** 中医知识图谱的分析、构建、应用与展望 [中国医学科学院，Beijing Forestry University] [[DOI](https://doi.org/10.32604/cmc.2024.055671)]

</details>

<details>
<summary>2021 · 1</summary>

- [*Computers in Biology and Medicine*] **Zhang et al. 2021: 计算中医诊断文献综述** 计算化中医诊断的文献综述（症状采集、辨证建模与系统） [澳门大学] [[DOI](https://doi.org/10.1016/j.compbiomed.2021.104358)]

</details>

<details>
<summary>2020 · 1</summary>

- [*Artificial Intelligence in Medicine*] **Chu et al. 2020: 中医定量知识表示模型综述** 中医知识定量表示模型（本体、规则、统计）综述 [Xidian University，Xi'an Polytechnic University，Guangdong Polytechnic Normal University，CM Hospital] [[DOI](https://doi.org/10.1016/j.artmed.2020.101810)]

</details>

<details>
<summary>2015 · 1</summary>

- [*Evidence-Based Complementary and Alternative Medicine*] **Zhao et al. 2015: 中医患者分类进展（ML 视角）** ML 驱动的中医病人/证候分类综述 [同济大学] [[DOI](https://doi.org/10.1155/2015/376716)]

</details>

<details>
<summary>2013 · 1</summary>

- [*Briefings in Bioinformatics*] **Gu & Chen 2013: 生物信息学遇见中医** 生物信息学×中医（组学、文本挖掘）历史综述 [浙江大学] [[DOI](https://doi.org/10.1093/bib/bbt063)]

</details>

<details>
<summary>2007 · 1</summary>

- [*Computer Methods and Programs in Biomedicine*] **Lukman et al. 2007: 中医计算方法综述** 计算方法（专家系统、ML、数据挖掘）全景，中医计算研究的方法学鼻祖 [University of Cambridge，University of Reading，南洋理工大学] [[DOI](https://doi.org/10.1016/j.cmpb.2007.09.008)]

</details>


</details>

## 专利

收中医大模型、知识图谱、RAG、智能问诊与处方推荐等系统专利，不限中国；不收中药组方、制剂专利全集。

<details>
<summary>22 件，按公开年收着</summary>

<details>
<summary>2026 · 11</summary>

- [*CN122529089A*] **基于大语言模型的中医对话生成方法及装置** 用长期记忆库与用户画像生成个性化中医对话（公开，未授权） [杭州旺柴科技] [[专利](https://patents.google.com/patent/CN122529089A/zh)]
- [*CN122436154A*] **张锡纯中医理法方药数字化传承与智能分析系统** 辨病辨证规则 + 三路检索 + LLM 融合，做张锡纯学派理法方药分析（公开，未授权） [广州知云草堂医疗科技] [[专利](https://eureka.patsnap.com/patent/CN122436154A)]
- [*CN122025029A*] **融合类别信息因果对比学习与LLM图注意力的中医处方推荐方法** 症状-草药异构/同构图 + LLM 增强因果机制做处方推荐（公开，未授权） [湖州师范学院] [[专利](https://eureka.patsnap.com/patent/CN122025029A)]
- [*CN122050861A*] **大模型与双通道检索结合的中医智能诊疗平台构建方法** LLM+中医知识图谱双通道检索，面向名医经验传承与处方生成（公开，未授权） [上海中医药大学附属岳阳中西医结合医院] [[专利](https://patents.google.com/patent/CN122050861A/zh)]
- [*CN122117314A*] **基于大语言模型的智能针灸诊断智能体系统及方法** 针灸知识库 + 图谱 + 向量检索 + 重排序，LLM 智能体分类问题并主动追问（公开，未授权） [河南理工大学] [[专利](https://eureka.patsnap.com/patent/CN122117314A)]
- [*CN122091073A*] **基于多任务联合优化的中医处方生成方法及装置** 预训练大模型做自回归处方序列 + 草药集合预测，照顾低频药（公开，未授权） [杭州电子科技大学] [[专利](https://eureka.patsnap.com/patent/CN122091073A)]
- [*CN121862376A*] **基于知识图谱和大语言模型的中医辨证问答系统及方法** 古籍/医案分块抽实体建图谱，再按局部与全局关键词检索生成辨证问答（公开，未授权） [南京邮电大学] [[专利](https://patents.google.com/patent/CN121862376A/zh)]
- [*CN121687367A*] **基于结构化证据子图检索增强生成的中医草药推荐方法及系统** 多跳证据子图 + Hopfield 联想检索做草药推荐，并用图谱约束压幻觉（公开，未授权） [浙江中医药大学] [[专利](https://patents.google.com/patent/CN121687367A/zh)]
- [*CN121743505A*] **基于知识增强的中医医案按语生成方法及装置** 图谱子图混合检索后，按病因病机、治则、方药、预后四要素生成医案按语（公开，未授权） [浙江大学] [[专利](https://patents.google.com/patent/CN121743505A/zh)]
- [*CN121480736A*] **基于知识蒸馏与强化学习的肿瘤中医智能处方推荐方法及系统** GPT-4o 教师蒸馏 Qwen 学生，再 DPO，做可解释的肿瘤中医处方（公开，未授权） [南京中医药大学] [[专利](https://patents.google.com/patent/CN121480736A/zh)]
- [*CN121436134A*] **一种多模态知识图谱构建方法及系统** 用大模型从中医药文本抽三元组，再融合真实病历层做成多模态图谱（公开，未授权） [杭州甘之草科技] [[专利](https://patents.google.com/patent/CN121436134A/zh)]

</details>

<details>
<summary>2025 · 6</summary>

- [*CN120690391B*] **一种基于知识图谱技术的中药经典名方智能推荐方法** 口语到术语的语义映射 + 体质过滤 + 多症状协同，推荐经典名方（已授权） [顺福科技集团] [[专利](https://patents.google.com/patent/CN120690391B/zh)]
- [*CN120108694A*] **基于知识图谱与医案增强RAG的中医智能问诊方法及系统** Leiden 子图检索 + 全局/本地混合召回，再由大模型统一生成问诊建议（公开，未授权） [江苏大学] [[专利](https://patents.google.com/patent/CN120108694A/zh)]
- [*CN120221058A*] **基于多模态知识图谱与大语言模型的中医康复诊断系统** 舌苔、脉象与问诊特征对齐知识图谱嵌入，再交给中医康复专家大模型（公开，未授权） [浙江中医药大学] [[专利](https://patents.google.com/patent/CN120221058A/zh)]
- [*CN120067279B*] **基于AI大语言模型的中医智能问诊方法及系统** 面舌形体图像、语音气息与病症库融合的多模态问诊系统（已授权） [医脉人工智能医疗科技（天津）] [[专利](https://patents.google.com/patent/CN120067279B/zh)]
- [*CN119763764A*] **一种基于大语言模型的中药处方推荐方法及系统** 软提示 + 交叉注意力把患者文本送进大模型，输出可控中药处方（公开，未授权） [杭州甘之草科技] [[专利](https://patents.google.com/patent/CN119763764A/zh)]
- [*CN119416782A*] **基于大语言模型的中医方学习方法、装置、设备及介质** 用 Qwen 等大模型对齐文言医案术语与白话，做名老中医方学习（公开，未授权） [成都字节流科技] [[专利](https://patents.google.com/patent/CN119416782A/zh)]

</details>

<details>
<summary>2024 · 5</summary>

- [*CN119149754A*] **基于大模型和知识图谱的中医药方剂配伍方法及装置** 中医药大模型与知识图谱协同做方剂配伍（公开，未授权） [天津大学，天大智图（天津）科技] [[专利](https://patents.google.com/patent/CN119149754A/zh)]
- [*CN119092157B*] **一种基于大语言模型的中药问答方法、装置、设备及介质** 在 Baichuan2-7B-Chat 上做中药问答（2025.02 授权） [浙江大学，长三角智慧绿洲创新中心] [[专利](https://patents.google.com/patent/CN119092157B/zh)]
- [*CN118838996A*] **基于大语言模型和知识图谱的中医药问答系统构建方法** LLM 生成与知识图谱补全闭环的中医药问答（公开，未授权） [北京理工大学，北京理工大学唐山研究院] [[专利](https://patents.google.com/patent/CN118838996A/zh)]
- [*CN118230893A*] **基于AI大模型的智能中医处方推荐方法及系统** 用病历训练 AI 大模型生成个性化中药处方，并接到医院信息系统（公开，未授权） [杭州甘之草科技] [[专利](https://patents.google.com/patent/CN118230893A/zh)]
- [*CN117828050B*] **基于长文档检索增强生成的中医问答方法、设备及介质** 长文档 RAG（扩展、召回、重排序、来源标注）做中医问答（2024.07 授权） [北京智谱华章科技] [[专利](https://patents.google.com/patent/CN117828050B/zh)]

</details>


</details>

## 论文

这里只收方法、评测和系统论文。发布了领域大模型的条目在「开源模型」，不在这里重复。

<details>
<summary>Agent（11）：问诊流程、多智能体</summary>

- [*arXiv*] **DeepTCM1.0** 基于DeepSeek V3.2的11专家多智能体，解析中药复方机制（桂枝汤验证）；Research Square后上到arXiv [广州中医药大学，Chinese Medicine Guangdong Laboratory (Hengqin)，Changzhi Medical College] [[论文](https://arxiv.org/abs/2608.18103)] [[预印本](https://doi.org/10.21203/rs.3.rs-9844166/v1)]
- [*arXiv*] **DeepRoot** 多智能体把《神农本草经》建成可核验Neo4j图谱再做治疗推理，代码与评测脚本已开源 [[论文](https://arxiv.org/abs/2606.15931)] [[代码](https://github.com/CarlisleMa/deeprootv1)]
- [*Journal of Pharmaceutical Analysis*] **TCM-Agent** 面向网络药理学与中药发现的 LLM 多智能体系统 [[论文](https://doi.org/10.1016/j.jpha.2026.101581)] [[代码](https://github.com/AITCM/TCM-Agent)]
- [*arXiv*] **MACAT** 多智能体文化感知翻译框架，实验覆盖中医经典与《论语》文化负载词英译 [[论文](https://arxiv.org/abs/2606.01276)]
- [*Applied Sciences*] **KM-Agent** 韩医/东亚传统医学工具增强Agent，检索4780条药材–证候–穴位元数据，并在TCMBench等上评测。MDPI/OpenAlex 署名圆光大学、釜山大学、东国大学等 [圆光大学，釜山大学等] [[论文](https://www.mdpi.com/2076-3417/16/7/3377)] [[代码](https://github.com/wonyung-lee/km-agent)]
- [*arXiv*] **DERM-3R** 资源受限下的中医皮肤病多模态多智能体框架（识别/表征/辨证论治三智能体） [[论文](https://arxiv.org/abs/2604.09596)]
- [*arXiv*] **CORE-Acu** 针灸临床决策：结构化推理轨迹与知识图谱安全否决闭环 [[论文](https://arxiv.org/abs/2603.08321)]
- [*arXiv*] **经方 (Jingfang)** 基于LLM的中医多智能体诊疗系统，辨证精度提升124% [[论文](https://arxiv.org/abs/2502.04345)]
- **仁术AI (RenShu-AI)** FastAPI + LangGraph 多智能体中医问诊系统，融合 GraphRAG 与 DeepSeek-TCM [[代码](https://github.com/yanlinPeng-code/RenShu-AI)]
- [*Information*] **中药化合物检索智能体** 中药化合物信息检索AI智能体系统 [郑州大学] [[DOI](https://doi.org/10.3390/info16070543)]
- [*Journal of King Saud University Computer and Information Sciences*] **DiagX-DT** 辨证排除式推理框架，结合思维链与外部中医知识库迭代剔除不合理证候选项 [[DOI](https://doi.org/10.1007/s44443-025-00123-1)]

</details>

<details>
<summary>多模态 / 四诊（4）：舌、面、脉</summary>

- [*ICASSP 2025*] **少样本舌诊上下文多任务微调** 舌象到体质直接判别的少样本上下文多任务LLM微调方法 [东北大学] [[DOI](https://doi.org/10.1109/ICASSP49660.2025.10887764)]
- [*arXiv*] **TCDiff** 三联级联扩散模型生成高保真多模态中医EHR，并构建**TCM-SZ1**基准数据集 [[论文](https://arxiv.org/abs/2508.01615)]
- **Chinese-LLaVA-Med** 基于 LLaVA 架构的中文医学多模态大模型，支持中文医学影像问答，配套 llava-med-zh-eval 评测集与开源 7B 权重 [[代码](https://github.com/BUAADreamer/Chinese-LLaVA-Med)]
- **XrayGLM** 会看胸部X光片的中文多模态医学大模型 [澳门理工大学] [[代码](https://github.com/WangRongsheng/XrayGLM)]

</details>

<details>
<summary>RAG / 知识图谱（27）：检索和医案、方剂图谱</summary>

<details>
<summary>2026 · 6</summary>

- [*Communications in Computer and Information Science (Springer)*] **Hybrid Retrieval + Re-ranking TCM Prescription Generation** 混合检索+重排序增强LLM的中医处方生成（Springer CCIS会议论文） [齐鲁工业大学，Shandong University，Shandong Academy of Sciences，山东中医药大学] [[论文](https://doi.org/10.1007/978-981-92-3563-6_21)]
- [*arXiv*] **Evidence-Based TCM Visualization Diagnosis System** Neo4j知识图谱（241证型/1263症状）+四阶段症状匹配（含LLM验证）+信息增益主动问诊的中医可视化诊疗系统 [[论文](https://arxiv.org/abs/2606.06869)]
- **儿童流感中成药推荐系统（KG+LLM）** 整合权威指南构建儿童流感中成药知识图谱并与LLM集成（JMIR Preprints预印本） [[预印本](https://doi.org/10.2196/preprints.101648)]
- [*Frontiers in Medicine*] **靳三针知识图谱问答 (Jin San Zhen KG-QA)** 靳三针针灸流派知识图谱+大模型问答工具 [广州中医药大学] [[DOI](https://doi.org/10.3389/fmed.2026.1755583)]
- [*Frontiers in Medicine*] **树状自反思检索中医问答** 树状组织语料+自反思检索的中医 QA 方法（Frontiers in Medicine 2026） [澳门科技大学] [[DOI](https://doi.org/10.3389/fmed.2026.1752778)]
- [*Frontiers in Medicine*] **TCM-DiffRAG** 通用知识图谱 + 个性化知识图谱 + CoT 的辨证推理 RAG 框架 [Guangdong Institute of Intelligence Science and Technology, Zhuhai，Hangzhou Ganzhicao Technology Co., Ltd，BoardWare Information System Limited] [[正式发表](https://doi.org/10.3389/fmed.2026.1804478)] [[论文](https://arxiv.org/abs/2602.22828)] [[代码](https://github.com/LiJianmin6706/Tcm_Diff_RAG)]

</details>

<details>
<summary>2025 · 12</summary>

- [*IEEE BIBM 2025*] **中成药知识体系构建** LLM+知识图谱构建中成药知识体系 [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356149)]
- [*数据分析与知识发现*] **中医药标准知识问答系统** 检索增强技术构建中医药标准知识问答系统的探索与实践 [中国中医科学院等] [[DOI](https://doi.org/10.11925/infotech.2096-3467.2024.0747)]
- [*Frontiers in Medicine*] **中医医案问答系统** 融合大语言模型与知识图谱的中医医案问答系统，提升医案检索与分析效率（Frontiers in Medicine 2025） [安徽中医药大学] [[DOI](https://doi.org/10.3389/fmed.2024.1512329)]
- [*JMIR Medical Informatics*] **Yaoshi-RAG（药食同源RAG）** 基于不确定知识图谱的药食同源膳食推荐RAG，提升LLM个性化与可解释性 [[DOI](https://doi.org/10.2196/75279)]
- [*Frontiers in Pharmacology*] **TCMRD-KG** 基于古籍文献的风湿病中医知识图谱创新设计 [北京中医药大学] [[DOI](https://doi.org/10.3389/fphar.2025.1535596)]
- [*Digital Chinese Medicine*] **TCMLCM** 基于KG2T的中医肺癌智能问答模型 [南京中医药大学] [[DOI](https://doi.org/10.1016/j.dcmed.2025.03.011)]
- **TCM-Sage** 面向中医师的证据合成RAG助手（混合向量+知识图谱） [[代码](https://github.com/AndyZHENG0715/TCM-Sage)]
- [*Pharmacological Research*] **RAG-CPMF** 多LLM校验+RAG的中成药智能推荐框架，并发布持续更新的大规模中成药公开数据集 [[DOI](https://doi.org/10.1016/j.phrs.2025.107883)] [[数据](https://gitee.com/tcmdoc/cpm)]
- [*arXiv*] **OpenTCM** 基于 GraphRAG 的中医知识检索与诊断系统，含妇科古籍知识图谱 [[论文](https://arxiv.org/abs/2504.20118)] [[代码](https://github.com/OpenTCM01/OpenTCM)]
- [*IEEE BIBM*] **MRD-RAG** 模拟临床推理的多轮诊断RAG框架，并构建覆盖中西医的**DiagnosGraph**（876病/7997节点/37201三元组） [香港科技大学] [[正式发表](https://doi.org/10.1109/bibm66473.2025.11357107)] [[论文](https://arxiv.org/abs/2504.07724)]
- [*Interdisciplinary Sciences*] **LLM驱动中医知识图谱构建** LLM驱动的中医知识图谱构建与应用 [河南工业大学] [[DOI](https://doi.org/10.1007/s12539-025-00735-1)]
- [*Journal of Medical and Biological Engineering*] **LLM+RAG中医推理** LLM与RAG结合的中医推理方法 [台北市立联合医院] [[DOI](https://doi.org/10.1007/s40846-025-00988-7)]

</details>

<details>
<summary>2024 · 8</summary>

- [*JMIR Medical Informatics*] **中医领域知识图谱补全** 中医领域知识图谱补全与质量评估研究 [Zhejiang Chinese Medical University，Guangdong Provincial Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2196/55090)]
- [*南京中医药大学学报*] **中医药问答大语言模型** RAG 结合 P-Tuning v2 微调的中医药问答大模型（ChatGLM2-6B） [南京中医药大学] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1375)]
- [*计算机科学与探索*] **中医药大模型知识增强方法** 面向中医药大模型的知识增强方法，基于约十万首经典方剂构建图谱并保持方剂结构性 [天津大学] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2407082)]
- [*Methods of Information in Medicine*] **TCMSF** 中医证候古籍知识图谱构建框架 TCMSF，将古籍中的证候知识系统化组织并语义关联，为中医信息化提供基础（Methods of Information in Medicine 2024） [中国中医科学院] [[DOI](https://doi.org/10.1055/a-2590-6348)]
- [*EIECC*] **TCM MLKG-RAG** 多层知识图谱检索增强生成的中医智能诊断 [University of Science and Technology of China] [[DOI](https://doi.org/10.1109/EIECC64539.2024.10929529)]
- [*OSF Preprints（预印本）*] **RAG 增强中医问答置信度** 检索增强生成提升大模型中医问答置信度（预印本） [[DOI](https://doi.org/10.31219/osf.io/ns2v3)]
- [*Electronics*] **LLM 构建中医知识图谱** 基于大语言模型的中医知识图谱构建 [同济大学] [[DOI](https://doi.org/10.3390/electronics13071395)]
- [*Database (Oxford)*] **ACUBERT** 针灸适应证知识库的经络实体识别与分类模型 [南京中医药大学，Nanjing KG Data Technology] [[DOI](https://doi.org/10.1093/database/baae083)]

</details>

<details>
<summary>2023 · 1</summary>

- [*计算机科学与探索*] **大模型融合知识图谱问答系统** LLM 与知识图谱深度融合的中医药方剂垂直领域问答系统 [天津大学] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2308070)]

</details>


</details>

<details>
<summary>处方 / 组方（11）：荐药、组方、药对</summary>

- [*arXiv*] **Patient-Conditioned Dual Hypergraph Reasoning** 患者条件化双超图推理实现可审计的中医处方支持，将症状/舌/脉证据围绕证型与治则组织（天津大学） [[论文](https://arxiv.org/abs/2607.04025)]
- [*KSII Transactions on Internet and Information Systems*] **GAT+LLM TCM Prescription Generation** 图注意力网络与LLM结合的中医处方智能生成模型（KSII TIIS正式发表） [[DOI](https://doi.org/10.3837/tiis.2026.05.006)]
- [*Chinese Medicine*] **TCMNet** LLM辅助疾病知识挖掘+PPI网络与结合预测的方剂优化策略 [浙江省中医药研究院] [[DOI](https://doi.org/10.1186/s13020-026-01360-w)]
- [*Digital Chinese Medicine*] **CMM-EmbedCluster** 基于LLM与药性理论的中药聚类框架，构建567味药性知识库 [南京中医药大学] [[DOI](https://doi.org/10.1016/j.dcmed.2026.05.010)]
- [*IEEE Journal of Biomedical and Health Informatics*] **草药-药物相互作用预测** LLM增强的草药-药物相互作用预测 [深圳大学] [[DOI](https://doi.org/10.1109/jbhi.2025.3558667)]
- [*JMIR Medical Informatics*] **中医方剂分类加权投票** LLM加权投票中医方剂分类方法 [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.2196/69286)]
- [*IEEE BIBM*] **TCM-FTP** 面向中药处方预测的大模型微调方法 [香港科技大学，北京交通大学，中国中医科学院，河南中医药大学] [[DOI](https://doi.org/10.1109/BIBM62325.2024.10822451)]
- [*JAMIA*] **PresRecST** 按「辨证—立法—荐药」递进推荐中药处方（JAMIA 2024）；配套公开 TCM-Lung 编码子集与 TCM-PD 复现表，代码在 GitHub [北京交通大学，中国中医科学院，河南中医药大学] [[DOI](https://doi.org/10.1093/jamia/ocae066)] [[代码](https://github.com/2020MEAI/PresRecST)]
- [*IEEE BIBM*] **中医方剂 LLM 分类** 微调大语言模型并结合提示模板进行中医方剂分类，数据源自中成药国家医保目录等（IEEE BIBM 2023） [Leipzig University，Changchun University of Chinese Medicine，Liaoning Technical University，Sichuan Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385776)]
- [*IEEE Access*] **PreGenerator** 检索与生成方法结合的中医处方推荐模型 [College of Physics, Taiyuan University of Technology, Taiyuan, China，North Automatic Control Technology Institute, Taiyuan, China] [[DOI](https://doi.org/10.1109/ACCESS.2023.3316219)]
- [*IEEE BIBM*] **LLM+GNN 中医处方推荐** 大语言模型与图神经网络结合的中医处方推荐模型 [南京中医药大学] [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385489)]

</details>

<details>
<summary>抽取 / 编码器（5）：NER、关系抽取、BERT 类编码器</summary>

- [*Applied Intelligence*] **KDC-NER** 知识引导数据增强+大模型微调的中医嵌套命名实体识别框架 [江西中医药大学] [[DOI](https://doi.org/10.1007/s10489-026-07095-3)]
- [*npj Digital Medicine*] **补充替代医学文献抽取语言模型** 用于补充替代医学文献数据抽取与偏倚风险评估的语言模型 [兰州大学] [[DOI](https://doi.org/10.1038/s41746-025-01457-w)]
- [*Scientific Reports*] **双通道知识注意力辨证模型** 双通道知识注意力的中医辨证NLP模型，缓解生僻字与术语抽取难题 [[DOI](https://doi.org/10.1038/s41598-025-96404-w)]
- [*Journal of the American Medical Informatics Association*] **LLM 腧穴定位关系抽取** 大语言模型关系抽取案例研究：腧穴定位知识 [中国中医科学院，The University of Texas MD Anderson Cancer Center , Houston, TX 77030] [[DOI](https://doi.org/10.1093/jamia/ocae233)]
- [*Frontiers in Artificial Intelligence*] **Evi-BERT** 中医RCT证据自动抽取的信息抽取模型开发与验证 [北京航空航天大学，北京中医药大学] [[DOI](https://doi.org/10.3389/frai.2024.1454945)]

</details>

<details>
<summary>评测论文（39）：基准和考试；要下载评测集走下面「数据集」</summary>

<details>
<summary>2026 · 14</summary>

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

</details>

<details>
<summary>2025 · 16</summary>

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

</details>

<details>
<summary>2024 · 7</summary>

- [*南京中医药大学学报*] **中医标准化评估基准** 覆盖13个学科共29506道题的中医测评基准，系统评测3个通用模型与5个中文医疗模型 [成都中医药大学] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1383)]
- [*arXiv*] **TCMD** 面向大模型评测的中医执业考试选择题集（论文报告约 2851 训 / 600 测）；独立打开论文页未见官方 GitHub 或 Hugging Face 下载 [[论文](https://arxiv.org/abs/2406.04941)]
- [*Journal of Translational Medicine*] **LLM 中医语言文化偏差研究** 比较不同国家大模型的中医表现，论证本土化模型的必要性 [Zhujiang Hospital，Southern Medical University，Shanghai Jiao Tong University，Shanghai First People's Hospital] [[DOI](https://doi.org/10.1186/s12967-024-05128-4)]
- [*Research Square（预印本）*] **GPT-4 中医研究生考试评估** GPT-4 与国产主流大模型在中医研究生考试数据集上的表现评估（预印本） [China Academy of Chinese Medical Science，中国中医科学院，北京中医药大学，Changchun University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.21203/rs.3.rs-4392855/v1)]
- [*J Integr Complement Med*] **GPT vs ERNIE 中医文化背景对比研究** 以文化背景为框架对比 GPT 与 ERNIE 在中医任务上的表现（J Integr Complement Med 2024） [北京大学，College of Engineering, Boston University, Boston, MA, USA.] [[DOI](https://doi.org/10.1089/jicm.2024.0902)]
- [*arXiv*] **ChatGPT 中医知识理解探究** ChatGPT 对中医知识理解能力的评测 [[论文](https://arxiv.org/abs/2403.09164)]
- [*Chinese Medicine and Culture*] **ChatGPT 中医交互可行性研究** 以 ChatGPT 为例探讨交互式AI应用于中医的可行性与挑战 [上海中医药大学] [[DOI](https://doi.org/10.1097/MC9.0000000000000103)]

</details>

<details>
<summary>2023 · 2</summary>

- **中医新冠文献 LLM 命名实体识别** 大语言模型用于中医新冠文献命名实体识别的比较研究（预印本） [[DOI](https://doi.org/10.2196/preprints.54346)]
- [*JMIR Medical Education*] **ChatGPT 针灸教育研究** ChatGPT 作为针灸学习工具的对照研究 [Seoul National University Hospital] [[DOI](https://doi.org/10.2196/47427)]

</details>


</details>

<details>
<summary>平台 / 工具（4）：编目、门户、可运行工具</summary>

- [*arXiv*] **TCMIIES** 浏览器端零安装的LLM学术文献结构化信息抽取系统，面向中医等专科领域研究者 [[论文](https://arxiv.org/abs/2605.07507)]
- [*Science of Traditional Chinese Medicine*] **TCM Data Hub（谊元）** 谊元 (YiYuan) LLM驱动的中医数据平台 [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.1097/st9.0000000000000118)]
- [*Cell Discovery*] **神农Alpha** 西湖大学神农 Alpha：AI 驱动的天然药物知识智能编目、获取与翻译共享协作平台（Cell Discovery 2025） [西湖大学] [[DOI](https://doi.org/10.1038/s41421-025-00776-2)] [[网站](https://shennongalpha.westlake.edu.cn/)] [[论文](https://www.nature.com/articles/s41421-025-00776-2)] [[代码](https://github.com/shennong-program/shennongname)]
- [*IJACSA*] **草药智能配送聊天机器人** AI 聊天机器人驱动的智能草药配送系统 [University of the Cordilleras，Naresuan University Hospital，Catanduanes State University] [[DOI](https://doi.org/10.14569/ijacsa.2023.0140358)]

</details>

<details>
<summary>其他方法（6）：对齐、提示、专科任务</summary>

- [*Translation Review*] **Beyond the Poetic Bard（中医AI翻译评论）** 讨论生成式AI翻译中医文本的精确性、认识论与医学语境局限（Translation Review） [[DOI](https://doi.org/10.1080/07374836.2026.2679929)]
- [*生物化学与生物物理进展*] **病机推理CoT监督（脾胃病）** 以病机推理思维链监督替代固定标签分类，做脾胃病症候表现识别与多维评估（《生物化学与生物物理进展》） [[论文](https://www.pibb.ac.cn/pibbcn/article/abstract/20260141)]
- [*arXiv*] **中医提示工程框架** 基于提示工程框架的大语言模型中医智能理解方法 [[论文](https://arxiv.org/abs/2410.19451)]
- [*arXiv*] **RLAIF 中医对齐** 通过AI反馈强化学习增强大语言模型的中医能力 [[论文](https://arxiv.org/abs/2411.00897)]
- [*Digital Chinese Medicine*] **BSG 中医智能问答** 基于 BSG 深度学习模型的中医智能问答系统（方剂与中药实例） [Hunan University of Traditional Chinese Medicine，Central South University] [[DOI](https://doi.org/10.1016/j.dcmed.2024.04.006)]
- [*IEEE BIBM*] **中医疫病防治问答模型** 基于大语言模型的中医疫病防治问答模型 [南京中医药大学] [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385748)]

</details>

<details>
<summary>更早的工作（50）：专家系统、舌脉、本体、早期编码器</summary>

<details>
<summary>2020–2022 · 16</summary>

- [*Discover Applied Sciences*] **Mathematical modeling of Chinese medicine by complex-valued five-agent network** 复值五智能体网络统一阴阳互补与五行反馈的线性代数表述。 [National Cheng Kung University] [[DOI](https://doi.org/10.1007/s42452-025-06602-4)]
- [*Lv Q et al., *Signal Transduct Target Ther* 8(1):127*] **TCMBank** TCMBank（platform阶段历史锚点） [中山大学，澳门科技大学] [[DOI](https://doi.org/10.1038/s41392-023-01339-1)]
- [*Interdisciplinary*] **Historical Analysis of Medical Artificial Intelligence Development in China: Research Cent** 以中医专家系统为中心的中国医学 AI 发展史梳理（二次文献锚点；作者以 DOI 页为准）。 [Okayama University of Science，Okayama University] [[DOI](https://doi.org/10.18926/interdisciplinary/65464)]
- [*Zhang Y et al., *Acta Pharm Sin B* 13(6):2559-2571*] **ETCM v2.0** ETCM v2.0（platform阶段历史锚点） [中国医学科学院，中国科学院，Shanghai Institute of Materia Medica，Guiyang Medical University] [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)]
- [*Scientific Reports*] **Discovering golden ratio in the world’s first five-agent network in ancient China** 用多智能体网络理论量化五行和谐稳态，并给出电路/编队实验验证。 [National Cheng Kung University] [[DOI](https://doi.org/10.1038/s41598-023-46071-6)]
- [*BioMed Research International*] **乙肝中医 KG 问答系统** 基于知识图谱的中医诊治病毒性乙型肝炎问答系统 [中国中医科学院，First Affiliated Hospital of Henan University] [[DOI](https://doi.org/10.1155/2022/7139904)]
- [*CCL*] **ZY-BERT** TCM-SD 同文提出的中医领域预训练编码器（约 0.4B token 语料）；权重在网盘，仓库另含辨证微调代码。与 2411.00897 RLAIF 文不是同一工作 [[论文](https://arxiv.org/abs/2203.10839)] [[正式发表](https://aclanthology.org/2022.ccl-1.80/)] [[代码](https://github.com/Borororo/ZY-BERT)]
- [*BioMed Research International*] **TCMPR 子网术语映射处方推荐** 草药-症状知识图谱（1.8 万实体 / 10 万关系）+ 子网术语映射，用 CNN 做处方推荐 [北京交通大学，清华大学] [[DOI](https://doi.org/10.1155/2022/4845726)]
- [*Digital Health*] **Research and application of tongue and face diagnosis based on deep learning** 舌面诊深度学习预处理/分割/分类技术路线综述与验证。 [成都中医药大学] [[DOI](https://doi.org/10.1177/20552076221124436)]
- [*Evid. Based Complement. Alternat. Med.*] **Deep Learning Multi-label Tongue Image Analysis and Its Application in a Population Underg** Faster R-CNN 多标签舌象（裂纹/齿痕/腻苔等）及体检人群关联分析。 [上海中医药大学，复旦大学] [[DOI](https://doi.org/10.1155/2022/3384209)]
- [*Digital Chinese Medicine*] **Data-driven based four examinations in TCM: a survey** 数据驱动四诊（含深度学习）设备—算法—数据集全景。 [Beijing University of Civil Engineering and Architecture，University of Maryland, Baltimore，Shandong University] [[DOI](https://doi.org/10.1016/j.dcmed.2022.12.004)]
- [*JMIR Medical Informatics*] **Ensemble Learning-Based Pulse Signal Recognition: Classification Model Development Study** SVM（时/频域结构特征）与 DCNN 决策级融合的脉象识别。 [华东理工大学，上海中医药大学] [[DOI](https://doi.org/10.2196/28039)]
- [*IEEE Trans. Cybernetics*] **Automatic Construction of Chinese Herbal Prescriptions From Tongue Images Using CNNs and A** 舌象→方剂端到端生成，引入治法主题辅助损失。 [South China University of Technology，Guangdong General Hospital] [[DOI](https://doi.org/10.1109/tcyb.2019.2909925)]
- [*BMC Medical Informatics and Decision Making*] **中医临床细粒度 NER 语料** 基于中医临床病历构建细粒度实体识别语料 [成都中医药大学，Chengdu University of Information Technology] [[DOI](https://doi.org/10.1186/s12911-020-1079-2)]
- [*IEEE ICKG*] **TCMKG** 基于深度学习的中医知识图谱平台 [University of Electronic Science and Technology of China，成都中医药大学] [[DOI](https://doi.org/10.1109/ICBK50248.2020.00084)]
- [*Comput. Struct. Biotechnol. J.*] **Artificial intelligence in tongue diagnosis: Using deep convolutional neural network for r** ResNet34 齿痕舌识别，强调跨设备泛化。 [Being University of Chinese Medicine, Beijing 100029, China，Beijing University of Posts and Telecommunications, Beijing 100876, China，Beijing Normal University, Beijing 100875, China，中国科学院] [[DOI](https://doi.org/10.1016/j.csbj.2020.04.002)]

</details>

<details>
<summary>2010s · 19</summary>

- [*IEEE Trans. Cybernetics*] **Tooth-Marked Tongue Recognition Using Multiple Instance Learning and CNN Features** CNN 特征+多示例学习识别齿痕舌，标志舌诊进入深度学习。 [Shanghai University，Shanghai University of Engineering Science] [[DOI](https://doi.org/10.1109/tcyb.2017.2772289)]
- [*JAMIA*] **TCM-BERT** 用领域语料继续预训练 BERT，把中医临床记录分成五类病（JAMIA 2019）。CKCEST 版权，全量 46205 条不公开，仓库只有划分样例和网盘微调权重 [美国西北大学，浙江大学] [[DOI](https://doi.org/10.1093/jamia/ocz164)] [[代码](https://github.com/yao8839836/tcm_bert)]
- [*Xu HY et al., *Nucleic Acids Res* 47(D1):D976-D982*] **ETCM** ETCM（platform阶段历史锚点） [中国中医科学院，北京大学，中国科学院] [[DOI](https://doi.org/10.1093/nar/gky987)]
- [*BMC Medical Informatics and Decision Making*] **An ontological framework for the formalization, organization and usage of TCM-Knowledge** 基于 GFO 的 GFO-TCM 中层本体，修正 TCMLS-SN 语义问题。 [Leipzig University，中国医学科学院，中国中医科学院] [[DOI](https://doi.org/10.1186/s12911-019-0760-9)]
- [*IEEE IAEAC*] **语义中医方剂知识图谱 (Miao et al. 2018)** 自顶向下建本体、从方剂文本抽实体关系，构建语义方剂知识图谱 [Communication University of China，Academy of Broadcasting Science] [[DOI](https://doi.org/10.1109/IAEAC.2018.8577236)]
- [*CISP-BMEI*] **Constitution Identification of Tongue Image Based on CNN** CNN 舌象体质辨识，对比传统手工特征 ML。 [Beijing University of Technology] [[DOI](https://doi.org/10.1109/cisp-bmei.2018.8633075)]
- [*Artificial Intelligence in Medicine*] **中医养生知识图谱 (Yu et al. 2017)** 整合术语、文献与数据库的大规模中医养生知识图谱，支持检索、可视化与推荐 [北京中医药大学，中国中医科学院] [[DOI](https://doi.org/10.1016/j.artmed.2017.04.001)]
- [*BioMed Research International*] **Diagnostic Method of Diabetes Based on Support Vector Machine and Tongue Images** 标准化舌象+SVM/PCA/GA 的糖尿病筛查模型。 [上海中医药大学] [[DOI](https://doi.org/10.1155/2017/7961494)]
- [*IEEE BIBM*] **中医期刊关系抽取 (Wang & Poon 2016)** 从中医期刊全文做关系抽取，为后续知识图谱构建提供方法 [The University of Sydney] [[DOI](https://doi.org/10.1109/BIBM.2016.7822725)]
- [*Ru J et al., *J Cheminform* 6(1):13*] **TCMSP** TCMSP（platform阶段历史锚点） [North West Agriculture and Forestry University，Northwest A&F University，Dalian University of Technology，Dalian University] [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- [*Comput. Math. Methods Med.*] **Pulse Waveform Classification Using Support Vector Machine with Gaussian Time Warp Edit Di** GTWED-SVM 在 2470 条五类脉波上的弹性核分类。 [Harbin Ice Flower Hospital, Harbin 150086, China，哈尔滨工业大学] [[DOI](https://doi.org/10.1155/2014/947254)]
- [*Evid. Based Complement. Alternat. Med.*] **A disturbance rejection framework for the study of traditional Chinese medicine** 用工程控制论“抗扰”隐喻解释五行调控与治法逻辑。 [Cleveland State University，北京中医药大学] [[DOI](https://doi.org/10.1155/2014/787529)]
- [*Journal of Biomedical Informatics*] **中医症状名识别** 自由文本中医临床记录中症状名识别的监督方法 [四川大学，成都中医药大学，Sichuan Agricultural University，Beihua University] [[DOI](https://doi.org/10.1016/j.jbi.2013.09.008)]
- [*Xue R et al., *Nucleic Acids Res* 41(D1):D1089-D1095*] **TCMID** TCMID（platform阶段历史锚点） [Shanghai Jiao Tong University，四川大学，Shanghai Mental Health Center，华东师范大学] [[DOI](https://doi.org/10.1093/nar/gks1100)]
- [*Evid. Based Complement. Alternat. Med.*] **Automated Tongue Feature Extraction for ZHENG Classification in Traditional Chinese Medici** 舌象颜色特征学习映射寒热证（ZHENG）的代表性工作。 [清华大学] [[DOI](https://doi.org/10.1155/2012/912852)]
- [*Journal of Biomedical Informatics*] **Text mining for traditional Chinese medical knowledge discovery: a survey** 中医文本挖掘方法与语料资源的早期系统综述。 [北京交通大学，University of Bradford，中国医学科学院] [[DOI](https://doi.org/10.1016/j.jbi.2010.01.002)]
- [*Journal of Chinese Integrative Medicine*] **Feature extraction and recognition of traditional Chinese medicine pulse based on hemodyna** 以波速与反射系数作脉象特征并用 SVM 识别弦/滑/平脉。 [[链接](http://www.jcimjournal.com/EN/10.3736/jcim20100802)]
- [*Artificial Intelligence in Medicine*] **Development of traditional Chinese medicine clinical data warehouse for medical knowledge ** 临床数据仓库支撑知识发现与决策支持的系统论文。 [北京交通大学，中国中医科学院，北京中医药大学，Guang’anmen Hospital] [[DOI](https://doi.org/10.1016/j.artmed.2009.07.012)]
- [*EURASIP J. Adv. Signal Process.*] **Classification of Pulse Waveforms Using Edit Distance with Real Penalty** ERP 编辑距离应对脉波局部时移的经典波形分类。 [哈尔滨工业大学] [[DOI](https://doi.org/10.1155/2010/303140)]

</details>

<details>
<summary>2000s · 10</summary>

- [*IEEE CSIE*] **Syndrome Differentiation in Intelligent TCM Diagnosis System** 区间值直觉模糊集用于智能中医辨证决策。 [Xiamen University] [[DOI](https://doi.org/10.1109/csie.2009.782)]
- [*Int. J. Information Technology & Decision Making*] **Equilibrium and nonequilibrium modeling of YinYang WuXing for diagnostic decision support ** 双极线性代数刻画阴阳五行均衡/非均衡并原型化诊断 DSS。 [中国科学院] [[DOI](https://doi.org/10.1142/s0219622009003521)]
- [*IEEE ITME*] **Traditional Chinese medical diagnosis based on fuzzy and certainty reasoning** 多层模糊筛选+多智能体协作诊断（MADHS）原型。 [Memorial University of Newfoundland] [[DOI](https://doi.org/10.1109/itme.2008.4743874)]
- [*WWW* (demo/industrial)*] **Information retrieval and knowledge discovery on the semantic web of traditional Chinese m** 大规模中医语义网与草药—药物相互作用图谱挖掘。 [浙江大学] [[DOI](https://doi.org/10.1145/1367497.1367668)]
- [*Journal of Chinese Integrative Medicine*] **Establishment of a fuzzy mathematical model for syndrome differentiation of gastric cancer** 基于临床大样本的胃癌证候模糊数学模型，服务辨证客观化。 [[链接](http://www.jcimjournal.com/EN/10.3736/jcim20081104)]
- [*IEEE BMEI*] **Building Clinical Data Warehouse for Traditional Chinese Medicine Knowledge Discovery** 结构化病历驱动的中医临床数据仓库与 OLAP/挖掘平台。 [北京交通大学，中国医学科学院，Guang’anmen Hospital，北京中医药大学] [[DOI](https://doi.org/10.1109/bmei.2008.83)]
- [*IEEE SITIS*] **A Novel Computerized Method Based on Support Vector Machine for Tongue Diagnosis** 色纹理特征+SVM/贝叶斯网络的早期计算机舌诊。 [南京大学，City University of Hong Kong] [[DOI](https://doi.org/10.1109/sitis.2007.115)]
- [*Artificial Intelligence in Medicine*] **Knowledge discovery in traditional Chinese medicine: State of the art and perspectives** 方剂/本草/证候/诊断四子域的早期 KDD 综述。 [浙江大学] [[DOI](https://doi.org/10.1016/j.artmed.2006.07.005)]
- [*Information Sciences*] **YinYang bipolar logic and bipolar fuzzy logic** 阴阳双极逻辑/模糊逻辑，为后续 YYWX 代数模型奠基。 [Georgia Southern University，The University of Texas at Austin] [[DOI](https://doi.org/10.1016/j.ins.2003.05.010)]
- [*Artificial Intelligence in Medicine*] **Ontology development for unified traditional Chinese medical language system** UTCMLS/TCMLS 本体工程奠基作，对标 UMLS 思路。 [浙江大学，Sichuan Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.artmed.2004.01.014)]

</details>

<details>
<summary>1970s–1990s · 5</summary>

- [*Complementary Therapies in Medicine*] **A computer model of the “five elements” theory of traditional Chinese medicine** 布尔网络模拟五行吸引子及扰动对稳态的影响。 [University of Verona，University of Perugia] [[DOI](https://doi.org/10.1016/S0965-2299(98)80005-8)]
- [*Physica Scripta*] **Functional structure model of human body and Yinyang-Wuxing equations** 早期以微分方程刻画人体五行功能子系统与经络自组织。 [University of Science and Technology of China] [[DOI](https://doi.org/10.1088/0031-8949/36/6/015)]
- [*Fuzzy Sets and Systems*] **Fuzzy match and floating threshold strategy for expert system in traditional Chinese medicine** 模糊匹配+浮动阈值，把不确定性引入中医辨证专家系统。 [Beijing Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/0165-0114(85)90052-1)]
- [*医院史料：*] **关幼波肝病诊疗程序（肝病专家系统）** 国内公认最早投入使用的中医名老中医经验计算机诊疗程序（1979.1）。 [[链接](https://www.bjzhongyi.com/gzb_mygs_detail/4656.html)]
- [*Computers and Biomedical Research*] **An artificial intelligence program to advise physicians regarding antimicrobial therapy** MYCIN 前身，规则型医学专家系统范式（中医专家系统的方法学参照）。 [Stanford University] [[DOI](https://doi.org/10.1016/0010-4809(73)90029-3)]

</details>


</details>

## 数据集

按用途点开。官网挂了的标「官网已挂」，门户在但核心功能不通的标「服务异常」，都仍收论文/镜像；想对一下评测集，看 [Datasets](wiki/Datasets.md) 和 [Benchmarks](wiki/Benchmarks.md)。

<details>
<summary>公开资料整理（2）</summary>

- **awesome_Chinese_medical_NLP** — 中文医学 NLP 公开资源整理：术语集、语料库、词向量、预训练模型、知识图谱、NER、QA 等（含 CBLUE 挑战榜） [[资料](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)]
- **中成药公开数据集（RAG-CPMF）** — RAG-CPMF配套的持续更新大规模中成药公开数据 [[数据](https://gitee.com/tcmdoc/cpm)] [[论文](https://doi.org/10.1016/j.phrs.2025.107883)]

</details>

<details>
<summary>中药组方 / 提取物（23）</summary>

- **HERB 2.0 本草组鉴** — 整合临床试验、荟萃分析、高通量实验与文献的中药证据库，并提供实体关系知识图谱 [[网站](http://herb.ac.cn/v2)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11701625/)] [[DOI](https://doi.org/10.1093/nar/gkae1037)]
- **CMAUP 有用植物集体分子活性库** — BIDD的有用植物（含中药）多靶点活性、通路与疾病景观库，2024版扩展功能与关联信息，站点可下载 [[网站](https://www.bidd.group/CMAUP/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767869/)] [[DOI](https://doi.org/10.1093/nar/gkad921)]
- **BATMAN-TCM 2.0 中药成分–靶点注释库** — 已知与预测的中药成分–靶蛋白相互作用库，2.0大幅扩充TTI覆盖并支持由靶反查成分 [[网站](http://bionet.ncpsb.org.cn/batman-tcm/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767940/)] [[DOI](https://doi.org/10.1093/nar/gkad926)]
- **TCMBank 中药–成分–靶点–疾病库** — 可下载的大规模中药–成分–靶点–疾病关系库，含文献自动抽取后人工核对的持续更新模块 [[网站](http://tcmbank.cn/)] [[DOI](https://doi.org/10.1038/s41392-023-01339-1)]
- **ITCM 整合中医药与药效转录组平台** — 整合多方剂/药材/成分/靶点，并提供496个中药成分的1488条药理转录谱；成分表达数据另见Synapse [[网站](http://itcm.biotcm.net/)] [[DOI](https://doi.org/10.1093/bib/bbad027)]
- **ETCM 2.0 中医药百科全书** — 收录古代方剂、中成药、药材与成分，并提供成分靶点与多尺度网络；v1站点仍在，现行入口为ETCM2 [[网站](http://www.tcmip.cn/ETCM2/front/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10326295/)] [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)]
- **DCABM-TCM 中药入血成分与代谢物库** — 文献挖掘的方剂/草药入血原型与代谢物及其检测条件（约1816个有结构入血成分） [[网站](http://bionet.ncpsb.org.cn/dcabm-tcm/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10428213/)]
- **LTM-TCM 中西医分子表型链接库**（官网已挂） — 整合十四个权威库与临床/古籍记录的症状–方剂–植物–成分–靶点平台（约4.8万方）；官网cloud.tasly.com域名已无法解析，核验走论文DOI [[原网站](http://cloud.tasly.com/#/tcm/home)] [[DOI](https://doi.org/10.1016/j.phrs.2022.106185)]
- **HIT 2.0 草药成分靶点库**（服务异常） — 人工审核的草药成分–靶点活性对（约1237成分/2208靶点），覆盖2000–2020文献；门户可打开，分析后端端口当前不通 [[网站](http://hit2.badd-cao.net/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728248/)] [[DOI](https://doi.org/10.1093/nar/gkab1011)]
- **SuperTCM 中药生物文化数据库**（官网已挂） — Charité团队整合药典与多源数据的中药–物种–成分–靶点–通路–疾病库（约6516味药）；官网tcm.charite.de已无法解析 [[原网站](http://tcm.charite.de/supertcm)] [[论文](https://europepmc.org/article/MED/34656056)] [[DOI](https://doi.org/10.1016/j.biopha.2021.112315)]
- **TCMIO 中医药免疫肿瘤学数据库** — 面向免疫肿瘤的中药/方剂–成分–靶点–通路库，提供浏览、下载与REST API [[网站](http://tcmio.xielab.net/)] [[数据](http://tcmio.xielab.net/download)] [[DOI](https://doi.org/10.3389/fphar.2020.00439)]
- **SymMap 2.0 症状映射中医药数据库** — 草药–中医症状–西医症状–成分–靶点–疾病整合库，2.0按新版药典扩草药/证候并开放关系表下载 [[网站](http://www.symmap.org/)] [[数据](http://www.symmap.org/download/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323958/)]
- **YaTCM 中药方剂–成分–靶点库**（官网已挂） — 约1813首方、6220味药、4.7万天然产物及靶点/通路分析工具；南开官网当前403，核验走开放论文 [[原网站](http://cadd.pharmacy.nankai.edu.cn/yatcm/home)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6280608/)] [[DOI](https://doi.org/10.1016/j.csbj.2018.11.002)]
- **TCMID 2.0 中医药整合数据库**（官网已挂） — 上海团队的方剂–草药–成分–靶点整合库（与NUS的TCM-ID不是同一库）；官网megabionet已不可达，公开核验走Zenodo摘录与NAR论文 [[原网站](http://www.megabionet.org/tcmid/)] [[数据](https://zenodo.org/records/8066910)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5753259/)] [[DOI](https://doi.org/10.1093/nar/gkx1028)]
- **TCMAnalyzer 中药化学信息学分析平台**（官网已挂） — 中山大学RCDD的方剂/药材/成分网络分析与骨架检索服务（约1493方、618味药）；官网rcdd.org.cn当前超时 [[原网站](http://www.rcdd.org.cn/tcmanalyzer)] [[论文](https://pubmed.ncbi.nlm.nih.gov/29425456/)] [[DOI](https://doi.org/10.1021/acs.jcim.7b00549)]
- **TCM-Mesh 中药网络药理学分析库**（官网已挂） — 草药–化合物–基因–疾病网络与毒副作用记录（约6235味药）；官网当前403，核验走开放论文 [[原网站](http://mesh.tcm.microbioinformatics.org/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5460194/)] [[DOI](https://doi.org/10.1038/s41598-017-03039-7)]
- **TM-MC 东北亚传统药物成分库**（官网已挂） — 韩国韩医学研究院从文献抽取的东北亚药材–化合物库；2015初版约536种药材，2024的2.0扩到约3.4万化合物；官网当前超时 [[原网站](http://informatics.kiom.re.kr/compound/)] [[DOI](https://doi.org/10.1186/s12906-015-0758-5)] [[2.0论文](https://doi.org/10.1186/s12906-023-04331-y)]
- **CEMTDD 中国少数民族传统药物数据库**（官网已挂） — 以新疆维吾尔/哈萨克等民族药为主的草药–化合物–靶点–疾病库（约621草药）；原域名cemtdd.com已改作他用，核验走PMC论文 [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627337/)] [[DOI](https://doi.org/10.18632/oncotarget.3789)]
- **TCMSP 中药系统药理学数据库** — 草药–成分–靶点–疾病网络与ADME参数平台，现行公开站为TCMSP 2.3，提供草药/分子/靶点关系表下载 [[网站](https://www.tcmsp-e.com/tcmsp.php)] [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- **CVDHD 心血管病本草数据库**（官网已挂） — 面向心血管病的本草化合物三维结构、靶点与通路库，用于虚拟筛选与网络药理；原北大站点当前超时 [[原网站](http://pkuxxj.pku.edu.cn/CVDHD)] [[DOI](https://doi.org/10.1186/1758-2946-5-51)]
- **TCM Database@Taiwan 中药三维结构库**（官网已挂） — 453味药材中约2万个分离化合物的2D/3D结构库，面向虚拟筛选；原站tcm.cmu.edu.tw已不可达，核验走PLOS论文页 [[原网站](http://tcm.cmu.edu.tw/)] [[论文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0015939)] [[DOI](https://doi.org/10.1371/journal.pone.0015939)]
- **TCMGeneDIT 中药–基因–疾病文本挖掘库**（官网已挂） — 从文献挖掘中药、基因、疾病、功效与成分关联，并接入通路与PPI；官网tcm.lifescience.ntu.edu.tw已无法解析 [[原网站](http://tcm.lifescience.ntu.edu.tw/)] [[论文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2582235/)] [[DOI](https://doi.org/10.1186/1472-6882-8-58)]
- **TCM-ID 中医药信息数据库（NUS BIDD）** — 新加坡BIDD维护的方剂–药材–成分–靶点库，含药典/经典方与CFDA批准方；与TCMID 2.0不是同一资源 [[网站](https://www.bidd.group/TCMID/)]

</details>

<details>
<summary>临床结构化 / 处方（2）</summary>

- **TCM-Lung 肺系病辨证处方编码集** — 河南中医药大学一附院肺系病案处理后 14948 条，仓库公开 4484 条编码（症状/证候/治法/处方 ID）；全名需邮件申请。与 TCMNSCLC 不是同一份数据 [[代码](https://github.com/2020MEAI/PresRecST)] [[论文](https://doi.org/10.1093/jamia/ocae066)]
- **TCM-PD / PTM 方剂–症状推荐集** — Yao 等 TKDE 2018 处方主题模型配套数据：原始 98334 首、预处理 33765 首（症状–中药 ID）；CKCEST 版权、仅研究使用。PresRecST 的 prescript_1195.csv 即此集复现表 [[代码](https://github.com/yao8839836/PTM)] [[DOI](https://doi.org/10.1109/TKDE.2017.2787158)]

</details>

<details>
<summary>通用中文医疗（13）</summary>

- **PromptCBLUE 中文医疗NLP指令化评测** — 把CBLUE的16项中文医疗NLP任务改写成生成式指令，CCKS-2023评测任务，中文医疗LLM早期统一榜之一 [[代码](https://github.com/michael-wzhu/PromptCBLUE)]
- **Huatuo-26M 大规模中文医疗问答** — 目前最大的开源中文医疗QA（约2600万对），含百科/图谱/问诊；精简版Huatuo-Lite常被拿来SFT或RAG [[论文](https://arxiv.org/abs/2305.01526)] [[正式发表](https://aclanthology.org/2025.findings-naacl.211/)] [[代码](https://github.com/FreedomIntelligence/Huatuo-26M)] [[数据集](https://huggingface.co/datasets/FreedomIntelligence/Huatuo26M-Lite)]
- **DISC-Med-SFT 医疗对话指令数据** — 复旦DISC配套的约47万条医疗对话SFT（图谱三元组+真实问诊重构），不含偏好数据 [[数据集](https://huggingface.co/datasets/Flmc/DISC-Med-SFT)] [[论文](https://arxiv.org/abs/2308.14346)]
- **ChiMed 中文医疗多阶段语料（Qilin-Med）** — Qilin-Med发布的约3GB中文医疗语料（CPT/SFT/DPO），与预训练集ChiMed 2.0不是同一资源 [[数据集](https://huggingface.co/datasets/williamliu/ChiMed)] [[论文](https://arxiv.org/abs/2310.09089)]
- **CMExam 中文执业医师考试评测集** — 源自国家医学考试的中文医考题（约6.8万），带多维标注，常被中文医疗/中医LLM当知识回忆对照 [[论文](https://arxiv.org/abs/2306.03030)] [[代码](https://github.com/williamliujl/CMExam)]
- **CMB 中文综合医学评测（Exam + Clin）** — 中大深圳FreedomIntelligence的中文医疗综合基准：CMB-Exam约28万题+CMB-Clin复杂病案，中医论文里最常见的西医/综合对照榜 [[论文](https://arxiv.org/abs/2308.08833)] [[正式发表](https://aclanthology.org/2024.naacl-long.343/)] [[代码](https://github.com/FreedomIntelligence/CMB)] [[数据集](https://huggingface.co/datasets/FreedomIntelligence/CMB)]
- **IMCS-21 智能医疗问诊对话** — 约4116场儿科在线问诊，带实体/意图/症状/报告标注，后接入CBLUE四任务 [[DOI](https://doi.org/10.1093/bioinformatics/btac817)] [[代码](https://github.com/lemuria-wchen/imcs21)] [[CBLUE任务](https://github.com/lemuria-wchen/imcs21-cblue)]
- **CBLUE 中文生物医学语言理解评测** — 中文生物医学NLU总榜（NER/关系/诊断归一化/分类等），PromptCBLUE的源任务集；天池有提交入口 [[论文](https://aclanthology.org/2022.acl-long.544/)] [[代码](https://github.com/CBLUEbenchmark/CBLUE)]
- **MedDialog 中英医疗对话** — 大规模医患对话（中文约110万场），中文医疗多轮问诊微调的常用源数据 [[论文](https://arxiv.org/abs/2004.03329)] [[代码](https://github.com/UCSD-AI4H/Medical-Dialogue-System)]
- **webMedQA 在线医疗咨询问答** — 从健康咨询网站收集的中文非事实型医问（约6.3万问，1正4负答案），早期中文医疗QA常用源 [[DOI](https://doi.org/10.1186/s12911-019-0761-8)] [[代码](https://github.com/hejunqing/webMedQA)]
- **CMeKG 中文医学知识图谱** — 覆盖疾病、药物、症状等的中文医学KG，本草/华驼和ChatGLM-Med的指令数据主要来源；原门户不稳，核验走工具仓 [[代码](https://github.com/king-yyf/CMeKG_tools)]
- **cMedQA2 中文社区医疗问答** — 中文医疗论坛问答（约10.8万问/20万答），扁鹊语料和后续SFT常把它当作源数据 [[代码](https://github.com/zhangsheng93/cMedQA2)]
- **cMedQA v1 中文社区医疗问答** — 从中文健康社区抓取的问答匹配集（仓库表：约 5.4 万问 / 10.2 万答，非商用研究）；论文 DOI 与 README 对得上，后续版本见 cMedQA2 [[代码](https://github.com/zhangsheng93/cMedQA)] [[论文](https://doi.org/10.3390/app7080767)]

</details>

<details>
<summary>东亚传统医学（3）</summary>

- **韩医领域嵌入对比学习数据** — 从韩医术语与本体构造的query–positive–negatives（约11.3万对），用于BGE-M3等检索微调 [[数据集](https://huggingface.co/datasets/cnupo23/korean-medicine-embedding-dataset)]
- **KNApSAcK KAMPO 汉方处方与生药库** — 奈良先端大整理的汉方公开库（约1581处方、278生药），生命科学数据库档案可下载 [[数据集](https://dbarchive.biosciencedbc.jp/data/knapsack-kampo/)] [[DOI](https://doi.org/10.1093/pcp/pcr165)]
- **OASIS 韩国传统医学信息门户** — 韩国韩医学研究院的传统医学文献与资源门户，可检索韩医论文与本草资料 [[网站](https://oasis.kiom.re.kr/)]

</details>

<details>
<summary>原始书籍 / 预训练语料（5）</summary>

- **中医经典全文语料（内经/伤寒/金匮/温病等 115 部）** — 中医经典全文数字化语料：内经、难经、伤寒论、金匮要略及温病经典 [[数据集](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)]
- **高质量中医预训练数据集（医案/典籍/百科等）** — 非网络来源高质量中医预训练数据集（约 1GB），含临床案例、名家典籍、医学百科等，99% 简体中文 [[数据集](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)]
- **ShizhenGPT 中医预训练语料（论文报告共 15B+ tokens：Stage1 文本 11.92B 含 6.3B 中医语料，Stage2 多模态约 3.6B）** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- **700 项中医药古籍文本** — 中医药古籍文本语料合集，收录近 700 项古籍文本 [[数据集](https://github.com/xiaopangxia/TCM-Ancient-Books)]
- **ChiMed 2.0 中文医疗预训练数据集（覆盖中医语料）** [[论文](https://arxiv.org/abs/2507.15275)]

</details>

<details>
<summary>评测基准（17）</summary>

- **TCM-RobustSDT** — 中医临床推理LLM鲁棒性基准数据集（Figshare） [[数据集](https://doi.org/10.6084/m9.figshare.33054974)]
- **中药处方审核评测基准** — 328道处方规范性与合理性选择题，面向中药处方安全审核评测 [[论文](https://doi.org/10.1038/s41597-025-06387-6)] [[数据](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[代码](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)]
- **TCM-AQA61 / CME-AQA 针灸推拿动作质量评估** — 针灸（A）与推拿（T）各 61 名受试者的第一人称+第三人称同步视频，两位中医师标注分类与连续指标；配套跨视角多模态评估框架 CME-AQA [[论文](https://arxiv.org/abs/2606.28104)] [[DOI](https://doi.org/10.1109/TNSRE.2026.3705649)] [[代码](https://github.com/FrancisXZhang/cme-aqa)] [[数据](https://researchdata.durham.ac.uk/collections/r1jm214p229)]
- **LingLan（灵兰秘典）大规模多任务中医评测基准 (2026)** [[数据集](https://github.com/TCMAI-BJTU/LingLan)] [[论文](https://arxiv.org/abs/2602.01779)]
- **ZhongJing-OMNI 中医多模态评测（含舌诊）** [[数据集](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]
- **TCMEval-SDT 辨证思维评测（专家标注病案）** — 中医辨证思维评测基准，含 300 例证候诊断案例（来源网络、古籍与医院病案），元数据遵循 FAIR 原则（Scientific Data 2025） [[DOI](https://doi.org/10.1038/s41597-025-04772-9)] [[论文](https://www.nature.com/articles/s41597-025-04772-9)] [[代码](https://github.com/zhuyan166/TCMEval)]
- **TCMBench 中医药大模型全面评测基准** — 面向中医领域的综合性大模型评测基准 TCMBench（arXiv 2024） [[数据集](https://github.com/ywjawmw/TCMBench)] [[论文](https://arxiv.org/abs/2406.01126)]
- **TCM-Vision-Benchmark 中医视觉评测（药材识别/望诊等，约 7k 题）** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Vision-Benchmark)]
- **标准化舌象病理标注数据集** — 6719张标准化舌象、20类病理多标签公开数据集，含检测基线 [[论文](https://arxiv.org/abs/2507.18288)] [[数据](https://doi.org/10.5061/dryad.1c59zw48r)] [[代码](https://github.com/btbuIntelliSense/Intelligent-tongue-diagnosis-detection-dataset)]
- **TCM-Ladder 中医多模态问答评测基准 (NeurIPS 2025)** — 中医多模态问答评测基准 TCM-Ladder，面向真实世界任务综合评估中医多模态大模型（arXiv 2025） [[数据集](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[榜单](https://tcmladder.com)] [[论文](https://arxiv.org/abs/2505.24063)]
- **TCM-Eval 动态可扩展中医评测基准** [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- **TCM-BEST4SDT 辨证论治病例评测基准** [[数据集](https://github.com/DYJG-research/TCM-BEST4SDT)] [[论文](https://arxiv.org/abs/2512.02816)]
- **TCM-5CEval 五维中医深度评测** [[论文](https://arxiv.org/abs/2511.13169)]
- **TCM-3CEval 核心知识·经典理解·临床决策三轴评测** [[论文](https://arxiv.org/abs/2503.07041)]
- **MTCMB 中医多任务评测基准（知识/推理/安全）** — 中医多任务评测基准 MTCMB 数据，覆盖知识、推理与安全维度，12 子集约 7100 样本（arXiv 2025） [[数据集](https://github.com/Wayyuanyuan/MTCMB)] [[论文](https://arxiv.org/abs/2506.01252)]
- **HWTCMBench 中医能力评测集** [[数据集](https://huggingface.co/datasets/Monor/hwtcm)]
- **TCM-SD 中医辨证评测基准** — 首个大规模公开中医辨证文本基准（54152 条真实病历、148 证，CC BY-NC-SA 4.0）；仓库写明完整数据在 TCM_SD_with_knowledge，天池 dataId=139034 [[论文](https://arxiv.org/abs/2203.10839)] [[正式发表](https://aclanthology.org/2022.ccl-1.80/)] [[代码](https://github.com/Borororo/ZY-BERT)] [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=139034)]

</details>

<details>
<summary>考试数据集（2）</summary>

- **TCM-Text-Exams 近年中医执业/考研真题文本基准** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams)]
- **医疗大模型中文考试评估** [[数据集](https://github.com/jingnant/Medical-LLMs-Chinese-Exam)]

</details>

<details>
<summary>指令/对话数据集（12）</summary>

- **HSQ-TD（健身气功指令微调数据集）** — 健身气功养生领域首个指令微调数据集，57,843条指令基于官方教材与专业文献蒸馏（ScienceDB） [[数据集](https://doi.org/10.57760/sciencedb.35843)]
- **黄帝内经SFT指令集** — 杏核配套约2009条内经相关指令数据，含thinking/output字段 [[数据集](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2)]
- **TCMNSCLC 非小细胞肺癌中医推理真实世界数据集** — 真实世界医案全标注（辨证/治法/汤药/中成药）的中医推理数据集 [[数据集](https://huggingface.co/datasets/zhangxinxin0428/TCMNSCLC)] [[DOI](https://doi.org/10.5281/zenodo.21027568)]
- **高质量中医 SFT 数据集** [[数据集](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]
- **TCMChat-dataset-600k 中药知识问答与推荐指令数据** [[数据集](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- **ShizhenGPT 多模态指令微调数据（文本/视觉/语音/ECG 等，论文 Table 3 合计约 31.1 万条）** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- **中医药指令数据集 ShenNong_TCM_Dataset** [[数据集](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)]
- **MedChatZH 中医问诊数据集** [[代码](https://github.com/tyang816/MedChatZH)] [[数据集](https://huggingface.co/datasets/tyang816/MedChatZH)]
- **中文医疗在线问诊数据集 ChatMed_Consult_Dataset（50w+在线问诊+ChatGPT回复）** [[数据集](https://huggingface.co/datasets/michaelwzhu/ChatMed_Consult_Dataset)]
- **CMtMedQA 仲景真实多轮医患对话（约 7 万条）** [[数据集](https://huggingface.co/datasets/Suprit/CMtMedQA)]
- **白泽中医药语料库V3** — 约15.7万条中医QA，覆盖理论、中药、方剂、诊断、针灸与临床 [[数据集](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3)]
- **中国药典指令数据集** — 基于《中国药典》一部构建的KnowledgeQA与PrescriptionWriting指令数据 [[数据](https://github.com/QLU-NLP/BianCang/tree/main/ChP-TCM)] [[论文](https://arxiv.org/abs/2411.11027)]

</details>

<details>
<summary>知识图谱（6）</summary>

- **灵枢症状中心上下文知识图谱** — 北交大等症状中心中西医桥接图谱（导出约1733万实体、3947万关系，含三元组+上下文四元组），门户提供可视化、推理与有据问答 [[论文](https://arxiv.org/abs/2608.20402)] [[网站](http://www.tcmkg.com/)]
- **ChatMed 知识图谱** [[数据集](https://github.com/ywjawmw/TCM_KG)]
- **TCM-MKG 中医药多维知识图谱** [[数据](https://zenodo.org/records/15395588)]
- **OpenTCM 妇科古籍知识图谱（约 4.8 万实体 / 15.2 万关系）** [[代码](https://github.com/OpenTCM01/OpenTCM)] [[论文](https://arxiv.org/abs/2504.20118)]
- **TCM-QG 中医文献问题生成（CHIP2020）** — 约 5000 篇中医文本、1.3 万问答对，用来补知识库和自动提问（CC BY-SA 4.0） [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86895)] [[资料](http://openkg.cn/dataset/tcm-qg)]
- **TCM-NER 中药说明书实体识别（OpenKG / CHIP）** — 1997 篇中药说明书、13 类实体共 59803 个标注，用来自动构建用药知识图谱（CC BY-SA 4.0） [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86819)] [[资料](http://openkg.cn/dataset/tcm-ner)]

</details>

---

要搜索或按标签筛，用[项目页](https://tyang816.github.io/zh/projects/tcm/)。说明写在 [Wiki](wiki/Home.md)。
改条目请编辑 `data/catalog.yml`，再运行 `python3 scripts/build_readme.py`，不要直接改这个 README。
