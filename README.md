# 🔥 开源中医模型、数据、论文、专利

**语言 / Language:** [中文](README.md) | [English](README_EN.md)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  ![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork) [![中文门户](https://img.shields.io/badge/中医资源-门户-blue)](https://tyang816.github.io/zh/projects/tcm/) [![Project](https://img.shields.io/badge/Project-tyang816.github.io-informational)](https://tyang816.github.io/projects/tcm/)

开源中医模型、数据、论文、专利精选，也带一点相关中文医疗。现在大概有 104 条新闻、117 个模型、95 篇综述、73 件专利、206 个数据集、449 篇方法论文、36 门公开课，以及 [452 位中医药人工智能导师](wiki/People.md)。[欢迎补条目](CONTRIBUTING.md)。

[项目页](https://tyang816.github.io/projects/tcm/) · [中文项目页](https://tyang816.github.io/zh/projects/tcm/) · [Wiki](wiki/Home.md) · [主页](https://tyang816.github.io/zh/)

## 先看这里

真能下载复现的中医权重大概 21 个，都在[开源模型](#开源模型)里。新闻里医院、公司发的，多数没有公开权重，当不了实验底座。

近年的研究逐渐扩展到多模态、Agent 和临床推理评测。对比模型时，应分别查看考试知识、证候判别和处方任务；TCM-Ladder、LingLanMedBench、MTCMB 提供了互补的评测资源。

| 你想做什么 | 可以先看 | 备注 |
| --- | --- | --- |
| 本机跑通一个模型 | **[扁仓 (BianCang)](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)**、**[仲景 (ZhongJing)](https://huggingface.co/CMLM/ZhongjingGPT1_13B)** | 论文、权重、代码都有 |
| 做中医问诊 | **[MedChatZH](https://github.com/tyang816/MedChatZH)** | 还有配套问诊数据 |
| 舌诊、四诊 | **[ShizhenGPT](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)** | 多模态，数据和权重都开 |
| 自己接着训 | **[ChatTCM](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)**、**[神农大模型 (ShenNong-TCM-LLM)](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)** | 预训练或指令数据是公开的 |
| 电脑比较一般 | **[杏核 (Xinghe)](https://huggingface.co/zsyjsld/Xinghe1.2-9B)** | 9B，有 GGUF |
| 做对比实验 | **[TCM-Ladder](https://arxiv.org/abs/2505.24063)**、**[LingLanMedBench（灵兰）](https://arxiv.org/abs/2602.01779v2)** | 任务说得比较清楚；更多在[数据集](#数据集) |
| 写相关工作 | 近两年的 scoping review | 先翻[综述](#综述)，别从单篇模型论文起 |
| 找公开课 | [学习资料](#学习资料) | 高校公开课和系列讲座，只收可核验的一手链接 |
| 找导师 | [导师](wiki/People.md) | 完整名单按高校、产业、医院和地区排列 |

同名不一定是同一个东西。「仲景」至少有 ZhongJingGPT 和 AAAI 那条 CMtMedQA；TCM-Eval 也不止一套。说不清时看 [Getting Started](wiki/Getting-Started.md)。

## 导师

完整名单共 452 位，写在 [Wiki · 导师](wiki/People.md)，先按地区，再按高校、医院或公司。这里只保留人数统计。

**按单位类型**

| 分类 | 人数 |
| --- | ---: |
| 高校 | 360 |
| 产业 | 47 |
| 医院 | 45 |

**按地区**

| 分类 | 人数 |
| --- | ---: |
| 北京 | 80 |
| 天津 | 28 |
| 河北 | 5 |
| 山西 | 4 |
| 内蒙古 | 8 |
| 辽宁 | 8 |
| 吉林 | 4 |
| 黑龙江 | 4 |
| 上海 | 45 |
| 江苏 | 21 |
| 浙江 | 16 |
| 安徽 | 12 |
| 福建 | 13 |
| 江西 | 13 |
| 山东 | 20 |
| 河南 | 12 |
| 湖北 | 15 |
| 湖南 | 17 |
| 广东 | 30 |
| 广西 | 9 |
| 海南 | 1 |
| 重庆 | 4 |
| 四川 | 7 |
| 贵州 | 13 |
| 云南 | 9 |
| 西藏 | 3 |
| 陕西 | 3 |
| 甘肃 | 2 |
| 青海 | 3 |
| 宁夏 | 3 |
| 新疆 | 3 |
| 香港 | 9 |
| 澳门 | 4 |
| 台湾 | 7 |
| 日本 | 3 |
| 韩国 | 5 |
| 新加坡 | 1 |
| 美国 | 1 |
| 澳大利亚 | 1 |
| 其他 | 6 |

## 开源模型

上面是起步用的。要翻全部能下的权重，或只有论文/产品、通用中文医疗底座、闭源产品和日韩汉方/韩医，点开即可。

<details>
<summary>能下载的权重，共 21 个</summary>

| 模型 | 年 | 机构 | 特色 | 链接 |
| --- | :---: | --- | --- | --- |
| **知方丹台 (ZhiFangDanTai)** | 2026 | 首都师范大学 | RAG · 图谱 | [论文](https://arxiv.org/abs/2509.05867) · [权重](https://huggingface.co/tczzx6/ZhiFangDanTai1.0) · [数据](https://huggingface.co/datasets/tczzx6/ZhiFangDanTai1.0) |
| **灵丹-V2 (Lingdan-V2)** | 2026 | 北京交通大学 | 处方 · 推理 | [论文](https://arxiv.org/abs/2610.14705) · [权重](https://huggingface.co/TCMLLM/Lingdan-8B-R1) · [代码](https://github.com/TCMAI-BJTU/Lingdan-V2) |
| **杏核 (Xinghe)** | 2026 | Xinghe-TCM | 推理 · 古籍 | [权重](https://huggingface.co/zsyjsld/Xinghe1.2-9B) · [数据](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2) |
| **仲景 (ZhongJing)** | 2026 | 福耀科技大学 | 专家知识引导的中医大模型 ZhongJingGPT。它把领域微调和认知心… | [论文](https://doi.org/10.26599/TST.2025.9010046) · [权重](https://huggingface.co/CMLM/ZhongjingGPT1_13B) · [代码](https://github.com/pariskang/CMLM-ZhongJing) |
| **中医体质 Qwen3-8B 量化权重** | 2026 | — | 面向中医体质的 Qwen3-8B 量化权重，仓库里有 q4、q5 和 q… | [权重](https://huggingface.co/chenhaodev/tcm-constitution-qwen3-8b-gguf) |
| **TCM-Qwen3.5-9B-SFT-R2** | 2026 | Xxiao2023 (Hugging Face) | 推理 | [权重](https://huggingface.co/Xxiao2023/TCM-Qwen3.5-9B-SFT-R2) |
| **TCM-Qwen2.5-7B-SFT** | 2026 | — | 基于 Qwen2.5-7B 的中医监督微调权重，模型文件是完整的 saf… | [权重](https://huggingface.co/Xxiao2023/TCM-Qwen2.5-7B-SFT-V1) |
| **Qwen3.5-9B 中医继续预训练** | 2026 | — | Qwen3.5-9B 做完中医继续预训练后的全量权重，一个约 17.9… | [权重](https://huggingface.co/arthur789/qwen3.5-9b-tcm-cpt) |
| **MiMo-9B-TCM-Andrology-LoRA** | 2026 | johnson (Hugging Face) | 处方 | [权重](https://huggingface.co/johnson/MiMo-9B-TCM-Andrology-LoRA) · [数据](https://huggingface.co/datasets/johnson/TCM-Andrology-EMR) |
| **Fu-TCM-9B** | 2026 | fudanxai (Hugging Face account) | fudanxai账号发布的9.41B参数BF16权重，已核验8个safe… | [权重](https://huggingface.co/fudanxai/Fu-TCM-9B) · [数据](https://huggingface.co/datasets/fudanxai/Fu_TCM) |
| **Fu-TCM-27B** | 2026 | 复旦大学 | 多模态 | [论文](https://arxiv.org/abs/2610.38333) · [权重](https://huggingface.co/fudanxai/Fu-TCM-27B) · [数据](https://huggingface.co/datasets/fudanxai/Fu_TCM) |
| **白泽 (Baize-TCM-LLM)** | 2025 | 中国中医科学院中药研究所 | 中国中医科学院中药研究所基于Qwen3的中医问答模型系列（0.6B/8B… | [权重](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model) · [数据](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3) |
| **扁仓 (BianCang)** | 2025 | 齐鲁工业大学 | 系列中医大模型（JBHI 正式发表）；2025.12 开源 14B 版本 | [论文](https://arxiv.org/abs/2411.11027) · [权重](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct) · [代码](https://github.com/QLU-NLP/BianCang) |
| **ViTCM-LLM** | 2025 | Tsinghua Shenzhen International Graduate School | 多模态 · RAG | [论文](https://doi.org/10.1109/bibm66473.2025.11357113) · [权重](https://huggingface.co/Mark-CHAE/ViTCM-LLM) · [代码](https://github.com/jw-chae/ViTCM_LLM) |
| **TCM-VisResolve (TCM-VR)** | 2025 | 云南民族大学 | 多模态 | [论文](https://doi.org/10.1109/BIBM66473.2025.11356679) · [权重](https://huggingface.co/dylanyang963/TCM-VR) |
| **ShizhenGPT** | 2025 | 香港中文大学(深圳)等 | 多模态 | [论文](https://arxiv.org/abs/2508.14706) · [权重](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni) · [代码](https://github.com/FreedomIntelligence/ShizhenGPT) |
| **TCMLLM / 灵丹 (Lingdan)** | 2024 | 北京交通大学 | 中医药大模型与处方推荐 | [论文](https://doi.org/10.1016/j.dcmed.2025.01.007) · [权重](https://huggingface.co/TCMLLM/Lingdan-13B-Base) · [代码](https://github.com/2020MEAI/TCMLLM) |
| **TCMChat** | 2024 | 浙江大学 | 生成式中医药大模型，经预训练+监督微调构建，配套 60 万条中药知识对话… | [论文](https://doi.org/10.1016/j.phrs.2024.107530) · [权重](https://huggingface.co/ZJUFanLab/TCMChat-600k) · [代码](https://github.com/ZJUFanLab/TCMChat) · [数据](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k) |
| **MedChatZH** | 2024 | 华东理工大学 | 基于 Baichuan-7B 的中医问诊对话模型，公开配套问诊数据与模型… | [论文](https://doi.org/10.1016/j.compbiomed.2024.108290) · [代码](https://github.com/tyang816/MedChatZH) · [权重](https://huggingface.co/tyang816/medchatzh) · [数据](https://huggingface.co/datasets/tyang816/MedChatZH) |
| **ChatTCM** | 2024 | — | HF 用户 SylvanL 开源的中医 LLM：Qwen2-7B 继续预… | [权重](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain) |
| **神农大模型 (ShenNong-TCM-LLM)** | 2023 | 华东师范大学 | 首个中医药大规模语言模型"神农"，配套 ShenNong_TCM_Dat… | [权重](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM) · [代码](https://github.com/michael-wzhu/ShenNong-TCM-LLM) · [数据](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset) |

</details>

<details>
<summary>只有论文或产品、没有核验权重的（50）</summary>

<details>
<summary>2026 · 15</summary>

- [*Digital Chinese Medicine*] **青囊 (QingNangTCM)** 基于 GLM-4-9B-Chat，以 P-Tuning v2 适配中医问答与临床推理；构建 100,000 条 QnTCM_Dataset 训练语料。 [河北北方学院] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.002)]
- [*ISCTIS 2026*] **舌面多模态融合智能诊断** 舌-面多模态特征融合+LLM驱动的中医智能诊断 [厦门理工学院] [[DOI](https://doi.org/10.1109/ISCTIS70043.2026.11572361)]
- **砭石云中医** **砭石云中医**是智慧眼基于已备案砭石多模态大模型的中医方案，用症状到方药的知识图谱支持四诊采集和辅助辨证。 [智慧眼科技] [[官网](https://www.a-eye.cn/news_list/420.html)] [[网站](https://www.a-eye.cn/news_list/356.html)]
- **岐元** **岐元**是上海中医药大学附属第七人民医院的中医垂类大模型，采用预训练、领域微调和专家强化学习，支持生成式病历和名老中医 Agent 数字孪生。 [上海中医药大学附属第七人民医院] [[新闻](https://finance.sina.com.cn/jjxw/2026-07-26/doc-inikassr0678770.shtml)]
- [*Information Fusion*] **天医 (Tianyi)** 南京中医药大学等提出 7.6B 参数中医大模型，按读书—临证—跟师多阶段训练，配套TCMEval评测与真实世界验证（Information Fusion 2026年2月） [南京中医药大学] [[正式发表](https://doi.org/10.1016/j.inffus.2025.103663)] [[论文](https://arxiv.org/abs/2505.13156)] [[新闻](https://blog.sciencenet.cn/blog-279293-1501581.html)]
- **华族本草** **华族本草**是贵州医科大学中药全国重点实验室牵头的民族药大模型，以数智岐黄和 Qwen 为底座，融合多民族医药古籍与知识图谱，覆盖成分筛选、配伍、质控和教学。 [贵州医科大学，中药功效成分发掘与利用全国重点实验室] [[官网](https://www.gmc.edu.cn/info/1059/30300.htm)] [[新闻](https://www.news.cn/tech/20260804/f973d6fa9de640328fec0194c63335a3/c.html)]
- [*JMIR Medical Informatics*] **TongueVLM** 中医舌诊多模态大模型，支持舌象描述生成与体质推理。JMIR 页被拦截，OpenAlex 记录作者单位为合肥工业大学与安徽中医药大学等 [合肥工业大学，安徽中医药大学等] [[论文](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- [*APWeb-WAIM 2025*] **TCM-R1** 通过GRPO增强中医推理能力的大模型 [西南大学] [[论文](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*世界科学技术-中医药现代化*] **TCM Classic-Translator（中医古籍今译）** 用《黄帝内经》《伤寒论》等文言—白话平行语料，对 DeepSeek、Qwen、Baichuan 做 LoRA 微调并融合注释，得到 TCM Classic-Translator。BLEU-4、ROUGE-1、ROUGE-2、ROUGE-L 分别为 39.3534、55.0474、35.8099、54.6551。 [中国中医科学院中医药信息研究所，南京中医药大学人工智能与信息技术学院] [[DOI](https://doi.org/10.11842/wst.20250916005)]
- [*Digital Chinese Medicine*] **Qwen-TCM-Dia** 基于 Qwen2.5 的中医泄泻专科模型，以两阶段 LoRA 完成领域续训和思维链指令微调，连接症状、病机、治法与方药。 [首都医科大学附属北京中医医院，北京中医药大学等] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.003)]
- [*arXiv*] **Med-Shicheng（师承）** 沿用 Tianyi 的多阶段训练思路，在 Qwen2.5-1.5B-Base 上实施续训、监督微调和 KTO，学习 5 位中医名家的经验，覆盖 7 类任务。 [南京中医药大学等] [[论文](https://arxiv.org/abs/2603.23520)] [[代码](https://github.com/NJUCM-BJUCM-TCM-AI/Med-Shicheng)]
- [*Chinese Herbal Medicines*] **HerbWise** 面向传统草药（THM）的领域大模型，服务草药现代化与标准化 [成都中医药大学] [[DOI](https://doi.org/10.1016/j.chmed.2026.02.010)]
- [*Chinese Medicine*] **GastroTCM** 中医消化内科大模型，基于Llama3-8B微调并结合RAG与智能体框架。Chinese Medicine 论文署名清华大学 TCM-X 与中日友好医院等 [清华大学，中日友好医院等] [[论文](https://link.springer.com/article/10.1186/s13020-025-01295-8)]
- [*arXiv*] **DongYuan** 中西医结合脾胃病诊断LLM框架，融合中医辨证与西医诊断推理。arXiv PDF 署名河北省中医院、中科院自动化所、中科闻歌与天津大学 [河北省中医院，中国科学院自动化研究所等] [[论文](https://arxiv.org/abs/2603.28191)]
- [*Chinese Medicine*] **DFGLM-TCM** 北京中医药大学东方医院与智谱等的中医临床系统，把通用中医知识与名医经验分模块建模后多任务协同。论文已发；代码和训练、验证数据未公开，合格研究者可向通讯作者申请。 [北京中医药大学，智谱华章] [[DOI](https://doi.org/10.1186/s13020-026-01512-y)]

</details>

<details>
<summary>2025 · 23</summary>

- **薪火中国药** **薪火中国药**是北京中医药大学牵头建设的中医药教育大模型，覆盖助学、助教、助研、助管和对外传播，并于2026年通过生成式人工智能服务备案。 [北京中医药大学，科大讯飞，中国中医药出版社] [[官网](https://www.bucm.edu.cn/xwgl/6762cbff37ae4939829bbd3efae96225.htm)] [[网站](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)] [[新闻](https://www.beijing.gov.cn/fuwu/lqfw/gggs/202604/t20260423_4605343.html)]
- [*arXiv*] **智明堂 (ZMT-M1)** 中医大模型及TCM-Eval动态可扩展评测基准 [北京航空航天大学] [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- [*Chinese Medicine*] **悬壶 (XuanHuGPT)** 基于 ChatGLM2-6B，采用 LoRA 与 P-Tuning v2 进行中医领域参数高效微调。 [河北北方学院] [[DOI](https://doi.org/10.1186/s13020-025-01200-3)]
- **张仲景中医药大模型** **张仲景中医药大模型**由河南中医药大学与北京科技大学等联合发布，覆盖智能辨证、证素推荐、经方应用和方药分析，并接入临床辅助诊疗。 [河南中医药大学，北京科技大学] [[官网](https://hactcm.edu.cn/info/1022/211754.htm)] [[网站](https://news.ustb.edu.cn/info/1981/67772.htm)]
- **广医·岐智** **广医·岐智**是中国中医科学院广安门医院的中医医疗服务大模型，支持导诊、预问诊、病历生成和辨证方剂建议，2.0增加智能体医生，并已完成算法备案。 [中国中医科学院广安门医院] [[官网](https://www.gamyy.cn/gzb/news/big/110133.html)] [[网站](https://www.gamyy.cn/gzb/news/big/114632.html)] [[新闻](https://www.gamyy.cn/gzb/news/big/113898.html)]
- [*Expert Systems with Applications*] **岐伯 (Qibo)** 天津大学等提出的中医大模型与Qibo Benchmark，持续预训练+SFT提升辨证与问答能力 [天津大学，天津中医药大学] [[正式发表](https://doi.org/10.1016/j.eswa.2025.127672)] [[论文](https://arxiv.org/abs/2403.16056)] [[DOI](https://doi.org/10.1016/j.eswa.2025.127672)]
- **女娲 (Nüwa / TCM-Nvwa)** 一套中医大模型训练流程：持续预训练、监督微调、奖励模型和 RLAIF，底座是 Ziya-LLaMA-13B。仓库放了部分预训练、问答和奖励数据，权重没有单独放出来。 [[代码](https://github.com/synbol/TCM-Nvwa)]
- [*arXiv*] **天惠 (TianHui)** 面向12类中医场景的领域LLM（DeepSeek-R1-Distill-Qwen-14B+PT/SFT），开源代码与评测脚本。arXiv PDF 署名成都中医药大学智能医学院 [成都中医药大学] [[论文](https://arxiv.org/abs/2509.19834)] [[代码](https://github.com/JYfantast/TianHui)]
- **固生堂中医大脑** **固生堂中医大脑**把国医 AI 分身接入医院信息系统，在病情采集、病历生成、辅助辨证和开方环节给出可溯源的名医思路。 [固生堂] [[官网](https://www.gstzy.cn/news/detail/10/14076.html)] [[网站](https://www.gstzy.cn/news/detail/10/14125.html)]
- **众星·长白岐黄** **众星·长白岐黄**是长春中医药大学、吉林工商学院等联合研发的多模态中医药推理大模型，设有家庭健康助手和吉派中医医生助手两个入口。 [长春中医药大学，吉林工商学院，长春工程学院] [[官网](https://www.jlbtc.edu.cn/info/1042/93113.htm)] [[新闻](https://news.cnjiwang.com/jwyc/202512/4006547.html)]
- **伊尹中医经典大模型** **伊尹中医经典大模型**由中医在线用医典和经方经验训练，在问诊中展示辨证思路，并在嵩县基层医疗机构提供辅助诊疗。 [中医在线，中原药谷] [[新闻](https://www.cntcm.com.cn/content/202509/17/c284139.html)]
- **任度·素问** **任度·素问**是传神语联基于任度大模型和自研 moH 混合熵架构的中医模型，提供主动问诊、辨证和方剂建议，并通过信通院中医药大模型 4+ 级评估。 [传神语联] [[网站](https://www.transn.com/about_us/consult/article/1965645664716955649)]
- **中医横琴 (Hengqin-R1)** **中医横琴（Hengqin-R1）**是中医药广东省实验室的垂类推理大模型，融合精调、强化学习与知识图谱，支撑辨证、中西药联用智能体和四诊客观化。 [中医药广东省实验室（横琴实验室）] [[官网](https://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/dtxx/content/post_3807664.html)] [[网站](https://www.gzucm.edu.cn/info/1621/109561.htm)]
- [*Computers in Biology and Medicine*] **TCM-KLLaMA** 知识图谱与大模型融合的中医方剂智能生成模型。PubMed 40056842 署名浙江工商大学与西湖大学医学院附属杭州市第一人民医院 [浙江工商大学，西湖大学医学院附属杭州市第一人民医院] [[DOI](https://doi.org/10.1016/j.compbiomed.2025.109887)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/40056842)]
- [*Chinese Medicine*] **TCM-DS** 基于 DeepSeek-LLM-7B，结合 LoRA 与检索增强生成（RAG），用于药食同源食疗方推荐。 [澳门科技大学] [[DOI](https://doi.org/10.1186/s13020-025-01249-0)]
- [*arXiv*] **RACE-Align** 检索增强+CoT 式 DPO 的轻量中医对齐模型（Qwen3-1.7B），探索小模型对齐路线。arXiv PDF 署名上海科技大学、河南大学与辽宁中医药大学 [上海科技大学，河南大学，辽宁中医药大学] [[arXiv](https://arxiv.org/abs/2506.02726)]
- [*IEEE ICIP 2025*] **MCM** 多智能体协同的中医多模态诊断框架（ICIP 2025） [上海计算机软件技术开发中心] [[代码](https://github.com/JerryMazeyu/MCM)] [[正式发表](https://doi.org/10.1109/icip55913.2025.11084334)]
- [*arXiv*] **Ladder-base (GRPO-TCM)** TCM-Ladder团队提出的首个GRPO强化学习对齐中医LLM。arXiv PDF 署名密苏里大学与上海中医药大学等 [密苏里大学，上海中医药大学等] [[论文](https://arxiv.org/abs/2510.17402)]
- [*arXiv*] **Hengqin-RA-v1** 类风湿关节炎中医诊疗大模型及配套数据集。这篇预印本已由 arXiv 撤回，撤回说明是作者身份和单位无法核实；当前作者栏为 Yishen Liu。 [[论文](https://arxiv.org/abs/2501.02471)]
- [*Applied Sciences*] **Gen-SynDi** 知识引导的生成式AI框架，用于辨证与疾病诊断的双向教学 [College of Korean Medicine, Wonkwang University, Iksan 54538, Republic of Korea，College of Korean Medicine, Woosuk University, Jeon-Ju 54987, Republic of Korea，Dongje Medical Co., Ltd., Daegu 42187, Republic of Korea，College of Medicine, Yeungnam University, Daegu 42415, Republic of Korea] [[DOI](https://doi.org/10.3390/app15094862)]
- [*arXiv*] **DoPI** 引导模型与专家模型协同的主动问诊系统；在论文模拟问诊评测中，DoPI-7B 的最终诊断准确率为 84.68%。 [天津大学，香港中文大学等] [[论文](https://arxiv.org/abs/2507.04877)]
- [*IEEE BIBM 2025*] **ChatGLM-FGIDs-TCM** 知识融合的ChatGLM中医临床决策支持模型，面向功能性胃肠病（FGIDs） [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356283)]
- [*arXiv*] **BenCao（指令微调本草助手）** 基于ChatGPT自然语言指令对齐的中医多模态助手，对接舌象API与知识库，部署于GPTs Store（区别于华驼/本草）。arXiv HTML 署名密苏里大学与上海中医药大学等 [密苏里大学，上海中医药大学等] [[论文](https://arxiv.org/abs/2510.17415)]

</details>

<details>
<summary>2024 · 10</summary>

- **智赋岐黄天功** **智赋岐黄天功**是智赋岐黄与哈尔滨工业大学联合研发的中医大模型，用医案和名医验方训练多种辨证体系，作为四诊仪体质辨识的算法底座并已完成算法备案。 [智赋岐黄，哈尔滨工业大学] [[官网](https://qihuang-ai.com/ai-platform/tiangong)] [[网站](https://qihuang-ai.com/about)]
- **数智本草** **数智本草**是天士力与华为云基于盘古语言大模型和盘古药物分子大模型开发的中医药双模态模型，用古籍、方剂和文献支持问答、分子计算与中药研发筛选。 [天士力，华为云] [[官网](https://www.huawei.com/cn/huaweitech/publication/202503/pioneer-developers-of-huaweicloud)] [[网站](https://tjdsj.tjcac.gov.cn/tjsg/hyzx/202405/t20240523_6632807.html)] [[新闻](https://www.news.cn/politics/20240509/be28f085474b45fd9d6829766195568d/c.html)]
- **数智岐黄** **数智岐黄**由华东师范大学联合上海中医药大学等研发，1.0提供中医药问答、健康咨询和知识图谱交互，2.0升级为覆盖中西药数据的多模态大模型。 [华东师范大学，上海中医药大学，临港实验室] [[官网](https://www.ecnu.edu.cn/info/1426/65503.htm)] [[网站](https://www.shanghai.gov.cn/nw4411/20240120/1a19dcf117f7430b971db72e53ed4d9b.html)] [[新闻](https://hub.baai.ac.cn/view/41476)]
- **天河·灵枢** **天河·灵枢**由国家超算天津中心联合天津中医药大学等研发，1.0面向针灸并配三维穴位数字人，2.0把覆盖范围扩到20余个临床学科。 [国家超级计算天津中心，天津中医药大学，现代中医药海河实验室] [[官网](https://www.nscc-tj.cn/xwxq.php?id=628)] [[网站](https://www.tjutcm.edu.cn/info/1047/2084.htm)] [[新闻](https://www.tjlgbj.gov.cn/tjlgb/system/2025/08/09/030003838.shtml)]
- **大数中医 (BigDataTCM)** 河南工业大学复杂性科学研究院与阿帕斯联合研发的中医垂直领域大模型（34B），提供医疗问答、诊断支持与中医知识服务 [河南工业大学] [[代码](https://github.com/HAUT-CS/BigDataTCM)]
- **大医金匮** **大医金匮**是中科闻歌与中国中医科学院联合打造的中医大模型，学习典籍与临床医案，用于辨证推理、治疗方案生成和四诊健康管理。 [中科闻歌，中国中医科学院] [[网站](https://tcm.wenge.com/)]
- [*AAAI*] **仲景（CMtMedQA 线，Yang et al.）** 与 Kang 系 ZhongJingGPT 同名不同源的中医大模型：Ziya-LLaMA-13B 全流程 CPT+SFT+RLHF，基于约 7 万条真实多轮医患对话 CMtMedQA（AAAI 2024；注意与 Tsinghua Sci Technol 的 ZhongJingGPT 无作者与工件交集） [华东师范大学等] [[论文](https://doi.org/10.1609/aaai.v38i17.29907)] [[arXiv](https://arxiv.org/abs/2308.03549)]
- **仲思** **仲思**是招联消费金融联合中山大学、广州中医药大学深圳医院发布的中医垂直大模型，覆盖知识问答、问诊病历生成和方剂推荐，并在深圳社康场景使用。 [招联消费金融，中山大学，广州中医药大学深圳医院] [[新闻](https://www.stcn.com/article/detail/1454029.html)]
- [*Computer Methods and Programs in Biomedicine Update*] **TCM-GPT** 面向中医领域自适应的高效预训练大模型。期刊元数据署名北京邮电大学与伦敦大学学院 [北京邮电大学，伦敦大学学院] [[DOI](https://doi.org/10.1016/j.cmpbup.2024.100158)] [[论文](https://arxiv.org/abs/2311.01786)]
- [*Scientific Reports*] **CPMI-ChatGLM** 中成药指令数据的 ChatGLM 参数高效微调模型。OpenAlex/期刊单位为安徽中医药大学与中国中医科学院安徽中医药计算机应用研究所 [安徽中医药大学，中国中医科学院安徽中医药计算机应用研究所] [[DOI](https://doi.org/10.1038/s41598-024-56874-w)]

</details>

<details>
<summary>2023 · 2</summary>

- **黄帝 (HuangDi)** 基于 Ziya-LLaMA-13B 的中医古籍知识问答大模型，预训练融合 22 本"十三五"中医教材与中医网站语料，古籍指令数据 SFT（图书馆论坛 2024 报道） [南京大学, 郑州大学] [[代码](https://github.com/Zlasejd/HuangDI)]
- **岐黄问道** **岐黄问道**是南京大经中医发布的中医垂直大模型，基于千万级知识图谱和临床数据，面向医疗机构做辨证、处方和养生建议。 [南京大经中医药信息技术有限公司] [[新闻](https://js.cnr.cn/rdzt/qnjs/qnjsgdxw/20230801/t20230801_526358407.shtml)]

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
- **太一2 (Taiyi-2)** 太一二代开源生物医学模型，底座从Qwen-7B换成GLM4-9B，重做数据过滤与任务指令。官方模型卡仍引用太一1的JAMIA论文（10.1093/jamia/ocae037），没有单独的太一2论文 [大连理工大学] [[模型](https://huggingface.co/DUTIR-BioNLP/Taiyi2-chat)] [[代码](https://github.com/DUTIR-BioNLP/Taiyi-LLM)]
- [*arXiv*] **卫宁WiNGPT3** 卫宁第三代医疗推理模型（32B，底座Qwen2.5），多阶段SFT+RL与长思维链，对接WiNEX医院流程；技术报告和代码已公开，权重未核验可下载 [卫宁健康] [[论文](https://arxiv.org/abs/2505.17387)] [[代码](https://github.com/winninghealth/WiNGPT3)]

</details>

<details>
<summary>2024 · 5</summary>

- [*arXiv*] **明医 (MING)** 中文医疗问诊大模型 MING，以稀疏 LoRA 混合专家（MING-MoE）增强医疗多任务学习能力（arXiv 2024） [上海交通大学] [[论文](https://arxiv.org/abs/2404.09027)] [[相关 MedCare](https://aclanthology.org/2024.findings-emnlp.619/)] [[代码](https://github.com/MediaBrain-SJTU/MING)]
- [*JAMIA*] **太一 (Taiyi)** 大连理工DUTIR的中英双语生物医学大模型，底座Qwen-7B，覆盖问答、医患对话、报告生成与信息抽取等 [大连理工大学] [[DOI](https://doi.org/10.1093/jamia/ocae037)] [[代码](https://github.com/DUTIR-BioNLP/Taiyi-LLM)] [[模型](https://huggingface.co/DUTIR-BioNLP/Taiyi-LLM)]
- [*arXiv*] **华佗GPT-o1 (HuatuoGPT-o1)** 华佗系列医疗复杂推理模型，用可验证医题和医学验证器做搜索微调与强化学习。仓库给出 7B、8B 和 70B。 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2412.18925)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-o1)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-7B)]
- [*arXiv*] **华佗GPT-Vision (HuatuoGPT-Vision)** 华佗系列医学多模态模型，大规模注入医学视觉知识，常作中文医学影像/多模态对照 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2406.19280)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-Vision)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B-Qwen2.5VL)]
- [*arXiv*] **Apollo** 中大深圳FreedomIntelligence的多语种医疗LLM（含中文），配套ApolloCorpus与XMedBench [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2403.03640)] [[代码](https://github.com/FreedomIntelligence/Apollo)] [[模型](https://huggingface.co/FreedomIntelligence/Apollo-7B)]

</details>

<details>
<summary>2023 · 20</summary>

- [*arXiv*] **麒麟-Med (Qilin-Med)** 多阶段知识注入的中文医疗LLM（CPT+SFT+DPO，底座Baichuan-7B），发布约3GB ChiMed语料，可再加RAG。arXiv PDF 署名北京大学、港科大（广州）等 [北京大学，香港科技大学（广州）等] [[论文](https://arxiv.org/abs/2310.09089)] [[代码](https://github.com/williamliujl/Qilin-Med)] [[数据集](https://huggingface.co/datasets/williamliu/ChiMed)]
- [*arXiv*] **本草[原名：华驼(HuaTuo)]** 哈工大社会计算与信息检索研究中心做的本草，原来叫华驼。它用中文医学知识做指令微调，论文是 2023 年的 HuaTuo。同组后来又写了知识微调的工作，2025 年 2 月登在 ACM TKDD。 [哈尔滨工业大学] [[论文](https://arxiv.org/abs/2304.06975)] [[相关论文](https://arxiv.org/abs/2309.04175)] [[期刊](https://doi.org/10.1145/3686807)] [[代码](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)]
- **扁鹊-2 (BianQue-2)** 扁鹊二代开源医疗问诊模型，强化多轮追问；CMB 等中文医疗评测里的常见对照 [华南理工大学，广东省数字孪生人重点实验室] [[代码](https://github.com/scutcyr/BianQue)] [[模型](https://huggingface.co/scutcyr/BianQue-2)]
- [*arXiv*] **扁鹊 (BianQue)** 中文领域生活空间主动健康大模型 [华南理工大学，广东省数字孪生人重点实验室] [[代码](https://github.com/scutcyr/BianQue)] [[论文](https://arxiv.org/abs/2310.15896)]
- **孙思邈 (Sunsimiao)** 孙思邈中文医疗大模型，Sunsimiao-7B 基于 Qwen2-7B 以高质量医疗数据微调，在 CMB-Exam 达 30B 量级 SOTA [华东理工大学] [[代码](https://github.com/X-D-Lab/Sunsimiao)]
- **启真医学大模型 (QiZhenGPT)** 中文医疗场景、药品知识问答、优化疾病、手术、检验等 [浙江大学] [[代码](https://github.com/CMKRG/QiZhenGPT)]
- **卫宁WiNGPT2** 卫宁健康开源医疗大模型，底座Qwen，覆盖医学问答、病历理解和多轮问诊，7B/14B可下载 [卫宁健康] [[模型](https://huggingface.co/winninghealth/WiNGPT2-14B-Chat)] [[7B](https://huggingface.co/winninghealth/WiNGPT2-7B-Chat)]
- [*arXiv*] **华佗GPT-II (HuatuoGPT-II)** 中大深圳华佗系列二代，单阶段领域适配；7B/13B以Baichuan2为底座，是中文医疗评测里最常见的开源对照之一 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2311.09774)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-II)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT2-7B)]
- [*EMNLP findings*] **华佗GPT** 中文医学语料训练的大型语言模型 [香港中文大学(深圳)，深圳市大数据研究院] [[DOI](https://doi.org/10.18653/v1/2023.findings-emnlp.725)] [[论文](https://aclanthology.org/2023.findings-emnlp.725/)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT)]
- [*arXiv*] **SoulChat** 华南理工数字孪生人实验室的心理健康对话大模型，与扁鹊同系列，常作中文医疗/健康对话对照 [华南理工大学，广东省数字孪生人重点实验室] [[论文](https://arxiv.org/abs/2311.00273)] [[代码](https://github.com/scutcyr/SoulChat)] [[模型](https://huggingface.co/scutcyr/SoulChat)]
- **PULSE** 上海人工智能实验室 OpenMEDLab 的中文医疗大模型。PULSE-7b 基于 bloomz-7b1-mt，PULSE-20b 基于 InternLM-20B，覆盖医考、报告解读、病历结构化与模拟诊疗。 [上海人工智能实验室] [[代码](https://github.com/openmedlab/PULSE)] [[模型](https://huggingface.co/OpenMEDLab/PULSE-7bv5)]
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

- **讯飞星火医疗** 科大讯飞的星火医疗大模型X1，2025年3月发布，用在讯飞晓医上。报道里的测试数据来自讯飞晓医、智医助理等真实场景。 [科大讯飞] [[官网](https://www.xunfeihealthcare.com/)] [[新闻](https://www.cn-healthcare.com/article/20250303/wap-content-585822.html)]
- **蚂蚁阿福 / 蚂蚁医疗大模型** 2024年7月5日，支付宝在世界人工智能大会发布多模态医疗大模型，基座是百灵，能看药品、报告和影像。2025年12月15日，健康应用AQ升级为蚂蚁阿福，可以拍皮肤、检查报告和药盒来问。 [蚂蚁集团] [[官网](https://www.antafu.com/)] [[新闻稿](https://www.antgroup.com/news-media/press-releases/1720166400000)] [[新闻](https://www.antgroup.com/news-media/press-releases/1765785600000)]
- **腾讯混元医疗** 腾讯健康基于混元的闭源医疗大模型，覆盖问答、导诊、病历与影像；天衍实验室发布，无公开权重 [腾讯] [[官网](https://healthcare.tencent.com/)] [[新闻](https://healthcare.tencent.com/news/1603)]
- [*Sci China Life Sci*] **盘古药物分子大模型 (PanGu Drug Model)** 华为云与中科院上海药物所的闭源分子预训练模型（约17亿小分子），做属性预测/生成/优化；数智本草曾以其为底座之一 [华为云，中国科学院上海药物研究所] [[DOI](https://doi.org/10.1007/s11427-022-2239-y)] [[官网](https://www.huaweicloud.com/cases/pgyw.html)]

</details>

<details>
<summary>日韩汉方 / 韩医模型与系统（1）</summary>

- **KAMPO LLM** 官网仍开：VARYTEX 与日本东洋医学会合作的闭源汉方 API；页面写明 471 题评测 Pro 97.4%、Flash 92.1%，无公开权重 [VARYTEX，日本东洋医学会] [[官网](https://kampollm.varytex.co.jp/)]

</details>

<details>
<summary>Hugging Face 上的其他尺寸和 GGUF（11）</summary>

- **杏核内经推理模型** [[模型](https://huggingface.co/zsyjsld/Xinghe1.2-9B)] [[GGUF](https://huggingface.co/zsyjsld/Xinghe1.2-9B-GGUF)]
- **仲景** [[ZhongjingGPT1_13B](https://huggingface.co/CMLM/ZhongjingGPT1_13B)] [[ZhongJing-2-1.8B](https://huggingface.co/CMLL/ZhongJing-2-1_8b)]
- **白泽中医大模型** [[模型](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model)] [[8B-16bit](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit)]
- **ShizhenGPT 系列** [[7B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-LLM)] [[7B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-VL)] [[7B-Omni](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[32B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-LLM)] [[32B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-VL)]
- **扁仓 (BianCang) 系列** [[Qwen2.5-7B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)] [[Qwen2.5-14B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-14B-Instruct)]
- **MedChatZH** [[medchatzh](https://huggingface.co/tyang816/medchatzh)]
- **TCMChat** [[TCMChat-600k](https://huggingface.co/ZJUFanLab/TCMChat-600k)]
- **灵丹** [[Lingdan-13B-Base](https://huggingface.co/TCMLLM/Lingdan-13B-Base)] [[Lingdan-13B-PR](https://huggingface.co/TCMLLM/Lingdan-13B-PR)]
- **ChatTCM全参SFT版** [[模型](https://huggingface.co/SylvanL/ChatTCM-7B-SFT)]
- **ChatTCM** [[ChatTCM-7B-Pretrain](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)]
- **神农** [[ShenNong-TCM-LLM](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]

</details>

## 新闻

<details>
<summary>104 条，最近有：上海市卫生健康委员会、上海市中医药管理局 · 云南省人民政府办公厅印发《云南省中医药振 · 岐元</summary>

<details>
<summary>2026 · 68</summary>

- [2026.11.19] 上海市卫生健康委员会、上海市中医药管理局印发《上海市中医药高质量发展实施方案（2026—2030年）》（沪卫中发〔2026〕13号，成文2026年11月16日，上海市卫生健康委员会官网中医药工作栏目发布日期2026年11月19日）。方案依据国家《中医药振兴发展“十五五”规划》和《上海市国民经济和社会发展第十五个五年规划纲要》，经市卫生健康委第97次委务会审议通过，部署完善服务体系、全生命周期服务、中西医结合、人才队伍、传承创新、产业、文化、开放发展、数智化赋能与标准化、领域改革等10个方面30项任务。到2030年的目标包括：区属公立中医类医院全市覆盖率达100%；公立中医医院中医类别执业（助理）医师比例达60%、设置老年病科比例达90%、提供儿科服务比例达100%；社区卫生服务中心第一执业点中医类别执业（助理）医师比例达20%，能提供6类15项以上中医适宜技术的比例达80%；65岁以上老年人中医药健康管理率达80%，0—36个月儿童中医药健康管理率达90%；公立中医医院电子病历系统应用水平达到4级以上的比例达95%、三级公立中医医院达到5级以上的比例达50%；居民中医药健康文化素养水平达45%左右；新增牵头发布的国际标准不低于5项。数智化部分提出打造“数智中医药”，构建开放标准语料库，深化上海中药云平台，并开展中医药人工智能大模型研发与应用。本次打开了上海市卫生健康委员会官方通知全文页，并打开了同站2026年11月24日发布的政策解读页。这是上海市“十五五”中医药实施方案，不是单项产品发布。 [[上海市卫生健康委员会](https://wsjkw.sh.gov.cn/zyygz2/20261119/5ddfb74bd99345c5a97619b324230e35.html)] [[政策解读](https://wsjkw.sh.gov.cn/zyygz2/20261124/b3aae808c20f46a19d6372a449948dde.html)]
- [2026.11.11] 云南省人民政府办公厅印发《云南省中医药振兴发展“十五五”规划》（云政办发〔2026〕46号，成文2026年11月5日，云南省人民政府门户网站2026年11月11日公布）。规划提出到2030年中医药振兴发展取得新成效，实现人人享有中医药服务；部署建强服务体系、全生命周期服务供给、中西医协同、人才队伍、传承创新、产业和健康服务、文化繁荣、开放发展，以及加速中医药数智化赋能与标准化建设。数智化部分明确推进各级中医医疗机构规范接入省级全民健康信息平台，促进中医药高质量数据集建设和数据安全合规流通利用；探索“中医药+人工智能”，推动中医智能辅助诊疗等技术应用，加快智慧中医医院、中医互联网医院建设，并支持引进针灸、推拿机器人、智能煎制装备等数智化装备。规划还专节部署提升藏、傣、彝等少数民族医药服务能力。本次打开了云南省人民政府门户网站官方全文页。这是省级规划部署，不是已经上线的模型发布。 [[云南省人民政府](https://www.yn.gov.cn/zwgk/zcwj/yzfb/202611/t20261111_4383311.html)]
- [2026.11.09] 中新网11月9日报道，第九届进博会上，上海市第七人民医院完成进博会首秀，中医药人工智能中心主任赵铎路演**岐元**中医垂类大模型，现场还有AI面诊智能体与中医教学机器人「小柒」。岐元已于2026年7月发布，本报道写的是进博会展示与对口支援医院应用，不是首次发布。 [[链接](https://www.chinanews.com.cn/jk/2026/11-09/10729099.shtml)]
- [2026.11.09] 新华社北京11月9日电，国务院总理李强签署国务院令（国令第850号），公布《中医药传统知识保护条例》。条例共32条，明确建立保护数据库与保护名录等制度，自2027年1月1日起施行。 [[新华社](https://www.news.cn/politics/leaders/20261109/115bf875b154445787539419282ce542/c.html)] [[中国政府网](https://www.gov.cn/yaowen/liebiao/202611/content_7085599.htm)] [[条例全文](https://www.gov.cn/zhengce/zhengceku/202611/content_7085592.htm)]
- [2026.11.05] 新京报11月5日转载称，第五届问止中医临床学术会议于11月1日在深圳举行，会上正式发布中医评测基准**TCMQA**。报道称该基准含38279道执业医考选择题，并公布101位执业中医师作答形成的参考基线；题库与评测材料已在Hugging Face开源。本站已收录该基准条目，此为发布新闻。报道未把答题成绩等同于临床辨证能力。 [[链接](https://www.bjnews.com.cn/detail/1793844088129508.html)]
- [2026.11.05] 人民网11月5日采访国家中医药管理局监测统计中心主任厉将斌，介绍中医药独立赛道、名医智能体及高质量数据集建设。为新闻与建设线索，未附数据下载。 [[链接](https://finance.people.com.cn/n1/2026/1105/c1004-40828489.html)]
- [2026.11.05] 中科闻歌11月5日称，其国科智医团队联合中国中医科学院构建的中医大模型辨证论治评测基准**TCM-BEST4SDT**，论文在Nature Portfolio旗下《Scientific Data》在线发表。报道称基准含600条样本、27个评测维度，数据集和评测代码已公开。本站已收录该基准条目，此为发表新闻。 [[链接](https://www.wenge.com/site/a/202611/05/1070720261105103301.html)]
- [2026.11.04] 北京市卫健委11月4日刊载：10月30日会议讨论中医知识结构化、可信AI数据集、西苑医院中医药肿瘤科学数据系统等；报道未发布开放数据包。 [[链接](https://wjw.beijing.gov.cn/xwzx_20031/jcdt/202611/t20261104_4931739.html)]
- [2026.11.03] 山西省卫生健康委员会、山西省发展和改革委员会印发《山西省“十五五”中医药发展规划》（晋卫中医药科技发〔2026〕3号，成文2026年10月28日，省卫生健康委官网2026年11月3日公布）。规划提出到2030年中医药强省建设取得决定性进展，以科技创新、数智化转型、中西医协同为牵引，做大做强中医药“晋”字品牌；并专章部署加速中医药数智化赋能，包括建立中医药行业可信数据空间和人工智能高质量数据集，支持多模态大模型等技术用于中医辅助决策、病历质控、名老中医经验传承和中药新药研发，加强智慧中医医院建设并推动基层应用中医智能辅助诊疗。本次打开了山西省卫生健康委官方全文页。这是省级规划部署，不是已经上线的模型发布。 [[山西省卫生健康委](https://wjw.shanxi.gov.cn/tzgg/zcwj/202611/t20261103_10251747.shtml)]
- [2026.11.03] 山东省人民政府印发《山东省中医药发展“十五五”规划》（鲁政发〔2026〕23号，成文2026年10月23日，2026年11月3日公布）。规划提出实施齐鲁中医药振兴发展“六名四化”战略，推动中医药现代化、产业化、智慧化、生活化，到2030年实现人人享有中医药服务；重点任务包括中医药古籍数字化、数字智能应用人才培养，以及推动中医药数智化赋能。这是省级规划部署，不是已经上线的模型发布。 [[山东省人民政府](http://www.shandong.gov.cn/art/2026/11/3/art_267492_89889.html)] [[政策解读](http://www.shandong.gov.cn/art/2026/11/3/art_306404_21741.html)]
- [2026.11.03] 数字中国建设峰会网站11月3日转载经济日报报道，介绍《人工智能赋能全球传统医学发展报告（2026）》及杭州市中医院“中医小安”机器人。报道涵盖AI传统医学整体，不等同于TCM大语言模型统计。 [[链接](https://www.digitalchina.gov.cn/2026/szzg/xyzx/202611/t20261103_5389002.htm)]
- [2026.11.02] 广东省卫生健康委、广东省中医药局、广东省发展改革委印发《广东省中医药发展“十五五”规划》（粤卫〔2026〕4号，成文2026年10月8日，2026年11月2日在省中医药局官网公布）。规划以中西医协同、数智化转型、粤港澳联动为引领，提出到2030年全面实现人人享有优质中医药服务；并专章部署加速中医药数智化赋能，支持中医药大模型和智能体开发应用，探索建设高质量数据集、数字化平台与知识图谱，加强智慧中医医院建设。这是省级规划部署，不是已经上线的模型发布。 [[广东省中医药局](http://szyyj.gd.gov.cn/zwgk/gsgg/content/post_4974266.html)]
- [2026.10.28] 国家中医药管理局综合司印发《2026—2028年周期全国基层中医药工作示范市（县）建设标准》（国中医药综医政函〔2026〕225号，成文2026年10月10日，国家中医药管理局官网页面标注时间为2026年10月28日）。通知依据《全国基层中医药工作示范市（县）管理办法》（国中医药医政发〔2026〕5号），规范开展本周期示范市（县）创建工作，并废止2022年印发的示范市、示范县建设标准（国中医药医政发〔2022〕1号）。本次检索打开了湖南省人民政府门户网站转载的国家中医药管理局网站全文（该站标注发文日期2026-10-10、发布时间2026-11-03、信息来源为国家中医药管理局网站），并核到官网原链为http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39041.html；本轮直接访问该官网地址返回超时或HTTP 500。这是示范创建标准，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39041.html)] [[湖南省人民政府转载](http://www.hunan.gov.cn/zqt/zcsd/202611/t20261103_34093522.html)]
- [2026.10.28] 国家中医药管理局综合司公布2026—2028年周期全国基层中医药工作示范市（县）创建单位名单（国中医药综医政函〔2026〕238号，成文2026年10月23日）。通知要求各创建单位对照本周期建设标准推进创建任务，省级中医药主管部门加强管理指导与日常监测，国家中医药管理局将在周期结束前组织评估验收，合格的正式命名。本次打开了湖南省人民政府门户网站转载的国家中医药管理局网站全文（该站标注发文日期2026-10-23、发布时间2026-11-03、信息来源为国家中医药管理局网站）；官网原链为http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39040.html，本轮直接访问该官网地址返回超时或HTTP 500。这是创建单位名单公布，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39040.html)] [[湖南省人民政府转载](http://www.hunan.gov.cn/zqt/zcsd/202611/t20261103_34093548.html)]
- [2026.10.28] 国家中医药局综合司、国家卫生健康委办公厅印发《关于推进基层中医适宜技术推广应用的通知》（国中医药综医政发〔2026〕8号，成文2026年10月14日，国家中医药管理局官网及中国政府网转载新华社稿2026年10月28日发布）。通知要求建设国家、省、市、县推广网络，到2030年县级推广中心基本全覆盖，优先推广6类15项以上中医适宜技术；并专章部署推广工作数智化支撑，探索应用人工智能辅助教学、辅助诊疗和质控分析工具。这是基层适宜技术推广政策，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39042.html)] [[中国政府网](https://www.gov.cn/lianbo/202610/content_7084413.htm)]
- [2026.10.27] 凤凰网财经10月31日报道，天纪易岐称其端侧模型**易岐中医AI**已于10月27日完成调试并上线，可在完全断网的本地终端推理，面向体质辨识、健康评估等场景。此为公司发布稿转载，本页未独立核验其临床效果或部署范围。该模型与古籍数据库ETCM不是同一事物。 [[链接](https://news.10jqka.com.cn/20261031/c681322899.shtml)]
- [2026.10.26] 福建省卫生健康委员会、福建省中医药管理局等十三部门印发《福建省提升中药质量促进中医药产业高质量发展的若干措施》（闽卫规〔2026〕4号，成文2026年10月15日，省卫生健康委官网2026年10月26日公布，有效期至2030年12月31日）。措施落实国办发〔2025〕11号，部署闽产道地药材保护、规范化种植、产业集群和中药工业升级等，并明确引导中药企业加快智能化改造、梯度建设智能工厂，以及建设信息化追溯系统。本次打开了省政府卫生健康委官方页面和主动公开PDF。这是省级产业质量政策，不是单项产品发布。 [[福建省卫生健康委](https://wjw.fujian.gov.cn/xxgk/fgwj/zxwj/202610/t20261026_7240705.htm)] [[官方PDF](https://wjw.fujian.gov.cn/xxgk/fgwj/zxwj/202610/P020261026658500638498.pdf)]
- [2026.10.24] 广安门医院10月24日报道，10月17日至18日的2026世界传统医药大会上，**广医·岐智**展示院内部署与病历生成，杭州市中医院具身智能机器人**中医小安**演示舌面象和脉象采集，中科云诊则展示**妙悟岐黄**辅助诊疗与可追溯辨证。报道中的分诊人次、书写时长和辨证一致率来自参展方介绍，不宜直接当成评测结论。 [[链接](https://www.gamyy.cn/gzb/news/trends/118061.html)]
- [2026.10.22] 湖北省卫生健康委员会官网2026年10月22日发布政策解读称，经省人民政府同意后，省卫生健康委、省发展改革委、省中医药管理局于2026年9月19日联合印发《湖北省中医药发展“十五五”规划》。解读明确规划提出到2030年实现人人享有中医药服务，并部署数智赋能与标准化等重点任务，包括持续推进智慧医院建设、深化数据资源开发利用和推进中医药人工智能建设。本次打开了湖北省卫生健康委的官方解读页；官网列出的规划正文链接在本次核验中返回404，故不以正文页作为依据。这是省级规划部署，不是已经上线的模型发布。 [[政策解读](https://wjw.hubei.gov.cn/zfxxgk/zc/zcjd_1/202610/t20261022_6037633.shtml)]
- [2026.10.21] 智通财经10月21日报道，医渡科技在2026世界传统医药大会成果发布环节推出中医循证智能体**小黄岐**，面向古籍与指南检索、辅助辨证、方剂查询和中医术语中英互译，并称回答可追溯证据来源。报道中的知识条目数量与医院落地范围来自企业介绍，本页未独立核验。 [[链接](https://www.zhitongcaijing.com/content/detail/1509924.html)]
- [2026.10.20] 川观新闻10月20日报道，《四川省中医药发展“十五五”规划》印发，提出支持中医药数智创新平台建设，开发名中医智能化诊疗等大模型，开展基层中医智能辅助诊疗试点，并建设高质量数据集与数智中医药协同创新中心。这是规划部署，不是已经上线的模型发布。 [[链接](https://cbgc.scol.com.cn/news/8074897)]
- [2026.10.18] 北京市科技信息门户转载《北京日报》报道，10月18日在2026世界传统医药大会“北京成果”专场，北京数智中医产业发展研究院发布智能体“数小禾”，基于本地算力和自主知识产权知识库，提供中英文中医智能服务。 [[链接](https://www.ncsti.gov.cn/kjdt/xwjj/202610/t20261027_259363.html)]
- [2026.10.18] 凤凰网科技10月19日转载称，传神素问与名医在线于10月18日在2026世界传统医药大会联合发布**范吉平数字孪生**，以传神素问中医大模型为底座，整理医案与诊疗资料后用于问诊、辨证和处方建议。这是名医数字孪生的单例发布，报道未给出可独立核验的临床对照结果。 [[链接](https://tech.ifeng.com/c/8xLt1uquwDi)]
- [2026.10.16] 中国中医药报10月16日报道汉派中医骨伤诊疗数据集在湖北数据流通平台交易，涉及16.8万条结构化诊疗数据、3600个经验方与辨证论治思维链；属于许可流通案例。 [[链接](https://www.cntcm.com.cn/content/202610/16/c505880.html)]
- [2026.10.14] 国家中医药管理局印发《中医医疗质量控制中心管理规定》（国中医药医政发〔2026〕10号，成文2026年10月8日，国家中医药管理局官网2026年10月14日公布全文，自印发之日起施行）。规定适用于各级中医质控中心建设与管理，明确国家级中心由国家中医药局设置管理，省级及以下参照执行；并规定质控中心应利用信息化手段开展质控，使用现有数据采集平台收集分析中医质控数据，落实网络和数据安全要求。本次打开了国家中医药管理局官方全文页及政策解读页。这是质控组织管理规定，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-10-14/38883.html)] [[政策解读](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-10-14/38884.html)]
- [2026.10.12] 《海南自由贸易港中医药发展促进条例》已由海南省第七届人民代表大会常务委员会第二十六次会议于2026年9月30日通过，以海南省人民代表大会常务委员会公告第114号公布，自2026年11月1日起施行，共九章五十条。条例结合海南自由贸易港实际，对中医药服务、中药保护与产业发展、黎苗等民族医药发展、人才培养与科技支撑、传承创新与文化传播、开放发展与国际合作及保障措施作出制度安排；明确鼓励智慧中医医疗机构建设，允许综合运用互联网等现代信息技术和具备医疗器械资质的人工智能设备提供中医药服务，支持黎苗医药传承人运用数字设备和人工智能建立数字化、影像化传承档案，并支持建设中医药真实世界研究平台。本次打开了三亚市人大官网登载的条例全文，以及《海南日报》2026年10月12日文件版刊登的常委会公告。这是省级地方性法规，不是已经上线的模型发布。 [[三亚市人大](https://rd.sanya.gov.cn/rdsite/jgjs/202610/abc6e991368744248da826826aa4d6f3.shtml)] [[海南日报](http://news.hndaily.cn/html/2026-10/12/content_58468_19930810.htm)]
- [2026.10.09] 湖南省人民政府办公厅印发《湖南省中医药发展“十五五”规划》（湘政办发〔2026〕53号，发文日期2026年10月9日）。规划提出到2030年实现人人享有中医药服务，部署九个方面34项重点任务，其中包括加速中医药数智化赋能：建设智慧中医医院、探索处方共享与数据互联，加快中医药人工智能应用场景建设，扩大智能辅助诊疗和中药智能调配在基层的应用，并加强高质量数据集建设。省中医药管理局解读于2026年11月11日在省政府门户发布。这是省级规划部署，不是已经上线的模型发布。 [[湖南省人民政府](https://www.hunan.gov.cn/hnszf/xxgk/wjk/szfbgt/202610/t20261023_34087538.html)] [[政策解读](http://www.hunan.gov.cn/hnszf/xxgk/jd/bmjd/202611/t20261111_34099599.html)]
- [2026.10.09] 报道称徐桂华团队10月9日发布灵素·艾护中医护理大模型，面向辨证施护、科研与居家康养，27所加盟医院为首批应用单位 [[链接](https://finance.sina.com.cn/jjxw/2026-10-10/doc-iniutqmk0582279.shtml)]
- [2026.10.08] 国家中医药管理局医政司发布《关于做好中医护理方案和护理人员中医技术使用手册使用工作的通知》（国家中医药管理局官网标注时间2026年10月8日）。通知称，为提升中医护理能力、优化中医护理服务，国家中医药局委托中华中医药学会组织专家修订形成中风等13个病种中医护理方案（2026年版）和《护理人员中医技术使用手册（2026年版）》，并已在中华中医药学会网站发布，要求各级中医药主管部门组织相关医疗机构结合实际推广应用。本次打开了国家中医药管理局官方通知页。这是护理方案推广通知，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-10-08/38852.html)]
- [2026.09.30] 福建省卫生健康委员会、福建省中医药管理局印发《福建省“十五五”中医药振兴发展规划》（2026年9月29日印发，省卫生健康委官网标注发布时间2026年9月30日）。规划提出到2030年中医药高质量发展体制机制更加健全，实现人人享有中医药服务，推进中医药强省建设；部署服务体系、全生命周期服务、中西医协同、人才队伍、传承创新、产业新体系、文化传播、闽台融合与开放发展，以及数智化赋能、标准化和“三医”协同改革。数智化部分提出打造闽派中医特色高质量数据集与中医智能体，开展数据资产确权转化试点，落实“数据要素×”三年行动，支持省级中医医院打造智慧院区、建设专科大模型，归集名老中医经验，推动中医智能辅助决策系统与诊疗装备落地应用。这与已入库的《福建省提升中药质量促进中医药产业高质量发展的若干措施》不是同一份文件。本次打开了福建省卫生健康委官方全文页及附件PDF。这是省级规划部署，不是已经上线的模型发布。 [[福建省卫生健康委](https://wjw.fujian.gov.cn/xxgk/fgwj/zxwj/202610/t20261008_7222126.htm)] [[规划PDF](https://wjw.fujian.gov.cn/xxgk/fgwj/zxwj/202610/P020261008767413247349.pdf)]
- [2026.09.30] 宁夏回族自治区卫生健康委员会、自治区发展和改革委员会印发《宁夏回族自治区中医药振兴发展“十五五”规划》（自治区人民政府宁政函〔2026〕55号于2026年9月11日批复同意，两部门2026年9月16日印发，自治区卫生健康委官网2026年9月30日公布全文）。规划提出到2030年覆盖全民和全生命周期的中医药服务体系更加健全，实现人人享有中医药服务；部署完善服务体系、提升全生命周期服务能力、中西医协同、人才队伍、传承创新、健康服务融合、文化繁荣和开放发展，以及数智化标准化赋能与治理。数智化部分提出探索人工智能赋能中医药对外交流和高质量发展路径，实施自治区中医药智慧赋能项目，规范建设智慧中医医院和智慧中药房，并加强人工智能技术在基层中医药服务中的精准应用。本次打开了自治区卫生健康委官方全文页和自治区人民政府批复页。这是省级规划部署，不是已经上线的模型发布。 [[宁夏卫生健康委](https://wsjkw.nx.gov.cn/zfxxgk_279/fdzdgknr/gfxwj/202609/t20260930_5362324.html)] [[宁夏回族自治区人民政府](https://www.nx.gov.cn/zwgk/qzfwj/202609/t20260924_5356174.html)]
- [2026.09.24] 中国中医药报9月24日报道广安门医院慢性胃炎数据集完成产权登记，并建设中医专病可信数据空间；数据用于广医·岐智微调、科研和名医经验教学，未见公开下载。 [[链接](https://www.cntcm.com.cn/content/202609/24/c505607.html)]
- [2026.09.22] 大洋网9月22日报道，第二届广东省人工智能应用对接大会上，广东省中医院介绍名老中医辅助诊疗大模型矩阵，并称**禤国维**皮肤病诊疗大模型已于2025年6月投用。报道写核心病种诊断准确率达95%以上、已辅助决策2917次，上述数字来自院方介绍，不是外部对照试验结论。该院矩阵启动此前已有报道。 [[链接](https://news.dayoo.com/guangzhou/202609/22/139995_55006505.htm)]
- [2026.09.21] 中国中医药报9月30日报道，9月20日至21日，2026年数智中医药推进现场会暨数据要素综合试验区现场会在重庆举行，交流人工智能赋能中医药、数据要素与应用场景。报道提到横琴垂类模型、中药工业大模型和各地智能体实践，是会议综述，不代表新的模型首发。 [[链接](https://www.cntcm.com.cn/content/202609/30/c505658.html)]
- [2026.09.19] 中新网报道方证大模型9月19日开放接入，覆盖临床辅助诊疗、科研数据挖掘和人才培养，并计划部署到龙华医院及医联体 [[链接](https://www.chinanews.com.cn/jk/2026/09-19/10699553.shtml)]
- [2026.09.15] 界面新闻报道，9月15日第七届馆交会暨中医药发展大会上，传神素问推出**百医孪生计划**，拟依托其「素问」中医大模型为全国100位名老中医打造数字分身。这是计划发布，报道未列出已完成的全部名单，也未提供可独立核验的一致率数据。 [[链接](https://www.jiemian.com/article/15106308.html)]
- [2026.09.07] 工业和信息化部等六部门印发工信部联消费〔2026〕204号意见，将中药列为历史经典产业，并部署编制人工智能赋能实施指南、建设高质量数据集、用大模型解析传统工艺，以及发展智慧药房和产业工艺知识图谱。 [[工信部](https://www.miit.gov.cn/jgsj/xfpgys/wjfb/art/2026/art_ece6902ba0b24ad2806e670618f17a9f.html)] [[新华社](http://www.news.cn/politics/20260907/1d0ae2bfeb1f4d0fb58f7611ba77a3c3/c.html)]
- [2026.09] 中国中医科学院广安门医院在2026服贸会展示**广医·岐智2.0**，以AI医生「安安」覆盖患者服务、临床诊疗、病房管理等六大场景 [[链接](https://app.xinhuanet.com/news/article.html?articleId=202609101de3e66a53f7474ba7d373deaaa7e122)]
- [2026.09] 2026服贸会中医药展区，北京中医药大学**首发首展**中医体质辨识体系与具身智能推拿机器人，同期还有智能诊脉设备体验 [[链接](https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202608/t20260807_4812596.html)]
- [2026.08.27] 学校官网称，8月27日“黔小杏医疗大模型”在2026数博会发布，以中医药文献、名医经验和临床数据训练，用于辅助诊断、体质辨识、养生推荐和用药指导。 [[链接](https://www.gzy.edu.cn/info/1501/12735.htm)]
- [2026.08] 南方财经报道，广州中医药大学以通用大模型为基座、用约20亿词元中医药数据持续训练“杏林智慧教学大模型”，已在中医各家学说、中国医学史和中医外科学试点。 [[链接](https://m.21jingji.com/article/20260824/herald/ef692f3ceba10c36edd3952f4d5ca892.html)]
- [2026.07.31] 广西壮族自治区人民政府办公厅印发《广西中医药（壮瑶医药）振兴发展“十五五”规划》（桂政办发〔2026〕50号，成文2026年7月24日，自治区人民政府门户网站2026年7月31日公布，刊于政府公报2026年第15期）。规划提出到2030年中医药传承创新发展机制更加完善，覆盖全民、全生命周期的中医药服务体系更加健全，基本形成服务惠民、产业兴旺、创新活跃、开放包容的中医药发展新格局；并专章部署加速中医药数智化赋能，实施“人工智能＋中医药”行动，建设智慧中医医院，支持基层配备中医智能辅助诊疗系统，建立中医药人工智能高质量数据集，推进人工智能在中医辅助决策、名老中医经验传承、诊疗康复等场景应用，支持自治区人工智能壮瑶医诊疗场景工程研究中心等项目。本次打开了自治区人民政府门户网站官方全文页。这是省级规划部署，不是已经上线的模型发布。 [[广西壮族自治区人民政府](http://www.gxzf.gov.cn/zfwj/zxwj/t27966422.shtml)]
- [2026.07.29] 贵州医科大学等在中国—东盟教育交流周发布全国首个民族药创制全域智能平台**华族本草**，以数智岐黄+Qwen为底座融汇多民族医药古籍 [[链接](https://www.gmc.edu.cn/info/1058/30267.htm)]
- [2026.07.28] 国家中医药局等十一部门印发《医疗卫生强基工程中医药行动方案》（国中医药医政发〔2026〕6号，成文2026年7月11日）。方案提出到2030年基层中医药服务网络全面建立，基础设施和数智化条件明显改善，并部署七项行动；其中明确加快县级中医医院信息化、持续推进智慧中医医院建设，探索医学人工智能辅助诊疗在基层中医药服务和名中医经验传承等场景的应用。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202607/content_7076920.htm)] [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-07-28/38433.html)]
- [2026.07.24] 上海中医药大学附属第七人民医院正式发布**岐元大模型**，采用预训练+领域微调+专家强化学习，支持生成式病历与名老中医Agent数字孪生，并亮相WAIC [[链接](https://dwgk.shutcm.edu.cn/2026/0725/c1890a175544/page.htm)]
- [2026.07.23] 经国务院批复同意（国函〔2026〕71号），国家中医药局、国家发展改革委联合印发《中医药振兴发展“十五五”规划》（国中医药规财发〔2026〕8号）。规划提出到2030年实现人人享有中医药服务，并部署十个方面重点任务，其中包括加速中医药数智化赋能与标准化建设；政策解读明确提出运用人工智能等新技术挖掘和传承中医药宝库。这是国家层面的五年规划，不是单项产品发布。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202607/content_7076394.htm)] [[国家中医药管理局](http://www.natcm.gov.cn/guicaisi/zhengcewenjian/2026-07-22/38398.html)] [[新华社](https://www.news.cn/20260723/d6c2ca040e534b9186271da832c4ec6b/c.html)]
- [2026.07.03] 北京市卫生健康委网站转载《中国妇女报》报道，7月3日论坛以“数启岐黄·智赋本草”为主题在京举行，发布中医药智能体技术要求等标准、16项数字中医药应用场景案例，并启动“数据要素×”大赛北京分赛中医药赛道。 [[链接](https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202607/t20260706_4748255.html)]
- [2026.07.01] 山西省卫生健康委员会、山西省药品监督管理局印发《中药饮片代煎服务质量管理规范》（晋卫中医药科技规〔2026〕1号，成文2026年6月16日）。规范适用于省内各级各类医疗机构，以及承接省内中药饮片代煎服务的生产、经营企业，覆盖医疗机构委托企业代煎和患者委托零售药店代煎两类场景；明确代煎属于中药饮片使用和销售的延伸服务，坚持患者自愿。规范厘清质量责任，医疗机构对代煎剂质量负主体责任，受托企业承担直接质量责任，禁止毒性中药、麻醉类中药饮片处方委托代煎，禁止将代煎业务再委托。追溯方面要求煎药过程视频监控资料留存不少于90天，代煎药液附带追溯二维码，原始处方、煎制工艺数据和设备运行日志至少保存一年，数据保存期限不少于三年。附则写明本规范有效期五年，自2026年8月1日起施行。本次打开了山西省卫生健康委员会政策文件栏目官方全文页，该页标注发布时间为2026-07-01 13:40，页面URL路径为2026-07-29。2026年11月24日，省卫生健康委员会新闻页和人民网山西频道（来源《山西日报》）对同一规范作了报道，作为后发新闻链接保留，不另作新条目。这是省级中药饮片代煎质量规范，此前目录漏收。 [[山西省卫生健康委员会](https://wjw.shanxi.gov.cn/tzgg/zcwj/202607/t20260729_10186628.shtml)] [[省卫生健康委员会新闻](https://wjw.shanxi.gov.cn/xwzx/szyw/202611/t20261124_10265935.shtml)] [[人民网山西频道](http://sx.people.com.cn/n2/2026/1124/c352662-41759168.html)]
- [2026.07] 新华网报道，2026年7月国家人工智能应用中试基地（医疗）在河南省人工智能大会集中发布中医经络辅诊模型、中西医结合食管癌大模型、中医药高质量数据集、中药研发大模型和名中医数字智能体。 [[链接](http://www.ha.xinhuanet.com/20260928/c8569fe1fbdb4ebc81053d86c6d93682/c.html)]
- [2026.07] 智慧眼携**砭石云中医**亮相WAIC 2026，以已备案砭石多模态大模型为底座，展示四诊仪与辅助诊疗系统 [[链接](http://www.eeo.com.cn/2026/0720/965556.shtml)]
- [2026.07] 安顿健康在WAIC 2026首发**七诊合参**中医机器人，集成面/红外面/舌/耳/闻/问/脉采集；报道称底座为2350亿参数的中医大模型。该页未写天回 [[链接](https://www.news.cn/finance/20260720/f6a8625c1be4412d9c311a232c7a35fa/c.html)]
- [2026.06] 中科闻歌通过港交所上市聆讯；报道提及与中国中医科学院合作的**大医金匮**中医大模型已通过中国信通院最高级别可信AI认证 [[链接](https://www.ncsti.gov.cn/kjdt/xwjj/202606/t20260610_249369.html)]
- [2026.05] 北京中医药大学中药学院称薪火中国药在世界数字教育大会发布，问答版已上线国家智慧教育公共服务平台 [[链接](https://zhongyao.bucm.edu.cn/yyxw/fb4b320d30c34e358de28a637c9f6f2c.htm)]
- [2026.04.24] 浙江省人民政府办公厅印发《浙江省“十五五”中医药发展规划》（浙政办发〔2026〕14号，2026年4月24日）。规划提出到2030年基本建成中医药现代化先行省，中医药人工智能应用水平全国领先，并统筹服务、产业、科技、人才、文化、治理、数智“七位一体”现代化；主要指标明确中医类医疗机构医学大模型应用率到2030年达到100%，同时提出推动浙江成为中医药人工智能发展的重要策源地。这是省级规划部署，不是已经上线的模型发布。 [[浙江省政府公开文本](https://zjjcmspublicnew.oss-cn-hangzhou-zwynet-d01-a.internet.cloud.zj.gov.cn/cms_files/filemanager/1567290/attach/20266/054C52CACC6589E4F1917D8B993978B9.pdf)] [[商务部转载](https://tradeinservices.mofcom.gov.cn/article/zcfb/zcfg/202607/200234.html)] [[浙江中医药大学转载](https://itc.zcmu.edu.cn/202607132.pdf)]
- [2026.04.21] 国家中医药管理局印发《全国基层中医药工作示范市（县）管理办法》（国中医药医政发〔2026〕5号）。办法规定示范市（县）创建每3年为一个周期，由国家中医药管理局负责总体规划与组织管理；申报经市县级自评、省级审核推荐、国家局复核后确定为创建单位，创建周期结束前6个月开展省级和国家评估验收，合格后命名。中国中医药报官网全文页标注来源为国家中医药管理局、日期为2026年4月22日；官网原链为http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-04-21/37964.html。本次打开了中国中医药报全文页；本轮直接访问国家中医药管理局原页返回超时或HTTP 500。这是示范创建管理办法，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-04-21/37964.html)] [[中国中医药报](https://www.cntcm.com.cn/m/content/202604/22/c502106.html)] [[政策解读](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-04-21/37965.html)]
- [2026.04.21] 北京中医药大学牵头研发的**薪火中国药**中医药教育大模型通过国家生成式人工智能服务备案，成为国内首个获批面向公众服务的中医药领域大模型 [[链接](https://regional.chinadaily.com.cn/education/cn/2026-04/22/c_1177692.htm)]
- [2026.04.14] 广西壮族自治区卫生健康委员会、自治区中医药管理局、自治区工业和信息化厅印发《广西中医药产业高质量发展三年行动方案（2026—2028年）》（桂中医药发〔2026〕10号，成文2026年4月9日，经自治区人民政府同意，自治区卫生健康委官网2026年4月14日公布全文）。方案提出到2028年中医药全产业链总产值突破1100亿元；部署中药材种植养殖、中药制造数智化绿色化改造、质量追溯体系，以及拓展人工智能＋中医药诊疗服务应用场景，支持基层配备中医智能辅助诊疗系统、便携式智能理疗设备和远程会诊终端，并投入支持智慧中医医院建设。这与同日核验入库的《广西中医药（壮瑶医药）振兴发展“十五五”规划》不是同一份文件。本次打开了自治区卫生健康委官方全文页及政策解读页。这是省级产业行动方案，不是已经上线的模型发布。 [[广西卫生健康委](https://wsjkw.gxzf.gov.cn/xxgk_49493/fdzdgk/gkwj/zzqzcwj/t27468144.shtml)] [[政策解读](https://wsjkw.gxzf.gov.cn/xxgk_49493/fdzdgk/gkwj/zcjd/t27468260.shtml)]
- [2026.04.08] 国家中医药局、国家卫生健康委印发《医院中药饮片管理规范（2026版）》（国中医药医政发〔2026〕3号，成文2026年4月8日，中国政府网国务院部门文件库刊登全文）。规范适用于各级各类医院中药饮片采购、验收、贮藏与养护、调剂、临方炮制、煎煮、临方加工、处方点评等管理，自发布之日起施行，2007年版规范同时废止。文件要求以质量管理为核心，鼓励使用信息化手段加强中药饮片管理；对代煎服务明确医院负主体责任、受托机构负直接责任，并要求建立健全代煎质量跟踪、追溯、监控体系。本次打开了中国政府网官方全文页。这是部门管理规范，不是已经上线的模型发布。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202604/content_7066059.htm)]
- [2026.04] 山东中医药大学附属医院启动山东省卫健委「人工智能＋」中医药重点场景**智汇岐黄**大模型项目 [[链接](http://ccpd.china.com.cn/2026-04/17/content_43401621.html)]
- [2026.03.27] 国家中医药管理局印发《三级中医医院评审标准（2026年版）》（国中医药医政函〔2026〕39号，成文2026年3月13日）。通知提出，为落实“强基、稳二、控三”工作部署和分级诊疗制度要求，优化完善中医医院评审制度，该标准自通知印发之日起实施，2017年版三级中医医院、三级中西医结合医院、三级民族医医院评审标准及其实施细则等评审规定同时废止。本次打开了中国政府网国务院部门文件页（来源标注为国家中医药局网站）及可公开下载的官方PDF（政府网文件最后修改时间为2026年3月28日）。官网原链为http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-03-27/37885.html。这是医院评审标准，不是单项产品发布。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202603/content_7064072.htm)] [[官方PDF](https://www.gov.cn/zhengce/zhengceku/202603/P020260328646933871054.pdf)] [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-03-27/37885.html)]
- [2026.03.23] 国家中医药局、国家卫生健康委、国家疾控局印发《乡镇卫生院 社区卫生服务中心中医药服务管理基本规范》（国中医药医政发〔2026〕2号，成文2026年3月11日），对2003年版乡镇卫生院、社区卫生服务中心两项基本规范进行合并修订。规范共六章，适用于依法设立的乡镇卫生院、社区卫生服务中心，明确中医科和中药房建设、人员配备、服务内容及业务指导等要求。本次打开了中国政府网国务院部门文件页全文（来源标注为国家中医药局网站），并核到新华社经中国政府网转发的报道（2026年3月24日）。官网原链为http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-03-23/37872.html。这是基层中医药服务管理规范，不是单项产品发布。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202603/content_7063623.htm)] [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-03-23/37872.html)] [[新华社报道](https://www.gov.cn/lianbo/202603/content_7063620.htm)]
- [2026.03.17] 中国中医药报报道，2026年3月17日研讨会上，中医药信息研究所所长李海燕介绍医源中医大模型已用于医案结构化、智能问诊、处方推荐和中成药合理使用等场景。 [[链接](https://www.cntcm.com.cn/content/202603/20/c501417.html)]
- [2026.03] 上海中医药大学称方证多模态大模型入选医疗领域国家人工智能应用中试基地阶段成果，基座为视觉语言模型 [[链接](https://kjrw.shutcm.edu.cn/2026/0330/c805a172392/page.htm)]
- [2026.02] 工信部等八部门印发《中药工业高质量发展实施方案（2026—2030年）》，明确运用人工智能与知识图谱赋能经典名方与名老中医经验方研发 [[链接](https://www.gov.cn/zhengce/zhengceku/202602/content_7057174.htm)]
- [2026.01.09] 科技日报报道，1月9日广东省中医院启动名老中医辅助诊疗大模型矩阵；禤国维皮肤病诊疗大模型和心血管病诊疗大模型已投入临床。 [[链接](https://www.stdaily.com/web/gdxw/2026-01/12/content_460323.html)]
- [2026.01] 新华网报道，2025年12月24日河南健康产业大会上，河南省卫生健康委展示中医经络辅助诊断模型和豫产豫药多模态神农本草大模型，后者用于药材识别、真伪鉴别、成分定量和产地溯源。 [[链接](http://www.ha.xinhuanet.com/20260105/b91d84bacd1c46389a007e0cc201962d/c.html)]
- [2026.01] 成都中医药大学官网称，温川飙团队牵头的“中医药AI模型高质量数据集”（项目编号2025-AISJK-02013）入选工信部与药监局2025年度人工智能医疗器械创新任务揭榜名单。 [[链接](https://www.cdutcm.edu.cn/info/1074/138321.htm)]
- [2026.01] 中医聪宝称素问中医内容生成大模型算法列入国家网信办第十四批深度合成服务算法备案 [[链接](https://www.tcmbrain.com/?list_43/180.html)]

</details>

<details>
<summary>2025 · 30</summary>

- [2025.12.20] 吉林发布**众星·长白岐黄1.0** AI原生多模态中医药大模型 [[链接](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- [2025.12] **智明堂ZMT-M1**在国家中医执业医师资格考试模拟测试中以96.26分获得该领域最佳成绩，已在全国100余间诊室试点应用 [[链接](https://m.tech.china.com/redian/2025/1229/122025_1789291.html)]
- [2025.12] 广安门医院官网称广医·岐智取得国家级深度合成算法备案，并称是国内首家完成该项备案的中医院 [[链接](https://www.gamyy.cn/gzb/news/big/114632.html)]
- [2025.12] 固生堂发布“中医大脑”及国医大师施杞教授AI数字分身，已累计发布14位顶级专家数字分身。八大专科出自另一则十大分身报道，本页未写 [[链接](https://www.jjckb.cn/20251231/693ca93b14ff4f57adc359959dc0320d/c.html)]
- [2025.11.02] 北京科技大学新闻网称，2025年11月2日郑州大会上，学校联合郑州市卫健委、郑州市中医院和河南中医药大学数智中医药研究院发布岐黄针灸大模型，四诊采集后生成针灸处方。 [[链接](https://news.ustb.edu.cn/info/1087/72015.htm)]
- [2025.11] 国家卫健委等五部门印发《关于促进和规范”人工智能+医疗卫生”应用发展的实施意见》，明确支撑建设中医药诊疗大模型 [[链接](https://www.gov.cn/zhengce/zhengceku/202511/content_7047018.htm)]
- [2025.10.26] 中国经济网报道10月26日发布中西医结合高血压诊疗大模型Idiom-Hypertension，用于高血压规范管理 [[链接](https://www.ce.cn/cysc/yy/hydt/202510/t20251027_2541616.shtml)]
- [2025.10.21] 科技日报报道CTA在中医药临床疗效评价大会发布，基于Qwen2.5-14B微调，面向临床试验方案、数据管理与统计 [[链接](https://www.stdaily.com/web/gdxw/2025-10/21/content_418966.html)]
- [2025.09.18] 中原药谷基层中医药振兴工程下，**伊尹中医经典大模型**在嵩县发布启用，融合中医教育与AI辅助诊疗服务县域基层 [[链接](http://www.ha.xinhuanet.com/20250918/a3da94037689422dbcd1fe57fa62ef94/c.html)]
- [2025.09.12] 广安门医院官网称，2025年9月12日服贸会论坛发布广医·岐智2.0，并推出AI医生安安，已出现在门诊导诊屏和预问诊界面。 [[链接](https://www.gamyy.cn/gzb/news/big/113898.html)]
- [2025.09] **智赋岐黄天功**中医AI大模型通过国家深度合成服务算法备案，应用于中医四诊仪与体质辨识 [[链接](http://zs.scbzol.com/zs/2025/0919/328624.html)]
- [2025.09] 页面受评对象是**传神素问**中医大模型，获得可信AI中医药大模型4+级；正文写它由传神语联基于任度大模型打造 [[链接](https://zhongyi.gmw.cn/2025-09/10/content_38277329.htm)]
- [2025.09] 中国中医科学院官网称，2025年9月10日至14日服贸会上，其智能科学与工程技术研究中心展示大医金匮大语言模型与多轮问诊系统，以及舌诊仪和移动中医智能检测厅。 [[链接](https://www.cacms.ac.cn/news_dynamic/detail/5080.html)]
- [2025.08.09] 国家超算天津中心联合天津中医药大学等发布**天河·灵枢**2.0，由针灸专科扩展至20余科；同步启动中医药智能模型评价体系 [[链接](http://tj.people.com.cn/n2/2025/0809/c375366-41317410.html)]
- [2025.08.06] 湖北日报报道，2025年8月6日湖北中医药大学、湖北时珍实验室与传神语联签约，以传神·素问中医大模型开展产学研用合作。 [[链接](https://news.hubeidaily.net/mobile/c_4393128.html)]
- [2025.08.01] **固生堂**正式发布十大“国医AI分身”，基于国医大师及名中医临床经验构建。页面写专家模拟一致性达86%以上，不是辨证准确率 [[链接](http://sz.people.com.cn/n2/2025/0801/c202846-41310443.html)]
- [2025.07] 中国中医科学院广安门医院与多家医联体单位成立**广医·岐智大模型智能体联盟**，推进跨机构智能诊疗能力辐射 [[链接](https://www.gamyy.cn/gzb/news/big/112751.html)]
- [2025.06.19] **中医横琴**垂类大模型正式发布 [[链接](https://www.stdaily.com/web/gdxw/2025-06/20/content_357526.html)]
- [2025.06.18] 国家数据局收录成都中医药大学案例：用大模型对996册中医古籍做自动分词和实体识别，并基于ChatGLM-6B关联中医术语、构建穴位-脏腑等知识图谱。 [[链接](https://www.nda.gov.cn/sjj/ywpd/szkjyjcss/0618/20250618095629525611799_pc.html)]
- [2025.06.06] 南京中医药大学人工智能与信息技术学院页面称，2025年6月6日发布灵山中医大模型（小杏仁）和素山中药大模型（素山智思体），分别服务中医临床教学科研和中药学教学科研。 [[链接](https://xxjs.njucm.edu.cn/2025/0529/c445a156198/pagem.htm)]
- [2025.05.17] 四川在线5月17日报道，成都体育学院联合中科视语发布中医运动医学**寰枢**大模型与智能体，定位竞技体育、大众健康和科教场景，可生成运动处方和节气养生方案。这是2025年的发布报道，本页未核验权重或对外接口是否公开。 [[链接](https://sichuan.scol.com.cn/ggxw/202505/82968100.html)]
- [2025.05.10] 北京中医药大学官网称，2025年5月10日发布薪火中国药智思体1.0，依托讯飞星火与DeepSeek，参数超700亿，面向助学、助教、助研、助管和国际合作。 [[链接](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)]
- [2025.05.10] 中国中医科学院发布中医药大模型评测标准 [[链接](https://www.news.cn/politics/20250510/5e6a0b4978b44b69b67dbfb7282fd220/c.html)]
- [2025.04.11] 凤凰网报道，2025年4月11日华为云生态大会上，九为健康发布基于盘古大模型的九为神农中医大模型智能体，覆盖药物研发、复方优化和辅助诊疗。 [[链接](https://biz.ifeng.com/c/8iTNRXVw44k)]
- [2025.04] 传神语联发布**任度·素问**中医大模型，基于全自研混合熵(moH)技术架构，支持智能问诊、辨证分析、方剂推荐 [[链接](https://www.transn.com/about_us/consult/article/1924766101036437505)]
- [2025.03.28] 中国中医科学院广安门医院28日正式发布**广医·岐智**中医大模型，成为国内首家本地化部署”算力+模型+应用”一体化服务的中医医院 [[链接](https://www.xinhuanet.com/tech/20250328/8b1685ad8c6f48c9bdc2add1658edac3/c.html)]
- [2025.03.20] 国务院办公厅印发《关于提升中药质量促进中医药产业高质量发展的意见》（国办发〔2025〕11号，成文2025年3月15日，中国政府网国务院文件栏目发布日期2025年3月20日）。意见经国务院同意，从中药资源保护利用、中药材产业发展、产业转型升级、药品价值评估和配备使用、科技创新、质量监管、开放发展和综合保障等方面提出措施。产业升级部分提出推进中药工业数字化智能化发展，运用数智技术、绿色技术赋能全产业链，建设数字化车间和智能工厂；临床价值评估部分提出利用循证医学等手段，开发中医药临床疗效评价大模型，促进人用经验向临床证据转化；并支持特色优势医疗机构中药制剂依法调剂使用，鼓励建设基层共享中药房。本次打开了中国政府网官方全文页。这是国务院办公厅产业质量政策，不是单项产品发布。目录此前仅有福建省落实该意见的若干措施，未收本文件本身。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202503/content_7014717.htm)]
- [2025.03.13] 新华网报道，2025年3月13日南京中医药大学黄煌团队与杭州脉景健康发布黄煌经方AI辅助诊疗系统，用大语言模型与知识图谱把“方人相应”做成可计算诊疗流程。 [[链接](http://www.js.xinhuanet.com/20250314/aa816bb98d1041afa0fa7bca45583d1b/c.html)]
- [2025.03] 云诊科技官网称，公司基于自研舌诊多模态模型TongueLMM和DeepSeek-R1发布云诊华医大模型，用于辨证论治、体质辨识和诊疗报告生成。 [[链接](https://www.ai-tongue.com/pages/news/2025/04/9a6f1920-4819-406e-8d1f-6ba0b838a7f8.html)]
- [2025.01.08] 2025年1月8日，北京科技大学联合河南中医药大学发布张仲景中医药大模型1.0，功能包括智能辨证、证素推荐、经方应用和方药分析。 [[链接](https://news.ustb.edu.cn/info/1087/67760.htm)]

</details>

<details>
<summary>2024 · 5</summary>

- [2024.12] 招联消费金融联合中山大学、广州中医药大学深圳医院发布中医垂直大模型**仲思**，落地深圳多家社康中心智能问诊 [[链接](https://finance.sina.com.cn/jjxw/2024-12-16/doc-inczrzsp5791684.shtml)]
- [2024.11] 华东师范大学、上海中医药大学、华东理工大学、海军军医大学、临港实验室和华润江中一起做了**数智岐黄**。1.0 在 2024 年 1 月 19 日发布。2024 年 11 月 25 日，他们在上海一场论坛上介绍了 2.0。 [[链接](https://pharm.ecnu.edu.cn/08/27/c43775a657447/page.htm)]
- [2024.09] 中科闻歌发布**大医金匮**中医大模型及中医智能健康管理平台，基于1500余本中医典籍及海量临床医案训练 [[链接](https://36kr.com/newsflashes/2946967562099592)]
- [2024.07.19] 两部门印发国中医药综发〔2024〕6号意见，推动中医药数字化转型，提出加强数据要素开发利用、打造中医药大模型和智慧服务应用。文件成文日期为2024年7月19日。 [[链接](http://www.natcm.gov.cn/bangongshi/zhengcewenjian/2024-08-14/34672.html)]
- [2024.05.10] 天士力与华为云联合发布**数智本草**大模型，基于盘古语言与药物分子模型。 [[链接](https://www.taslypharma.com/tsl/40931.jhtml)]

</details>

<details>
<summary>2023 · 1</summary>

- [2023.07.29] 南京大经中医发布**岐黄问道·大模型**，基于千万级知识图谱与临床数据，面向医疗机构开放内测 [[链接](http://js.news.cn/20230729/fa034db71a00487b819a4ad95b44673e/c.html)]

</details>


</details>

## 综述

<details>
<summary>95 篇，按年收着</summary>

<details>
<summary>2026 · 47</summary>

- [*Frontiers in Pharmacology*] **Deng et al. 2026: 人工智能解码中药复方抗癌机制的进展、挑战与展望** 赣州市人民医院邓永康、娄宗泽、李国政、黄苗、吴桂华在 Frontiers in Pharmacology 发表叙述性综述，系统整理人工智能用于解码中药复方抗癌机制的近期工作，重点覆盖多味复方及其组合机制，包括机器学习筛选、深度学习活性预测、文献挖掘、网络药理学、分子对接与虚拟筛选，以及多组学整合，并讨论数据不标准、模型可解释性不足、外部验证不够以及中医理论与生物医学计算框架衔接困难等瓶颈。页面标注日期为2026年8月19日与2026年11月4日。本次打开了期刊官方全文页。这是综述，不是新模型发布。 [Ganzhou People's Hospital] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2026.1972299/full)] [[DOI](https://doi.org/10.3389/fphar.2026.1972299)]
- [*Frontiers in Pharmacology*] **Huang 等：以代谢综合征为案例评估人工智能用于中医经典名方研发的技术成熟度** Huang、Jiang、Hu、Ye、Liu 等以代谢综合征为案例，回顾知识图谱、大语言模型和高通量验证三条技术线在中医经典名方精准研发中的就绪程度。作者引用《中医方剂大辞典》第二版约 99,584 个方名条目，并称 2013–2024 年国家药监局年均批准中药新药不足 10 个（合计 77 个）。文中评估知识图谱约处在技术成熟度等级（TRL）3–6，大语言模型约在 TRL 1–5，并指出三条技术线并不均衡。这是技术就绪度叙事综述，不是新药获批报告或疗效试验。本次打开了期刊全文页。 [中药经典名方现代化国家重点实验室，南昌大学第二附属医院江西省分子医学重点实验室，江西省科技基础条件平台中心江西省计算中心，江西中医药大学附属医院，中山大学深圳校区生物医学工程学院广东省传感技术与生物医学仪器重点实验室] [[DOI](https://doi.org/10.3389/fphar.2026.1970742)] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2026.1970742/full)]
- [*Frontiers in Artificial Intelligence and Applications*] **Hu Ziquan：中医药院校学科群建设中的人工智能应用定量系统综述（2023–2025）** Hu Ziquan 在 IOS Press 丛书 Frontiers in Artificial Intelligence and Applications 第 433 卷《Digitalization and Management Innovation V》发表定量系统综述（第 730–743 页），纳入 2023–2025 年 372 篇同行评议文献（国际 98、国内 274），并用作者自建的 TI、RDI、IDI、CKII 等指数描述研究主题、区域差异与技术瓶颈。文中给出五类主题的 TI 值，并报告模型可解释性总体偏低（平均 IDI=0.72）、古典中医知识融入不足（平均 CKII=0.20）等作者计算结果。页面可见摘要，未见作者单位。这是机构与学科发展导向的定量综述，不是临床试验。本次打开了 IOS Press 电子书官方页面。 [[DOI](https://doi.org/10.3233/FAIA261138)] [[论文](https://ebooks.iospress.nl/doi/10.3233/FAIA261138)]
- [*Guidelines and Standards of Chinese Medicine*] **Liu Changning、Zhang Xiaoduo、Shang Hongcai：数智技术驱动的循证中医药研究系统整合** Liu Changning、Zhang Xiaoduo、Shang Hongcai 通讯在《Guidelines and Standards of Chinese Medicine》2026 年 10 月 26 日优先发表综述，讨论循证中医药研究体系在方法与中医整体观不完全兼容、辨证主观性和疗效评价指标共识不足等问题，并综述大数据、人工智能和“互联网+”等数智技术在证据库建设、规范化临床研究设计和中药质量保障中的可能路径。这是标准与方法学综述，不是已部署系统的效果评价。本次打开了 Ovid 期刊官方页面，可见摘要与作者单位。 [北京中医药大学东直门医院教育部中医内科学重点实验室，广州中医药大学深圳市宝安中医院心内科，北京中医药大学东方医院] [[DOI](https://doi.org/10.1097/gscm.0000000000000131)] [[论文](https://www.ovid.com/jnls/gscm/fulltext/10.1097/gscm.0000000000000131~systematic-integration-of-evidence-based-traditional-chinese)]
- [*Frontiers in Neurology*] **Huang 等：舌诊用于中风中医辨证的诊断准确性系统综述、荟萃分析与人工智能模型叙事综合** Huang、Yin、Shao、Jiang、Wang、Xu 按诊断试验准确性方法检索至 2026 年 2 月 23 日，纳入中国大陆 10 项研究、3,437 名受试者（人工舌诊 6 项 2,191 人，人工智能辅助 4 项 1,246 人），并在 PROSPERO 注册 CRD420261288502。作者明确警告证据确定性很低、金标准独立性得不到保证，因此把结果视为与既有证候分类流程的探索性一致，而不是已经临床验证的诊断准确性。人工智能部分按 SWiM 做叙事综合。本次打开了期刊全文页。 [安徽中医药大学针灸推拿学院，安徽中医药大学医药信息工程学院，安徽中医药大学第二附属医院，安徽中医药大学第一附属医院，皖北卫生职业学院临床医学系，安徽中医药大学第一临床医学院] [[DOI](https://doi.org/10.3389/fneur.2026.1874937)] [[论文](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2026.1874937/full)]
- [*Frontiers in Physiology*] **Li 等：2015–2026 年中医舌诊人工智能研究的文献计量综述** Li、Yang、Lin、Wang、Yan、Zheng、Xiang、Tang 对 2015 年 1 月至 2026 年 8 月 Web of Science 核心合集与 CNKI 中的中医舌诊人工智能文献做文献计量比较，纳入 482 篇（WoSCC 295、CNKI 187），并用 CiteSpace、VOSviewer 分析合作网络、关键词与突现主题。作者强调两个库需分开分析。这是研究格局综述，不是诊断准确性的临床验证。本次打开了期刊全文页。 [广州市干部和人才健康管理中心中医科，长沙医学院护理学院，中信湘雅生殖与遗传专科医院影像科 / 湖南省生殖与遗传临床研究中心] [[DOI](https://doi.org/10.3389/fphys.2026.1895902)] [[论文](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2026.1895902/full)]
- [*Frontiers in Medicine*] **Wang 等：人工智能舌象分析用于胃癌、癌前病变及相关胃肠疾病无创筛查的系统综述** Wang、Li、Zhang、Shao、Gao、Zhang 按 PRISMA 2020 检索至 2026 年 6 月 10 日，纳入 2018–2025 年 9 项用机器学习或深度学习分析数字舌象、并报告定量指标的研究，覆盖胃癌、胃黏膜癌前病变或高风险筛查及相关胃肠疾病。作者报告内部验证 AUC 约 0.61–0.99，但仅 3 项有外部验证且普遍出现性能下降，校准评估少见。结论把该方法定位为有前景、仍处早期的胃镜前辅助分层工具，而不是胃镜替代。PROSPERO 注册号 CRD420261444857。本次打开了期刊全文页。 [山东中医药大学第一临床医学院，山东中医药大学附属医院神经内二科] [[DOI](https://doi.org/10.3389/fmed.2026.1931256)] [[论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1931256/full)]
- [*Biomedical and Environmental Sciences*] **Jia 等：中西医结合视角下心血管疾病临床决策支持系统的双轨并行与融合创新综述** Jia、Zhang、Tong 等，Ma、Li、Zhang Huamin 通讯，在《生物医学与环境科学》2026 年 39 卷 9 期第 1115–1130 页综述心血管疾病临床决策支持系统，并专节讨论中医临床决策支持系统（TCM-CDSS）借助“理法方药”、名医经验和知识图谱，形成从辨证到推荐方药的闭环。文中称高血压相关研究已报告处方和血压方面的改善，但对主要心血管事件和死亡率的影响仍需进一步评价。这是综述，不是新系统的前瞻性临床试验。本次打开了 besjournal.com 官方论文页。官网可见收稿日期 2026-03-01、接受日期 2026-08-17、在线日期 2026-09-20。 [中国中医科学院中医基础理论研究所，中国中医科学院中医药信息研究所，中国中医科学院中医临床基础医学研究所，中国中医科学院中医药数据中心，北京中医药大学中医学院，中国中医科学院中药研究所] [[DOI](https://doi.org/10.3967/bes2026.094)] [[论文](https://www.besjournal.com/en/article/doi/10.3967/bes2026.094)]
- [*集成技术*] **贺宇翔等 2026：人工智能驱动的中医药现代化：从经验范式到数据智能范式的转变** 深圳理工大学生物医学工程学院贺宇翔、唐若凝、尤志峰、张鹏，药学院冯志炜，医疗器械产业技术研究院李健，与中国科学院深圳先进技术研究院成文翔、柯丽青等在《集成技术》发表综述。张鹏另有山东中科先进技术有限公司署名。文章以“从经验范式到数据智能范式的转变”为主线，围绕中药物质基础解析、复方配伍优化、制药工程与产业转型、知识工程与大模型应用四个方向，讨论人工智能如何通过数据建模、跨模态融合与系统推理推动中医药研究走向数据驱动、证据约束和人机协同；同时指出各方向成熟度不均衡，以及可解释性、知识标准化和伦理治理方面的挑战。期刊元数据标注刊于2026年第15卷第5期第83–101页，发表日期2026-09-16，在线日期2026-06-15，DOI为10.12146/j.issn.2095-3135.20260517001。本次打开了期刊官方论文页，并核到可公开获取的官方PDF（许可标注为CC BY 3.0）。这是综述，不是新模型发布。 [深圳理工大学，中国科学院深圳先进技术研究院，山东中科先进技术有限公司] [[论文](https://jcjs.siat.ac.cn/article/doi/10.12146/j.issn.2095-3135.20260517001)] [[PDF](https://jcjs.siat.ac.cn/cn/article/pdf/preview/10.12146/j.issn.2095-3135.20260517001.pdf)] [[DOI](https://doi.org/10.12146/j.issn.2095-3135.20260517001)]
- [*兰州大学学报(医学版)*] **从大语言模型到智能体（兰州大学学报医学版综述）** 以「大模型→智能体」演进为主线的中医临床辅助诊疗中文系统综述，梳理研究进展、关键问题与方向（兰州大学学报(医学版) 2026;52(4):49-57） [[DOI](https://doi.org/10.13885/j.issn.2097-681X.T20260032)]
- **Agentic and Knowledge-Grounded LLMs in TCM（预注册）** 2026 年 7 月在 OSF 登记的综述计划，准备从证据图谱、文本挖掘和能不能用到临床上，看中医里的智能体和带知识的大模型。综述还在做。 [[预注册](https://doi.org/10.17605/osf.io/kq8jx)]
- [*International Journal of Pattern Recognition and Artificial Intelligence*] **中医大模型关键技术综述（IJPRAI）** 系统综述中医大模型知识组织、辅助诊断与临床决策支持关键技术（World Scientific IJPRAI正式发表） [Guangdong Provincial Hospital of Traditional Chinese Medicine，Guangdong University Of Finances and Economics，Guangdong University of Finance] [[DOI](https://doi.org/10.1142/s0218001426590263)]
- [*Journal of Traditional Chinese Medical Sciences*] **AI驱动中医诊断智能化综述（JTCMS）** 综述多模态融合与大模型在中医四诊智能化中的应用、挑战与展望（JTCMS正式发表） [暨南大学，北京中医药大学] [[DOI](https://doi.org/10.1016/j.jtcms.2026.05.002)]
- [*Frontiers in Medicine*] **Nie et al. 2026: Artificial intelligence guided acupuncture decision making and treatment: a review of research** 长春中医药大学针灸推拿学院聂茹、邓凯月、何静、贾佳琳、王鸿烨、袁淑婷、李铁在 Frontiers in Medicine 发表综述，按临床流程回顾人工智能在针灸中的应用，覆盖穴位选择标准化、定位辅助、实时安全监测和个性化疗效预测四方面，并讨论现有工作与后续智能针灸系统发展建议。作者指出已有中医人工智能综述多为宽泛概览，较少直接对照针灸临床工作流。期刊页标注文章类型为 Review，在线 2026年4月13日、发表 2026年4月27日，刊于第13卷。本次打开了 Frontiers 官方全文页并下载了官方 PDF。这是综述，不是新模型发布。 [Changchun University of Chinese Medicine] [[论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1752082/full)] [[PDF](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1752082/pdf)] [[DOI](https://doi.org/10.3389/fmed.2026.1752082)]
- [*Frontiers in Neurology*] **Chan et al. 2026: Integrating machine learning into acupuncture research: a scoping review** 中国医药大学针灸研究所与附属安南医院 Chan Wancy、Huang Guan-Jun、Huang Chien-Chen、Chen Yi-Hung 在 Frontiers in Neurology 发表范围综述（期刊页标注文章类型为 Systematic Review），梳理 2011–2024 年 PubMed 中针灸与机器学习交叉文献。作者纳入 36 篇，称 2019 年后明显增加、多数来自中国；17 篇关注疗效预测且以疼痛相关病种为主，其余涉及手法识别、处方推荐、穴位敏化与特异性、使用频次预测、经脉传导以及针刺机器人定位等。疗效预测研究中支持向量机最常用，11 项中有 7 项将磁共振成像作为特征，并以治疗应答分类为标签。作者认为预测表现整体积极，但样本量小、方法异质、数据类型不一和缺乏标准化数据集限制了可泛化性。期刊页标注在线 2025年12月22日、发表 2026年1月14日，刊于第16卷，文章号 1689061。本次打开了 Frontiers 官方全文页并下载了官方 PDF。这是综述，不是新模型发布。 [China Medical University，An Nan Hospital, China Medical University] [[论文](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2025.1689061/full)] [[PDF](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2025.1689061/pdf)] [[DOI](https://doi.org/10.3389/fneur.2025.1689061)]
- [*上海中医药杂志*] **人工智能驱动下的中医智能诊疗研究进展与挑战** 以中医辨治六步程式为骨架的全链路（四诊-辨证-处方-疗效预测）中文综述，对照监督/无监督/强化/深度学习范式（上海中医药杂志 2026;60(1)） [[DOI](https://doi.org/10.16305/j.1007-1334.2026.z20250609004)]
- [*Chinese Science Bulletin*] **面向临床的中西药联用安全性数智评价** 中西药联用的不良反应隐匿、机制复杂，且个体差异大。文章提出一条从智能预测、风险识别、机制验证到数智决策的评价路径，覆盖用药前预警和用药中识别。 [[DOI](https://doi.org/10.1360/csb-2026-0084)]
- [*Communications in Computer and Information Science (Springer)*] **多模态大模型驱动舌脉面诊智能化综述（Springer 书章）** 唯一以「多模态LLM×四诊感知」为题的综述性文本，覆盖舌/脉/面诊智能化（Springer CCIS 会议书章，评审强度低于期刊） [Chinese Academy of Social Sciences，Institute of Ethnology and Anthropology，University of Chinese Academy of Social Sciences] [[DOI](https://doi.org/10.1007/978-981-95-7299-1_15)]
- [*中华中医药学刊*] **人工智能赋能中医数字化诊断：现状与挑战（中华中医药学刊）** 短文，写人工智能在中医数字化诊断里能做什么，也写了数据质量、说得清说不清、以及和中医理论怎么接上。刊在《中华中医药学刊》。 [[DOI](https://doi.org/10.13193/j.issn.1673-7717.2026.01.004)]
- [*Chinese Medicine*] **中医为何需要可解释人工智能** 认为中医人工智能的障碍不只是预测分数，而是数据驱动模型和证候、病机这类理论推理对不上，所以需要可解释性。 [[DOI](https://doi.org/10.1186/s13020-026-01455-4)]
- [*Healthcare*] **东亚传统医学如何进入国际卫生信息标准** 范围综述：检索 2016 年 1 月至 2026 年 3 月的英文文献，看韩医、中医和汉方概念怎样映射进主流卫生信息标准。 [[DOI](https://doi.org/10.3390/healthcare14183011)]
- [*Integrative Medicine Research*] **Yao et al. 2026: LLM 与循证中医整合（Scoping Review）** PRISMA scoping review，纳入 12 篇（2022-11 至 2026-01），覆盖 LLM 循证中医的证据生成、合成与转化 [University of Geneva，中国医学科学院，Gansu University of Traditional Chinese Medicine，Lanzhou University] [[DOI](https://doi.org/10.1016/j.imr.2026.101349)]
- [*Journal of Pharmaceutical Analysis*] **Xu et al. 2026: 基于 LLM 的中医智能问答系统综述** 中医智能问答系统谱系综述（KG-QA→LLM-QA、RAG） [天津大学，Tianjin haihe hospital] [[DOI](https://doi.org/10.1016/j.jpha.2025.101406)]
- [*Engineering*] **XiangShu Omics: A Framework Based on the Spatio–Temporal Field Rhythms of Human Life and Systems Intelligence Methodology** 这篇综述首次系统提出象数组学，并写道其大模型按理、法、方、药的经典治疗逻辑整合大语言模型，例如数智岐黄。 [[DOI](https://doi.org/10.1016/j.eng.2026.02.018)]
- [*Artificial Intelligence Review*] **Wu et al. 2026: AI 在中药材中的应用综述** 中药学×AI 全栈 survey（成分、靶点、质控，含 LLM 一节） [Northeastern University，First Hospital of China Medical University，China Medical University，Liaoning University] [[DOI](https://doi.org/10.1007/s10462-026-11513-w)]
- [*Medical Review*] **Wang et al. 2026: 重思中医大模型评测** 指出中医大模型评测仍缺少质量底线：未筛选古籍和网页语料可能含过时或禁用建议，单病例基准也不足以代表临床 [北京中医药大学] [[DOI](https://doi.org/10.1515/mr-2026-0006)]
- [*Chinese Medicine*] **Wang et al. 2026: 人工智能在中医药研发中的发展与应用综述** 2026年1月8日发表于 Chinese Medicine 的综述，梳理人工智能在中药研发设计、制药过程与市场准入等环节的应用与局限，并讨论与新兴技术结合的方向。 [[DOI](https://doi.org/10.1186/s13020-025-01288-7)] [[论文](https://link.springer.com/article/10.1186/s13020-025-01288-7)]
- [*Chinese Herbal Medicines*] **Sun et al. 2026: 生成模型在中医药中的进展与应用** 综述生成模型在中医药中的进展与应用 [[DOI](https://doi.org/10.1016/j.chmed.2026.08.013)]
- [*Information*] **Lu et al. 2026: 深度学习中医诊断方法学质量审计** 系统综述+验证缺口分析：DL 中医疾病诊断研究的方法学质量与临床转化 [香港中文大学] [[DOI](https://doi.org/10.3390/info17060554)]
- [*ACL 2026*] **LLM-Based Multi-Agent Systems for Clinical Workflows（ACL 2026，邻近）** 工作流级多智能体综述+四层评测栈（safety/process/outcome/operations）；无TCM交集但过程评测主张方法学同构（邻近） [Sanford Health，University of Massachusetts Lowell，University of Massachusetts Amherst] [[DOI](https://doi.org/10.18653/v1/2026.acl-long.2123)]
- [*Chinese Medicine*] **Han et al. 2026: LLM 在中医中的调优与临床应用（Scoping Review）** PRISMA-ScR scoping review，纳入 27 篇（至 2025-05），聚焦 LoRA/CPT/RAG 调优配方与临床应用统计 [中国医学科学院，Jining Traditional Chinese Medicine Hospital，中国中医科学院，北京中医药大学] [[DOI](https://doi.org/10.1186/s13020-026-01346-8)]
- [*Chinese Medicine*] **Guo et al. 2026: AI 与多模态数据融合推动中医现代化** AI 全景综述（ML/DL/KG/NLP/LLM），LLM 为一节，附多尺度数据资源与平台编目 [Ningbo College of Health Sciences，Shenzhen Second People's Hospital，Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1186/s13020-025-01194-y)]
- [*Chinese Medicine and Culture*] **From Empirical Wisdom to Computational Intelligence: A Knowledge-Data Dual-Driven Paradigm for Modernizing Traditional Chinese Medicine** 该文提出知识与数据双驱动范式：用大规模知识图谱和中医专用大语言模型把隐性经验变成可计算结构，并把四诊数字化为多模态中医表型。 [[DOI](https://doi.org/10.1097/mc9.0000000000000198)]
- [*Science of Traditional Chinese Medicine*] **Dong et al. 2026: 中医处方推荐计算方法综述** 综述从临床数据学习处方规律的计算方法，覆盖智能处方推荐如何支持中医临床决策 [南京中医药大学，北京交通大学] [[DOI](https://doi.org/10.1097/st9.0000000000000110)]
- [*Journal of Integrative Medicine*] **Deep learning in TCM（J Integr Med）** 深度学习单技术线综述：医学影像、药材物质研究、数据挖掘等应用实例（J Integr Med 2026;24(4):471-480） [天津大学] [[DOI](https://doi.org/10.1016/j.joim.2026.03.001)]
- [*OSF Registries*] **Cong H et al. 中医古籍知识挖掘范围综述（OSF 预注册）** 2026 年 4 月 15 日在 OSF 登记的一份范围综述计划，准备梳理知识图谱、大模型和两者结合的框架怎样从中医古籍里整理知识。综述还在做。 [[DOI](https://doi.org/10.17605/osf.io/5z367)]
- [*Science of Traditional Chinese Medicine*] **Chen et al. 2026: LLM 在中医的下一步（叙述性综述）** 叙述性前瞻：多模态、Agent 与临床落地路线 [北京中医药大学] [[DOI](https://doi.org/10.1097/st9.0000000000000109)]
- [*OSF Registries*] **Cai R et al. 中医辨证分类范围综述（OSF 预注册）** 2026 年 4 月 3 日在 OSF 登记的一份范围综述计划，准备梳理大模型怎样做中医辨证、证素和辨证推理，并按 PRISMA-ScR 来写。综述还在做。 [[DOI](https://doi.org/10.17605/osf.io/2hyeq)]
- [*Intelligence-Based Medicine*] **Artificial intelligence: A catalyst for the modernization of traditional Chinese medicine** 这篇范围综述检索PubMed、Web of Science和中国知网截至2025年的文献，并写道深度学习和大语言模型在舌象分析与辨证上表现有前景，部分研究接近专家水平。 [[DOI](https://doi.org/10.1016/j.ibmed.2026.100415)]
- [*Journal of Advanced Research*] **AI-driven multi-scale target analysis of traditional Chinese medicine: From the pharmacological effects of single compounds to the synergistic mechanisms of formulae** 这篇中药多尺度靶点分析综述把研发面向中医的专用大语言模型列为未来方向，用来解码中药的药理逻辑。 [[DOI](https://doi.org/10.1016/j.jare.2026.03.050)]
- [*Pharmacological Research - Modern Chinese Medicine*] **AI in TCM: multimodal data to pharmacology and clinical decision（PRMCM 综述）** 一篇英文综述，从多模态数据、药理研究写到临床决策。2026 年发表在 Pharmacological Research - Modern Chinese Medicine。 [Saveetha University] [[DOI](https://doi.org/10.1016/j.prmcm.2026.100842)]
- [*Research*] **AI in TCM: Unraveling Herbal Medicine's Mechanisms（Research）** 主张AI从相关分析范式走向重建证候辨证与方剂配伍生物逻辑的药材机制中心宽口径综述（Research 2026;9:1224） [Zhejiang Chinese Medical University] [[DOI](https://doi.org/10.34133/research.1224)]
- [*Journal of Integrative Medicine*] **AI empowers the innovation of TCM（J Integr Med 评论）** 单作者评论性综述：古籍挖掘、诊疗标准化、药物研发周期三痛点×AI（J Integr Med 2026） [上海中医药大学] [[DOI](https://doi.org/10.1016/j.joim.2026.05.004)]
- [*Chinese Medicine and Culture*] **AI and Big Data in TCM Standardization and Internationalization（Chin Med Cult）** 谈人工智能和大数据怎样帮助中医做标准化、走到国际上去。刊在 Chinese Medicine and Culture 2026 年第 9 卷第 3 期。 [南洋理工大学] [[DOI](https://doi.org/10.1097/mc9.0000000000000203)]
- [*Science of Traditional Chinese Medicine*] **2026: 面向中医药证据知情决策的数字智能循证** 讨论如何用数字智能循证方法，把辨证论治推进到证据知情的中医药决策 [兰州大学，University of Geneva] [[DOI](https://doi.org/10.1097/st9.0000000000000105)]
- [*Science of Traditional Chinese Medicine*] **2026: 数字化与智能化时代的中医药机遇与挑战** 从专家系统到深度学习和大语言模型，讨论数字化、智能化给中医药带来的机遇与挑战 [中国中医科学院] [[DOI](https://doi.org/10.1097/st9.0000000000000102)]
- [*Digital Chinese Medicine*] **2026: 中医智能诊断的跨学科融合与发展趋势** 讨论中医智能诊断的跨学科融合与发展趋势 [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.001)]

</details>

<details>
<summary>2025 · 29</summary>

- [*Frontiers in Medicine*] **Hou et al. 2025: Artificial intelligence in acupuncture: bridging traditional knowledge and precision integrative medicine** 辽宁中医药大学针灸推拿学院侯国梁、董宝强、于本祥、戴建宇、林星星、程泽忠在 Frontiers in Medicine 发表综述，整理人工智能用于针灸疗效预测及相关技术的进展，覆盖深度学习、元分析建模、自然语言处理、计算机视觉和神经影像分析等，并举卷积神经网络用于舌象分类与证型识别、基于 Transformer 的模型从经典文献中自动抽取临床知识等例子。作者讨论数据有限且异质、标注不一致和临床验证不足，并建议建设联邦多模态数据平台、可解释框架和开放科学实践。期刊页标注文章类型为 Review，在线 2025年7月15日、发表 2025年7月31日，刊于第12卷。本次打开了 Frontiers 官方全文页并下载了官方 PDF。这是综述，不是新模型发布。 [Liaoning University of Traditional Chinese Medicine] [[论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1633416/full)] [[PDF](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1633416/pdf)] [[DOI](https://doi.org/10.3389/fmed.2025.1633416)]
- [*协和医学杂志*] **陈子佳 et al. 2025: 大语言模型在中医药领域的应用、挑战与前景** 综述大语言模型与中医四诊合参、辨证诊疗和复方研究的结合，并讨论价值风险、可解释性、技术短板与政策准入等挑战。 [中国中医科学院] [[DOI](https://doi.org/10.12290/xhyxzz.2024-0315)] [[论文](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2024-0315)]
- [*Pharmaceuticals*] **评估药物–草药相互作用的人工智能工具** 综述用人工智能模型评估药物和草药相互作用的工具。 [[DOI](https://doi.org/10.3390/ph18030282)]
- [*iScience*] **计算机辅助穴位定位系统综述** 系统综述用传统算法和深度学习在不同解剖区域做穴位定位的研究，并讨论效果和限制。 [[DOI](https://doi.org/10.1016/j.isci.2025.113708)]
- [*Chinese Medicine*] **肿瘤治疗中的草药–化学药相互作用** 综述肿瘤患者联用草药和抗癌药时的相互作用，包括药效、药代机制和风险预测。 [[DOI](https://doi.org/10.1186/s13020-025-01156-4)]
- [*Chinese Medicine*] **深度学习穴位定位综述** 按身体部位、网络结构、定位策略和图像模态，综述深度学习穴位定位的数据集、指标和适用场景。 [[DOI](https://doi.org/10.1186/s13020-025-01173-3)]
- [*中华中医药学刊*] **杨乐乐 et al. 2025: 大语言模型在中医药领域的应用展望思考** 梳理医学大语言模型发展脉络，展望其在中医药研究、知识挖掘与辅助诊疗中的应用，并讨论风险、对策与发展方向。 [中国中医科学院中医药信息研究所，Leipzig University] [[DOI](https://doi.org/10.13193/j.issn.1673-7717.2025.02.004)]
- [*中华中医药学刊*] **叶桦 et al. 2025: 大语言模型赋能中医药传承：前沿进展与应用展望** 2025年11月11日网络首发的中文综述，系统梳理大语言模型在中医药数据挖掘、临床辅助决策与文化传承中的研究进展、挑战与展望。期刊页未提供DOI。 [成都中医药大学智能医学学院，成都中医药大学基础医学院] [[论文](https://zyhs.cbpt.cnki.net/portal/journal/portal/client/paper/3e19461f3fb08c22b2659ea83eb41d5a)]
- [*Chinese Medicine*] **古籍知识图谱×多智能体融合综述（Chin Med）** 古籍KG构建（术语统一、数据标准化）挑战-展望型综述，首次把multi-agent写入中医古籍议题（Chin Med 2025;20:168） [北京大学] [[DOI](https://doi.org/10.1186/s13020-025-01226-7)]
- [*智能系统学报*] **医疗领域的大型语言模型综述（智能系统学报，邻近）** 中文医疗LLM通用综述（训练流程/策略/场景/挑战），与中医LLM综述圈属母子集关系（邻近） [[DOI](https://doi.org/10.11992/tis.202405003)]
- [*智能系统学报*] **医学大语言模型的研发与应用系统综述（智能系统学报，邻近）** 系统综述129个医学专用LLM（截至2024-06）+4类临床应用研究；系统检索协议方法学可比（邻近） [[DOI](https://doi.org/10.11992/tis.202410020)]
- [*上海中医药杂志*] **刘嘉艺 et al. 2025: 生成式人工智能在中医药标准化研究中的应用前景与挑战** 综述生成式人工智能在中医药健康服务、质量提升、信息管理与智能诊疗等标准化相关场景中的应用现状、前景与挑战。 [兰州大学，中国中医科学院中医临床基础医学研究所，广东省中医院] [[DOI](https://doi.org/10.16305/j.1007-1334.2025.z20241121005)] [[论文](https://shzyyzz.shzyyzz.com/zh/article/doi/10.16305/j.1007-1334.2025.z20241121005/)]
- [*中华中医药学刊*] **人工智能实现中医四诊的发展现状、问题及解决路径（中华中医药学刊）** 从望、闻、问、切看人工智能做中医四诊走到哪。望诊用摄像头拍面、舌、舌下、唇和眼睛，结合分割和颜色模型做量化；闻诊采集异常声音和气味，用神经网络和电子鼻做分析。刊在《中华中医药学刊》2025年第43卷第11期。 [[论文](https://www.sinomed.ac.cn/article.do?ui=2026106036)]
- [*AI Medicine*] **Zhang et al. 2025: 中医 LLM 短综述与展望** 短 survey+展望，TCM LLM 模型与任务速览 [Northeastern University] [[DOI](https://doi.org/10.53941/aim.2025.100003)]
- [*Journal of Evidence-Based Medicine*] **Yip et al. 2025: 中西医结合 LLM 进展与挑战** 综述：LLM 在整合医学（中西医结合）中的进展、挑战与机遇 [Hong Kong Baptist University，Guangdong-Hongkong-Macau Joint Laboratory of Collaborative Innovation for Environmental Quality] [[DOI](https://doi.org/10.1111/jebm.70031)]
- [*Acta Materia Medica*] **Yin et al. 2025: 数据挖掘、大模型与多模态融合的中医AI综述** 从数据挖掘、大语言模型和多模态融合三条线综述人工智能如何解析中药复方的多成分、多靶点机制 [浙江大学] [[DOI](https://doi.org/10.15212/amm-2025-0045)]
- [*American Journal of Chinese Medicine*] **Wang et al. 2025: AI 驱动中医诊断模型进展** 综述：AI 诊断模型（四诊客观化、辨证） [清华大学，南京大学] [[DOI](https://doi.org/10.1142/S0192415X25500259)]
- [*Journal of Pharmaceutical Analysis*] **The integration of machine learning into TCM（J Pharm Anal）** 机器学习×中医整合综述：诊断客观化与机制阐释两条线（J Pharm Anal 2025;15(8):101157） [Hangzhou Normal University] [[DOI](https://doi.org/10.1016/j.jpha.2024.101157)]
- [*American Journal of Chinese Medicine*] **Shataer et al. 2025: LLM 在中医应用（State-of-the-Art Review）** 叙述性综述，扫描 TCM LLM 应用场景（诊疗、教育、翻译、科研） [Centre for Intelligent Healthcare, Coventry University, Coventry CV1 5RW, UK] [[DOI](https://doi.org/10.1142/S0192415X25500375)]
- [*Journal of Evidence-Based Medicine*] **Ren et al. 2025: 中医大语言模型（Scoping Review）** Arksey–O'Malley scoping review，纳入 29 篇（至 2024-04），覆盖知识管理、辅助诊疗与考试准确率 [成都中医药大学，中国医学科学院，Institute of Health Data Science Lanzhou University Lanzhou China，Institute of Global Health University of Geneva Geneva Switzerland] [[DOI](https://doi.org/10.1111/jebm.12658)]
- [*Pharmacological Research*] **Meng et al. 2025: 大模型+虚拟细胞助力中医变革** 综述：大模型与虚拟细胞用于中风方药现代分析 [Northeastern University，Shenyang Medical College] [[DOI](https://doi.org/10.1016/j.phrs.2025.107953)]
- [*Science of Traditional Chinese Medicine*] **Liu et al. 2025: 网络药理学推动大模型用于中医药研究** 综述网络药理学如何把药物—靶点—疾病网络与大语言模型结合起来，解释中药复方的多靶点机制 [清华大学] [[DOI](https://doi.org/10.1097/st9.0000000000000073)]
- [*Healthcare*] **Intelligent Question-Answering Systems in Healthcare（Healthcare，邻近）** 2018-2025医疗QA综述+CiteSpace计量，明确含中医方剂开发应用场景（邻近综述，非TCM专用） [Beijing Information Science & Technology University] [[DOI](https://doi.org/10.3390/healthcare13182269)]
- [*Journal of Evidence-Based Medicine*] **Guo et al. 2025: GPT 能否加速中医智能诊疗（综述+实证）** 综述+实证分析，讨论 GPT 适配中医诊疗的挑战与幻觉问题 [Xiyuan Hospital China Academy of Chinese Medicinal Sciences Beijing China，北京大学] [[DOI](https://doi.org/10.1111/jebm.70004)]
- [*Asia-pacific Journal of Convergent Research Interchange*] **Domestic and International Research Trends in Artificial Intelligence Applications in Korean Medicine: An Analysis from 2019 to 2025** 作者系统回顾了2019至2025年23项韩医人工智能研究（国内10篇、国际13篇），并指出近期工作越来越多使用大语言模型和其他生成式人工智能。 [[DOI](https://doi.org/10.47116/apjcri.2025.11.02)]
- [*Acupuncture and Herbal Medicine*] **Chen et al. 2025: 中医大语言模型系统综述** 系统综述，纳入 10 篇（至 2024 年中），聚焦生成任务证据 [天津大学，现代中药海河实验室，Italian National Institute of Health, Rome, Italy] [[DOI](https://doi.org/10.1097/HM9.0000000000000143)]
- [*Current Medical Science*] **Artificial Intelligence in Traditional Chinese Medicine: Multimodal Fusion and Machine Learning for Enhanced Diagnosis and Treatment Efficacy** 综述人工智能在中医诊断和治疗中的多模态融合与机器学习。 [[DOI](https://doi.org/10.1007/s11596-025-00103-6)]
- [*MedComm – Future Medicine*] **Artificial Intelligence in Traditional Chinese Medicine: Bridging Ancient Practice and Future Innovation** 该综述按“构建—应用—挑战—展望”分析中医大模型，并指出Qibo和MedChatZH等系统已经出现，但此前综述缺少对共同特征的综合分析。 [[DOI](https://doi.org/10.1002/mef2.70042)]
- [*Current Medical Science*] **AI for Spleen-Stomach Disorders in TCM（Curr Med Sci）** 单病种（脾胃病）KG+智能诊疗综述：「症状-证候-疾病-方剂」框架的知识工程化（Curr Med Sci 2025;45(6):1348-1357） [Hubei University of Chinese Medicine，Hubei Provincial Hospital of Traditional Chinese Medicine，Hospital Conde S. Januário，Union Hospital] [[DOI](https://doi.org/10.1007/s11596-025-00128-x)]

</details>

<details>
<summary>2024 · 7</summary>

- [*Engineering*] **系统论框架下整合人工智能与中医药整体物质基础研究（框架综述）** 曾敬其、贾晓斌通讯。发表于 Engineering 2024 年 40 卷第 9 期的框架性综述，提出用系统功能解码模型（SFDM）把人工智能接到中医药整体物质基础研究，整理自上而下五个维度与自下而上的要素—结构—功能路径，并展望“组分-证候”端到端模型与口服制剂 IVIVC 机理模型。这不是系统评价，两种技术方案在本文中没有实现和定量评测。许可为 CC BY-NC-ND 4.0。中文正式本 25 页。 [中国药科大学中药学院，中国药科大学天然药物活性组分与药效国家重点实验室] [[DOI](https://doi.org/10.1016/j.eng.2024.04.009)] [[论文](https://www.engineering.org.cn/engi/CN/10.1016/j.eng.2024.04.009)]
- [*中草药*] **萧文科 et al. 2024: 中医药大语言模型的关键技术与构建策略** 专论梳理中医药大模型的数据存储与处理、RAG、MoE、RLHF、知识蒸馏及训练评测方法，并提出面向中医药数据特点的构建策略与应用场景。 [成都中医药大学] [[DOI](https://doi.org/10.7501/j.issn.0253-2670.2024.17.001)] [[论文](http://www.tiprpress.com/zcy/article/pdf/20241701)]
- [*计算机工程与应用*] **苏尤丽 et al. 2024: 人工智能在中医诊疗领域的研究综述** 中文综述：专家系统→机器学习→深度学习三阶段中医 AI 诊疗发展与挑战 [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2312-0400)]
- [*南京中医药大学学报*] **李欣桐 et al. 2024: 中医药领域大语言模型的研究进展与应用前景** 中文综述：中医药 LLM 研究过程、前沿技术（提示工程/RAG/RLHF）与应用前景 [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1393)]
- [*Computers in Biology and Medicine*] **Tian et al. 2024: 四诊机器学习综述** 望闻问切四诊的 ML 传感与模型综述 [Northeastern University，Ningbo University，辽宁中医药大学] [[DOI](https://doi.org/10.1016/j.compbiomed.2024.108074)]
- [*中国工程科学*] **Song et al. 2024: AI 辅助中医辨证关键问题与技术挑战** 战略研究综述：多模态数据融合、症状关联、证候量化与推理及中医药大模型关键问题 [Shanghai University of Engineering Science，Digital China Health (China)，Zhejiang Lab，中国医学科学院] [[DOI](https://doi.org/10.15302/J-SSCAE-2024.02.010)]
- [*Computer Materials & Continua*] **Qu et al. 2024: 中医知识图谱综述** 中医知识图谱的分析、构建、应用与展望 [中国医学科学院，Beijing Forestry University] [[DOI](https://doi.org/10.32604/cmc.2024.055671)]

</details>

<details>
<summary>2023 · 3</summary>

- [*Chinese Medicine*] **中医药与天然产物中的机器学习：现状与展望** Ma、Liu、Li 共同第一，Li 与 Wang 通讯。这是发表于 Chinese Medicine 的叙述性综述，回顾中医药与天然产物研究中的机器学习，介绍团队的冠心病证素模型，并提出把机器学习、中医理论和计算生物学结合起来的展望。不是系统评价，表中准确率来自被引文献。未见新代码或新数据。许可为 CC BY 4.0。 [中国中医科学院广安门医院，天津中医药大学] [[DOI](https://doi.org/10.1186/s13020-023-00741-9)] [[论文](https://cmjournal.biomedcentral.com/articles/10.1186/s13020-023-00741-9)]
- [*Annals of Translational Medicine*] **中医四诊人工智能研究现状与趋势的科学计量研究** Tian、Hongwu Wang 通讯等。发表于 Annals of Translational Medicine 2023 年 11 卷第 3 期的科学计量研究，用 Web of Science、VOSviewer 和 CiteSpace 分析中医四诊人工智能文献。正文写 2007–2022 年 136 篇有效研究，不是系统评价，也没有 PRISMA。许可为 CC BY-NC-ND 4.0。正式本 16 页，DOI 10.21037/atm-22-6431。与本站已有 surv-tian2024 不是同一篇。 [天津中医药大学健康科学与工程学院，华北理工大学中医学院，南京中医药大学研究生院，南京中医药大学附属医院高血压研究所] [[DOI](https://doi.org/10.21037/atm-22-6431)] [[论文](https://atm.amegroups.org/article/view/109099)]
- [*Current Opinion in Structural Biology*] **中药计算毒性研究小综述** 综述用计算方法研究中药毒性的工作。 [[DOI](https://doi.org/10.1016/j.sbi.2023.102588)]

</details>

<details>
<summary>2022 · 1</summary>

- [*Frontiers in Pharmacology*] **人工智能在补充替代医学中的应用：系统性范围综述** Chu、Youn 通讯等按 JBI 和 PRISMA-ScR 梳理人工智能在补充替代医学中的应用，检索三个英文库，终选 32 篇，主要涉及针灸、舌唇诊和草药。这是系统性范围综述，不是元分析。正文、流程图和表 1 的计数不完全一致。未见新代码或新数据。许可为 CC BY。 [仁川 Daecheong Public Health Subcenter，庆熙大学研究生院，圆光大学韩医学院，韩国韩医药振兴院，庆熙大学韩医学院预防医学科] [[DOI](https://doi.org/10.3389/fphar.2022.826044)] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.826044/full)]

</details>

<details>
<summary>2021 · 2</summary>

- [*Frontiers in Pharmacology*] **人工智能、深度学习与云计算用于中西医诊治类风湿关节炎** Wang、Hou 共同第一，Zhang 与 Wang 通讯。这是发表于 Frontiers in Pharmacology 的叙述性综述，讨论人工智能、深度学习和云计算在传统医学与西医诊治类风湿关节炎中的应用设想，并给出概念模型。不是系统评价，也不是已实现的诊疗系统。未见新代码或新数据。许可为 CC BY。 [成都中医药大学民族医药学院，成都中医药大学药学院，成都市第二人民医院，西南特色中药资源国家重点实验室，成都中医药大学中医药创新研究院] [[DOI](https://doi.org/10.3389/fphar.2021.765435)] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2021.765435/full)]
- [*Computers in Biology and Medicine*] **Zhang et al. 2021: 计算中医诊断文献综述** 计算化中医诊断的文献综述（症状采集、辨证建模与系统） [澳门大学] [[DOI](https://doi.org/10.1016/j.compbiomed.2021.104358)]

</details>

<details>
<summary>2020 · 1</summary>

- [*Artificial Intelligence in Medicine*] **Chu et al. 2020: 中医定量知识表示模型综述** 中医知识定量表示模型（本体、规则、统计）综述 [Xidian University，Xi'an Polytechnic University，Guangdong Polytechnic Normal University，CM Hospital] [[DOI](https://doi.org/10.1016/j.artmed.2020.101810)]

</details>

<details>
<summary>2019 · 1</summary>

- [*Engineering*] **中药安全性研究：方法、应用与展望** 综述中药不良反应为何难研究：成分复杂，药物和机体的相互作用也难事先判断，和化学药、生物药的毒性研究不是同一类问题。 [[DOI](https://doi.org/10.1016/j.eng.2018.11.019)]

</details>

<details>
<summary>2018 · 1</summary>

- [*Journal of Clinical and Translational Hepatology*] **中药肝损伤与药物性肝损伤的比较（叙述性综述）** Jing 与 Teschke 通讯。2018 年发表于 Journal of Clinical and Translational Hepatology 的叙述性综述，比较中药／草药性肝损伤与化学药物性肝损伤的流行病学、临床特征和 RUCAM 分级。不是系统评价，主要比较表转述既有队列。摘要与表 4、正文与表 6／图 2 存在文字和数字冲突。许可为 CC BY-NC 4.0。 [中国人民解放军医学院，解放军第302医院整合医学中心，哈瑙医院内科II消化与肝病科（歌德大学教学医院）] [[DOI](https://doi.org/10.14218/JCTH.2017.00033)] [[论文](https://www.xiahepublishing.com/ArticleFullText.aspx?sid=2&jid=1&id=10.14218%2fJCTH.2017.00033)]

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
<summary>73 件，按公开年收着</summary>

<details>
<summary>2026 · 33</summary>

- [*CN122531762A*] **基于生成式模拟医案构建的定制化中医处方推荐大模型** 用规则引擎穷举结构化中医特征，再由大语言模型写成模拟医案，并微调得到定制化处方推荐大模型（公开，未授权） [北京中医药大学] [[专利](https://patents.google.com/patent/CN122531762A/zh)]
- [*CN122529089A*] **基于大语言模型的中医对话生成方法及装置** 用长期记忆库与用户画像生成个性化中医对话（公开，未授权） [杭州旺柴科技] [[专利](https://patents.google.com/patent/CN122529089A/zh)]
- [*CN122508432A*] **一种面向中医药知识图谱的综合质量评估方法** 把小样本送入中医药微调大语言模型，做知识图谱质量预评估（公开，未授权） [湖北省标准化与质量研究院] [[专利](https://patents.google.com/patent/CN122508432A/zh)]
- [*CN122599028A*] **一种基于AI大模型的中医天地岁人四维辨证辅助诊疗系统** 结合多部位多压力脉象、时序节律编码与体质识别，生成中药和经络穴位推荐。2026年8月18日公开；原页显示Pending，仅为技术方案公开。 [Gaobele Biotech Guangzhou Co ltd] [[专利](https://patents.google.com/patent/CN122599028A/zh)]
- [*CN122436154A*] **张锡纯中医理法方药数字化传承与智能分析系统** 辨病辨证规则 + 三路检索 + LLM 融合，做张锡纯学派理法方药分析（公开，未授权） [广州知云草堂医疗科技] [[专利](https://eureka.patsnap.com/patent/CN122436154A)]
- [*CN122436116A*] **基于知识图谱与大语言模型的脾胃学派理法方药分析系统** 融合脾胃学派知识图谱、向量检索与大语言模型，完成选方验证、安全校验和处方生成（公开，未授权） [广州智韵草堂医学科技有限公司] [[专利](https://patents.google.com/patent/CN122436116A/zh)]
- [*CN122436251A*] **一种融合时空特征的针灸推理模型构建方法、系统及设备** 对齐四诊与病程的时空特征，检索历史针灸方案后，用微调大模型和思维链做针灸推理并三维展示（公开，未授权） [北京科技大学] [[专利](https://patents.google.com/patent/CN122436251A/zh)]
- [*CN121436110B*] **一种基于知识图谱的中医垂域大模型的训练方法** 以证候—症状词库、易混元组和上下文消歧整理预训练语料。A公开页时间线显示2026年7月31日授权并公布B文本；B正文此次未取得，技术摘要依据A公开文本。 [Daan Health Technology Beijing Co ltd] [[授权](https://patents.google.com/patent/CN121436110B/zh)] [[公开](https://patents.google.com/patent/CN121436110A/zh)]
- [*CN122364665A*] **一种基于大语言模型的中医古籍症状标准化处理方法** 用大语言模型从中医古籍切片识别候选症状，并映射到标准症状语义场完成术语标准化（公开，未授权） [黑龙江中医药大学] [[专利](https://patents.google.com/patent/CN122364665A/zh)]
- [*CN122135923A*] **辅助诊断结果和参考处方生成方法、装置、介质及计算机设备** 病历和诊疗思路各走向量与文本两路，四路召回后融合排序，由大模型生成中医诊断、证型、西医诊断和中药处方。2026年6月2日公开，尚未授权。 [浙江固生智能科技有限公司] [[专利](https://eureka.patsnap.com/patent/CN122135923A)]
- [*CN122245713A*] **基于大语言模型的中医智能问诊方法及系统** 从多模态问诊数据解析问诊意图，再用双路径检索中医知识，生成问诊结果（公开，未授权） [深圳市蓝宇飞扬科技有限公司] [[专利](https://patents.google.com/patent/CN122245713A/zh)]
- [*CN120913881B*] **基于多模态中医大语言模型的数据分析方法、系统、终端及介质** 用舌象、语音和问诊文本训练多模态中医大模型，输出初步中医分析。2026年6月12日授权。 [深圳心语心言智能技术有限公司] [[专利](https://eureka.patsnap.com/patent/CN120913881B)]
- [*CN122135936A*] **一种面向中医方剂推荐的知识图谱大模型问答方法及系统** 用中文指令大语言模型编码病历语义，与动态中医知识图谱的图向量做门控融合，推荐方剂并生成问答结果（公开，未授权） [北京科技大学] [[专利](https://patents.google.com/patent/CN122135936A/zh)]
- [*CN122025029A*] **融合类别信息与LLM的因果驱动对比学习与图注意力的中药处方推荐方法** 症状-草药异构/同构图 + LLM 增强因果机制做处方推荐（公开，未授权） [湖州师范学院] [[专利](https://eureka.patsnap.com/patent/CN122025029A)]
- [*CN122050861A*] **基于大模型结合双通道检索的中医智慧诊疗平台构建方法** LLM+中医知识图谱双通道检索，面向名医经验传承与处方生成（公开，未授权） [上海中医药大学附属岳阳中西医结合医院，上海市皮肤病医院] [[专利](https://patents.google.com/patent/CN122050861A/zh)]
- [*CN120913769B*] **基于多模态大模型的中医舌诊药饮推荐方法** 用大模型根据舌象生成病症描述并推荐药饮。2025年11月7日公开，2026年5月29日授权。 [天大智图（天津）科技有限公司，桂林电子科技大学] [[专利](https://patents.google.com/patent/CN120913769B/zh)]
- [*CN122117314A*] **一种基于大语言模型的智能针灸诊断Agent系统及诊断方法** 针灸知识库 + 图谱 + 向量检索 + 重排序，LLM 智能体分类问题并主动追问（公开，未授权） [河南工业大学] [[专利](https://eureka.patsnap.com/patent/CN122117314A)]
- [*CN121436111B*] **一种基于多模态数据融合的中医智能辨证模型训练系统及方法** 通过症状链、证候要素评分、证型逻辑组合与矛盾检测组织辨证推理。2026年5月15日授权，Google Patents显示Active；其权利要求侧重结构化推理，未据此认定公开了LLM权重。 [Daan Health Technology Beijing Co ltd] [[专利](https://patents.google.com/patent/CN121436111B/zh)]
- [*CN122091073A*] **一种基于多任务联合优化的中药处方生成方法与装置** 预训练大模型做自回归处方序列 + 草药集合预测，照顾低频药（公开，未授权） [杭州电子科技大学] [[专利](https://eureka.patsnap.com/patent/CN122091073A)]
- [*CN122050683A*] **一种基于图注意力网络与大语言模型的中药处方生成方法** 把中药处方生成转为多标签分类，用图注意力网络和大语言模型建模药物协同与禁忌。2026年5月15日公开。 [杭州市第一人民医院（西湖大学附属杭州市第一人民医院）] [[专利](https://patents.google.com/patent/CN122050683A/zh)]
- [*CN121862376A*] **基于知识图谱和大语言模型的中医辨证问答系统及方法** 古籍/医案分块抽实体建图谱，再按局部与全局关键词检索生成辨证问答（公开，未授权） [南京邮电大学] [[专利](https://patents.google.com/patent/CN121862376A/zh)]
- [*CN121687367A*] **基于结构化证据子图检索增强生成的中医草药推荐方法及系统** 多跳证据子图 + Hopfield 联想检索做草药推荐，并用图谱约束压幻觉（公开，未授权） [浙江中医药大学] [[专利](https://patents.google.com/patent/CN121687367A/zh)]
- [*CN121743505A*] **基于知识增强的中医医案按语生成方法及装置** 图谱子图混合检索后，按病因病机、治则、方药、预后四要素生成医案按语（公开，未授权） [浙江大学] [[专利](https://patents.google.com/patent/CN121743505A/zh)]
- [*CN121709160A*] **一种基于视觉语言模型的中医舌诊智能分析方法** 以Qwen-VL为舌诊视觉语言模型，经舌诊知识引导微调后，由舌象生成舌色、苔色等结构化结果及自然语言描述（公开，未授权） [中国计量大学] [[专利](https://patents.google.com/patent/CN121709160A/zh)]
- [*CN121480736A*] **基于知识蒸馏与强化学习的肿瘤中医智能处方推荐方法及系统** GPT-4o 教师蒸馏 Qwen 学生，再 DPO，做可解释的肿瘤中医处方（公开，未授权） [南京中医药大学] [[专利](https://patents.google.com/patent/CN121480736A/zh)]
- [*CN121524286A*] **一种心血管疾病的基于针灸诊疗知识图谱的智能问答系统** 构建心血管疾病针灸诊疗知识图谱，结构化查询结果交云端大语言模型润色；查不到时由大语言模型直接作答并提示仅供参考（公开，未授权） [天津中医药大学第一附属医院，江汉大学] [[专利](https://patents.google.com/patent/CN121524286A/zh)]
- [*CN121562809A*] **一种基于动态语义分块、知识图谱与多跳路径规划的中医大语言模型AI题库智能生成方法及系统** 对中医文本做语义分块和知识图谱多跳路径，再训练大语言模型生成中医题库（公开，未授权） [北京安戈普罗科技有限公司] [[专利](https://patents.google.com/patent/CN121562809A/zh)]
- [*CN121460056A*] **一种基于人工智能的方剂配制方法、系统、介质和设备** 用大语言模型从医案实体判定病名与证型并生成初步方剂，再由大语言模型评分，未达标则按结构化建议重新生成（公开，未授权） [中国计量大学] [[专利](https://patents.google.com/patent/CN121460056A/zh)]
- [*CN121460113A*] **一种基于中医语言大模型的中医智能分析方法及系统** 用LoRA微调得到中医语言大模型，按证型和主诉输出方剂（公开，未授权） [杭州轩岐智能科技有限公司，浙江中医药大学附属第三医院，北京航空航天大学] [[专利](https://patents.google.com/patent/CN121460113A/zh)]
- [*CN121393746A*] **基于大语言模型的经络辨证与针灸方案生成方法及系统** 把多源诊疗数据量化并提质后，结合经络辨证知识库和大语言模型生成针灸方案。2026年1月23日公开。 [广州双龙脉健康产业科技有限公司] [[专利](https://patents.google.com/patent/CN121393746A/zh)]
- [*CN121281871A*] **基于医学大语言模型多智能体的中医药临床数据自动化处理系统** 任务理解智能体、临床数据治理工具库和数据治理智能体协作，做中医疗效评价数据的结构化、标准化与流程生成。2026年1月6日公开；Google Patents显示Pending。 [四川大学华西医院] [[专利](https://patents.google.com/patent/CN121281871A/zh)]
- [*CN121331451A*] **一种融合舌象、心率及文本的多模态健康状态评估方法** 以舌象为主、结合心率和使用者自述文本，用提示词引导DeepSeek大模型生成健康状态评估（公开，未授权） [刘家豪] [[专利](https://patents.google.com/patent/CN121331451A/zh)]
- [*CN121436134A*] **一种多模态知识图谱构建方法及系统** 用大模型从中医药文本抽三元组，再融合真实病历层做成多模态图谱（公开，未授权） [杭州甘之草科技] [[专利](https://patents.google.com/patent/CN121436134A/zh)]

</details>

<details>
<summary>2025 · 25</summary>

- [*CN121210613A*] **基于检索增强生成的针灸大模型构建方法、系统及装置** 训练针灸大语言模型，问答请求做知识库向量检索后生成回答，诊断请求再检索针灸方案库给出治疗条目。2025年12月26日公开。 [北京科技大学] [[专利](https://patents.google.com/patent/CN121210613A/zh)]
- [*CN120690391B*] **一种基于知识图谱技术的中药经典名方智能推荐方法** 口语到术语的语义映射 + 体质过滤 + 多症状协同，推荐经典名方。2025年12月16日授权。 [顺福科技集团] [[专利](https://patents.google.com/patent/CN120690391B/zh)]
- [*CN121212280A*] **一种基于大语言模型的人-信息-物理三元数据融合中药制造知识图谱构建系统、电子设备及存储介质** 用大语言模型按中药术语和关系约束从制造文本抽取三元组，再按人-信息-物理本体构建中药制造知识图谱。2025年12月25日公开。 [北京中医药大学] [[专利](https://patents.google.com/patent/CN121212280A/zh)]
- [*CN121096596A*] **一种基于多模态大语言模型的中医临床辅助决策系统和方法** 融合舌象视觉特征与临床文本，检索相似病例后，由多模态大语言模型生成证候、诊断、中药处方和推理过程。2025年12月9日公开。 [清华大学深圳国际研究生院] [[专利](https://patents.google.com/patent/CN121096596A/zh)]
- [*CN121034544A*] **融合动态知识图谱的针灸大模型辨证方法及调理优化系统** 动态更新针灸知识图谱，结合患者时序临床特征，用图注意力和强化学习辨证并生成针灸方案。2025年11月28日公开。 [广东中科凯泽信息科技有限公司] [[专利](https://patents.google.com/patent/CN121034544A/zh)]
- [*CN120998428A*] **大小模型协同中药方剂优化方法、系统、终端及存储介质** 用方剂优化大语言模型给出宏观优化方，再用药效物质小模型溯源药材并调整组成，综合后形成最终方剂推荐。2025年11月20日公开，尚未授权。 [天津中医药大学] [[专利](https://patents.google.com/patent/CN120998428A/zh)]
- [*CN120809097A*] **基于大语言模型的中医五音疗疾个性化音乐生成系统及其构建方法** 先用大语言模型做中医辨证，再在五音特征约束下生成个性化五音治疗音乐。2025年10月17日公开。 [苏州昂升网络科技有限公司] [[专利](https://patents.google.com/patent/CN120809097A/zh)]
- [*CN120674039A*] **针灸穴位推荐方法及其模型获取方法、装置、设备及介质** 用病历对语言模型做初步训练，建立症状与针灸穴位的语义映射，再经参数微调与策略优化得到穴位推荐模型（公开，未授权） [河南工业大学] [[专利](https://patents.google.com/patent/CN120674039A/zh)]
- [*CN120337029A*] **一种基于大模型的中药分类方法** 对多源中药数据做实体识别并映射现代药理指标，再自适应微调预训练大模型完成中药分类。2025年7月18日公开。 [湖南省中医药研究院] [[专利](https://patents.google.com/patent/CN120337029A/zh)]
- [*CN120299726A*] **一种基于大模型智能体协作规划的中医诊断场景模拟方法** 把非结构化医案做成结构化知识，再用患者、医生、助手和专家几类大模型智能体协作，模拟中医诊断流程。2025年7月11日公开，尚未授权。 [华南理工大学] [[专利](https://eureka.patsnap.com/patent/CN120299726A)]
- [*CN120108651A*] **基于胸肺科中医问诊报告大语言模型的中医方剂推荐方法和系统** 用多知识域共享微调胸肺科中医问诊大语言模型，输出体质和症状参数，并推荐药食同源方剂。2025年6月5日公开。 [澳门科技大学] [[专利](https://patents.google.com/patent/CN120108651A/zh)]
- [*CN120108694A*] **基于知识图谱与医案增强RAG的中医智能问诊方法及系统** Leiden 子图检索 + 全局/本地混合召回，再由大模型统一生成问诊建议（公开，未授权） [江苏大学] [[专利](https://patents.google.com/patent/CN120108694A/zh)]
- [*CN120216657A*] **基于大语言模型的中药药物警戒问答系统的构建方法** 建立中药知识库并训练药物警戒检索增强模型PV-RAG，按自然语言提问生成中药安全回答。2025年6月27日公开。 [南京邮电大学] [[专利](https://patents.google.com/patent/CN120216657A/zh)]
- [*CN120221058A*] **基于多模态知识图谱与大语言模型的中医康复诊断系统** 舌苔、脉象与问诊特征对齐知识图谱嵌入，再交给中医康复专家大模型（公开，未授权） [浙江中医药大学] [[专利](https://patents.google.com/patent/CN120221058A/zh)]
- [*CN120067279B*] **基于AI大语言模型的中医智能问诊方法及系统** 面舌形体图像、语音气息与病症库融合的多模态问诊系统。2025年6月27日授权。 [医脉人工智能医疗科技（天津）] [[专利](https://patents.google.com/patent/CN120067279B/zh)]
- [*CN120148827A*] **一种基于大模型的心血管疾病医疗决策支持方法** 用预训练大模型融合中医证候知识和西医病理图谱，生成含西药、中医方剂和非药物干预的心血管决策方案。2025年6月13日公开，尚未授权。 [溧阳市中医医院] [[专利](https://eureka.patsnap.com/patent/CN120148827A)]
- [*CN119941636A*] **中医药多模态LLM训练方法及其应用** 分别提取舌苔与脉象特征，经跨模态注意力与文本特征融合后接入大语言模型，训练中医药多模态LLM。2025年5月6日公开。 [粤港澳大湾区精准医学研究院（广州）] [[专利](https://patents.google.com/patent/CN119941636A/zh)]
- [*CN119811630A*] **应用大语言模型的泌尿科中医问诊结果预测方法和系统** 用大语言模型从泌尿科中医问诊描述预测病灶核心关键词，并按反馈数据实时调整模型参数。2025年4月11日公开。 [中医药广东省实验室] [[专利](https://patents.google.com/patent/CN119811630A/zh)]
- [*CN119905208A*] **基于多源特征融合的中医方剂智能推荐方法、介质和设备** 融合内容推荐、协同过滤，并用大语言模型分析症状文本，按加权得分推荐个性化方剂（公开，未授权） [福建中医药大学] [[专利](https://patents.google.com/patent/CN119905208A/zh)]
- [*CN119763764A*] **一种基于大语言模型的中药处方推荐方法及系统** 软提示 + 交叉注意力把患者文本送进大模型，输出可控中药处方（公开，未授权） [杭州甘之草科技] [[专利](https://patents.google.com/patent/CN119763764A/zh)]
- [*CN119811698A*] **一种基于OCR识别和大模型的中药方数据解析方法及装置** 对手写中药方做OCR，把相冲、用量和服药建议拼成提示词送入大模型，生成处方综合判断。2025年4月11日公开。 [同力天合（北京）管理软件股份有限公司] [[专利](https://patents.google.com/patent/CN119811698A/zh)]
- [*CN119416782A*] **基于大语言模型的中医方学习方法、装置、设备及介质** 用 Qwen 等大模型对齐文言医案术语与白话，做名老中医方学习（公开，未授权） [成都字节流科技] [[专利](https://patents.google.com/patent/CN119416782A/zh)]
- [*CN119517372A*] **一种基于大语言模型的中医问答系统及方法** 从中医药文献构建数据集并训练大语言模型，接收用户医学问题后生成对话回答。2025年2月27日公开。 [郑新翰] [[专利](https://patents.google.com/patent/CN119517372A/zh)]
- [*CN119446558A*] **一种基于大语言模型的中医知识图谱生成方法及系统** 以中药和诊察治疗数据训练模型，按患者信息可视化输出治疗方案，并用疗效反馈继续更新模型。2025年2月17日公开。 [中国中医科学院中医药信息研究所] [[专利](https://patents.google.com/patent/CN119446558A/zh)]
- [*CN119252469A*] **一种用于智能中医系统的大语言模型的构建方法** 用舌诊图像标记和历史病历训练舌诊问诊模型，并据此构建用于智能中医系统的大语言模型。2025年1月7日公开。 [深圳问止中医健康科技有限公司] [[专利](https://patents.google.com/patent/CN119252469A/zh)]

</details>

<details>
<summary>2024 · 15</summary>

- [*CN119149754A*] **基于大模型和知识图谱的中医药方剂配伍方法及装置** 中医药大模型与知识图谱协同做方剂配伍（公开，未授权） [天津大学，天大智图（天津）科技] [[专利](https://patents.google.com/patent/CN119149754A/zh)]
- [*CN119069137A*] **利用AI大模型进行舌象分析的方法及装置** 在中医舌诊场景用AI大模型按体质、症状和综合解读做舌象分析（公开，未授权） [深圳伯德睿捷健康科技有限公司] [[专利](https://patents.google.com/patent/CN119069137A/zh)]
- [*CN119092157B*] **一种基于大语言模型的中药问答方法、装置、设备及介质** 在 Baichuan2-7B-Chat 上做中药问答。2025年2月7日授权。 [浙江大学，长三角智慧绿洲创新中心] [[专利](https://patents.google.com/patent/CN119092157B/zh)]
- [*CN119049664A*] **基于AI大模型的中医元气充盈智能健康管理系统** 把可穿戴数据转成中医术语后送入AI中医大模型（公开；2026-02-06已视为撤回） [重庆鼐龙生物科技有限公司] [[专利](https://patents.google.com/patent/CN119049664A/zh)]
- [*CN119049665A*] **基于AI大模型智能人体域网的中医六经辨证智能对话健康管理系统** 包含中医六经辨证术语大模型和对话式健康管理（公开；2026-02-06已视为撤回） [重庆鼐龙生物科技有限公司] [[专利](https://patents.google.com/patent/CN119049665A/zh)]
- [*CN118899077A*] **一种基于多模态大模型的中医舌诊分析系统及方法** 用云诊 TongueAI 生成舌面象解读、多轮问答和体质推理数据，指令微调得到 TongueLMM，用于舌诊解读、多轮问答和体质推理。2024年11月8日公开。 [合肥云诊信息科技有限公司] [[专利](https://patents.google.com/patent/CN118899077A/zh)]
- [*CN118838996A*] **基于大语言模型和知识图谱的中医药问答系统构建方法** LLM 生成与知识图谱补全闭环的中医药问答（公开，未授权） [北京理工大学，北京理工大学唐山研究院] [[专利](https://patents.google.com/patent/CN118838996A/zh)]
- [*CN118430833A*] **一种基于大语言模型的中医知识深度挖掘方法** 同时训练检索增强和模型微调，使系统既能解释中医名词和证候，也能按患者输入给出治疗方案（公开，未授权） [西南大学] [[专利](https://patents.google.com/patent/CN118430833A/zh)]
- [*CN117828050B*] **基于长文档检索增强生成的中医问答方法、设备及介质** 长文档 RAG（扩展、召回、重排序、来源标注）做中医问答。2024年4月5日公开，2024年7月9日授权。 [北京智谱华章科技] [[专利](https://patents.google.com/patent/CN117828050B/zh)]
- [*CN118280556A*] **一种基于计算视觉与大语言模型辅助中医诊疗的系统** 大语言模型处理语音问诊，计算机视觉把患者图像转成诊断信息，检索增强后作为大语言模型输入，辅助中医诊疗（公开，未授权） [深圳金草健康科技有限公司] [[专利](https://patents.google.com/patent/CN118280556A/zh)]
- [*CN118230893A*] **一种基于AI大模型的中医处方智能推荐方法和系统** 用病历训练 AI 大模型生成个性化中药处方，并接到医院信息系统（公开，未授权） [杭州甘之草科技] [[专利](https://patents.google.com/patent/CN118230893A/zh)]
- [*CN118098506A*] **一种基于大语言模型的针灸辅助诊疗和模型评价的方法** 用标注症状和穴位操作的数据微调ChatGLM3-6B，输出针灸方案，并用句子相似度评价生成结果（公开，未授权） [东北大学] [[专利](https://patents.google.com/patent/CN118098506A/zh)]
- [*CN118070907A*] **一种基于大语言模型的中医客服回复系统** 用同义词增广中医资料并训练Transformer大语言模型，微调后解析客户请求并生成回复；该申请于2024-07-09授权为CN118070907B [卓世智星（天津）科技有限公司] [[专利](https://patents.google.com/patent/CN118070907A/zh)]
- [*CN117786590A*] **以大语言模型为先验的智能中医系统** 用大语言模型优化患者诊断文本，再做语义理解，预测中医证候和病因并给出治疗建议。2024年4月1日公开。 [上海源庐加佳信息科技有限公司] [[专利](https://patents.google.com/patent/CN117786590A/zh)]
- [*CN117493579A*] **一种基于大语言模型的中医知识图谱构建方法** 用大语言模型从中医文本抽取命名实体和实体关系，按相似度融合后生成中医知识图谱（公开，未授权） [同济大学] [[专利](https://patents.google.com/patent/CN117493579A/zh)]

</details>


</details>

## 论文

这里只收方法、评测和系统论文。发布了领域大模型的条目在「开源模型」，不在这里重复。

<details>
<summary>Agent（20）：问诊流程、多智能体</summary>

<details>
<summary>2026 · 12</summary>

- [*Chinese Medicine*] **MAGR-TCM：知识图谱驱动的多智能体中医妇科居家问诊与分诊模型（Lv 等）** Lv、Pan、Li、Hu、Xu、Jin、Fang 等提出 MAGR-TCM，在专家监督下从 741 份高质量医案抽取知识图谱（文中称 10,231 个实体、32,051 条关系），并以四个智能体组成的检索增强生成框架，试图从口语化主诉重建中医“病–证–法–方–药”推理链，用于妇科居家健康咨询与分诊。作者报告该模型在 RAGAS 自动评估和专家人工评估中优于所比较基线，并在安全性测试集上达到 100% 敏感度与特异度；这些数字均为论文自报。这是面向居家场景的方法学与原型评估，不是临床疗效试验。本次打开了 Springer Nature / Chinese Medicine 论文页。 [安徽中医药大学医药信息工程学院，安徽中医药大学中医学院，安徽中医药大学中西医结合学院] [[DOI](https://doi.org/10.1186/s13020-026-01485-y)] [[论文](https://link.springer.com/article/10.1186/s13020-026-01485-y)]
- [*arXiv*] **Evidence-Based TCM Visualization Diagnosis System** 以症状—证候知识图谱、症状匹配和信息增益策略进行主动问诊，配合诊疗可视化；问诊策略展示以案例为主。 [[论文](https://arxiv.org/abs/2606.06869)]
- [*arXiv*] **DeepTCM1.0** 基于DeepSeek V3.2的11专家多智能体，解析中药复方机制（桂枝汤验证）；Research Square后上到arXiv [广州中医药大学，Chinese Medicine Guangdong Laboratory (Hengqin)，Changzhi Medical College] [[论文](https://arxiv.org/abs/2608.18103)] [[预印本](https://doi.org/10.21203/rs.3.rs-9844166/v1)]
- [*arXiv*] **DeepRoot** 多智能体把《神农本草经》建成可核验Neo4j图谱再做治疗推理，代码与评测脚本已开源 [[论文](https://arxiv.org/abs/2606.15931)] [[代码](https://github.com/CarlisleMa/deeprootv1)]
- [*Studies in Health Technology and Informatics*] **韩医CPX场景自动生成** 用大模型和检索增强，加上多模态临床线索，自动生成韩医标准化病人CPX场景并给出量化反馈；10名专家验证 [韩国韩医学研究院] [[DOI](https://doi.org/10.3233/shti260671)]
- [*arXiv*] **TCMScience** 中医科研发现智能体，把语言模型提案与执行、发布权限分开，避免不同证据类型混推 [[论文](https://arxiv.org/abs/2610.24601)]
- [*Journal of Pharmaceutical Analysis*] **TCM-Agent** 面向网络药理学与中药发现的 LLM 多智能体系统 [[论文](https://doi.org/10.1016/j.jpha.2026.101581)] [[代码](https://github.com/AITCM/TCM-Agent)]
- [*arXiv*] **MACAT** 多智能体文化感知翻译框架，实验覆盖中医经典与《论语》文化负载词英译 [[论文](https://arxiv.org/abs/2606.01276)]
- [*Applied Sciences*] **KM-Agent** 韩医/东亚传统医学工具增强Agent，检索4780条药材–证候–穴位元数据，并在TCMBench等上评测。MDPI/OpenAlex 署名圆光大学、釜山大学、东国大学等 [圆光大学，釜山大学等] [[论文](https://www.mdpi.com/2076-3417/16/7/3377)] [[代码](https://github.com/wonyung-lee/km-agent)]
- [*arXiv*] **DERM-3R** 资源受限下的中医皮肤病多模态多智能体框架（识别/表征/辨证论治三智能体） [[论文](https://arxiv.org/abs/2604.09596)]
- [*arXiv*] **CORE-Acu** 针灸临床决策：结构化推理轨迹与知识图谱安全否决闭环 [[论文](https://arxiv.org/abs/2603.08321)]
- [*Engineering Applications of Artificial Intelligence*] **AcuModel / AcuAgent** 结合 AcuModel、针灸知识图谱、语义路由与规则约束，进行主动追问和针灸推理；公开项目说明及样例，完整权重与训练数据需向作者申请。 [[DOI](https://doi.org/10.1016/j.engappai.2026.116139)] [[资料](https://github.com/mosheng555/AcuModel-And-AcuAgent)]

</details>

<details>
<summary>2025 · 7</summary>

- [*arXiv*] **经方 (Jingfang)** 多智能体中医问诊与辨证论治系统，结合十问歌引导问诊、证候判别模型和双阶段处方检索。 [[论文](https://arxiv.org/abs/2502.04345)]
- [*中医杂志*] **基于雅意大模型的中医智能预问诊** 刘奕清、李迎、杨洪军等用 DeepSpeed ZeRO-3 微调 YAYI 2-30B，并用症状关系带权无向图做智能体辨证。模拟测试里，执业医师题正确率 94.09%，执业中药师 78.00%，症状术语 87.50%，经络 68.80%。临床测试辨证准确率 88.33%，问诊轮次和时间少于主治医师。2025年第 66 卷第 9 期 895–900 页。 [中国中医科学院医学实验中心，中国科学院自动化研究所，天津中科闻歌科技有限公司，中国中医科学院中医基础理论研究所] [[DOI](https://doi.org/10.13288/j.11-2166/r.2025.09.005)] [[论文](https://link.cnki.net/doi/10.13288/j.11-2166/r.2025.09.005)]
- **仁术AI (RenShu-AI)** FastAPI + LangGraph 多智能体中医问诊系统，融合 GraphRAG 与 DeepSeek-TCM [[代码](https://github.com/yanlinPeng-code/RenShu-AI)]
- [*Information*] **中药化合物检索智能体** 中药化合物信息检索AI智能体系统 [郑州大学] [[DOI](https://doi.org/10.3390/info16070543)]
- [*Journal of King Saud University Computer and Information Sciences*] **DiagX-DT** 辨证排除式推理框架，结合思维链与外部中医知识库迭代剔除不合理证候选项 [[DOI](https://doi.org/10.1007/s44443-025-00123-1)]
- [*proceedings-article*] **An Intelligent TCM Diagnosis System with Localized LLMs and Modular Multimodal Reasoning Enhanced by RAG** 该本地部署系统用望、闻、问、切四个智能体，经模块化组件处理和多模态检索增强生成，把舌象、声音、脉象和症状交给中心推理模块生成诊断与健康建议。 [Hosei University，Fuzhou University，Hong Kong Polytechnic University，Beihang University] [[DOI](https://doi.org/10.1109/cyberscitech68397.2025.00061)]
- [*Neurocomputing*] **AcuGPT-Agent** 围绕针灸治疗不孕，结合专科大模型、知识图谱和跨知识库路由，并以 EvalAcu 评估知识与任务能力。 [南京中医药大学] [[DOI](https://doi.org/10.1016/j.neucom.2025.131116)]

</details>

<details>
<summary>2024 · 1</summary>

- [*대한한의학회지*] **Pilot Development of a 'Clinical Performance Examination (CPX) Practicing Chatbot' Utilizing Prompt Engineering** 作者把韩国韩医学研究院的标准化病人情景改写成文本，用角色提示和少样本提示调用GPT-4，做成韩医临床技能考试练习聊天机器人；内部评价中正确性和依从性较高，保密性和自然度仍需改进。 [Gachon University，Pusan National University] [[DOI](https://doi.org/10.13048/jkm.24013)]

</details>


</details>

<details>
<summary>多模态 / 四诊（37）：舌、面、脉</summary>

<details>
<summary>2026 · 17</summary>

- [*arXiv*] **Seeing Is Not Enough: Knowledge-Grounded Active Inquiry from Uncertain Visual Evidence** 牛津大学 Yucheng Liu 与中国科学院北京纳米能源与系统研究所 Everett X. Wang（通讯）提出，在中医舌诊中相似舌象可能对应不同证候，而关键症状并不出现在照片里，因此用舌象与脉象预测来引导针对性地问诊，并用获得的回答收窄证候清单后再报告。作者构建 2600 例由真实舌象照片、指定证候、模拟症状回答和生成脉象组成的病例，其中 2599 例进入来源不相交的五折评估。论文称在干净图像上，仅用舌象/脉象预测的细粒度证候准确率为 46.4%；在获取代价为 12 时，不问诊图像/脉象证据的问诊准确率为 34.4%，二者结合达到 65.8%，前三纳入率为 90.8%。本次打开了 arXiv 摘要页与真实 PDF（2610.38774，页面为 v2）。结果均为作者自报。 [University of Oxford，Beijing Institute of Nanoenergy and Nanosystems, Chinese Academy of Sciences] [[论文](https://arxiv.org/abs/2610.38774)] [[PDF](https://arxiv.org/pdf/2610.38774)]
- [*arXiv*] **acuSimNet: Multi-View Self-Occlusion-Awared Visibility Learning for Cranio-Cervical Acupuncture Points** 佐治亚理工学院马佳涛与德比大学孙启磊提出面向头颈部穴位多视角、自遮挡可见性预测的多任务网络 acuSimNet。论文称穴位由抽象原则定义而非清晰解剖标志，现有方法多为单视角或依赖相对位置推算，对自身、毛发或衣物遮挡关注不足；该工作在174个头颈部穴位的高维分类设定下训练，作者报告验证集准确率达99.97%，并将达到99%准确率的训练轮次从既有方法的约3000轮降至86轮。标题按原文保留 Awared 拼写。本次打开了arXiv摘要页（2611.20025，2026年11月15日提交）。结果均为作者自报。 [Georgia Institute of Technology，University of Derby] [[论文](https://arxiv.org/abs/2611.20025)] [[PDF](https://arxiv.org/pdf/2611.20025)]
- [*arXiv*] **SEAT: Sign-Type Evidence-Audited Transport for Multi-Label Tongue Diagnosis** 东北大学徐柳怡、王青、梁子凯、卢安阳与钱一宁（通讯，东北大学秦皇岛分校）提出面向多标签舌诊的证据审核框架 SEAT。论文称单张舌象常同时出现多种体征，证据类型包括局部形态、全局色度及标签共现，既有方法多用共享表征和统一多标签头，难以核验预测是否来自临床相关证据。SEAT 在冻结的 DINOv2 图像块特征上，分别用掩膜引导的体征特异注意力处理局部形态，用 LAB/HSV 颜色原型上的半松弛最优传输强化淡白舌识别，并用共现感知传输正则塑造批次级标签边际。作者报告在 TongueDx 基准上，六个随机种子的平均宏平均 F1 为 72.59（标准差 1.04），六模型集成达到 74.15。论文注明已投 IEEE。本次打开了 arXiv 摘要页与真实 PDF（2611.19748），并打开了作者给出的代码仓库页。结果均为作者自报。 [Northeastern University] [[论文](https://arxiv.org/abs/2611.19748)] [[PDF](https://arxiv.org/pdf/2611.19748)] [[代码](https://github.com/NEU-TCM-Lab/Sign-type-Evidence-Audited-Transport)]
- [*Frontiers in Medicine*] **Cracks-YOLO：结合可切换空洞卷积与 Transformer 的舌裂纹 YOLOv5 检测方法（Ding 等）** Ding、Wu、Shen、Lin、Men 针对舌裂纹形态、尺度和分布多变、既有检测精度与速度不足的问题，在 YOLOv5 骨干中引入可切换空洞卷积以调整感受野，并加入 Transformer 编码器以捕捉长程依赖，用于中医舌裂纹检测。这是目标检测方法论文；本次打开的摘要未在提取范围内给出完整定量结果，故不转写具体准确率。不是临床疗效试验。本次打开了期刊全文页。 [广州中医药大学医药信息工程学院，香港城市大学商学院] [[DOI](https://doi.org/10.3389/fmed.2026.1901533)] [[论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1901533/full)]
- [*Health Information Science and Systems*] **ConsTCM: aligning fundus images with constitution differentiation in multimodal language model for Traditional Chinese Medicine** 天津大学纪翔宇、饶国政等提出 ConsTCM，用两阶段监督微调把眼底影像与中医体质辨识对齐到多模态语言模型：先在通用眼底检查数据上做基础微调，再以医院真实自标注病例做面向体质任务的特定微调，并混合已有分类任务与医院数据构建微调集。作者报告相对基线提升 5.6%，消融中相对基础模型在客观评估上提升 47%。期刊页标注在线 2026年4月6日，刊于 Health Information Science and Systems 2026年14卷1期文章号 50，封面日期 2026年12月。本次打开了 Springer 官方文章页。页面版权为版权所有、非开放获取，官方 PDF 链路返回的是 HTML 而非 PDF。指标均为作者自报。 [Tianjin University，Tianjin University of Traditional Chinese Medicine，La Trobe University，Institute of Science Tokyo] [[论文](https://link.springer.com/article/10.1007/s13755-026-00442-1)] [[DOI](https://doi.org/10.1007/s13755-026-00442-1)]
- [*BMC Medical Informatics and Decision Making*] **脉波与语音联合筛查冠心病和心衰** 上海中医药大学等把桡动脉脉搏波当作脉诊，把语音当作闻诊，用来筛查冠心病和心力衰竭。同步记了 553 人，包括健康人、冠心病和心衰，另有 194 人做外部验证。 [[DOI](https://doi.org/10.1186/s12911-026-03518-w)]
- [*Sensors*] **红外热像面部穴位两级定位** 按骨度分寸和中医解剖规则整理多姿态红外面部热像，先检测人脸，再回归穴位位置。 [[DOI](https://doi.org/10.3390/s26144498)]
- [*Journal of Traditional Chinese Medicine*] **空腹过程的寸关尺脉图定量** 51 名健康人在空腹前（第 0 天）、空腹中（第 4 天）和空腹后（第 7 天）采集左寸、右寸和右关脉图，比较与胃肠虚实有关的脉象参数。 [[DOI](https://doi.org/10.19852/j.cnki.jtcm.2026.02.019)]
- [*arXiv*] **白睛异常分割（HD-DinoMoE）** 中医目诊看白睛缺少定量。这篇用分层混合专家网络，在复杂拍摄条件下分割巩膜表面异常。 [[论文](https://arxiv.org/abs/2606.04888)]
- [*Medicine in Novel Technology and Devices*] **基于中医脉诊矩阵的客观脉象分析** 用中医脉诊矩阵做客观脉象分析。文章认为现有脉图定义不完整，客观化标准也不统一。 [[DOI](https://doi.org/10.1016/j.medntd.2026.100429)]
- [*IEEE Journal of Biomedical and Health Informatics*] **可控 Transformer 面诊** 用一个可控的 Transformer，同时做多项中医面诊任务。2026 年发表。 [[DOI](https://doi.org/10.1109/jbhi.2026.3706751)]
- [*proceedings-article*] **Multimodal TCM Seven-Emotion Recognition: A Three-Modality Joint Consultation Framework Based on LLMs and Cross-Attention Fusion** 该七情识别框架在IEMOCAP的10593个样本上宏观F1为87.6%，再用冻结的大语言模型把神经预测写成中医辨证报告。 [Zhejiang University of Technology] [[DOI](https://doi.org/10.1145/3829441.3829486)]
- [*Lecture Notes in Computer Science Medical Image Computing and Computer Assisted Interventi*] **MLLM-Enhanced Region-Aware Bidirectional Evidence-Based Model for Tongue Diagnosis** 用多模态大模型做区域感知的双向循证舌诊。 [[DOI](https://doi.org/10.1007/978-3-032-38098-2_44)]
- [*arXiv*] **LingLan多模态辨证大模型** 面向望闻问切多模态数据的中医诊断大模型。与灵兰秘典评测基准（arXiv 2602.01779）不是同一篇 [清华大学深圳国际研究生院] [[论文](https://arxiv.org/abs/2609.25715)]
- [*Chinese Medicine*] **GNN-BERT 的症状–穴位推荐** 用异构图和图神经网络，再配合微调的 BERT，建模症状和穴位的配伍，用来推荐穴位。 [[DOI](https://doi.org/10.1186/s13020-026-01458-1)]
- [*arXiv*] **Alpha-TCM: A Nine-Layer Framework for TCM-Guided Multimodal Inference and Structured-Prior Auditing** 提出将语义、多模态采集、质量、知识先验、概率推断、时序更新、决策、语言交互与人工治理分开的九层中医系统架构，并在合成数据上对第1–5层的知识–证据接口做了可复核实验。作者明确这是系统设计与合成原型，不能用于验证中医理论，也不支持临床诊断或治疗主张。 [牛津大学，中国科学院北京纳米能源与系统研究所] [[论文](https://arxiv.org/abs/2610.38754)]
- [*Studies in Rhythm Engineering Cognitive Neuroscience and Artificial Intelligence*] **AI Tongue Diagnosis: Expert System with LLMs for Abdominal Disease Detection Through Mobile App** 用大语言模型做移动端舌诊专家系统，面向腹部疾病检测。 [[DOI](https://doi.org/10.1007/978-3-032-19966-9_2)]

</details>

<details>
<summary>2025 · 11</summary>

- [*Biomedical and Environmental Sciences*] **贫血女性舌面图像特征分析与风险筛查模型构建** Hongyuan Fu、Yi Chun、Yahan Zhang 同等贡献，Yongzhi Li 与许家佗通讯。发表于 Biomedical and Environmental Sciences 2025 年 38 卷第 8 期的方法论文，在曙光医院纳入 533 名 20–49 岁女性，用面舌图像颜色与纹理特征筛查贫血。LASSO 从 62 个指标中选出 19 个；ANN 测试集 AUC 0.849、准确率 0.781，ResNet50V2 融合模型 AUC 0.846、准确率 0.818。官方期刊 PDF 可下载，未见印刷 Creative Commons 许可，也未见代码或原始图像。DOI 10.3967/bes2025.047。 [上海中医药大学中医学院，上海中医药大学教务处，上海中医药大学中医健康服务协同创新中心，中国航天员科研训练中心航天员健康实验室] [[DOI](https://doi.org/10.3967/bes2025.047)] [[论文](https://www.besjournal.com/en/article/doi/10.3967/bes2025.047)]
- [*Chinese Medicine*] **Liu 等：双中心舌象深度学习中医体质识别模型** Liu、Fan 共同第一、Zhang 通讯在东直门医院与广安门医院前瞻采集 1374 例舌象，融合传统特征与深度特征识别五种体质。摘要与表 5 的准确率印刷不一致，AUC 两处均为 0.948／0.898，须并记。正文未见代码仓库。须与本站 tonguenet、chen2025-tongue-analysis 及其他体质条目区分。 [北京中医药大学生命科学学院，清华大学天津高端装备研究院] [[DOI](https://doi.org/10.1186/s13020-025-01126-w)] [[论文](https://cmjournal.biomedcentral.com/articles/10.1186/s13020-025-01126-w)]
- [*Frontiers in Physiology*] **Chen 等：面向中医辅助诊断的深度学习自动化舌象分析系统** Chen、Chen、Zhou、Zhu、He、Zhang 通讯提出采集硬件、半监督分割、颜色校正和特征分类一体的舌诊系统。临床样本 2,738 例。作者自报 U2net-MT 舌体分割 Dice 0.967；正文未见代码仓库，训练／测试张数未清楚给出。须与本站 tonguenet、TongueDx／TongueDx2 区分。 [四川大学生物医学工程学院，四川省第二中医医院] [[DOI](https://doi.org/10.3389/fphys.2025.1559389)] [[论文](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1559389/full)]
- [*Frontiers in Physiology*] **TongueNet：面向中医舌诊的多模态融合与多标签分类模型（Yang 等）** Yang、Dong、Lin、Lü 通讯提出 TongueNet，融合舌象与文本并对病性、病位做多标签分类。训练使用 Roboflow 汇总的 4,815 张舌象。作者自报病性准确率 89.12%、F1 48.07%；正文未见代码仓库。须区分内蒙古自治区中医医院、内蒙古医科大学与内蒙古大学。 [内蒙古自治区中医医院风湿科，内蒙古医科大学中医学院，内蒙古大学数学科学学院] [[DOI](https://doi.org/10.3389/fphys.2025.1527751)] [[论文](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1527751/full)]
- [*Scientific Reports*] **脉诊机器学习识别妊娠与冠心病** 用 MEMS/CMOS 便携脉诊仪采集健康女性、冠心病女性和孕早期女性的脉图，再用机器学习区分妊娠和冠心病。 [[DOI](https://doi.org/10.1038/s41598-025-19780-3)]
- [*IEEE BIBM 2025*] **用大模型构建中医舌诊本体** 用大语言模型辅助构建中医舌诊本体 [[DOI](https://doi.org/10.1109/bibm66473.2025.11356313)]
- [*Lecture Notes in Electrical Engineering*] **智能脉诊：信号处理与深度学习** 用信号处理和深度学习对中医脉诊信号做健康状态分类。 [[DOI](https://doi.org/10.1007/978-981-95-1999-6_19)]
- [*ICASSP 2025*] **少样本舌诊上下文多任务微调** 舌象到体质直接判别的少样本上下文多任务LLM微调方法 [东北大学] [[DOI](https://doi.org/10.1109/ICASSP49660.2025.10887764)]
- [*International Conference on Digital Transformation and Management*] **多通道桡动脉信号的脉象识别** 用多通道设备采集桡动脉搏动，去噪并提取特征后，用卷积神经网络识别常见脉象。样本量和记录都没有公开。 [[DOI](https://doi.org/10.1145/3795546.3795575)]
- [*Medical Engineering & Physics*] **TPC-GCN：中医脉象分类** 先用改进的 SMOTE 扩充脉象样本，再提取多域特征，用图卷积网络做中医脉象分类。 [[DOI](https://doi.org/10.1016/j.medengphy.2025.104401)]
- [*arXiv*] **TCDiff** 三联级联扩散模型生成高保真多模态中医EHR，并构建**TCM-SZ1**基准数据集 [[论文](https://arxiv.org/abs/2508.01615)]

</details>

<details>
<summary>2024 · 5</summary>

- [*IEEE ECBIOS*] **高血压的中医面色分类** 建立用于高血压的中医面色分类模型。 [[DOI](https://doi.org/10.1109/ecbios61468.2024.10885481)]
- [*Digital Chinese Medicine*] **面色与体型的中医体质图像辨识** 给健康人拍全身站立照，按中医体质量表标上体质。面色和体型用颜色空间和局部二值模式提取，全身图像再用双分支网络提取深度特征，合在一起用随机森林辨认体质。准确率 0.842，精确率 0.868，F1 0.790。 [[DOI](https://doi.org/10.1016/j.dcmed.2024.09.002)]
- [*Bioengineering*] **面向糖尿病的中医脉诊卷积神经网络** 整理脉诊信号供卷积神经网络使用，以提高中医脉诊判断糖尿病的一致性。脉诊长期依赖指下感觉，重复性差。 [[DOI](https://doi.org/10.3390/bioengineering11060561)]
- [*IEEE ITNEC*] **统计特征与 MobileViT 的中医面色分类** 用统计特征和 MobileViT 做中医面色自动分类。 [[DOI](https://doi.org/10.1109/itnec60942.2024.10733073)]
- **Chinese-LLaVA-Med** 基于 LLaVA 架构的中文医学多模态大模型，支持中文医学影像问答，配套 llava-med-zh-eval 评测集与开源 7B 权重 [[代码](https://github.com/BUAADreamer/Chinese-LLaVA-Med)]

</details>

<details>
<summary>2023 · 4</summary>

- [*Frontiers in Physiology*] **Shi 等：基于舌象的肺癌风险预警模型** Shi、Guo（共同第一）、Chun、Liu、Liu、Tu、Xu 通讯用 TFDA-1 舌象对 862 名参与者建立肺癌风险预警模型。仅用舌象时随机森林准确率 0.679±0.048、AUC 0.752±0.051，为作者自报；数据因项目保密不公开。须与本站其他舌诊条目区分，不修改人物页 person-xu-jiatuo。 [上海中医药大学实验教学中心，上海中医药大学基础医学院，上海中医药大学附属龙华医院] [[DOI](https://doi.org/10.3389/fphys.2023.1154294)] [[论文](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2023.1154294/full)]
- [*BMC Complementary Medicine and Therapies*] **桡动脉脉搏波识别多囊卵巢综合征** 用桡动脉脉搏波参数和机器学习区分多囊卵巢综合征与健康人，共 459 名受试者，用来把中医脉诊客观化。 [[DOI](https://doi.org/10.1186/s12906-023-04249-5)]
- [*Phenomics*] **仿生设备采集中医脉象的规程** 给出用仿生脉诊设备把中医脉象信息数字化采集的规程。 [[DOI](https://doi.org/10.1007/s43657-023-00104-2)]
- **XrayGLM** 会看胸部X光片的中文多模态医学大模型 [澳门理工大学] [[代码](https://github.com/WangRongsheng/XrayGLM)]

</details>


</details>

<details>
<summary>RAG / 知识图谱（72）：检索和医案、方剂图谱</summary>

<details>
<summary>2026 · 21</summary>

- [*JMIR AI*] **儿童流感中成药知识图谱增强问答系统（KG+LLM）** 中国中医科学院中医临床基础医学研究所 Haoyuan Li、Guozhen Zhao 等与北京中医药大学针灸推拿学院合作，提出面向儿童流感中成药推荐的知识图谱增强问答系统，通讯作者为 Nannan Shi。页面作者名单为英文，未擅自音译中文名。该工作已于2026年11月13日正式发表于 JMIR AI 第5卷，DOI 为 10.2196/101648。论文称儿童流感中成药的临床证据分散在指南、专家共识和临床研究中，证候用药所需的多维知识增加了检索与标准化难度。本次打开了 JMIR AI 正式发表页；PMC 页面本轮返回 HTTP 500，故未作为已打开来源。保留原预印本链接。这是已有条目的正式发表更新，不是新条目。 [China Academy of Chinese Medical Sciences，Beijing University of Chinese Medicine] [[论文](https://ai.jmir.org/2026/1/e101648)] [[DOI](https://doi.org/10.2196/101648)] [[预印本](https://doi.org/10.2196/preprints.101648)]
- [*计算机工程与应用*] **ReTCM：融合反思机制与检索增强生成的中医问诊模型（向洋等）** 西南科技大学向洋、李理、韩东轩、苑中旭在《计算机工程与应用》发表ReTCM。论文提出融合中医知识图谱、对齐理论–证候–治疗过程的三层外部知识库、检索增强生成与证据驱动反思机制，用于中医问诊，以减少幻觉与推理偏差。作者报告其在ROUGE-L、METEOR、FactScore和CMB上优于多种基线，并称在CMB上较HuangDI和GPT-4o分别提高5.8和6.9个百分点。期刊页标注接收2026年1月8日、修回2026年4月2日、在线2026年11月1日、出版2026年10月30日，刊于2026年62卷21期114–125页。本次打开了期刊官方页面。指标为作者自报。 [西南科技大学，四川省工业自主可控人工智能工程技术研究中心，中国科学技术大学] [[论文](http://cea.ceaj.org/CN/10.3778/j.issn.1002-8331.2601-0109)] [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2601-0109)]
- [*BMC Bioinformatics*] **LLM-H2G：融合大模型语义的超图对比学习草药–疾病关联预测（Zhang 等）** Zhang、Yin、Wu、Yao、Yang、Cui、Li、Hu Pengwei、Hu Lun 提出 LLM-H2G，把草药、化合物、蛋白质和疾病放入增强异构超图，用大模型对实体名做语义编码，再以 InfoNCE 目标与结构表示对齐。作者报告在 TCM-suite 与 Ethnobotany 基准上优于多种网络嵌入、图神经网络、图对比学习和超图基线，稀疏连接草药上的差距更大；消融显示语义增强与超图构建都必要。病例分析属于计算归因与文献支持的新关联提示。这是计算方法研究，不是临床试验。本次打开了 Springer / BMC Bioinformatics 论文页。 [中国科学院新疆理化技术研究所，中国科学院大学，新疆师范大学计算机科学技术学院] [[DOI](https://doi.org/10.1186/s12859-026-06652-4)] [[论文](https://link.springer.com/article/10.1186/s12859-026-06652-4)]
- [*Communications in Computer and Information Science (Springer)*] **Hybrid Retrieval + Re-ranking TCM Prescription Generation** 混合检索+重排序增强LLM的中医处方生成（Springer CCIS会议论文） [齐鲁工业大学，Shandong University，Shandong Academy of Sciences，山东中医药大学] [[论文](https://doi.org/10.1007/978-981-92-3563-6_21)]
- [*BMC Medical Informatics and Decision Making*] **将韩医院电子病历转换到 OMOP CDM：方法与意义** Park、Lee 通讯等把圆光大学光州韩医院电子病历转到 OMOP CDM 5.3，建成含 88,449 名患者的 WKTKM 库，并为韩医药特有概念扩展 KIOM 术语。患者数据不能公开；ETL 代码在 GitHub，映射规则在补充材料。这是方法学概念验证，不是疗效试验。许可为 CC BY 4.0。 [韩国韩医学研究院，韩国韩医药振兴院韩医药大数据中心，庆熙大学姜东医院，圆光大学韩医学院] [[DOI](https://doi.org/10.1186/s12911-026-03418-z)] [[论文](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-026-03418-z)] [[代码](https://github.com/ManYoungPark/KCDM_OMOP)]
- [*Health Information Science and Systems*] **LDComKG: an LLM-powered dual-enhanced framework for community-aware knowledge graph completion in traditional Chinese medicine** 南京中医药大学曾星、王紫妍、柴静娴等提出 LDComKG，用大语言模型从中医古籍非结构化文本中自动抽取实体与关系以构建知识图谱，再结合 Leiden 社区发现和 GraphSAGE 节点表示，用于链接预测与图谱补全。作者报告在标注的古代医籍数据集上，GPT-4o-mini 配置下准确率 93.33%、F1 93.69%、AUC 95.87%，GPT-4o 配置下准确率 95.94%、F1 95.07%、AUC 97.72%，并与 KEPLER、CoLAKE 等做了比较。期刊页标注在线 2026年2月18日，刊于 Health Information Science and Systems 2026年14卷1期文章号 41，封面日期 2026年12月。本次打开了 Springer 官方文章页。页面版权为版权所有、非开放获取，官方 PDF 链路返回的是 HTML 而非 PDF。指标均为作者自报。 [Nanjing University of Chinese Medicine，Nanjing Hospital of Chinese Medicine affiliated to Nanjing University of Chinese Medicine] [[论文](https://link.springer.com/article/10.1007/s13755-026-00429-y)] [[DOI](https://doi.org/10.1007/s13755-026-00429-y)]
- [*Frontiers in Medicine*] **靳三针知识图谱问答 (Jin San Zhen KG-QA)** 靳三针针灸流派知识图谱+大模型问答工具 [广州中医药大学] [[DOI](https://doi.org/10.3389/fmed.2026.1755583)]
- [*兰州大学学报(医学版)*] **融合知识图谱与大语言模型的中医证据构建方法** 张雪芹、文天才等从数智循证视角提出融合知识图谱与大语言模型的中医多源证据结构化、分级整合与动态更新方法，并在既有证据生态系统平台上作可行性说明。 [中国中医科学院] [[DOI](https://doi.org/10.13885/j.issn.2097-681X.T20260017)] [[论文](https://cjournal.hep.com.cn/1000-2812/CN/10.13885/j.issn.2097-681X.T20260017)]
- [*IEEE BigComp 2026*] **知识图谱增强的中医问答大模型** 用知识图谱增强大模型的中医问答，补辨证推理并降低多源数据带来的幻觉 [燕山大学，福建中医药大学，暨南大学] [[DOI](https://doi.org/10.1109/bigcomp68355.2026.00029)]
- [*Frontiers in Medicine*] **树状自反思检索中医问答** 树状组织语料+自反思检索的中医 QA 方法（Frontiers in Medicine 2026） [澳门科技大学] [[DOI](https://doi.org/10.3389/fmed.2026.1752778)]
- [*arXiv*] **TCMaster: Confidence-Aware Querying and Workload-Guided Physical Design for Multi-Source Traditional Chinese Medicine Knowledge Graphs** 清华大学、北京中医药大学与广东省中医药省实验室陈峥等提出面向多源中医药知识图谱的置信查询与物理设计方法 TCMaster，整合药典、方剂、分子数据和大模型抽取的微语义，构建约22.1万实体、72.3万条基础边的属性图，并在边上来源置信度约束下重写 Cypher 查询。作者报告在 Neo4j 上的检索加速，以及图谱检索使 TCMbench 问答准确率提高20.0个百分点。规模与结果均为作者自报。 [清华大学，北京中医药大学，广东省中医药省实验室] [[论文](https://arxiv.org/abs/2609.25712)]
- [*Journal of King Saud University - Computer and Information Sciences*] **TCMKG: Knowledge-Grounded question answering in Traditional Chinese Medicine via dynamic prompt evolution framework** TCMKG在新安医案上用专家引导提示抽取实体，建成含37192个实体、130030条关系的中医知识图谱，信息抽取精确率0.89、召回率0.88、F1为0.88。 [Anhui University of Traditional Chinese Medicine，Hefei University] [[DOI](https://doi.org/10.1007/s44443-026-00743-1)]
- [*Digital Chinese Medicine*] **TCM-HyperRAG** 用高阶知识超图增强中医疾病诊断和处方推荐，并把可追溯证据交给骨干大模型 [[DOI](https://doi.org/10.1016/j.dcmed.2026.08.004)]
- [*Frontiers in Medicine*] **TCM-DiffRAG** 通用知识图谱 + 个性化知识图谱 + CoT 的辨证推理 RAG 框架 [Guangdong Institute of Intelligence Science and Technology, Zhuhai，Hangzhou Ganzhicao Technology Co., Ltd，BoardWare Information System Limited] [[正式发表](https://doi.org/10.3389/fmed.2026.1804478)] [[论文](https://arxiv.org/abs/2602.22828)] [[代码](https://github.com/LiJianmin6706/Tcm_Diff_RAG)]
- [*Frontiers in Pharmacology*] **TCM-CoT-RAG** 面向中医风湿病临床决策的检索增强系统，用思维链约束专家式推理，降低大模型幻觉 [[DOI](https://doi.org/10.3389/fphar.2026.1884526)]
- [*Neural Networks*] **LLM-SDaT** 把知识注入大模型，用于中医辨证 [浙江大学] [[DOI](https://doi.org/10.1016/j.neunet.2026.108812)]
- [*世界科学技术-中医药现代化*] **KG-IMHRE（赵炳南流派可解释多跳检索增强问答）** 以赵炳南皮肤科流派知识图谱为库，用子图挖掘和动态检索语句引导大模型做可解释多跳问答。流派测试基准上选择题 85.2、问答题 45.78、总分 73.38，问答题专家评分 4.2。 [中国中医科学院中医药信息研究所] [[DOI](https://doi.org/10.11842/wst.20250706001)]
- [*ISBCB 2026*] **GraphRAG-TCM: A Hybrid Retrieval-Augmented Generation System for Traditional Chinese Medicine Clinical Decision Support** Wang、Ren 等在 ISBCB 2026 提出面向中医临床决策支持的混合检索增强系统，结合向量检索、词法检索与知识图谱遍历。篇目与作者信息核验自 Crossref 与 DOI 登记。 [河南工学院，中医药广东省实验室] [[DOI](https://doi.org/10.1145/3820664.3820702)] [[论文](https://dl.acm.org/doi/10.1145/3820664.3820702)]
- [*proceedings-article*] **Construction of a Knowledge Graph for Functional Specification Standards of Traditional Chinese Medicine Information Systems Based on Large Language Models** 作者以中医药信息学会22份中医信息系统功能规范团体标准为语料，用CRISPE框架约束提示，让DeepSeek抽取实体和关系并加规则约束来建知识图谱。 [Hubei University of Chinese Medicine] [[DOI](https://doi.org/10.1145/3833450.3833480)]
- [*International Conference on Optics, Electronics, and Communication Engineering (*] **A knowledge-enhanced prescription generation model for TCM syndrome differentiation via multilevel memory retrieval** 该处方生成模型用加权BM25检索相似病例，并接入《本草纲目》药物知识图谱以及十八反、十八畏，再把检索结果交给大语言模型，实验在CCL2025中医基准上进行。 [Chengdu Medical College，First Affiliated Hospital of Chengdu Medical College] [[DOI](https://doi.org/10.1117/12.3123588)]
- [*Journal of Visualized Experiments*] **A Study on An Intelligent Diagnosis and Treatment Assistant System For Acupuncture in Diminished Ovarian Reserve Based on A Knowledge Graph** 作者用大语言模型加人工标注，从82部针灸文献和临床数据中建成含16558个实体、80084条关系的图谱；在90例卵巢储备功能减退患者中，系统辨证与专家的一致率为86.7%。 [Nanjing University of Chinese Medicine，Xuzhou Medical College，Nanjing General Hospital of Nanjing Military Command，Nanjing University] [[DOI](https://doi.org/10.3791/71182)]

</details>

<details>
<summary>2025 · 31</summary>

- [*Journal of Translational Medicine*] **DHerbKB：面向慢性肾脏病饮食管理与毒性中药控制的知识库** Wang、Yuan 通讯、Chen 通讯等构建 DHerbKB，整合慢性肾脏病饮食原则与毒性中药信息，并提供在线推荐系统。纳入 8,725 种食物营养数据和多类毒性中药条目。128 次非专业用户评估为作者自报的可用性检查。系统地址为 https://dherbkb.hywanglab.org.cn/。许可为 CC BY-NC-ND 4.0。 [北京中医药大学王琦书院、国家中医体质与治未病研究院，北京中医药大学中医学院，南京中医药大学人工智能与信息技术学院，河海大学计算机与软件学院，中国中医科学院中药研究所，北京大学第一医院肾内科，浙江中医药大学附属宁波市中医院，香港大学玛丽医院肾脏科] [[DOI](https://doi.org/10.1186/s12967-025-07178-8)] [[论文](https://translational-medicine.biomedcentral.com/articles/10.1186/s12967-025-07178-8)] [[系统](https://dherbkb.hywanglab.org.cn/)]
- [*上海中医药杂志*] **融合大语言模型与知识图谱的抑郁症中西医结合智能问答系统** 谭平、刘惠娜通讯、韦昌法通讯。发表于《上海中医药杂志》2025 年 59 卷第 7 期的方法论文，把《抑郁症中西医结合诊疗指南》做成 303 个实体、436 条关系的 Neo4j 知识图谱，再用模板匹配与 ChatGLM4 生成可溯源回答。20 道问题的 5 位专家总体评分为模板匹配 64.25、单独 ChatGLM4 80.25、融合系统 83.63。32 例门诊展示为定性描述，文中没有开放代码或图谱。官方期刊 PDF 可下载，未见印刷 Creative Commons 许可。 [湖南中医药大学信息科学与工程学院，湖南中医药大学医学院，湖南省智慧中医工程技术研究中心] [[DOI](https://doi.org/10.16305/j.1007-1334.2025.z20240925004)] [[论文](https://shzyyzz.shzyyzz.com/zh/article/doi/10.16305/j.1007-1334.2025.z20240925004/)]
- [*世界科学技术-中医药现代化*] **阿尔茨海默病指南知识库问答（ChatGLM3）** 用 LangChain 把 ChatGLM3-6B 接到本地库，库含中国中西医结合学会、中华医学会认证的阿尔茨海默病诊疗指南、规范和教科书。相对裸 ChatGLM3-6B，事实准确性 Win 88.09%、完整性 Win 85.71%。 [湖南中医药大学信息科学与工程学院] [[DOI](https://doi.org/10.11842/wst.20240329007)]
- [*世界科学技术-中医药现代化*] **监督微调结合检索增强的中医知识问答** 以 ChatGLM3 为基座，用 PissA 做监督微调并接 RAG。文中模型 BLEU 14.5830、ROUGE-1 34.6730；接入 RAG 后中医题库推理 F 值 0.6398，高于 ChatGLM3 基线 0.2654。 [南京中医药大学人工智能与信息技术学院，南京大学信息管理学院，江苏省中医流派研究院] [[DOI](https://doi.org/10.11842/wst.20241121002)]
- [*Journal of Pharmaceutical Analysis*] **可解释图神经网络量化中药配伍** 在中医药多维知识图谱上，用可解释图神经网络量化配伍。图谱把术语和饮片连起来，药性作为虚拟节点；在 6080 首方上评估饮片在方中的作用，并用 215 首新冠相关方做验证。 [[DOI](https://doi.org/10.1016/j.jpha.2025.101342)] [[arXiv](https://arxiv.org/abs/2411.11474)]
- [*IEEE ICCBDAI 2025*] **动态知识图谱与大模型的中医生理建模** 把动态知识图谱接进大模型，补中医生理知识覆盖不足和更新成本高的问题 [北京科技大学] [[DOI](https://doi.org/10.1109/iccbdai66607.2025.11388184)]
- [*IEEE BIBM 2025*] **中成药知识体系构建** LLM+知识图谱构建中成药知识体系 [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356149)]
- [*CCIS*] **中医问诊中的大模型与知识图谱** 以中医问诊为例，把大语言模型和知识图谱结合起来 [天津大学，天津中医药大学] [[DOI](https://doi.org/10.1007/978-981-96-1809-5_28)]
- [*CCIS*] **中医药知识图谱问答系统** 把中医药知识图谱和大语言模型接成智能问答系统 [[DOI](https://doi.org/10.1007/978-981-96-1809-5_26)]
- [*数据分析与知识发现*] **中医药标准知识问答系统** 检索增强技术构建中医药标准知识问答系统的探索与实践 [中国中医科学院等] [[DOI](https://doi.org/10.11925/infotech.2096-3467.2024.0747)]
- [*Frontiers in Medicine*] **中医医案问答系统** 融合大语言模型与知识图谱的中医医案问答系统，提升医案检索与分析效率（Frontiers in Medicine 2025） [安徽中医药大学] [[DOI](https://doi.org/10.3389/fmed.2024.1512329)]
- [*JMIR Medical Informatics*] **Yaoshi-RAG（药食同源RAG）** 基于不确定知识图谱的药食同源膳食推荐RAG，提升LLM个性化与可解释性 [[DOI](https://doi.org/10.2196/75279)]
- [*Frontiers in Pharmacology*] **TCMRD-KG** 基于古籍文献的风湿病中医知识图谱创新设计 [北京中医药大学] [[DOI](https://doi.org/10.3389/fphar.2025.1535596)]
- [*Digital Chinese Medicine*] **TCMLCM** 基于KG2TRAG的中医肺癌智能问答模型 [南京中医药大学] [[DOI](https://doi.org/10.1016/j.dcmed.2025.03.011)]
- [*Journal of Pharmaceutical Analysis*] **TCMKD 中医药知识发现平台** 手工校对后汇集证候、方剂、中成药、药材、成分、靶点和疾病。平台提供挖掘、富集和网络定位分析。 [[DOI](https://doi.org/10.1016/j.jpha.2025.101297)] [[网站](https://cbcb.cdutcm.edu.cn/TCMKD/)]
- **TCM-Sage** 面向中医师的证据合成RAG助手（混合向量+知识图谱） [[代码](https://github.com/AndyZHENG0715/TCM-Sage)]
- [*proceedings-article*] **Smart Virtual Patients for TCM: Combining Knowledge Graphs and Language Models** 该中医虚拟病人把大语言模型和知识图谱与束搜索、Sentence-BERT剪枝结合，症状一致性53.2%、召回率62.5%，均高于提示加知识图谱的基线。 [Universiti Sains Malaysia，Sultan Qaboos University] [[DOI](https://doi.org/10.1109/icitda68167.2025.11332301)]
- [*IEEE International Conference on Electrical, Automation and Computer Engineering*] **Research on the Organization and Application of Traditional Chinese Medicine Processing Knowledge in Lingnan Herbal Medicine Ancient Texts by Integrating Large Models and Knowledge Graph Technology** 作者用大语言模型和知识图谱整理岭南本草古籍中的药材、炮制方法、辅料和功效，在Neo4j中建图，并结合BERT-CAN-NER与大模型生成做自然语言问答。 [Guangzhou University of Chinese Medicine] [[DOI](https://doi.org/10.1109/iceace67491.2025.11439512)]
- [*proceedings-article*] **Research on the Construction of a Traditional Chinese Medicine Coronary Heart Disease Question-Answering System Integrating Large Language Models and Knowledge Graphs** 作者用提示引导大语言模型从近十年8部冠心病中医或中西医结合指南中抽取实体和关系，建成含452个节点、690条关系的知识图谱，并以BERT+CNN做最优意图识别。 [China Academy of Chinese Medical Sciences，Tongji University] [[DOI](https://doi.org/10.1145/3777577.3777709)]
- [*Pharmacological Research*] **RAG-CPMF** 多LLM校验+RAG的中成药智能推荐框架，并发布持续更新的大规模中成药公开数据集 [[DOI](https://doi.org/10.1016/j.phrs.2025.107883)] [[数据](https://gitee.com/tcmdoc/cpm)]
- [*arXiv*] **OpenTCM** 基于 GraphRAG 的中医知识检索与诊断系统，含妇科古籍知识图谱 [[论文](https://arxiv.org/abs/2504.20118)] [[代码](https://github.com/OpenTCM01/OpenTCM)]
- [*proceedings-article*] **Method for Constructing TCM Syndrome Differentiation Q&A System with LLM-RAG** 该中医辨证问答框架把整理过的中医知识库通过结构化检索接到大语言模型上，以提高回答的事实准确性、语境精度和专业性。 [Baoshan University] [[DOI](https://doi.org/10.1145/3784013.3784061)]
- [*IEEE BIBM*] **MRD-RAG** 模拟临床推理的多轮诊断RAG框架，并构建覆盖中西医的**DiagnosGraph**（876病/7997节点/37201三元组） [香港科技大学] [[正式发表](https://doi.org/10.1109/bibm66473.2025.11357107)] [[论文](https://arxiv.org/abs/2504.07724)]
- [*Interdisciplinary Sciences*] **LLM驱动中医知识图谱构建** LLM驱动的中医知识图谱构建与应用 [河南工业大学] [[DOI](https://doi.org/10.1007/s12539-025-00735-1)]
- [*Journal of Medical and Biological Engineering*] **LLM+RAG中医推理** LLM与RAG结合的中医推理方法 [台北市立联合医院] [[DOI](https://doi.org/10.1007/s40846-025-00988-7)]
- [*International Conference on e-Education, e-Business, e-Management and e-Learning*] **Knowledge Graphs Combined with ChatGPT in the Field of Acupuncture: A Case Study on the Treatment of Depression** 该研究把针灸原理做成抑郁症知识图谱，并用大语言模型优化知识整合，供研究者和临床医生使用。 [Nanjing University，Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1109/ic4e65071.2025.11075342)]
- [*International Conference on Biomedical and Intelligent Systems*] **Jiezhai Gong 妇产科医案知识图谱** 用 Neo4j 构建 Jiezhai Gong 妇产科医案知识图谱。 [[DOI](https://doi.org/10.1145/3745034.3745089)]
- [*Proceedings of the 2nd International Conference on Machine Learning and Automation, CONF-M*] **Chinese Medicine Question Answering Robot Based on RAG and Self-Built Dataset** 用检索增强生成和自建数据集构建中医问答机器人。 [大连理工大学，西安电子科技大学] [[DOI](https://doi.org/10.4108/eai.21-11-2024.2354617)]
- [*计算机工程与应用*] **ChatTCM（苑中旭等）：融合思维链与知识图谱的中医问答模型** 苑中旭等提出将大模型微调与中医书籍三元组知识图谱、思维链动态交互结合的中医问答方法 ChatTCM；与目录既有的 SylvanL/ChatTCM 权重不是同一条目。文中 BLEU/ROUGE 与准确率为作者自报。 [西南科技大学，中国科学技术大学] [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2408-0101)] [[论文](http://cea.ceaj.org/CN/10.3778/j.issn.1002-8331.2408-0101)]
- [*JAMIA*] **AcuKG** 用实体识别、关系抽取和本体映射，把针灸指南、文献和临床试验整理成知识图谱 [中国中医科学院] [[DOI](https://doi.org/10.1093/jamia/ocaf179)]
- [*Communications in Computer and Information Science Health Information Processing. Evaluati*] **A TCM Syndrome Differentiation Thinking Method Based on Chain of Thought and Knowledge Retrieval Augmentation** CotKE-TCM 用思维链提示，并检索相似医案、模型生成的中医知识和临床经验，辅助大模型做辨证；在 CHIP 2024 评测集上测试。 [之江实验室，上海理工大学，ANTA Group] [[DOI](https://doi.org/10.1007/978-981-96-4298-4_3)]

</details>

<details>
<summary>2024 · 15</summary>

- [*上海中医药杂志*] **基于 GPTs 的中医知识图谱实体和关系抽取研究** 何宇浩、李明通讯等。发表于《上海中医药杂志》2024 年 58 卷第 8 期的方法论文，用 ChatGPT 4.0 的自定义 GPTs 从《中华医方》351 首方剂抽取实体与关系并导入 neo4j，再与基于 bert-Chinese 的 CasRel、GPLinker 比较。GPTs 总计 P、R、F1 为 97.44%、98.09%、97.48%。实验由海外合作者完成，未见开放 GPTs、提示词或标注数据。正式本为 58(8):1–6，DOI 10.16305/j.1007-1334.2024.2401070。官方期刊 PDF 可下载，未见印刷 Creative Commons 许可。 [上海中医药大学，佩珀代因大学] [[DOI](https://doi.org/10.16305/j.1007-1334.2024.2401070)] [[论文](https://shzyyzz.shzyyzz.com/zh/article/doi/10.16305/j.1007-1334.2024.2401070/)]
- [*中国数字医学*] **循证中医指南 PICO 知识图谱问答** 崔唐明、孙美玲、孙华君、李海燕以多囊卵巢综合征指南为例，用文心一言抽取 PICO 知识，Neo4j 存成 13 类、248 节点、337 条关系的指南图谱，并预设 12 类临床问题、24 个问句模板。2024 年第 19 卷第 5 期 20–27 页。 [中国中医科学院中医药信息研究所] [[论文](https://www.zgszyx.org.cn/CN/Y2024/V19/I5/20)]
- [*IEEE BIBM 2024*] **名老中医针灸医案知识图谱** 用大模型做信息抽取，构建名老中医针灸医案知识图谱 [中国中医科学院] [[DOI](https://doi.org/10.1109/bibm62325.2024.10821904)]
- [*JMIR Medical Informatics*] **中医领域知识图谱补全** 中医领域知识图谱补全与质量评估研究 [Zhejiang Chinese Medical University，Guangdong Provincial Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2196/55090)]
- [*南京中医药大学学报*] **中医药问答大语言模型** RAG 结合 P-Tuning v2 微调的中医药问答大模型（ChatGLM2-6B） [南京中医药大学] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1375)]
- [*计算机科学与探索*] **中医药大模型知识增强方法** 面向中医药大模型的知识增强方法，基于约十万首经典方剂构建图谱并保持方剂结构性 [天津大学] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2407082)]
- [*Methods of Information in Medicine*] **TCMSF** 中医证候古籍知识图谱构建框架 TCMSF，将古籍中的证候知识系统化组织并语义关联，为中医信息化提供基础（Methods of Information in Medicine 2024） [中国中医科学院] [[DOI](https://doi.org/10.1055/a-2590-6348)]
- [*IEEE International Conference on Medical Artificial Intelligence (MedAI)*] **TCMRD-KG: Design and Development of a Rheumatism Knowledge Graph Based on Ancient Chinese Literature** TCMRD-KG是首个基于中医古籍痹证内容的知识图谱，实体标注结合了主流大语言模型自动标注和人工复核。 [Beijing University of Chinese Medicine，China Academy of Chinese Medical Sciences，Guang’anmen Hospital，Institute of Basic Theory for Chinese Medicine] [[DOI](https://doi.org/10.1109/medai62885.2024.00083)]
- [*Computational and Structural Biotechnology Journal*] **TCMM 中药现代化统一数据库** 提出一个面向中药现代化和治疗创新的统一数据库。 [[DOI](https://doi.org/10.1016/j.csbj.2024.04.016)]
- [*EIECC*] **TCM MLKG-RAG** 多层知识图谱检索增强生成的中医智能诊断 [University of Science and Technology of China] [[DOI](https://doi.org/10.1109/EIECC64539.2024.10929529)]
- [*OSF Preprints（预印本）*] **RAG 增强中医问答置信度** 检索增强生成提升大模型中医问答置信度（预印本） [[DOI](https://doi.org/10.31219/osf.io/ns2v3)]
- [*arXiv*] **Prompt-RAG: Pioneering Vector Embedding-Free Retrieval-Augmented Generation in Niche Domains, Exemplified by Korean Medicine** Prompt-RAG不使用向量嵌入，在韩医问答聊天机器人上，其相关性和信息量优于ChatGPT以及基于向量嵌入的检索增强生成。 [Gachon University，Stanford Medicine，Stanford University] [[论文](https://arxiv.org/abs/2401.11246)]
- [*Phytomedicine*] **PresRecRF** 把分子知识图谱与大模型抽出的中医语义表示融合，同时预测草药和剂量。代码与数据在 GitHub。 [北京交通大学] [[DOI](https://doi.org/10.1016/j.phymed.2024.156116)] [[代码](https://github.com/2020MEAI/PresRecRF)]
- [*Electronics*] **LLM 构建中医知识图谱** 基于大语言模型的中医知识图谱构建 [同济大学] [[DOI](https://doi.org/10.3390/electronics13071395)]
- [*Database (Oxford)*] **ACUBERT** 针灸适应证知识库的经络实体识别与分类模型 [南京中医药大学，Nanjing KG Data Technology] [[DOI](https://doi.org/10.1093/database/baae083)]

</details>

<details>
<summary>2023 · 5</summary>

- [*Frontiers of Information Technology & Electronic Engineering*] **知识引导的中医荐药（FITEE）** 用典籍和处方抽出的症状–草药知识图谱做图注意力表示，并在预测层加入方剂学信息。 [[DOI](https://doi.org/10.1631/FITEE.2200662)]
- [*IEEE ICIEA*] **温病文献的 BERT 命名实体识别** 用 BERT 识别中医温病文献中的命名实体。 [[DOI](https://doi.org/10.1109/iciea58696.2023.10241595)]
- [*计算机科学与探索*] **大模型融合知识图谱问答系统** LLM 与知识图谱深度融合的中医药方剂垂直领域问答系统 [天津大学] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2308070)]
- [*Computers in Biology and Medicine*] **《伤寒论》问题意图分类（TinyBERT-CNN）** 用 TinyBERT 和卷积神经网络融合，对《伤寒论》里的问题做意图分类。 [[DOI](https://doi.org/10.1016/j.compbiomed.2023.107075)]
- [*世界科学技术-中医药现代化*] **MMKGQA（海洋中药知识图谱问答）** 以细粒度海洋中药图谱 MMKG 为库，用 Aho-Corasick 与 Word2Vec 做实体识别和问题分类，建成 MMKGQA。问卷调查语料上平均精确率 97.93%、召回率 83.41%、F1 89.10%。不是大语言模型系统。 [南京中医药大学人工智能与信息技术学院] [[DOI](https://doi.org/10.11842/wst.20220514002)]

</details>


</details>

<details>
<summary>处方 / 组方（40）：荐药、组方、药对</summary>

<details>
<summary>2026 · 17</summary>

- [*arXiv*] **Development of an HPLC Analytical Method Based on Large Language Models: A Case Study of the Eczema External Wash Formula** 浙江大学龚行楚等以湿疹外洗方为例，提出用人机协同、由大语言模型推荐色谱方案并经实验验证与迭代优化的中药复方HPLC方法开发流程。论文称在五种提示策略中，专家角色设定加结构化推理表现最好；最终方法采用SunShell C18柱和0.1%甲酸水–乙腈梯度，在55分钟内分离7个指标成分，并用LC-MS表征20个成分。配方由防风、黄柏、地肤子、白鲜皮、荆芥、苦参、蛇床子七味组成。本次打开了arXiv摘要页与PDF（2611.20994，2026年11月16日提交）。方法细节与结果均为作者自报。 [Zhejiang University，Tianjin University of Traditional Chinese Medicine，Hangzhou Third People's Hospital，Jinhua Institute of Zhejiang University] [[论文](https://arxiv.org/abs/2611.20994)] [[PDF](https://arxiv.org/pdf/2611.20994)]
- [*arXiv*] **Patient-Conditioned Dual Hypergraph Reasoning** 患者条件化双超图推理实现可审计的中医处方支持，将症状/舌/脉证据围绕证型与治则组织（天津大学） [[论文](https://arxiv.org/abs/2607.04025)]
- [*KSII Transactions on Internet and Information Systems*] **GAT+LLM TCM Prescription Generation** 图注意力网络与LLM结合的中医处方智能生成模型（KSII TIIS正式发表） [[DOI](https://doi.org/10.3837/tiis.2026.05.006)]
- [*Aging and Disease*] **Precious3GPT 用于中药来源抗衰老配方的筛选与设计** Galkin、Ren、Zhavoronkov 通讯。发表于 Aging and Disease 的计算概念验证，用 Precious3GPT 生成的衰老组学签名与 BATMAN-TCM2 交叉，筛选或设计中药抗衰老配方，并公开多智能体流程与数据集。跨物种分析得到 13 个基因和 34 个多组织化合物，华山五子丹含其中 20 个。本文没有对这些配方做实验或临床验证。印刷本三幅图题注与图面错位。许可按 PDF 为 Creative Commons Attribution License。 [Insilico Medicine AI Limited（阿布扎比），Insilico Medicine Hong Kong Ltd.（香港科学园），Insilico Medicine Shanghai Ltd.（上海）] [[DOI](https://doi.org/10.14336/AD.2024.1697)] [[论文](https://www.aginganddisease.org/EN/10.14336/AD.2024.1697)] [[代码](https://github.com/Insilico-org/TCMxPlore)]
- [*世界科学技术-中医药现代化*] **知识蒸馏中医辨证论治模型** 以 GPT-4o 为教师，从中医医案蒸馏辨证论治指令，再对 Qwen2.5-7B 做 LoRA 监督微调。论文报告推理过程更可读，同时保住处方推荐精度。未给独立品牌名，也未见公开权重。 [南京中医药大学人工智能与信息技术学院，南京大学信息管理学院，江苏省中医流派研究院] [[DOI](https://doi.org/10.11842/wst.20250422007)]
- [*arXiv*] **理法方药对齐的中医处方生成** 四阶段对齐处方生成：补可审计的理法方药推理、随证加减，以及十八反等禁忌 [清华大学] [[论文](https://arxiv.org/abs/2609.25755)]
- [*Expert Systems with Applications*] **异构网络预测中药毒性** 用异构网络预测中药毒性。 [[DOI](https://doi.org/10.1016/j.eswa.2025.129969)]
- [*CCIS*] **多阶段学习的中医处方推荐大模型** 用多阶段学习训练面向中医处方推荐的大语言模型 [厦门大学] [[DOI](https://doi.org/10.1007/978-981-92-0291-1_11)]
- [*Evidence-Based Chinese Medicine and Technology Assessment*] **中西药相互作用专论库** 为临床决策支持库整理有证据的中西药相互作用专论。2026 年发表。 [[DOI](https://doi.org/10.26599/ecmta.2026.9570040)] [[网站](https://www.imgateway.net)]
- [*Frontiers in Pharmacology*] **中药复方剂量调整方法** 讨论怎样把经验用药收成可调整的复方剂量，往更精细的用法走。2026 年发表在 Frontiers in Pharmacology。 [[DOI](https://doi.org/10.3389/fphar.2026.1815285)]
- [*Pharmacological Research - Modern Chinese Medicine*] **中药化合物的多监管安全评价机器学习框架** 从 TCMSP、TCMID、PubChem 和 ChEMBL 汇集 24 种药材的 127 个活性成分，用随机森林，并按 FDA、EMA 和 CFDA 的不同侧重点做安全评分。 [[DOI](https://doi.org/10.1016/j.prmcm.2026.100772)]
- [*Zenodo*] **UniTCM** 把方剂和疾病对应到分子层面的反向药理学平台，包含标准化、临床发现、分子分析、系统核对和分析工具五层。 [[代码](https://doi.org/10.5281/zenodo.21711675)] [[网站](https://unitcm.qfxulab.com/)]
- [*Chinese Medicine*] **TCMNet** LLM辅助疾病知识挖掘+PPI网络与结合预测的方剂优化策略 [浙江省中医药研究院] [[DOI](https://doi.org/10.1186/s13020-026-01360-w)]
- [*Current Molecular Pharmacology*] **TCMDATA** 面向靶点的中医网络药理分析和人工智能解读的 R 包。2026 年发表在 Current Molecular Pharmacology。 [[代码](https://github.com/YuLab-SMU/TCMDATA)] [[DOI](https://doi.org/10.1016/j.cmp.2026.09.003)]
- [*Frontiers in Pharmacology*] **MSAT：中药物不良反应预测** 用 FAERS 自发报告训练异构图神经网络，预测中药相关的不良反应。2026 年发表在 Frontiers in Pharmacology。 [[DOI](https://doi.org/10.3389/fphar.2026.1774128)]
- [*Mathematics*] **LLM-Driven Unsupervised Discovery of Semantic Decision Dimensions for Dynamic Scheduling and Intelligent Systems: A Traditional Chinese Medicine Case Study** DeepSeek-V3.2从12163条中药记录、64107个短句中归纳出458个原始标签并合并为22个语义类；Qwen3-Embedding-8B测得19个概念的内部一致性平均超过60%，专家合理性均分4.64（1到5分）。 [Changchun University of Chinese Medicine，Shandong University of Arts，Tsinghua University] [[DOI](https://doi.org/10.3390/math14152681)]
- [*Digital Chinese Medicine*] **CMM-EmbedCluster** 基于LLM与药性理论的中药聚类框架，构建567味药性知识库 [南京中医药大学] [[DOI](https://doi.org/10.1016/j.dcmed.2026.05.010)]

</details>

<details>
<summary>2025 · 11</summary>

- [*IEEE Journal of Biomedical and Health Informatics*] **草药-药物相互作用预测** LLM增强的草药-药物相互作用预测 [深圳大学] [[DOI](https://doi.org/10.1109/jbhi.2025.3558667)]
- [*IEEE BIBM*] **方剂推荐中的剂量预测** 在推荐中药方剂的同时预测剂量，用了扩散模型和异构层次网络。2025 年 IEEE BIBM。 [[DOI](https://doi.org/10.1109/bibm66473.2025.11357222)]
- [*Chinese Medicine*] **强化学习的可解释中医处方推荐** 用强化学习做可解释的中医处方推荐，并把较小语言模型里的隐含偏好用上。2025 年发表在 Chinese Medicine。 [[DOI](https://doi.org/10.1186/s13020-025-01250-7)]
- [*Scientific Reports*] **图注意力网络预测中药相互作用** 用图注意力网络预测中药之间的相互作用，用来提前发现配伍风险。 [[DOI](https://doi.org/10.1038/s41598-025-00725-9)]
- [*arXiv*] **可解释框架量化中医症状–方药对应** 用古代和经典方剂记录训练模型，把症状模式对应到个体化方药这条原则量化，以便和现代生物医学对照。 [[论文](https://arxiv.org/abs/2507.11176)]
- [*IEEE BIBM 2025*] **医学知识增强的双层对齐中药处方推荐** 用医学知识增强的双层对齐网络做中药处方推荐，避免只依赖结构化输入或多阶段流水线 [南京信息工程大学] [[DOI](https://doi.org/10.1109/bibm66473.2025.11356282)]
- [*JMIR Medical Informatics*] **中医方剂分类加权投票** LLM加权投票中医方剂分类方法 [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.2196/69286)]
- [*IEEE International Conference on Bioinformatics and Biomedicine (BIBM)*] **Two-Stage Chain-of-Thought Fine-Tuning for TCM Medication Decision-Making in Nsclc** 针对非小细胞肺癌，两阶段思维链微调在处方生成和中成药推荐上分别比基线提高1.2%和6.1%。 [China Academy of Chinese Medical Sciences，Qinghai Normal University，Chinese Academy of Social Sciences，Institute of Ethnology and Anthropology] [[DOI](https://doi.org/10.1109/bibm66473.2025.11356901)]
- [*IEEE JBHI*] **TEmbed-DDI：中西药相互作用标注** 用大语言模型和双向神经网络做跨域药物相互作用标注，并把中药相互作用纳入评测 [[DOI](https://doi.org/10.1109/jbhi.2025.3563289)]
- [*proceedings-article*] **Dynamic Disease Tracking and Personalized Prescription Recommendation Using Large Language Model in Traditional Chinese Medicine** 该系统把多轮问诊和时间序列分析接进大语言模型以推荐个体化中药处方，并在1000例失眠病例上提高了初诊推断、诊断准确性和系统适应性。 [National Central University，National Taiwan University of Science and Technology，Research Center for Humanities and Social Sciences, Academia Sinica] [[DOI](https://doi.org/10.1109/iccbe65177.2025.11255949)]
- [*IEEE Transactions on Computational Biology and Bioinformatics*] **AN-IHP：注意力网络预测配伍禁忌药对** 用注意力网络预测中药里配伍禁忌的药对。 [[DOI](https://doi.org/10.1109/tcbbio.2024.3498094)]

</details>

<details>
<summary>2024 · 5</summary>

- [*Analytical Chemistry*] **质谱机器学习预测中药毒性** 用质谱和机器学习预测中药毒性。 [[DOI](https://doi.org/10.1021/acs.analchem.4c05311)]
- [*Computer Methods in Biomechanics and Biomedical Engineering*] **复方煎煮时长分类** 按多维特征给中药复方的煎煮时长做分类。2024 年发表。 [[DOI](https://doi.org/10.1080/10255842.2024.2302225)]
- [*IEEE BIBM*] **TCM-FTP** 面向中药处方预测的大模型微调方法 [香港科技大学，北京交通大学，中国中医科学院，河南中医药大学] [[DOI](https://doi.org/10.1109/BIBM62325.2024.10822451)]
- [*JAMIA*] **PresRecST** 按「辨证—立法—荐药」递进推荐中药处方（JAMIA 2024）；配套公开 TCM-Lung 编码子集与 TCM-PD 复现表，代码在 GitHub [北京交通大学，中国中医科学院，河南中医药大学] [[DOI](https://doi.org/10.1093/jamia/ocae066)] [[代码](https://github.com/2020MEAI/PresRecST)]
- [*IEEE International Conference on Computer and Communication Engineering Technolo*] **A Study of Automated Data Mining of Medication Rules in Traditional Chinese Medicine Prescriptions Based on Large Language Model** 作者用大语言模型通过人机问答，对治疗骨质疏松的中药处方做频次、聚类和Apriori关联分析，结果与SPSS人工统计高度相似。 [Jinan University] [[DOI](https://doi.org/10.1109/ccet62233.2024.10837914)]

</details>

<details>
<summary>2023 · 7</summary>

- [*中国药房*] **生成式人工智能 GPT-4 驱动的中药处方生成研究** 陈祺焘、夏丽珍通讯等。发表于《中国药房》2023 年 34 卷第 23 期的短篇方法论文，把药典和《中药学》文本发送给 GPT-4 及联网模型并生成 30 张中药处方，由同院 3 名专家盲评。表 2 平均分为专家共识 3.756、GPT-4 3.622、联网模型 3.501，两两比较均 P＞0.05；图灵测试按 138/270 记为 51.11%。正文中的“训练”不是参数更新或微调。未见代码或处方数据发布，也未见印刷 Creative Commons 许可。 [三明市中西医结合医院药学部] [[DOI](https://doi.org/10.6039/j.issn.1001-0408.2023.23.02)] [[论文](https://journal.china-pharmacy.com/zh/article/doi/10.6039/j.issn.1001-0408.2023.23.02/)]
- [*中国实验方剂学杂志*] **改良 Transformer 的冠心病证候要素诊断与处方模型** 李洪峥、王阶通讯等。发表于《中国实验方剂学杂志》2023 年 29 卷第 1 期的方法论文，以证候要素为中介，用多头注意力、复合词向量和随机失活构建改良 Transformer，在 8030 例王阶医案上训练，并对 100 例真实开方做定性比较。摘要未给出这 100 例的数值准确率；正文引用的 93% 和 96.46% 属于前期工作。Song 等综述曾把卷期误印为 9(1)，正式本为 29(1):148–154。官方期刊 PDF 可下载，未见印刷 Creative Commons 许可。 [中国中医科学院广安门医院，清华大学信息科学技术学院，清华大学深圳国际研究生院，帝国理工学院] [[DOI](https://doi.org/10.13422/j.cnki.syfjx.20221347)] [[论文](https://www.syfjxzz.com/cn/article/doi/10.13422/j.cnki.syfjx.20221347)] [[程序](https://aipresc.xiaobaishiji.com/)]
- [*arXiv*] **深度强化学习的序贯中药治疗规划** 把慢性病的中药治疗看成多次就诊上的序贯决策，用深度强化学习规划后续处方，而不是只给一次方。 [[论文](https://arxiv.org/abs/2304.12828)]
- [*Chinese Medicine*] **喜炎平严重不良事件的投影重要性** 用变量投影重要性分析年龄和中西药联用，对喜炎平注射液不良事件严重程度的影响。2023 年发表在 Chinese Medicine。 [[DOI](https://doi.org/10.1186/s13020-023-00718-8)]
- [*IEEE BIBM*] **中医方剂 LLM 分类** 微调大语言模型并结合提示模板进行中医方剂分类，数据源自中成药国家医保目录等（IEEE BIBM 2023） [Leipzig University，Changchun University of Chinese Medicine，Liaoning Technical University，Sichuan Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385776)]
- [*IEEE Access*] **PreGenerator** 检索与生成方法结合的中医处方推荐模型 [College of Physics, Taiyuan University of Technology, Taiyuan, China，North Automatic Control Technology Institute, Taiyuan, China] [[DOI](https://doi.org/10.1109/ACCESS.2023.3316219)]
- [*IEEE BIBM*] **LLM+GNN 中医处方推荐** 大语言模型与图神经网络结合的中医处方推荐模型 [南京中医药大学] [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385489)]

</details>


</details>

<details>
<summary>抽取 / 编码器（11）：NER、关系抽取、BERT 类编码器</summary>

- [*世界科学技术-中医药现代化*] **杏林-NER (XingLin-NER)** 面向中医临床文本术语多变的问题，用结构化指令和推理式指令做生成式命名实体识别，得到杏林-NER 系列，并用 TCM-BERT 语义相似度作评估。属抽取方法，不是通用领域对话大模型。 [中国中医科学院中医药信息研究所] [[DOI](https://doi.org/10.11842/wst.20250327010)]
- [*Scientific Reports*] **中医命名实体识别的知识蒸馏** 用知识蒸馏做中医命名实体识别，把大模型的识别能力收进更小的模型。2026 年发表在 Scientific Reports。 [[DOI](https://doi.org/10.1038/s41598-026-56313-y)]
- [*Artificial Intelligence in Medicine*] **中医临床命名实体与关系联合识别** 用字符级卷积循环交互网络，同时做中医临床命名实体识别和关系抽取。2026 年发表在 Artificial Intelligence in Medicine。 [[DOI](https://doi.org/10.1016/j.artmed.2026.103372)]
- [*proceedings-article*] **Named Entity Recognition in Traditional Chinese medicine Literature Data for Obesity Based on Large Language Models** 在中医肥胖文献实体识别上，经多轮提示优化的DeepSeek-R1在测试集F1达到0.927。 [Hubei University of Chinese Medicine] [[DOI](https://doi.org/10.1145/3833450.3833478)]
- [*Applied Intelligence*] **KDC-NER** 知识引导数据增强+大模型微调的中医嵌套命名实体识别框架 [江西中医药大学] [[DOI](https://doi.org/10.1007/s10489-026-07095-3)]
- [*npj Digital Medicine*] **补充替代医学文献抽取语言模型** 用于补充替代医学文献数据抽取与偏倚风险评估的语言模型 [兰州大学] [[DOI](https://doi.org/10.1038/s41746-025-01457-w)]
- [*Scientific Reports*] **双通道知识注意力辨证模型** 双通道知识注意力的中医辨证NLP模型，缓解生僻字与术语抽取难题 [[DOI](https://doi.org/10.1038/s41598-025-96404-w)]
- [*Lecture Notes on Data Engineering and Communications Technologies*] **中医药专利关系抽取** 用大语言模型和多样化语义交互抽取中医药专利中的关系 [湖北工业大学] [[DOI](https://doi.org/10.1007/978-3-032-10344-4_1)]
- [*Scientific Reports*] **中医病历嵌套实体识别** 识别中医电子病历里套在一起的实体，比如症状和它所在的部位。2025 年发表在 Scientific Reports。 [[DOI](https://doi.org/10.1038/s41598-025-22283-w)]
- [*Journal of the American Medical Informatics Association*] **LLM 腧穴定位关系抽取** 大语言模型关系抽取案例研究：腧穴定位知识 [中国中医科学院，The University of Texas MD Anderson Cancer Center , Houston, TX 77030] [[DOI](https://doi.org/10.1093/jamia/ocae233)]
- [*Frontiers in Artificial Intelligence*] **Evi-BERT** 中医RCT证据自动抽取的信息抽取模型开发与验证 [北京航空航天大学，北京中医药大学] [[DOI](https://doi.org/10.3389/frai.2024.1454945)]

</details>

<details>
<summary>评测论文（83）：基准和考试；要下载评测集走下面「数据集」</summary>

<details>
<summary>2026 · 47</summary>

- [*arXiv*] **OmniTongue: A Comprehensive MLLM Benchmark for Automated Tongue Diagnosis in Traditional Chinese Medicine** 东北大学徐柳怡、郭云、李树生、张学文、钱一宁、卢安阳等提出面向中医舌诊的多模态大模型评测基准 OmniTongue。论文称其整合1351张经专家核验的舌象与21616条指令对，覆盖16个临床维度、分区标注和66个细粒度标签，用于考察多模态大模型对舌象全局与局部病理特征的理解。作者报告现有多模态大模型仍有明显差距，医学专用模型也未显示稳定的领域优势。代码与数据集页面写明将在后续公开发布。本次打开了arXiv摘要页（2611.22652，2026年11月17日提交）。规模与结果均为作者自报。 [Northeastern University] [[论文](https://arxiv.org/abs/2611.22652)] [[PDF](https://arxiv.org/pdf/2611.22652)]
- [*Frontiers in Digital Health*] **Zhou 等：面向临床落地的中医大语言模型评价思考（Perspective）** Zhou、Wang、Zhang、Bai、Sun、Liu、Li 在 Frontiers in Digital Health 发表 Perspective，指出执业资格考题虽便于评测中医大模型，但不能单独证明其可支持临床推理或改善患者照护。文章讨论知识表征、专业能力覆盖、评测数据完整性、计分方式与中医实践匹配等四类潜在偏倚，并建议把动态临床情景、开放式生成、多模态评测、纵向复测和临床验证结合起来。这是评价框架评论，不是新的基准数据集或临床试验。本次打开了期刊全文页。 [中国中医科学院中医药信息研究所，北京中医药大学东方医院，国家中医药管理局监测统计中心] [[DOI](https://doi.org/10.3389/fdgth.2026.2009170)] [[论文](https://www.frontiersin.org/journals/digital-health/articles/10.3389/fdgth.2026.2009170/full)]
- [*Frontiers in Medicine*] **LEAF：大模型抽取症状后的多目标进化特征选择与可解释中医呼吸系证候辨证基准（Luo 等）** Luo、Ding、Zhang、Miao、Shi 提出 LEAF 两阶段框架，在公开 TCM-SD 基准的 3,253 条记录、14 种呼吸系证候上，先用大模型抽取 35 项来自公开中医来源的症状本体，再比较 NSGA-II、SPEA2、CMOPSO、NSDE 等四种多目标进化算法做可解释特征选择。文中在三种可替换大模型里将 Qwen2.5-14B-Instruct 排在最前，其后为 Phi-4 和中医领域模型扁仓（BianCang）。这是可解释中间表示与算法比较研究，不是临床疗效试验。本次打开了期刊全文页。 [长春中医药大学，长春中医药大学附属医院肺病科] [[DOI](https://doi.org/10.3389/fmed.2026.1990580)] [[论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1990580/full)]
- [*Future Internet (MDPI)*] **RAG+LoRA 中医执照考试推理架构** RAG+LoRA生成式架构，构建台湾中医师执照考试11,476题（2005–2025）数据集，准确率61.0%→89.0%+（Future Internet） [Chung Shan Medical University Hospital，Chung Shan Medical University] [[DOI](https://doi.org/10.3390/fi18060280)]
- [*Scientific Data*] **辨证论治大模型基准数据集** Scientific Data发布的辨证论治基准，用来评估大模型在中医个体化、整体性临床任务上的能力 [中国中医科学院，中国科学院，天津大学] [[DOI](https://doi.org/10.1038/s41597-026-07587-4)]
- [*arXiv*] **证伪导向的可审计辨证协议** 在公开TCMEval-SDT的200例辨证上，用与具体模型无关的证伪协议约束可审计决策，强调输出纪律而不只是换更大的模型 [[论文](https://arxiv.org/abs/2610.18298)]
- [*Frontiers in Plant Science*] **药用植物多模态大模型评测** 多模态LLM药用植物识别系统评测 [绍兴文理学院] [[DOI](https://doi.org/10.3389/fpls.2026.1765281)]
- [*Frontiers in Medical Technology*] **胸痹/冠心病的中西医数据治理** 以胸痹（冠心病）为例，按 HL7 FHIR 和 SNOMED CT 建了 9 个子集、352 个数据元，其中 42.6% 是中医专用。触发引擎有 128 条规则。前瞻对照纳入 972 人。 [[DOI](https://doi.org/10.3389/fmedt.2026.1759773)]
- [*Digital Chinese Medicine*] **知识图谱增强的长尾证候辨证** 用知识图谱增强长尾学习，做中医证候辨证。 [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.005)]
- [*Journal of Evidence-Based Medicine*] **中医证候诊断标准适用性评价指南** 用德尔菲法给出证候诊断标准的适用性评价指南，共 5 个域、25 条：可获得性、可读性、可实施性、可接受性和总评。每条按 5 点量表打分。 [[DOI](https://doi.org/10.1111/jebm.70153)]
- [*Journal of Evidence-Based Medicine*] **中医考题大/轻量模型对比** 大规模与轻量级LLM中医考题系统对比 [河南大学第一附属医院] [[DOI](https://doi.org/10.1111/jebm.70118)]
- [*Journal of Traditional Chinese Medical Sciences*] **中医智能预问诊临床评估** LLM智能预问诊系统三甲医院临床评估，采用医-AI-患三元模式 [北京中医医院] [[DOI](https://doi.org/10.1016/j.jtcms.2026.06.002)]
- [*Frontiers in Medicine*] **中医教育AI导师评估** 跨认知层级的多模态LLM中医教育评估 [北京中医药大学] [[DOI](https://doi.org/10.3389/fmed.2026.1893231)]
- [*Scientific Reports*] **中医执业考试三模型评估** Gemini等3个LLM在中医国家执业医师考试上的系统评估 [上海交通大学] [[DOI](https://doi.org/10.1038/s41598-026-49200-z)]
- [*Guidelines and Standards of Chinese Medicine*] **中医大模型临床实践评测方法** 针对现有医学大模型评测以西医范式为主、缺少中医专用标准的问题，构建面向临床实践的中医大模型评测方法 [中国中医科学院] [[DOI](https://doi.org/10.1097/gscm.0000000000000123)]
- [*npj Digital Medicine*] **中医场景中医疗大模型的提示词效应** 在中医任务上评估16个大模型，说明提示词效应随模型而变，制约医疗大模型在中医场景的稳定部署 [长庚纪念医院，阳明交通大学，长庚大学] [[DOI](https://doi.org/10.1038/s41746-026-03397-5)]
- [*JMIR Formative Research*] **中医临床决策5-LLM对比** 5个LLM中医临床决策能力对比研究 [南京中医药大学] [[DOI](https://doi.org/10.2196/80167)]
- [*arXiv*] **TongueDx2** 舌诊深度学习设计空间系统消融研究（20+模型版本），含5109图像/976专家标注 [[论文](https://arxiv.org/abs/2607.28148)]
- [*arXiv*] **TCMQA** 论文报告38,279题和101名执业医师；当前HF数据卡为qa 33,872题、医师标注5,250题（102名医师、15,151次作答）。两个配置不可直接相加为独立题数，使用时需固定公开版本。CC BY-NC-SA 4.0。 [[论文](https://arxiv.org/abs/2609.33014)] [[数据集](https://huggingface.co/datasets/TechTCM/TCMQA)]
- [*Frontiers in Artificial Intelligence*] **TCMI-F-6D** 中医信息学跨学科基础能力六维基准 [安徽中医药大学] [[DOI](https://doi.org/10.3389/frai.2026.1780967)] [[代码](https://github.com/123adf-dev/TCMI-F-6D-Benchmark)]
- [*arXiv*] **TCMClinicalReason-Bench** 用2000份多中心电子病历，检验模型能否按病例证据完成从病因病机、证候、治则到处方的推理 [南京中医药大学] [[论文](https://arxiv.org/abs/2610.04215)]
- [*ICIC 2026*] **TCMBenchEval** 基于真实临床医案的LLM中医评测基准 [汕头大学] [[DOI](https://doi.org/10.1007/978-981-92-3498-1_1)]
- [*WISE 2025*] **TCM-Eval (WISE 2025)** 天津大学、天津大学福州国际联合学院、天津中医药大学及其第一附属医院、天津大学国际工程师学院合作的多维中医评测框架；与智明堂TCM-Eval（arXiv 2511.07148）同名但为不同工作 [天津大学，天津大学福州国际联合学院，天津中医药大学，天津中医药大学第一附属医院，天津大学国际工程师学院] [[DOI](https://doi.org/10.1007/978-981-95-7251-9_15)]
- [*Scientific Data*] **TCM-BEST4SDT** 600 条评测样本：300 条辨证论治病例，以及中医基础知识、医学伦理和内容安全各 100 题；涵盖 27 个评价维度。 [[DOI](https://doi.org/10.6084/m9.figshare.30615956)] [[论文](https://arxiv.org/abs/2512.02816)] [[代码](https://github.com/DYJG-research/TCM-BEST4SDT)] [[正式发表](https://doi.org/10.1038/s41597-026-07587-4)]
- [*Communications Medicine*] **TCM-3CEval** 中医大模型三轴评测（核心知识、经典理解、临床决策） [[论文](https://arxiv.org/abs/2503.07041)] [[正式发表](https://doi.org/10.1038/s43856-026-01631-5)]
- [*Frontiers in Medicine*] **Supporting postgraduate exam preparation with large language models: implications for traditional Chinese medicine education** 在2023年中医考研题上，文心一言准确率50.30%、ChatGLM为46.67%，两者都超过及格线，医学人文模块得分最高。 [Beijing University of Chinese Medicine，Dongzhimen Hospital Affiliated to Beijing University of Chinese Medicine，Changchun University of Chinese Medicine，Leipzig University] [[DOI](https://doi.org/10.3389/fmed.2025.1667104)]
- [*JMIR*] **STC-NF：中医症状术语两段式规范化** 针对一条原文对应多个症状、缺少行业标准术语的问题，先把症状拆成 12 类细粒度语义，再用三个命名实体识别模型做两段式规范化，拼回标准术语。数据来自电子病历。 [[DOI](https://doi.org/10.2196/85825)]
- **Med-Bench-Arena** 面向医学与中医药LLM/Agent的开源评测平台，支持HF/vLLM/LiteLLM、多模态与中医特色指标（ZhongJing团队） [[代码](https://github.com/pariskang/Med-Bench-Arena)]
- [*Scientific Data*] **MTCMB** 中医多任务评测基准，12 个数据集、7,100 个样本，覆盖知识、推理、方剂与安全任务（Scientific Data 2026）。 [[论文](https://arxiv.org/abs/2506.01252)] [[代码](https://github.com/Wayyuanyuan/MTCMB)] [[正式发表](https://doi.org/10.1038/s41597-026-07967-w)]
- [*arXiv*] **MMIR-TCM** 记忆增强的多模态舌诊与临床决策框架，提出 MedTCM 数据集与 TDEU 评测指标 [[论文](https://arxiv.org/abs/2607.01814)]
- [*arXiv*] **LingLanMedBench（灵兰）** LingLanMedBench（原 LingLanMiDian）：5 大域、13 个子任务，共 25,620 条专家核验样本；每个子任务从完整集内选取 400 条构成 Hard 子集。 [北京交通大学等] [[论文](https://arxiv.org/abs/2602.01779v2)] [[代码](https://github.com/TCMAI-BJTU/LingLan)] [[网站](http://tcmnlp.com)]
- [*arXiv*] **Learning from Expert-Corrected Misdiagnoses: A Self-Evolving Consultation Agent for Traditional Chinese Medicine after Failed Treatment** 提出误治后再诊互动基准 TCM-MisDx（820例）与自我演化问诊智能体 TCM-SEA；作者报告在封闭测试集上综合分由61.8提升至65.5，治疗惯性率有所下降。文中指标均为作者自报，未见独立数据集下载入口。 [中国中医科学院实验研究中心，北京科技大学] [[论文](https://arxiv.org/abs/2610.40663)]
- [*Brain Behavior and Immunity Integrative*] **Large language models vs traditional Chinese medicine clinical reasoning: Analysis of a single migraine case study** 在一份标准化偏头痛病例上，9个大语言模型与两名中医师及已发表病例对照作答，32名专家盲评；GPT o3、Qwen 3和Gemini 2.5 Pro在部分维度上不低于对照，Aya Expanse 32B得分更低。 [Harvard University，Massachusetts General Hospital] [[DOI](https://doi.org/10.1016/j.bbii.2026.100192)]
- [*arXiv*] **Large Language Models Versus Physicians in Traditional Chinese Medicine: A Real-World Clinical Case Evaluation** 作者收集62家医院349例脱敏门诊病例，用其中60例比较16个大语言模型和60名执业中医师，并由5名资深中医专家按9个诊疗维度盲评。 [University of Missouri，Seventh People's Hospital of Shanghai，Yunnan University of Traditional Chinese Medicine，Northwestern University] [[论文](https://arxiv.org/abs/2609.17544)]
- [*JMIR Formative Research*] **Korean Medical Consultation With Open-Weight Large Language Models: Pilot Comparative Evaluation of Retrieval-Augmented Generation With Metadata Filtering** 用开源权重大模型和检索增强做韩医问诊聊天机器人，并比较带元数据过滤的检索增强效果。 [[DOI](https://doi.org/10.2196/72604)]
- [*Frontiers in Medicine*] **Knowledge-guided adaptive educational support for traditional Chinese medicine using large language models and knowledge graphs: integrating Confucian educational principles** 该智能中医辅导系统把大语言模型接到由《医宗金鉴》构建的知识图谱上；125名学生志愿者中102份问卷纳入分析，集成系统的即时后测成绩高于纯大语言模型组和自学组。 [Anhui University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1943401)]
- [*AI Engineering*] **Knowledge of Chatbots on Oriental Medicine-Based Theory and Practice of Acupuncture Is Inferior to That on Western Medicine-Based Acupuncture-Transmitted Infections** 用 2528 道东方医学针灸理论与操作题、100 道针灸相关感染题，比较五个免费聊天机器人（ChatGPT、Claude、Copilot、Gemini、Perplexity）和三个订阅版（ChatGPT、Claude、Perplexity）。针灸理论中位分 75%，低于感染题的 86%。 [National Chung Hsing University，Tung Wah College，The University of Hong Kong，Fuke Fengze Chinese Medicine Clinic] [[DOI](https://doi.org/10.53941/aieng.2026.100004)]
- [*medRxiv*] **KampoBench** 医师修订的汉方问诊基准：74个问诊场景、310条对话级评分标准，评的是问诊应用而不是考试得分 [[DOI](https://doi.org/10.64898/2026.10.07.26365005)]
- [*ICIC 2026*] **GraphRAG or Fine-Tuning? Evaluating Knowledge Integration via Manually Extracted Graphs in Traditional Chinese Medicine** Tong、Lin、Cai 在 ICIC 2026（LNCS）比较基于人工抽取中医知识图谱的 GraphRAG 与微调，评估知识注入效果。篇目、作者与 2026年7月15日在线出版信息核验自 Crossref。 [[DOI](https://doi.org/10.1007/978-981-92-3495-0_22)] [[论文](https://link.springer.com/10.1007/978-981-92-3495-0_22)]
- [*arXiv*] **Fu-TCM: a multimodal large language model that learns traditional Chinese medicine diagnostic reasoning** 介绍 Fu-TCM 的多模态辨证推理框架与 Bianzheng-Grounded Policy Optimization；作者报告 27B 模型在六个中医文本、视觉与辨证基准上取得最高宏平均准确率。文中自建的 Fu-bianzheng 等评测集未见独立公开下载入口。 [复旦大学，福建中医药大学附属人民医院] [[论文](https://arxiv.org/abs/2610.38333)]
- [*Terminology International Journal of Theoretical and Applied Issues in Specializ*] **From readable to executable** 作者用同一套三种提示，让ChatGPT-4o检验世界卫生组织2007年和2022年中医术语标准是否给出了足够明确的信息，以便在并存的英译变体中做可审计的选择。 [University of Malaya] [[DOI](https://doi.org/10.1075/term.00097.yu)]
- [*proceedings-article*] **Evaluating Semantic Fidelity and Cohesion in NMT and LLM-based Translation of Traditional Chinese Medicine Classics** 在中医经典英译上，以BERTScore对照人工参考译文，DeepSeek的语义保真高于Google Translate和ChatGPT-5，而ChatGPT-5的句间语义连贯更好。 [Northwestern Polytechnical University，Air Force Engineering University] [[DOI](https://doi.org/10.1109/icnlp69856.2026.11528039)]
- [*Current Bioinformatics*] **Evaluating Large Language Models for Query Refinement in Systematic Review Retrieval of Traditional Chinese Medicine** 作者用GPT-4o、GPT-5、DeepSeek-V3和DeepSeek-R1、六种提示，在知网、万方、PubMed和Embase上检索银屑病、新冠肺炎和2型糖尿病文献；去重后的金标准集有182条记录（分别为50、74和58条）。 [China Academy of Chinese Medical Sciences，Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2174/0115748936492177260915061800)]
- [*Expert Systems with Applications*] **DCB（中医动态临床基准）** 从 205 个临床病例构建医患对话，加入误导性症状或诊断信息，评测问诊、辨证、处方与分析任务。 [华东师范大学] [[DOI](https://doi.org/10.1016/j.eswa.2026.132267)]
- [*JMIR Formative Research*] **ChatGPT、DeepSeek与医师针灸方案对照** 比较ChatGPT、DeepSeek和医师生成的针灸治疗方案 [[DOI](https://doi.org/10.2196/95851)]
- [*arXiv*] **AcupunctureBench** 东北大学谭文军等提出面向针灸领域的多模态大模型评测基准，覆盖文本、图像和视频，含58,526道题目与1,216条视频样本，并评测14个大语言模型、14个多模态大模型和4个视频基础模型。论文称另有专用评测网站。文中规模与结果均为作者自报；匿名Hugging Face仓库为手动门禁且无数据卡，本次未作为独立公开数据集收录。 [东北大学，天津中医药大学，广东工业大学，哈尔滨工业大学（深圳）] [[论文](https://arxiv.org/abs/2611.05399)] [[评测](https://acupunctureeval.daytime001.xin)]
- [*Pattern Recognition*] **ATCMD-Bench** 首个Agentic中医诊断基准，通过多智能体模拟问诊评估LLM诊疗能力 [华南理工大学] [[DOI](https://doi.org/10.1016/j.patcog.2026.113679)]

</details>

<details>
<summary>2025 · 19</summary>

- [*Expert Systems with Applications*] **针灸大模型驯化与生成评估 (Taming LLMs for Acupuncture)** 面向针灸推拿诊断的大模型驯化方法，并在语义相似度层面评估生成质量 [[DOI](https://doi.org/10.1016/j.eswa.2024.125920)]
- [*JMIR Medical Informatics*] **辨证思维评测 (Syndrome Differentiation Thinking)** 评估并提升大语言模型中医辨证思维能力的方法开发研究 [[DOI](https://doi.org/10.2196/75103)]
- [*Bulletin of the World Health Organization*] **国际疾病分类与传统医学数据缺口** 讨论国际疾病分类体系里传统医学数据仍然缺失的问题。 [[DOI](https://doi.org/10.2471/blt.25.293540)]
- [*BMC Medical Informatics and Decision Making*] **中医症状的细粒度实体与关系抽取** 针对病历里半结构化、会嵌套的症状描述，做细粒度症状实体和关系抽取，避免粗标注把信息丢掉。 [[DOI](https://doi.org/10.1186/s12911-025-03257-4)]
- [*UbiComp Companion 2025*] **中医大模型误导信息检测评测** 评估大语言模型的中医知识表现与误导信息检测能力。 [清华大学] [[DOI](https://doi.org/10.1145/3714394.3756275)]
- [*JMIR Formative Research*] **中医卒中LLM评测** 中医卒中领域LLM定量基准研究 [成都中医药大学] [[DOI](https://doi.org/10.2196/81545)]
- [*Frontiers in Pharmacology*] **中医临床指南遵循评估** LLM遵循中医临床实践指南的内容分析评估 [兰州大学] [[DOI](https://doi.org/10.3389/fphar.2025.1649041)]
- [*CCL 2025*] **TCM-TBOSD 辨证论治评测** CCL 2025 评测任务。齐鲁工业大学（山东省科学院）与山东中医药大学附属医院用脱敏病历做成 TCM-TBOSD，1500 条，覆盖 10 种证型、4 种疾病、381 味药。处方字段是药名列表，论文写明不包括剂量。仓库有基线代码和数据使用保密承诺书，病例表没有直接放在文件列表里。 [齐鲁工业大学（山东省科学院），山东中医药大学附属医院] [[论文](https://aclanthology.org/2025.ccl-2.45/)] [[PDF](https://aclanthology.org/2025.ccl-2.45.pdf)] [[代码](https://github.com/QLU-NLP/TCM-Syndrome-and-Disease-Differentiation-and-Prescription-Recommendation)]
- [*NeurIPS 2025*] **TCM-Ladder** 中医多模态问答基准，含 52,169 个问答对，并包含图像、音频和视频数据（NeurIPS 2025）。 [[论文](https://arxiv.org/abs/2505.24063)] [[代码](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[榜单](https://tcmladder.com)] [[正式发表](https://proceedings.neurips.cc/paper_files/paper/2025/file/cbdd26a4490f5a8dad0d732508714029-Paper-Datasets_and_Benchmarks_Track.pdf)]
- [*arXiv*] **TCM-5CEval** 五维中医评测，含来自 30 门课程的 2,260 道题；对选择题进行选项循环置换，以检验回答对选项位置的敏感性。 [[论文](https://arxiv.org/abs/2511.13169)]
- [*npj Digital Medicine*] **TCM LLM针灸诊疗能力评估** 7个通用LLM与执业针灸师对照的真实病例评估（辨证/选穴/针法/方药），高影响力临床测评研究 [[DOI](https://doi.org/10.1038/s41746-025-01845-2)]
- [*JMIR Formative Research*] **Performance Assessment of ChatGPT-4.0 and ChatGLM Series in Traditional Chinese Medicine for Metabolic Associated Fatty Liver Disease: Comparative Study** 作者把87例经中医治疗的代谢相关脂肪性肝病病历交给ChatGPT-4.0、ChatGLM4、带知识库的ChatGLM4和ChatGLM3-6B，比较辨证论治、中西医概念混淆和治疗方案文本。 [Second Military Medical University，Chinese People's Liberation Army] [[DOI](https://doi.org/10.2196/66503)]
- [*arXiv*] **New Snow Tablets（新雪片）** 揭示通用与中医专用LLM依赖药名猜测成分的系统缺陷 [[论文](https://arxiv.org/abs/2504.03786)]
- [*JMIR Medical Education*] **GPT-4 作答台湾中医师执照考试** 用 GPT-4 回答 2022 年台湾中医师执照考试 480 题，并与两名持证中医师对照。直接选答和先解释再选答两种方式合在一起，模型准确率 43.9%，两名医师分别是 70% 和 78.4%。错误里约 55.3% 来自对中医概念的误解。这是执照考试和持证医师的对照，不是把证候、处方合理性和安全拦截分开测。 [[DOI](https://doi.org/10.2196/58897)] [[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939018/)]
- [*Preprints.org（预印本）*] **GPT 台湾中医执业考试评估** GPT-3.5/GPT-4/GPT-4o 在台湾中医执业考试中的表现与可靠性分析（预印本） [[DOI](https://doi.org/10.20944/preprints202501.1787.v1)]
- [*J Integr Complement Med*] **GPT vs ERNIE 中医文化背景对比研究** 拿文化背景当线索，看 GPT 和 ERNIE 做中医执业医师考试时差在哪里。2025 年发表在 Journal of Integrative and Complementary Medicine。 [北京大学，College of Engineering, Boston University, Boston, MA, USA.] [[DOI](https://doi.org/10.1089/jicm.2024.0902)]
- [*IJCNN 2025*] **From Metaphor to Mechanism** LLM解码中医隐喻/取象语言并映射现代医学概念 [Shandong Normal University,Jinan,China，China Pharmaceutical University,Nanjing,China，The University of Tokyo,Tokyo,Japan，Universiti Tunku Abdul Rahman,Perak,Malaysia] [[论文](https://arxiv.org/abs/2503.02760)] [[正式发表](https://doi.org/10.1109/ijcnn64981.2025.11228098)]
- [*arXiv*] **Conveying Imagistic Thinking in Traditional Chinese Medicine Translation: A Prompt Engineering and LLM-Based Evaluation Framework** 作者从《黄帝内经》选了四段基础条文，用提示引导DeepSeek V3.1传达隐喻和转喻，再让ChatGPT 5 Pro和Gemini 2.5 Pro模拟三类读者，在五个认知维度上给人工译文、基线译文和提示调整译文打分，提示调整译文全面最好。 [[论文](https://arxiv.org/abs/2512.01198)]
- [*The Electronic Library*] **Contemporary technological value of ancient Chinese medical books: an empirical patent citation analysis using large language models** 该文用大语言模型识别专利引文中的中医实体并分类引用意图；72.9%的专利引用知识融合程度低，《温病条辨》的技术影响排在所评古籍首位。 [Wuhan University，China Academy of Chinese Medical Sciences，Nanjing University] [[DOI](https://doi.org/10.1108/el-06-2025-0221)]

</details>

<details>
<summary>2024 · 13</summary>

- [*Big Data Mining and Analytics*] **MedBench：中文医学大语言模型综合评测基准（相邻工作）** Liu 与 Hu 共同第一，Zhang 通讯。2024 年发表于 Big Data Mining and Analytics 的中文医学大模型评测基准与云平台，含 300,901 题、43 个临床专科，并采用题答隔离和循环洗牌。这不是中医或中药专评。正确 DOI 为 10.26599/BDMA.2024.9020044，与清单中曾出现的 9020014 不是同一篇，也不是 LingLanMedBench 或 AAAI 同名基准。许可为 CC BY 4.0。 [上海人工智能实验室，上海交通大学医学院附属瑞金医院，香港中文大学（深圳），四川大学华西医院] [[DOI](https://doi.org/10.26599/BDMA.2024.9020044)] [[论文](https://www.sciopen.com/article/10.26599/BDMA.2024.9020044)] [[评测](https://medbench.opencompass.org.cn)]
- [*arXiv*] **用《伤寒论》检验八纲表里辨证** 用《伤寒论》的经验数据，把八纲里的表里看成降维，检验表里是否包含最多的症状信息、是否更抽象，以及是否有助于选方。 [[论文](https://arxiv.org/abs/2409.19531)]
- [*SCIS-ISIS*] **汉方问诊虚拟病人** 构建汉方问诊的虚拟病人，用来加强对汉方病机概念的理解和共情。 [[DOI](https://doi.org/10.1109/scisisis61014.2024.10759962)]
- [*南京中医药大学学报*] **中医标准化评估基准** 覆盖13个学科共29506道题的中医测评基准，系统评测3个通用模型与5个中文医疗模型 [成都中医药大学] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1383)]
- [*arXiv*] **Utilizing Large Language Models for Named Entity Recognition in Traditional Chinese Medicine against COVID-19 Literature: Comparative Study** 作者整理389篇中医药抗新冠文献，人工标注其中48篇的6类实体；模糊匹配下ChatGPT在6项任务中的5项超过BERT问答模型，精确匹配则相反，且GPT-4在药材、靶点和研究方法上的F1都未超过0.5。 [Institute of Basic Theory for Chinese Medicine，GESIS - Leibniz Institute for the Social Sciences，University of Bonn] [[论文](https://arxiv.org/abs/2408.13501)]
- [*arXiv*] **TCMD** 面向大模型评测的中医执业考试选择题集（论文报告约 2851 训 / 600 测）；独立打开论文页未见官方 GitHub 或 Hugging Face 下载 [[论文](https://arxiv.org/abs/2406.04941)]
- [*Integrative Medicine Research*] **TCM-BERT-CNN 整体证候分类** 从公开指南和教材整理专家知识，用 BERT 和卷积神经网络，由症状直接预测多个证候，并用十折交叉验证。 [[DOI](https://doi.org/10.1016/j.imr.2023.101019)]
- [*IEEE International Conference on Medical Artificial Intelligence (MedAI)*] **Reunderstanding of the Classification of Syndromes in the Traditional Chinese Medicine Classic “Shang Han Lun” Based on Large Language Models** 作者从《伤寒论》三阳病条文中选取10条，用中英文ChatGLM4.0和ChatGPT-4.0按现代医学共识重新归类；四个结果里中文ChatGLM4.0最接近原书三阳分类，英文ChatGLM4.0偏离最大。 [Beijing University of Chinese Medicine，China Academy of Chinese Medical Sciences，Wangjing Hospital of China Academy of Chinese Medical Sciences，Institute of Basic Theory for Chinese Medicine] [[DOI](https://doi.org/10.1109/medai62885.2024.00052)]
- [*Journal of Translational Medicine*] **LLM 中医语言文化偏差研究** 比较不同国家大模型的中医表现，论证本土化模型的必要性 [Zhujiang Hospital，Southern Medical University，Shanghai Jiao Tong University，Shanghai First People's Hospital] [[DOI](https://doi.org/10.1186/s12967-024-05128-4)]
- [*Research Square（预印本）*] **GPT-4 中医研究生考试评估** GPT-4 与国产主流大模型在中医研究生考试数据集上的表现评估（预印本） [China Academy of Chinese Medical Science，中国中医科学院，北京中医药大学，Changchun University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.21203/rs.3.rs-4392855/v1)]
- [*대한한의학회지*] **Development of an LLM-based CPX Practicing Chatbot for Korean Medicine Education: Implementation of Automated Scoring and Feedback Generation Framework** 韩医临床技能考试练习聊天机器人中，Claude-3.5-Sonnet在全部样例上定量评分完全正确，平均耗时43.2秒，快于GPT-4。 [Gachon University，Pusan National University] [[DOI](https://doi.org/10.13048/jkm.24067)]
- [*arXiv*] **ChatGPT 中医知识理解探究** ChatGPT 对中医知识理解能力的评测 [[论文](https://arxiv.org/abs/2403.09164)]
- [*Chinese Medicine and Culture*] **ChatGPT 中医交互可行性研究** 以 ChatGPT 为例探讨交互式AI应用于中医的可行性与挑战 [上海中医药大学] [[DOI](https://doi.org/10.1097/MC9.0000000000000103)]

</details>

<details>
<summary>2023 · 4</summary>

- [*World Journal of Traditional Chinese Medicine*] **中医脉诊重测信度与评分者一致性** 两名印度中医执业者对300名受试者做双侧脉诊，评估重测信度和评分者之间是否一致。 [[DOI](https://doi.org/10.4103/2311-8571.388728)]
- **中医新冠文献 LLM 命名实体识别** 大语言模型用于中医新冠文献命名实体识别的比较研究（预印本） [[DOI](https://doi.org/10.2196/preprints.54346)]
- [*Studies in Health Technology and Informatics*] **ICD-11 传统医学章与 SNOMED CT 的本体对照** 把 ICD-11 第26章的传统医学条目和 SNOMED CT 对照，用来建传统医学本体。 [[DOI](https://doi.org/10.3233/shti230249)]
- [*JMIR Medical Education*] **ChatGPT 针灸教育研究** ChatGPT 作为针灸学习工具的对照研究 [Seoul National University Hospital] [[DOI](https://doi.org/10.2196/47427)]

</details>


</details>

<details>
<summary>平台 / 工具（8）：编目、门户、可运行工具</summary>

- [*arXiv*] **TCMIIES** 浏览器端零安装的LLM学术文献结构化信息抽取系统，面向中医等专科领域研究者 [[论文](https://arxiv.org/abs/2605.07507)]
- [*GitHub*] **tcm-cli** 在终端里用自然语言查中医。可以问方剂组成、从症状看证候，也可以核配伍。需要 Python 3.10 以上和一个大模型接口密钥。本地数据可以用命令拉下来，包括药材、方剂，以及 TCMSP、TCMID 等。许可是 MIT。仓库建于 2026 年 2 月。 [[代码](https://github.com/tigerneil/tcm-cli)]
- [*Science of Traditional Chinese Medicine*] **TCM Data Hub（谊元）** 谊元 (YiYuan) LLM驱动的中医数据平台 [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.1097/st9.0000000000000118)]
- [*Cell Discovery*] **神农Alpha** 西湖大学神农 Alpha：AI 驱动的天然药物知识智能编目、获取与翻译共享协作平台（Cell Discovery 2025） [西湖大学] [[DOI](https://doi.org/10.1038/s41421-025-00776-2)] [[网站](https://shennongalpha.westlake.edu.cn/)] [[论文](https://www.nature.com/articles/s41421-025-00776-2)] [[代码](https://github.com/shennong-program/shennongname)]
- [*GitHub*] **pro_TCMLLM** 一份把神农指令数据接到 ChatGLM-6B 上的 P-Tuning 脚本。正在启用的命令把前缀长度设为 128、学习率 2e-2，训练和验证文件放在 ShenNong_TCM_Dataset 目录，最长 3000 步，单卡 batch 为 4，梯度累积为 2，并打开 fp16。仓库建于 2025 年 11 月。 [[代码](https://github.com/GT-Kai/TCMLLM)] [[脚本](https://github.com/GT-Kai/TCMLLM/blob/main/BaseModels/ChatGLM-6B/ptuning/train.sh)]
- [*IEEE BIBM 2025*] **DMease** 辅助中医师诊断和治疗糖尿病的人工智能工具 [北京邮电大学，北京中医药大学] [[DOI](https://doi.org/10.1109/bibm66473.2025.11356320)]
- [*IEEE International Conference on Computational Intelligence and Applications (IC*] **IC-BERT: An Instruction Classifier Model Alleviates the Hallucination of Large Language Models in Traditional Chinese Medicine** IC-BERT用BERT文本过滤器限制中医大模型可回答的问题范围，以减少超出能力范围时生成虚假事实。 [Hainan University] [[DOI](https://doi.org/10.1109/iccia62557.2024.10719061)]
- [*IJACSA*] **草药智能配送聊天机器人** AI 聊天机器人驱动的智能草药配送系统 [University of the Cordilleras，Naresuan University Hospital，Catanduanes State University] [[DOI](https://doi.org/10.14569/ijacsa.2023.0140358)]

</details>

<details>
<summary>其他方法（35）：对齐、提示、专科任务</summary>

<details>
<summary>2026 · 10</summary>

- [*Scientific Reports*] **Jiang、Liu、Han：用无监督聚类识别兼夹体质中的症状亚组** Jiang、Liu、Han 针对中医兼夹体质组合复杂（文中称 248 种可能组合）的问题，在《中医体质分类与判定》问卷（CCMQ）大规模问卷数据上比较 Likert 原始分与二值化编码，以及 UMAP、t-SNE、PCA 与 K-means、DBSCAN、高斯混合模型等组合。作者认为二值化编码、UMAP 与高斯混合模型的组合相对稳定，并给出十聚类解，各簇呈现偏热、偏寒和混合等可区分症状模式。这是问卷数据上的方法学探索，不是治疗试验。本次打开了 Nature Scientific Reports 论文页。 [北京中医药大学生命科学学院，北京中医药大学管理学院] [[DOI](https://doi.org/10.1038/s41598-026-74121-2)] [[论文](https://www.nature.com/articles/s41598-026-74121-2)]
- [*Philosophy, Ethics, and Humanities in Medicine*] **Yu、Yap、Amirdabbaghian：世界卫生组织中医标准中脉诊术语的标准化与英译修订** Yu、Yap、Amirdabbaghian 比较世界卫生组织 2007 年西太平洋地区传统医学术语国际标准与 2022 年《WHO 中医药国际标准术语》中共有的 49 个中文脉诊术语的英译，将跨版本变化分为保留、扩展和替换三类，并做描述性计数：17 个术语（34.7%）无词汇改动，8 个（16.3%）通过增加英语变体而扩展，24 个被替换。作者认为这是概念标准化过程，而不只是语言翻译。研究未做推断性统计。这是术语与标准化研究，不是脉诊算法或临床试验。本次打开了 Springer / BMC 论文页。 [马来亚大学语言与语言学学院] [[DOI](https://doi.org/10.1186/s13010-026-00236-z)] [[论文](https://link.springer.com/article/10.1186/s13010-026-00236-z)]
- [*Translation Review*] **Beyond the Poetic Bard（中医AI翻译评论）** 讨论生成式AI翻译中医文本的精确性、认识论与医学语境局限（Translation Review） [[DOI](https://doi.org/10.1080/07374836.2026.2679929)]
- [*生物化学与生物物理进展*] **病机推理CoT监督（脾胃病）** 以病机推理思维链监督替代固定标签分类，做脾胃病症候表现识别与多维评估（《生物化学与生物物理进展》） [[论文](https://www.pibb.ac.cn/pibbcn/article/abstract/20260141)]
- [*Expert Systems with Applications*] **针灸临床决策中的大模型补偿机制** 分析大语言模型在针灸临床决策中的补偿机制 [[DOI](https://doi.org/10.1016/j.eswa.2025.130870)]
- [*Journal of Integrative Medicine*] **肺磨玻璃结节的中医症状风险模型** 把中医临床症状和影像进展合在一起，评估肺磨玻璃结节往后发展的风险。2026 年发表在 Journal of Integrative Medicine。 [[DOI](https://doi.org/10.1016/j.joim.2026.01.002)]
- [*Chinese Medicine*] **大模型连接中医知识与临床实践** 讨论大语言模型如何把多源、隐性的中医知识和以证候为核心的临床诊疗连接起来 [杭州医学院，杭州师范大学，浙江工业大学] [[DOI](https://doi.org/10.1186/s13020-026-01489-8)]
- [*GitHub*] **吴鞠通温病技能** 把《温病条辨》《医医病书》《吴鞠通医案》和《温热经纬》整理成温病派技能，方便和六经方证对照。仓库简介写有医案 359 案、温病方 22 首，辨证用三焦和卫气营血。 [[代码](https://github.com/jangviktor-web/wujutong)]
- [*Biomedical Signal Processing and Control*] **Generating interpretable clinical reasoning chains in TCM via group relative policy optimization and multi-dimensional rewards** 以组相对策略优化和多维奖励，生成可解释的中医临床推理链。 [安徽中医药大学] [[DOI](https://doi.org/10.1016/j.bspc.2026.111275)]
- [*Digital Chinese Medicine*] **Fine-Med-Mental-T&P: a dual-track approach for high-quality instructional datasets of mental disorders in traditional Chinese medicine** Fine-Med-Mental-T&P用DeepSeek-V3生成、Qwen3-32B改写，从教材指南筛出16000条理论指令，并从600多个真实病例种子筛出4000条实践指令，合成20000条中医神志病指令数据。 [Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.004)]

</details>

<details>
<summary>2025 · 15</summary>

- [*Journal of Global Health*] **Ahn 等：世卫组织传统、补充与整合医学全球研究优先领域及与大语言模型的对照** Ahn、Zhou、Jiang、Kerr、Zhu、Song 与 Rudan 共同资深，用 CHNRI 方法邀请专家为传统、补充与整合医学研究设想打分，并与 ChatGPT-4o、Claude 3.5、Grok 3 的清单对照。53 人回应、34 人打分、157 条设想。这是优先领域共识，不是试验疗效。 [韩国韩医学振兴院，浙江大学医学院附属第二医院公共卫生学院，浙江大学国际医学院，爱丁堡大学 Usher Institute，杭州师范大学信息科学与技术学院，牛津大学] [[DOI](https://doi.org/10.7189/jogh.15.04336)] [[论文](https://jogh.org/2025/jogh-15-04336)]
- [*Frontiers in Pharmacology*] **CNN 预测急性缺血性卒中中医热证类型（预试验）** Yu、Zhu 通讯、Song 通讯等在宣武医院 193 例大动脉粥样硬化型急性缺血性卒中队列中，用卷积神经网络整合中医证候特征与实验室指标，预测热证或非热证。缺失删除后保留 123 条。综合特征测试集准确率和 F1 为 0.95，AUC 正文为 0.91、图 3C 为 0.90。作者自定位为预试验。数据不公开，未见代码。许可为 CC BY。 [首都医科大学宣武医院神经内科，北京大学未来技术学院，约翰霍普金斯大学惠廷工程学院] [[DOI](https://doi.org/10.3389/fphar.2025.1601601)] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1601601/full)]
- [*PLoS ONE*] **Li 等：计算机与手法选穴辅助膝骨关节炎物理治疗的随机对照试验方案** Li、Ahmad 通讯等发表的 STUDY PROTOCOL，比较 Acugraph 计算机选穴与手法选穴作为轻度至中度膝骨关节炎物理治疗辅助手段。计划纳入 50 例、12 次疗程。这是方案而不是试验结果，正文没有报告任何实测结局。本站综述 surv-acupoint-cad 已提示勿把该文献当成已完成试验。 [马来西亚国民大学健康科学学院康复与特殊需要研究中心物理治疗项目，Grand Care Rehab Seremban（物理治疗与针灸）] [[DOI](https://doi.org/10.1371/journal.pone.0313761)] [[论文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0313761)]
- [*CCIS*] **面向辨证的大模型微调** 微调大语言模型做中医辨证 [河海大学，北京中医药大学] [[DOI](https://doi.org/10.1007/978-981-96-4298-4_4)]
- [*世界科学技术-中医药现代化*] **轻量化中医药古籍大语言模型（LoRA）** 用 GPT-4 生成历代《伤寒论》问答，并入神农与 cMedQA2，对 Baichuan、ChatGLM3、Xverse、Qwen 等五个基座做 LoRA，再比较 Qwen-7B-Chat 的全量 LoRA 与 8bit/4bit QLoRA。微调后 Qwen-7B-Chat 的 BLEU、ROUGE-1、ROUGE-2、ROUGE-L 较基座提高 17.61、19.63、14.3、21.4。未命名独立模型。 [南京中医药大学人工智能与信息技术学院，辽宁中医药大学中医药创新工程技术中心] [[DOI](https://doi.org/10.11842/wst.20241014001)]
- [*情报科学*] **融合证素知识的中医证候术语映射** 用证素知识，把临床里的证候说法映射到标准证候名。刊在《情报科学》2025 年第 43 卷第 7 期。 [[论文](https://journal12.magtechjournal.com/jwk3_qbkx/CN/Y2025/V43/I7/48)]
- [*JMIR Formative Research*] **胰腺癌病历的证型识别** 从胰腺癌电子病历的自由文本里识别中医证型。2025 年发表在 JMIR Formative Research。 [[DOI](https://doi.org/10.2196/70602)] [[代码](https://github.com/wangzaimieyoutou/PCSD_Bert)]
- [*Combinatorial Chemistry & High Throughput Screening*] **痛经辨证的机器学习模型** 用机器学习给痛经做中医辨证。2025 年发表。 [[DOI](https://doi.org/10.2174/0113862073293191240212091028)]
- [*IEEE JBHI*] **用大模型理解中医：机制探索与创新应用** 提出面向中医理解的大模型方法，覆盖机制探索与创新应用 [[DOI](https://doi.org/10.1109/jbhi.2025.3631841)]
- [*北京中医药大学学报*] **基于大语言模型与文本嵌入计算的中医证素辨证自动化方法** 先训练指令调优嵌入模型 Instr-MT-TCM，再与大模型协同做证素辨证。1793 例、34 病 66 证上协同方法平均 F1 0.927，高于人工标注 0.512；并在 48 例前列腺癌上核算证素。作者孙肇阳、汪洋、马铭泽、陈妍文、吕镇秀、江甜甜、温慧玲、陈波、关静。 [北京中医药大学中医学院，天津中医药大学针灸推拿学院，天津中医药大学第一附属医院，天津中医药大学中医学院] [[论文](https://xb.bucm.edu.cn/zh/article/doi/10.3969/j.issn.1006-2157.2025.08.018/)]
- [*IET*] **基于Llama3的中医大模型** 在中医数据上微调Llama 3、Phi-3.5和Mistral，补通用模型对中文中医语料的不足 [暨南大学] [[DOI](https://doi.org/10.1049/icp.2025.1017)]
- [*Bioengineering*] **儿童多动症推拿的特征选择** 用机器学习挑选特征，并预测注意缺陷多动障碍儿童的中医推拿方案。2025 年发表在 Bioengineering。 [[DOI](https://doi.org/10.3390/bioengineering12101012)]
- [*CCIS*] **中医大模型指令微调** 面向中医药任务对大语言模型做指令微调 [大连理工大学] [[DOI](https://doi.org/10.1007/978-981-96-1809-5_34)]
- [*SPIE*] **TCMHP** 面向中医养生（治未病）的大语言模型，用专业数据补理论体系难以直接智能化的问题 [郑州大学，国家超算郑州中心] [[DOI](https://doi.org/10.1117/12.3068496)]
- [*ACAIB 2025*] **BioBERT-HDI：草药与化学药相互作用预测** 用 BioBERT 从文献文本预测草药和化学药的相互作用，并与其他机器学习模型比较。 [[DOI](https://doi.org/10.1145/3760269.3760325)]

</details>

<details>
<summary>2024 · 7</summary>

- [*Studies in Health Technology and Informatics*] **将 OMOP 通用数据模型应用于传统东亚医学数据集的可行性** Jiyun Cha、Eun Kyoung Ahn、Young-Heum Yoon、Man Young Park。发表于 Studies in Health Technology and Informatics 2024 年、MEDINFO 2023 论文集第 1349–1351 页的 3 页会议短文，从面瘫、痛经和中风的韩医临床指南抽取条目并映射到 OMOP CDM 6.0。52 个去重条目中 42 个为通用临床信息，10 个为 TEAM 特有；表级全部可映射，字段级有 3 个无法落入现有字段。许可为 CC BY-NC 4.0。DOI 10.3233/SHTI231189。与本站已有 park2026-tkm-omop 不是同一篇。 [韩国韩医学研究院，韩国韩医药振兴院] [[DOI](https://doi.org/10.3233/SHTI231189)] [[论文](https://ebooks.iospress.nl/doi/10.3233/SHTI231189)]
- [*JAMIA*] **灵丹 JAMIA：面向临床推理的中医知识编码** JAMIA论文提出灵丹，用大模型加强中医知识编码以提升临床推理任务。与后来的Digital Chinese Medicine灵丹处方评测不是同一篇 [北京交通大学，天士力] [[DOI](https://doi.org/10.1093/jamia/ocae087)]
- [*Heliyon*] **多囊卵巢证型的多标签预测** 比较不同特征选择和多标签模型，预测多囊卵巢综合征患者的中医证型。2024 年发表在 Heliyon。 [[DOI](https://doi.org/10.1016/j.heliyon.2024.e35283)]
- [*Chinese Journal of Pharmacovigilance*] **中药肝损伤不良反应的风险信号** 用不良反应监测数据，探索中药所致肝损伤的新风险信号和易感因素。期刊页给出论文，没有放出个例表。 [[论文](https://zgywjj.magtechjournal.com/EN/10.19803/j.1672-8629.20230779)] [[PDF](https://zgywjj.magtechjournal.com/EN/article/downloadArticleFile.do?attachType=PDF&id=3442)]
- [*arXiv*] **中医提示工程框架** 基于提示工程框架的大语言模型中医智能理解方法 [[论文](https://arxiv.org/abs/2410.19451)]
- [*arXiv*] **RLAIF 中医对齐** 通过AI反馈强化学习增强大语言模型的中医能力 [[论文](https://arxiv.org/abs/2411.00897)]
- [*Digital Chinese Medicine*] **BSG 中医智能问答** 基于 BSG 深度学习模型的中医智能问答系统（方剂与中药实例） [Hunan University of Traditional Chinese Medicine，Central South University] [[DOI](https://doi.org/10.1016/j.dcmed.2024.04.006)]

</details>

<details>
<summary>2023 · 3</summary>

- [*中国工程科学*] **新时代中医药发展现状与思考（战略述评）** 薛晓娟等，张伯礼通讯。发表于《中国工程科学》2023 年 25 卷第 5 期的战略述评与对策建议，出自工程院咨询项目“新时代中医药发展战略研究”。从理论、临床评价、资源、智能制造和国际推广五个方面梳理现状与问题，并提出六条对策。这不是系统评价，也不是新的算法或临床试验。许可据 Unpaywall 为 CC BY-NC-ND。 [天津中医药大学文化与健康传播学院，天津中医药大学管理学院，天津中医药大学中医药研究院，中国医学科学院北京协和医学院药用植物研究所，浙江大学药学院，中国中医药科技发展中心，北京中医药大学东直门医院，北京中医药大学] [[DOI](https://doi.org/10.15302/J-SSCAE-2023.05.007)] [[论文](https://www.engineering.org.cn/sscae/CN/10.15302/J-SSCAE-2023.05.007)]
- [*Military Medical Research*] **中西医有机结合临床实践指南编制方法（立场与指南）** Jin 等，Zeng 与 Shang 通讯。2023 年发表于 Military Medical Research 的立场文章兼指南方法标准，提出中西医“有机结合”临床实践指南的编制程序。对 54 份已发表中西医结合指南的盘点显示，仅 5.6% 按结合思路明确提出临床问题。这不是系统评价，也不是临床试验。许可为 CC BY 4.0。 [武汉大学中南医院循证与转化医学中心，中国中医科学院中医临床基础医学研究所，北京中医药大学东直门医院] [[DOI](https://doi.org/10.1186/s40779-023-00481-9)] [[论文](https://mmrjournal.biomedcentral.com/articles/10.1186/s40779-023-00481-9)]
- [*IEEE BIBM*] **中医疫病防治问答模型** 基于大语言模型的中医疫病防治问答模型 [南京中医药大学] [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385748)]

</details>


</details>

<details>
<summary>更早的工作（143）：专家系统、舌脉、本体、早期编码器</summary>

<details>
<summary>2020–2022 · 61</summary>

- [*Discover Applied Sciences*] **Mathematical modeling of Chinese medicine by complex-valued five-agent network** 复值五智能体网络统一阴阳互补与五行反馈的线性代数表述。 [National Cheng Kung University] [[DOI](https://doi.org/10.1007/s42452-025-06602-4)]
- [*Lv Q et al., *Signal Transduct Target Ther* 8(1):127*] **TCMBank** TCMBank（platform阶段历史锚点） [中山大学，澳门科技大学] [[DOI](https://doi.org/10.1038/s41392-023-01339-1)]
- [*Interdisciplinary*] **Historical Analysis of Medical Artificial Intelligence Development in China: Research Cent** 以中医专家系统为中心的中国医学 AI 发展史梳理（二次文献锚点；作者以 DOI 页为准）。 [Okayama University of Science，Okayama University] [[DOI](https://doi.org/10.18926/interdisciplinary/65464)]
- [*Zhang Y et al., *Acta Pharm Sin B* 13(6):2559-2571*] **ETCM v2.0** ETCM v2.0（platform阶段历史锚点） [中国医学科学院，中国科学院，Shanghai Institute of Materia Medica，Guiyang Medical University] [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)]
- [*Scientific Reports*] **Discovering golden ratio in the world’s first five-agent network in ancient China** 用多智能体网络理论量化五行和谐稳态，并给出电路/编队实验验证。 [National Cheng Kung University] [[DOI](https://doi.org/10.1038/s41598-023-46071-6)]
- [*Frontiers in Psychology*] **Lai 等：基于语音与 ResNet 识别气虚质与平和质** Lai、Guan、Men、Shang、Zhang 通讯用 48 名受试者的 720 条语音语谱图和 ResNet34 区分气虚质与平和质。作者自报准确率 81.5%、AUC 0.85；代码声明见 GitHub GYT0704/Voice_Classification。须与本站 voice-constitution-acoustic、constitution-tap 区分。 [广州中医药大学医学信息工程学院，北京中医药大学东直门医院教育部和北京市中医内科学重点实验室] [[DOI](https://doi.org/10.3389/fpsyg.2022.1043955)] [[论文](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1043955/full)]
- [*Frontiers in Oncology*] **机器学习预后模型：中药对Ⅰ–Ⅲ期结直肠癌复发转移的影响** Tang、Gao 共同第一，Yang 通讯。回顾性纳入 558 例根治术后Ⅰ–Ⅲ期结直肠癌患者，比较四种机器学习方法对 3 年和 5 年复发转移的内部验证表现，并加入中药干预和证型。代码印在 Gitee。5 年干预模型的正文与表 3 数字不一致。许可为 CC BY。 [中国中医科学院西苑医院肿瘤科，百度智能城市事业部] [[DOI](https://doi.org/10.3389/fonc.2022.1044344)] [[论文](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2022.1044344/full)] [[代码](https://gitee.com/doctortangmo/TCM-CRC-prognostic-model)]
- [*Frontiers in Pharmacology*] **双路径体外试验评价中药注射剂线粒体毒性** Shen、Feng 通讯、Ma 通讯等用 HepG2 葡萄糖／半乳糖三磷酸腺苷试验和 HCT116 呼吸缺陷细胞增殖试验，筛查 35 种中药注射剂。喜炎平、灯盏花素、双黄连和茵栀黄达到作者设定的线粒体毒性标准，并提示芦丁、黄芩苷、野黄芩苷和连翘苷为候选成分。这是体外筛查，不是临床试验。许可为 CC BY。 [澳门科技大学中药质量研究国家重点实验室，五邑大学生物科技与健康学院，中国药科大学生命科学与技术学院] [[DOI](https://doi.org/10.3389/fphar.2022.1039235)] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.1039235/full)]
- [*Frontiers in Pharmacology*] **结构–活性与机器学习识别潜在保肝中药** He、Xie 通讯、Wang 通讯等用机器学习预测中药成分的保肝活性，并结合功效类别和药性聚类提出 12 味潜在保肝中药。投票模型在 178 个化合物的测试集上准确率为 0.871。12 味中有 9 味已有动物或细胞实验文献支持。这是计算预测和文献核对，不是新的临床试验。许可为 CC BY。 [湖州师范学院医学院，湖州市中心医院，湖州学院理工学部，新疆维吾尔自治区中药民族药研究所，浙江药科职业大学中医学院] [[DOI](https://doi.org/10.3389/fphar.2022.969979)] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.969979/full)]
- [*Chinese Medicine*] **用人工智能筛选中西药联用中的肝毒性化合物** Chen、Zhao 通讯、Shang 通讯等收集 2035 个化合物，比较九种机器学习和深度信念网络，用于筛选中西药联用中单个化合物的肝毒性。随机森林训练集准确率 0.838，测试集为 0.767；深度信念网络测试集准确率 82.2%。数据需向作者索取，未见代码。许可为 CC BY 4.0。 [北京中医药大学东直门医院，复旦大学计算机科学技术学院，中国中医科学院临床基础医学研究所] [[DOI](https://doi.org/10.1186/s13020-022-00617-4)] [[论文](https://cmjournal.biomedcentral.com/articles/10.1186/s13020-022-00617-4)]
- [*Engineering*] **利用证候要素架构中医人工智能诊疗模型（观点评论）** 王阶、段练、李洪峥、刘金垒、陈恒文。发表于 Engineering 2022 年 8 卷第 1 期的 Views & Comments 短文，主张以证候要素为枢纽，用规则集成、指南症状积分、图卷积知识图谱和小样本数据构建中医人工智能诊疗模型，并以冠心病八大证候要素为例。这不是系统评价，也没有报告训练集例数或测试准确率。许可为 CC BY-NC-ND 4.0。与后续同团队《中国实验方剂学杂志》改良 Transformer 论文不是同一篇。 [中国中医科学院广安门医院] [[DOI](https://doi.org/10.1016/j.eng.2021.06.014)] [[论文](https://www.engineering.org.cn/engi/CN/10.1016/j.eng.2021.06.014)]
- [*ICMLC*] **神经网络判别经方方名** 从《伤寒论》和《金匮要略》原文抽出 261 首方、173 味药，训练神经网络：只给出药物组成、不给方名时，判断这是哪一首经方，并用代表不同经的加减方做检验。 [广州中医药大学，广州中医药大学第一附属医院] [[DOI](https://doi.org/10.1145/3529836.3529897)]
- [*Journal of Healthcare Engineering*] **按中医问诊思路做的证候辨证** 按中医问诊的思路做个性化证候辨证，针对计算问诊里追问不足、缺少问诊原则的问题。 [[DOI](https://doi.org/10.1155/2022/6553017)]
- [*AAAI*] **多模态中医体质端到端评估** 端到端评估中医体质。输入包括面象、舌象、脉和声音，以及问诊文本。 [[DOI](https://doi.org/10.1609/aaai.v36i11.21727)]
- [*Frontiers in Pharmacology*] **喜炎平联用药物与疑似过敏** 用国家医保抽样做巢式病例对照，看喜炎平注射液和其他药一起用时，疑似过敏的风险怎么变。2022 年发表在 Frontiers in Pharmacology。 [[DOI](https://doi.org/10.3389/fphar.2022.883407)]
- [*BioMed Research International*] **乙肝中医 KG 问答系统** 基于知识图谱的中医诊治病毒性乙型肝炎问答系统 [中国中医科学院，First Affiliated Hospital of Henan University] [[DOI](https://doi.org/10.1155/2022/7139904)]
- [*Evidence-Based Complementary and Alternative Medicine*] **上海 2 型糖尿病问诊证候识别** 用上海的中医问诊信息，识别 2 型糖尿病的证候。2022 年发表。 [[DOI](https://doi.org/10.1155/2022/2843218)]
- [*Digital Chinese Medicine*] **《伤寒论》知识图谱** 构建《伤寒论》知识图谱，并给出应用。 [[DOI](https://doi.org/10.1016/j.dcmed.2022.12.006)]
- [*Digital Chinese Medicine*] **《伤寒论》异构图与图卷积表示** 为《伤寒论》构建异构图，并用图卷积网络学习节点表示。 [[DOI](https://doi.org/10.1016/j.dcmed.2022.12.007)]
- [*CCL*] **ZY-BERT** TCM-SD 同文提出的中医领域预训练编码器（约 0.4B token 语料）；权重在网盘，仓库另含辨证微调代码。与 2411.00897 RLAIF 文不是同一工作 [[论文](https://arxiv.org/abs/2203.10839)] [[正式发表](https://aclanthology.org/2022.ccl-1.80/)] [[代码](https://github.com/Borororo/ZY-BERT)]
- [*World Health Organization*] **WHO 中医药国际标准术语** 世界卫生组织 2022 年公布的中医药术语标准，给临床、政策和病历使用同一套概念。出版物页面提供 PDF，用来对照证、证候和四诊的中英文说法。 [[网站](https://www.who.int/publications/i/item/9789240042322)] [[PDF](https://iris.who.int/bitstream/handle/10665/352306/9789240042322-eng.pdf)]
- [*BioMed Research International*] **TCMPR 子网术语映射处方推荐** 草药-症状知识图谱（1.8 万实体 / 10 万关系）+ 子网术语映射，用 CNN 做处方推荐 [北京交通大学，清华大学] [[DOI](https://doi.org/10.1155/2022/4845726)]
- [*Digital Health*] **Research and application of tongue and face diagnosis based on deep learning** 舌面诊深度学习预处理/分割/分类技术路线综述与验证。 [成都中医药大学] [[DOI](https://doi.org/10.1177/20552076221124436)]
- [*Journal of Ethnopharmacology*] **MGCN** 面向《伤寒论》方的多图卷积处方推荐：用证素图和证型图做症状特征聚合，再由多层感知机预测草药。 [[DOI](https://doi.org/10.1016/j.jep.2022.115109)]
- [*Neural Networks*] **KDHR** 知识驱动的多层图卷积荐药：把中医药知识图谱里的症状–草药关系做多层信息融合后再推荐。代码公开。 [[DOI](https://doi.org/10.1016/j.neunet.2021.11.010)] [[代码](https://github.com/Rao-Yulong/KDHR)]
- [*Chinese Acupuncture & Moxibustion*] **GB/T 12346-2021 经穴名称与定位解读** 解释国家标准《经穴名称与定位》（GB/T 12346-2021）相对 2006 版的变化，包括标准名称、术语、定义、部位表述，以及部分穴位骨度分寸和定位。 [[DOI](https://doi.org/10.13703/j.0255-2930.20220117-k0001)]
- [*Evid. Based Complement. Alternat. Med.*] **Deep Learning Multi-label Tongue Image Analysis and Its Application in a Population Underg** Faster R-CNN 多标签舌象（裂纹/齿痕/腻苔等）及体检人群关联分析。 [上海中医药大学，复旦大学] [[DOI](https://doi.org/10.1155/2022/3384209)]
- [*Digital Chinese Medicine*] **Data-driven based four examinations in TCM: a survey** 数据驱动四诊（含深度学习）设备—算法—数据集全景。 [Beijing University of Civil Engineering and Architecture，University of Maryland, Baltimore，Shandong University] [[DOI](https://doi.org/10.1016/j.dcmed.2022.12.004)]
- [*Frontiers in Physiology*] **用舌象和脉象区分疾病性与非疾病性疲劳** Shi、Xu 通讯等在上海中医药大学附属曙光医院采集舌象和脉象，用四种分类器区分疾病性疲劳与非疾病性疲劳。摘要中约 85% 的准确率来自舌脉加上年龄和体重指数；仅舌脉联合时逻辑回归准确率约为 67%。数据不能公开，未见代码。许可为 CC BY。 [上海中医药大学基础医学院，上海中医药大学中医健康服务协同创新中心] [[DOI](https://doi.org/10.3389/fphys.2021.708742)] [[论文](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2021.708742/full)]
- [*BMC Medical Informatics and Decision Making*] **层次注意力网络检测中药处方中的功效特异药组** Chen、Liu 共同第一。用层次注意力网络蒸馏中药处方，再以 Apriori 挖掘功效特异药组。13 种测试功效上，蒸馏后整体平均准确率约 15.57%–23.83%，高于未蒸馏对照。金标准来自互联网并经一位专家确认。表 1 和表 2 下有无关脚注。许可为 CC BY 4.0。 [四川大学计算机系，成都中医药大学基础医学院] [[DOI](https://doi.org/10.1186/s12911-021-01411-2)] [[论文](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-021-01411-2)]
- [*JMIR Medical Informatics*] **远程监督的中医跨度实体抽取** 用远程监督做跨度一级的中医实体抽取，从文本里直接抽出一段实体，而不是逐字标注。2021 年发表在 JMIR Medical Informatics。 [[DOI](https://doi.org/10.2196/28219)]
- [*Biomedical Signal Processing and Control*] **自适应神经模糊推理的中医睡眠障碍诊断** 用自适应神经模糊推理系统做中医睡眠障碍诊断。 [[DOI](https://doi.org/10.1016/j.bspc.2021.102942)]
- [*Zenodo*] **经方按症状排序（平人）** 把《伤寒杂病论》里某一方对应的证当作应有证，把病人当下的证当作现有证，两边匹配后给出 0% 到 100% 的适用性，并做成在线程序《平人》。输入用的是书里描述症状和病程的词。2021 年 12 月发布，许可 CC BY 4.0。 [[DOI](https://doi.org/10.5281/zenodo.5804283)] [[数据](https://zenodo.org/records/5804283)]
- [*Scientific Reports*] **湖北中药注射剂自发报告** 分析湖北省 2014 到 2019 年中药注射剂不良反应自发报告，看哪些品种和表现更值得留意。2021 年发表在 Scientific Reports。 [[DOI](https://doi.org/10.1038/s41598-021-88339-9)]
- [*Evidence-Based Complementary and Alternative Medicine*] **基于知识图谱的中成药处方监测** 用知识图谱做中成药处方监测，用来发现联用和剂量上的问题。2021 年发表。 [[DOI](https://doi.org/10.1155/2021/9970063)]
- [*Scientific Reports*] **台湾草药不良反应报告系统（1998–2016）** 介绍台湾 1998 年至 2016 年用于报告和评估草药不良反应的系统。 [[DOI](https://doi.org/10.1038/s41598-021-00704-w)]
- [*IEEE ICSGEA*] **中药处方剂量分配的模糊分析** 用模糊分析讨论中药处方里的剂量分配。 [[DOI](https://doi.org/10.1109/icsgea53208.2021.00138)]
- [*Communications in Computer and Information Science*] **中医病历症状规范化的自动方法** 讨论如何自动把中医病历中的症状名规范化。 [[DOI](https://doi.org/10.1007/978-3-030-78615-1_42)]
- [*Journal of Pharmacopuncture*] **《温热经纬》与《伤寒论》方剂网络** 对《温热经纬》和《伤寒论》中的方剂做网络分析。 [[DOI](https://doi.org/10.3831/kpi.2021.24.3.138)]
- [*ISAIMS*] **Wasserstein GAN 扩充腕部脉象** 用 Wasserstein GAN 为中医腕部脉象信号做数据增强。 [[DOI](https://doi.org/10.1145/3500931.3501003)]
- [*Journal of Biomedical Informatics*] **KeMRE：中药说明书的知识增强关系抽取** 用知识增强的关系抽取，从中药说明书文本中抽出医学关系。 [[DOI](https://doi.org/10.1016/j.jbi.2021.103834)]
- [*Frontiers in Pharmacology*] **ICD-10 疾病与汉方寒热虚实的对应** 在一家大型汉方门诊，把 2014 年 10 月至 2019 年 6 月、20 岁及以上患者的 ICD-10 诊断，对照到 ICD-11 传统医学里的寒热、虚实等模块。 [[DOI](https://doi.org/10.3389/fphar.2021.751403)]
- [*JMIR Medical Informatics*] **Ensemble Learning-Based Pulse Signal Recognition: Classification Model Development Study** SVM（时/频域结构特征）与 DCNN 决策级融合的脉象识别。 [华东理工大学，上海中医药大学] [[DOI](https://doi.org/10.2196/28039)]
- [*IEEE Trans. Cybernetics*] **Automatic Construction of Chinese Herbal Prescriptions From Tongue Images Using CNNs and A** 舌象→方剂端到端生成，引入治法主题辅助损失。 [South China University of Technology，Guangdong General Hospital] [[DOI](https://doi.org/10.1109/tcyb.2019.2909925)]
- [*Mathematical Biosciences and Engineering*] **基于高维特征的高精度脉诊分类** Ching-Han Huang、Yu-Min Wang、Shana Smith 通讯。发表于 Mathematical Biosciences and Engineering 2020 年 17 卷第 6 期的方法论文，从 ANSWatch 脉搏信号抽取 71 维特征，用主成分分析和人工神经网络区分 10 种脉型。解释 95% 方差的 27 个主成分平均准确率为 98.2%。正式本按 CC BY 4.0 可下载，未见代码或原始数据。DOI 10.3934/mbe.2020353。 [台湾大学机械工程学系] [[DOI](https://doi.org/10.3934/mbe.2020353)] [[论文](https://www.aimspress.com/article/doi/10.3934/mbe.2020353)]
- [*Frontiers in Neuroscience*] **静息态功能连接预测原发性痛经针刺疗效** Yu、Xie 同等贡献，Liang 与 Yang 通讯。54 例原发性痛经随机真、假针刺，最终分析 35 例。真针刺显著止痛，假针刺不显著。用 8 条基线功能连接做留一回归预测。正文与图 5 对疼痛变化值和变化率的对应不一致。许可为 CC BY。 [成都中医药大学针灸推拿学院脑研究中心，成都中医药大学附属医院放射科] [[DOI](https://doi.org/10.3389/fnins.2020.559191)] [[论文](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.559191/full)] [[代码](https://github.com/cdutcmysy/ROIwise_FC_mancova)]
- [*ICCIA*] **计算机视觉的中医面色识别** 用深度学习定位 68 个面部关键点，分割庭、颊、明堂等区域，再按多颜色空间的直方图识别中医面色。 [[DOI](https://doi.org/10.1109/iccia49625.2020.00029)]
- [*Sensors*] **穴位皮肤阻抗的手机脉诊** 用指尖按压动脉处皮肤的方式，在穴位上测皮肤阻抗，检验手机做中医脉诊是否可行。 [[DOI](https://doi.org/10.3390/s20164618)]
- [*World Journal of Traditional Chinese Medicine*] **用自然语言处理挖掘《伤寒论》** 用自然语言处理对《伤寒论》做文本挖掘和分析。 [[DOI](https://doi.org/10.4103/wjtcm.wjtcm_28_19)]
- [*JMIR Medical Informatics*] **模仿肺癌中医辨证的端到端模型** 训练端到端模型，模仿中医在肺癌诊断中的证候辨证。 [[DOI](https://doi.org/10.2196/17821)]
- [*Integrative Cancer Therapies*] **对 ICD-11 第26章传统医学条目的增补建议** ICD-11 第26章来自 WHO 西太区传统医学术语标准，是中日韩分类的并集。文章建议在保留已收录证候的同时补充仍缺的证候。 [[DOI](https://doi.org/10.1177/1534735420908334)]
- [*BMC Bioinformatics*] **从文献为抗抑郁药不良反应寻找中药替代** 先从文献找出不良反应明显的西药，再寻找可能减轻这些不良反应的中药。案例是抑郁症用药。 [[DOI](https://doi.org/10.1186/s12859-020-03735-8)]
- [*JMIR Medical Informatics*] **人工智能中医辅助诊断系统验证** 验证一套基于人工智能的中医辅助诊断系统。2020 年发表在 JMIR Medical Informatics。 [[DOI](https://doi.org/10.2196/17608)]
- [*Frontiers in Pharmacology*] **乳腺癌中医证型的神经网络区分** 用神经网络和聚类，区分乳腺癌患者的中医证型。2020 年发表在 Frontiers in Pharmacology。 [[DOI](https://doi.org/10.3389/fphar.2020.00670)]
- [*Journal of Ethnopharmacology*] **中药心脏不良反应的文献计量与关联规则** 用文献计量和关联规则归纳中药引起的心脏不良反应有哪些规律。 [[DOI](https://doi.org/10.1016/j.jep.2020.112582)]
- [*BMC Medical Informatics and Decision Making*] **中医临床细粒度 NER 语料** 基于中医临床病历构建细粒度实体识别语料 [成都中医药大学，Chengdu University of Information Technology] [[DOI](https://doi.org/10.1186/s12911-020-1079-2)]
- [*IEEE ICKG*] **TCMKG** 基于深度学习的中医知识图谱平台 [University of Electronic Science and Technology of China，成都中医药大学] [[DOI](https://doi.org/10.1109/ICBK50248.2020.00084)]
- [*Chinese Medicine*] **SiPA：同时预测中药相互作用** 因为成分、靶点和疾病之间的相互作用记录不够，提出 SiPA，用来同时预测并扩展中药相互作用网络。 [[DOI](https://doi.org/10.1186/s13020-020-00369-z)]
- [*arXiv*] **SMGCN** 证候感知的多图卷积荐药模型：在症状–草药图之外再建症状共现图和草药共现图，先融成隐式证候表示再推荐草药。 [华东师范大学，中国科学技术大学，同济大学] [[论文](https://arxiv.org/abs/2002.08575)]
- [*Journal of Integrative Medicine*] **PIPE-11：落地 ICD-11 传统医学章的临床决策支持** 介绍 Pattern Identification and Prescription Expert-11，用辨证和处方文献把 ICD-11 传统医学章做成可计算的临床决策支持。 [[DOI](https://doi.org/10.1016/j.joim.2020.08.003)]
- [*Comput. Struct. Biotechnol. J.*] **Artificial intelligence in tongue diagnosis: Using deep convolutional neural network for r** ResNet34 齿痕舌识别，强调跨设备泛化。 [Being University of Chinese Medicine, Beijing 100029, China，Beijing University of Posts and Telecommunications, Beijing 100876, China，Beijing Normal University, Beijing 100875, China，中国科学院] [[DOI](https://doi.org/10.1016/j.csbj.2020.04.002)]

</details>

<details>
<summary>2010s · 64</summary>

- [*PLOS Computational Biology*] **用机器学习预测中药归经** Wang、Tang 通讯等从 TCMID 收集 646 味中药及其成分的分子指纹和 ADME 特征，分别在中药水平和化合物水平预测归经。摘要最高准确率为 0.83；表 2 中化合物水平随机森林的最高平衡准确率为 0.67。代码印在 GitHub。许可为 CC BY。 [赫尔辛基大学医学院，华东理工大学药学院，赫尔辛基大学生命科学研究所] [[DOI](https://doi.org/10.1371/journal.pcbi.1007249)] [[论文](https://doi.org/10.1371/journal.pcbi.1007249)] [[代码](https://github.com/herb-medicne/meridian-prediction)]
- [*European Journal of Integrative Medicine*] **舌、声、脉联合的中医体质辨识** 把舌象、声音和脉象指标合在一起做中医体质辨识。 [[DOI](https://doi.org/10.1016/j.eujim.2019.04.001)]
- [*arXiv*] **脉搏压力波与妊娠的机器学习对应** 用深度学习把脉搏压力波和是否妊娠对应起来。文中妊娠识别准确率 84%，AUC 91%。用的是压力波，不是中医脉象的位、数、形、势。 [[论文](https://arxiv.org/abs/1910.01726)]
- [*IEEE Trans. Cybernetics*] **Tooth-Marked Tongue Recognition Using Multiple Instance Learning and CNN Features** CNN 特征+多示例学习识别齿痕舌，标志舌诊进入深度学习。 [Shanghai University，Shanghai University of Engineering Science] [[DOI](https://doi.org/10.1109/tcyb.2017.2772289)]
- [*JAMIA*] **TCM-BERT** 用领域语料继续预训练 BERT，把中医临床记录分成五类病（JAMIA 2019）。CKCEST 版权，全量 46205 条不公开，仓库只有划分样例和网盘微调权重 [美国西北大学，浙江大学] [[DOI](https://doi.org/10.1093/jamia/ocz164)] [[代码](https://github.com/yao8839836/tcm_bert)]
- [*Neurocomputing*] **IHPreten：配伍禁忌药对预测** 用带属性正则的监督学习框架，预测中药里的配伍禁忌药对。 [[DOI](https://doi.org/10.1016/j.neucom.2019.02.017)]
- [*Xu HY et al., *Nucleic Acids Res* 47(D1):D976-D982*] **ETCM** ETCM（platform阶段历史锚点） [中国中医科学院，北京大学，中国科学院] [[DOI](https://doi.org/10.1093/nar/gky987)]
- [*BMC Medical Informatics and Decision Making*] **An ontological framework for the formalization, organization and usage of TCM-Knowledge** 基于 GFO 的 GFO-TCM 中层本体，修正 TCMLS-SN 语义问题。 [Leipzig University，中国医学科学院，中国中医科学院] [[DOI](https://doi.org/10.1186/s12911-019-0760-9)]
- [*IEEE Access*] **ANDERATION：反社区发现用于中药配伍禁忌** 按节点的度以及组内度与组外度之比做反社区发现，用来在中药网络里找配伍禁忌。配伍禁忌是组内几乎没有连边、连边多在组外。 [[DOI](https://doi.org/10.1109/access.2019.2934227)]
- [*ACM CIKM*] **配伍禁忌药对的监督学习框架** 用监督学习预测中药配伍禁忌药对。与后来的 IHPreten 是同一方向的另一篇会议论文。 [[DOI](https://doi.org/10.1145/3269206.3269241)]
- [*IEEE IAEAC*] **语义中医方剂知识图谱 (Miao et al. 2018)** 自顶向下建本体、从方剂文本抽实体关系，构建语义方剂知识图谱 [Communication University of China，Academy of Broadcasting Science] [[DOI](https://doi.org/10.1109/IAEAC.2018.8577236)]
- [*arXiv*] **糖尿病证候的多实例多任务卷积网络** 把糖尿病患者的病历当成一维图像、症状当成像素，用多实例多任务卷积网络先找出相关症状，再对应到证候。 [[论文](https://arxiv.org/abs/1812.07764)]
- [*arXiv*] **由多尺度面容生成中药处方** 用卷积网络从多尺度面部特征生成中药处方。此前处方生成多只看症状，这篇挖掘面容和处方的关系。 [[论文](https://arxiv.org/abs/1812.06847)]
- [*BioMed Research International*] **桡动脉脉搏波的高血压机器学习分类** 用机器学习比较 450 名高血压患者和 479 名健康人的桡动脉脉搏波，为中医脉诊提供客观参照。 [[DOI](https://doi.org/10.1155/2018/2964816)]
- [*BMC Medical Informatics and Decision Making*] **中药不良反应信号的决策树分类** 用决策树给中药药物警戒里的信号检测做分类。2018 年发表在 BMC Medical Informatics and Decision Making。 [[DOI](https://doi.org/10.1186/s12911-018-0599-5)]
- [*CISP-BMEI*] **Constitution Identification of Tongue Image Based on CNN** CNN 舌象体质辨识，对比传统手工特征 ML。 [Beijing University of Technology] [[DOI](https://doi.org/10.1109/cisp-bmei.2018.8633075)]
- [*Journal of Biomedical Semantics*] **自动构建中文症状知识库** Ruan 通讯等从八个医疗网站、三个中文百科站点和上海曙光医院 25 万份电子病历自动构建中文症状知识库，并链接到 UMLS。结果部分报告 135,485 个实体和 26,821 个症状（含 3,968 个中医症状）；结论写成 135,484。电子病历条件随机场只给出精确率。知识库以关联开放数据发布。许可为 CC BY 4.0。 [华东理工大学，上海曙光医院] [[DOI](https://doi.org/10.1186/s13326-017-0145-x)] [[论文](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-017-0145-x)]
- [*InTech*] **妊娠禁忌中药概述** 书中一章，概述妊娠期间禁用的中药。 [[DOI](https://doi.org/10.5772/67066)]
- [*Artificial Intelligence in Medicine*] **中医养生知识图谱 (Yu et al. 2017)** 整合术语、文献与数据库的大规模中医养生知识图谱，支持检索、可视化与推荐 [北京中医药大学，中国中医科学院] [[DOI](https://doi.org/10.1016/j.artmed.2017.04.001)]
- [*Nucleic Acids Research*] **PharmMapper** 上传一个分子的三维结构，反查它可能落到哪些蛋白上。2017 年这一版扩到 23236 个蛋白，含 16159 个可成药药效团模型和 51431 个可配体药效团模型，序列聚类用的是 2016 年 1 月 1 日的 PDB 快照。中药成分只有结构、还没有实验靶点时可以用。 [[网站](https://www.lilab-ecust.cn/pharmmapper/)] [[说明](https://www.lilab-ecust.cn/pharmmapper/help.php)] [[DOI](https://doi.org/10.1093/nar/gkx374)]
- [*China Journal of Chinese Materia Medica*] **GB/T 31774 与 ISO 18668 中药编码对照** 对照中国国家标准 GB/T 31774-2015 和国际标准 ISO 18668 第 1 至第 4 部分的中药编码，说明相同和不同之处。 [[DOI](https://doi.org/10.19540/j.cnki.cjcmm.20170426.003)]
- [*BioMed Research International*] **Diagnostic Method of Diabetes Based on Support Vector Machine and Tongue Images** 标准化舌象+SVM/PCA/GA 的糖尿病筛查模型。 [上海中医药大学] [[DOI](https://doi.org/10.1155/2017/7961494)]
- [*Journal of Integrative Medicine*] **高血压患者的寸口脉与脉搏波** 在高血压患者中，把中医寸口脉诊和脉搏波、血流动力学放在一起看二者是否相关。 [[DOI](https://doi.org/10.1016/s2095-4964(16)60233-9)]
- [*Frontiers in Pharmacology*] **附子毒性成分指数** 用乌头碱、新乌头碱和次乌头碱的最小致死量做加权，提出附子的毒性成分指数，避免把三种双酯型生物碱的含量直接相加。2016 年发表在 Frontiers in Pharmacology。 [[DOI](https://doi.org/10.3389/fphar.2016.00164)]
- [*arXiv*] **舌、面与舌下融合识别糖尿病** 融合舌象、面容和舌下图像，识别糖尿病及其早期的糖调节受损。中医望诊把这几处当作无创依据，此前工作多只看单一模态。 [[论文](https://arxiv.org/abs/1604.03443)]
- [*Chinese Journal of Electronics*] **模糊支持向量机的中医面色识别** 分割面颊后，用基于颜色建模的模糊支持向量机识别中医面色，以降低离群点的影响。 [[DOI](https://doi.org/10.1049/cje.2016.05.013)]
- [*Journal of Traditional Chinese Medical Sciences*] **彩色人脸特征的中医体质分类** 采集 5150 人的彩色人脸图像，检测人脸并定位关键点，用面部特征做中医体质分类。 [[DOI](https://doi.org/10.1016/j.jtcms.2016.12.001)]
- [*International Symposium on Computer, Consumer and Control*] **九层卷积网络的腕部脉象分类** 用 9 层卷积网络直接对中医腕部脉象信号分类，不再手工选择特征。脉图没有公开。 [[DOI](https://doi.org/10.1109/is3c.2016.101)]
- [*IEEE BIBM*] **中医期刊关系抽取 (Wang & Poon 2016)** 从中医期刊全文做关系抽取，为后续知识图谱构建提供方法 [The University of Sydney] [[DOI](https://doi.org/10.1109/BIBM.2016.7822725)]
- [*Physica A*] **《伤寒论》的复杂网络模型** 用复杂网络描述《伤寒论》的结构。 [[DOI](https://doi.org/10.1016/j.physa.2016.03.115)]
- [*BMC Complementary and Alternative Medicine*] **腕部关脉物理量与高血压关联的预试验** Lee、Kim 通讯等在 393 名 46 至 73 岁韩国女性中分析关部脉波物理量与高血压的关联和预测。这是预试验：高血压仅 52 例，类别不均衡，高血压类别灵敏度很低。不能与本站其他脉搏高血压条目合并。许可为 CC BY 4.0。 [韩国韩医学研究院基础研究部] [[DOI](https://doi.org/10.1186/s12906-015-0756-7)] [[论文](https://bmccomplementalternmed.biomedcentral.com/articles/10.1186/s12906-015-0756-7)]
- [*Evidence-Based Complementary and Alternative Medicine*] **希尔伯特–黄变换与随机森林的冠心病脉象识别** 用希尔伯特–黄变换提取中医脉象的能量和样本熵，再用随机森林区分冠心病患者和健康人。 [[DOI](https://doi.org/10.1155/2015/895749)]
- [*China Journal of Chinese Materia Medica*] **含反药的附子处方关联规则** 用关联规则分析不同地区含配伍禁忌药的附子处方，并归纳这些配伍的特点。 [[DOI](https://doi.org/10.4268/cjcmm20150639)]
- [*PLOS ONE*] **共形预测与随机森林用于慢性疲劳中医证素多标签学习** Wang、Yang 通讯等在 736 例慢性疲劳数据上，用共形预测和随机森林做四个证素的多标签分类，并与共形朴素贝叶斯、共形 k 近邻和 ML-KNN 比较。最高子集准确率为 0.9959，但只做了留一交叉验证。补充材料提供数据。许可为 CC BY。 [华侨大学计算机科学与技术学院，厦门大学信息科学与工程学院，厦门大学中医系] [[DOI](https://doi.org/10.1371/journal.pone.0099565)] [[论文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0099565)]
- [*IEEE BIBM*] **视频面部特征的中医望神分类** 用视频里的面部特征做中医望神的自动分类。视频没有公开。 [[DOI](https://doi.org/10.1109/bibm.2014.6999314)]
- [*arXiv*] **用伽马密度拟合中医脉图** 把中医脉图当作波形，用多维变量分析，以伽马密度函数拟合脉图，用来形成可计算的脉象分类指标。 [[论文](https://arxiv.org/abs/1402.6649)]
- [*IEEE CIBCB*] **深度卷积网络分析腕部脉波** 用香农能量包络和希尔伯特变换抽出腕部脉波，再用深度卷积网络做中医脉诊识别。 [[DOI](https://doi.org/10.1109/cibcb.2014.6845525)]
- [*Evidence-Based Complementary and Alternative Medicine*] **小波包分形维的闻诊** 用小波包分形维和支持向量机，把中医闻诊里的声音做成可计算的证候判断。2014 年发表。 [[DOI](https://doi.org/10.1155/2014/502348)]
- [*International Journal of Pattern Recognition and Artificial Intelligence*] **均匀色空间的中医面色识别** 在均匀 Lab 色空间里识别中医面色。面像没有公开。 [[DOI](https://doi.org/10.1142/s0218001414500086)]
- [*IEEE ICCA*] **冠心病、其他心血管病与健康人的脉象参数** 用压力传感器采集 251 人的脉图：冠心病 102 人、非冠心病的心血管病 94 人、健康人 55 人，比较三组脉象参数。脉图没有公开。 [[DOI](https://doi.org/10.1109/icca.2014.6871077)]
- [*Evidence-Based Complementary and Alternative Medicine*] **中风患者韩医四诊的观察者一致性** 两名医师独立检查 168 名中风住院患者。脉诊体征的 AC1 为 0.66–0.89，望诊 0.66–0.95，闻诊 0.67–0.88，问诊 0.62–0.94。这是一致性研究，不是公开标注集。 [Korea Institute of Oriental Medicine] [[DOI](https://doi.org/10.1155/2014/465471)]
- [*BioMed Research International*] **中医面色的定性与定量分析** 用计算机对面色的颜色和光泽做定性和定量识别，以减少只靠经验望诊的主观性。 [[DOI](https://doi.org/10.1155/2014/207589)]
- [*Journal of Biomedical Informatics*] **中医症状名识别** 自由文本中医临床记录中症状名识别的监督方法 [四川大学，成都中医药大学，Sichuan Agricultural University，Beihua University] [[DOI](https://doi.org/10.1016/j.jbi.2013.09.008)]
- [*Ru J et al., *J Cheminform* 6(1):13*] **TCMSP** TCMSP（platform阶段历史锚点） [North West Agriculture and Forestry University，Northwest A&F University，Dalian University of Technology，Dalian University] [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- [*Comput. Math. Methods Med.*] **Pulse Waveform Classification Using Support Vector Machine with Gaussian Time Warp Edit Di** GTWED-SVM 在 2470 条五类脉波上的弹性核分类。 [Harbin Ice Flower Hospital, Harbin 150086, China，哈尔滨工业大学] [[DOI](https://doi.org/10.1155/2014/947254)]
- [*Evid. Based Complement. Alternat. Med.*] **A disturbance rejection framework for the study of traditional Chinese medicine** 用工程控制论“抗扰”隐喻解释五行调控与治法逻辑。 [Cleveland State University，北京中医药大学] [[DOI](https://doi.org/10.1155/2014/787529)]
- [*Journal of Alternative and Complementary Medicine*] **用声学特征辨体质** 从语音的声学特征辨认中医体质。2013 年发表。 [[DOI](https://doi.org/10.1089/acm.2012.0478)]
- [*Evidence-Based Complementary and Alternative Medicine*] **方剂网络中的十八反与十九畏** 用 362 首方剂建成方剂网络，并从化学空间和代谢空间考察十八反、十九畏药对。 [[DOI](https://doi.org/10.1155/2013/352145)]
- [*Xue R et al., *Nucleic Acids Res* 41(D1):D1089-D1095*] **TCMID** TCMID（platform阶段历史锚点） [Shanghai Jiao Tong University，四川大学，Shanghai Mental Health Center，华东师范大学] [[DOI](https://doi.org/10.1093/nar/gks1100)]
- [*BMC Complementary and Alternative Medicine*] **面像、体型、声音和问卷融合的四象体质辨识** 韩国韩医学研究院在 23 家韩医诊所收集 2973 名患者的面像、体型、声音和问卷，分别建四象体质模型后再融合。测试集男性准确率 64.0%，女性 55.2%。图像和问卷没有公开下载。 [Korea Institute of Oriental Medicine] [[DOI](https://doi.org/10.1186/1472-6882-12-85)]
- [*Bioinformation*] **基于结构相似的中药心血管毒性预测软件** 按化学结构相似性做软件，预测中药的心血管毒性。 [[DOI](https://doi.org/10.6026/973206300080110)]
- [*BMC Complementary and Alternative Medicine*] **唇色的中医望诊分类** 用多类支持向量机，按唇色做中医望诊。2012 年发表。 [[DOI](https://doi.org/10.1186/1472-6882-12-127)]
- [*Evid. Based Complement. Alternat. Med.*] **Automated Tongue Feature Extraction for ZHENG Classification in Traditional Chinese Medici** 舌象颜色特征学习映射寒热证（ZHENG）的代表性工作。 [清华大学] [[DOI](https://doi.org/10.1155/2012/912852)]
- [*China Journal of Chinese Materia Medica*] **胸痹处方中的十八反关联规则** 用关联规则查看胸痹处方里十八反药对的出现规律。 [[DOI](https://doi.org/10.4268/cjcmm20112434)]
- [*Chinese Medicine*] **用关联开放数据整合传统医药与现代药学研究（评论）** Samwald 通讯等。2010 年发表于 Chinese Medicine 的评论，用寻找潜在抗抑郁中药植物的用例，讨论关联开放数据。作者手工编码 76 条断言，并与 TCMGeneDIT 的 RDF 版互链。这是评论兼小型原型，不是已完成的药物发现。许可为 CC BY 2.0。 [爱尔兰国立大学戈尔韦分校数字企业研究所，耶鲁大学医学院医学信息学中心] [[DOI](https://doi.org/10.1186/1749-8546-5-43)] [[论文](https://cmjournal.biomedcentral.com/articles/10.1186/1749-8546-5-43)]
- [*BMC Bioinformatics*] **DMIM 药物网络与共模块分析（李梢等）：揭示中医方剂组合规则** 李梢通讯、Zhang、Jiang、Wei、Zhang 提出 DMIM，从 3865 首络病相关方剂构建药物网络，并以六味地黄方为例讨论多层网络共模块。体外实验报告蔓荆子黄素 IC50 3.2 μM、知母皂苷 A-III IC50 3.4 μM，为作者自报。不能与同年 drugCIPHER、TCMSP、HERB 或本站 2026 年 DeepTCM 合并。人物页李梢未改。 [清华大学自动化系，教育部生物信息学重点实验室，清华大学信息科学与技术国家实验室（TNLIST）] [[DOI](https://doi.org/10.1186/1471-2105-11-S11-S6)] [[论文](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-S11-S6)]
- [*PLoS ONE*] **drugCIPHER（Zhao、李梢）：关联药理空间与基因组空间的药物靶点推断框架** Zhao、李梢提出 drugCIPHER，用线性回归把药物治疗／化学相似性与蛋白质相互作用网络上的接近度关联起来，以在全基因组尺度推断药物靶点。这是 2010 年一般药理学方法，被后续中医药综述引用，不能与本站 TCMSP 或 2026 年 DeepTCM 合并。 [清华大学自动化系，教育部生物信息学重点实验室，清华大学信息科学与技术国家实验室（TNLIST）] [[DOI](https://doi.org/10.1371/journal.pone.0011764)] [[论文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0011764)]
- [*Chinese Medicine*] **语义网用于中医药数据协调（社论）** Cheung 通讯、Chen。2010 年发表于 Chinese Medicine 的社论，主张用语义网表示并协调中西医数据。文中引用 DartGrid，并写中国中医科学院本体有 8,000 余类、50,000 余实例，与本站已有 2007 年系统论文自报数字不同。这是短篇社论，没有新数据或评测。许可为 CC BY 2.0。 [耶鲁大学医学院医学信息学中心，浙江大学计算机学院] [[DOI](https://doi.org/10.1186/1749-8546-5-2)] [[论文](https://cmjournal.biomedcentral.com/articles/10.1186/1749-8546-5-2)]
- [*BMC Complementary and Alternative Medicine*] **冠心病问诊的多标签学习** 用多标签学习给冠心病的中医问诊诊断建模。2010 年发表。 [[DOI](https://doi.org/10.1186/1472-6882-10-37)]
- [*BMC Bioinformatics*] **中医病历症状名自动规范化** 把中医电子病历里的症状名自动规范到统一术语，以便从病历而不是只从手工整理的方剂里做挖掘。 [[DOI](https://doi.org/10.1186/1471-2105-11-40)]
- [*Journal of Biomedical Informatics*] **Text mining for traditional Chinese medical knowledge discovery: a survey** 中医文本挖掘方法与语料资源的早期系统综述。 [北京交通大学，University of Bradford，中国医学科学院] [[DOI](https://doi.org/10.1016/j.jbi.2010.01.002)]
- [*Journal of Chinese Integrative Medicine*] **Feature extraction and recognition of traditional Chinese medicine pulse based on hemodyna** 以波速与反射系数作脉象特征并用 SVM 识别弦/滑/平脉。 [[链接](http://www.jcimjournal.com/EN/10.3736/jcim20100802)]
- [*Artificial Intelligence in Medicine*] **Development of traditional Chinese medicine clinical data warehouse for medical knowledge ** 临床数据仓库支撑知识发现与决策支持的系统论文。 [北京交通大学，中国中医科学院，北京中医药大学，Guang’anmen Hospital] [[DOI](https://doi.org/10.1016/j.artmed.2009.07.012)]
- [*EURASIP J. Adv. Signal Process.*] **Classification of Pulse Waveforms Using Edit Distance with Real Penalty** ERP 编辑距离应对脉波局部时移的经典波形分类。 [哈尔滨工业大学] [[DOI](https://doi.org/10.1155/2010/303140)]

</details>

<details>
<summary>2000s · 13</summary>

- [*Evidence-Based Complementary and Alternative Medicine*] **用面部几何特征区分四象体质** 从面部照片提取距离、角度和距离比，用来区分四象体质。摘要给出的特征规模是距离 1225 项、角度 61250 项、距离比 749700 项。面像没有公开。 [Korea Institute of Oriental Medicine] [[DOI](https://doi.org/10.1093/ecam/nep065)]
- [*IEEE CSIE*] **Syndrome Differentiation in Intelligent TCM Diagnosis System** 区间值直觉模糊集用于智能中医辨证决策。 [Xiamen University] [[DOI](https://doi.org/10.1109/csie.2009.782)]
- [*Int. J. Information Technology & Decision Making*] **Equilibrium and nonequilibrium modeling of YinYang WuXing for diagnostic decision support ** 双极线性代数刻画阴阳五行均衡/非均衡并原型化诊断 DSS。 [中国科学院] [[DOI](https://doi.org/10.1142/s0219622009003521)]
- [*IEEE ITME*] **Traditional Chinese medical diagnosis based on fuzzy and certainty reasoning** 多层模糊筛选+多智能体协作诊断（MADHS）原型。 [Memorial University of Newfoundland] [[DOI](https://doi.org/10.1109/itme.2008.4743874)]
- [*WWW* (demo/industrial)*] **Information retrieval and knowledge discovery on the semantic web of traditional Chinese m** 大规模中医语义网与草药—药物相互作用图谱挖掘。 [浙江大学] [[DOI](https://doi.org/10.1145/1367497.1367668)]
- [*Journal of Chinese Integrative Medicine*] **Establishment of a fuzzy mathematical model for syndrome differentiation of gastric cancer** 基于临床大样本的胃癌证候模糊数学模型，服务辨证客观化。 [[链接](http://www.jcimjournal.com/EN/10.3736/jcim20081104)]
- [*IEEE BMEI*] **Building Clinical Data Warehouse for Traditional Chinese Medicine Knowledge Discovery** 结构化病历驱动的中医临床数据仓库与 OLAP/挖掘平台。 [北京交通大学，中国医学科学院，Guang’anmen Hospital，北京中医药大学] [[DOI](https://doi.org/10.1109/bmei.2008.83)]
- [*BMC Bioinformatics*] **面向中医药的语义电子科研** Chen 通讯等报告基于本体、语义视图和网格服务的中医药电子科研系统，工具包括 DartMapping、DartSearch、DartQuery 和 DartFlow。作者自报本体有两万余类、十万实例，系统接入 50 余个数据库和 800 个服务。这是系统描述，没有独立定量评测。许可为 CC BY 2.0。 [浙江大学计算机学院，中国中医科学院] [[DOI](https://doi.org/10.1186/1471-2105-8-S3-S6)] [[论文](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-S3-S6)]
- [*World Health Organization*] **WHO 西太区传统医学术语** 世界卫生组织西太平洋区 2007 年的传统医学国际标准术语，是 2022 年中医药术语之前的一版。PDF 可以从 IRIS 打开。 [[网站](https://iris.who.int/handle/10665/206952)] [[PDF](https://iris.who.int/server/api/core/bitstreams/24400634-2d52-4dde-bbb1-d28ee2c6fd42/content)]
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
<summary>公开资料整理（6）</summary>

- **针灸临床实践指南数据集** — 把针灸临床实践指南整理成数据集，以便在临床上直接使用。 [[论文](https://doi.org/10.1038/s41597-026-08112-3)]
- **中成药公开数据集（RAG-CPMF）** — RAG-CPMF配套的持续更新大规模中成药公开数据 [[数据](https://gitee.com/tcmdoc/cpm)] [[论文](https://doi.org/10.1016/j.phrs.2025.107883)]
- **awesome_Chinese_medical_NLP** — 中文医学 NLP 公开资源整理：术语集、语料库、词向量、预训练模型、知识图谱、NER、QA 等（含 CBLUE 挑战榜） [[资料](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)]
- **内蒙古自治区民族药目录** — 内蒙古自治区医疗保障局公开的民族药目录，以蒙医成方为主。公开稿日期为2023年12月25日。正文标题是内蒙古自治区民族药目录，备注写明目录内民族药按乙类管理。这是医保收载目录，不是蒙药成分研究库。 [[目录](https://ylbzj.nmg.gov.cn/zwgk/zfxxgk/fdzdgknr/bmwj/202312/P020231225623619008689.pdf)]
- **中医药中英术语数据集** — 中国科学数据发布的中医药中英术语对照数据集。 [[论文](https://doi.org/10.11922/csdata.2021.0009.zh)]
- **中医体质量表计分代码** — 中医体质量表 CCMQ 的 SAS 代码、SPSS 语法和一份 Excel 测试表，用来按问卷计算体质。2021 年 1 月发布，许可 CC BY 4.0。 [[DOI](https://doi.org/10.5281/zenodo.4431679)] [[数据](https://zenodo.org/records/4431679)]

</details>

<details>
<summary>中药组方 / 提取物（46）</summary>

- **中药扰动转录组图谱** — 汇集公开库中的中药处理转录组，用于解释中药干预的分子机制。 [[论文](https://doi.org/10.1038/s41597-026-06988-9)]
- **中药化学成分毒性实验库** — 从公开毒理学文献整理的中药化学成分毒性实验记录，含体内和体外实验。示例药物包括闹羊花、斑蝥、巴豆、洋金花、附子和轻粉。字段有给药途径、实验物种、LD50 等毒性指标、毒性剂量、靶器官和病理表现，并保留 PMID。 [[数据集](https://doi.org/10.57760/sciencedb.015ml)]
- **中医世家** — 在线查阅中医古籍、药材、方剂和医案。方剂索引 25425 项，可按首字或拼音找；药材索引 11307 项。 [[网站](https://www.zysjw.com.cn/)] [[方剂](https://www.zysjw.com.cn/zhongyaofang/index.html)] [[药材](https://www.zysjw.com.cn/zhongyaocai/index.html)]
- **TCMToxDB** — 中药毒性与安全使用数据库，区分方剂、饮片和成分的毒性，并按毒性表现整理靶点。站内集成五种药–靶、成分–靶预测算法。 [[论文](https://doi.org/10.1093/database/baag019)] [[网站](https://www.sdu-idea.cn/TCMToxDB)]
- **TCMDI** — 用机器学习预测中药—西药禁忌相互作用的基准。 [[数据集](https://github.com/hellowangqian/TCMDI)]
- **TCM-QM** — 3196个中药相关分子的气相DFT描述符，并附16918条去重后的草药—分子来源关系。 [[数据集](https://zenodo.org/records/22173180)]
- **TCM-MS2Link** — 把中药—化合物知识层TCM-MolLink与质谱数据收成可供模型使用的统一数据集。 [[数据集](https://doi.org/10.57760/sciencedb.31921)]
- **Cross-linguistic TCM Formula Names** — 中医方剂名称的跨语言对照表，覆盖中文、日本汉方、韩国韩医和英文，Zenodo 说明依据台湾官方方剂书和常用临床文献整理，文件为 xlsx。 [[数据集](https://zenodo.org/records/18724305)]
- **CHM-315** — 中药材细粒度图像集，DataCite 说明包含 315 类常用中药、共 126000 张图像，每类 400 张。 [[数据集](https://doi.org/10.6084/m9.figshare.32745123)]
- **Baize TCM Botanical Origin Images** — 药用植物基原鉴定图像数据，DataCite 标题写明用于 Baize Traditional Chinese Medicine，包含生境、原植物和药用部位图像，以及依据中国药典、中国植物志和恩格勒系统的中文与拉丁文鉴定信息。 [[数据集](https://doi.org/10.57760/sciencedb.41638)]
- **古代经典名方关键信息表** — 官方公布的经典名方关键信息，不是患者病历。三份通知分别是 2020 年 7 首、2023 年「竹叶石膏汤」等 25 首、2025 年「旋覆代赭汤」等 43 首。2025 年附表逐味给出基原、炮制规格和折算剂量。旋覆代赭汤中甘草为炒甘草 41.40 克、半夏为清半夏 34.50 克；全方以水 2000 毫升煮取 1200 毫升，去渣再煎至 600 毫升，每次温服 200 毫升、日三服。 [[2020通知](http://www.natcm.gov.cn/kejisi/zhengcewenjian/2020-11-10/18132.html)] [[2023通知](http://www.natcm.gov.cn/kejisi/gongzuodongtai/2023-07-28/31404.html)] [[2025通知](http://www.natcm.gov.cn/kejisi/gongzuodongtai/2025-02-12/35831.html)] [[2025PDF](https://www.nmpa.gov.cn/directory/web/nmpa/images/1739501159108056814.pdf)]
- **传统方剂—疾病关系标注语料** — 从生物医学文献标注传统方剂与疾病关系的语料，方剂按传统医学原则配伍。 [[论文](https://doi.org/10.1038/s41597-025-04377-2)]
- **TCMP-300** — 用于中药材植物识别的综合图像数据集。 [[论文](https://doi.org/10.1038/s41597-025-05522-7)] [[代码](https://github.com/winycg/TCMP-300)]
- **NPASS** — 天然产物的实验活性库。这一版有天然产物 204023 个、来源生物 48940 个、靶点 8764 个、活性记录 1048756 条，活性数值来自 ChEMBL 和文献。物种来源接过 TCM-ID、TCMID、TCMSP、TM-MC 等库。2026 年更新的论文在 2025 年 11 月登在 Nucleic Acids Research。 [[网站](https://bidd.group/NPASS/)] [[说明](https://bidd.group/NPASS/about.php)] [[DOI](https://doi.org/10.1093/nar/gkaf1196)]
- **HERB 2.0 本草组鉴** — 整合临床试验、荟萃分析、高通量实验与文献的中药证据库，并提供实体关系知识图谱 [[网站](http://herb.ac.cn/v2)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC11701625/)] [[DOI](https://doi.org/10.1093/nar/gkae1037)]
- **中医证候标准化数据库** — 浙江中医药大学作者发表的证候标准化综合库。论文报告624个证候、133518首方剂、8073种疾病、8259味中药、43413个成分和17602个靶点。站点可打开，前端脚本含证候与 TCMSSD 内容；未启用脚本时页面为空。本次未看到整库下载入口。 [[网站](http://tcmssd.ratcm.cn/)] [[DOI](https://doi.org/10.1016/j.phymed.2024.155486)]
- **中药植物基因组数据库 2.0** — 成都中医药大学等维护的中药植物基因组库。现行首页写明274种植物、324个基因组、414味药材和13809个成分，并提供 BLAST、JBrowse 等工具。2024年论文描述 2.0 升级。站点可浏览和分析；本次未核到整库打包下载。 [[网站](https://cbcb.cdutcm.edu.cn/TCMPG2/)] [[DOI](https://doi.org/10.48130/mpb-0024-0004)]
- **CMAUP 有用植物集体分子活性库** — BIDD的有用植物（含中药）多靶点活性、通路与疾病景观库，2024版扩展功能与关联信息，站点可下载 [[网站](https://www.bidd.group/CMAUP/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767869/)] [[DOI](https://doi.org/10.1093/nar/gkad921)]
- **BATMAN-TCM 2.0 中药成分–靶点注释库** — 已知与预测的中药成分–靶蛋白相互作用库，2.0大幅扩充TTI覆盖并支持由靶反查成分 [[网站](http://bionet.ncpsb.org.cn/batman-tcm/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767940/)] [[DOI](https://doi.org/10.1093/nar/gkad926)]
- **TCMBank 中药–成分–靶点–疾病库** — 可下载的大规模中药–成分–靶点–疾病关系库，含文献自动抽取后人工核对的持续更新模块 [[网站](http://tcmbank.cn/)] [[DOI](https://doi.org/10.1038/s41392-023-01339-1)]
- **ITCM 整合中医药与药效转录组平台** — 整合多方剂/药材/成分/靶点，并提供496个中药成分的1488条药理转录谱；成分表达数据另见Synapse [[网站](http://itcm.biotcm.net/)] [[DOI](https://doi.org/10.1093/bib/bbad027)]
- **ETCM 2.0 中医药百科全书** — 收录古代方剂、中成药、药材与成分，并提供成分靶点与多尺度网络；v1站点仍在，现行入口为ETCM2 [[网站](http://www.tcmip.cn/ETCM2/front/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10326295/)] [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)]
- **DCABM-TCM 中药入血成分与代谢物库** — 文献挖掘的方剂/草药入血原型与代谢物及其检测条件（约1816个有结构入血成分） [[网站](http://bionet.ncpsb.org.cn/dcabm-tcm/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10428213/)]
- **藏药材资源数据库** — 中国科学院西北高原生物研究所藏药研究重点实验室公开的藏药材名录（藏医）。页面为学名、拉丁名、药材名和药用部位表，并写明共15页；条目链接路径为2022年3–4月。这是药材名录，不是成分–靶点库。 [[网站](https://nwipb.cas.cn/zy/zyc/index.html)]
- **治法–处方与药材剂量表** — 仓库说明写有 23 类治法、400 多个治法亚类、4174 种常用药材及其剂量和来源，经典方 900 首以上，处方特征分 21 类。仓库里有 Treatment.csv 和《治法-处方数据集总表》。 [[数据集](https://github.com/lin-haust/TCM-prescription-datasets)]
- **TCM-Suite** — 把药材鉴定和网络药理放在同一个网站上。Watson 这边现在列着方剂 6692 首、药材 7322 味、化合物 704321 个、蛋白 19319 个、疾病 15437 种。Holmes 用标记基因做药材鉴定。2022 年发表在 iMeta。 [[网站](https://tcm-suite.geneis.cn/)] [[DOI](https://doi.org/10.1002/imt2.47)]
- **SymMap 2.0 症状映射中医药数据库** — 草药、中医症状、西医症状、成分、靶点和疾病的整合库。网站现为 2.0，按《中国药典》2020 年版补充，关系表可以下载。页脚署 2022 年。 [[网站](http://www.symmap.org/)] [[数据](http://www.symmap.org/download/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323958/)]
- **LTM-TCM 中西医分子表型链接库**（官网已挂） — 把十四个中药库，以及临床记录和古籍，接到症状、方剂、植物、成分和靶点上。库里有 1928 个症状、48126 首方、9122 种植物、34967 个成分和 13109 个靶点。cloud.tasly.com 这次域名解析不到。 [[原网站](http://cloud.tasly.com/#/tcm/home)] [[DOI](https://doi.org/10.1016/j.phrs.2022.106185)]
- **HIT 2.0 草药成分靶点库**（服务异常） — 人工审核的草药成分–靶点活性对（约1237成分/2208靶点），覆盖2000–2020文献；门户可打开，分析后端端口当前不通 [[网站](http://hit2.badd-cao.net/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728248/)] [[DOI](https://doi.org/10.1093/nar/gkab1011)]
- **SuperTCM 中药生物文化数据库**（官网已挂） — Charité 把药典和多来源资料收成一个库：6516 味中药、5372 个植物物种、55772 个活性成分、543 个靶点、254 条 KEGG 通路、8634 种疾病。tcm.charite.de 这次域名解析不到。 [[原网站](http://tcm.charite.de/supertcm)] [[论文](https://europepmc.org/article/MED/34656056)] [[DOI](https://doi.org/10.1016/j.biopha.2021.112315)]
- **TCMIO 中医药免疫肿瘤学数据库** — 面向免疫肿瘤的中药/方剂–成分–靶点–通路库，提供浏览、下载与REST API [[网站](http://tcmio.xielab.net/)] [[数据](http://tcmio.xielab.net/download)] [[DOI](https://doi.org/10.3389/fphar.2020.00439)]
- **Sowa Rigpa Materia Medica Dataset** — Data in Brief 公开的藏医（Sowa Rigpa）常用本草拉丁学名数据集。论文从《四部医典》等经典和嘎务多吉的本草分类里选出近 700 种常用药，给出藏文、Wylie 转写和拉丁学名，补充材料随文发布。作者来自甘肃中医药大学藏医学院、威斯康星大学麦迪逊分校和青海民族大学药学院。数据来源地写的是成都中医药大学民族医药学术传承创新研究中心。 [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC7689029/)] [[DOI](https://doi.org/10.1016/j.dib.2020.106498)]
- **傣药基原植物数据库**（服务异常） — 中国科学院西双版纳热带植物园在植物园联盟平台上的傣药基原植物库（傣医）。首页版权为2018年，简介写明傣医四塔、五蕴与解药理论。物种列表地址返回跳转提示，匿名状态下未见可浏览的物种清单。 [[网站](https://espc.cubg.cn/daim/index/index.html)]
- **YaTCM 中药方剂–成分–靶点库**（官网已挂） — 1813 首方、6220 味药、47696 个天然产物，并带靶点和通路分析。南开原站这次返回 403。 [[原网站](http://cadd.pharmacy.nankai.edu.cn/yatcm/home)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6280608/)] [[DOI](https://doi.org/10.1016/j.csbj.2018.11.002)]
- **TCMID 2.0 中医药整合数据库**（官网已挂） — 华东师范大学团队做的方剂、草药、成分和靶点库。数据和介绍在 Zenodo 与 Nucleic Acids Research 的论文里。名字和新加坡的 TCM-ID 容易看混，这是两个库。原站 megabionet.org/tcmid 这次打开超时。 [[原网站](http://www.megabionet.org/tcmid/)] [[数据](https://zenodo.org/records/8066910)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5753259/)] [[DOI](https://doi.org/10.1093/nar/gkx1028)]
- **TCMAnalyzer 中药化学信息学分析平台**（官网已挂） — 中山大学药物研发中心的网络分析工具。可以按骨架查一味药里可能有活性的成分，也能把分子、靶点、通路和疾病连成图。rcdd.org.cn 这次打开超时。 [[原网站](http://www.rcdd.org.cn/tcmanalyzer)] [[论文](https://pubmed.ncbi.nlm.nih.gov/29420025/)] [[DOI](https://doi.org/10.1021/acs.jcim.7b00549)]
- **香港浸会大学中药方剂图像数据库** — 香港浸会大学中医药学院的方剂图像库，公开浏览方剂组成、功用、主治和图像。浏览页显示约182首，访问计数自2017年11月起。在线查阅，不是方剂表批量下载。 [[网站](https://library.hkbu.edu.hk/electronic/libdbs/cmfid/)]
- **TCM-Mesh 中药网络药理学分析库**（官网已挂） — 做中药复方的网络药理。库里有 6235 味药、383840 个化合物、14298 个基因、6204 种疾病，以及 163221 条副作用记录和 71 条毒性记录。原站这次返回 403。 [[原网站](http://mesh.tcm.microbioinformatics.org/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5460194/)] [[DOI](https://doi.org/10.1038/s41598-017-03039-7)]
- **TM-MC 东北亚传统药物成分库** — 韩国韩医学研究院从文献抽取的东北亚药材和化合物库。2015 年初版约 536 种药材，2024 年的 2.0 扩到约 3.4 万个化合物。旧网址写明数据和服务已迁到 tm-mc.kr。 [[网站](https://tm-mc.kr)] [[原网站](http://informatics.kiom.re.kr/compound/)] [[DOI](https://doi.org/10.1186/s12906-015-0758-5)] [[2.0论文](https://doi.org/10.1186/s12906-023-04331-y)]
- **CEMTDD 中国少数民族传统药物数据库** — 以维吾尔药、哈萨克药等民族药为主的草药、化合物、靶点和疾病库，论文写约 621 味草药。 [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627337/)] [[DOI](https://doi.org/10.18632/oncotarget.3789)]
- **TCMSP 中药系统药理学数据库** — 查中药成分、靶点和疾病关系的药理学库，也给 ADME 参数。网站上现在同时放着旧版 2.3 和新版 9.0.1，关系表可以下载。 [[网站](https://www.tcmsp-e.com/tcmsp.php)] [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- **香港浸会大学中药材图像数据库** — 香港浸会大学中医药学院的中药材图像库。图书馆页面写明收录常用中药材420余种，包括来源、产地、性状、性味功效和高清图像，可按中文名、拉丁名和英文名检索。2013年上线，可公开在线浏览，不是批量下载包。 [[网站](https://library.hkbu.edu.hk/electronic/libdbs/mmd/)]
- **CVDHD 心血管病本草数据库**（官网已挂） — 收心血管相关本草里分出来的天然产物，用来做虚拟筛选和网络药理。有 35230 个化合物的三维结构，并对接到 2395 个靶蛋白，同时连着疾病、通路和临床标志物。原北大站点这次打开超时。 [[原网站](http://pkuxxj.pku.edu.cn/CVDHD)] [[DOI](https://doi.org/10.1186/1758-2946-5-51)]
- **TCM Database@Taiwan 中药三维结构库**（官网已挂） — 从 453 味药材里收了 2 万多种纯化合物，每种都有二维和三维结构，用来做虚拟筛选。原站 tcm.cmu.edu.tw 这次打开超时。 [[原网站](http://tcm.cmu.edu.tw/)] [[论文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0015939)] [[DOI](https://doi.org/10.1371/journal.pone.0015939)]
- **TCMGeneDIT 中药–基因–疾病文本挖掘库**（官网已挂） — 从文献里把中药、基因、疾病、功效和成分对上，并接上通路和蛋白相互作用。tcm.lifescience.ntu.edu.tw 这次域名解析不到。 [[原网站](http://tcm.lifescience.ntu.edu.tw/)] [[论文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2584015/)] [[DOI](https://doi.org/10.1186/1472-6882-8-58)]
- **TCM-ID 中医药信息数据库（NUS BIDD）** — 新加坡BIDD维护的方剂–药材–成分–靶点库，含药典/经典方与CFDA批准方；与TCMID 2.0不是同一资源 [[网站](https://www.bidd.group/TCMID/)]

</details>

<details>
<summary>临床结构化 / 处方（13）</summary>

- **赵汉青门诊处方（2025）** — 赵汉青 2025 年中医内科门诊的去标识处方：122 名患者、335 张处方、5951 条药味记录，每味药有克剂量。初诊 75 张、复诊 260 张。给药途径以口服汤剂为主（315 张），另有冲服 8 张、外洗 8 张、外用 4 张。每日两次 333 张，每日三次 2 张。药名里能看到炮制写法，含「炒」412 行、「炙」341 行、「麸」289 行、「醋」164 行、「姜」154 行、「酒」89 行、「煅」67 行、「制」63 行，另有法半夏 99 行；同一行可以同时含多个字。CC BY 4.0。仓库说明就诊机构为 Beijing Heniantang Hospital。 [[数据集](https://doi.org/10.5281/zenodo.21947836)] [[代码](https://github.com/zhhqtt/zhao-hanqing-tcm-dataset-2025)]
- **胆石症中医证候代谢组** — 胆石症患者肝郁气滞与肝胆湿热两种证候的血清和尿液代谢组数据。 [[论文](https://doi.org/10.1038/s41597-025-06537-w)]
- **汉派中医骨伤诊疗数据集** — 武汉市中医医院数据产品；报道包含16.8万条结构化诊疗数据、3600个经验方与汉派骨伤辨证思维链，已在湖北数据流通平台完成交易。仅核验发布报道，未发现可匿名批量下载的数据包。 [[新闻](https://www.cntcm.com.cn/content/202610/16/c505880.html)]
- **广安门医院慢性胃炎数据集** — 2026年完成产权登记的中医专病数据集，用于科研与大模型领域适配。报道区分院内使用、院外协同科研和产品交易，未给本数据集规模或公开下载；医院总体资源量不能当作该集样本数。 [[新闻](https://www.cntcm.com.cn/content/202609/24/c505607.html)]
- **古今医案云平台** — 中国中医科学院中医药信息研究所的医案检索、结构化与挖掘平台。该所2026年9月20日新闻写明，现行资源已形成110余万条高质量结构化古今医案，另有1963万条科研分析数据，注册用户约5.3万人。需注册或机构登录，未见公开批量下载。部分院校试用页仍写约50万条，与这一口径不同。 [[网站](https://www.yiankb.com/)]
- **TCMCPD** — 从病案整理的结构化库：4895 名患者、12900 次就诊、703 味中药，就诊–证候 11879 条，就诊–药味 63192 条。剂量单位以克为主（61386），另有钱 1067、枚 364、片 240、两 69、分 64、毫升 2。并连接症状、成分和靶点，附 Neo4j 节点和边。作者说明不转发受版权限制的医案原文。描述稿目前是 Research Square 预印本。 [[数据集](https://doi.org/10.5281/zenodo.20929034)]
- **TCM4NSCLC** — 来自一位资深中医门诊的 3,790 条非小细胞肺癌病例记录，包含重复就诊，用于辨证、处方及真实世界研究。 [[论文](https://doi.org/10.1038/s41597-026-07912-x)]
- **TCM-Andrology-EMR** — 数据卡报告67,073次就诊、25,103名患者，金标准26,923条，提供按患者切分的JSONL；药味无剂量，舌脉字段稀缺。作者明确未做伦理审查与患者知情同意；仅作资源索引，数据来源与再利用依据需进一步核实。 [[数据集](https://huggingface.co/datasets/johnson/TCM-Andrology-EMR)]
- **AcuiQ** — 从已发表文献中抽取的针灸选穴索引，按症状检索。每条记录附出处和证据类型（研究、典籍、网页、无来源），并记录原文的施治方式（针刺、电针、艾灸、指压等）和疗程。匿名使用，无需账号，提供 MCP 服务器和 REST API。数据库对十一条规范的偏离率登记表以 CC BY 4.0 公开。站内另售付费指南。 [[网站](https://acuiq.com)] [[MCP](https://acuiq.com/api/mcp)] [[API](https://acuiq.com/openapi.json)] [[数据](https://acuiq.com/wiki/research/conformance)]
- **六经辨证数据集** — 中医六经辨证数据集。 [[数据集](https://github.com/JustinWYJ/TCMdataset)]
- **TCM-Lung 肺系病辨证处方编码集** — 河南中医药大学一附院肺系病案处理后 14948 条，仓库公开 4484 条编码（症状/证候/治法/处方 ID）；全名需邮件申请。与 TCMNSCLC 不是同一份数据 [[代码](https://github.com/2020MEAI/PresRecST)] [[论文](https://doi.org/10.1093/jamia/ocae066)]
- **Famous Old TCM Doctors Cases** — 来源于《当代名老中医典型医案集》的当代名老中医门诊病案，数据卡写明每案含病情描述、辨证论治思路和治疗方药。 [[数据集](https://huggingface.co/datasets/TCMLM/real_clinical_cases_of_Famous_Old_TCM_Doctors)]
- **TCM-PD / PTM 方剂–症状推荐集** — Yao 等 TKDE 2018 处方主题模型配套数据：原始 98334 首、预处理 33765 首（症状–中药 ID）；CKCEST 版权、仅研究使用。PresRecST 的 prescript_1195.csv 即此集复现表 [[代码](https://github.com/yao8839836/PTM)] [[DOI](https://doi.org/10.1109/TKDE.2017.2787158)]

</details>

<details>
<summary>通用中文医疗（14）</summary>

- **四模型中文医学文献标引测试集** — 从100篇随机中文医学研究论文抽取要点，由四个大模型做抽取和摘要并打准确分。 [[数据集](https://doi.org/10.57760/sciencedb.o00130.03231)]
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
<summary>东亚传统医学（21）</summary>

- **东亚医学协会针灸经络图版库** — 既有资源补录（首发年份未确认）。按经脉并列展示十四经发挥、针灸资生经、类经图翼、经穴汇解和经络研究图版，可用于版本比较和针灸图文资料检索。是历史图版入口，非已标注视觉问答集；未确认统一批量下载及训练许可。 [[网站](https://aeam.jp/keiraku/)]
- **东亚医学协会医学古典文本** — 既有资源补录（首发年份未确认）。官方目录提供素问、灵枢、伤寒论、金匮要略、神农本草经、难经、扁鹊仓公传七类经典入口。抽查伤寒论为可提取文字的79页PDF，说明赵开美本底本；各文本版本与再利用条款需分别确认。 [[网站](https://aeam.jp/koten/)] [[原始文件](https://aeam.jp/wp/wp-content/uploads/2024/03/shanghanlun.pdf)]
- **VTM-TDA Benchmark** — 从杜德利《越南药用植物与药物》整理的越南传统医学计算基准，含724个已与POWO、PubChem等对齐的基原，以及1635条历史处方。 [[数据集](https://zenodo.org/records/23075405)]
- **TreeProbe** — 藏医基准，用来测大模型的文化偏差。 [[论文](https://arxiv.org/abs/2608.00640)]
- **韩医领域嵌入对比学习数据** — 从韩医术语与本体构造的query–positive–negatives（约11.3万对），用于BGE-M3等检索微调 [[数据集](https://huggingface.co/datasets/cnupo23/korean-medicine-embedding-dataset)]
- **医师修订的汉方问诊基准** — 74个汉方问诊场景、310条对话级评分标准，由持证汉方医师修订 [[论文](https://doi.org/10.64898/2026.10.07.26365005)]
- **HerbPairIAM** — 汉方复方药物不良反应信号的成分归因数据与模型产物，Zenodo 记录含 HerbPairIAM zip 及 README。 [[数据集](https://zenodo.org/records/19326537)]
- **健康成人韩医诊察数据集** — 先从文献抽出韩医诊察指标，经三轮专家意见形成方案，再在韩医医院连续四年采集健康成人的诊察数据。 [[论文](https://doi.org/10.3390/healthcare12090918)]
- **VietMedKG** — 越南传统医学知识图谱与基准。 [[数据集](https://github.com/HySonLab/VietMedKG)]
- **Polyglot Asian Medicine Knowledge Graph** — 2023年公开的多语亚洲传统与草药知识图谱门户，当前以中药为主并扩展至马来与东南亚药物，连接名称、学名、药用部位、文献出处与地理信息。 [[数据](https://kgraph.sg/polyglot/)] [[论文](https://doi.org/10.1007/978-981-99-8088-8_1)]
- **京都大学富士川文库数字古医书** — 京都大学古医书数字馆藏，含和汉医书及医学史资料；官方说明2018年4月完成数字化公开，并介绍与庆应义塾大学的IIIF联合展示。适合版本、影像及OCR研究，不能把馆藏部册数当成已清洗中医文本数。 [[网站](https://rmda.kulib.kyoto-u.ac.jp/collection/fujikawa)]
- **KampoDB** — 富山大学和汉医药学综合研究所维护的汉方作用机制库，整合处方、生药、天然化合物与靶蛋白，含已知相互作用和对接预测。关于页当前统计为汉方298首、生药180种、天然化合物3002个、蛋白或基因62906个、对接结果3063505条。2018年 Scientific Reports 论文为首篇描述；站点新闻写明2021年7月15日改版。 [[网站](https://wakanmoview.inm.u-toyama.ac.jp/kampo/)] [[关于](https://wakanmoview.inm.u-toyama.ac.jp/kampo/about/)] [[DOI](https://doi.org/10.1038/s41598-018-29516-1)]
- **韩医药素材银行药材目录 (KMMB)** — 韩国韩医药振兴院的韩医药素材银行。2016年1月1日由天然物物质银行与韩方生物素材银行合并而成。药材检索页现有 691 条，字段有药材名、异名、学名、基原植物和反应酶。 [[药材目录](https://kminfra.nikom.or.kr/kmmb/module/herbs/index.do?menu_idx=11)]
- **KMCRIC** — 庆熙大学韩医药融合研究信息中心的数据门户。数据中心页列出循证韩医文献库（收录2010年起的系统评价、随机对照试验和机制研究）、基于 Natural Standard 的韩药相互作用库、依据2008年WHO西太区标准穴位制作的取穴视频，以及庆熙大学与忠北大学药学院合作的生药更新库。中心长介绍写明2013年起任该中心所长。 [[数据中心](https://www.kmcric.com/database/data_main)] [[中心介绍](https://www.kmcric.com/about/head_of_centre)]
- **药用植物综合信息数据库 (MPDB)** — 医薬基盤·健康·营养研究所药用植物资源研究中心的汉方与生药综合图鉴。首页写明收录药用植物、生药、成分与基因、栽培和内部形态，并对国内流通的模型生药做了实测；页脚版权为2012–2025，资助来自厚生劳动科学研究费。另有可打开的汉方处方列表和日本药局方收载生药列表。 [[网站](https://mpdb.nibn.go.jp/)] [[汉方列表](https://mpdb.nibn.go.jp/mpdb-bin/list_data.cgi?category=syohou&lang=)] [[药局方生药](https://mpdb.nibn.go.jp/mpdb-bin/list_data.cgi?category=jplist&lang=ja)]
- **TradMPD**（官网已挂） — 富山大学和汉医药学综合研究所的传统医药数据库。文部科学省区域创新集群计划在2008–2012年资助。库里有生药基原、性味归经、汉方组成、适应和文献，处方文献一万余篇。和汉药实验文库含近80个化合物，以及80种生药热水提取物和80个汉方提取物的化学与生物测定，2024年起提供生物测定下载。数据库站点这次返回 503，研究所门户仍列出这个地址。 [[网站](https://dentomed.toyama-wakan.net/en/)] [[说明](https://dentomed.toyama-wakan.net/index_en)]
- **KNApSAcK KAMPO 汉方处方与生药库** — 奈良先端大整理的汉方公开库（约1581处方、278生药），生命科学数据库档案可下载 [[数据集](https://dbarchive.biosciencedbc.jp/data/knapsack-kampo/)] [[DOI](https://doi.org/10.1093/pcp/pcr165)]
- **OASIS 韩国传统医学信息门户** — 韩国韩医学研究院的传统医学文献与资源门户。2007年6月以韩医论文检索系统上线，2009年7月改版为传统医学信息门户，可检索韩医论文与本草资料 [[网站](https://oasis.kiom.re.kr/)]
- **KTKP Traditional Medicine** — 韩国知识产权部的传统知识门户中的韩医部分。英文介绍写明数据库于2005–2007年以韩国传统医学文献编成，2007年12月开始检索服务。介绍页当前结构计数为药材5500、处方7103、病证12500，并关联功效、主治、方药和专利分类号。 [[介绍](https://koreantk.com/ktkp2014/about/introduction.page)] [[药材](https://koreantk.com/ktkp2014/medicine/list-by-act-part.page)] [[处方](https://koreantk.com/ktkp2014/prescription/list-by-index.page)] [[病证](https://koreantk.com/ktkp2014/disease/list-by-index.page)]
- **EKAT** — 日本东洋医学会EBM委员会的汉方治疗证据报告。官网写明2007年起免费公开并持续更新，把在售汉方制剂的随机对照试验和荟萃分析做成结构化摘要；煎剂因品质不明不收，试验限于1986年以后、与市售制剂同品质者。有日文版和英文版，大韩韩医学会另有韩语译本。 [[网站](https://www.jsom.or.jp/ebm/ekat/)]
- **ETHMEDmmm**（官网已挂） — 富山大学和汉医药学综合研究所民族药物资料馆的生药标本库。首页表格写明和汉药461种、8942点，日文公开始于2000年4月；同站另有英文和汉药以及尤纳尼、泰药、阿育吠陀、印度尼西亚生药分库。最终更新说明为2018年3月30日的第7版。站点这次返回 503，研究所门户仍列出这个地址。 [[网站](https://ethmed.toyama-wakan.net/)]

</details>

<details>
<summary>原始书籍 / 预训练语料（17）</summary>

- **数字中医校书郎（CMETA）** — 既有资源补录（首发年份未确认）。中医善本协作校订平台，列有伤寒论多版本、金匮和古今医案按，界面提供Markdown/TXT导出与图文对照。需Google登录；本轮核验公开说明和导出界面，未测试登录后导出。原创校订成果CC BY 4.0，外部影像另行授权。 [[网站](https://cmeta.lctseng.csie.org/)]
- **中国哲学书电子化计划·黄帝内经** — 既有资源补录（首发年份未确认）。黄帝内经章节化全文与相关底本入口，可定位素问篇章并关联影印馆藏。页面英文译文标注AI及用户来源，不能作为专家审定英译金标准；本轮未核验批量导出许可。 [[网站](https://ctext.org/huangdi-neijing)]
- **中华古籍智慧化服务平台** — 既有资源补录（首发年份未确认）。国家图书馆牵头的综合古籍平台，提供全文、版本与知识检索，并列出OCR、句读和版本比对工具。可作为医家类文献补充来源；全库规模不等于中医古籍规模，未验证批量文本导出。 [[网站](https://guji.nlc.cn/)]
- **中医药智慧数字图书馆** — 既有资源补录（首发年份未确认）。中国中医科学院中医药信息研究所门户，提供民国图书、民国再版古籍、影印珍善本、民族医药图书和期刊检索。首页与分类入口可访问，设注册登录；未验证全文访问权限和批量下载。 [[网站](https://tsg.cintcm.cn/)]
- **上海中医药大学馆藏古籍库** — 既有资源补录（首发年份未确认）。学校图书馆介绍馆藏古籍高清扫描库，善本扫描分辨率高于600 DPI。官方入口明确校内校园网或校外VPN访问，适合底本影像核验；属机构资源，不是公开下载语料。 [[说明](https://lib.shutcm.edu.cn/Home/dbdetails/0eb195a0-b9ca-4248-ae41-c356a772cd96)]
- **tc_medical_base** — 五部中医典籍的条文级语料共 3569 条，并带有 sentence-BERT 向量，书目为宋本伤寒论、桂林古本伤寒杂病论、金匮玉函经、金匮要略方论和傅青主女科。 [[数据集](https://huggingface.co/datasets/huckiyang/tc_medical_base)]
- **中医经典全文语料（内经/伤寒/金匮/温病等 115 部）** — 中医经典全文数字化语料：内经、难经、伤寒论、金匮要略及温病经典 [[数据集](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)]
- **Tao-Shanghan-Corpus** — 可下载的《伤寒论》文献语料，把条文、注文和异文分开。2026 年 8 月 11 日发布的 1.0 版有条文记录 681 条，其中正条文 398 条，对齐的历史注文 2958 条，异文 616 条。许可是 CC BY 4.0。 [[DOI](https://doi.org/10.5281/zenodo.21889089)] [[数据](https://zenodo.org/records/21889089)]
- **TCM Ancient-to-Modern Open Metadata** — 古文今译受控语料的公开元数据伴随集：9,610条索引、固定切分、版本登记与哈希，以及10条独立编写的示例译文。实验古文、现代参考译文和教师推理轨迹不公开；不能将元数据当成9,610对可训练平行文本。 [[数据集](https://huggingface.co/datasets/xs12345/TCM-Ancient-Modern-Open)] [[代码](https://github.com/xiesi1234/R1-TCM-Translator)]
- **ShizhenGPT 中医预训练语料（论文报告共 15B+ tokens：Stage1 文本 11.92B 含 6.3B 中医语料，Stage2 多模态正文 3.8B、附录 3.84B）** — ShizhenGPT 中医预训练语料（论文报告共 15B+ tokens：Stage1 文本 11.92B 含 6.3B 中医语料，Stage2 多模态正文写 3.8B tokens，附录写 3.84B tokens） [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- **ChiMed 2.0 中文医疗预训练数据集（覆盖中医语料）** [[论文](https://arxiv.org/abs/2507.15275)]
- **国医典藏（中国中医古籍数字资源库）** — 中国中医科学院中医药信息研究所/图书馆的中医古籍图文库，现行入口为第4版站点。公开介绍收录先秦至清末民国医药典籍，可见口径为2500余种至3000余种，支持基本、高级和后控检索以及图文对照。校园网或注册查阅，不是公开批量下载。 [[网站](https://gydc-v4.cintcm.cn/)]
- **高质量中医预训练数据集（医案/典籍/百科等）** — 非网络来源高质量中医预训练数据集（约 1GB），含临床案例、名家典籍、医学百科等，99% 简体中文 [[数据集](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)]
- **国家中医药古籍数字图书馆** — 中国中医科学院中医药信息研究所自2022年起建设的古籍与传统知识发布门户，设古典医籍、民国文献、版本目录等分馆，并链出国医典藏等阅读系统。门户页可打开；读全文需进入分馆，不是公开批量下载。 [[网站](http://www.cintcm.com/)]
- **700 项中医药古籍文本** — 中医药古籍文本语料合集，收录近 700 项古籍文本 [[数据集](https://github.com/xiaopangxia/TCM-Ancient-Books)]
- **中医笈成** — 中医药古籍整理项目，按医经、诊法、本草、医方、医案等分类，提供全文检索、公开GitLab版本库与原始文件下载入口。公有领域文本的筛选、标点等编辑成果声明CC0，自创介绍页面CC BY 4.0；图片与个别页面另查。 [[网站](https://jicheng.tw/tcm/book/)] [[下载](https://jicheng.tw/tcm/download.html)] [[许可](https://jicheng.tw/tcm/copyright.html)]
- **中华医典（商业电子丛书，第6版为网页版）** — 商业电子丛书《中华医典》的现行销售站（飞熊科技）。站点写明收录古籍1156部、约4.5亿字，2000年获得国家电子出版物提名奖，裘沛然编审并题名。第6版是网页版，购买注册后使用，不是公开下载。 [[网站](https://www.zhyd1999.com/)]

</details>

<details>
<summary>评测基准（33）</summary>

- **TCM-RobustSDT** — 中医临床推理LLM鲁棒性基准数据集（Figshare） [[数据集](https://doi.org/10.6084/m9.figshare.33054974)]
- **大模型辨证论治评测基准** — Scientific Data发布的辨证论治基准，用来评估大模型的中医临床应用能力 [[论文](https://doi.org/10.1038/s41597-026-07587-4)]
- **病理标注舌象数据集** — 带病理标注的中医舌象图像集，用于降低人工舌诊的主观性。 [[论文](https://doi.org/10.62762/bish.2026.303296)]
- **病机思维链证候识别数据** — 在病机推理思维链监督下构建的证候表现识别数据，含结构化病案、金标准证候标签和模型预测。 [[数据集](https://doi.org/10.57760/sciencedb.35044)]
- **WHO TCM Terminology LLM Evaluation Set** — 用于评估大模型充当中医术语评价者的数据，DataCite 说明含 376 条来自 2022 年 WHO 中医国际标准术语的术语对照。 [[数据集](https://zenodo.org/records/21852353)]
- **TongueBench** — 2,694 张舌象、22 个标签；比较 9 个多模态模型、3 种提示策略及重复输出稳定性，配有图像数据和推理/评分示例。 [[DOI](https://doi.org/10.3389/frai.2026.1943004)] [[代码](https://github.com/mengyiha/TongueBench-Open)] [[数据集](https://zenodo.org/records/20701288)]
- **从病机到处方的真实病历推理基准** — 2000份多中心电子病历，检验模型能否按病例证据完成从病因病机到处方的推理 [[论文](https://arxiv.org/abs/2610.04215)]
- **TCM-DiagCommit** — 基于 TCM-SD 的 1,834 个源病例、148 个证候标签，构造 23,842 条任务记录；以固定三阶段信息披露评测证候辨别、证据利用及作出/延缓诊断的决策，提供数据和评分代码。 [[论文](https://arxiv.org/abs/2610.37243)] [[代码](https://github.com/Ethan-ai637/TCM-DiagCommit)] [[数据集](https://github.com/Ethan-ai637/TCM-DiagCommit/tree/main/data)]
- **TCM-BEST4SDT 辨证论治及知识、伦理与安全评测** — 600 条评测样本：300 条辨证论治病例，以及中医基础知识、医学伦理和内容安全各 100 题；涵盖 27 个评价维度。 [[数据集](https://github.com/DYJG-research/TCM-BEST4SDT)] [[论文](https://arxiv.org/abs/2512.02816)] [[正式发表](https://doi.org/10.1038/s41597-026-07587-4)]
- **TCM-AQA61 / CME-AQA 针灸推拿动作质量评估** — 针灸和推拿各 61 名受试者的第一人称、第三人称同步视频。两位有经验的中医物理治疗师各自评估全部受试者，再讨论达成一致。配套跨视角评估框架 CME-AQA。 [[论文](https://arxiv.org/abs/2606.28104)] [[DOI](https://doi.org/10.1109/TNSRE.2026.3705649)] [[代码](https://github.com/FrancisXZhang/cme-aqa)] [[数据](https://researchdata.durham.ac.uk/collections/r1jm214p229)]
- **TCM Term Prompt-Language Responses** — 18 个中医术语在 6 个通用模型、中英马来三种提示语言、各 3 次运行下生成的 972 条模型回答，并附 WHO 2007 与 2022 术语参照。 [[数据集](https://zenodo.org/records/22208549)]
- **MTCMB 中医多任务评测基准（知识/推理/安全）** — 中医多任务评测基准，12 个数据集、7,100 个样本，覆盖知识、推理、方剂与安全任务（Scientific Data 2026）。 [[数据集](https://github.com/Wayyuanyuan/MTCMB)] [[论文](https://arxiv.org/abs/2506.01252)] [[正式发表](https://doi.org/10.1038/s41597-026-07967-w)]
- **LingLanMedBench 多任务中医评测基准** — LingLanMedBench（原 LingLanMiDian）：5 大域、13 个子任务，共 25,620 条专家核验样本；每个子任务从完整集内选取 400 条构成 Hard 子集。 [[数据集](https://github.com/TCMAI-BJTU/LingLan)] [[论文](https://arxiv.org/abs/2602.01779v2)]
- **TongueProjectTCM Color Classification** — TongueProjectTCM 舌图像颜色分类数据，数据卡列出图像和整数标签，训练集 807 条、验证集 121 条。 [[数据集](https://huggingface.co/datasets/TongueProjectTCM/color-classification-opensource)]
- **TongueDx 远程舌诊多标签数据集** — 面向远程舌诊的公开图像集：5109 张、4650 名受试者，8 个二分类舌象属性（淡、边尖红、红点、瘀斑、裂纹、齿痕、厚苔、黄苔），并带年龄和性别。仓库可下。与后续消融论文 TongueDx2 不是同一篇。 [[数据集](https://github.com/tonguedx/tonguedx)] [[论文](https://arxiv.org/abs/2501.03053)]
- **TongueAtlas-4K** — 4000张临床舌象、由中医专家标注22类舌象表现的诊断基准，配套MIRNet（AAAI 2026待发表）。Zenodo记录为受限访问。 [[数据集](https://zenodo.org/records/17557646)]
- **TCMEval-SDT 辨证思维评测（专家标注病案）** — 中医辨证思维评测基准，含 300 例证候诊断案例（来源网络、古籍与医院病案），元数据遵循 FAIR 原则（Scientific Data 2025） [[DOI](https://doi.org/10.1038/s41597-025-04772-9)] [[论文](https://www.nature.com/articles/s41597-025-04772-9)] [[代码](https://github.com/zhuyan166/TCMEval)]
- **中药处方审核评测基准** — 328道处方规范性与合理性选择题，面向中药处方安全审核评测 [[论文](https://doi.org/10.1038/s41597-025-06387-6)] [[数据](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[代码](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)]
- **TCM-Vision-Benchmark 中医视觉评测（药材识别/望诊等，约 7k 题）** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Vision-Benchmark)]
- **标准化舌象病理标注数据集** — 6719张标准化舌象、20类病理多标签公开数据集，含检测基线 [[论文](https://arxiv.org/abs/2507.18288)] [[数据](https://doi.org/10.5061/dryad.1c59zw48r)] [[代码](https://github.com/btbuIntelliSense/Intelligent-tongue-diagnosis-detection-dataset)]
- **TCM-Ladder 中医多模态问答评测基准 (NeurIPS 2025)** — 中医多模态问答基准，含 52,169 个问答对，并包含图像、音频和视频数据（NeurIPS 2025）。 [[数据集](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[榜单](https://tcmladder.com)] [[论文](https://arxiv.org/abs/2505.24063)] [[正式发表](https://proceedings.neurips.cc/paper_files/paper/2025/file/cbdd26a4490f5a8dad0d732508714029-Paper-Datasets_and_Benchmarks_Track.pdf)]
- **TCM-Eval 动态可扩展中医评测基准** [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- **TCM-5CEval 五维中医深度评测** — 五维中医评测，含来自 30 门课程的 2,260 道题；对选择题进行选项循环置换，以检验回答对选项位置的敏感性。 [[论文](https://arxiv.org/abs/2511.13169)]
- **TCM-3CEval 核心知识·经典理解·临床决策三轴评测** [[论文](https://arxiv.org/abs/2503.07041)]
- **SYD_NK 内科证候测试集** — 366 条中医内科证候测试样本，每条是证候名加一段第一人称症状叙述。作者说明材料来自《中医内科学》，由中医学生校对，用于证候辨证。Apache-2.0。 [[数据集](https://huggingface.co/datasets/XiaoEnn/Syndrome_Differentiation_NK_test)]
- **MetaAcuPoint** — 用 Unreal Engine 的 MetaHuman 生成 900 张手部图像，按骨骼插槽标注 5 个手部穴位，供韩医穴位定位使用。 [[论文](https://doi.org/10.3390/healthcare13233093)]
- **Chinese Drug Name Overreliance Set** — 论文 Do "New Snow Tablets" Contain Snow? 的实验数据，用于检验大模型是否凭名称判断中药成分，卡内链接 arXiv:2504.03786。 [[数据集](https://huggingface.co/datasets/med-llm/tcm-llm-overrely-on-names)]
- **AcuSim** — 颈颅部穴位定位合成数据集。穴位标注依赖专家且成本高，该数据集用于扩大可检测的穴位定位数据。 [[论文](https://doi.org/10.1038/s41597-025-04934-9)]
- **ZhongJing-OMNI 中医多模态评测（含舌诊）** [[数据集](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]
- **TCMBench 中医药大模型全面评测基准** — 面向中医领域的综合性大模型评测基准 TCMBench（arXiv 2024） [[数据集](https://github.com/ywjawmw/TCMBench)] [[论文](https://arxiv.org/abs/2406.01126)]
- **HWTCMBench 中医能力评测集** [[数据集](https://huggingface.co/datasets/Monor/hwtcm)]
- **CMMLU Traditional Chinese Medicine** — CMMLU 中医测试集，数据卡写明可用 load_dataset 加载 185 条样本，文件为 traditional_chinese_medicine.json。 [[数据集](https://huggingface.co/datasets/shuyuej/CMMLU-Traditional-Chinese-Medicine-Benchmark)]
- **TCM-SD 中医辨证评测基准** — 首个大规模公开中医辨证文本基准（54152 条真实病历、148 证，CC BY-NC-SA 4.0）；仓库写明完整数据在 TCM_SD_with_knowledge，天池 dataId=139034 [[论文](https://arxiv.org/abs/2203.10839)] [[正式发表](https://aclanthology.org/2022.ccl-1.80/)] [[代码](https://github.com/Borororo/ZY-BERT)] [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=139034)]

</details>

<details>
<summary>考试数据集（8）</summary>

- **带执业医师参照的中医考试基准（公开版与论文口径不同）** — 论文报告38,279题和101名执业医师；当前HF数据卡为qa 33,872题、医师标注5,250题（102名医师、15,151次作答）。两个配置不可直接相加为独立题数，使用时需固定公开版本。CC BY-NC-SA 4.0。 [[论文](https://arxiv.org/abs/2609.33014)] [[数据集](https://huggingface.co/datasets/TechTCM/TCMQA)]
- **TCMLE** — 中医执业医师与执业助理医师资格考试题库共 7956 题，其中助理医师 2700 题、执业医师 5256 题，含真题和模拟题。 [[数据集](https://huggingface.co/datasets/Bolin97/TCMLE)]
- **TCM-Text-Exams 近年中医执业/考研真题文本基准** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams)]
- **Taiwan TCM Examination MCQ** — 来自台湾考选部网站的国家中医考试历届试题，README 写明年份为民国 96 至 111 年且不含 110 年，仓库文件为 basic theory of traditional Chinese medicine.csv。 [[数据集](https://huggingface.co/datasets/Liavan/Traditional-Chinese-Medicine-Multiple_choice_question)]
- **TCM Humanities MCQ** — 中医药语言模型团队整理的选择题，数据卡写明内容为医学人文、医学伦理和医师法规，来自中国医师资格考试相关题目，规模标注为不到 1000 条。 [[数据集](https://huggingface.co/datasets/TCMLM/TCM_Humanities)]
- **医疗大模型中文考试评估** [[数据集](https://github.com/jingnant/Medical-LLMs-Chinese-Exam)]
- **JTB Taiwan TCM Exam Questions** — JTB Tech 整理的台湾考选部中医相关试题，README 写明覆盖民国 90 年至 113 年，科目包括中医内科学、中医基础医学和中医临床医学。 [[数据集](https://huggingface.co/datasets/JTBTechnology/tcm_exam_questions)]
- **2023 Pharmacist Licensure Examination TCM Track** — 2023 年中国执业药师资格考试中药学轨道试题，数据卡写明来自网络收集，并指向 FreedomIntelligence/HuatuoGPT-II 仓库。 [[数据集](https://huggingface.co/datasets/FreedomIntelligence/2023_Pharmacist_Licensure_Examination-TCM_track)]

</details>

<details>
<summary>指令/对话数据集（22）</summary>

- **HSQ-TD（健身气功指令微调数据集）** — 健身气功养生领域首个指令微调数据集，57,843条指令基于官方教材与专业文献蒸馏（ScienceDB） [[数据集](https://doi.org/10.57760/sciencedb.35843)]
- **黄帝内经SFT指令集** — 杏核配套约2009条内经相关指令数据，含thinking/output字段 [[数据集](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2)]
- **TriCM-DF Acupuncture Corpus** — 面向中医大模型的专家审核指令语料，在针灸子领域按共识、专家经验和感知三个维度发布；仓库公开文本表，图像和视频文件不随包提供。 [[数据集](https://huggingface.co/datasets/Shutcm-TCME/TriCMDF)]
- **TCMNSCLC 非小细胞肺癌中医推理真实世界数据集** — 真实世界医案全标注（辨证/治法/汤药/中成药）的中医推理数据集 [[数据集](https://huggingface.co/datasets/zhangxinxin0428/TCMNSCLC)] [[DOI](https://doi.org/10.5281/zenodo.21027568)]
- **TCM Medical Case Commentary Generation** — 面向中医医案评注生成的数据，DataCite 说明含 510 条标准化原始医案，以及合计 2550 条的训练和测试实例，材料来自妇科经典。 [[数据集](https://doi.org/10.57760/sciencedb.j00133.00679)]
- **Gancao-TCM-Instruct** — 甘草中医诊疗指令数据集公开版含 25000 例、125000 条样本，覆盖疾病诊断、证候诊断、治法选择、基础方剂选择和具体中药选择。 [[数据集](https://huggingface.co/datasets/GancaoDoctorAI/gancao-tcm-instruct)]
- **Fu_TCM** — 已核验Fu_bianzheng.json、Fu_text.json、Fu_vision.json和图像文件；仓库共505个文件，标注Apache-2.0，但数据卡没有来源、样本统计或标注说明。图像文件名包含现代诊断图谱书名，底层素材授权尚待核对。 [[数据集](https://huggingface.co/datasets/fudanxai/Fu_TCM)]
- **tw-tcm** — minyichen/tw-tcm 的数据卡给出 8145 条训练样本，字段包括 question、answer、source 和 think。 [[数据集](https://huggingface.co/datasets/minyichen/tw-tcm)]
- **hwtcm-deepseek-r1-distill-data** — 海维团队用 DeepSeek 从网络原文蒸馏的中医推理问答指令数据。作者说明未经人工审查。 [[数据集](https://huggingface.co/datasets/Monor/hwtcm-deepseek-r1-distill-data)]
- **ShizhenGPT 多模态指令微调数据（文本/视觉/语音/ECG 等，论文 Table 3 合计约 31.1 万条）** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- **TCM Knowledge Q&A** — Science Data Bank 数据集，DataCite 说明以中医经典文献构建，含 6157 条问答知识对。 [[数据集](https://doi.org/10.57760/sciencedb.j00133.00565)]
- **白泽中医药语料库V3** — 约15.7万条中医QA，覆盖理论、中药、方剂、诊断、针灸与临床 [[数据集](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3)]
- **中医药知识问答实验数据** — 中医药问答数据集，并带提示工程用的知识图谱、知识库和实验结果。 [[数据集](https://doi.org/10.57760/sciencedb.j00133.00319)]
- **hwtcm-sft-v1** — 海维团队的中医单轮问答指令集，7096条。语料来自网站、论坛和书籍，由多个模型转成问答，并按专业性、安全性和流畅性评分。 [[数据集](https://huggingface.co/datasets/Monor/hwtcm-sft-v1)]
- **高质量中医 SFT 数据集** [[数据集](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]
- **TCM_19W_DataSet-SFT (part)** — 数据卡写明这是非网络来源的高质量中医指令微调数据的一部分，仓库文件为 TCM19W_Part1.json。 [[数据集](https://huggingface.co/datasets/cduoduo/TCM_19W_DataSet-SFT)]
- **TCMChat-dataset-600k 中药知识问答与推荐指令数据** [[数据集](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- **中国药典指令数据集** — 基于《中国药典》一部构建的KnowledgeQA与PrescriptionWriting指令数据 [[数据](https://github.com/QLU-NLP/BianCang/tree/main/ChP-TCM)] [[论文](https://arxiv.org/abs/2411.11027)]
- **中医药指令数据集 ShenNong_TCM_Dataset** [[数据集](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)]
- **MedChatZH 中医问诊数据集** [[代码](https://github.com/tyang816/MedChatZH)] [[数据集](https://huggingface.co/datasets/tyang816/MedChatZH)]
- **中文医疗在线问诊数据集 ChatMed_Consult_Dataset（110,113 条）** — 中文在线问诊数据，110,113 条。问题来自问诊网站，回答是 GPT-3.5 写的。 [[数据集](https://huggingface.co/datasets/michaelwzhu/ChatMed_Consult_Dataset)]
- **CMtMedQA 仲景真实多轮医患对话（约 7 万条）** [[数据集](https://huggingface.co/datasets/Suprit/CMtMedQA)]

</details>

<details>
<summary>知识图谱（24）</summary>

- **本草典开放数据（本草、方剂、证型、腧穴）** — 本草典编辑部发布的双语中医药种子数据，CC BY-SA 4.0，可直接下载 JSON。2026年4月17日生成的 v1 写明本草365条、方剂112条、证型84条、腧穴208条，另有经络、舌脉和关系图谱。同一页的覆盖说明写标准本草约530味中已收335味。这是编辑项目词表，不是国家标准。 [[网站](https://bencaodian.org/zh/about/data/)] [[数据](https://bencaodian.org/data/v1/herbs.json)]
- **医宗金鉴知识三元组** — 从《医宗金鉴》抽取的25571条知识三元组，覆盖中药、方剂、疾病、穴位和医理，关系类型1105种。 [[数据集](https://doi.org/10.57760/sciencedb.013fv)]
- **TCMEFO** — 中医功效形式化本体，DataCite 说明用于功效概念、关系和中药实例的分层可计算表示。 [[数据集](https://doi.org/10.6084/m9.figshare.32677743)]
- **TCM Disease-Pattern-Symptom-Herb KG v2** — 连接疾病、证候、症状和中药的语义知识图谱 2.0，Zenodo 文件为 node-v2-eng260502.csv 与 edge-v2-eng260502.csv。 [[数据集](https://zenodo.org/records/18173423)]
- **灵枢症状中心上下文知识图谱** — 北交大等症状中心中西医桥接图谱（导出约1733万实体、3947万关系，含三元组+上下文四元组），门户提供可视化、推理与有据问答 [[论文](https://arxiv.org/abs/2608.20402)] [[网站](http://www.tcmkg.com/)]
- **Chinese Herbal Efficacy Relations** — 把中药传统功效从自然语言整理成可计算的药–功效关系，DataCite 说明用途包括知识图谱构建、方剂功效预测和药–症关联。 [[数据集](https://zenodo.org/records/18207409)]
- **TCM-MKG 中医药多维知识图谱** — 曾敬淇、贾晓斌公开的中医药多维知识图谱，连接术语、饮片和药性。配套论文用可解释图神经网络在 6080 首方上量化配伍，并用 215 首新冠相关方做了验证。 [[数据](https://zenodo.org/records/15395588)] [[论文](https://doi.org/10.1016/j.jpha.2025.101342)]
- **OpenTCM 妇科古籍知识图谱（约 4.8 万实体 / 15.2 万关系）** [[代码](https://github.com/OpenTCM01/OpenTCM)] [[论文](https://arxiv.org/abs/2504.20118)]
- **针灸知识图谱** — 综合针灸知识图谱，来源包括指南、PubMed、临床试验和本体映射 [[论文](https://doi.org/10.1093/jamia/ocaf179)]
- **五部伤寒书知识图谱** — 从《伤寒论》《伤寒类方》《伤寒悬解》《伤寒论浅注》《伤寒九十论》抽出的知识图谱。节点 26771 个，关系 8272 条，CSV 可以导入 Neo4j。2024 年发布在 ScienceDB。 [[DOI](https://doi.org/10.57760/sciencedb.j00133.00432)]
- **中药异构网络结构集** — 汇总生物医学里常见的异构网络，其中包括药–靶、药–症状、药–药和症状–症状网络，也含蛋白质相互作用网络。 [[论文](https://doi.org/10.1016/j.dib.2024.110962)]
- **DragonTCM** — 由 American Dragon 及 Penner 著作整理的中医知识库，数据卡报告1,119条病证、2,580首方剂、1,044味中药与28,735条关系；作者说明由AI自动解析，可能含不准确处，许可为CC-BY-NC-4.0。 [[数据](https://huggingface.co/datasets/f-galkin/DragonTCM)]
- **中医 Neo4j 知识图谱** — 用 Neo4j 社区版搭建的中医知识图谱。示例从症状节点「便秘」出发，查与它相连的节点。 [[数据集](https://github.com/ywjawmw/TCM_KG)]
- **中医证候本体与疾病–证候–方剂关联平台**（服务异常） — 中国中医科学院中药研究所等建设的证候本体平台。iMeta 2023论文写明整理319个证候、8045种疾病和1359首方剂，并关联基因、疾病与方剂。论文页可核；前台页面当前没有可读的证候内容。与 ETCM 同在 tcmip.cn，但是独立证候系统。未见免登录的整库镜像。 [[网站](http://www.tcmip.cn/Syndrome/front/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10989962/)]
- **中医临床诊疗术语 第3部分：治法** — 现行国家标准《中医临床诊疗术语 第3部分：治法》，2023年3月17日发布并实施。国家标准全文公开系统提供在线预览和下载。这是治法术语标准页，不是独立词表数据包。 [[网站](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E8BBBAB76E1AF1498C5DA5DFBB2194EC)]
- **中医临床诊疗术语 第1部分：疾病** — 现行国家标准《中医临床诊疗术语 第1部分：疾病》，2023年3月17日发布并实施，主管部门为国家中医药局。国家标准全文公开系统提供在线预览和下载。证候部分和治法部分另有独立全文页。 [[网站](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=7377FB06FF43DC321BB6A4BF7DAA7F39)]
- **TCM-QG 中医文献问题生成（CHIP2020）** — 中医文献问题生成数据，3500 篇，每篇由人标了 1 到 4 对问答。许可是 CC BY-NC 2.0。 [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86895)] [[资料](http://openkg.cn/dataset/tcm-qg)]
- **TCM-NER 中药说明书实体识别（OpenKG / CHIP）** — 中药说明书的实体识别数据，用来做用药知识图谱。许可是 CC BY-NC 2.0。 [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86819)] [[资料](http://openkg.cn/dataset/tcm-ner)]
- **中医临床诊疗术语 第2部分：证候** — 现行国家标准《中医临床诊疗术语 第2部分：证候》，2021年11月26日发布并实施。国家标准全文公开系统提供在线预览和下载。这是证候术语标准页，不是独立词表数据包。 [[网站](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C71A9DAD24CB1252F12439D1F045DA6A)]
- **中医病证分类与代码** — 现行国家标准《中医病证分类与代码》，2021年10月11日发布并实施，替代 GB/T 15657-1995，主管部门为国家中医药局。国家标准全文公开系统提供在线预览和下载。这是标准全文页，不是独立的机器可读代码包。 [[网站](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=41FD9D06E5BE4F84EA1D8D07101BED2C)]
- **经穴名称与定位** — 现行国家标准《经穴名称与定位》，2021年11月26日发布并实施，主管部门为国家中医药局。国家标准全文公开系统提供在线预览和下载。这是标准全文页，不是单独打包的穴位词表。 [[网站](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=397548AE7248D3D87DD15E0AB8107185)]
- **中医药知识服务平台** — 中国中医科学院中医药信息研究所维护的知识服务首页，面向知识检索、知识图谱和疾病画像。同一信息所的中医学专业知识服务系统关于页写明，2019年起受中国工程科技知识中心委托建设专业知识服务，汇聚病证、方剂、中药与文献资源。首页可打开；高校试用说明要求校园网注册登录，未见公开批量下载。 [[网站](https://www.tcmkb.cn/)]
- **ICD-11 传统医学病情补充章** — WHO 对 ICD-11 补充章 Traditional Medicine Conditions 的官方说明。该章用于发病数据的可选双编码，不用于死亡报告。当前模块 I 覆盖源于古代中国、现用于中国、日本、韩国及其他地区的传统医学病情。本页是章节说明，具体编码在 ICD-11 浏览器中查阅，页面公开。 [[网站](https://www.who.int/standards/classifications/frequently-asked-questions/traditional-medicine)]
- **WHO 西太平洋区标准针灸穴位定位** — WHO 西太平洋区办事处2008年出版、2009年重印的穴位定位标准。IRIS 记录写明包含体表定位方法和361个穴位，用于教学、科研、临床、出版和学术交流，并提供英文 PDF。中国、日本、韩国专家参与定位协调。记录页公开。 [[网站](https://iris.who.int/handle/10665/353407)]

</details>

<details>
<summary>其他（2）</summary>

- **TCM-Flow** — Ma Shaochen 与 li xiong 在 Zenodo 发布的 TCM-Flow: A Traditional Chinese Medicine Virtual Screening Dataset。记录页标明 2026年10月23日以 v1 公开发布，资源类型为 Dataset，提供 15.4 MB 的 TCM-Flow_Dataset.zip 下载，许可为 Creative Commons Attribution 4.0 International。版本 DOI 为 10.5281/zenodo.23600814。本次通过 DOI 解析打开了 Zenodo 一手记录页。页面未给出更细的化合物或筛选规模数字，故不另行补写。这是可公开下载的数据集落地页，不是内部评测集。 [[Zenodo](https://zenodo.org/records/23600813)] [[DOI](https://doi.org/10.5281/zenodo.23600814)]
- **EthnoMedOne** — 贵州大学 Shuai Xiaomin 在 Zenodo 发布的 EthnoMedOne v1.0.0。记录页说明该数据集整合中国多种民族医药记载，并与标准化化合物、蛋白靶点、疾病、证候、症状及化合物属性等关联；提供 SQLite 库、对应 CSV、文档、来源与映射核查及示例查询。页面明确写明：所报告关联是标准化数据链接，不应理解为实验验证的机制或临床疗效。2026年10月22日以 v1 公开发布，许可为 CC BY 4.0，版本 DOI 为 10.5281/zenodo.23553718。本次通过 DOI 解析打开了 Zenodo 一手记录页。这是可公开下载的数据集落地页，不是内部评测集。 [[Zenodo](https://zenodo.org/records/23553717)] [[DOI](https://doi.org/10.5281/zenodo.23553718)]

</details>

## 学习资料

本栏收公开课、系列讲座等可核验的一手链接，不下载视频。优先高校、医院、学会或体系完整的课程。

<details>
<summary>中国大学 MOOC（32）</summary>

**北京中医药大学（11）**
- **北京中医药大学《中医入门》中国大学MOOC课程（王彤）** 北京中医药大学王彤主讲的《中医入门》公开课，在中国大学MOOC开出，从医话、医道、医理、医术四部分引导学习者认识中医理论与应用。本次打开了课程一手页面。当前学期于2026年9月28日开课，至2027年1月20日结束；平台记录的较早开课可追溯至2019年10月。这是高校正规公开课，不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/BUCM-1206405809)]
- **北京中医药大学《中医内科学选讲》中国大学MOOC课程（赵进喜）** 北京中医药大学赵进喜主讲的《中医内科学选讲》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期自2026年10月22日起开放，平台将结束时间记为远期长期开放；较早开课可追溯至2019年12月31日。这是高校正规公开课，不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/bucm-1206414807)]
- **北京中医药大学《中医基础理论》中国大学MOOC课程（马淑然）** 北京中医药大学马淑然主讲的《中医基础理论》公开课，在中国大学MOOC（爱课程/网易）开出，面向中医药专业学生和中医爱好者，系统讲授阴阳五行、藏象经络、气血津液、病因病机和治则治法。本次打开了课程一手页面。当前学期于2026年9月14日开课，至2027年1月20日结束；平台记录的较早开课可追溯至2019年10月。这是高校正规公开课，不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/BUCM-1206410812)]
- **北京中医药大学《中医妇科学》中国大学MOOC课程（史云）** 北京中医药大学史云主讲的《中医妇科学》公开课，在中国大学MOOC开出。课程页面介绍其为中医临床医学的重要组成部分和中医学专业临床主干课，适用于中医学、针灸推拿学、中西医结合等专业本科生及中医妇科、中西医结合妇科学研究生，帮助学生巩固经带胎产常见病的基础理论、妇科四诊及外治法等知识。本次打开了课程一手页面。当前学期于2026年9月7日开课，至2027年1月10日结束；平台记录的较早开课可追溯至2025年3月15日。这是高校正规公开课，不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/BUCM-1472333163)]
- **北京中医药大学《中医诊断学（上）》中国大学MOOC课程（王天芳等）** 北京中医药大学王天芳（教授）主讲的《中医诊断学（上）》公开课，在中国大学MOOC（爱课程/网易）开出，课程团队还有吴秀艳、薛晓琳、赵燕（教授）以及关静、宋月晗、马捷（副教授）。课程页面显示当前学期为2026年8月31日至2026年12月31日（Asia/Shanghai），选课人数5735；页面可核验的最早学期始于2015年10月29日。课程为该校中医诊断学在线开放课的上册，当前学期大纲从绪论进入望诊等内容，对应诊法部分的教学安排。本次打开了中国大学MOOC一手课程页。未下载视频。这是高校正规公开课，不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/BUCM-388001)]
- **北京中医药大学《中医诊断学（下）》中国大学MOOC课程（王天芳等）** 北京中医药大学王天芳（教授）主讲的《中医诊断学（下）》公开课，在中国大学MOOC（爱课程/网易）开出，课程团队还有吴秀艳、薛晓琳、赵燕（教授）以及关静、宋月晗、马捷（副教授）。课程页面显示当前学期为2026年8月31日至2026年12月31日（Asia/Shanghai），选课人数1654；页面可核验的最早学期始于2019年9月16日。下册侧重辨证，覆盖辨证总论、八纲辨证、阴阳虚损辨证、病因辨证、气血津液辨证、脏腑辨证，以及六经、卫气营血、三焦辨证，并含病案书写与诊法、辨证的综合运用。本次打开了中国大学MOOC一手课程页。未下载视频。这是高校正规公开课，不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/BUCM-1206420806)]
- **北京中医药大学《中医骨伤科学》中国大学MOOC课程（徐林）** 北京中医药大学徐林（二级教授）主讲的《中医骨伤科学》公开课，在中国大学MOOC（爱课程/网易）开出。课程页面写明北京中医药大学中医骨伤科学专业创建于2021年，课程概述强调中医骨伤学科相关学习与实践，培养中医骨伤临床实用复合型人才；大纲包括中医骨伤科发展简史、骨伤病的分类和病因病机、临床诊查、治疗方法、创伤急救、骨折、脱位、筋伤和骨病。本次打开了课程一手页面，页面学期数据为2026年1月27日至2026年12月31日（Asia/Shanghai）。未下载视频。这是高校正规公开课，不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/BUCM-1472329163)]
- **北京中医药大学《中药安全用药导论》中国大学MOOC课程（张冰等）** 北京中医药大学张冰、林志健、张晓朦等主讲的《中药安全用药导论》公开课，在中国大学MOOC开出，介绍中药药物警戒、不良反应识别与常见中成药安全问题，课程说明称2017年被评为教育部精品在线开放课程。本次打开了课程一手页面。当前学期于2026年9月7日开课，至2026年12月14日结束；平台记录的较早开课可追溯至2015年10月。这是高校正规公开课，不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/BUCM-387003)]
- **北京中医药大学《中药鉴定学》中国大学MOOC课程（杨瑶珺）** 北京中医药大学杨瑶珺主讲的《中药鉴定学》公开课，在中国大学MOOC开出。页面介绍课程从中药质量问题入手，以中药材及饮片性状鉴别为核心，依据辨状论质，结合显微和理化特征评价真伪优劣；并写明课程依托国家中医药管理局中药鉴定学重点学科，为国家首批一流本科课程，课程团队介绍闫永红教授为学术带头人。本次打开了课程一手页面，页面显示的主讲教师为杨瑶珺。当前学期于2026年8月31日开课，至2027年1月9日结束；平台记录的较早开课可追溯至2023年11月10日。这是高校正规公开课，不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/BUCM-1462115161)]
- **北京中医药大学《温病学》中国大学MOOC课程（谷晓红）** 北京中医药大学谷晓红主讲的《温病学》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年9月15日开课，至2026年12月31日结束；平台学期列表中目前仅见这一轮，故将首次开课记为2026年。这是高校正规公开课，不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/BUCM-1474575165)]
- **北京中医药大学《针灸学导论》中国大学MOOC课程（马文珠）** 北京中医药大学马文珠主讲的《针灸学导论》公开课，在中国大学MOOC开出。课程页面写明其为国家精品在线开放课程认定课程。本次打开了课程一手页面。当前学期于2026年9月29日开课，至2026年12月31日结束；平台记录的较早开课可追溯至2015年11月24日。这是高校正规公开课，不是已收录的该校《中医基础理论》《中医入门》《中药安全用药导论》三门课，也不是营销短视频。 [北京中医药大学] [[课程](https://www.icourse163.org/course/BUCM-387004)]

**河南中医药大学（6）**
- **河南中医药大学《中医各家学说》中国大学MOOC课程（李丽等）** 河南中医药大学李丽、刘文礼、李成文、郭凤鹏、蔡丽娜、赵迪克、孔沈燕主讲的《中医各家学说》公开课，在中国大学MOOC开出。页面介绍课程研究历代名医学术思想、临证经验与特色，兼及中医学术流派与学说，帮助学生了解名医治学门径并评估取舍其学术思想。本次打开了课程一手页面。当前学期于2026年8月28日开课，至2027年1月3日结束；平台记录的较早开课可追溯至2022年2月21日。这是高校正规公开课，不是营销短视频。 [河南中医药大学] [[课程](https://www.icourse163.org/course/HACTCM-1465577165)]
- **河南中医药大学《中医基础理论》中国大学MOOC课程（崔姗姗）** 河南中医药大学崔姗姗主讲的《中医基础理论》公开课，在中国大学MOOC开出。课程页面写明其为国家级精品在线开放课程，面向高等中医药院校专业基础课学习，系统讲授中医学形成发展、气一元论与阴阳五行、藏象、精气血津液、经络与体质、病因病机及养生防治原则。本次打开了课程一手页面。当前学期于2026年7月20日开课，至2026年12月25日结束；平台记录的较早开课可追溯至2017年10月9日。这是高校正规公开课，不是营销短视频。 [河南中医药大学] [[课程](https://www.icourse163.org/course/HACTCM-1002126013)]
- **河南中医药大学《中医诊断学》中国大学MOOC课程（车志英）** 河南中医药大学车志英主讲的《中医诊断学》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年8月28日开课，至2026年12月31日结束；平台记录的较早开课可追溯至2019年2月28日。这是高校正规公开课，不是营销短视频。 [河南中医药大学] [[课程](https://www.icourse163.org/course/HACTCM-1205691801)]
- **河南中医药大学《内经选读》中国大学MOOC课程（霍磊）** 河南中医药大学霍磊主讲的《内经选读》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年8月24日开课，至2026年12月18日结束；平台记录的较早开课可追溯至2020年3月20日。这是高校正规公开课，不是营销短视频。 [河南中医药大学] [[课程](https://www.icourse163.org/course/HACTCM-1456170164)]
- **河南中医药大学《金匮要略》中国大学MOOC课程（王勇）** 河南中医药大学王勇主讲的《金匮要略》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年8月24日开课，至2026年12月27日结束；平台记录的较早开课可追溯至2020年3月21日。这是高校正规公开课，不是营销短视频。 [河南中医药大学] [[课程](https://www.icourse163.org/course/HACTCM-1456121167)]
- **河南中医药大学《针灸学》中国大学MOOC课程（高希言）** 河南中医药大学高希言主讲的《针灸学》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年8月31日开课，至2027年1月10日结束；平台记录的较早开课可追溯至2020年3月21日。这是高校正规公开课，不是营销短视频。 [河南中医药大学] [[课程](https://www.icourse163.org/course/HACTCM-1456089164)]

**南京中医药大学（4）**
- **南京中医药大学《中医诊断学》中国大学MOOC课程（徐征）** 南京中医药大学徐征主讲的《中医诊断学》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年7月22日开课，至2027年1月8日结束；平台记录的较早开课可追溯至2021年6月28日。这是高校正规公开课，不是营销短视频。 [南京中医药大学] [[课程](https://www.icourse163.org/course/NJUTCM-1463994165)]
- **南京中医药大学《中药学》中国大学MOOC课程（唐德才）** 南京中医药大学唐德才主讲的《中药学》公开课，在中国大学MOOC开出。课程页面可见“国家精品在线开放课程认定”相关表述，并提到国家级一流课程。本次打开了课程一手页面。当前学期于2026年8月31日开课，至2027年1月10日结束；平台记录的较早开课可追溯至2017年11月14日。这是高校正规公开课，不是营销短视频。 [南京中医药大学] [[课程](https://www.icourse163.org/course/NJUTCM-1001752319)]
- **南京中医药大学《伤寒论》中国大学MOOC课程（凌云）** 南京中医药大学凌云主讲的《伤寒论》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年8月28日开课，至2027年1月10日结束；平台记录的较早开课可追溯至2019年10月22日。这是高校正规公开课，不是营销短视频。 [南京中医药大学] [[课程](https://www.icourse163.org/course/NJUTCM-1207040811)]
- **南京中医药大学《小儿推拿学》中国大学MOOC课程（吴云川等）** 南京中医药大学吴云川（教授）主讲的《小儿推拿学》公开课，在中国大学MOOC开出，课程团队还包括王建珠（副教授/主治中医师）、杨小存、王宇航、徐勰（讲师）。课程概述写明以中医学理论和临床知识为基础，讲解小儿推拿常用穴位、常用手法及常见疾病的保健推拿方法；大纲覆盖概述、上肢及头面颈项胸腹腰背下肢穴位、常用手法，以及肺系、脾系、肾系和其他疾病。本次打开了课程一手页面。当前学期于2026年9月9日开课，至2026年12月20日结束；平台记录的较早开课可追溯至2019年12月2日。页面显示选课人数 450。这是高校正规公开课，不是营销短视频。 [南京中医药大学] [[课程](https://www.icourse163.org/course/NJUTCM-1207426810)]

**广州中医药大学（3）**
- **广州中医药大学《中医儿科学》中国大学MOOC课程（许尤佳等）** 广州中医药大学许尤佳（教授/主任医师）主讲的《中医儿科学》公开课，在中国大学MOOC开出，课程团队还包括杨京华（主任中医师）和刘卓勋（副主任医师）。课程概述写明以中医学理论体系为指导，研究从胎儿至青少年的生长发育、生理病理及疾病防治，内容分总论（中医儿科学基础与各年龄期儿童保健）和各论（各系统常见病），面向医学类本科学生并兼顾社会学习者。本次打开了课程一手页面。当前学期于2026年8月24日开课，至2026年12月31日结束；平台记录的较早开课可追溯至2019年9月23日。页面显示选课人数 1374。这是高校正规公开课，不是营销短视频。 [广州中医药大学] [[课程](https://www.icourse163.org/course/GZZYY-1206620837)]
- **广州中医药大学《方剂学》中国大学MOOC课程（全世建）** 广州中医药大学全世建主讲的《方剂学》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年8月31日开课，至2027年1月9日结束；平台记录的较早开课可追溯至2021年9月6日。这是高校正规公开课，不是营销短视频。 [广州中医药大学] [[课程](https://www.icourse163.org/course/GZZYY-1463109166)]
- **广州中医药大学《精讲精学中医基础理论》中国大学MOOC课程（严灿）** 广州中医药大学严灿主讲的《精讲精学中医基础理论》公开课，在中国大学MOOC开出。课程对中医基础理论重点内容作深入讲解，覆盖哲学基础、藏象、气血津液、病因与发病、病机和防治原则；页面说明经络和体质等部分以自学资料为主。本次打开了课程一手页面。当前学期于2026年9月14日开课，至2027年1月30日结束；平台记录的较早开课可追溯至2020年10月2日。这是高校正规公开课，不是营销短视频。 [广州中医药大学] [[课程](https://www.icourse163.org/course/GZZYY-1461246162)]

**福建中医药大学（3）**
- **福建中医药大学《中医健康理念》中国大学MOOC课程（李灿东）** 福建中医药大学李灿东主讲的《中医健康理念》公开课，在中国大学MOOC开出。课程页面写明其为国家精品在线开放课程认定课程，以《黄帝内经》健康养生理论为指导，讲解健康原则、自我评价、气血阴阳与脏腑状态辨别及虚证调补等，属中医类通识课。本次打开了课程一手页面。当前学期于2026年9月1日开课，至2026年12月31日结束；平台记录的较早开课可追溯至2019年4月29日。这是高校正规公开课，不是营销短视频。 [福建中医药大学] [[课程](https://www.icourse163.org/course/FJZYY-1205912818)]
- **福建中医药大学《中医运动疗法--易筋经》中国大学MOOC课程（鄢行辉）** 福建中医药大学鄢行辉主讲的《中医运动疗法--易筋经》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年9月15日开课，至2026年12月15日结束；平台记录的较早开课可追溯至2019年5月16日。这是高校正规公开课，不是营销短视频。 [福建中医药大学] [[课程](https://www.icourse163.org/course/FJZYY-1206075802)]
- **福建中医药大学《内经选读》中国大学MOOC课程（高嘉骏）** 福建中医药大学高嘉骏主讲的《内经选读》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年8月6日开课，至2026年12月31日结束；平台记录的较早开课可追溯至2019年9月9日。这是高校正规公开课，不是营销短视频。 [福建中医药大学] [[课程](https://www.icourse163.org/course/FJZYY-1206624802)]

**南方医科大学（1）**
- **南方医科大学《中医外科学》诠说中国大学MOOC课程（邓燕等）** 南方医科大学邓燕、杨柳、赖梅生、潘恩山、陈景良主讲的《中医外科学》诠说公开课，在中国大学MOOC开出。页面介绍课程覆盖皮肤与性传播疾病、乳房病、疮疡、肛门直肠病、男科病、周围血管病、甲状腺病、体表肿瘤及其他外科疾病等，以病例引入并提出问题，再在教学中解答。本次打开了课程一手页面。当前学期于2026年9月7日开课，至2027年1月10日结束；平台记录的较早开课可追溯至2020年12月1日。这是高校正规公开课，不是营销短视频。 [南方医科大学] [[课程](https://www.icourse163.org/course/SMU-1461533168)]

**山东中医药大学（1）**
- **山东中医药大学《中医基础理论》中国大学MOOC课程（郑红）** 山东中医药大学郑红主讲的《中医基础理论》公开课，在中国大学MOOC开出。页面介绍课程依托该校中医基础理论国家重点学科，系统讲授精气阴阳五行、藏象、精气血津液神、经络与体质，以及病因、发病、病机和防治原则。本次打开了课程一手页面。当前学期于2026年9月6日开课，至2027年1月10日结束；平台记录的较早开课可追溯至2020年3月16日。这是高校正规公开课，不是营销短视频。 [山东中医药大学] [[课程](https://www.icourse163.org/course/SDUTCM-1450194213)]

**成都中医药大学（1）**
- **成都中医药大学《中药学》中国大学MOOC课程（王建）** 成都中医药大学王建主讲的《中药学》公开课，在中国大学MOOC开出。课程页面写明其为国家精品在线开放课程认定课程，系统介绍中药学基本理论和常用中药的性能、功效及临床应用。本次打开了课程一手页面。当前学期于2026年9月16日开课，至2026年12月31日结束；平台记录的较早开课可追溯至2018年3月1日。这是高校正规公开课，不是营销短视频。 [成都中医药大学] [[课程](https://www.icourse163.org/course/CDUTCM-1002533010)]

**暨南大学（1）**
- **暨南大学《中医基础理论》中国大学MOOC课程（陈利国）** 暨南大学陈利国主讲的《中医基础理论》公开课，在中国大学MOOC开出。课程面向中医专业学生和中医爱好者，讲解中医理论体系的产生发展、整体观念与辨证论治、阴阳五行，以及对人体、疾病和养生防治的认识。本次打开了课程一手页面。当前学期于2026年8月3日开课，至2026年12月27日结束；平台记录的较早开课可追溯至2019年9月26日。这是高校正规公开课，不是营销短视频。 [暨南大学] [[课程](https://www.icourse163.org/course/JNU-1206450825)]

**长春中医药大学（1）**
- **长春中医药大学《内经选读》中国大学MOOC课程（苏颖）** 长春中医药大学苏颖主讲的《内经选读》公开课，在中国大学MOOC开出。本次打开了课程一手页面。当前学期于2026年8月31日开课，至2027年1月17日结束；平台记录的较早开课可追溯至2020年3月23日。这是高校正规公开课，不是营销短视频。 [长春中医药大学] [[课程](https://www.icourse163.org/course/CCUCM-1450258188)]

</details>

<details>
<summary>Coursera（3）</summary>

**香港中文大学（2）**
- **香港中文大学 Coursera 课程 Everyday Chinese Medicine 2（Yung Tat To）** 香港中文大学在 Coursera 开出的 Everyday Chinese Medicine 2 公开课。一手课程页写明由 The Chinese University of Hong Kong 提供，授课教师为香港中西医结合医学研究所的 Yung Tat To，向公众和医护人员介绍中医基本原理。页面记录的 launchedAt 为 2020-02-03。本次用 curl 打开了 Coursera 课程页（HTTP 200）。这是大学正规公开课，不是营销短视频。 [香港中文大学] [[课程](https://www.coursera.org/learn/everyday-chinese-medicine-2)]
- **香港中文大学 Coursera 课程 Everyday Chinese Medicine（Vincent CHUNG）** 香港中文大学在 Coursera 开出的 Everyday Chinese Medicine 公开课。一手课程页写明由 The Chinese University of Hong Kong 提供，授课教师为香港中西医结合医学研究所的 Prof. Vincent CHUNG，面向公众介绍中医诊治思路及中医服务与草药产品的规管。页面记录的 launchedAt 为 2017-09-25。本次用 curl 打开了 Coursera 课程页（HTTP 200）。这是大学正规公开课，不是营销短视频。 [香港中文大学] [[课程](https://www.coursera.org/learn/everyday-chinese-medicine)] [[学院](https://www.scm.cuhk.edu.hk/en-gb/elearning-platform/coursera/)]

**香港科技大学（1）**
- **香港科技大学 Coursera 课程 Health Concepts in Chinese Medicine（Robert Ko）** 香港科技大学在 Coursera 开出的 Health Concepts in Chinese Medicine 公开课。一手课程页写明由 The Hong Kong University of Science and Technology 提供，授课教师为生命科学部的 Robert Ko，在现代医学语境下讲解中医基本理论。页面记录的 launchedAt 为 2017-11-06。本次用 curl 打开了 Coursera 课程页（HTTP 200）。这是大学正规公开课，不是营销短视频。 [香港科技大学] [[课程](https://www.coursera.org/learn/health-concepts-chinese-medicine)]

</details>

<details>
<summary>智慧树（1）</summary>

**安徽中医药大学（1）**
- **安徽中医药大学《医古文》智慧树课程（卜菲菲、张雪梅、王硕建）** 安徽中医药大学卜菲菲、张雪梅、王硕建主讲的《医古文》公开课，在智慧树开出，并由国家高等教育智慧教育平台提供可核验的课程页。页面写明开课平台为智慧树，开课高校为安徽中医药大学，开课教师为上述三人，并显示1万+人选课。当前学期起止在平台数据中为 2026-07-20T16:00:00.000Z 至 2027-01-19T16:00:00.000Z，按东八区为 2026年7月21日至 2027年1月20日；页面还给出 2026/07/21 与 2027/01/20 的日期写法，更新日期为 2026/11/20。本次打开了智慧教育平台一手课程页（HTTPS 200）。智慧树课程首页会跳转到前端壳页，未再解析出可核验的学期或教师字段，故不以该壳页为唯一依据。平台页可见的学期仅此一轮，故将首次开课暂记为 2026年。这是高校正规公开课，不是营销短视频。 [安徽中医药大学] [[课程](https://www.chinaooc.com.cn/course/671ad41616d8a05eedca3bca)] [[智慧树](https://coursehome.zhihuishu.com/courseHome/1000050200/455682/26)]

</details>

---

要搜索或按标签筛，用[项目页](https://tyang816.github.io/zh/projects/tcm/)。说明写在 [Wiki](wiki/Home.md)。
改条目请编辑 `data/catalog.yml`，再运行 `python3 scripts/build_readme.py`，不要直接改这个 README。
