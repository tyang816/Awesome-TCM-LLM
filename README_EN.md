# 🔥 Open TCM Models, Data, Papers, and Patents

**Language / 语言:** [English](README_EN.md) | [中文](README.md)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  ![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork) [![中文门户](https://img.shields.io/badge/中医资源-门户-blue)](https://tyang816.github.io/zh/projects/tcm/) [![Project](https://img.shields.io/badge/Project-tyang816.github.io-informational)](https://tyang816.github.io/projects/tcm/)

Open TCM models, datasets, papers, and patents, plus a few related Chinese medical resources. Right now: 55 news items, 111 models, 62 surveys, 69 patents, 167 datasets, 249 method papers. [PRs welcome](CONTRIBUTING.md).

[Project page](https://tyang816.github.io/projects/tcm/) · [Chinese catalog](https://tyang816.github.io/zh/projects/tcm/) · [Wiki](wiki/Home.md) · [Homepage](https://tyang816.github.io/)

## Start here

Only about 12 TCM checkpoints are actually public; they are under [Open models](#open-models). Hospital and company releases in the news usually ship no weights, so they make poor experimental baselines.

Since 2025 the interesting work has been multimodal models, agents, and evaluation—not another 7B chatbot. Licensing-exam scores measure recall, not whether a model can do pattern differentiation. For comparisons, TCM-Ladder, LingLan, and MTCMB are a better place to start.

| If you want to… | Try | Note |
| --- | --- | --- |
| Get a model running | **[BianCang](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)**, **[仲景 (ZhongJing)](https://huggingface.co/CMLM/ZhongjingGPT1_13B)** | Paper, weights, and code |
| Build TCM inquiry | **[MedChatZH](https://github.com/tyang816/MedChatZH)** | Comes with consult dialogues |
| Tongue / four diagnoses | **[ShizhenGPT](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)** | Multimodal; weights and data are public |
| Train further | **[ChatTCM](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)**, **[神农大模型 (ShenNong-TCM-LLM)](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)** | Pretrain or instruction data is released |
| Stay small | **[Xinghe](https://huggingface.co/zsyjsld/Xinghe1.2-9B)** | 9B, GGUF available |
| Run a comparison | **[TCM-Ladder](https://arxiv.org/abs/2505.24063)**, **[LingLan](https://arxiv.org/abs/2602.01779)** | Tasks are spelled out; more under [Datasets](#datasets) |
| Write related work | Recent scoping reviews | Skim [Surveys](#surveys) before individual model papers |

Same name does not mean the same project. ZhongJingGPT is not the AAAI CMtMedQA line, and more than one benchmark is called TCM-Eval. [Getting Started](wiki/Getting-Started.md) if that is confusing.

## Open models

The table above is a shortlist. Expand the folds for public checkpoints, paper-only models, general Chinese medical bases, closed products, and Kampo/Korean-medicine work.

<details>
<summary>Public weights (12)</summary>

| Model | Year | Org | Focus | Links |
| --- | :---: | --- | --- | --- |
| **Xinghe** | 2026 | Xinghe-TCM | Reason · Classics | [Weights](https://huggingface.co/zsyjsld/Xinghe1.2-9B) · [Data](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2) |
| **ZhiFangDanTai** | 2025 | Capital Normal University | RAG · KG | [Paper](https://arxiv.org/abs/2509.05867) · [Weights](https://huggingface.co/tczzx6/ZhiFangDanTai1.0) · [Data](https://huggingface.co/datasets/tczzx6/ZhiFangDanTai1.0) |
| **Baize-TCM-LLM** | 2025 | Institute of Chinese Materia Medica | ICMM Baize TCM QA models on Qwen3 (0… | [Weights](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model) · [Data](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3) |
| **BianCang** | 2025 | Qilu University of Technology | BianCang TCM LLM series (IEEE JBHI)… | [Paper](https://arxiv.org/abs/2411.11027) · [Weights](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct) · [Code](https://github.com/QLU-NLP/BianCang) |
| **仲景 (ZhongJing)** | 2025 | — | ZhongJingGPT, an expert-knowledge-gu… | [Paper](https://doi.org/10.26599/TST.2025.9010046) · [Weights](https://huggingface.co/CMLM/ZhongjingGPT1_13B) · [Code](https://github.com/pariskang/CMLM-ZhongJing) |
| **ViTCM-LLM** | 2025 | Tsinghua Shenzhen International Graduate School | MM · RAG | [Paper](https://doi.org/10.1109/bibm66473.2025.11357113) · [Weights](https://huggingface.co/Mark-CHAE/ViTCM-LLM) · [Code](https://github.com/jw-chae/ViTCM_LLM) |
| **TCMChat** | 2025 | — | Generative TCM LLM built via pre-tra… | [Paper](https://doi.org/10.1016/j.phrs.2024.107530) · [Weights](https://huggingface.co/ZJUFanLab/TCMChat-600k) · [Code](https://github.com/ZJUFanLab/TCMChat) · [Data](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k) |
| **ShizhenGPT** | 2025 | The Chinese University of Hong Kong | MM | [Paper](https://arxiv.org/abs/2508.14706) · [Weights](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni) · [Code](https://github.com/FreedomIntelligence/ShizhenGPT) |
| **ChatTCM** | 2025 | — | SylvanL open TCM LLM (Qwen2-7B conti… | [Weights](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain) |
| **TCMLLM / Lingdan** | 2024 | Beijing Jiaotong University | TCMLLM / Lingdan for TCM modeling an… | [Paper](https://doi.org/10.1016/j.dcmed.2025.01.007) · [Weights](https://huggingface.co/TCMLLM/Lingdan-13B-Base) · [Code](https://github.com/2020MEAI/TCMLLM) |
| **MedChatZH** | 2024 | — | MedChatZH: a fine-tuned LLM for TCM… | [Paper](https://doi.org/10.1016/j.compbiomed.2024.108290) · [Code](https://github.com/tyang816/MedChatZH) · [Weights](https://huggingface.co/tyang816/medchatzh) · [Data](https://huggingface.co/datasets/tyang816/MedChatZH) |
| **神农大模型 (ShenNong-TCM-LLM)** | 2023 | — | ShenNong-TCM-LLM, the first TCM larg… | [Weights](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM) · [Code](https://github.com/michael-wzhu/ShenNong-TCM-LLM) · [Data](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset) |

</details>

<details>
<summary>Paper or product only, no verified weights (52)</summary>

<details>
<summary>2026 · 14</summary>

- [*Digital Chinese Medicine*] **QingNangTCM** Parameter-efficient fine-tuned TCM QA and clinical reasoning model; builds the 100k-item **QnTCM_Dataset**. [Hebei North University] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.002)]
- [*ISCTIS 2026*] **Tongue–face multimodal fusion diagnosis** Tongue–face multimodal feature fusion with LLM-driven intelligent TCM diagnosis. [Xiamen University of Technology] [[DOI](https://doi.org/10.1109/ISCTIS70043.2026.11572361)]
- **砭石云中医** Bianshi Yun Zhongyi is Wisdom Eye's TCM application on its filed multimodal Bianshi model, using a symptom-to-formula knowledge graph for four-diagnostic capture and decision support. [[Website](https://www.a-eye.cn/news_list/420.html)] [[Website](https://www.a-eye.cn/news_list/356.html)]
- **Lingdan-V2** BJTU's second Lingdan TCM reasoning family (Qwen3 4B/8B/14B with CPT, SFT, and prescription GRPO). ModelScope checkpoints exist but require access requests, so they are not marked freely downloadable. [Beijing Jiaotong University] [[Code](https://github.com/TCMAI-BJTU/Lingdan-V2)] [[ModelScope](https://modelscope.cn/models/TCMAIBJTU/Lingdan-14B-R1)] [[Paper](https://arxiv.org/abs/2610.14705)]
- **岐元** Qiyuan is the Seventh People's Hospital of Shanghai's TCM model, trained with pretraining, domain fine-tuning, and expert reinforcement learning, for generative records and famous-doctor agent twins. [[News](https://finance.sina.com.cn/jjxw/2026-07-26/doc-inikassr0678770.shtml)]
- **华族本草** Huazu Bencao is an ethnic-medicine model led by Guizhou Medical University, using Shuzhi Qihuang and Qwen to connect multi-ethnic classics and a knowledge graph across ingredient screening, formulation, quality control, and teaching. [[Website](https://www.gmc.edu.cn/info/1059/30300.htm)] [[News](https://www.news.cn/tech/20260804/f973d6fa9de640328fec0194c63335a3/c.html)]
- [*JMIR Medical Informatics*] **TongueVLM** Multimodal VLM for TCM tongue diagnosis, description generation, and constitution reasoning. JMIR page blocked; OpenAlex lists HFUT and Anhui University of Chinese Medicine et al. [Hefei University of Technology, Anhui University of Chinese Medicine et al.] [[Paper](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- [*世界科学技术-中医药现代化*] **TCM Classic-Translator（中医古籍今译）** TCM Classic-Translator is a named LoRA model for classical-to-modern TCM translation, trained on Huangdi Neijing and Shanghan Lun parallels with commentary augmentation. Reported scores are BLEU-4 39.35 and ROUGE-L 54.66. No public weights were found. [[DOI](https://doi.org/10.11842/wst.20250916005)]
- [*Digital Chinese Medicine*] **Qwen-TCM-Dia** Specialty fine-tuned model for TCM diarrhea care (CPT + CoT SFT) covering symptom→pathomechanism→method→formula chains. Digital Chinese Medicine authors at Beijing Hospital of TCM (CMU) and BUCM et al. [Beijing Hospital of TCM, Capital Medical University, Beijing University of Chinese Medicine et al.] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.003)]
- [*arXiv*] **Med-Shicheng** Lightweight master-physician experience-inheritance framework built on Tianyi; a single model internalizes 5 national masters' knowledge systems across 7 task types. [Nanjing University of Chinese Medicine et al.] [[Paper](https://arxiv.org/abs/2603.23520)] [[Code](https://github.com/NJUCM-BJUCM-TCM-AI/Med-Shicheng)]
- [*Chinese Herbal Medicines*] **HerbWise** Domain LLM for traditional herbal medicine (THM), serving herbal modernization and standardization. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.chmed.2026.02.010)]
- [*Chinese Medicine*] **GastroTCM** TCM gastroenterology LLM fine-tuned from Llama3-8B with RAG and agent scaffolding. Chinese Medicine paper from Tsinghua TCM-X and China-Japan Friendship Hospital et al. [Tsinghua University, China-Japan Friendship Hospital et al.] [[Paper](https://link.springer.com/article/10.1186/s13020-025-01295-8)]
- [*arXiv*] **DongYuan** Integrative spleen–stomach disease diagnosis LLM framework combining TCM pattern differentiation with Western diagnostic reasoning. arXiv PDF authors at Hebei Provincial Hospital of TCM and CASIA et al. [Hebei Provincial Hospital of Traditional Chinese Medicine, Institute of Automation, Chinese Academy of Sciences et al.] [[Paper](https://arxiv.org/abs/2603.28191)]
- [*Chinese Medicine*] **DFGLM-TCM** Dongfang Hospital / Zhipu TCM clinical system that models textbook knowledge and practitioner experience in separate modules; paper is out, weights are not. [Beijing University of Chinese Medicine, Zhipu AI] [[DOI](https://doi.org/10.1186/s13020-026-01512-y)]

</details>

<details>
<summary>2025 · 27</summary>

- **薪火中国药** Xinhuo Zhongguoyao is an education TCM model led by Beijing University of Chinese Medicine for study, teaching, research, administration, and international communication, and it received generative-AI service filing in 2026. [[Website](https://www.bucm.edu.cn/xwgl/6762cbff37ae4939829bbd3efae96225.htm)] [[Website](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)] [[News](https://www.beijing.gov.cn/fuwu/lqfw/gggs/202604/t20260423_4605343.html)]
- **智赋岐黄天功** Zhifu Qihuang Tiangong is a TCM model from Zhifu Qihuang and Harbin Institute of Technology, trained on cases and famous-doctor formulas for several syndrome systems, and it backs four-diagnostic constitution reports under algorithm filing. [[Website](https://qihuang-ai.com/ai-platform/tiangong)] [[Website](https://qihuang-ai.com/about)]
- [*arXiv*] **ZMT-M1** ZMT-M1 TCM LLM and the dynamic, extensible TCM-Eval benchmark platform. [Beihang University] [[Paper](https://arxiv.org/abs/2511.07148)] [[Platform](https://tcmeval.bamaidical.com)]
- [*Chinese Medicine*] **XuanHuGPT** TCM domain LLM built with parameter-efficient fine-tuning (PEFT). [Hebei North University] [[DOI](https://doi.org/10.1186/s13020-025-01200-3)]
- **张仲景中医药大模型** The Zhang Zhongjing TCM model, released by Henan University of Chinese Medicine and the University of Science and Technology Beijing, covers syndrome differentiation, syndrome-element recommendation, classical formulas, and formula analysis for clinical decision support. [[Website](https://hactcm.edu.cn/info/1022/211754.htm)] [[Website](https://news.ustb.edu.cn/info/1981/67772.htm)]
- **广医·岐智** Guangyi Qizhi is Guang'anmen Hospital's TCM service model for triage, pre-consultation, charting, and syndrome-formula advice; version 2.0 adds an agent doctor and the system has completed algorithm filing. [[Website](https://www.gamyy.cn/gzb/news/big/110133.html)] [[Website](https://www.gamyy.cn/gzb/news/big/114632.html)] [[News](https://www.gamyy.cn/gzb/news/big/113898.html)]
- [*Expert Systems with Applications*] **Qibo** TCM LLM and Qibo Benchmark from Tianjin University et al.; CPT + SFT for SDT and QA. [Tianjin University, Tianjin University of Traditional Chinese Medicine] [[Published](https://doi.org/10.1016/j.eswa.2025.127672)] [[Paper](https://arxiv.org/abs/2403.16056)] [[DOI](https://doi.org/10.1016/j.eswa.2025.127672)]
- **女娲 (Nüwa / TCM-Nvwa)** Nüwa TCM LLM training stack (continual pretraining, SFT, reward modeling, RLAIF) on Ziya-LLaMA-13B. Repo ships only partial pretrain/TCM-QR/reward data and no standalone weights; GitHub created April 2025, distinct from arXiv 2411.00897. [[Code](https://github.com/synbol/TCM-Nvwa)]
- [*arXiv*] **TianHui** Domain LLM for 12 TCM scenarios (DeepSeek-R1-Distill-Qwen-14B + PT/SFT) with open code and eval scripts. arXiv PDF authors at Chengdu University of TCM. [Chengdu University of Traditional Chinese Medicine] [[Paper](https://arxiv.org/abs/2509.19834)] [[Code](https://github.com/JYfantast/TianHui)]
- [*Information Fusion*] **Tianyi** ~7B TCM LLM from NJUCM et al. with reading–clinic–apprenticeship training stages, TCMEval, and real-world validation. [Nanjing University of Chinese Medicine] [[Published](https://doi.org/10.1016/j.inffus.2025.103663)] [[Paper](https://arxiv.org/abs/2505.13156)] [[News](https://blog.sciencenet.cn/blog-279293-1501581.html)]
- **固生堂中医大脑** Gushengtang TCM Brain connects national-physician AI avatars to the hospital information system for history taking, record drafting, syndrome support, and prescription support with traceable rationale. [[Website](https://www.gstzy.cn/news/detail/10/14076.html)] [[Website](https://www.gstzy.cn/news/detail/10/14125.html)]
- **众星·长白岐黄** Zhongxing Changbai Qihuang is a multimodal reasoning TCM model from Changchun University of Chinese Medicine and partner universities, with a family health assistant and a Jipai doctor assistant. [[Website](https://www.jlbtc.edu.cn/info/1042/93113.htm)] [[News](https://news.cnjiwang.com/jwyc/202512/4006547.html)]
- **伊尹中医经典大模型** The Yiyin classic TCM model from Zhongyi Online is trained on medical canons and classical prescriptions, shows its syndrome-reasoning steps, and supports primary-care clinics in Song County. [[News](https://www.cntcm.com.cn/content/202509/17/c284139.html)]
- **任度·素问** Rendu Suwen is Transn's TCM model on its Rendu base and moH architecture, offering proactive consultation, syndrome analysis, and formula suggestions, and it passed CAICT's TCM large-model evaluation at level 4+. [[Website](https://www.transn.com/about_us/consult/article/1965645664716955649)]
- **中医横琴 (Hengqin-R1)** Hengqin-R1 is the Guangdong Provincial Laboratory of TCM's vertical reasoning model, combining fine-tuning, reinforcement learning, and a knowledge graph for syndrome reasoning, combined Chinese-Western medication agents, and objective four diagnostics. [[Website](https://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/dtxx/content/post_3807664.html)] [[Website](https://www.gzucm.edu.cn/info/1621/109561.htm)]
- [*IEEE BIBM 2025*] **TCM-VisResolve (TCM-VR)** Qwen2.5-VL-based TCM multimodal LLM — 163-class dried-herb recognition over 220k images plus clinical MCQs with 880k candidate answers. [Minzu University of China] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356679)]
- [*APWeb-WAIM 2025*] **TCM-R1** TCM LLM with GRPO-enhanced reasoning. [Southwest University] [[Paper](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*Computers in Biology and Medicine*] **TCM-KLLaMA** KG-fused LLM for intelligent TCM formula generation. PubMed 40056842 lists Zhejiang Gongshang University and Hangzhou First People's Hospital (Westlake University School of Medicine). [Zhejiang Gongshang University, Hangzhou First People's Hospital, Westlake University School of Medicine] [[DOI](https://doi.org/10.1016/j.compbiomed.2025.109887)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/40056842)]
- [*Chinese Medicine*] **TCM-DS** Domain LLM for medicine–food homology dietary-therapy recommendation. [Macau University of Science and Technology] [[DOI](https://doi.org/10.1186/s13020-025-01249-0)]
- [*arXiv*] **RACE-Align** RACE-Align: retrieval-augmented, CoT-style DPO alignment of a compact Qwen3-1.7B for TCM reasoning. arXiv PDF authors at ShanghaiTech, Henan University, and Liaoning University of TCM. [ShanghaiTech University, Henan University, Liaoning University of Traditional Chinese Medicine] [[arXiv](https://arxiv.org/abs/2506.02726)]
- [*IEEE ICIP 2025*] **MCM** Multi-agent collaborative multimodal TCM diagnosis framework (IEEE ICIP 2025). [Shanghai Computer Software Technology Development Center] [[Code](https://github.com/JerryMazeyu/MCM)] [[Published](https://doi.org/10.1109/icip55913.2025.11084334)]
- [*arXiv*] **Ladder-base (GRPO-TCM)** First GRPO reinforcement-learning-aligned TCM LLM, from the TCM-Ladder team. arXiv PDF authors at University of Missouri and Shanghai University of TCM et al. [University of Missouri, Shanghai University of Traditional Chinese Medicine et al.] [[Paper](https://arxiv.org/abs/2510.17402)]
- [*arXiv*] **Hengqin-RA-v1** LLM and companion dataset for TCM diagnosis and treatment of rheumatoid arthritis. arXiv/DOI page lists Chinese Medicine Guangdong Laboratory and Southern University of Science and Technology. [Chinese Medicine Guangdong Laboratory, Southern University of Science and Technology] [[Paper](https://arxiv.org/abs/2501.02471)]
- [*Applied Sciences*] **Gen-SynDi** Knowledge-guided generative-AI framework for dual education of syndrome differentiation and disease diagnosis. [College of Korean Medicine, Wonkwang University, Iksan 54538, Republic of Korea, College of Korean Medicine, Woosuk University, Jeon-Ju 54987, Republic of Korea, Dongje Medical Co., Ltd., Daegu 42187, Republic of Korea, College of Medicine, Yeungnam University, Daegu 42415, Republic of Korea] [[DOI](https://doi.org/10.3390/app15094862)]
- [*arXiv*] **DoPI** Doctor-like proactive inquiry TCM LLM (guide + expert models); reported inquiry accuracy 84.68%. arXiv HTML authors at Tianjin University and CUHK et al. [Tianjin University, The Chinese University of Hong Kong et al.] [[Paper](https://arxiv.org/abs/2507.04877)]
- [*IEEE BIBM 2025*] **ChatGLM-FGIDs-TCM** Knowledge-fused ChatGLM clinical decision-support model for functional gastrointestinal disorders (FGIDs). [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356283)]
- [*arXiv*] **BenCao** Instruction-aligned multimodal TCM assistant (ChatGPT/GPTs Store) with tongue APIs and knowledge bases (distinct from HuaTuo/BenCao). arXiv HTML authors at University of Missouri and Shanghai University of TCM et al. [University of Missouri, Shanghai University of Traditional Chinese Medicine et al.] [[Paper](https://arxiv.org/abs/2510.17415)]

</details>

<details>
<summary>2024 · 9</summary>

- **数智本草** Shuzhi Bencao is Tasly and Huawei Cloud's dual language-and-molecule TCM model, built on Pangu, for classic-text QA, molecular computation, and herbal R&D screening. [[Website](https://www.huawei.com/cn/huaweitech/publication/202503/pioneer-developers-of-huaweicloud)] [[Website](https://tjdsj.tjcac.gov.cn/tjsg/hyzx/202405/t20240523_6632807.html)] [[News](https://www.news.cn/politics/20240509/be28f085474b45fd9d6829766195568d/c.html)]
- **数智岐黄** Shuzhi Qihuang is a TCM model from East China Normal University and partner institutes; version 1.0 offers QA and knowledge-graph interaction, and version 2.0 extends it to multimodal Chinese and Western medicine data. [[Website](https://www.ecnu.edu.cn/info/1426/65503.htm)] [[Website](https://www.shanghai.gov.cn/nw4411/20240120/1a19dcf117f7430b971db72e53ed4d9b.html)] [[News](https://hub.baai.ac.cn/view/41476)]
- **天河·灵枢** Tianhe Lingshu is a TCM model from the National Supercomputing Center in Tianjin and Tianjin University of Traditional Chinese Medicine; version 1.0 targets acupuncture with a 3D acupoint avatar, and version 2.0 covers more than 20 clinical specialties. [[Website](https://www.nscc-tj.cn/xwxq.php?id=628)] [[Website](https://www.tjutcm.edu.cn/info/1047/2084.htm)] [[News](https://www.tjlgbj.gov.cn/tjlgb/system/2025/08/09/030003838.shtml)]
- **大数中医 (BigDataTCM)** BigDataTCM (34B): a vertical TCM LLM co-developed by HAUT's Complexity Science institute and Apus, offering medical QA, diagnostic support and TCM knowledge services. [[Code](https://github.com/HAUT-CS/BigDataTCM)]
- **大医金匮** Dayi Jingui is a TCM model jointly built by Wenge and the China Academy of Chinese Medical Sciences for syndrome reasoning, treatment planning, and four-diagnostic health management. [[Website](https://tcm.wenge.com/)]
- [*AAAI*] **仲景（CMtMedQA 线，Yang et al.）** ZhongJing (CMtMedQA line, Yang et al.): a TCM LLM distinct from the Kang-line ZhongJingGPT—full CPT+SFT+RLHF pipeline on Ziya-LLaMA-13B over ~70K real multi-turn doctor-patient dialogues (AAAI 2024). [[Paper](https://doi.org/10.1609/aaai.v38i17.29907)] [[arXiv](https://arxiv.org/abs/2308.03549)]
- **仲思** Zhongsi is a vertical TCM model released by Merchants Union Consumer Finance with Sun Yat-sen University and Shenzhen Hospital of Guangzhou University of Chinese Medicine for QA, consultation notes, and formula suggestions in community clinics. [[News](https://www.stcn.com/article/detail/1454029.html)]
- [*Computer Methods and Programs in Biomedicine Update*] **TCM-GPT** Efficient pre-training of LLMs for domain adaptation in Traditional Chinese Medicine. Journal metadata lists BUPT and UCL. [Beijing University of Posts and Telecommunications, University College London] [[DOI](https://doi.org/10.1016/j.cmpbup.2024.100158)] [[Paper](https://arxiv.org/abs/2311.01786)]
- [*Scientific Reports*] **CPMI-ChatGLM** Parameter-efficient fine-tuning of ChatGLM with Chinese patent medicine instructions. Authors at Anhui University of Chinese Medicine and CACMS Anhui Computer Application Research Institute. [Anhui University of Chinese Medicine, Anhui Computer Application Research Institute of Chinese Medicine, CACMS] [[DOI](https://doi.org/10.1038/s41598-024-56874-w)]

</details>

<details>
<summary>2023 · 2</summary>

- **黄帝 (HuangDi)** HuangDi: a TCM classics QA LLM built on Ziya-LLaMA-13B, pretrained on 22 TCM textbooks plus TCM web corpora and SFT-tuned with ancient-book instruction data (Library Tribune 2024). [[Code](https://github.com/Zlasejd/HuangDI)]
- **岐黄问道** Qihuang Wendao is Nanjing Dajing TCM's vertical model, using a large TCM knowledge graph and clinical data for syndrome diagnosis, prescriptions, and regimen advice in medical institutions. [[News](https://js.cnr.cn/rdzt/qnjs/qnjsgdxw/20230801/t20230801_526358407.shtml)]

</details>


</details>

<details>
<summary>General Chinese medical models, often used as bases (30)</summary>

<details>
<summary>2026 · 1</summary>

- [*arXiv*] **Baichuan-M3** Baichuan's third open medical reasoning model (235B on Qwen3) with SPAR staged RL and fact-aware RL for active inquiry and hallucination control; strong HealthBench and SCAN-bench results. [Baichuan Intelligence] [[Paper](https://arxiv.org/abs/2602.06570)] [[Code](https://github.com/baichuan-inc/Baichuan-M3-235B)] [[Model](https://huggingface.co/baichuan-inc/Baichuan-M3-235B)]

</details>

<details>
<summary>2025 · 4</summary>

- [*arXiv*] **Baichuan-M2** Baichuan's second open medical reasoning model (32B on Qwen2.5-32B) with a large verifier system and multi-stage RL; strong open-source HealthBench results. [Baichuan Intelligence] [[Paper](https://arxiv.org/abs/2509.02208)] [[Code](https://github.com/baichuan-inc/Baichuan-M2-32B)] [[Model](https://huggingface.co/baichuan-inc/Baichuan-M2-32B)]
- [*arXiv*] **Baichuan-M1** Baichuan's from-scratch open medical LLM (14B), trained on ~20T medical+general tokens across 20+ specialties; a common base for later TCM fine-tunes. [Baichuan Intelligence] [[Paper](https://arxiv.org/abs/2502.12671)] [[Code](https://github.com/baichuan-inc/Baichuan-M1-14B)] [[Model](https://huggingface.co/baichuan-inc/Baichuan-M1-14B-Instruct)] [[Base](https://huggingface.co/baichuan-inc/Baichuan-M1-14B-Base)]
- **Taiyi-2** Second Taiyi open biomedical model, moving from Qwen-7B to GLM4-9B with tighter data filters and task instructions. The model card still cites the Taiyi-1 JAMIA paper (10.1093/jamia/ocae037); there is no separate Taiyi-2 paper. [Dalian University of Technology] [[Model](https://huggingface.co/DUTIR-BioNLP/Taiyi2-chat)] [[Code](https://github.com/DUTIR-BioNLP/Taiyi-LLM)]
- [*arXiv*] **WiNGPT3** Winning Health's third medical reasoning model (32B on Qwen2.5) with multi-stage SFT+RL and WiNEX hospital integration; tech report and code are public, weights are not verified as downloadable. [Winning Health] [[Paper](https://arxiv.org/abs/2505.17387)] [[Code](https://github.com/winninghealth/WiNGPT3)]

</details>

<details>
<summary>2024 · 6</summary>

- [*ACM Trans. Knowl. Discov. Data*] **BenCao (formerly HuaTuo)** Instruction-tuned Chinese medical LLM (BenCao / formerly HuaTuo). [Harbin Institute of Technology] [[Paper](https://arxiv.org/pdf/2309.04175.pdf)] [[Code](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)]
- [*arXiv*] **明医 (MING)** MING: a Chinese medical consultation LLM using a sparse mixture of low-rank adapter experts (MING-MoE) for medical multi-task learning (arXiv 2024). [[Paper](https://arxiv.org/abs/2404.09027)] [[Related MedCare](https://aclanthology.org/2024.findings-emnlp.619/)] [[Code](https://github.com/MediaBrain-SJTU/MING)]
- [*JAMIA*] **Taiyi** DUTIR bilingual biomedical LLM on Qwen-7B for QA, doctor–patient dialogue, report generation, and information extraction (JAMIA 2024). [Dalian University of Technology] [[DOI](https://doi.org/10.1093/jamia/ocae037)] [[Code](https://github.com/DUTIR-BioNLP/Taiyi-LLM)] [[Model](https://huggingface.co/DUTIR-BioNLP/Taiyi-LLM)]
- [*arXiv*] **HuatuoGPT-o1** HuatuoGPT medical complex-reasoning model trained with verifiable problems and a medical verifier; 7B/72B cover Chinese and English. [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[Paper](https://arxiv.org/abs/2412.18925)] [[Code](https://github.com/FreedomIntelligence/HuatuoGPT-o1)] [[Model](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-7B)]
- [*arXiv*] **HuatuoGPT-Vision** HuatuoGPT multimodal medical model that injects visual knowledge at scale; a common Chinese medical vision baseline. [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[Paper](https://arxiv.org/abs/2406.19280)] [[Code](https://github.com/FreedomIntelligence/HuatuoGPT-Vision)] [[Model](https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B-Qwen2.5VL)]
- [*arXiv*] **Apollo** FreedomIntelligence multilingual medical LLM (including Chinese) with ApolloCorpus and XMedBench. [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[Paper](https://arxiv.org/abs/2403.03640)] [[Code](https://github.com/FreedomIntelligence/Apollo)] [[Model](https://huggingface.co/FreedomIntelligence/Apollo-7B)]

</details>

<details>
<summary>2023 · 19</summary>

- [*arXiv*] **Qilin-Med** Multi-stage Chinese medical LLM (CPT+SFT+DPO on Baichuan-7B) releasing the ~3GB ChiMed corpus, optionally with RAG. arXiv PDF authors at Peking University and HKUST (Guangzhou) et al. [Peking University, Hong Kong University of Science and Technology (Guangzhou) et al.] [[Paper](https://arxiv.org/abs/2310.09089)] [[Code](https://github.com/williamliujl/Qilin-Med)] [[Dataset](https://huggingface.co/datasets/williamliu/ChiMed)]
- **BianQue-2** Second BianQue open consultation model with stronger multi-turn questioning; a common CMB baseline. [South China University of Technology, Guangdong Key Laboratory of Digital Twin Humans] [[Code](https://github.com/scutcyr/BianQue)] [[Model](https://huggingface.co/scutcyr/BianQue-2)]
- [*arXiv*] **BianQue** Chinese proactive health LLM for everyday living spaces (BianQue). [South China University of Technology, Guangdong Key Laboratory of Digital Twin Humans] [[Code](https://github.com/scutcyr/BianQue)] [[Paper](https://arxiv.org/abs/2310.15896)]
- **孙思邈 (Sunsimiao)** Sunsimiao Chinese medical LLM; Sunsimiao-7B fine-tuned from Qwen2-7B on curated medical data, reaching 30B-level SOTA on CMB-Exam. [[Code](https://github.com/X-D-Lab/Sunsimiao)]
- **QiZhenGPT** Chinese clinical QA model for drugs, diseases, procedures, and labs (QiZhenGPT). [Zhejiang University] [[Code](https://github.com/CMKRG/QiZhenGPT)]
- **WiNGPT2** Winning Health open medical LLM on Qwen for medical QA, record understanding, and multi-turn consults; 7B/14B weights are public. [Winning Health] [[Model](https://huggingface.co/winninghealth/WiNGPT2-14B-Chat)] [[7B](https://huggingface.co/winninghealth/WiNGPT2-7B-Chat)]
- [*arXiv*] **HuatuoGPT-II** Second HuatuoGPT generation with one-stage medical adaptation; 7B/13B use Baichuan2 backbones and remain a standard Chinese medical baseline. [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[Paper](https://arxiv.org/abs/2311.09774)] [[Code](https://github.com/FreedomIntelligence/HuatuoGPT-II)] [[Model](https://huggingface.co/FreedomIntelligence/HuatuoGPT2-7B)]
- [*EMNLP findings*] **HuaTuoGPT** Large language model trained on Chinese medical corpora (HuaTuoGPT). [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[DOI](https://doi.org/10.18653/v1/2023.findings-emnlp.725)] [[Paper](https://aclanthology.org/2023.findings-emnlp.725/)] [[Code](https://github.com/FreedomIntelligence/HuatuoGPT)]
- [*arXiv*] **SoulChat** SCUT mental-health dialogue LLM from the same lab as BianQue; a common Chinese health-conversation baseline. [South China University of Technology, Guangdong Key Laboratory of Digital Twin Humans] [[Paper](https://arxiv.org/abs/2311.00273)] [[Code](https://github.com/scutcyr/SoulChat)] [[Model](https://huggingface.co/scutcyr/SoulChat)]
- **PULSE** OpenMEDLab Chinese medical LLM (Bloom 7B/14B) for exams, report reading, record structuring, and simulated diagnosis. [Shanghai AI Laboratory] [[Code](https://github.com/openmedlab/PULSE)] [[Model](https://huggingface.co/OpenMEDLab/PULSE-7bv5)]
- **MedicalGPT** Open training stack for Chinese medical LLMs (pretrain/SFT/RLHF/DPO), often reused as a baseline pipeline in TCM fine-tuning. [[Code](https://github.com/shibing624/MedicalGPT)]
- [*arXiv*] **IvyGPT** LLaMA-based Chinese medical QA model fine-tuned with curated clinical QA and RLHF; listed as an open baseline in the CMB paper. arXiv PDF authors at Macao Polytechnic University. [Macao Polytechnic University] [[Paper](https://arxiv.org/abs/2307.10512)] [[Code](https://github.com/Ivy0529/IvyGPT)]
- [*arXiv*] **DoctorGLM** Early open Chinese consultation model on ChatGLM-6B with LoRA/P-Tuning; a frequent 2023 Chinese medical baseline. arXiv HTML authors at ShanghaiTech and United Imaging Intelligence et al. [ShanghaiTech University, United Imaging Intelligence et al.] [[Paper](https://arxiv.org/abs/2304.01097)] [[Code](https://github.com/xionghonglin/DoctorGLM)]
- [*arXiv*] **DISC-MedLLM** Fudan DISC conversational medical LLM on Baichuan-13B, with DISC-Med-SFT built from knowledge graphs and reconstructed consultations. [Fudan University] [[Paper](https://arxiv.org/abs/2308.14346)] [[Code](https://github.com/FudanDISC/DISC-MedLLM)] [[Model](https://huggingface.co/Flmc/DISC-MedLLM)] [[Dataset](https://huggingface.co/datasets/Flmc/DISC-Med-SFT)]
- [*arXiv*] **ClinicalGPT** BUPT clinical Chinese medical model (BLOOM-7B) fine-tuned on records, knowledge, exams, and multi-turn consults; a common CMB-era baseline. HF hosts a medicalai snapshot. [Beijing University of Posts and Telecommunications] [[Paper](https://arxiv.org/abs/2306.09968)] [[Model](https://huggingface.co/medicalai/ClinicalGPT-base-zh)]
- [*arXiv*] **ChiMed-GPT** USTC Chinese medical LLM continued from Ziya-v2 with pretraining, SFT, and RLHF for extraction, QA, and multi-turn dialogue. [University of Science and Technology of China] [[Paper](https://arxiv.org/abs/2311.06025)] [[Code](https://github.com/synlp/ChiMed-GPT)] [[Model](https://huggingface.co/SYNLP/ChiMed-GPT-1.0)]
- **ChatMed** ChatMed series of Chinese medical LLMs, including ChatMed-Consult trained on 500k+ online consultation dialogues. GitHub README cites Wei Zhu and Xiaoling Wang; no standalone journal paper. [East China Normal University] [[Code](https://github.com/michael-wzhu/ChatMed)] [[Model](https://huggingface.co/michaelwzhu/ChatMed-Consult)]
- **ChatGLM-Med** HIT-SCIR ChatGLM-6B instruction-tuned on Chinese medical KGs, sharing data lineage with BenCao/HuaTuo; a frequent CMB baseline. [Harbin Institute of Technology] [[Code](https://github.com/SCIR-HI/Med-ChatGLM)]
- **CareGPT** Open Chinese medical LLM training stack (pretrain through DPO) with accompanying weights, often used to reproduce Chinese medical fine-tunes. README attributes the work to Macao Polytechnic University. [Macao Polytechnic University] [[Code](https://github.com/WangRongsheng/CareGPT)]

</details>


</details>

<details>
<summary>Closed Chinese medical products, no verified weights (4)</summary>

- **iFlytek Spark Medical** Closed iFlytek medical LLM (Spark Medical X1/X2) behind Zhiyi Assistant and Xiaoyi; no public weights, listed as an industry baseline. [iFlytek] [[Website](https://www.xunfeihealthcare.com/)] [[News](https://www.cn-healthcare.com/article/20250303/wap-content-585822.html)]
- **Ant Afu** Closed Ant multimodal medical LLM, first shipped as Alipay AQ and later rebranded Afu for consults, report and pill-box reading; announced at WAIC 2024, no public weights. [Ant Group] [[Website](https://www.antafu.com/)] [[Press](https://www.antgroup.com/news-media/press-releases/1720166400000)]
- **Tencent Hunyuan Medical** Closed Tencent Health medical LLM on Hunyuan for QA, triage, records, and imaging; announced by Tencent Jarvis Lab, no public weights. [Tencent] [[Website](https://healthcare.tencent.com/)] [[News](https://healthcare.tencent.com/news/1603)]
- [*Sci China Life Sci*] **PanGu Drug Model** Closed Huawei Cloud / SIMM molecule foundation model (~1.7B small molecules) for property prediction, generation, and optimization; later used under Shuzhi Bencao. [Huawei Cloud, Shanghai Institute of Materia Medica, CAS] [[DOI](https://doi.org/10.1007/s11427-022-2239-y)] [[Website](https://www.huaweicloud.com/cases/pgyw.html)]

</details>

<details>
<summary>Kampo / Korean-medicine models and systems (1)</summary>

- **KAMPO LLM** Official site still live. Closed Kampo API from VARYTEX with the Japan Society for Oriental Medicine; page reports 97.4% (Pro) and 92.1% (Flash) on 471 specialist-training items; no public weights. [VARYTEX, Japan Society for Oriental Medicine] [[Website](https://kampollm.varytex.co.jp/)]

</details>

<details>
<summary>Other Hugging Face sizes and GGUF (12)</summary>

- **Xinghe** — Xinghe Neijing reasoning model weights. [[Model](https://huggingface.co/zsyjsld/Xinghe1.2-9B)] [[GGUF](https://huggingface.co/zsyjsld/Xinghe1.2-9B-GGUF)]
- **ZhiFangDanTai** (site down) — ZhiFangDanTai formula-generation weights. The public Hugging Face page returned 404 on 2026-10-21. [[Model](https://huggingface.co/tczzx6/ZhiFangDanTai1.0)]
- **Baize** — Baize TCM LLM weights. [[Model](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model)] [[8B-16bit](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit)]
- **medchatzh** — MedChatZH weights. [[medchatzh](https://huggingface.co/tyang816/medchatzh)]
- **ZhongJing** — ZhongJing GPT weights. [[ZhongjingGPT1_13B](https://huggingface.co/CMLM/ZhongjingGPT1_13B)] [[ZhongJing-2-1.8B](https://huggingface.co/CMLL/ZhongJing-2-1_8b)]
- **TCMChat** — TCMChat weights. [[TCMChat-600k](https://huggingface.co/ZJUFanLab/TCMChat-600k)]
- **ShizhenGPT** — ShizhenGPT multimodal weight series. [[7B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-LLM)] [[7B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-VL)] [[7B-Omni](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[32B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-LLM)] [[32B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-VL)]
- **ShenNong-TCM-LLM** — ShenNong-TCM-LLM weights. [[ShenNong-TCM-LLM](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]
- **Lingdan** — Lingdan / TCMLLM weights. [[Lingdan-13B-Base](https://huggingface.co/TCMLLM/Lingdan-13B-Base)] [[Lingdan-13B-PR](https://huggingface.co/TCMLLM/Lingdan-13B-PR)]
- **ChatTCM-7B-SFT** — ChatTCM full-parameter SFT checkpoint. [[Model](https://huggingface.co/SylvanL/ChatTCM-7B-SFT)]
- **ChatTCM** — ChatTCM pretrained weights. [[ChatTCM-7B-Pretrain](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)]
- **BianCang** — BianCang open-weight series. [[Qwen2.5-7B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)] [[Qwen2.5-14B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-14B-Instruct)]

</details>

## News

<details>
<summary>55 items; recent: 南京中医药大学发布灵素·艾护中医护理大模 · 广医·岐智2.0 · 首发首展</summary>

<details>
<summary>2026 · 22</summary>

- [2026.10] Reports say Nanjing University of Chinese Medicine released the LingSu Aihu TCM nursing model on 9 October; 27 member hospitals are the first sites. [[Link](https://finance.sina.com.cn/jjxw/2026-10-10/doc-iniutqmk0582279.shtml)]
- [2026.09] Guang'anmen Hospital shows **Guangyi Qizhi 2.0** at CIFTIS 2026, with AI doctor An'an covering six hospital scenes from patient service to ward management. [[Link](https://app.xinhuanet.com/news/article.html?articleId=202609101de3e66a53f7474ba7d373deaaa7e122)]
- [2026.09] Beijing University of Chinese Medicine debuts a TCM constitution-identification system and an embodied tuina robot at the CIFTIS 2026 TCM pavilion. [[Link](https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202608/t20260807_4812596.html)]
- [2026.09] China News Service reports that the formula-syndrome model opened for access on 19 September, covering assisted care, research mining, and training, with planned deployment at Longhua Hospital. [[Link](https://www.chinanews.com.cn/jk/2026/09-19/10699553.shtml)]
- [2026.08] The university site says the Qian Xiaoxing medical model was released on 27 August 2026, trained on TCM literature, expert experience, and clinical data for diagnosis support, constitution identification, wellness advice, and medication guidance. [[Link](https://www.gzy.edu.cn/info/1501/12735.htm)]
- [2026.08] Southern Finance reports that Guangzhou University of Chinese Medicine continued-trains a general model on about 2 billion TCM tokens into the Xinglin teaching model, now piloted in three core courses. [[Link](https://m.21jingji.com/article/20260824/herald/ef692f3ceba10c36edd3952f4d5ca892.html)]
- [2026.07] Guizhou Medical University and partners launch **HuaZu BenCao**, a national ethnic-medicine AI platform built on ShuZhi QiHuang + Qwen integrating multi-ethnic materia medica classics. [[Link](https://www.gmc.edu.cn/info/1058/30267.htm)]
- [2026.07] Xinhua reports that in July 2026 the national medical AI pilot base released five results in Henan, including a meridian-diagnosis model, an esophageal-cancer model, a TCM dataset, a Chinese-medicine R&D model, and a famous-doctor agent. [[Link](http://www.ha.xinhuanet.com/20260928/c8569fe1fbdb4ebc81053d86c6d93682/c.html)]
- [2026.07] Insightful Eye presents **Bianshi Cloud TCM** at WAIC 2026, built on a registered Bianshi multimodal model with four-diagnosis devices and assisted-care systems. [[Link](http://www.eeo.com.cn/2026/0720/965556.shtml)]
- [2026.07] Andun Health debuts a **seven-diagnosis** TCM robot at WAIC 2026, integrating face, infrared face, tongue, ear, auscultation, inquiry, and pulse. The page cites a 235-billion-parameter TCM model and does not mention TianHui. [[Link](https://www.news.cn/finance/20260720/f6a8625c1be4412d9c311a232c7a35fa/c.html)]
- [2026.07] Shanghai Seventh People's Hospital (SHUTCM) releases the **Qiyuan** TCM LLM with pretraining, domain fine-tuning, and expert RL; supports generative medical records and master-physician Agent digital twins; showcased at WAIC. [[Link](https://dwgk.shutcm.edu.cn/2026/0725/c1890a175544/page.htm)]
- [2026.06] Zhongke Wenge passes HKEX listing hearing; reports note the **DaYi JinKui** TCM LLM (with CACMS) has obtained top-tier CAICT Trusted AI certification. [[Link](https://www.ncsti.gov.cn/kjdt/xwjj/202606/t20260610_249369.html)]
- [2026.05] Beijing University of Chinese Medicine says XinHuo ZhongGuoYao appeared at the 2026 World Digital Education Conference and its Q&A edition is on the national smart-education platform. [[Link](https://zhongyao.bucm.edu.cn/yyxw/fb4b320d30c34e358de28a637c9f6f2c.htm)]
- [2026.04] Affiliated Hospital of Shandong University of TCM launches the provincial AI+ TCM scenario project **ZhiHui QiHuang**. [[Link](http://ccpd.china.com.cn/2026-04/17/content_43401621.html)]
- [2026.04] Beijing University of Chinese Medicine's **XinHuo ZhongGuoYao** TCM education LLM completes national generative-AI service filing—the first publicly approved TCM-domain model of its kind. [[Link](https://regional.chinadaily.com.cn/education/cn/2026-04/22/c_1177692.htm)]
- [2026.03] China News of Traditional Chinese Medicine reported that on 17 March 2026 Li Haiyan said the Yiyuan TCM model is being tried for case structuring, intelligent inquiry, prescription recommendation, and rational use of Chinese patent medicines. [[Link](https://www.cntcm.com.cn/content/202603/20/c501417.html)]
- [2026.03] Shanghai University of TCM says its formula-syndrome multimodal model was selected as a stage result of a national AI application pilot base. [[Link](https://kjrw.shutcm.edu.cn/2026/0330/c805a172392/page.htm)]
- [2026.02] Eight ministries issue the TCM Industry High-Quality Development Plan (2026–2030), calling for AI and knowledge graphs to empower classical formulas and master physicians' prescriptions. [[Link](https://www.gov.cn/zhengce/zhengceku/202602/content_7057174.htm)]
- [2026.01] Xinhua reports that on 24 December 2025 Henan's health commission showed a meridian-assisted diagnosis model and the Yuyao multimodal Shennong materia medica model for herb identification, authentication, assay, and origin tracing. [[Link](http://www.ha.xinhuanet.com/20260105/b91d84bacd1c46389a007e0cc201962d/c.html)]
- [2026.01] Science and Technology Daily reports that on 9 January Guangdong Provincial Hospital of Chinese Medicine launched a matrix of famous-doctor decision models; dermatology and cardiovascular models are already in clinical use. [[Link](https://www.stdaily.com/web/gdxw/2026-01/12/content_460323.html)]
- [2026.01] Chengdu University of TCM said Wen Chuanbiao's team project, a high-quality TCM AI-model dataset numbered 2025-AISJK-02013, was selected for the 2025 MIIT and NMPA AI medical-device challenge list. [[Link](https://www.cdutcm.edu.cn/info/1074/138321.htm)]
- [2026.01] TCM Congbao says its Suwen content-generation algorithm was included in the 14th CAC deep-synthesis filing batch. [[Link](https://www.tcmbrain.com/?list_43/180.html)]

</details>

<details>
<summary>2025 · 28</summary>

- [2025.12] **ZMT-M1** scores 96.26 on a simulated national TCM practitioner exam and is piloted in 100+ clinics. [[Link](https://m.tech.china.com/redian/2025/1229/122025_1789291.html)]
- [2025.12] Guang'anmen Hospital reports that Guangyi Qizhi completed national deep-synthesis algorithm filing and describes itself as the first TCM hospital to do so. [[Link](https://www.gamyy.cn/gzb/news/big/114632.html)]
- [2025.12] Gushengtang launches a “TCM Brain” and an AI twin of National TCM Master Shi Qi, with 14 expert twins released. The eight-specialty claim is from a different story, not this page. [[Link](https://www.jjckb.cn/20251231/693ca93b14ff4f57adc359959dc0320d/c.html)]
- [2025.12] Jilin releases **ZhongXing·Changbai Qihuang 1.0**, an AI-native multimodal TCM LLM. [[Link](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- [2025.11] USTB said that on 2 November 2025 in Zhengzhou it jointly released the Qihuang Acupuncture model, which turns four-diagnostic readings into acupuncture prescriptions. [[Link](https://news.ustb.edu.cn/info/1087/72015.htm)]
- [2025.11] Five national health ministries issue AI+ healthcare guidelines that explicitly support building TCM diagnostic LLMs. [[Link](https://www.gov.cn/zhengce/zhengceku/202511/content_7047018.htm)]
- [2025.10] China Economic Net reports the 26 October release of Idiom-Hypertension, an integrated Chinese-Western model for hypertension care. [[Link](https://www.ce.cn/cysc/yy/hydt/202510/t20251027_2541616.shtml)]
- [2025.10] Science and Technology Daily reports the CTA clinical-research agent, fine-tuned from Qwen2.5-14B for trial protocols, data management, and statistics. [[Link](https://www.stdaily.com/web/gdxw/2025-10/21/content_418966.html)]
- [2025.09] Guang'anmen Hospital said that on 12 September 2025, at the CIFTIS forum, it released Guangyi Qizhi 2.0 and the AI doctor An'an, already shown on outpatient guidance and pre-consultation screens. [[Link](https://www.gamyy.cn/gzb/news/big/113898.html)]
- [2025.09] **ZhiFu Qihuang Tiangong** TCM AI model completes national deep-synthesis algorithm filing for four-diagnosis devices and constitution assessment. [[Link](http://zs.scbzol.com/zs/2025/0919/328624.html)]
- [2025.09] The evaluated model on this page is **Chuanshen Suwen**, which passed CAICT Trusted AI TCM LLM Level 4+. The text says Transn built it on the Rendu base model. [[Link](https://zhongyi.gmw.cn/2025-09/10/content_38277329.htm)]
- [2025.09] **YiYin** classical TCM LLM goes live in Song County, Henan, combining TCM education with AI-assisted care for county clinics. [[Link](http://www.ha.xinhuanet.com/20250918/a3da94037689422dbcd1fe57fa62ef94/c.html)]
- [2025.09] The China Academy of Chinese Medical Sciences said that at CIFTIS on 10-14 September 2025 its intelligent-science center showed the Dayi Jinkui LLM and multi-turn inquiry system, plus tongue-diagnosis and mobile TCM testing units. [[Link](https://www.cacms.ac.cn/news_dynamic/detail/5080.html)]
- [2025.08] NSCC-TJ and Tianjin University of TCM release **TianHe·LingShu** 2.0 (expanded beyond acupuncture to 20+ specialties) and launch a TCM intelligent-model evaluation system. [[Link](http://tj.people.com.cn/n2/2025/0809/c375366-41317410.html)]
- [2025.08] **Gushengtang** releases ten “National Master AI twins” trained on master clinicians' experience. The page reports expert-simulation consistency above 86%, not pattern-differentiation accuracy. [[Link](http://sz.people.com.cn/n2/2025/0801/c202846-41310443.html)]
- [2025.08] Hubei Daily reported that on 6 August 2025 Hubei University of Chinese Medicine, Hubei Shizhen Laboratory, and Transn signed a cooperation agreement centered on the Chuanshen Suwen TCM model. [[Link](https://news.hubeidaily.net/mobile/c_4393128.html)]
- [2025.07] Guang'anmen Hospital forms the **GuangYi·QiZhi** LLM agent alliance with medical consortium partners for cross-institution intelligent care. [[Link](https://www.gamyy.cn/gzb/news/big/112751.html)]
- [2025.06] Nanjing University of Chinese Medicine said that on 6 June 2025 it released Lingshan TCM Model (Xiao Xingren) and Sushan Chinese Materia Medica Model (Sushan Zhisiti) for clinical, teaching, and research use. [[Link](https://xxjs.njucm.edu.cn/2025/0529/c445a156198/pagem.htm)]
- [2025.06] The National Data Administration listed a Chengdu University of TCM case that uses a large model to segment and tag 996 classical books and ChatGLM-6B to link TCM terms into graphs such as point-organ relations. [[Link](https://www.nda.gov.cn/sjj/ywpd/szkjyjcss/0618/20250618095629525611799_pc.html)]
- [2025.06] **TCM Hengqin** vertical LLM is officially released. [[Link](https://www.stdaily.com/web/gdxw/2025-06/20/content_357526.html)]
- [2025.05] Beijing University of Chinese Medicine said that on 10 May 2025 it released Xinhuo Zhongguoyao Zhisiti 1.0, a education model of more than 70 billion parameters built on iFlytek Spark and DeepSeek. [[Link](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)]
- [2025.05] China Academy of Chinese Medical Sciences releases evaluation standards for TCM large models. [[Link](https://www.news.cn/politics/20250510/5e6a0b4978b44b69b67dbfb7282fd220/c.html)]
- [2025.04] Transn releases **RenDu·SuWen** TCM LLM (mixture-of-entropy architecture) for inquiry, pattern differentiation, and formula recommendation. [[Link](https://www.transn.com/about_us/consult/article/1924766101036437505)]
- [2025.04] Ifeng reported that on 11 April 2025, at the Huawei Cloud ecosystem conference, Jiuwei Health released the Jiuwei Shennong TCM agent on the Pangu model for drug R&D, formula optimization, and clinical support. [[Link](https://biz.ifeng.com/c/8iTNRXVw44k)]
- [2025.03] Guang'anmen Hospital releases **GuangYi·QiZhi**, described as the first TCM hospital with integrated local compute + model + application deployment. [[Link](https://www.xinhuanet.com/tech/20250328/8b1685ad8c6f48c9bdc2add1658edac3/c.html)]
- [2025.03] Hefei Yunzhen said it released the Yunzhen Huayi TCM model on its TongueLMM tongue model and DeepSeek-R1 for syndrome differentiation, constitution assessment, and report generation. [[Link](https://www.ai-tongue.com/pages/news/2025/04/9a6f1920-4819-406e-8d1f-6ba0b838a7f8.html)]
- [2025.03] Xinhua reported that on 13 March 2025 Huang Huang's team at Nanjing University of Chinese Medicine and Hangzhou Maijing Health released an AI system that combines an LLM and a knowledge graph to operationalize formula-person matching. [[Link](http://www.js.xinhuanet.com/20250314/aa816bb98d1041afa0fa7bca45583d1b/c.html)]
- [2025.01] On 8 January 2025, the University of Science and Technology Beijing and Henan University of Chinese Medicine released Zhang Zhongjing TCM Large Model 1.0 for syndrome differentiation, syndrome-element recommendation, classical formulas, and formula analysis. [[Link](https://news.ustb.edu.cn/info/1087/67760.htm)]

</details>

<details>
<summary>2024 · 4</summary>

- [2024.12] China UnionPay Consumer Finance with Sun Yat-sen University and GZUCMS Shenzhen Hospital release vertical TCM LLM **ZhongSi** for community clinic inquiry. [[Link](https://finance.sina.com.cn/jjxw/2024-12-16/doc-inczrzsp5791684.shtml)]
- [2024.09] Zhongke Wenge releases **DaYi JinKui** TCM LLM and a health platform trained on 1,500+ TCM classics and a large set of clinical cases. [[Link](https://36kr.com/newsflashes/2946967562099592)]
- [2024.05] Tasly and Huawei Cloud release **ShuZhi BenCao** on Pangu language and molecular models. This page does not mention a CAICT Level 4+ evaluation. [[Link](https://news.pharmnet.com.cn/news/2024/05/10/591622.html)]
- [2024.03] ECNU, SHUTCM, ECUST, NMMU, Lingang Lab, and CR Jiangzhong jointly develop the **ShuZhi QiHuang** TCM LLM. The linked ECNU page is a later write-up of ShuZhi QiHuang 2.0, not the original 2024.03 release announcement. [[Link](https://pharm.ecnu.edu.cn/08/27/c43775a657447/page.htm)]

</details>

<details>
<summary>2023 · 1</summary>

- [2023.07] Nanjing Dajing TCM releases **QiHuang Wendao** LLM with large knowledge graphs and clinical data for institutional beta use. [[Link](http://js.news.cn/20230729/fa034db71a00487b819a4ad95b44673e/c.html)]

</details>


</details>

## Surveys

<details>
<summary>62 surveys, grouped by year</summary>

<details>
<summary>2026 · 32</summary>

- [*兰州大学学报(医学版)*] **从大语言模型到智能体（兰州大学学报医学版综述）** Chinese-language systematic review organized around the LLM-to-agent transition for TCM clinical assisted diagnosis and treatment (J. Lanzhou Univ. Med. Sci. 2026;52(4):49-57). [[DOI](https://doi.org/10.13885/j.issn.2097-681X.T20260032)]
- **Agentic and Knowledge-Grounded LLMs in TCM（预注册）** OSF preregistration (not a completed review) of a systematic review on agentic and knowledge-grounded LLMs in TCM: evidence mapping, text mining, and translation readiness. [[Link](https://doi.org/10.17605/osf.io/kq8jx)]
- [*International Journal of Pattern Recognition and Artificial Intelligence*] **中医大模型关键技术综述（IJPRAI）** Survey of key technologies for TCM LLMs: knowledge organization, aided diagnosis, and clinical decision support (formally published in IJPRAI, World Scientific). [Guangdong Provincial Hospital of Traditional Chinese Medicine, Guangdong University Of Finances and Economics, Guangdong University of Finance] [[DOI](https://doi.org/10.1142/s0218001426590263)]
- [*Journal of Traditional Chinese Medical Sciences*] **AI驱动中医诊断智能化综述（JTCMS）** Survey on multimodal fusion and LLMs for intelligent four-diagnosis in TCM: applications, challenges and outlook (JTCMS). [[DOI](https://doi.org/10.1016/j.jtcms.2026.05.002)]
- [*上海中医药杂志*] **人工智能驱动下的中医智能诊疗研究进展与挑战** Chinese review structured on the six-step TCM diagnosis-treatment chain (four diagnoses, pattern differentiation, prescription, outcome prediction), contrasting supervised/unsupervised/RL/deep-learning paradigms (Shanghai J. TCM 2026;60(1)). [[DOI](https://doi.org/10.16305/j.1007-1334.2026.z20250609004)]
- [*Communications in Computer and Information Science (Springer)*] **多模态大模型驱动舌脉面诊智能化综述（Springer 书章）** The only review text dedicated to multimodal-LLM-driven tongue, pulse, and facial diagnosis in TCM (Springer CCIS book chapter; weaker peer review than journals). [Chinese Academy of Social Sciences, Institute of Ethnology and Anthropology, University of Chinese Academy of Social Sciences] [[DOI](https://doi.org/10.1007/978-981-95-7299-1_15)]
- [*中华中医药学刊*] **人工智能赋能中医数字化诊断：现状与挑战（中华中医药学刊）** Short Chinese review of AI-empowered digital TCM diagnosis: applications, data-quality, interpretability, and theory-integration challenges (bibliographic record only). [[DOI](https://doi.org/10.13193/j.issn.1673-7717.2026.01.004)]
- [*Integrative Medicine Research*] **Yao et al. 2026: LLM 与循证中医整合（Scoping Review）** PRISMA scoping review (12 studies, 2022-11 to 2026-01) on integrating LLMs with evidence-based Chinese medicine. [University of Geneva, Gansu University of Traditional Chinese Medicine, Lanzhou University] [[DOI](https://doi.org/10.1016/j.imr.2026.101349)]
- [*Journal of Pharmaceutical Analysis*] **Xu et al. 2026: 基于 LLM 的中医智能问答系统综述** Review of intelligent TCM question-answering systems based on LLMs (KG-QA to LLM-QA and RAG). [Tianjin haihe hospital] [[DOI](https://doi.org/10.1016/j.jpha.2025.101406)]
- [*Engineering*] **XiangShu Omics: A Framework Based on the Spatio–Temporal Field Rhythms of Human Life and Systems Intelligence Methodology** This review says it is the first to systematically construct XiangShu omics, and states that its large model integrates large language models grounded in the classical logic of principle, method, formula, and medicine, such as Shu-Zhi Qihuang. [[DOI](https://doi.org/10.1016/j.eng.2026.02.018)]
- [*Artificial Intelligence Review*] **Wu et al. 2026: AI 在中药材中的应用综述** Full-stack survey of AI in TCM herbs — compounds, targets, quality control, with an LLM section. [Northeastern University, First Hospital of China Medical University, China Medical University, Liaoning University] [[DOI](https://doi.org/10.1007/s10462-026-11513-w)]
- [*Medical Review*] **Wang et al. 2026: 重思中医大模型评测** Argues that TCM LLM evaluation still lacks a quality floor: unfiltered classics and web text can contain outdated advice, and a single case is not a benchmark. [[DOI](https://doi.org/10.1515/mr-2026-0006)]
- [*Chinese Herbal Medicines*] **Sun et al. 2026: 生成模型在中医药中的进展与应用** Reviews advances and applications of generative models in traditional Chinese medicine. [[DOI](https://doi.org/10.1016/j.chmed.2026.08.013)]
- [*Information*] **Lu et al. 2026: 深度学习中医诊断方法学质量审计** Systematic review and validation-gap analysis of deep learning for TCM disease diagnosis. [[DOI](https://doi.org/10.3390/info17060554)]
- [*ACL 2026*] **LLM-Based Multi-Agent Systems for Clinical Workflows（ACL 2026，邻近）** Adjacent ACL 2026 survey of workflow-level multi-agent clinical systems with a four-layer evaluation stack; no TCM coverage but methodologically isomorphic process-evaluation claims. [Sanford Health, University of Massachusetts Lowell, University of Massachusetts Amherst] [[DOI](https://doi.org/10.18653/v1/2026.acl-long.2123)]
- [*Chinese Medicine*] **Han et al. 2026: LLM 在中医中的调优与临床应用（Scoping Review）** PRISMA-ScR scoping review (27 studies to 2025-05) on tuning (LoRA/CPT/RAG) and clinical application of TCM LLMs. [Jining Traditional Chinese Medicine Hospital] [[DOI](https://doi.org/10.1186/s13020-026-01346-8)]
- [*Chinese Medicine*] **Guo et al. 2026: AI 与多模态数据融合推动中医现代化** Panoramic AI review (ML/DL/KG/NLP/LLM) for TCM modernization with multimodal data integration. [Ningbo College of Health Sciences, Shenzhen Second People's Hospital, Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1186/s13020-025-01194-y)]
- [*Chinese Medicine and Culture*] **From Empirical Wisdom to Computational Intelligence: A Knowledge-Data Dual-Driven Paradigm for Modernizing Traditional Chinese Medicine** The paper proposes a knowledge–data dual-driven paradigm that turns implicit traditional Chinese medicine experience into computable structure with large-scale knowledge graphs and TCM-specific large language models, and digitizes the four examinations into a multimodal TCM phenomics. [[DOI](https://doi.org/10.1097/mc9.0000000000000198)]
- [*Science of Traditional Chinese Medicine*] **Dong et al. 2026: 中医处方推荐计算方法综述** Reviews computational herbal-prescription recommendation and how it can support TCM clinical decisions. [[DOI](https://doi.org/10.1097/st9.0000000000000110)]
- [*Journal of Integrative Medicine*] **Deep learning in TCM（J Integr Med）** Single-technology review of deep learning in TCM: medical imaging, herbal material research, data mining (J. Integr. Med. 2026;24(4):471-480). [[DOI](https://doi.org/10.1016/j.joim.2026.03.001)]
- [*OSF Preprints*] **Cong H et al. TCM×LLM 综述（OSF 预印本）** OSF-preprint review of LLMs in TCM (not peer-reviewed; archival). [[DOI](https://doi.org/10.17605/osf.io/5z367)]
- [*Science of Traditional Chinese Medicine*] **Chen et al. 2026: LLM 在中医的下一步（叙述性综述）** Narrative review on the next step of LLMs in TCM — multimodality, agents, and clinical translation. [[DOI](https://doi.org/10.1097/st9.0000000000000109)]
- [*OSF Preprints*] **Cai R et al. TCM×LLM scoping review（OSF 预印本）** OSF-preprint scoping review of LLMs in TCM (not peer-reviewed; archival). [[DOI](https://doi.org/10.17605/osf.io/2hyeq)]
- [*Intelligence-Based Medicine*] **Artificial intelligence: A catalyst for the modernization of traditional Chinese medicine** This scoping review searched PubMed, Web of Science, and CNKI through 2025 and states that deep learning and large language models show promising accuracy on tongue-image analysis and syndrome differentiation, in some studies approaching expert-level performance. [[DOI](https://doi.org/10.1016/j.ibmed.2026.100415)]
- [*Journal of Advanced Research*] **AI-driven multi-scale target analysis of traditional Chinese medicine: From the pharmacological effects of single compounds to the synergistic mechanisms of formulae** This review of multi-scale traditional Chinese medicine target analysis lists the development of TCM-specific large language models among its future directions, in order to decode TCM pharmacological logic. [[DOI](https://doi.org/10.1016/j.jare.2026.03.050)]
- [*Pharmacological Research - Modern Chinese Medicine*] **AI in TCM: multimodal data to pharmacology and clinical decision（PRMCM 综述）** Broad AI-in-TCM review from multimodal data integration to pharmacological research and clinical decision support (Pharmacol. Res. Mod. Chin. Med. 2026; found in the third-round scan). [Saveetha University] [[DOI](https://doi.org/10.1016/j.prmcm.2026.100842)]
- [*Research*] **AI in TCM: Unraveling Herbal Medicine's Mechanisms（Research）** Broad AI-in-TCM review arguing AI should move beyond correlational analysis toward reconstructing the biological logic of syndrome differentiation and formula compatibility (Research 2026;9:1224). [Zhejiang Chinese Medical University] [[DOI](https://doi.org/10.34133/research.1224)]
- [*Journal of Integrative Medicine*] **AI empowers the innovation of TCM（J Integr Med 评论）** Single-author perspective on AI for TCM innovation: classics mining, diagnosis standardization, drug R&D cycles (J. Integr. Med. 2026). [[DOI](https://doi.org/10.1016/j.joim.2026.05.004)]
- [*Chinese Medicine and Culture*] **AI and Big Data in TCM Standardization and Internationalization（Chin Med Cult）** Perspective on AI and big data for TCM standardization and internationalization (Chin. Med. Cult. 2026, ahead of print). [[DOI](https://doi.org/10.1097/mc9.0000000000000203)]
- [*Science of Traditional Chinese Medicine*] **2026: 面向中医药证据知情决策的数字智能循证** Discusses digital intelligent evidence-based methods for evidence-informed decisions in Chinese medicine. [University of Geneva] [[DOI](https://doi.org/10.1097/st9.0000000000000105)]
- [*Science of Traditional Chinese Medicine*] **2026: 数字化与智能化时代的中医药机遇与挑战** Discusses opportunities and challenges for TCM as AI moves from expert systems to deep learning and large language models. [[DOI](https://doi.org/10.1097/st9.0000000000000102)]
- [*Digital Chinese Medicine*] **2026: 中医智能诊断的跨学科融合与发展趋势** Discusses interdisciplinary integration and development trends of intelligent diagnosis in TCM. [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.001)]

</details>

<details>
<summary>2025 · 20</summary>

- [*Chinese Medicine*] **古籍知识图谱×多智能体融合综述（Chin Med）** Challenges-and-prospects review of knowledge-graph construction over ancient TCM classics, first to frame multi-agent convergence in this area (Chin. Med. 2025;20:168). [[DOI](https://doi.org/10.1186/s13020-025-01226-7)]
- [*智能系统学报*] **医疗领域的大型语言模型综述（智能系统学报，邻近）** Adjacent Chinese general survey of medical LLMs (training pipeline, strategies, scenarios, challenges), a superset-context reference for TCM LLM surveys. [[DOI](https://doi.org/10.11992/tis.202405003)]
- [*智能系统学报*] **医学大语言模型的研发与应用系统综述（智能系统学报，邻近）** Adjacent systematic review of 129 medical-domain LLMs (to 2024-06) and four clinical application categories; methodologically comparable search protocol. [[DOI](https://doi.org/10.11992/tis.202410020)]
- [*中华中医药学刊*] **人工智能实现中医四诊的发展现状、问题及解决路径（中华中医药学刊）** Short Chinese review of AI-based four-diagnosis objectification: face/tongue acquisition, electronic nose, pulse sensing, and low fusion of multi-diagnosis data (bibliographic record only). [[Paper](https://www.sinomed.ac.cn/article.do?ui=2026106036)]
- [*AI Medicine*] **Zhang et al. 2025: 中医 LLM 短综述与展望** Short survey and outlook on TCM LLM models and tasks. [Northeastern University] [[DOI](https://doi.org/10.53941/aim.2025.100003)]
- [*Journal of Evidence-Based Medicine*] **Yip et al. 2025: 中西医结合 LLM 进展与挑战** Review of LLMs in integrative medicine — progress, challenges, and opportunities. [Hong Kong Baptist University, Guangdong-Hongkong-Macau Joint Laboratory of Collaborative Innovation for Environmental Quality] [[DOI](https://doi.org/10.1111/jebm.70031)]
- [*Acta Materia Medica*] **Yin et al. 2025: 数据挖掘、大模型与多模态融合的中医AI综述** Reviews AI for TCM across data mining, large language models, and multimodal fusion, aimed at multi-component herbal formulas. [[DOI](https://doi.org/10.15212/amm-2025-0045)]
- [*American Journal of Chinese Medicine*] **Wang et al. 2025: AI 驱动中医诊断模型进展** Systematic review of AI-driven TCM diagnostic models (four-diagnosis objectification, pattern differentiation). [[DOI](https://doi.org/10.1142/S0192415X25500259)]
- [*Journal of Pharmaceutical Analysis*] **The integration of machine learning into TCM（J Pharm Anal）** Review of machine-learning integration into TCM along diagnostic objectification and mechanism-elucidation lines (J. Pharm. Anal. 2025;15(8):101157). [Hangzhou Normal University] [[DOI](https://doi.org/10.1016/j.jpha.2024.101157)]
- [*American Journal of Chinese Medicine*] **Shataer et al. 2025: LLM 在中医应用（State-of-the-Art Review）** State-of-the-art review scanning TCM LLM application scenarios (care, education, translation, research). [Centre for Intelligent Healthcare, Coventry University, Coventry CV1 5RW, UK] [[DOI](https://doi.org/10.1142/S0192415X25500375)]
- [*Journal of Evidence-Based Medicine*] **Ren et al. 2025: 中医大语言模型（Scoping Review）** Arksey-O'Malley scoping review (29 studies to 2024-04) covering knowledge management, assisted care, and exam accuracy. [Institute of Health Data Science Lanzhou University Lanzhou China, Institute of Global Health University of Geneva Geneva Switzerland] [[DOI](https://doi.org/10.1111/jebm.12658)]
- [*Pharmacological Research*] **Meng et al. 2025: 大模型+虚拟细胞助力中医变革** Review of large models and virtual cells aiding modern analysis of stroke treatment with TCM formulas. [Northeastern University, Shenyang Medical College] [[DOI](https://doi.org/10.1016/j.phrs.2025.107953)]
- [*Science of Traditional Chinese Medicine*] **Liu et al. 2025: 网络药理学推动大模型用于中医药研究** Reviews how network pharmacology and large language models jointly explain multi-target mechanisms of TCM formulas. [[DOI](https://doi.org/10.1097/st9.0000000000000073)]
- [*Healthcare*] **Intelligent Question-Answering Systems in Healthcare（Healthcare，邻近）** Adjacent review (not TCM-specific): 2018-2025 healthcare QA survey with CiteSpace bibliometrics, explicitly covering TCM formula-development scenarios (Healthcare 2025). [Beijing Information Science & Technology University] [[DOI](https://doi.org/10.3390/healthcare13182269)]
- [*Journal of Evidence-Based Medicine*] **Guo et al. 2025: GPT 能否加速中医智能诊疗（综述+实证）** Survey plus empirical analysis of whether GPTs can accelerate intelligent TCM diagnosis and treatment. [Xiyuan Hospital China Academy of Chinese Medicinal Sciences Beijing China] [[DOI](https://doi.org/10.1111/jebm.70004)]
- [*Asia-pacific Journal of Convergent Research Interchange*] **Domestic and International Research Trends in Artificial Intelligence Applications in Korean Medicine: An Analysis from 2019 to 2025** The authors systematically reviewed 23 Korean-medicine artificial-intelligence studies from 2019 to 2025, ten domestic and thirteen international, and report that recent work increasingly uses large language models and other generative AI. [[DOI](https://doi.org/10.47116/apjcri.2025.11.02)]
- [*Acupuncture and Herbal Medicine*] **Chen et al. 2025: 中医大语言模型系统综述** Systematic review of 10 studies (to mid-2024) on LLMs in TCM generative tasks. [Italian National Institute of Health, Rome, Italy] [[DOI](https://doi.org/10.1097/HM9.0000000000000143)]
- [*Current Medical Science*] **Artificial Intelligence in Traditional Chinese Medicine: Multimodal Fusion and Machine Learning for Enhanced Diagnosis and Treatment Efficacy** Reviews multimodal fusion and machine learning for AI-assisted diagnosis and treatment in traditional Chinese medicine. [[DOI](https://doi.org/10.1007/s11596-025-00103-6)]
- [*MedComm – Future Medicine*] **Artificial Intelligence in Traditional Chinese Medicine: Bridging Ancient Practice and Future Innovation** This review analyzes traditional Chinese medicine large language models along construction, application, challenges, and prospects, noting that systems such as Qibo and MedChatZH already exist while earlier reviews lacked a synthesis of shared characteristics. [[DOI](https://doi.org/10.1002/mef2.70042)]
- [*Current Medical Science*] **AI for Spleen-Stomach Disorders in TCM（Curr Med Sci）** Single-disease-area (spleen-stomach) review of KG plus intelligent diagnosis/treatment with a symptom-syndrome-disease-formula framework (Curr. Med. Sci. 2025;45(6)). [Hubei University of Chinese Medicine, Hubei Provincial Hospital of Traditional Chinese Medicine, Hospital Conde S. Januário, Union Hospital] [[DOI](https://doi.org/10.1007/s11596-025-00128-x)]

</details>

<details>
<summary>2024 · 5</summary>

- [*计算机工程与应用*] **Su et al. 2024 — Review of AI in TCM diagnosis and treatment (Chinese)** Chinese-language review of three AI stages in TCM care — expert systems, ML, and deep learning — with challenges. [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2312-0400)]
- [*南京中医药大学学报*] **Li et al. 2024 — Research progress and prospects of LLMs in TCM (Chinese)** Chinese-language review of TCM LLM pipelines, frontier techniques (prompting/RAG/RLHF), and application prospects. [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1393)]
- [*Computers in Biology and Medicine*] **Tian et al. 2024: 四诊机器学习综述** Review of machine learning for TCM four diagnoses — inspection, auscultation-olfaction, inquiry, and palpation. [Northeastern University, Ningbo University] [[DOI](https://doi.org/10.1016/j.compbiomed.2024.108074)]
- [*中国工程科学*] **Song et al. 2024: AI 辅助中医辨证关键问题与技术挑战** Strategic-study review of key issues in AI-assisted TCM syndrome differentiation — multimodal fusion, symptom association, pattern quantification and reasoning, and TCM LLMs. [Shanghai University of Engineering Science, Digital China Health (China), Zhejiang Lab] [[DOI](https://doi.org/10.15302/J-SSCAE-2024.02.010)]
- [*Computer Materials & Continua*] **Qu et al. 2024: 中医知识图谱综述** Review of knowledge graphs in TCM — analysis, construction, applications, and prospects. [Beijing Forestry University] [[DOI](https://doi.org/10.32604/cmc.2024.055671)]

</details>

<details>
<summary>2021 · 1</summary>

- [*Computers in Biology and Medicine*] **Zhang et al. 2021: 计算中医诊断文献综述** Literature survey of computational TCM diagnosis — symptom acquisition, pattern modeling, and systems. [[DOI](https://doi.org/10.1016/j.compbiomed.2021.104358)]

</details>

<details>
<summary>2020 · 1</summary>

- [*Artificial Intelligence in Medicine*] **Chu et al. 2020: 中医定量知识表示模型综述** Review of quantitative knowledge representation models of TCM (ontologies, rules, statistics). [Xidian University, Xi'an Polytechnic University, Guangdong Polytechnic Normal University, CM Hospital] [[DOI](https://doi.org/10.1016/j.artmed.2020.101810)]

</details>

<details>
<summary>2015 · 1</summary>

- [*Evidence-Based Complementary and Alternative Medicine*] **Zhao et al. 2015: 中医患者分类进展（ML 视角）** Review of ML-driven advances in patient classification for TCM. [[DOI](https://doi.org/10.1155/2015/376716)]

</details>

<details>
<summary>2013 · 1</summary>

- [*Briefings in Bioinformatics*] **Gu & Chen 2013: 生物信息学遇见中医** Historical review of bioinformatics meeting TCM (omics and text mining). [[DOI](https://doi.org/10.1093/bib/bbt063)]

</details>

<details>
<summary>2007 · 1</summary>

- [*Computer Methods and Programs in Biomedicine*] **Lukman et al. 2007: 中医计算方法综述** Foundational survey of computational methods for TCM (expert systems, ML, data mining). [University of Cambridge, University of Reading] [[DOI](https://doi.org/10.1016/j.cmpb.2007.09.008)]

</details>


</details>

## Patents

TCM LLM, knowledge-graph, RAG, inquiry, and prescription-recommendation system patents worldwide—not a dump of herbal-formula patents.

<details>
<summary>69 patents, grouped by publication year</summary>

<details>
<summary>2026 · 29</summary>

- [*CN122531762A*] **基于生成式模拟医案构建的定制化中医处方推荐大模型** A rule engine enumerates structured TCM features, an LLM turns them into simulated cases, and those cases fine-tune a customized prescription model (published, not granted). [[Patent](https://patents.google.com/patent/CN122531762A/zh)]
- [*CN122529089A*] **TCM dialogue generation with a large language model and long-term memory** Generates personalized TCM dialogue from a long-term memory bank and user portrait (published, not granted). [Hangzhou Wangchai Technology] [[Patent](https://patents.google.com/patent/CN122529089A/zh)]
- [*CN122508432A*] **一种面向中医药知识图谱的综合质量评估方法** Sends a small sample to a TCM-tuned large model for a preliminary quality check of a TCM knowledge graph (published, not granted). [[Patent](https://patents.google.com/patent/CN122508432A/zh)]
- [*CN122436154A*] **Digital inheritance and analysis of Zhang Xichun's theory, method, formula, and herbs** Rule engine plus three-way retrieval and an LLM for Zhang Xichun school analysis (published, not granted). [Guangzhou Zhiyun Caotang Medical Technology] [[Patent](https://eureka.patsnap.com/patent/CN122436154A)]
- [*CN122436116A*] **基于知识图谱与大语言模型的脾胃学派理法方药分析系统** Combines a spleen-stomach school knowledge graph, vector retrieval, and an LLM for formula selection, safety checks, and prescription writing (published, not granted). [[Patent](https://patents.google.com/patent/CN122436116A/zh)]
- [*CN122436251A*] **一种融合时空特征的针灸推理模型构建方法、系统及设备** Aligns four-examination and course features, retrieves past acupuncture plans, and uses a fine-tuned LLM with chain-of-thought for an explainable plan (published, not granted). [[Patent](https://patents.google.com/patent/CN122436251A/zh)]
- [*CN122364665A*] **一种基于大语言模型的中医古籍症状标准化处理方法** An LLM finds candidate symptom spans in sliced classical TCM texts and maps them into a standard symptom semantic field (published, not granted). [[Patent](https://patents.google.com/patent/CN122364665A/zh)]
- [*CN122135923A*] **辅助诊断结果和参考处方生成方法、装置、介质及计算机设备** Recalls similar records and treatment rationales on four paths, then a large model drafts TCM diagnosis, syndrome pattern, and a reference prescription (published, not granted). [[Patent](https://eureka.patsnap.com/patent/CN122135923A)]
- [*CN122245713A*] **基于大语言模型的中医智能问诊方法及系统** Intent is parsed from multimodal inquiry data, then dual-path retrieval over TCM knowledge produces the consultation result (published, not granted). [[Patent](https://patents.google.com/patent/CN122245713A/zh)]
- [*CN120913881B*] **基于多模态中医大语言模型的数据分析方法、系统、终端及介质** Trains a multimodal TCM large model on tongue images, speech, and inquiry text, then outputs a preliminary TCM analysis (granted June 2026). [[Patent](https://eureka.patsnap.com/patent/CN120913881B)]
- [*CN122135936A*] **一种面向中医方剂推荐的知识图谱大模型问答方法及系统** Encodes a case with a Chinese instruction LLM, fuses it with a dynamic TCM knowledge graph, and returns formula recommendations as answers (published, not granted). [[Patent](https://patents.google.com/patent/CN122135936A/zh)]
- [*CN122025029A*] **Causal contrastive learning and LLM graph attention for TCM prescription recommendation** Heterogeneous and homogeneous symptom-herb graphs plus an LLM-enhanced causal mechanism (published, not granted). [Huzhou University] [[Patent](https://eureka.patsnap.com/patent/CN122025029A)]
- [*CN122050861A*] **TCM diagnosis-and-treatment platform combining an LLM with dual-channel retrieval** LLM plus TCM knowledge-graph dual-channel retrieval for inheriting master-physician experience and generating formulas (published, not granted). [Yueyang Hospital of Integrated Traditional Chinese and Western Medicine, SHUTCM] [[Patent](https://patents.google.com/patent/CN122050861A/zh)]
- [*CN120913769B*] **基于多模态大模型的中医舌诊药饮推荐方法** A multimodal model turns a tongue image into a condition description and a medicinal-drink recommendation (granted May 2026). [[Patent](https://patents.google.com/patent/CN120913769B/zh)]
- [*CN122117314A*] **LLM-based intelligent acupuncture diagnosis agent** Acupuncture knowledge bases, graph, vector search and reranking, with an LLM agent that classifies questions and asks follow-ups (published, not granted). [Henan University of Technology] [[Patent](https://eureka.patsnap.com/patent/CN122117314A)]
- [*CN122091073A*] **Multi-task joint optimization for TCM prescription generation** A pretrained LLM predicts herb sequences and herb sets jointly, with extra weight on rare herbs (published, not granted). [Hangzhou Dianzi University] [[Patent](https://eureka.patsnap.com/patent/CN122091073A)]
- [*CN122050683A*] **一种基于图注意力网络与大语言模型的中药处方生成方法** Herbal prescription generation is cast as multi-label classification, with graph attention and an LLM modeling drug synergy and contraindications (published, not granted). [[Patent](https://patents.google.com/patent/CN122050683A/zh)]
- [*CN121862376A*] **Knowledge-graph and LLM system for TCM syndrome-differentiation QA** Chunks classics and cases, extracts a graph, then retrieves local and global keywords for syndrome-differentiation answers (published, not granted). [Nanjing University of Posts and Telecommunications] [[Patent](https://patents.google.com/patent/CN121862376A/zh)]
- [*CN121687367A*] **Structured evidence-subgraph RAG for TCM herb recommendation** Multi-hop evidence subgraphs plus Hopfield associative retrieval for herb recommendation, with graph constraints against hallucination (published, not granted). [Zhejiang Chinese Medical University] [[Patent](https://patents.google.com/patent/CN121687367A/zh)]
- [*CN121743505A*] **Knowledge-enhanced generation of TCM case commentaries** Retrieves knowledge-graph subgraphs, then writes case notes along etiology, treatment principles, formulas, and prognosis (published, not granted). [Zhejiang University] [[Patent](https://patents.google.com/patent/CN121743505A/zh)]
- [*CN121709160A*] **一种基于视觉语言模型的中医舌诊智能分析方法** Fine-tunes Qwen-VL with tongue-diagnosis prompts so a tongue image yields structured color and coating labels plus a natural-language reading (published, not granted). [[Patent](https://patents.google.com/patent/CN121709160A/zh)]
- [*CN121480736A*] **Knowledge-distillation and RL for oncology TCM prescription recommendation** Distills GPT-4o into a Qwen student, then DPO, for interpretable oncology TCM prescriptions (published, not granted). [Nanjing University of Chinese Medicine] [[Patent](https://patents.google.com/patent/CN121480736A/zh)]
- [*CN121524286A*] **一种心血管疾病的基于针灸诊疗知识图谱的智能问答系统** Builds a cardiovascular acupuncture knowledge graph and sends hits to a cloud LLM for wording; if retrieval fails, the LLM answers with a caution (published, not granted). [[Patent](https://patents.google.com/patent/CN121524286A/zh)]
- [*CN121562809A*] **一种基于动态语义分块、知识图谱与多跳路径规划的中医大语言模型AI题库智能生成方法及系统** Chunks TCM text, plans multi-hop paths on a knowledge graph, and trains a large model to generate a TCM question bank (published, not granted). [[Patent](https://patents.google.com/patent/CN121562809A/zh)]
- [*CN121460056A*] **一种基于人工智能的方剂配制方法、系统、介质和设备** An LLM maps case entities to disease and syndrome, drafts a formula, scores it, and regenerates from structured advice until the score passes (published, not granted). [[Patent](https://patents.google.com/patent/CN121460056A/zh)]
- [*CN121460113A*] **一种基于中医语言大模型的中医智能分析方法及系统** LoRA-tunes a TCM language model that maps syndrome and chief complaint to a formula (published, not granted). [[Patent](https://patents.google.com/patent/CN121460113A/zh)]
- [*CN121393746A*] **基于大语言模型的经络辨证与针灸方案生成方法及系统** Multi-source clinical data are quantified and cleaned, then a meridian-syndrome knowledge base and an LLM generate acupuncture plans (published, not granted). [[Patent](https://patents.google.com/patent/CN121393746A/zh)]
- [*CN121331451A*] **一种融合舌象、心率及文本的多模态健康状态评估方法** Takes tongue image as the main signal, adds heart rate and self-reported text, and prompts DeepSeek to write a health-status assessment (published, not granted). [[Patent](https://patents.google.com/patent/CN121331451A/zh)]
- [*CN121436134A*] **Multimodal knowledge-graph construction from TCM texts and records** An LLM extracts triples from TCM texts, then fuses a real-world case layer into a multimodal graph (published, not granted). [Hangzhou Ganzhicao Technology] [[Patent](https://patents.google.com/patent/CN121436134A/zh)]

</details>

<details>
<summary>2025 · 25</summary>

- [*CN121210613A*] **基于检索增强生成的针灸大模型构建方法、系统及装置** An acupuncture LLM answers questions from vector-retrieved knowledge snippets and, for diagnosis requests, retrieves treatment entries from an acupuncture-plan library (published, not granted). [[Patent](https://patents.google.com/patent/CN121210613A/zh)]
- [*CN120690391B*] **Knowledge-graph recommendation of classic TCM formulas** Maps colloquial symptoms to terms, filters by constitution, and recommends classic formulas (granted). [Shunfu Technology Group] [[Patent](https://patents.google.com/patent/CN120690391B/zh)]
- [*CN121212280A*] **一种基于大语言模型的人-信息-物理三元数据融合中药制造知识图谱构建系统、电子设备及存储介质** An LLM extracts triples from manufacturing text under TCM term and relation constraints, then a human-cyber-physical ontology assembles a manufacturing knowledge graph (published, not granted). [[Patent](https://patents.google.com/patent/CN121212280A/zh)]
- [*CN121096596A*] **一种基于多模态大语言模型的中医临床辅助决策系统和方法** Tongue-image features are fused with clinical text, similar cases are retrieved, and a multimodal LLM drafts syndrome, diagnosis, herbal prescription, and reasoning (published, not granted). [[Patent](https://patents.google.com/patent/CN121096596A/zh)]
- [*CN121034544A*] **融合动态知识图谱的针灸大模型辨证方法及调理优化系统** A dynamically updated acupuncture knowledge graph is combined with time-series clinical features, graph attention, and reinforcement learning to differentiate syndromes and draft acupuncture plans (published, not granted). [[Patent](https://patents.google.com/patent/CN121034544A/zh)]
- [*CN120998428A*] **大小模型协同中药方剂优化方法、系统、终端及存储介质** A formula-optimization LLM proposes a macro revision, a smaller pharmacologic model traces constituent herbs, and the two are merged into a final formula (published, not granted). [[Patent](https://patents.google.com/patent/CN120998428A/zh)]
- [*CN120809097A*] **基于大语言模型的中医五音疗疾个性化音乐生成系统及其构建方法** An LLM first performs TCM syndrome differentiation, then generates personalized five-tone therapy music under tonal constraints (published, not granted). [[Patent](https://patents.google.com/patent/CN120809097A/zh)]
- [*CN119941636B*] **中医药多模态LLM训练方法及其应用** Extracts tongue-coating and pulse features, fuses them with text by cross-modal attention, and trains a multimodal TCM large language model (granted). [[Patent](https://patents.google.com/patent/CN119941636B/zh)]
- [*CN120674039A*] **针灸穴位推荐方法及其模型获取方法、装置、设备及介质** Trains a language model on medical records so symptoms map to acupuncture points, then applies parameter tuning and policy optimization (published, not granted). [[Patent](https://patents.google.com/patent/CN120674039A/zh)]
- [*CN120337029A*] **一种基于大模型的中药分类方法** Entities from multi-source herbal data are mapped to modern pharmacological indicators, then a pretrained large model is adaptively fine-tuned to classify herbs (published, not granted). [[Patent](https://patents.google.com/patent/CN120337029A/zh)]
- [*CN120299726A*] **一种基于大模型智能体协作规划的中医诊断场景模拟方法** Turns unstructured case records into structured knowledge, then large-model agents collaborate to simulate a TCM diagnostic encounter (published, not granted). [[Patent](https://eureka.patsnap.com/patent/CN120299726A)]
- [*CN120108651A*] **基于胸肺科中医问诊报告大语言模型的中医方剂推荐方法和系统** Shared knowledge domains fine-tune a chest-and-lung TCM inquiry LLM that outputs constitution and symptom parameters and recommends food-medicine formulas (published, not granted). [[Patent](https://patents.google.com/patent/CN120108651A/zh)]
- [*CN120108694A*] **Knowledge-graph and case-enhanced RAG for intelligent TCM inquiry** Leiden subgraph search plus hybrid global/local recall, then a single LLM response (published, not granted). [Jiangsu University] [[Patent](https://patents.google.com/patent/CN120108694A/zh)]
- [*CN120216657A*] **基于大语言模型的中药药物警戒问答系统的构建方法** A Chinese-materia-medica knowledge base trains the pharmacovigilance RAG model PV-RAG to answer natural-language safety questions (published, not granted). [[Patent](https://patents.google.com/patent/CN120216657A/zh)]
- [*CN120221058A*] **Multimodal knowledge-graph and LLM system for TCM rehabilitation diagnosis** Aligns tongue, pulse, and inquiry features with knowledge-graph embeddings before a rehabilitation expert LLM (published, not granted). [Zhejiang Chinese Medical University] [[Patent](https://patents.google.com/patent/CN120221058A/zh)]
- [*CN120067279B*] **AI-LLM method and system for intelligent TCM inquiry** Multimodal inquiry fusing face/body/tongue images, speech prosody, and a disease library (granted). [Yi Mai Artificial Intelligence Medical Technology (Tianjin)] [[Patent](https://patents.google.com/patent/CN120067279B/zh)]
- [*CN120148827A*] **一种基于大模型的心血管疾病医疗决策支持方法** A pretrained large model fuses TCM syndrome knowledge with a Western pathology graph to propose cardiovascular decisions that include Chinese herbal formulas (published, not granted). [[Patent](https://eureka.patsnap.com/patent/CN120148827A)]
- [*CN119811630B*] **应用大语言模型的泌尿科中医问诊结果预测方法和系统** An LLM predicts core lesion keywords from urological TCM inquiry text and adjusts its parameters from recorded feedback (granted 6 March 2026; application published 11 April 2025). [[Patent](https://patents.google.com/patent/CN119811630B/zh)]
- [*CN119905208A*] **基于多源特征融合的中医方剂智能推荐方法、介质和设备** Blends content-based recommendation, collaborative filtering, and an LLM reading of symptom text to rank personalized formulas (published, not granted). [[Patent](https://patents.google.com/patent/CN119905208A/zh)]
- [*CN119252469B*] **一种用于智能中医系统的大语言模型的构建方法** Labeled tongue images and historical records train a tongue-inquiry model used to construct an LLM for an intelligent TCM system (granted). [[Patent](https://patents.google.com/patent/CN119252469B/zh)]
- [*CN119763764A*] **LLM-based Chinese-medicine prescription recommendation with soft prompts** Soft prompts and cross-attention feed patient text into an LLM for controllable herb recommendations (published, not granted). [Hangzhou Ganzhicao Technology] [[Patent](https://patents.google.com/patent/CN119763764A/zh)]
- [*CN119811698B*] **一种基于OCR识别和大模型的中药方数据解析方法及装置** Handwritten herbal prescriptions are OCR'd into prompts on incompatibility, dosage, and administration, which a large model scores into an overall judgment (granted 20 June 2025; application published 11 April 2025). [[Patent](https://patents.google.com/patent/CN119811698B/zh)]
- [*CN119416782A*] **LLM method for learning famous-physician TCM formulas** Aligns classical-Chinese case terms with vernacular text using models such as Qwen (published, not granted). [Chengdu Byte Stream Technology] [[Patent](https://patents.google.com/patent/CN119416782A/zh)]
- [*CN119517372A*] **一种基于大语言模型的中医问答系统及方法** A dataset built from TCM literature trains an LLM that takes a user's medical question and returns a dialogue answer (published, not granted). [[Patent](https://patents.google.com/patent/CN119517372A/zh)]
- [*CN119446558A*] **一种基于大语言模型的中医知识图谱生成方法及系统** A model trained on herbal and consultation data visualizes treatment options for a patient and is updated from outcome ratings (published, not granted). [[Patent](https://patents.google.com/patent/CN119446558A/zh)]

</details>

<details>
<summary>2024 · 15</summary>

- [*CN119149754A*] **LLM and knowledge-graph method for TCM formula compatibility** Pairs a TCM LLM with a knowledge graph for formula compatibility (published, not granted). [Tianjin University, Tianda Zhitu (Tianjin) Technology] [[Patent](https://patents.google.com/patent/CN119149754A/zh)]
- [*CN119069137A*] **利用AI大模型进行舌象分析的方法及装置** Uses a large model to read tongue images by constitution, symptoms, and an overall interpretation (published, not granted). [[Patent](https://patents.google.com/patent/CN119069137A/zh)]
- [*CN119092157B*] **LLM-based Chinese-materia-medica question answering** Chinese-materia-medica QA fine-tuned from Baichuan2-7B-Chat (granted February 2025). [Zhejiang University, Yangtze River Delta Wisdom Oasis Innovation Center] [[Patent](https://patents.google.com/patent/CN119092157B/zh)]
- [*CN119049664A*] **基于AI大模型的中医元气充盈智能健康管理系统** Converts wearable signals into TCM terms and passes them to a TCM large model (published; deemed withdrawn on 6 February 2026). [[Patent](https://patents.google.com/patent/CN119049664A/zh)]
- [*CN119049665A*] **基于AI大模型智能人体域网的中医六经辨证智能对话健康管理系统** A six-meridian TCM dialogue system over a body-area network and a large model (published; deemed withdrawn on 6 February 2026). [[Patent](https://patents.google.com/patent/CN119049665A/zh)]
- [*CN118899077A*] **一种基于多模态大模型的中医舌诊分析系统及方法** Tongue- and face-image instructions fine-tune a general LLM such as LLaMA into TongueLMM for tongue interpretation, multi-turn QA, and constitution reasoning (published, not granted). [[Patent](https://patents.google.com/patent/CN118899077A/zh)]
- [*CN118838996A*] **Building a TCM QA system from a large language model and a knowledge graph** Closed loop of LLM generation and knowledge-graph completion for TCM QA (published, not granted). [Beijing Institute of Technology, BIT Tangshan Research Institute] [[Patent](https://patents.google.com/patent/CN118838996A/zh)]
- [*CN117786590B*] **以大语言模型为先验的智能中医系统** An LLM rewrites patient diagnostic text, which is then semantically interpreted to predict TCM syndromes and causes and to suggest treatment (granted). [[Patent](https://patents.google.com/patent/CN117786590B/zh)]
- [*CN118430833A*] **一种基于大语言模型的中医知识深度挖掘方法** Retrieval augmentation and model fine-tuning are trained together so the system can explain TCM terms and syndromes and suggest treatment from a patient query (published, not granted). [[Patent](https://patents.google.com/patent/CN118430833A/zh)]
- [*CN117828050B*] **Long-document retrieval-augmented generation for TCM question answering** Long-document RAG (expansion, recall, reranking, source citations) for TCM QA (granted July 2024). [Beijing Zhipu Huazhang Technology] [[Patent](https://patents.google.com/patent/CN117828050B/zh)]
- [*CN118280556A*] **一种基于计算视觉与大语言模型辅助中医诊疗的系统** An LLM handles spoken inquiry while computer vision converts patient images into findings that are retrieved and fed back to the LLM for TCM decision support (published, not granted). [[Patent](https://patents.google.com/patent/CN118280556A/zh)]
- [*CN118230893A*] **AI-large-model system for intelligent TCM prescription recommendation** Trains an AI large model on medical records to recommend personalized TCM prescriptions, wired into a hospital IS (published, not granted). [Hangzhou Ganzhicao Technology] [[Patent](https://patents.google.com/patent/CN118230893A/zh)]
- [*CN118098506A*] **一种基于大语言模型的针灸辅助诊疗和模型评价的方法** ChatGLM3-6B is fine-tuned on labeled symptoms, points, and operations to propose acupuncture plans, which are scored by sentence similarity (published, not granted). [[Patent](https://patents.google.com/patent/CN118098506A/zh)]
- [*CN118070907A*] **一种基于大语言模型的中医客服回复系统** Synonym-augmented TCM text trains a Transformer LLM that is fine-tuned to parse customer requests and draft replies; the application was granted as CN118070907B on 2024-07-09. [[Patent](https://patents.google.com/patent/CN118070907A/zh)]
- [*CN117493579A*] **一种基于大语言模型的中医知识图谱构建方法** An LLM extracts named entities and relations from TCM text, merges similar entities, and builds a TCM knowledge graph (published, not granted). [[Patent](https://patents.google.com/patent/CN117493579A/zh)]

</details>


</details>

## Papers

Methods, evaluations, and systems only. Named domain LLMs live under Open models.

<details>
<summary>Agents (17): 问诊流程、多智能体</summary>

<details>
<summary>2026 · 9</summary>

- [*arXiv*] **DeepTCM1.0** DeepTCM1.0: 11-expert multi-agent system on DeepSeek V3.2 for interpreting TCM formula mechanisms (Guizhi Decoction case); now on arXiv after the Research Square preprint. [Chinese Medicine Guangdong Laboratory (Hengqin), Changzhi Medical College] [[Paper](https://arxiv.org/abs/2608.18103)] [[Preprint](https://doi.org/10.21203/rs.3.rs-9844166/v1)]
- [*arXiv*] **DeepRoot** Multi-agent pipeline that turns the Shen Nong Ben Cao Jing into a verified Neo4j graph for therapeutic reasoning; code and evaluation scripts are public. [[Paper](https://arxiv.org/abs/2606.15931)] [[Code](https://github.com/CarlisleMa/deeprootv1)]
- [*Studies in Health Technology and Informatics*] **韩医CPX场景自动生成** LLM plus retrieval-augmented generation and multimodal cues to automate traditional Korean medicine CPX scenarios; validated by 10 experts. [[DOI](https://doi.org/10.3233/shti260671)]
- [*arXiv*] **TCMScience** An autonomous TCM research agent that separates language-model proposals from execution and release authority. [[Paper](https://arxiv.org/abs/2610.24601)]
- [*Journal of Pharmaceutical Analysis*] **TCM-Agent** LLM multi-agent system for network pharmacology and herbal discovery. [[Paper](https://doi.org/10.1016/j.jpha.2026.101581)] [[Code](https://github.com/AITCM/TCM-Agent)]
- [*arXiv*] **MACAT** Multi-agent culture-aware translation framework, evaluated on culture-loaded terms from TCM classics and the Analects. [[Paper](https://arxiv.org/abs/2606.01276)]
- [*Applied Sciences*] **KM-Agent** Tool-augmented agent for Korean / East Asian traditional medicine over 4,780 herb–syndrome–acupoint metadata records, evaluated on TCMBench-style sets. MDPI/OpenAlex authors at Wonkwang University and Pusan National University et al. [Wonkwang University, Pusan National University et al.] [[Paper](https://www.mdpi.com/2076-3417/16/7/3377)] [[Code](https://github.com/wonyung-lee/km-agent)]
- [*arXiv*] **DERM-3R** Resource-constrained multimodal multi-agent framework for TCM dermatology (recognition / representation / SDT agents). [[Paper](https://arxiv.org/abs/2604.09596)]
- [*arXiv*] **CORE-Acu** Acupuncture clinical decision support with structured reasoning traces and a knowledge-graph safety veto loop. [[Paper](https://arxiv.org/abs/2603.08321)]

</details>

<details>
<summary>2025 · 7</summary>

- [*arXiv*] **Jingfang** LLM-based multi-agent TCM diagnosis/treatment system reporting large relative SDT gains under the authors' protocol. [[Paper](https://arxiv.org/abs/2502.04345)]
- [*中医杂志*] **基于雅意大模型的中医智能预问诊** Liu et al. fine-tune YAYI 2-30B and couple it to a weighted symptom graph agent. Practitioner-exam accuracy is 94.09%, and on the clinical test syndrome accuracy is 88.33% with fewer turns and less time than attending physicians. [[DOI](https://doi.org/10.13288/j.11-2166/r.2025.09.005)] [[Paper](https://link.cnki.net/doi/10.13288/j.11-2166/r.2025.09.005)]
- **RenShu-AI** FastAPI + LangGraph multi-agent TCM consultation system combining GraphRAG and DeepSeek-TCM. [[Code](https://github.com/yanlinPeng-code/RenShu-AI)]
- [*Information*] **TCM compound retrieval agent** AI agent-based system for retrieving TCM compound information. [Zhengzhou University] [[DOI](https://doi.org/10.3390/info16070543)]
- [*Journal of King Saud University Computer and Information Sciences*] **DiagX-DT** Exclusionary syndrome-differentiation reasoning with CoT and an external TCM knowledge base. [[DOI](https://doi.org/10.1007/s44443-025-00123-1)]
- [*proceedings-article*] **An Intelligent TCM Diagnosis System with Localized LLMs and Modular Multimodal Reasoning Enhanced by RAG** The locally deployed system uses four agents for inspection, listening, inquiry, and palpation, coordinated by modular component processing and multimodal retrieval-augmented generation, and a central reasoning module turns tongue images, voice, pulse, and symptoms into a diagnosis and health advice. [Hosei University, Fuzhou University, Hong Kong Polytechnic University, Beihang University] [[DOI](https://doi.org/10.1109/cyberscitech68397.2025.00061)]
- [*Neurocomputing*] **AcuGPT-Agent** An LLM agent for acupuncture-based infertility treatment. [[DOI](https://doi.org/10.1016/j.neucom.2025.131116)]

</details>

<details>
<summary>2024 · 1</summary>

- [*대한한의학회지*] **Pilot Development of a 'Clinical Performance Examination (CPX) Practicing Chatbot' Utilizing Prompt Engineering** The authors turned a National Institute of Korean Medicine standardized-patient scenario into text and used role prompting and few-shot prompting with GPT-4 to build a Korean-medicine CPX practice chatbot; internal scoring found relatively high correctness and compliance, with confidentiality and naturalness still needing improvement. [Gachon University, Pusan National University] [[DOI](https://doi.org/10.13048/jkm.24013)]

</details>


</details>

<details>
<summary>Multimodal (9): 舌、面、脉</summary>

- [*proceedings-article*] **Multimodal TCM Seven-Emotion Recognition: A Three-Modality Joint Consultation Framework Based on LLMs and Cross-Attention Fusion** The seven-emotion framework reached a macro F1 of 87.6% on 10,593 IEMOCAP samples, then used a frozen large language model to turn the neural predictions into traditional Chinese medicine syndrome-differentiation reports. [Zhejiang University of Technology] [[DOI](https://doi.org/10.1145/3829441.3829486)]
- [*Lecture Notes in Computer Science Medical Image Computing and Computer Assisted Interventi*] **MLLM-Enhanced Region-Aware Bidirectional Evidence-Based Model for Tongue Diagnosis** A multimodal large-model method for region-aware, bidirectional evidence-based tongue diagnosis. [[DOI](https://doi.org/10.1007/978-3-032-38098-2_44)]
- [*arXiv*] **LingLan多模态辨证大模型** A multimodal TCM diagnosis model over the four examinations. Not the LingLan benchmark paper (arXiv 2602.01779). [[Paper](https://arxiv.org/abs/2609.25715)]
- [*Studies in Rhythm Engineering Cognitive Neuroscience and Artificial Intelligence*] **AI Tongue Diagnosis: Expert System with LLMs for Abdominal Disease Detection Through Mobile App** A mobile tongue-diagnosis expert system that uses large language models to detect abdominal disease. [[DOI](https://doi.org/10.1007/978-3-032-19966-9_2)]
- [*IEEE BIBM 2025*] **用大模型构建中医舌诊本体** Uses a large language model to help construct a TCM tongue-diagnosis ontology. [[DOI](https://doi.org/10.1109/bibm66473.2025.11356313)]
- [*ICASSP 2025*] **Few-shot tongue-diagnosis in-context multitask learning** Few-shot in-context multitask fine-tuning of LLMs mapping tongue images directly to constitutions. [Northeastern University] [[DOI](https://doi.org/10.1109/ICASSP49660.2025.10887764)]
- [*arXiv*] **TCDiff** Triplet cascaded diffusion model generating high-fidelity multimodal TCM EHRs, with the **TCM-SZ1** benchmark dataset. [[Paper](https://arxiv.org/abs/2508.01615)]
- **Chinese-LLaVA-Med** Chinese medical multimodal LLM based on the LLaVA architecture, with the llava-med-zh-eval benchmark and open 7B weights. [[Code](https://github.com/BUAADreamer/Chinese-LLaVA-Med)]
- **XrayGLM** Chinese multimodal medical LLM for chest X-ray interpretation. [[Code](https://github.com/WangRongsheng/XrayGLM)]

</details>

<details>
<summary>RAG / knowledge graphs (56): 检索和医案、方剂图谱</summary>

<details>
<summary>2026 · 15</summary>

- [*Communications in Computer and Information Science (Springer)*] **Hybrid Retrieval + Re-ranking TCM Prescription Generation** Hybrid retrieval with re-ranking to enhance LLM-based TCM prescription generation (Springer CCIS conference paper). [Shandong University, Shandong Academy of Sciences] [[Paper](https://doi.org/10.1007/978-981-92-3563-6_21)]
- [*arXiv*] **Evidence-Based TCM Visualization Diagnosis System** Evidence-based TCM visualization diagnosis system: Neo4j knowledge graph (241 patterns, 1,263 symptoms) with four-stage symptom matching (LLM-verified) and information-gain-driven active inquiry. [[Paper](https://arxiv.org/abs/2606.06869)]
- **Pediatric influenza Chinese patent-medicine recommender (KG + LLM)** Knowledge graph of Chinese patent medicines for pediatric influenza built from authoritative guidelines and integrated with an LLM (JMIR Preprints). [[Preprint](https://doi.org/10.2196/preprints.101648)]
- [*Frontiers in Medicine*] **Jin San Zhen KG-QA** Knowledge graph + LLM QA tool for the Jin San Zhen acupuncture school. [Guangzhou University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1755583)]
- [*IEEE BigComp 2026*] **知识图谱增强的中医问答大模型** Knowledge-graph-enhanced large language models for TCM question answering. [[DOI](https://doi.org/10.1109/bigcomp68355.2026.00029)]
- [*Frontiers in Medicine*] **Tree-organized self-reflective retrieval for TCM QA** Tree-organized self-reflective retrieval for TCM question answering (Frontiers in Medicine 2026). [[DOI](https://doi.org/10.3389/fmed.2026.1752778)]
- [*Journal of King Saud University - Computer and Information Sciences*] **TCMKG: Knowledge-Grounded question answering in Traditional Chinese Medicine via dynamic prompt evolution framework** TCMKG used expert-guided prompting on the Xin'an medical-case corpus to build a traditional Chinese medicine knowledge graph of 37,192 entities and 130,030 relations, with information-extraction precision 0.89, recall 0.88, and F1 0.88. [Anhui University of Traditional Chinese Medicine, Hefei University] [[DOI](https://doi.org/10.1007/s44443-026-00743-1)]
- [*Digital Chinese Medicine*] **TCM-HyperRAG** Higher-order knowledge hypergraphs for TCM diagnosis and prescription recommendation, with traceable evidence passed to a backbone model. [[DOI](https://doi.org/10.1016/j.dcmed.2026.08.004)]
- [*Frontiers in Medicine*] **TCM-DiffRAG** Syndrome-differentiation RAG with a general KG, a personalized KG, and chain-of-thought. [Guangdong Institute of Intelligence Science and Technology, Zhuhai, Hangzhou Ganzhicao Technology Co., Ltd, BoardWare Information System Limited] [[Published](https://doi.org/10.3389/fmed.2026.1804478)] [[Paper](https://arxiv.org/abs/2602.22828)] [[Code](https://github.com/LiJianmin6706/Tcm_Diff_RAG)]
- [*Frontiers in Pharmacology*] **TCM-CoT-RAG** Retrieval-augmented generation with chain-of-thought for TCM rheumatology decisions. [[DOI](https://doi.org/10.3389/fphar.2026.1884526)]
- [*Neural Networks*] **LLM-SDaT** A knowledge-informed LLM framework for TCM syndrome differentiation. [[DOI](https://doi.org/10.1016/j.neunet.2026.108812)]
- [*世界科学技术-中医药现代化*] **KG-IMHRE（赵炳南流派可解释多跳检索增强问答）** KG-IMHRE guides an LLM with subgraph mining and dynamic retrieval queries over the Zhao Bingnan dermatology school graph. On that benchmark it scores 85.2 on multiple choice, 45.78 on open questions, and 73.38 overall. [[DOI](https://doi.org/10.11842/wst.20250706001)]
- [*proceedings-article*] **Construction of a Knowledge Graph for Functional Specification Standards of Traditional Chinese Medicine Information Systems Based on Large Language Models** Using 22 group-standard documents on functional specifications for traditional Chinese medicine information systems, the authors constrained DeepSeek with CRISPE prompts to extract entities and relations and then applied rule-based constraints to build a knowledge graph. [Hubei University of Chinese Medicine] [[DOI](https://doi.org/10.1145/3833450.3833480)]
- [*International Conference on Optics, Electronics, and Communication Engineering (*] **A knowledge-enhanced prescription generation model for TCM syndrome differentiation via multilevel memory retrieval** The prescription model retrieves similar cases with weighted BM25 and adds a drug knowledge graph from the Compendium of Materia Medica plus the eighteen incompatibilities and eighteen antagonisms, then passes that evidence to a large language model; experiments used the CCL2025 traditional Chinese medicine benchmark. [Chengdu Medical College, First Affiliated Hospital of Chengdu Medical College] [[DOI](https://doi.org/10.1117/12.3123588)]
- [*Journal of Visualized Experiments*] **A Study on An Intelligent Diagnosis and Treatment Assistant System For Acupuncture in Diminished Ovarian Reserve Based on A Knowledge Graph** Using large language models plus manual annotation on 82 acupuncture texts and clinical data, the authors built a graph of 16,558 entities and 80,084 relations; on 90 patients with diminished ovarian reserve, diagnostic agreement with experts was 86.7%. [Nanjing University of Chinese Medicine, Xuzhou Medical College, Nanjing General Hospital of Nanjing Military Command, Nanjing University] [[DOI](https://doi.org/10.3791/71182)]

</details>

<details>
<summary>2025 · 25</summary>

- [*世界科学技术-中医药现代化*] **阿尔茨海默病指南知识库问答（ChatGLM3）** LangChain grounds ChatGLM3-6B on a local library of Alzheimer guidelines and textbooks endorsed by the China Association of Chinese Medicine and the Chinese Medical Association. Against bare ChatGLM3-6B, factual-accuracy wins are 88.09% and completeness wins 85.71%. [[DOI](https://doi.org/10.11842/wst.20240329007)]
- [*世界科学技术-中医药现代化*] **监督微调结合检索增强的中医知识问答** ChatGLM3 is supervised-fine-tuned with PissA and then wrapped in RAG. Reported scores are BLEU 14.5830 and ROUGE-1 34.6730; with RAG the TCM item-bank F rises to 0.6398 from a 0.2654 ChatGLM3 baseline. [[DOI](https://doi.org/10.11842/wst.20241121002)]
- [*IEEE ICCBDAI 2025*] **动态知识图谱与大模型的中医生理建模** Connects dynamic knowledge graphs with large language models for TCM physiological modeling. [[DOI](https://doi.org/10.1109/iccbdai66607.2025.11388184)]
- [*IEEE BIBM 2025*] **Chinese patent medicine knowledge system** Constructing a knowledge system for traditional Chinese patent medicine using LLMs and KGs. [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356149)]
- [*CCIS*] **中医问诊中的大模型与知识图谱** Case study of integrating large language models with knowledge graphs in TCM consultation. [[DOI](https://doi.org/10.1007/978-981-96-1809-5_28)]
- [*CCIS*] **中医药知识图谱问答系统** An intelligent TCM question-answering system that joins a knowledge graph with large language models. [[DOI](https://doi.org/10.1007/978-981-96-1809-5_26)]
- [*数据分析与知识发现*] **中医药标准知识问答系统** Retrieval-augmented QA system for TCM standards knowledge, built and evaluated in practice. [China Academy of Chinese Medical Sciences et al.] [[DOI](https://doi.org/10.11925/infotech.2096-3467.2024.0747)]
- [*Frontiers in Medicine*] **中医医案问答系统** A TCM case-based QA system integrating LLMs and knowledge graphs for efficient case retrieval and analysis (Front. Med. 2025). [[DOI](https://doi.org/10.3389/fmed.2024.1512329)]
- [*JMIR Medical Informatics*] **Yaoshi-RAG** Uncertain-KG RAG for medicine–food homology dietary recommendation with personalization and explainability. [[DOI](https://doi.org/10.2196/75279)]
- [*Frontiers in Pharmacology*] **TCMRD-KG** Innovative design of a rheumatology TCM knowledge graph from ancient literature. [Beijing University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fphar.2025.1535596)]
- [*Digital Chinese Medicine*] **TCMLCM** KG2T-based intelligent QA model for TCM lung cancer. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2025.03.011)]
- **TCM-Sage** Evidence-synthesis RAG assistant for TCM practitioners (hybrid vector + knowledge graph). [[Code](https://github.com/AndyZHENG0715/TCM-Sage)]
- [*proceedings-article*] **Smart Virtual Patients for TCM: Combining Knowledge Graphs and Language Models** The traditional Chinese medicine virtual patient combines a large language model and a knowledge graph with beam search and Sentence-BERT pruning, reaching 53.2% symptom consistency and 62.5% recall, both above the prompt-plus-knowledge-graph baseline. [Universiti Sains Malaysia, Sultan Qaboos University] [[DOI](https://doi.org/10.1109/icitda68167.2025.11332301)]
- [*IEEE International Conference on Electrical, Automation and Computer Engineering*] **Research on the Organization and Application of Traditional Chinese Medicine Processing Knowledge in Lingnan Herbal Medicine Ancient Texts by Integrating Large Models and Knowledge Graph Technology** The authors used large language models and a knowledge graph to organize medicinal materials, processing methods, adjuvants, and effects in Lingnan herbal classics, stored the graph in Neo4j, and combined BERT-CAN-NER with generative large models for natural-language question answering. [Guangzhou University of Chinese Medicine] [[DOI](https://doi.org/10.1109/iceace67491.2025.11439512)]
- [*proceedings-article*] **Research on the Construction of a Traditional Chinese Medicine Coronary Heart Disease Question-Answering System Integrating Large Language Models and Knowledge Graphs** Prompted large language models extracted entities and relations from eight coronary-heart-disease guidelines of traditional or integrative Chinese medicine published in the past decade, producing a knowledge graph of 452 nodes and 690 relations, with BERT+CNN selected as the best intent-recognition model. [China Academy of Chinese Medical Sciences, Tongji University] [[DOI](https://doi.org/10.1145/3777577.3777709)]
- [*Pharmacological Research*] **RAG-CPMF** Multi-LLM verification + RAG for Chinese patent medicine recommendation, with a living public CPM dataset. [[DOI](https://doi.org/10.1016/j.phrs.2025.107883)] [[Data](https://gitee.com/tcmdoc/cpm)]
- [*arXiv*] **OpenTCM** GraphRAG TCM retrieval and diagnosis system with a gynecology classics knowledge graph. [[Paper](https://arxiv.org/abs/2504.20118)] [[Code](https://github.com/OpenTCM01/OpenTCM)]
- [*proceedings-article*] **Method for Constructing TCM Syndrome Differentiation Q&A System with LLM-RAG** The syndrome-differentiation question-answering framework connects a curated traditional Chinese medicine repository to a large language model through structured retrieval, in order to improve factual accuracy, contextual precision, and professional quality. [Baoshan University] [[DOI](https://doi.org/10.1145/3784013.3784061)]
- [*IEEE BIBM*] **MRD-RAG** Multi-round diagnostic RAG simulating clinical reasoning; builds **DiagnosGraph** spanning TCM and Western medicine (876 diseases / 7,997 nodes / 37,201 triples). [[Published](https://doi.org/10.1109/bibm66473.2025.11357107)] [[Paper](https://arxiv.org/abs/2504.07724)]
- [*Interdisciplinary Sciences*] **LLM-driven TCM KG construction** LLM-driven construction and application of a TCM knowledge graph. [Henan University of Technology] [[DOI](https://doi.org/10.1007/s12539-025-00735-1)]
- [*Journal of Medical and Biological Engineering*] **LLM + RAG TCM inference** Combining LLMs with RAG for TCM inference. [Taipei City Hospital] [[DOI](https://doi.org/10.1007/s40846-025-00988-7)]
- [*International Conference on e-Education, e-Business, e-Management and e-Learning*] **Knowledge Graphs Combined with ChatGPT in the Field of Acupuncture: A Case Study on the Treatment of Depression** The study built a depression-specific acupuncture knowledge graph and used large language models to optimize knowledge integration for researchers and clinicians. [Nanjing University, Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1109/ic4e65071.2025.11075342)]
- [*Proceedings of the 2nd International Conference on Machine Learning and Automation, CONF-M*] **Chinese Medicine Question Answering Robot Based on RAG and Self-Built Dataset** Builds a traditional Chinese medicine question-answering robot with retrieval-augmented generation and a self-built dataset. [[DOI](https://doi.org/10.4108/eai.21-11-2024.2354617)]
- [*JAMIA*] **AcuKG** A knowledge graph of medical acupuncture built with entity recognition, relation extraction, and ontology mapping. [[DOI](https://doi.org/10.1093/jamia/ocaf179)]
- [*Communications in Computer and Information Science Health Information Processing. Evaluati*] **A TCM Syndrome Differentiation Thinking Method Based on Chain of Thought and Knowledge Retrieval Augmentation** CotKE-TCM prompts a large language model with chain-of-thought and retrieves similar cases, generated TCM knowledge, and clinical experience for syndrome differentiation, tested on the CHIP 2024 track. [ANTA Group] [[DOI](https://doi.org/10.1007/978-981-96-4298-4_3)]

</details>

<details>
<summary>2024 · 13</summary>

- [*中国数字医学*] **循证中医指南 PICO 知识图谱问答** Cui et al. use ERNIE Bot to extract PICO triples from a polycystic-ovary guideline, store 248 nodes and 337 relations in Neo4j, and draft 12 question classes with 24 templates for a guideline QA system. [[Paper](https://www.zgszyx.org.cn/CN/Y2024/V19/I5/20)]
- [*IEEE BIBM 2024*] **名老中医针灸医案知识图谱** Builds a knowledge graph of famous acupuncturists' cases by extracting information with a large language model. [[DOI](https://doi.org/10.1109/bibm62325.2024.10821904)]
- [*JMIR Medical Informatics*] **中医领域知识图谱补全** Domain knowledge graph completion and quality evaluation for Traditional Chinese Medicine. [Zhejiang Chinese Medical University, Guangdong Provincial Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2196/55090)]
- [*南京中医药大学学报*] **中医药问答大语言模型** TCM QA LLM combining RAG with P-Tuning v2 fine-tuning on ChatGLM2-6B. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1375)]
- [*计算机科学与探索*] **中医药大模型知识增强方法** Knowledge augmentation for TCM LLMs — a graph built from ~100k classical formulas preserving prescription structure. [Tianjin University] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2407082)]
- [*Methods of Information in Medicine*] **TCMSF** TCMSF: a construction framework for a TCM syndrome ancient-book knowledge graph that organizes syndrome knowledge from classical texts in a structured, semantically oriented way (Methods Inf. Med. 2024). [[DOI](https://doi.org/10.1055/a-2590-6348)]
- [*IEEE International Conference on Medical Artificial Intelligence (MedAI)*] **TCMRD-KG: Design and Development of a Rheumatism Knowledge Graph Based on Ancient Chinese Literature** TCMRD-KG is described as the first rheumatism-specific knowledge graph built from ancient traditional Chinese medicine books, with entity labeling that combines automatic annotation by mainstream large language models and manual review. [Beijing University of Chinese Medicine, China Academy of Chinese Medical Sciences, Guang’anmen Hospital, Institute of Basic Theory for Chinese Medicine] [[DOI](https://doi.org/10.1109/medai62885.2024.00083)]
- [*EIECC*] **TCM MLKG-RAG** TCM intelligent diagnosis based on multi-layer knowledge graph retrieval-augmented generation. [University of Science and Technology of China] [[DOI](https://doi.org/10.1109/EIECC64539.2024.10929529)]
- [*OSF Preprints（预印本）*] **RAG 增强中医问答置信度** Implementing retrieval-augmented generation to build LLM confidence in TCM (preprint). [[DOI](https://doi.org/10.31219/osf.io/ns2v3)]
- [*arXiv*] **Prompt-RAG: Pioneering Vector Embedding-Free Retrieval-Augmented Generation in Niche Domains, Exemplified by Korean Medicine** Prompt-RAG, which does not use vector embeddings, outperformed ChatGPT and vector-embedding retrieval-augmented generation on relevance and informativeness in a Korean-medicine question-answering chatbot. [Gachon University, Stanford Medicine, Stanford University] [[Paper](https://arxiv.org/abs/2401.11246)]
- [*Phytomedicine*] **PresRecRF** Fuses a molecular knowledge graph with TCM semantic representations from large models, and predicts both herbs and dosages. Code and data are on GitHub. [[DOI](https://doi.org/10.1016/j.phymed.2024.156116)] [[Code](https://github.com/2020MEAI/PresRecRF)]
- [*Electronics*] **LLM 构建中医知识图谱** Constructing Traditional Chinese Medicine knowledge graphs based on large language models. [[DOI](https://doi.org/10.3390/electronics13071395)]
- [*Database (Oxford)*] **ACUBERT** ACUBERT for meridian entity recognition and classification in acupuncture indication knowledge bases. [Nanjing KG Data Technology] [[DOI](https://doi.org/10.1093/database/baae083)]

</details>

<details>
<summary>2023 · 3</summary>

- [*Frontiers of Information Technology & Electronic Engineering*] **知识引导的中医荐药（FITEE）** Graph-attention herb recommendation guided by a knowledge graph mined from TCM literature and prescriptions, with formula-theory signals added in the prediction layer. [[DOI](https://doi.org/10.1631/FITEE.2200662)]
- [*计算机科学与探索*] **大模型融合知识图谱问答系统** Vertical-domain QA system deeply integrating LLMs with knowledge graphs for TCM formulas. [Tianjin University] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2308070)]
- [*世界科学技术-中医药现代化*] **MMKGQA（海洋中药知识图谱问答）** MMKGQA answers marine Chinese materia medica questions from the MMKG graph using Aho-Corasick and Word2Vec. On six common question types, mean precision, recall, and F1 are 97.93%, 83.41%, and 89.10%. It is not an LLM system. [[DOI](https://doi.org/10.11842/wst.20220514002)]

</details>


</details>

<details>
<summary>Prescription (20): 荐药、组方、药对</summary>

<details>
<summary>2026 · 8</summary>

- [*arXiv*] **Patient-Conditioned Dual Hypergraph Reasoning** Patient-conditioned dual-hypergraph reasoning for auditable TCM prescription support, organizing symptom/tongue/pulse evidence around patterns and treatment principles (Tianjin University). [[Paper](https://arxiv.org/abs/2607.04025)]
- [*KSII Transactions on Internet and Information Systems*] **GAT+LLM TCM Prescription Generation** Intelligent TCM prescription generation combining graph attention networks with LLMs (formally published in KSII TIIS). [[DOI](https://doi.org/10.3837/tiis.2026.05.006)]
- [*世界科学技术-中医药现代化*] **知识蒸馏中医辨证论治模型** GPT-4o distills TCM case records into syndrome-differentiation instructions, then LoRA-tunes Qwen2.5-7B. The paper reports more readable reasoning while keeping prescription accuracy. No brand name or public weights. [[DOI](https://doi.org/10.11842/wst.20250422007)]
- [*arXiv*] **理法方药对齐的中医处方生成** Four-stage alignment for TCM prescription generation covering auditable li-fa-fang-yao reasoning, follow-up adjustment, and contraindications such as the eighteen antagonisms. [[Paper](https://arxiv.org/abs/2609.25755)]
- [*CCIS*] **多阶段学习的中医处方推荐大模型** A large language model for TCM prescription recommendation trained in multiple stages. [[DOI](https://doi.org/10.1007/978-981-92-0291-1_11)]
- [*Chinese Medicine*] **TCMNet** LLM-assisted disease knowledge mining with PPI networks and binding prediction for formula optimization. [Zhejiang Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1186/s13020-026-01360-w)]
- [*Mathematics*] **LLM-Driven Unsupervised Discovery of Semantic Decision Dimensions for Dynamic Scheduling and Intelligent Systems: A Traditional Chinese Medicine Case Study** DeepSeek-V3.2 induced 458 raw labels from 12,163 traditional Chinese medicine herb records and 64,107 short sentences, merged into 22 semantic categories; Qwen3-Embedding-8B found average internal coherence above 60% for 19 concepts, and experts rated reasonableness 4.64 on a 1-to-5 scale. [Changchun University of Chinese Medicine, Shandong University of Arts, Tsinghua University] [[DOI](https://doi.org/10.3390/math14152681)]
- [*Digital Chinese Medicine*] **CMM-EmbedCluster** LLM + medicinal-property-theory clustering framework for Chinese materia medica, with a 567-herb property knowledge base. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2026.05.010)]

</details>

<details>
<summary>2025 · 6</summary>

- [*IEEE Journal of Biomedical and Health Informatics*] **LLM herb–drug interaction prediction** LLM-enhanced herbal medicine–drug interaction prediction. [Shenzhen University] [[DOI](https://doi.org/10.1109/jbhi.2025.3558667)]
- [*IEEE BIBM 2025*] **医学知识增强的双层对齐中药处方推荐** Medical-knowledge-enhanced dual-level alignment network for herbal prescription recommendation. [[DOI](https://doi.org/10.1109/bibm66473.2025.11356282)]
- [*JMIR Medical Informatics*] **Weighted-voting TCM formula classification** Weighted-voting LLM approach for TCM formula classification. [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.2196/69286)]
- [*IEEE International Conference on Bioinformatics and Biomedicine (BIBM)*] **Two-Stage Chain-of-Thought Fine-Tuning for TCM Medication Decision-Making in Nsclc** For non-small-cell lung cancer, the two-stage chain-of-thought fine-tuning improved prescription generation and proprietary-Chinese-medicine recommendation by 1.2% and 6.1% over the baseline. [China Academy of Chinese Medical Sciences, Qinghai Normal University, Chinese Academy of Social Sciences, Institute of Ethnology and Anthropology] [[DOI](https://doi.org/10.1109/bibm66473.2025.11356901)]
- [*IEEE JBHI*] **TEmbed-DDI：中西药相互作用标注** Annotates cross-domain drug interactions with large language models and bidirectional networks, and adds a Chinese-medicine interaction evaluation. [[DOI](https://doi.org/10.1109/jbhi.2025.3563289)]
- [*proceedings-article*] **Dynamic Disease Tracking and Personalized Prescription Recommendation Using Large Language Model in Traditional Chinese Medicine** The system connects multi-turn consultation and temporal analysis to a large language model for personalized traditional Chinese medicine prescriptions, and on 1,000 insomnia cases it improved initial-case inference, diagnostic accuracy, and adaptability. [National Central University, National Taiwan University of Science and Technology, Research Center for Humanities and Social Sciences, Academia Sinica] [[DOI](https://doi.org/10.1109/iccbe65177.2025.11255949)]

</details>

<details>
<summary>2024 · 3</summary>

- [*IEEE BIBM*] **TCM-FTP** Fine-tuning LLMs for herbal prescription prediction. [[DOI](https://doi.org/10.1109/BIBM62325.2024.10822451)]
- [*JAMIA*] **PresRecST** Progressive herb-prescription recommendation following syndrome differentiation then treatment planning (JAMIA 2024); ships a public encoded TCM-Lung subset and a TCM-PD reproduction table. [[DOI](https://doi.org/10.1093/jamia/ocae066)] [[Code](https://github.com/2020MEAI/PresRecST)]
- [*IEEE International Conference on Computer and Communication Engineering Technolo*] **A Study of Automated Data Mining of Medication Rules in Traditional Chinese Medicine Prescriptions Based on Large Language Model** Through interactive questioning, a large language model ran frequency, clustering, and Apriori association analyses on traditional Chinese medicine prescriptions for osteoporosis, and the automated results were highly similar to manual SPSS statistics. [Jinan University] [[DOI](https://doi.org/10.1109/ccet62233.2024.10837914)]

</details>

<details>
<summary>2023 · 3</summary>

- [*IEEE BIBM*] **中医方剂 LLM 分类** Fine-tuned LLMs with refined prompt templates for TCM formula classification, using data sources such as the national medical-insurance catalog of proprietary Chinese medicines (IEEE BIBM 2023). [Leipzig University, Changchun University of Chinese Medicine, Liaoning Technical University, Sichuan Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385776)]
- [*IEEE Access*] **PreGenerator** TCM prescription recommendation model combining retrieval and generation. [College of Physics, Taiyuan University of Technology, Taiyuan, China, North Automatic Control Technology Institute, Taiyuan, China] [[DOI](https://doi.org/10.1109/ACCESS.2023.3316219)]
- [*IEEE BIBM*] **LLM+GNN 中医处方推荐** TCM prescription recommendation combining large language models with graph neural networks. [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385489)]

</details>


</details>

<details>
<summary>Extraction / PLM (8): NER、关系抽取、BERT 类编码器</summary>

- [*世界科学技术-中医药现代化*] **杏林-NER (XingLin-NER)** XingLin-NER is a generative NER framework that instruction-tunes structured and reasoning prompts for variable TCM clinical terms, scored with TCM-BERT semantic similarity. It is an extraction method, not a general TCM chat model. [[DOI](https://doi.org/10.11842/wst.20250327010)]
- [*proceedings-article*] **Named Entity Recognition in Traditional Chinese medicine Literature Data for Obesity Based on Large Language Models** For named-entity recognition in traditional Chinese medicine obesity literature, prompt-optimized DeepSeek-R1 reached an F1-score of 0.927 on the test set. [Hubei University of Chinese Medicine] [[DOI](https://doi.org/10.1145/3833450.3833478)]
- [*Applied Intelligence*] **KDC-NER** Knowledge-guided data augmentation + LLM fine-tuning framework for nested NER in TCM. [Jiangxi University of Chinese Medicine] [[DOI](https://doi.org/10.1007/s10489-026-07095-3)]
- [*npj Digital Medicine*] **LM extraction for complementary medicine** Language models for data extraction and risk-of-bias assessment in complementary medicine literature. [Lanzhou University] [[DOI](https://doi.org/10.1038/s41746-025-01457-w)]
- [*Scientific Reports*] **双通道知识注意力辨证模型** Dual-channel knowledge-attention NLP model for TCM syndrome differentiation, addressing rare characters and terminology extraction. [[DOI](https://doi.org/10.1038/s41598-025-96404-w)]
- [*Lecture Notes on Data Engineering and Communications Technologies*] **中医药专利关系抽取** Relation extraction over TCM patents with a large language model and diversified semantic interaction. [[DOI](https://doi.org/10.1007/978-3-032-10344-4_1)]
- [*Journal of the American Medical Informatics Association*] **LLM 腧穴定位关系抽取** Relation extraction with LLMs — a case study on acupuncture point locations. [The University of Texas MD Anderson Cancer Center , Houston, TX 77030] [[DOI](https://doi.org/10.1093/jamia/ocae233)]
- [*Frontiers in Artificial Intelligence*] **Evi-BERT** Automated information-extraction model (Evi-BERT) enhancing RCT evidence extraction for TCM. [[DOI](https://doi.org/10.3389/frai.2024.1454945)]

</details>

<details>
<summary>Evaluation (62): 基准和考试；要下载评测集走下面「数据集」</summary>

<details>
<summary>2026 · 31</summary>

- [*Future Internet (MDPI)*] **RAG+LoRA 中医执照考试推理架构** RAG+LoRA generative architecture with an 11,476-item Taiwan TCM licensing-exam dataset (2005-2025), raising accuracy from 61.0% to 89.0%+ (Future Internet, MDPI). [Chung Shan Medical University Hospital, Chung Shan Medical University] [[DOI](https://doi.org/10.3390/fi18060280)]
- [*Scientific Data*] **辨证论治大模型基准数据集** Scientific Data benchmark for evaluating syndrome differentiation and treatment in large language models. [[DOI](https://doi.org/10.1038/s41597-026-07587-4)]
- [*arXiv*] **证伪导向的可审计辨证协议** A model-agnostic falsification protocol for auditable syndrome differentiation on the public 200-case TCMEval-SDT set. [[Paper](https://arxiv.org/abs/2610.18298)]
- [*Frontiers in Plant Science*] **Medicinal-plant MLLM benchmark** Benchmarking multimodal LLMs for medicinal plant identification. [Shaoxing University] [[DOI](https://doi.org/10.3389/fpls.2026.1765281)]
- [*arXiv*] **LingLan** Large multi-task TCM benchmark: 5 domains, 13 subtasks, 25,624 instances. [Beijing Jiaotong University et al.] [[Paper](https://arxiv.org/abs/2602.01779)] [[Code](https://github.com/TCMAI-BJTU/LingLan)] [[Website](http://tcmnlp.com)]
- [*Journal of Evidence-Based Medicine*] **Large vs lightweight LLMs on TCM exams** Systematic comparison of large-scale vs lightweight LLMs on TCM exam questions. [First Affiliated Hospital of Henan University] [[DOI](https://doi.org/10.1111/jebm.70118)]
- [*Expert Systems with Applications*] **End-to-end TCM clinical support benchmark** Benchmark for end-to-end TCM clinical support across the full LLM care pipeline. [East China Normal University] [[DOI](https://doi.org/10.1016/j.eswa.2026.132267)]
- [*Journal of Traditional Chinese Medical Sciences*] **TCM intelligent pre-consultation clinical evaluation** Tertiary-hospital clinical evaluation of an LLM intelligent pre-consultation system using a physician–AI–patient triad model. [Beijing Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.jtcms.2026.06.002)]
- [*Frontiers in Medicine*] **TCM AI-tutor evaluation** Multimodal LLM evaluation for TCM education across cognitive levels. [Beijing University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1893231)]
- [*Scientific Reports*] **Three-LLM TCM licensing exam evaluation** Systematic evaluation of 3 LLMs (incl. Gemini) on the national TCM medical licensing examination. [Shanghai Jiao Tong University] [[DOI](https://doi.org/10.1038/s41598-026-49200-z)]
- [*Guidelines and Standards of Chinese Medicine*] **中医大模型临床实践评测方法** Builds a clinical-practice evaluation for TCM large language models, arguing that Western medical benchmarks do not fit. [[DOI](https://doi.org/10.1097/gscm.0000000000000123)]
- [*npj Digital Medicine*] **中医场景中医疗大模型的提示词效应** Evaluates 16 models on TCM and shows that prompt effects depend on the model, which complicates reliable deployment. [[DOI](https://doi.org/10.1038/s41746-026-03397-5)]
- [*arXiv*] **TongueDx2** Systematic ablation of the tongue-diagnosis DL design space (20+ model variants); TongueDx2 includes 5,109 images / 976 expert annotations. [[Paper](https://arxiv.org/abs/2607.28148)]
- [*arXiv*] **TCMQA** Open benchmark of 38,279 TCM licensing questions paired with 15,151 answers from 101 licensed practitioners. [[Paper](https://arxiv.org/abs/2609.33014)]
- [*Frontiers in Artificial Intelligence*] **TCMI-F-6D** Six-dimensional benchmark of interdisciplinary foundational competence in TCM informatics. [Anhui University of Chinese Medicine] [[DOI](https://doi.org/10.3389/frai.2026.1780967)] [[Code](https://github.com/123adf-dev/TCMI-F-6D-Benchmark)]
- [*arXiv*] **TCMClinicalReason-Bench** 2,000 multicenter EHR cases testing whether a model can reason from pathogenesis and syndrome to treatment principle and prescription. [[Paper](https://arxiv.org/abs/2610.04215)]
- [*ICIC 2026*] **TCMBenchEval** Benchmark evaluating LLMs on real clinical TCM case records (ICIC 2026). [Shantou University] [[DOI](https://doi.org/10.1007/978-981-92-3498-1_1)]
- [*Frontiers in Medicine*] **Supporting postgraduate exam preparation with large language models: implications for traditional Chinese medicine education** On the 2023 Chinese postgraduate examination for traditional Chinese medicine, Ernie Bot scored 50.30% and ChatGLM 46.67%, both above the passing score, with the highest scores in the medical humanities module. [Beijing University of Chinese Medicine, Dongzhimen Hospital Affiliated to Beijing University of Chinese Medicine, Changchun University of Chinese Medicine, Leipzig University] [[DOI](https://doi.org/10.3389/fmed.2025.1667104)]
- **Med-Bench-Arena** Open evaluation platform for medical and TCM LLMs/Agents (HF/vLLM/LiteLLM, multimodal, TCM-specific metrics), from the ZhongJing team. [[Code](https://github.com/pariskang/Med-Bench-Arena)]
- [*arXiv*] **MMIR-TCM** Memory-augmented multimodal tongue diagnosis and clinical decision framework; proposes MedTCM dataset and TDEU metric. [[Paper](https://arxiv.org/abs/2607.01814)]
- [*Brain Behavior and Immunity Integrative*] **Large language models vs traditional Chinese medicine clinical reasoning: Analysis of a single migraine case study** On one standardized migraine case, nine large language models were compared with two traditional Chinese medicine physicians and a published case response, scored blindly by 32 experts; GPT o3, Qwen 3, and Gemini 2.5 Pro matched or exceeded selected comparators in some domains, while Aya Expanse 32B scored lower. [Harvard University, Massachusetts General Hospital] [[DOI](https://doi.org/10.1016/j.bbii.2026.100192)]
- [*arXiv*] **Large Language Models Versus Physicians in Traditional Chinese Medicine: A Real-World Clinical Case Evaluation** From 349 de-identified outpatient cases at 62 hospitals, the authors used 60 cases to compare 16 large language models with 60 practicing traditional Chinese medicine physicians, scored blindly by five senior experts across nine diagnostic and therapeutic dimensions. [University of Missouri, Seventh People's Hospital of Shanghai, Yunnan University of Traditional Chinese Medicine, Northwestern University] [[Paper](https://arxiv.org/abs/2609.17544)]
- [*JMIR Formative Research*] **Korean Medical Consultation With Open-Weight Large Language Models: Pilot Comparative Evaluation of Retrieval-Augmented Generation With Metadata Filtering** An open-weight LLM chatbot for Korean medical consultation, comparing retrieval-augmented generation with metadata filtering. [[DOI](https://doi.org/10.2196/72604)]
- [*Frontiers in Medicine*] **Knowledge-guided adaptive educational support for traditional Chinese medicine using large language models and knowledge graphs: integrating Confucian educational principles** The intelligent traditional Chinese medicine tutor links a large language model to a knowledge graph from the Golden Mirror of Medicine; of 125 student volunteers, 102 questionnaires were analyzed, and the integrated system produced higher immediate post-test scores than the large-language-model-only group and the self-study group. [Anhui University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1943401)]
- [*AI Engineering*] **Knowledge of Chatbots on Oriental Medicine-Based Theory and Practice of Acupuncture Is Inferior to That on Western Medicine-Based Acupuncture-Transmitted Infections** Compares free and subscribed ChatGPT, Claude, Copilot, Gemini, and Perplexity on 2,528 oriental-medicine acupuncture theory items and 100 acupuncture-infection items; the median theory score was 75%, below 86% on the infection items. [National Chung Hsing University, Tung Wah College, The University of Hong Kong, Fuke Fengze Chinese Medicine Clinic] [[DOI](https://doi.org/10.53941/aieng.2026.100004)]
- [*medRxiv*] **KampoBench** Physician-reviewed Kampo consultation benchmark: 74 scenarios and 310 dialogue-level criteria, scoring application rather than exam recall. [[DOI](https://doi.org/10.64898/2026.10.07.26365005)]
- [*Terminology International Journal of Theoretical and Applied Issues in Specializ*] **From readable to executable** Using the same three prompts for each sampled term, the authors tested with ChatGPT-4o whether the WHO 2007 and 2022 traditional Chinese medicine terminology standards give enough explicit information for auditable selection among coexisting English variants. [University of Malaya] [[DOI](https://doi.org/10.1075/term.00097.yu)]
- [*proceedings-article*] **Evaluating Semantic Fidelity and Cohesion in NMT and LLM-based Translation of Traditional Chinese Medicine Classics** For English translation of traditional Chinese medicine classics, DeepSeek exceeded Google Translate and ChatGPT-5 on BERTScore semantic fidelity to the human reference, while ChatGPT-5 produced more semantically coherent text across sentences. [Northwestern Polytechnical University, Air Force Engineering University] [[DOI](https://doi.org/10.1109/icnlp69856.2026.11528039)]
- [*Current Bioinformatics*] **Evaluating Large Language Models for Query Refinement in Systematic Review Retrieval of Traditional Chinese Medicine** The authors tested GPT-4o, GPT-5, DeepSeek-V3, and DeepSeek-R1 under six prompts for literature retrieval in CNKI, Wanfang, PubMed, and Embase on psoriasis, COVID-19, and type 2 diabetes; the deduplicated gold-standard set contained 182 records (50, 74, and 58). [China Academy of Chinese Medical Sciences, Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2174/0115748936492177260915061800)]
- [*JMIR Formative Research*] **ChatGPT、DeepSeek与医师针灸方案对照** Compares ChatGPT, DeepSeek, and physician-generated acupuncture treatment plans. [[DOI](https://doi.org/10.2196/95851)]
- [*Pattern Recognition*] **ATCMD-Bench** First agentic TCM diagnosis benchmark, evaluating LLMs through multi-agent simulated consultations. [South China University of Technology] [[DOI](https://doi.org/10.1016/j.patcog.2026.113679)]

</details>

<details>
<summary>2025 · 19</summary>

- [*Expert Systems with Applications*] **针灸大模型驯化与生成评估 (Taming LLMs for Acupuncture)** Taming LLMs for acupuncture & moxibustion diagnosis, with generation quality evaluated at the semantic-similarity level. [[DOI](https://doi.org/10.1016/j.eswa.2024.125920)]
- [*JMIR Medical Informatics*] **辨证思维评测 (Syndrome Differentiation Thinking)** Method-development study evaluating and improving LLMs' TCM syndrome-differentiation thinking ability. [[DOI](https://doi.org/10.2196/75103)]
- [*UbiComp Companion 2025*] **TCM misinformation detection evaluation** Safety evaluation framework with 3,000+ TCM exam items × 4 paradigms, covering wrong-option, misleading, and fabrication detection. [Tsinghua University] [[DOI](https://doi.org/10.1145/3714394.3756275)]
- [*JMIR Formative Research*] **TCM stroke LLM benchmark** Quantitative benchmark study of LLMs in the TCM stroke domain. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2196/81545)]
- [*Frontiers in Pharmacology*] **TCM guideline adherence evaluation** Content-analysis evaluation of LLM adherence to clinical practice guidelines in Chinese medicine. [Lanzhou University] [[DOI](https://doi.org/10.3389/fphar.2025.1649041)]
- [*JMIR Formative Research*] **5-LLM TCM clinical decision comparison** Comparative study of 5 LLMs for TCM clinical decision-making. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.2196/80167)]
- [*NeurIPS 2025*] **TCM-Ladder** First large multimodal TCM QA benchmark with 52,000+ items (NeurIPS 2025). [[Paper](https://arxiv.org/abs/2505.24063)] [[Code](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[Leaderboard](https://tcmladder.com)]
- [*WISE 2025*] **TCM-Eval (WISE 2025)** Multi-dimensional TCM evaluation framework (WISE 2025); a different work from the ZMT-M1 TCM-Eval (arXiv 2511.07148) despite the identical name. [Tianjin International Joint Academy of Biomedicine] [[DOI](https://doi.org/10.1007/978-981-95-7251-9_15)]
- [*arXiv*] **TCM-BEST4SDT** Case benchmark for syndrome differentiation and treatment (knowledge / ethics / safety / SDT). [[DOI](https://doi.org/10.6084/m9.figshare.30615956)] [[Paper](https://arxiv.org/abs/2512.02816)] [[Code](https://github.com/DYJG-research/TCM-BEST4SDT)]
- [*arXiv*] **TCM-5CEval** Five-dimension deep evaluation extending TCM-3CEval with materia medica and non-drug therapies. [[Paper](https://arxiv.org/abs/2511.13169)]
- [*Communications Medicine*] **TCM-3CEval** Three-axis TCM LLM evaluation: core knowledge, classics comprehension, and clinical decision-making. [[Paper](https://arxiv.org/abs/2503.07041)] [[Published](https://doi.org/10.1038/s43856-026-01631-5)]
- [*npj Digital Medicine*] **TCM LLM acupuncture clinical evaluation** Real-case evaluation of 7 general LLMs vs licensed acupuncturists on SDT, point selection, needling, and herbs (*npj Digital Medicine*). [[DOI](https://doi.org/10.1038/s41746-025-01845-2)]
- [*JMIR Formative Research*] **Performance Assessment of ChatGPT-4.0 and ChatGLM Series in Traditional Chinese Medicine for Metabolic Associated Fatty Liver Disease: Comparative Study** The authors gave medical records of 87 metabolic-dysfunction-associated fatty-liver-disease cases treated with traditional Chinese medicine to ChatGPT-4.0, ChatGLM4, ChatGLM4 with a knowledge base, and ChatGLM3-6B, comparing syndrome differentiation, confusion of Chinese and Western concepts, and treatment-plan text. [Second Military Medical University, Chinese People's Liberation Army] [[DOI](https://doi.org/10.2196/66503)]
- [*arXiv*] **New Snow Tablets** Reveals systematic flaws of general and TCM-specific LLMs that guess formula ingredients from drug names. [[Paper](https://arxiv.org/abs/2504.03786)]
- [*Scientific Data*] **MTCMB** Multi-task TCM benchmark (~12 subsets, ~7.1k samples) covering knowledge, reasoning, formulas, and safety. [[Paper](https://arxiv.org/abs/2506.01252)] [[Code](https://github.com/Wayyuanyuan/MTCMB)] [[Published](https://doi.org/10.1038/s41597-026-07967-w)]
- [*Preprints.org（预印本）*] **GPT 台湾中医执业考试评估** GPT-3.5/GPT-4/GPT-4o performance on the Taiwan TCM licensing examination with reliability analysis (preprint). [[DOI](https://doi.org/10.20944/preprints202501.1787.v1)]
- [*IJCNN 2025*] **From Metaphor to Mechanism** LLMs decode TCM metaphor / imagistic-thinking language and map it to modern medical concepts. [Shandong Normal University,Jinan,China, China Pharmaceutical University,Nanjing,China, The University of Tokyo,Tokyo,Japan, Universiti Tunku Abdul Rahman,Perak,Malaysia] [[Paper](https://arxiv.org/abs/2503.02760)] [[Published](https://doi.org/10.1109/ijcnn64981.2025.11228098)]
- [*arXiv*] **Conveying Imagistic Thinking in Traditional Chinese Medicine Translation: A Prompt Engineering and LLM-Based Evaluation Framework** From four foundational passages of Huangdi Neijing, prompt scaffolding guided DeepSeek V3.1 to convey metaphor and metonymy; ChatGPT 5 Pro and Gemini 2.5 Pro then simulated three reader types and scored human, baseline, and prompt-adjusted translations on five cognitive dimensions, with the prompt-adjusted translations best on all five. [[Paper](https://arxiv.org/abs/2512.01198)]
- [*The Electronic Library*] **Contemporary technological value of ancient Chinese medical books: an empirical patent citation analysis using large language models** Large language models recognized traditional Chinese medicine entities and classified citation intent in patents; 72.9% of the patent citations showed low knowledge integration, and Systematic Differentiation of Warm Diseases ranked highest in technological impact. [Wuhan University, China Academy of Chinese Medical Sciences, Nanjing University] [[DOI](https://doi.org/10.1108/el-06-2025-0221)]

</details>

<details>
<summary>2024 · 10</summary>

- [*南京中医药大学学报*] **中医标准化评估基准** Standardized TCM evaluation benchmark of 29,506 questions across 13 subjects; tests 3 general and 5 Chinese medical LLMs. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1383)]
- [*arXiv*] **Utilizing Large Language Models for Named Entity Recognition in Traditional Chinese Medicine against COVID-19 Literature: Comparative Study** The authors assembled 389 articles on traditional Chinese medicine against COVID-19 and manually annotated 48 of them with six entity types; under fuzzy match ChatGPT beat BERT question-answering models on 5 of 6 tasks, while exact match reversed that pattern, and none of GPT-4's F1 scores on herb, target, or research method exceeded 0.5. [Institute of Basic Theory for Chinese Medicine, GESIS - Leibniz Institute for the Social Sciences, University of Bonn] [[Paper](https://arxiv.org/abs/2408.13501)]
- [*arXiv*] **TCMD** TCMD, a TCM licensing-exam multiple-choice set for LLM evaluation (paper reports ~2,851 train / 600 test). Independent check found no official GitHub or Hugging Face download. [[Paper](https://arxiv.org/abs/2406.04941)]
- [*IEEE International Conference on Medical Artificial Intelligence (MedAI)*] **Reunderstanding of the Classification of Syndromes in the Traditional Chinese Medicine Classic “Shang Han Lun” Based on Large Language Models** From ten selected Three-Yang passages in Shang Han Lun, Chinese and English ChatGLM 4.0 and ChatGPT-4.0 reclassified cases by modern medical consensus; among the four outputs, Chinese ChatGLM 4.0 was closest to the original Three-Yang grouping and English ChatGLM 4.0 diverged the most. [Beijing University of Chinese Medicine, China Academy of Chinese Medical Sciences, Wangjing Hospital of China Academy of Chinese Medical Sciences, Institute of Basic Theory for Chinese Medicine] [[DOI](https://doi.org/10.1109/medai62885.2024.00052)]
- [*Journal of Translational Medicine*] **LLM 中医语言文化偏差研究** Comparing LLMs developed in different countries on TCM; highlights language/cultural bias and the need for localized models. [Zhujiang Hospital, Southern Medical University, Shanghai Jiao Tong University, Shanghai First People's Hospital] [[DOI](https://doi.org/10.1186/s12967-024-05128-4)]
- [*Research Square（预印本）*] **GPT-4 中医研究生考试评估** GPT-4 vs mainstream Chinese LLMs on a TCM postgraduate examination dataset (preprint). [China Academy of Chinese Medical Science, Changchun University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.21203/rs.3.rs-4392855/v1)]
- [*J Integr Complement Med*] **GPT vs ERNIE 中医文化背景对比研究** A culture-framed comparison of GPT versus ERNIE on TCM tasks (J. Integr. Complement. Med. 2024). [College of Engineering, Boston University, Boston, MA, USA.] [[DOI](https://doi.org/10.1089/jicm.2024.0902)]
- [*대한한의학회지*] **Development of an LLM-based CPX Practicing Chatbot for Korean Medicine Education: Implementation of Automated Scoring and Feedback Generation Framework** In the Korean-medicine CPX practice chatbot, Claude-3.5-Sonnet scored every sample with perfect quantitative accuracy and averaged 43.2 seconds, faster than GPT-4. [Gachon University, Pusan National University] [[DOI](https://doi.org/10.13048/jkm.24067)]
- [*arXiv*] **ChatGPT 中医知识理解探究** Evaluating ChatGPT's comprehension of Traditional Chinese Medicine knowledge. [[Paper](https://arxiv.org/abs/2403.09164)]
- [*Chinese Medicine and Culture*] **ChatGPT 中医交互可行性研究** Feasibility and challenges of interactive AI for TCM, using ChatGPT as an example. [[DOI](https://doi.org/10.1097/MC9.0000000000000103)]

</details>

<details>
<summary>2023 · 2</summary>

- **中医新冠文献 LLM 命名实体识别** Comparative study of LLMs for named entity recognition in TCM COVID-19 literature (preprint). [[DOI](https://doi.org/10.2196/preprints.54346)]
- [*JMIR Medical Education*] **ChatGPT 针灸教育研究** Comparative study of ChatGPT as a learning tool in acupuncture education. [Seoul National University Hospital] [[DOI](https://doi.org/10.2196/47427)]

</details>


</details>

<details>
<summary>Platforms / tools (6): 编目、门户、可运行工具</summary>

- [*arXiv*] **TCMIIES** TCMIIES: a browser-based, zero-installation LLM system for structured information extraction from academic literature, aimed at TCM and other specialty researchers. [[Paper](https://arxiv.org/abs/2605.07507)]
- [*Science of Traditional Chinese Medicine*] **TCM Data Hub (YiYuan)** YiYuan LLM-driven TCM data platform. [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.1097/st9.0000000000000118)]
- [*Cell Discovery*] **神农Alpha** ShennongAlpha (Westlake University): an AI-driven sharing and collaboration platform for intelligent curation, acquisition and translation of natural-medicinal-material knowledge (Cell Discov. 2025). [[DOI](https://doi.org/10.1038/s41421-025-00776-2)] [[Website](https://shennongalpha.westlake.edu.cn/)] [[Paper](https://www.nature.com/articles/s41421-025-00776-2)] [[Code](https://github.com/shennong-program/shennongname)]
- [*IEEE BIBM 2025*] **DMease** An AI assistant for TCM doctors diagnosing and treating diabetes mellitus. [[DOI](https://doi.org/10.1109/bibm66473.2025.11356320)]
- [*IEEE International Conference on Computational Intelligence and Applications (IC*] **IC-BERT: An Instruction Classifier Model Alleviates the Hallucination of Large Language Models in Traditional Chinese Medicine** IC-BERT uses a BERT text filter to limit which questions a traditional Chinese medicine large language model may answer, so as to reduce fabricated facts when questions fall outside its capability. [Hainan University] [[DOI](https://doi.org/10.1109/iccia62557.2024.10719061)]
- [*IJACSA*] **草药智能配送聊天机器人** Smarter herbal medication delivery system employing an AI-powered chatbot. [University of the Cordilleras, Naresuan University Hospital, Catanduanes State University] [[DOI](https://doi.org/10.14569/ijacsa.2023.0140358)]

</details>

<details>
<summary>Other methods (18): 对齐、提示、专科任务</summary>

<details>
<summary>2026 · 5</summary>

- [*Translation Review*] **Beyond the Poetic Bard（中医AI翻译评论）** Beyond the Poetic Bard: a perspective on accuracy, epistemology, and medical-context limits of generative-AI translation of TCM texts (Translation Review). [[DOI](https://doi.org/10.1080/07374836.2026.2679929)]
- [*Progress in Biochemistry and Biophysics*] **Pathogenesis-reasoning CoT supervision for spleen-stomach disorders** Pathogenesis-reasoning chain-of-thought supervision replacing fixed-label classification for spleen-stomach disease syndrome recognition and multi-dimensional evaluation (Prog. Biochem. Biophys.). [[Paper](https://www.pibb.ac.cn/pibbcn/article/abstract/20260141)]
- [*Chinese Medicine*] **大模型连接中医知识与临床实践** Discusses how large language models can link implicit TCM knowledge with syndrome-based clinical practice. [[DOI](https://doi.org/10.1186/s13020-026-01489-8)]
- [*Biomedical Signal Processing and Control*] **Generating interpretable clinical reasoning chains in TCM via group relative policy optimization and multi-dimensional rewards** Generates interpretable traditional Chinese medicine clinical reasoning chains with group relative policy optimization and multi-dimensional rewards. [[DOI](https://doi.org/10.1016/j.bspc.2026.111275)]
- [*Digital Chinese Medicine*] **Fine-Med-Mental-T&P: a dual-track approach for high-quality instructional datasets of mental disorders in traditional Chinese medicine** Fine-Med-Mental-T&P used DeepSeek-V3 to draft and Qwen3-32B to rewrite answers, screening 16,000 theory instructions from textbooks and guidelines and 4,000 practice instructions from more than 600 real case seeds, for 20,000 instruction pairs on traditional Chinese medicine mental disorders. [Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.004)]

</details>

<details>
<summary>2025 · 8</summary>

- [*CCIS*] **面向辨证的大模型微调** Fine-tunes large language models for TCM syndrome differentiation. [[DOI](https://doi.org/10.1007/978-981-96-4298-4_4)]
- [*Expert Systems with Applications*] **针灸临床决策中的大模型补偿机制** Studies compensation mechanisms of large language models in acupuncture clinical decision-making. [[DOI](https://doi.org/10.1016/j.eswa.2025.130870)]
- [*世界科学技术-中医药现代化*] **轻量化中医药古籍大语言模型（LoRA）** Shanghan Lun QA pairs from GPT-4, plus ShenNong and cMedQA2, are used to LoRA-tune five base models and to compare full LoRA with 8-bit and 4-bit QLoRA on Qwen-7B-Chat. That model gains 17.61 BLEU and 21.4 ROUGE-L over its base. No separate model name. [[DOI](https://doi.org/10.11842/wst.20241014001)]
- [*IEEE JBHI*] **用大模型理解中医：机制探索与创新应用** An LLM method for mechanism exploration and downstream application in TCM. [[DOI](https://doi.org/10.1109/jbhi.2025.3631841)]
- [*北京中医药大学学报*] **基于大语言模型与文本嵌入计算的中医证素辨证自动化方法** Instr-MT-TCM, an instruction-tuned TCM embedding model, is paired with an LLM for syndrome-element differentiation. On 1,793 real cases the joint method reaches mean F1 0.927 versus 0.512 for manual labels, and is applied to 48 prostate-cancer cases. [[Paper](https://xb.bucm.edu.cn/zh/article/doi/10.3969/j.issn.1006-2157.2025.08.018/)]
- [*IET*] **基于Llama3的中医大模型** Fine-tunes Llama 3, Phi-3.5, and Mistral on TCM data to improve Chinese TCM language coverage. [[DOI](https://doi.org/10.1049/icp.2025.1017)]
- [*CCIS*] **中医大模型指令微调** Instruction fine-tuning of large language models for TCM. [[DOI](https://doi.org/10.1007/978-981-96-1809-5_34)]
- [*SPIE*] **TCMHP** A large language model for TCM health preservation (preventive care). [[DOI](https://doi.org/10.1117/12.3068496)]

</details>

<details>
<summary>2024 · 4</summary>

- [*JAMIA*] **灵丹 JAMIA：面向临床推理的中医知识编码** JAMIA paper on Lingdan, a TCM large language model for encoding domain knowledge in clinical reasoning tasks. Distinct from the later Digital Chinese Medicine prescription-evaluation paper. [[DOI](https://doi.org/10.1093/jamia/ocae087)]
- [*arXiv*] **中医提示工程框架** Prompt-engineering framework for LLM intelligent understanding in TCM. [[Paper](https://arxiv.org/abs/2410.19451)]
- [*arXiv*] **RLAIF 中医对齐** Enhancing LLMs' TCM capabilities through reinforcement learning from AI feedback. [[Paper](https://arxiv.org/abs/2411.00897)]
- [*Digital Chinese Medicine*] **BSG 中医智能问答** Intelligent QA system for TCM based on a BSG deep-learning model (prescription and materia medica cases). [Hunan University of Traditional Chinese Medicine, Central South University] [[DOI](https://doi.org/10.1016/j.dcmed.2024.04.006)]

</details>

<details>
<summary>2023 · 1</summary>

- [*IEEE BIBM*] **中医疫病防治问答模型** LLM-based QA model for TCM epidemic prevention and treatment. [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385748)]

</details>


</details>

<details>
<summary>Before LLMs (53): 专家系统、舌脉、本体、早期编码器</summary>

<details>
<summary>2020–2022 · 19</summary>

- [*Discover Applied Sciences*] **Mathematical modeling of Chinese medicine by complex-valued five-agent network** Historical anchor: Mathematical modeling of Chinese medicine by complex-valued five-agent network. [National Cheng Kung University] [[DOI](https://doi.org/10.1007/s42452-025-06602-4)]
- [*Lv Q et al., *Signal Transduct Target Ther* 8(1):127*] **TCMBank** Historical anchor: TCMBank. [[DOI](https://doi.org/10.1038/s41392-023-01339-1)]
- [*Interdisciplinary*] **Historical Analysis of Medical Artificial Intelligence Development in China: Research Cent** Historical anchor: Historical Analysis of Medical Artificial Intelligence Development in China: Research Cent. [Okayama University of Science, Okayama University] [[DOI](https://doi.org/10.18926/interdisciplinary/65464)]
- [*Zhang Y et al., *Acta Pharm Sin B* 13(6):2559-2571*] **ETCM v2.0** Historical anchor: ETCM v2.0. [Shanghai Institute of Materia Medica, Guiyang Medical University] [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)]
- [*Scientific Reports*] **Discovering golden ratio in the world’s first five-agent network in ancient China** Historical anchor: Discovering golden ratio in the world’s first five-agent network in ancient China. [National Cheng Kung University] [[DOI](https://doi.org/10.1038/s41598-023-46071-6)]
- [*BioMed Research International*] **乙肝中医 KG 问答系统** Knowledge-graph-based QA system for TCM diagnosis and treatment of viral hepatitis B. [First Affiliated Hospital of Henan University] [[DOI](https://doi.org/10.1155/2022/7139904)]
- [*CCL*] **ZY-BERT** Domain TCM encoder from the TCM-SD paper (~0.4B-token corpus); weights are on cloud drive, with syndrome-differentiation fine-tune code in the repo. Not the same work as arXiv 2411.00897. [[Paper](https://arxiv.org/abs/2203.10839)] [[Published](https://aclanthology.org/2022.ccl-1.80/)] [[Code](https://github.com/Borororo/ZY-BERT)]
- [*BioMed Research International*] **TCMPR 子网术语映射处方推荐** Herb-symptom knowledge graph (~18k entities / ~100k relations) plus subnetwork term mapping and a CNN for prescription recommendation. [[DOI](https://doi.org/10.1155/2022/4845726)]
- [*Digital Health*] **Research and application of tongue and face diagnosis based on deep learning** Historical anchor: Research and application of tongue and face diagnosis based on deep learning. [[DOI](https://doi.org/10.1177/20552076221124436)]
- [*Journal of Ethnopharmacology*] **MGCN** Multi-graph convolutional prescription model on the Treatise on Cold Damage. Symptom features are aggregated on state-element and syndrome graphs, then an MLP predicts the herb set. [[DOI](https://doi.org/10.1016/j.jep.2022.115109)]
- [*Neural Networks*] **KDHR** Knowledge-driven herb recommendation by multi-layer graph-convolution fusion over a TCM knowledge graph. Code is public. [[DOI](https://doi.org/10.1016/j.neunet.2021.11.010)] [[Code](https://github.com/Rao-Yulong/KDHR)]
- [*Evid. Based Complement. Alternat. Med.*] **Deep Learning Multi-label Tongue Image Analysis and Its Application in a Population Underg** Historical anchor: Deep Learning Multi-label Tongue Image Analysis and Its Application in a Population Underg. [[DOI](https://doi.org/10.1155/2022/3384209)]
- [*Digital Chinese Medicine*] **Data-driven based four examinations in TCM: a survey** Historical anchor: Data-driven based four examinations in TCM: a survey. [Beijing University of Civil Engineering and Architecture, University of Maryland, Baltimore, Shandong University] [[DOI](https://doi.org/10.1016/j.dcmed.2022.12.004)]
- [*JMIR Medical Informatics*] **Ensemble Learning-Based Pulse Signal Recognition: Classification Model Development Study** Historical anchor: Ensemble Learning-Based Pulse Signal Recognition: Classification Model Development Study. [[DOI](https://doi.org/10.2196/28039)]
- [*IEEE Trans. Cybernetics*] **Automatic Construction of Chinese Herbal Prescriptions From Tongue Images Using CNNs and A** Historical anchor: Automatic Construction of Chinese Herbal Prescriptions From Tongue Images Using CNNs and A. [South China University of Technology, Guangdong General Hospital] [[DOI](https://doi.org/10.1109/tcyb.2019.2909925)]
- [*BMC Medical Informatics and Decision Making*] **中医临床细粒度 NER 语料** Fine-grained entity-recognition corpus built from TCM clinical records. [Chengdu University of Information Technology] [[DOI](https://doi.org/10.1186/s12911-020-1079-2)]
- [*IEEE ICKG*] **TCMKG** Deep-learning-based TCM knowledge graph platform. [University of Electronic Science and Technology of China] [[DOI](https://doi.org/10.1109/ICBK50248.2020.00084)]
- [*arXiv*] **SMGCN** Syndrome-aware multi-graph convolution for herb recommendation. Besides the symptom–herb graph, it adds symptom and herb co-occurrence graphs, fuses an implicit syndrome vector, then ranks herbs. [[Paper](https://arxiv.org/abs/2002.08575)]
- [*Comput. Struct. Biotechnol. J.*] **Artificial intelligence in tongue diagnosis: Using deep convolutional neural network for r** Historical anchor: Artificial intelligence in tongue diagnosis: Using deep convolutional neural network for r. [Being University of Chinese Medicine, Beijing 100029, China, Beijing University of Posts and Telecommunications, Beijing 100876, China, Beijing Normal University, Beijing 100875, China] [[DOI](https://doi.org/10.1016/j.csbj.2020.04.002)]

</details>

<details>
<summary>2010s · 19</summary>

- [*IEEE Trans. Cybernetics*] **Tooth-Marked Tongue Recognition Using Multiple Instance Learning and CNN Features** Historical anchor: Tooth-Marked Tongue Recognition Using Multiple Instance Learning and CNN Features. [Shanghai University, Shanghai University of Engineering Science] [[DOI](https://doi.org/10.1109/tcyb.2017.2772289)]
- [*JAMIA*] **TCM-BERT** BERT further pretrained on TCM clinical text for five-way disease classification (JAMIA 2019). CKCEST holds copyright; the full 46,205 records are not released, only splits plus drive-hosted fine-tuned weights. [[DOI](https://doi.org/10.1093/jamia/ocz164)] [[Code](https://github.com/yao8839836/tcm_bert)]
- [*Xu HY et al., *Nucleic Acids Res* 47(D1):D976-D982*] **ETCM** Historical anchor: ETCM. [[DOI](https://doi.org/10.1093/nar/gky987)]
- [*BMC Medical Informatics and Decision Making*] **An ontological framework for the formalization, organization and usage of TCM-Knowledge** Historical anchor: An ontological framework for the formalization, organization and usage of TCM-Knowledge. [Leipzig University] [[DOI](https://doi.org/10.1186/s12911-019-0760-9)]
- [*IEEE IAEAC*] **语义中医方剂知识图谱 (Miao et al. 2018)** Semantic TCM prescription knowledge graph built top-down from formula texts. [Communication University of China, Academy of Broadcasting Science] [[DOI](https://doi.org/10.1109/IAEAC.2018.8577236)]
- [*CISP-BMEI*] **Constitution Identification of Tongue Image Based on CNN** Historical anchor: Constitution Identification of Tongue Image Based on CNN. [Beijing University of Technology] [[DOI](https://doi.org/10.1109/cisp-bmei.2018.8633075)]
- [*Artificial Intelligence in Medicine*] **中医养生知识图谱 (Yu et al. 2017)** Large TCM health-preservation knowledge graph integrating terms, literature, and databases, with retrieval, visualization, and recommendation. [[DOI](https://doi.org/10.1016/j.artmed.2017.04.001)]
- [*BioMed Research International*] **Diagnostic Method of Diabetes Based on Support Vector Machine and Tongue Images** Historical anchor: Diagnostic Method of Diabetes Based on Support Vector Machine and Tongue Images. [[DOI](https://doi.org/10.1155/2017/7961494)]
- [*IEEE BIBM*] **中医期刊关系抽取 (Wang & Poon 2016)** Relation extraction from TCM journal full text to support later knowledge-graph construction. [The University of Sydney] [[DOI](https://doi.org/10.1109/BIBM.2016.7822725)]
- [*Ru J et al., *J Cheminform* 6(1):13*] **TCMSP** Historical anchor: TCMSP. [North West Agriculture and Forestry University, Northwest A&F University, Dalian University of Technology, Dalian University] [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- [*Comput. Math. Methods Med.*] **Pulse Waveform Classification Using Support Vector Machine with Gaussian Time Warp Edit Di** Historical anchor: Pulse Waveform Classification Using Support Vector Machine with Gaussian Time Warp Edit Di. [Harbin Ice Flower Hospital, Harbin 150086, China] [[DOI](https://doi.org/10.1155/2014/947254)]
- [*Evid. Based Complement. Alternat. Med.*] **A disturbance rejection framework for the study of traditional Chinese medicine** Historical anchor: A disturbance rejection framework for the study of traditional Chinese medicine. [Cleveland State University] [[DOI](https://doi.org/10.1155/2014/787529)]
- [*Journal of Biomedical Informatics*] **中医症状名识别** Supervised methods for symptom name recognition in free-text TCM clinical records. [Sichuan Agricultural University, Beihua University] [[DOI](https://doi.org/10.1016/j.jbi.2013.09.008)]
- [*Xue R et al., *Nucleic Acids Res* 41(D1):D1089-D1095*] **TCMID** Historical anchor: TCMID. [Shanghai Jiao Tong University, Shanghai Mental Health Center] [[DOI](https://doi.org/10.1093/nar/gks1100)]
- [*Evid. Based Complement. Alternat. Med.*] **Automated Tongue Feature Extraction for ZHENG Classification in Traditional Chinese Medici** Historical anchor: Automated Tongue Feature Extraction for ZHENG Classification in Traditional Chinese Medici. [[DOI](https://doi.org/10.1155/2012/912852)]
- [*Journal of Biomedical Informatics*] **Text mining for traditional Chinese medical knowledge discovery: a survey** Historical anchor: Text mining for traditional Chinese medical knowledge discovery: a survey. [University of Bradford] [[DOI](https://doi.org/10.1016/j.jbi.2010.01.002)]
- [*Journal of Chinese Integrative Medicine*] **Feature extraction and recognition of traditional Chinese medicine pulse based on hemodyna** Historical anchor: Feature extraction and recognition of traditional Chinese medicine pulse based on hemodyna. [[Link](http://www.jcimjournal.com/EN/10.3736/jcim20100802)]
- [*Artificial Intelligence in Medicine*] **Development of traditional Chinese medicine clinical data warehouse for medical knowledge ** Historical anchor: Development of traditional Chinese medicine clinical data warehouse for medical knowledge . [Guang’anmen Hospital] [[DOI](https://doi.org/10.1016/j.artmed.2009.07.012)]
- [*EURASIP J. Adv. Signal Process.*] **Classification of Pulse Waveforms Using Edit Distance with Real Penalty** Historical anchor: Classification of Pulse Waveforms Using Edit Distance with Real Penalty. [[DOI](https://doi.org/10.1155/2010/303140)]

</details>

<details>
<summary>2000s · 10</summary>

- [*IEEE CSIE*] **Syndrome Differentiation in Intelligent TCM Diagnosis System** Historical anchor: Syndrome Differentiation in Intelligent TCM Diagnosis System. [Xiamen University] [[DOI](https://doi.org/10.1109/csie.2009.782)]
- [*Int. J. Information Technology & Decision Making*] **Equilibrium and nonequilibrium modeling of YinYang WuXing for diagnostic decision support ** Historical anchor: Equilibrium and nonequilibrium modeling of YinYang WuXing for diagnostic decision support . [[DOI](https://doi.org/10.1142/s0219622009003521)]
- [*IEEE ITME*] **Traditional Chinese medical diagnosis based on fuzzy and certainty reasoning** Historical anchor: Traditional Chinese medical diagnosis based on fuzzy and certainty reasoning. [Memorial University of Newfoundland] [[DOI](https://doi.org/10.1109/itme.2008.4743874)]
- [*WWW* (demo/industrial)*] **Information retrieval and knowledge discovery on the semantic web of traditional Chinese m** Historical anchor: Information retrieval and knowledge discovery on the semantic web of traditional Chinese m. [[DOI](https://doi.org/10.1145/1367497.1367668)]
- [*Journal of Chinese Integrative Medicine*] **Establishment of a fuzzy mathematical model for syndrome differentiation of gastric cancer** Historical anchor: Establishment of a fuzzy mathematical model for syndrome differentiation of gastric cancer. [[Link](http://www.jcimjournal.com/EN/10.3736/jcim20081104)]
- [*IEEE BMEI*] **Building Clinical Data Warehouse for Traditional Chinese Medicine Knowledge Discovery** Historical anchor: Building Clinical Data Warehouse for Traditional Chinese Medicine Knowledge Discovery. [Guang’anmen Hospital] [[DOI](https://doi.org/10.1109/bmei.2008.83)]
- [*IEEE SITIS*] **A Novel Computerized Method Based on Support Vector Machine for Tongue Diagnosis** Historical anchor: A Novel Computerized Method Based on Support Vector Machine for Tongue Diagnosis. [City University of Hong Kong] [[DOI](https://doi.org/10.1109/sitis.2007.115)]
- [*Artificial Intelligence in Medicine*] **Knowledge discovery in traditional Chinese medicine: State of the art and perspectives** Historical anchor: Knowledge discovery in traditional Chinese medicine: State of the art and perspectives. [[DOI](https://doi.org/10.1016/j.artmed.2006.07.005)]
- [*Information Sciences*] **YinYang bipolar logic and bipolar fuzzy logic** Historical anchor: YinYang bipolar logic and bipolar fuzzy logic. [Georgia Southern University, The University of Texas at Austin] [[DOI](https://doi.org/10.1016/j.ins.2003.05.010)]
- [*Artificial Intelligence in Medicine*] **Ontology development for unified traditional Chinese medical language system** Historical anchor: Ontology development for unified traditional Chinese medical language system. [Sichuan Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.artmed.2004.01.014)]

</details>

<details>
<summary>1970s–1990s · 5</summary>

- [*Complementary Therapies in Medicine*] **A computer model of the “five elements” theory of traditional Chinese medicine** Historical anchor: A computer model of the “five elements” theory of traditional Chinese medicine. [University of Verona, University of Perugia] [[DOI](https://doi.org/10.1016/S0965-2299(98)80005-8)]
- [*Physica Scripta*] **Functional structure model of human body and Yinyang-Wuxing equations** Historical anchor: Functional structure model of human body and Yinyang-Wuxing equations. [University of Science and Technology of China] [[DOI](https://doi.org/10.1088/0031-8949/36/6/015)]
- [*Fuzzy Sets and Systems*] **Fuzzy match and floating threshold strategy for expert system in traditional Chinese medicine** Historical anchor: Fuzzy match and floating threshold strategy for expert systems in traditional Chinese medicine. [Beijing Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/0165-0114(85)90052-1)]
- [*Hospital historical archive*] **Guan Youbo liver-disease diagnosis and treatment program** Historical anchor: an early computer-based expert system encoding renowned TCM physician Guan Youbo's approach to liver disease. [[Link](https://www.bjzhongyi.com/gzb_mygs_detail/4656.html)]
- [*Computers and Biomedical Research*] **An artificial intelligence program to advise physicians regarding antimicrobial therapy** Historical anchor: An artificial intelligence program to advise physicians regarding antimicrobial therapy. [Stanford University] [[DOI](https://doi.org/10.1016/0010-4809(73)90029-3)]

</details>


</details>

## Datasets

Grouped by use. Official sites that are down are marked “site down”; portals that are up but broken are marked “site issue”. Both stay listed with the paper or a mirror. For a longer note on benches, see [Datasets](wiki/Datasets.md) and [Benchmarks](wiki/Benchmarks.md).

<details>
<summary>Curated lists (3)</summary>

- **awesome_Chinese_medical_NLP** — Curated list of Chinese medical NLP resources: terminologies, corpora, word vectors, pretrained models, KGs, NER and QA (incl. CBLUE). [[Resources](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)]
- **CPM Chinese patent medicine dataset** — Living large-scale public Chinese patent medicine data accompanying RAG-CPMF. [[Data](https://gitee.com/tcmdoc/cpm)] [[Paper](https://doi.org/10.1016/j.phrs.2025.107883)]
- **内蒙古自治区民族药目录** — Public ethnic-medicine catalogue PDF from the Inner Mongolia Healthcare Security Administration, mainly finished Mongolian formulas. The government filename is dated 25 December 2023. The extracted text is titled the Inner Mongolia ethnic-medicine catalogue and notes that listed drugs are managed as class B. It is a reimbursement list, not a research compound database. The 2026 Mongolian-medicine knowledge-base launch has no open platform URL. [[Catalogue](https://ylbzj.nmg.gov.cn/zwgk/zfxxgk/fdzdgknr/bmwj/202312/P020231225623619008689.pdf)]

</details>

<details>
<summary>Formula / extract databases (39)</summary>

- **中药扰动转录组图谱** — Harmonized transcriptomic atlas of traditional Chinese medicine perturbations, assembled from public treatment experiments. [[Paper](https://doi.org/10.1038/s41597-026-06988-9)]
- **TCMDI** — Benchmark for predicting contraindicated interactions between traditional Chinese medicines and drugs. [[Dataset](https://github.com/hellowangqian/TCMDI)]
- **TCM-QM** — Gas-phase DFT descriptors for 3,196 TCM-related molecules, with 16,918 deduplicated herb–molecule provenance links. [[Dataset](https://zenodo.org/records/22173180)]
- **TCM-MS2Link** — AI-ready dataset joining curated herb–compound links (TCM-MolLink) with MS/MS spectra. [[Dataset](https://doi.org/10.57760/sciencedb.31921)]
- **Cross-linguistic TCM Formula Names** — Cross-linguistic table of TCM formula names in Chinese, Japanese Kampo, Korean Han medicine, and English, compiled from official formularies and clinical references in Taiwan. [[Dataset](https://zenodo.org/records/18724305)]
- **CHM-315** — Fine-grained Chinese herbal-medicine image set with 315 categories and 126,000 images, 400 images per category. [[Dataset](https://doi.org/10.6084/m9.figshare.32745123)]
- **Baize TCM Botanical Origin Images** — Medicinal-plant origin images for Baize Traditional Chinese Medicine, covering habitats, original plants, and medicinal parts, with Chinese and Latin identification based on the Chinese Pharmacopoeia, Flora of China, and the Engler system. [[Dataset](https://doi.org/10.57760/sciencedb.41638)]
- **传统方剂—疾病关系标注语料** — Annotated corpus of traditional formula–disease relations in biomedical articles. Formulas are herb combinations prepared under traditional medicine principles. [[Paper](https://doi.org/10.1038/s41597-025-04377-2)]
- **TCMP-300** — Image dataset of traditional Chinese medicinal plants for plant recognition. [[Paper](https://doi.org/10.1038/s41597-025-05522-7)] [[Code](https://github.com/winycg/TCMP-300)]
- **HERB 2.0** — Evidence-centered TCM resource integrating clinical trials, meta-analyses, high-throughput experiments, literature, and a knowledge graph. [[Website](http://herb.ac.cn/v2)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11701625/)] [[DOI](https://doi.org/10.1093/nar/gkae1037)]
- **TCMSSD** — Syndrome-standardization database reported by authors at Zhejiang Chinese Medical University. The paper reports 624 syndromes, 133,518 prescriptions, 8,073 diseases, 8,259 herbs, 43,413 ingredients, and 17,602 targets. The site opens and its front-end script contains syndrome and TCMSSD content; without JavaScript the page is empty. No full-database download entry was found. [[Website](http://tcmssd.ratcm.cn/)] [[DOI](https://doi.org/10.1016/j.phymed.2024.155486)]
- **TCMPG 2.0** — Traditional Chinese medicine plant-genome database maintained by Chengdu University of Traditional Chinese Medicine and collaborators. The current homepage lists 274 plants, 324 genomes, 414 herbs, and 13,809 ingredients, with BLAST, JBrowse, and other tools. A 2024 paper describes the 2.0 upgrade. The site is open for browsing and analysis; a full packaged dump was not verified. [[Website](https://cbcb.cdutcm.edu.cn/TCMPG2/)] [[DOI](https://doi.org/10.48130/mpb-0024-0004)]
- **CMAUP** — BIDD landscape of multi-target activities, pathways, and diseases for useful plants including TCM herbs; 2024 update, downloadable from the official site. [[Website](https://www.bidd.group/CMAUP/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767869/)] [[DOI](https://doi.org/10.1093/nar/gkad921)]
- **BATMAN-TCM 2.0** — Known and predicted TCM ingredient–target protein interactions, with greatly expanded TTI coverage and target-to-ingredient search. [[Website](http://bionet.ncpsb.org.cn/batman-tcm/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767940/)] [[DOI](https://doi.org/10.1093/nar/gkad926)]
- **TCMBank** — Large downloadable herb–ingredient–target–disease resource with literature-mining updates after manual checks. [[Website](http://tcmbank.cn/)] [[DOI](https://doi.org/10.1038/s41392-023-01339-1)]
- **ITCM** — Integrated formula/herb/ingredient/target platform plus 1,488 pharmacotranscriptomic profiles for 496 TCM ingredients (expression data also on Synapse). [[Website](http://itcm.biotcm.net/)] [[DOI](https://doi.org/10.1093/bib/bbad027)]
- **ETCM 2.0** — Encyclopedia of TCM formulas, patent drugs, materia medica, and ingredients with target prediction and multi-scale networks; v1 site remains online. [[Website](http://www.tcmip.cn/ETCM2/front/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10326295/)] [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)]
- **DCABM-TCM** — Literature-mined blood constituents and metabolites of TCM prescriptions and herbs, with experimental detection conditions (~1,816 structured absorbed constituents). [[Website](http://bionet.ncpsb.org.cn/dcabm-tcm/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10428213/)]
- **藏药材资源数据库** — Tibetan materia-medica list published by the Key Laboratory of Tibetan Medicine Research at the CAS Northwest Institute of Plateau Biology. The page is a table of Chinese name, Latin name, drug name, and part used, and it states that there are 15 pages. Entry paths are dated March–April 2022. It is a crude-drug list, not a compound–target database. [[Website](https://nwipb.cas.cn/zy/zyc/index.html)]
- **LTM-TCM** (site down) — Symptom–prescription–plant–ingredient–target platform linking 14 source databases plus clinical and classical records (~48k formulas). Official Tasly cloud no longer resolves; verify via the paper DOI. [[Original site](http://cloud.tasly.com/#/tcm/home)] [[DOI](https://doi.org/10.1016/j.phrs.2022.106185)]
- **HIT 2.0** (site issue) — Manually curated herbal-ingredient–target activity pairs (~1,237 ingredients / 2,208 targets, 2000–2020 literature). Portal opens; the analysis backend port is currently down (marked site issue). [[Website](http://hit2.badd-cao.net/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728248/)] [[DOI](https://doi.org/10.1093/nar/gkab1011)]
- **SuperTCM** (site down) — Charité biocultural TCM resource linking drugs, botanical species, ingredients, targets, KEGG pathways, and diseases (~6,516 drugs). Official tcm.charite.de no longer resolves. [[Original site](http://tcm.charite.de/supertcm)] [[Paper](https://europepmc.org/article/MED/34656056)] [[DOI](https://doi.org/10.1016/j.biopha.2021.112315)]
- **TCMIO** — Immuno-oncology TCM database of prescriptions, herbs, ingredients, targets, and pathways, with downloads and a REST API. [[Website](http://tcmio.xielab.net/)] [[Data](http://tcmio.xielab.net/download)] [[DOI](https://doi.org/10.3389/fphar.2020.00439)]
- **Sowa Rigpa Materia Medica Dataset** — Open Data in Brief table of Latin identifications for commonly used Sowa Rigpa materia medica. The paper says about 700 commonly used items were selected from the Four Medical Treatises and Gawé Dorjé’s classification, with Tibetan script, Wylie transliteration, and Latin names; the supplement is published with the article. Affiliations include the School of Tibetan Medicine at Gansu University of Chinese Medicine, the College of Pharmacy at Qinghai Nationalities University, and the ethnic-medicine center at Chengdu University of Traditional Chinese Medicine. [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC7689029/)] [[DOI](https://doi.org/10.1016/j.dib.2020.106498)]
- **SymMap 2.0** — Herb–TCM symptom–modern symptom–ingredient–target–disease maps, expanded with newer pharmacopoeia records and downloadable relationship tables. [[Website](http://www.symmap.org/)] [[Data](http://www.symmap.org/download/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323958/)]
- **傣药基原植物数据库** (site issue) — Dai medicinal-plant source database on the Chinese Union of Botanical Gardens platform, from Xishuangbanna Tropical Botanical Garden, CAS. The home page is copyrighted 2018 and describes Dai medicine’s four towers, five aggregates, and antidote theory. The species-list URL returns a redirect notice, and no anonymously browsable species catalogue was confirmed. [[Website](https://espc.cubg.cn/daim/index/index.html)]
- **YaTCM** (site down) — About 1,813 prescriptions, 6,220 herbs, and 47k natural products with target/pathway tools. Nankai site currently returns 403; verify via the open-access paper. [[Original site](http://cadd.pharmacy.nankai.edu.cn/yatcm/home)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6280608/)] [[DOI](https://doi.org/10.1016/j.csbj.2018.11.002)]
- **TCMID 2.0** (site down) — Integrative formula–herb–ingredient–target database (distinct from NUS TCM-ID). Original megabionet site is down; verify via Zenodo extract and the NAR paper. [[Original site](http://www.megabionet.org/tcmid/)] [[Data](https://zenodo.org/records/8066910)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5753259/)] [[DOI](https://doi.org/10.1093/nar/gkx1028)]
- **TCMAnalyzer** (site down) — RCDD chemo-/bioinformatics service for formula/herb/ingredient networks and scaffold search (~1,493 formulas, 618 herbs). Official rcdd.org.cn currently times out. [[Original site](http://www.rcdd.org.cn/tcmanalyzer)] [[Paper](https://pubmed.ncbi.nlm.nih.gov/29420025/)] [[DOI](https://doi.org/10.1021/acs.jcim.7b00549)]
- **中药方剂图像数据库** — Formula image library from the School of Chinese Medicine, Hong Kong Baptist University, openly browsing composition, actions, indications, and images. The browse page shows about 182 formulas, and the public counter starts in November 2017. It is an online reference, not a bulk formula-table download. [[Website](https://library.hkbu.edu.hk/electronic/libdbs/cmfid/)]
- **TCM-Mesh** (site down) — Herb–compound–gene–disease network with toxicity/side-effect records (~6,235 herbs). Official portal currently returns 403; verify via the open paper. [[Original site](http://mesh.tcm.microbioinformatics.org/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5460194/)] [[DOI](https://doi.org/10.1038/s41598-017-03039-7)]
- **TM-MC** (site down) — KIOM literature-derived Northeast Asian medicinal-material–compound database; the 2015 release covers ~536 materials, and the 2024 2.0 paper expands to ~34k compounds. Official site currently times out. [[Original site](http://informatics.kiom.re.kr/compound/)] [[DOI](https://doi.org/10.1186/s12906-015-0758-5)] [[2.0 paper](https://doi.org/10.1186/s12906-023-04331-y)]
- **CEMTDD** (site down) — Ethnic-minority herbal–compound–target–disease resource (~621 herbs, mainly Uygur/Kazakh). Original cemtdd.com now hosts something else; verify via the PMC paper. [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627337/)] [[DOI](https://doi.org/10.18632/oncotarget.3789)]
- **TCMSP** — Herb–ingredient–target–disease networks with ADME parameters; public site is TCMSP 2.3 with downloadable relationship tables. [[Website](https://www.tcmsp-e.com/tcmsp.php)] [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- **中药材图像数据库** — Chinese medicinal-material image library from the School of Chinese Medicine, Hong Kong Baptist University. The library page states more than 420 commonly used crude drugs, with source, origin, morphology, properties, indications, and high-resolution images, searchable by Chinese, Latin, and English names. It has been online since 2013 and is openly browsable, not a bulk download. [[Website](https://library.hkbu.edu.hk/electronic/libdbs/mmd/)]
- **CVDHD** (site down) — Cardiovascular herbal database of 3D compound structures, targets, and pathways for virtual screening and network pharmacology. Original Peking University site currently times out. [[Original site](http://pkuxxj.pku.edu.cn/CVDHD)] [[DOI](https://doi.org/10.1186/1758-2946-5-51)]
- **TCM Database@Taiwan** (site down) — About 20k isolated-compound 2D/3D structures from 453 TCM materials for virtual screening. Original tcm.cmu.edu.tw is unreachable; verify via the PLOS paper. [[Original site](http://tcm.cmu.edu.tw/)] [[Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0015939)] [[DOI](https://doi.org/10.1371/journal.pone.0015939)]
- **TCMGeneDIT** (site down) — Text-mined associations among TCM, genes, diseases, effects, and ingredients, with pathway and PPI links. Official NTU site no longer resolves. [[Original site](http://tcm.lifescience.ntu.edu.tw/)] [[Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2584015/)] [[DOI](https://doi.org/10.1186/1472-6882-8-58)]
- **TCM-ID** — NUS BIDD formula–herb–ingredient–target resource covering pharmacopoeia, classical, and CFDA-approved prescriptions; not the same database as TCMID 2.0. [[Website](https://www.bidd.group/TCMID/)]

</details>

<details>
<summary>Clinical structured / prescription sets (6)</summary>

- **古今医案云平台** — Case search, structuring, and mining platform of the Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences. An institute news item on 2026-09-20 states that the current resource holds more than 1.1 million structured historical and modern cases, plus 19.63 million analysis records, with about 53,000 registered users. Registration or institutional login is required, and no public bulk download was found. Some campus trial notes still say about 500,000 cases. [[Website](https://www.yiankb.com/)]
- **胆石症中医证候代谢组** — Serum and urine metabolomics for two TCM syndromes in cholelithiasis: liver qi stagnation and liver-gallbladder damp-heat. [[Paper](https://doi.org/10.1038/s41597-025-06537-w)]
- **六经辨证数据集** — Traditional Chinese medicine dataset for six-meridian syndrome differentiation. [[Dataset](https://github.com/JustinWYJ/TCMdataset)]
- **TCM-Lung** — Pulmonary-disease cases from FAH-HUCM (14,948 processed; 4,484 encoded public rows of symptom/syndrome/method/prescription IDs). Full names on request. Not the same resource as TCMNSCLC. [[Code](https://github.com/2020MEAI/PresRecST)] [[Paper](https://doi.org/10.1093/jamia/ocae066)]
- **Famous Old TCM Doctors Cases** — Outpatient cases from Contemporary Famous Old Chinese Medicine Doctors' Typical Cases Collection; the card says each case includes the illness description, syndrome differentiation, and prescriptions. [[Dataset](https://huggingface.co/datasets/TCMLM/real_clinical_cases_of_Famous_Old_TCM_Doctors)]
- **TCM-PD** — Yao et al. TKDE 2018 prescription topic-model set (98,334 raw / 33,765 processed symptom–herb ID pairs). CKCEST copyright, research use only. PresRecST's prescript_1195.csv is a reproduction table. [[Code](https://github.com/yao8839836/PTM)] [[DOI](https://doi.org/10.1109/TKDE.2017.2787158)]

</details>

<details>
<summary>General Chinese medical data (14)</summary>

- **四模型中文医学文献标引测试集** — Key-information extraction and summary scores from four large models on 100 Chinese medical research articles. [[Dataset](https://doi.org/10.57760/sciencedb.o00130.03231)]
- **PromptCBLUE** — CBLUE's 16 Chinese medical NLP tasks rewritten as generative instructions; an early unified Chinese medical LLM leaderboard (CCKS 2023). [[Code](https://github.com/michael-wzhu/PromptCBLUE)]
- **Huatuo-26M** — Largest open Chinese medical QA resource (~26M pairs from encyclopedias, KGs, and consults); Huatuo-Lite is the usual SFT/RAG subset. [[Paper](https://arxiv.org/abs/2305.01526)] [[Published](https://aclanthology.org/2025.findings-naacl.211/)] [[Code](https://github.com/FreedomIntelligence/Huatuo-26M)] [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/Huatuo26M-Lite)]
- **DISC-Med-SFT** — Fudan DISC medical-dialogue SFT set (~470k examples from KG triples and reconstructed consults; no preference data). [[Dataset](https://huggingface.co/datasets/Flmc/DISC-Med-SFT)] [[Paper](https://arxiv.org/abs/2308.14346)]
- **ChiMed (Qilin)** — Qilin-Med's ~3GB Chinese medical corpus (CPT/SFT/DPO); not the same resource as the ChiMed 2.0 pretraining set. [[Dataset](https://huggingface.co/datasets/williamliu/ChiMed)] [[Paper](https://arxiv.org/abs/2310.09089)]
- **CMExam** — Chinese medical licensing-exam set (~68k annotated items) used as a knowledge-recall baseline by Chinese medical and TCM LLMs. [[Paper](https://arxiv.org/abs/2306.03030)] [[Code](https://github.com/williamliujl/CMExam)]
- **CMB** — FreedomIntelligence comprehensive Chinese medical benchmark (CMB-Exam ~280k items plus CMB-Clin cases); the most common non-TCM comparison board in TCM LLM papers. [[Paper](https://arxiv.org/abs/2308.08833)] [[Published](https://aclanthology.org/2024.naacl-long.343/)] [[Code](https://github.com/FreedomIntelligence/CMB)] [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/CMB)]
- **IMCS-21** — About 4,116 pediatric online consults annotated for entities, intents, symptoms, and reports; later wired into four CBLUE dialogue tasks. [[DOI](https://doi.org/10.1093/bioinformatics/btac817)] [[Code](https://github.com/lemuria-wchen/imcs21)] [[CBLUE tasks](https://github.com/lemuria-wchen/imcs21-cblue)]
- **CBLUE** — Chinese biomedical NLU benchmark (NER, relations, diagnosis normalization, classification); the source-task suite behind PromptCBLUE, with a Tianchi submission portal. [[Paper](https://aclanthology.org/2022.acl-long.544/)] [[Code](https://github.com/CBLUEbenchmark/CBLUE)]
- **MedDialog** — Large doctor–patient dialogue corpus (about 1.1M Chinese encounters) used for multi-turn Chinese medical fine-tuning. [[Paper](https://arxiv.org/abs/2004.03329)] [[Code](https://github.com/UCSD-AI4H/Medical-Dialogue-System)]
- **webMedQA** — Early Chinese non-factoid medical QA from health-consult sites (~63k questions, one positive and four negative answers each). [[DOI](https://doi.org/10.1186/s12911-019-0761-8)] [[Code](https://github.com/hejunqing/webMedQA)]
- **CMeKG** — Chinese medical knowledge graph of diseases, drugs, and symptoms; main source for BenCao/HuaTuo and ChatGLM-Med instruction data. Official portal is unstable; verify via the tools repo. [[Code](https://github.com/king-yyf/CMeKG_tools)]
- **cMedQA2** — Chinese community medical QA (~108k questions / 200k answers), a common source for BianQue-style SFT mixtures. [[Code](https://github.com/zhangsheng93/cMedQA2)]
- **cMedQA** — Chinese community medical QA-matching set (repo table ~54k questions / 102k answers; non-commercial research). Paper DOI matches the README; see cMedQA2 for the later release. [[Code](https://github.com/zhangsheng93/cMedQA)] [[Paper](https://doi.org/10.3390/app7080767)]

</details>

<details>
<summary>East Asian traditional medicine (16)</summary>

- **VTM-TDA Benchmark** — A FAIR computational benchmark of Vietnamese traditional medicine digitized from Do Tat Loi's pharmacopoeia, with 724 harmonized botanical entities and 1,635 historical prescriptions. [[Dataset](https://zenodo.org/records/23075405)]
- **TreeProbe** — Tibetan-medicine benchmark for measuring cultural bias in large language models. [[Paper](https://arxiv.org/abs/2608.00640)]
- **Korean Medicine Embedding Dataset** — Query–positive–negatives (~113k pairs) built from Korean-medicine terms and an ontology, for embedding fine-tunes such as BGE-M3. [[Dataset](https://huggingface.co/datasets/cnupo23/korean-medicine-embedding-dataset)]
- **KampoBench** — Physician-reviewed Kampo consultation benchmark with 74 scenarios and 310 dialogue-level criteria. [[Paper](https://doi.org/10.64898/2026.10.07.26365005)]
- **HerbPairIAM** — Data and model artifacts for attributing adverse-reaction signals to components of multi-component Kampo medicines, with a zip archive and README on Zenodo. [[Dataset](https://zenodo.org/records/19326537)]
- **VietMedKG** — Knowledge graph and benchmark for traditional Vietnamese medicine. [[Dataset](https://github.com/HySonLab/VietMedKG)]
- **KampoDB** — Kampo mechanism database maintained by the Institute of Natural Medicine, University of Toyama. It links formulas, crude drugs, natural compounds, and target proteins, including known interactions and docking predictions. The about page currently lists 298 Kampo formulas, 180 crude drugs, 3,002 natural compounds, 62,906 proteins or genes, and 3,063,505 docking results. The 2018 Scientific Reports paper is the citation; the site news records a renewal on 15 July 2021. [[Website](https://wakanmoview.inm.u-toyama.ac.jp/kampo/)] [[About](https://wakanmoview.inm.u-toyama.ac.jp/kampo/about/)] [[DOI](https://doi.org/10.1038/s41598-018-29516-1)]
- **韩医药素材银行药材目录 (KMMB)** — Searchable crude-drug holdings of the Korean Medicine Material Bank at the National Institute for Korean Medicine Development. The open herb page reports 691 results, with name, synonym, scientific name, botanical source, and reacting enzymes. An institute project file records that the bank was formed on 1 January 2016 by merging the natural-substance bank and the herbal biomaterial bank. [[Herbs](https://kminfra.nikom.or.kr/kmmb/module/herbs/index.do?menu_idx=11)]
- **KMCRIC** — Data portal of the Korean Medicine Convergence Research Information Center at Kyung Hee University. The data-center page lists an evidence-based Korean-medicine literature set of systematic reviews, RCTs, and mechanism studies published since 2010; an herb-interaction set based on Natural Standard; acupoint videos made from the 2008 WHO Western Pacific standard locations; and a crude-drug update built with the Kyung Hee and Chungbuk pharmacy faculties. The director’s biography says the directorship began in 2013. [[Data](https://www.kmcric.com/database/data_main)] [[About](https://www.kmcric.com/about/head_of_centre)]
- **药用植物综合信息数据库 (MPDB)** — Comprehensive medicinal-plant database of the NIBIOHN Research Center for Medicinal Plant Resources. The home page describes medicinal plants, crude drugs, constituents and genes, cultivation, and internal morphology, plus measured data for representative crude drugs in Japanese circulation. The footer copyright is 2012–2025, funded by a MHLW research grant. Separate Kampo-formula and Japanese Pharmacopoeia crude-drug lists are online. [[Website](https://mpdb.nibn.go.jp/)] [[Formulas](https://mpdb.nibn.go.jp/mpdb-bin/list_data.cgi?category=syohou&lang=)] [[Crude drugs](https://mpdb.nibn.go.jp/mpdb-bin/list_data.cgi?category=jplist&lang=ja)]
- **TradMPD** — Traditional Medical and Pharmaceutical Database at the University of Toyama Institute of Natural Medicine. The English about page says it was supported by a MEXT regional innovation cluster grant for 2008–2012. It covers crude-drug identity, properties, Kampo composition and indications, and more than 10,000 Kampo papers. The Wakanyaku Library holds nearly 80 compounds plus chemical and bioassay data for hot-water extracts of 80 crude drugs and 80 Kampo extracts, with bioassay downloads from 2024. [[Website](https://dentomed.toyama-wakan.net/en/)] [[About](https://dentomed.toyama-wakan.net/index_en)]
- **KNApSAcK KAMPO** — NAIST Kampo public database (~1,581 formulas, 278 crude drugs), downloadable from the NBDC life-science archive. [[Dataset](https://dbarchive.biosciencedbc.jp/data/knapsack-kampo/)] [[DOI](https://doi.org/10.1093/pcp/pcr165)]
- **OASIS (KIOM)** — KIOM traditional-medicine literature portal for Korean-medicine papers and herbal resources. [[Website](https://oasis.kiom.re.kr/)]
- **KTKP Traditional Medicine** — Korean-medicine slice of the Korean Traditional Knowledge Portal, run for the Ministry of Intellectual Property. The English introduction says the database was compiled from traditional Korean medicine literature in 2005–2007 and opened for search in December 2007. The same page currently counts 5,500 herbs, 7,103 prescriptions, and 12,500 diseases, linked to effects, indications, formulas, and patent classes. [[About](https://koreantk.com/ktkp2014/about/introduction.page)] [[Herbs](https://koreantk.com/ktkp2014/medicine/list-by-act-part.page)] [[Formulas](https://koreantk.com/ktkp2014/prescription/list-by-index.page)] [[Patterns](https://koreantk.com/ktkp2014/disease/list-by-index.page)]
- **EKAT** — Evidence Reports of Kampo Treatment, a structured-abstract database from the Japan Society for Oriental Medicine EBM committee. The site says it has been free and updated since 2007. It covers RCTs and meta-analyses of Kampo products still on the market, limited to reports since 1986 that used the same quality as marketed products; decoctions are excluded because product quality is unknown. Japanese and English editions are provided, and the Association of Korean Medicine has a Korean translation. [[Website](https://www.jsom.or.jp/ebm/ekat/)]
- **ETHMEDmmm** — Ethnomedicine specimen database of the Museum of Materia Medica at the University of Toyama. The home-page table lists 461 kinds and 8,942 Japanese–Chinese crude-drug specimens, opened in Japanese in April 2000. The same site also has an English crude-drug list and separate Unani, Thai, Ayurvedic, and Indonesian collections. The latest note is a version-7 rebuild on 30 March 2018. [[Website](https://ethmed.toyama-wakan.net/)]

</details>

<details>
<summary>Books / pretraining corpora (9)</summary>

- **tc_medical_base** — Clause-level corpus of five classical TCM texts totaling 3,569 clauses with sentence-BERT embeddings: Song-edition Shanghan Lun, Guilin Shanghan Zabing Lun, Jingui Yuhan Jing, Jingui Yaolue, and Fu Qingzhu Nüke. [[Dataset](https://huggingface.co/datasets/huckiyang/tc_medical_base)]
- **classical-tcm-canon** — Full-text digitizations of the TCM canon: Neijing, Nanjing, Shanghan Lun, Jingui Yaolue and warm-disease classics. [[Dataset](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)]
- **Traditional-Chinese-Medicine-Dataset-Pretrain** — High-quality TCM pretraining dataset from non-Internet sources (~1GB; clinical cases, classics, encyclopedia), 99% simplified Chinese. [[Dataset](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)]
- **TCM-Pretrain-Data-ShizhenGPT** — ShizhenGPT pretraining corpus (15B+ tokens reported in the paper — Stage-1 text 11.92B incl. 6.3B TCM, plus Stage-2 multimodal ~3.6B). [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- **TCM-Ancient-Books** — A corpus of nearly 700 TCM ancient-book texts. [[Dataset](https://github.com/xiaopangxia/TCM-Ancient-Books)]
- **ChiMed 2.0** — Upgraded Chinese medical pretraining dataset covering TCM corpora for LLM pretraining. [[Paper](https://arxiv.org/abs/2507.15275)]
- **国医典藏** — Image-and-text library of historical Chinese medical books from the Institute of Information on Traditional Chinese Medicine and its library, CACMS. The current entry is the version-4 site. Public descriptions put the holdings at roughly 2,500 to 3,000 titles from pre-Qin through the late Qing and Republican periods, with basic, advanced, and controlled-vocabulary search and image-text viewing. Access is by campus network or registration, not a public bulk download. [[Website](https://gydc-v4.cintcm.cn/)]
- **国家中医药古籍数字图书馆** — Ancient-book and traditional-knowledge portal started in 2022 by the Institute of Information on Traditional Chinese Medicine, CACMS. It has halls for classical texts, Republican-era documents, and bibliographic catalogs, and links out to reading systems including Guoyi Diancang. The portal opens; full text is reached through the sub-libraries and is not a public bulk download. [[Website](http://www.cintcm.com/)]
- **中华医典** — Commercial sales site (Feixiong Technology) for the Zhonghua Yidian electronic collection. The site states 1,156 classical titles and about 450 million characters, a 2000 national electronic-publication nomination, and Qiu Peiran as editorial reviewer and title writer. Edition 6 is a web version used after purchase and registration, not a public download. [[Website](https://www.zhyd1999.com/)]

</details>

<details>
<summary>Benchmarks (30)</summary>

- **TCM-RobustSDT** — TCM-RobustSDT: a robustness benchmark dataset for LLM clinical reasoning in TCM (Figshare). [[Dataset](https://doi.org/10.6084/m9.figshare.33054974)]
- **辨证论治基准数据集** — Scientific Data benchmark for syndrome differentiation and treatment with large language models. [[Paper](https://doi.org/10.1038/s41597-026-07587-4)]
- **病理标注舌象数据集** — Tongue-image dataset with pathological annotations for AI-assisted TCM diagnosis. [[Paper](https://doi.org/10.62762/bish.2026.303296)]
- **病机思维链证候识别数据** — Syndrome-manifestation cases with gold labels and model predictions, built under pathogenesis reasoning chain-of-thought supervision. [[Dataset](https://doi.org/10.57760/sciencedb.35044)]
- **WHO TCM Terminology LLM Evaluation Set** — Evaluation set for using large language models as judges of TCM terminology, containing 376 contrasts from the 2022 WHO International Standard Terminologies on Traditional Chinese Medicine. [[Dataset](https://zenodo.org/records/21852353)]
- **TongueBench** — Quality-controlled tongue-image set of 2,694 photographs with file-level metadata; the open file is TongueBench Dataset.zip. [[Dataset](https://zenodo.org/records/20701288)]
- **TCMEval-PA** — 328 multiple-choice items on prescription normative quality and safety auditing. [[Paper](https://doi.org/10.1038/s41597-025-06387-6)] [[Data](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[Code](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)]
- **TCMClinicalReason-Bench** — 2,000 multicenter records for reasoning from pathogenesis to prescription. [[Paper](https://arxiv.org/abs/2610.04215)]
- **TCM-AQA61 / CME-AQA** — Dual-view acupuncture and Tuina action-quality videos from 61 subjects each (first- and third-person), with expert categorical and continuous ratings; paired with the CME-AQA cross-view multimodal assessment framework. [[Paper](https://arxiv.org/abs/2606.28104)] [[DOI](https://doi.org/10.1109/TNSRE.2026.3705649)] [[Code](https://github.com/FrancisXZhang/cme-aqa)] [[Data](https://researchdata.durham.ac.uk/collections/r1jm214p229)]
- **TCM Term Prompt-Language Responses** — 972 model responses for 18 TCM terms across six general-purpose models, three prompt languages (Chinese, English, and Malay), and three runs, with WHO 2007 and 2022 terminology references. [[Dataset](https://zenodo.org/records/22208549)]
- **LingLan** — LingLan large multi-task TCM evaluation benchmark (2026). [[Dataset](https://github.com/TCMAI-BJTU/LingLan)] [[Paper](https://arxiv.org/abs/2602.01779)]
- **ZhongJing-OMNI** — ZhongJing-OMNI multimodal TCM eval (including tongue). [[Dataset](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]
- **TongueProjectTCM Color Classification** — TongueProjectTCM tongue-image set whose card lists images and integer labels, with 807 training and 121 validation examples. [[Dataset](https://huggingface.co/datasets/TongueProjectTCM/color-classification-opensource)]
- **TongueDx** — Public remote-tongue dataset: 5,109 images from 4,650 subjects, eight binary attributes (pale, red tip/side, red spots, ecchymosis, cracks, tooth marks, thick fur, yellow fur), plus age and sex. The repository is downloadable. This is not the later TongueDx2 ablation paper. [[Dataset](https://github.com/tonguedx/tonguedx)] [[Paper](https://arxiv.org/abs/2501.03053)]
- **TongueAtlas-4K** — A 4,000-image clinical tongue benchmark with certified TCM expert labels for 22 appearance categories, released for MIRNet (AAAI 2026, to appear). The Zenodo record is restricted. [[Dataset](https://zenodo.org/records/17557646)]
- **TCMEval-SDT** — TCMEval-SDT: a benchmark of 300 syndrome-diagnosis cases (web, classical texts, hospital records) for evaluating TCM syndrome-differentiation reasoning, with FAIR metadata (Sci. Data 2025). [[DOI](https://doi.org/10.1038/s41597-025-04772-9)] [[Paper](https://www.nature.com/articles/s41597-025-04772-9)] [[Code](https://github.com/zhuyan166/TCMEval)]
- **TCMBench** — TCMBench: a comprehensive benchmark for evaluating LLMs in traditional Chinese medicine (arXiv 2024). [[Dataset](https://github.com/ywjawmw/TCMBench)] [[Paper](https://arxiv.org/abs/2406.01126)]
- **TCM-Vision-Benchmark** — TCM vision benchmark (herb recognition / inspection, ~7k items). [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Vision-Benchmark)]
- **TCM-Tongue** — 6,719 standardized tongue images with 20-class multi-label pathology annotations and detection baselines. [[Paper](https://arxiv.org/abs/2507.18288)] [[Data](https://doi.org/10.5061/dryad.1c59zw48r)] [[Code](https://github.com/btbuIntelliSense/Intelligent-tongue-diagnosis-detection-dataset)]
- **TCM-Ladder** — TCM-Ladder: a multimodal QA benchmark for comprehensively evaluating TCM multimodal LLMs on real-world tasks (arXiv 2025). [[Dataset](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[Leaderboard](https://tcmladder.com)] [[Paper](https://arxiv.org/abs/2505.24063)]
- **TCM-Eval** — Dynamic, extensible TCM evaluation platform. [[Paper](https://arxiv.org/abs/2511.07148)] [[Platform](https://tcmeval.bamaidical.com)]
- **TCM-BEST4SDT** — Case benchmark for syndrome differentiation and treatment. [[Dataset](https://github.com/DYJG-research/TCM-BEST4SDT)] [[Paper](https://arxiv.org/abs/2512.02816)]
- **TCM-5CEval** — Five-dimension deep TCM evaluation suite. [[Paper](https://arxiv.org/abs/2511.13169)]
- **TCM-3CEval** — Three-axis eval: core knowledge, classics, clinical decisions. [[Paper](https://arxiv.org/abs/2503.07041)]
- **MTCMB** — MTCMB dataset: a multi-task TCM benchmark covering knowledge, reasoning and safety, 12 subsets with ~7,100 samples (arXiv 2025). [[Dataset](https://github.com/Wayyuanyuan/MTCMB)] [[Paper](https://arxiv.org/abs/2506.01252)]
- **HWTCMBench** — HWTCMBench TCM capability evaluation set. [[Dataset](https://huggingface.co/datasets/Monor/hwtcm)]
- **Chinese Drug Name Overreliance Set** — Experiment data for the paper on whether LLMs over-rely on names to identify ingredients of Chinese drugs, linked from the dataset card to arXiv:2504.03786. [[Dataset](https://huggingface.co/datasets/med-llm/tcm-llm-overrely-on-names)]
- **AcuSim** — Synthetic dataset for localising cervicocranial acupuncture points, built because expert annotation is costly and limits detector training. [[Paper](https://doi.org/10.1038/s41597-025-04934-9)]
- **CMMLU Traditional Chinese Medicine** — CMMLU Traditional Chinese Medicine test split; the card shows a 185-example load and the file traditional_chinese_medicine.json. [[Dataset](https://huggingface.co/datasets/shuyuej/CMMLU-Traditional-Chinese-Medicine-Benchmark)]
- **TCM-SD** — First large public TCM syndrome-differentiation text benchmark (54,152 real records, 148 syndromes, CC BY-NC-SA 4.0). Full set is in the repo folder TCM_SD_with_knowledge; Tianchi id 139034. [[Paper](https://arxiv.org/abs/2203.10839)] [[Published](https://aclanthology.org/2022.ccl-1.80/)] [[Code](https://github.com/Borororo/ZY-BERT)] [[Data](https://tianchi.aliyun.com/dataset/dataDetail?dataId=139034)]

</details>

<details>
<summary>Exam datasets (8)</summary>

- **TCMQA** — 38,279 TCM licensing questions with 15,151 responses from 101 licensed practitioners. [[Paper](https://arxiv.org/abs/2609.33014)]
- **TCMLE** — Chinese TCM practitioner licensing question bank with 7,956 items: 2,700 assistant-practitioner and 5,256 practitioner questions, including past papers and mocks. [[Dataset](https://huggingface.co/datasets/Bolin97/TCMLE)]
- **TCM-Text-Exams** — Recent TCM licensure / graduate-exam text benchmark. [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams)]
- **Medical-LLMs-Chinese-Exam** — Chinese medical exam evaluation for medical LLMs. [[Dataset](https://github.com/jingnant/Medical-LLMs-Chinese-Exam)]
- **Taiwan TCM Examination MCQ** — Past national TCM exam questions from Taiwan's Ministry of Examination; the README gives ROC years 96–111 excluding 110, and the repository file is basic theory of traditional Chinese medicine.csv. [[Dataset](https://huggingface.co/datasets/Liavan/Traditional-Chinese-Medicine-Multiple_choice_question)]
- **TCM Humanities MCQ** — Multiple-choice questions on medical humanities, ethics, and physician regulations, curated by the Traditional Chinese Medicine Language Model Team; the card marks the size as under 1,000. [[Dataset](https://huggingface.co/datasets/TCMLM/TCM_Humanities)]
- **JTB Taiwan TCM Exam Questions** — JTB Tech compilation of Taiwan Ministry of Examination TCM questions for ROC years 90–113, covering TCM internal medicine, basic medicine, and clinical medicine. [[Dataset](https://huggingface.co/datasets/JTBTechnology/tcm_exam_questions)]
- **2023 Pharmacist Licensure Examination TCM Track** — TCM Pharmacy track items from the 2023 Chinese National Pharmacist Licensure Examination; the card says they were collected online and points to FreedomIntelligence/HuatuoGPT-II. [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/2023_Pharmacist_Licensure_Examination-TCM_track)]

</details>

<details>
<summary>Instruction / dialogue datasets (21)</summary>

- **HSQ-TD（健身气功指令微调数据集）** — HSQ-TD: the first instruction-tuning dataset for health Qigong/wellness, with 57,843 instructions distilled from official textbooks and professional literature (ScienceDB). [[Dataset](https://doi.org/10.57760/sciencedb.35843)]
- **中医药知识问答实验数据** — Traditional Chinese medicine question-answering set plus the knowledge graph, prompt-engineering code, and experiment outputs. [[Dataset](https://doi.org/10.57760/sciencedb.j00133.00319)]
- **neijing-sft-v1.2** — ~2,009 Neijing-related instruction samples for Xinghe, with thinking/output fields. [[Dataset](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2)]
- **TriCM-DF Acupuncture Corpus** — Expert-verified instruction corpus for TCM models, instantiated for acupuncture across consensus, experiential, and perception tables; the repository releases text, not the image or video files. [[Dataset](https://huggingface.co/datasets/Shutcm-TCME/TriCMDF)]
- **TCMNSCLC** — Real-world NSCLC TCM reasoning dataset with fully annotated cases (pattern differentiation / treatment method / decoction / patent medicine). [[Dataset](https://huggingface.co/datasets/zhangxinxin0428/TCMNSCLC)] [[DOI](https://doi.org/10.5281/zenodo.21027568)]
- **TCM Medical Case Commentary Generation** — Generation set for TCM medical-case commentary, with 510 standardized source cases and 2,550 training and test instances compiled from gynecological classics. [[Dataset](https://doi.org/10.57760/sciencedb.j00133.00679)]
- **Gancao-TCM-Instruct** — Public Gancao-TCM-Instruct release with 25,000 cases and 125,000 samples covering disease diagnosis, syndrome diagnosis, treatment selection, base-formula selection, and herb selection. [[Dataset](https://huggingface.co/datasets/GancaoDoctorAI/gancao-tcm-instruct)]
- **tw-tcm** — minyichen/tw-tcm card lists 8,145 training examples with question, answer, source, and think fields. [[Dataset](https://huggingface.co/datasets/minyichen/tw-tcm)]
- **hwtcm-deepseek-r1-distill-data** — Haiwei AI Team's DeepSeek-distilled TCM reasoning QA set built from web text. The authors state that it was not manually reviewed. [[Dataset](https://huggingface.co/datasets/Monor/hwtcm-deepseek-r1-distill-data)]
- **Traditional-Chinese-Medicine-Dataset-SFT** — High-quality TCM supervised fine-tuning dataset. [[Dataset](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]
- **TCMChat-dataset-600k** — TCMChat herbal QA and recommendation instruction data (~600k). [[Dataset](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- **TCM-Instruction-Tuning-ShizhenGPT** — ShizhenGPT multimodal SFT data (text/vision/speech/ECG etc.; ~311k items total per paper Table 3). [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- **TCM Knowledge Q&A** — Science Data Bank set of 6,157 question-answer pairs built from classic Chinese medicine literature. [[Dataset](https://doi.org/10.57760/sciencedb.j00133.00565)]
- **ShenNong_TCM_Dataset** — ShenNong TCM instruction dataset. [[Dataset](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)]
- **MedChatZH** — MedChatZH TCM consultation dataset. [[Code](https://github.com/tyang816/MedChatZH)] [[Dataset](https://huggingface.co/datasets/tyang816/MedChatZH)]
- **ChatMed_Consult_Dataset** — Chinese online medical consult dataset (500k+ consults with ChatGPT replies). [[Dataset](https://huggingface.co/datasets/michaelwzhu/ChatMed_Consult_Dataset)]
- **CMtMedQA** — ZhongJing real multi-turn doctor–patient dialogues (~70k). [[Dataset](https://huggingface.co/datasets/Suprit/CMtMedQA)]
- **Baize-TCM-Corpus-V3** — ~157k TCM QA items covering theory, herbs, formulas, diagnosis, acupuncture, and clinic. [[Dataset](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3)]
- **hwtcm-sft-v1** — Haiwei AI Team's 7,096-example TCM instruction set. Text from websites, forums, and books was converted to QA and scored for expertise, safety, and fluency. [[Dataset](https://huggingface.co/datasets/Monor/hwtcm-sft-v1)]
- **TCM_19W_DataSet-SFT (part)** — The card describes a partial non-web TCM instruction-tuning set, released as TCM19W_Part1.json. [[Dataset](https://huggingface.co/datasets/cduoduo/TCM_19W_DataSet-SFT)]
- **ChP-TCM** — KnowledgeQA and PrescriptionWriting instructions built from Chinese Pharmacopoeia Vol. I. [[Data](https://github.com/QLU-NLP/BianCang/tree/main/ChP-TCM)] [[Paper](https://arxiv.org/abs/2411.11027)]

</details>

<details>
<summary>Knowledge graphs (21)</summary>

- **本草典开放数据** — Bilingual TCM seed data from the Bencao Dian editorial group, released under CC BY-SA 4.0 as directly downloadable JSON. Version 1, generated on 17 April 2026, lists 365 herb records, 112 formulas, 84 patterns, and 208 acupoints, plus meridians, tongue and pulse entries, and a relation graph. A coverage note on the same page says 335 of about 530 standard materia medica items are included. This is an editorial vocabulary, not a national standard. [[Website](https://bencaodian.org/zh/about/data/)] [[Data](https://bencaodian.org/data/v1/herbs.json)]
- **医宗金鉴知识三元组** — 25,571 knowledge triples extracted from the Golden Mirror of Medicine, covering medicinals, formulas, diseases, acupoints, and theory across 1,105 relation types. [[Dataset](https://doi.org/10.57760/sciencedb.013fv)]
- **TCMEFO** — Formal ontology for traditional Chinese medicine efficacy, providing a hierarchical computable framework over concepts, relations, and herbal-medicine instances. [[Dataset](https://doi.org/10.6084/m9.figshare.32677743)]
- **TCM Disease-Pattern-Symptom-Herb KG v2** — Version 2.0 semantic knowledge graph linking diseases, patterns, symptoms, and herbs, released as node and edge CSV files. [[Dataset](https://zenodo.org/records/18173423)]
- **LingShu** — Symptom-centric contextual KG bridging TCM and biomedicine (~17.33M entities, ~39.47M relations including triples and contextual quadruples), with a portal for visualization, reasoning, and evidence-grounded QA. [[Paper](https://arxiv.org/abs/2608.20402)] [[Website](http://www.tcmkg.com/)]
- **Chinese Herbal Efficacy Relations** — Structured herb–efficacy relations converted from classical TCM efficacy wording for knowledge-graph construction, formula-efficacy prediction, and herb–symptom association. [[Dataset](https://zenodo.org/records/18207409)]
- **TCM_KG** — ChatMed knowledge graph. [[Dataset](https://github.com/ywjawmw/TCM_KG)]
- **TCM-MKG** — TCM multi-dimensional knowledge graph. [[Data](https://zenodo.org/records/15395588)]
- **OpenTCM-KG** — OpenTCM gynecology classics KG (~48k entities / ~152k relations). [[Code](https://github.com/OpenTCM01/OpenTCM)] [[Paper](https://arxiv.org/abs/2504.20118)]
- **AcuKG** — Knowledge graph of medical acupuncture assembled from guidelines, literature, trials, and ontology mapping. [[Paper](https://doi.org/10.1093/jamia/ocaf179)]
- **SoFDA** (site issue) — Syndrome-ontology platform built by the Institute of Chinese Materia Medica, CACMS, and collaborators. The iMeta 2023 paper describes 319 curated syndromes, 8,045 diseases, and 1,359 formulas, linked to genes, diseases, and formulas. The paper page checks out; the front page currently shows no readable syndrome content. It shares the tcmip.cn host with ETCM but is a separate syndrome system. No anonymous full-database mirror was found. [[Website](http://www.tcmip.cn/Syndrome/front/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10989962/)]
- **GB/T 16751.3-2023** — Current national standard Clinic terminology of traditional Chinese medical diagnosis and treatment — Part 3: Therapeutic methods, issued and effective on 17 March 2023. The official full-text disclosure system offers online preview and download. This is the therapeutic-method standard page, not a separate vocabulary dump. [[Website](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E8BBBAB76E1AF1498C5DA5DFBB2194EC)]
- **GB/T 16751.1-2023** — Current national standard Clinic terminology of traditional Chinese medical diagnosis and treatment — Part 1: Diseases, issued and effective on 17 March 2023, under the National Administration of Traditional Chinese Medicine. The official full-text disclosure system offers online preview and download. Syndrome and therapeutic-method parts have their own full-text pages. [[Website](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=7377FB06FF43DC321BB6A4BF7DAA7F39)]
- **TCM-QG** — About 5,000 TCM documents and 13,000 question-answer pairs from CHIP2020, for knowledge-base expansion and question generation (CC BY-SA 4.0). [[Data](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86895)] [[Resources](http://openkg.cn/dataset/tcm-qg)]
- **TCM-NER** — 1,997 Chinese-medicine package inserts with 59,803 entities in 13 types for building a medication knowledge graph (OpenKG / CHIP, CC BY-SA 4.0). [[Data](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86819)] [[Resources](http://openkg.cn/dataset/tcm-ner)]
- **GB/T 16751.2-2021** — Current national standard Clinic terminology of traditional Chinese medical diagnosis and treatment — Part 2: Syndromes/patterns, issued and effective on 26 November 2021. The official full-text disclosure system offers online preview and download. This is the syndrome-terminology standard page, not a separate vocabulary dump. [[Website](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C71A9DAD24CB1252F12439D1F045DA6A)]
- **GB/T 15657-2021** — Current Chinese national standard Classification and codes of diseases and patterns of traditional Chinese medicine, issued and effective on 11 October 2021, replacing GB/T 15657-1995, under the National Administration of Traditional Chinese Medicine. The official full-text disclosure system offers online preview and download. This is the standard page, not a standalone machine-readable code package. [[Website](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=41FD9D06E5BE4F84EA1D8D07101BED2C)]
- **GB/T 12346-2021** — Current Chinese national standard Nomenclature and location of meridian points, issued and effective on 26 November 2021, under the National Administration of Traditional Chinese Medicine. The official full-text disclosure system offers online preview and download. This is the standard page, not a separately packaged acupoint table. [[Website](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=397548AE7248D3D87DD15E0AB8107185)]
- **中医药知识服务平台** — Knowledge-service homepage maintained by the Institute of Information on Traditional Chinese Medicine, CACMS, for search, knowledge graphs, and disease profiles. A related about page from the same institute says that, starting in 2019, it built a professional TCM knowledge service for the China Knowledge Centre for Engineering Sciences and Technology, bringing together diseases, formulas, herbs, and literature. The homepage opens; campus trial notes require registration on an institutional network, and no public bulk download was found. [[Website](https://www.tcmkb.cn/)]
- **ICD-11传统医学章节** — Official WHO explanation of the ICD-11 supplementary chapter Traditional Medicine Conditions. The chapter is for optional dual coding of morbidity and is not used for mortality. Module I covers traditional-medicine conditions that originated in ancient China and are now used in China, Japan, Korea, and elsewhere. This page explains the chapter; the codes themselves are read in the ICD-11 browser. The page is public. [[Website](https://www.who.int/standards/classifications/frequently-asked-questions/traditional-medicine)]
- **WHO西太区标准穴位定位** — WHO Regional Office for the Western Pacific standard for acupuncture point locations, published in 2008 and reprinted in 2009. The IRIS record states the surface-location method and 361 points for teaching, research, clinical service, publication, and academic exchange, and provides the English PDF. Experts from China, Japan, and Korea joined the location consensus. The record page is public. [[Website](https://iris.who.int/handle/10665/353407)]

</details>

---

Search and filter by tag on the [project page](https://tyang816.github.io/projects/tcm/). Longer notes live in the [wiki](wiki/Home.md).
Add entries in `data/catalog.yml` and run `python3 scripts/build_readme.py`. Do not edit this README by hand.
