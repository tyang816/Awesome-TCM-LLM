# 🔥 Open TCM Models, Data, Papers, and Patents

**Language / 语言:** [English](README_EN.md) | [中文](README.md)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  ![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork) [![中文门户](https://img.shields.io/badge/中医资源-门户-blue)](https://tyang816.github.io/zh/projects/tcm/) [![Project](https://img.shields.io/badge/Project-tyang816.github.io-informational)](https://tyang816.github.io/projects/tcm/)

Open TCM models, datasets, papers, and patents, plus a few related Chinese medical resources. Right now: 29 news items, 92 models, 47 surveys, 22 patents, 85 datasets, 157 method papers. [PRs welcome](CONTRIBUTING.md).

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
| **Xinghe** | 2026 | — | Reason · Classics | [Weights](https://huggingface.co/zsyjsld/Xinghe1.2-9B) · [Data](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2) |
| **ZhiFangDanTai** | 2025 | — | RAG · KG | [Paper](https://arxiv.org/abs/2509.05867) · [Weights](https://huggingface.co/tczzx6/ZhiFangDanTai1.0) |
| **Baize-TCM-LLM** | 2025 | Institute of Chinese Materia Medica | ICMM Baize TCM QA models on Qwen3 (0… | [Weights](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model) · [Data](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3) |
| **BianCang** | 2025 | Qilu University of Technology | BianCang TCM LLM series (IEEE JBHI)… | [Paper](https://arxiv.org/abs/2411.11027) · [Weights](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct) · [Code](https://github.com/QLU-NLP/BianCang) |
| **仲景 (ZhongJing)** | 2025 | — | ZhongJingGPT, an expert-knowledge-gu… | [Paper](https://doi.org/10.26599/TST.2025.9010046) · [Weights](https://huggingface.co/CMLM/ZhongjingGPT1_13B) · [Code](https://github.com/pariskang/CMLM-ZhongJing) |
| **ViTCM-LLM** | 2025 | Tsinghua Shenzhen International Graduate School | MM · RAG | [Paper](https://doi.org/10.1109/bibm66473.2025.11357113) · [Weights](https://huggingface.co/Mark-CHAE/ViTCM-LLM) · [Code](https://github.com/jw-chae/ViTCM_LLM) |
| **TCMChat** | 2025 | — | Generative TCM LLM built via pre-tra… | [Paper](https://doi.org/10.1016/j.phrs.2024.107530) · [Weights](https://huggingface.co/ZJUFanLab/TCMChat-600k) · [Code](https://github.com/ZJUFanLab/TCMChat) · [Data](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k) |
| **ShizhenGPT** | 2025 | The Chinese University of Hong Kong | MM | [Paper](https://arxiv.org/abs/2508.14706) · [Weights](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni) · [Code](https://github.com/FreedomIntelligence/ShizhenGPT) |
| **ChatTCM** | 2025 | — | Fully open TCM LLM from pretraining… | [Weights](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain) |
| **TCMLLM / Lingdan** | 2024 | Beijing Jiaotong University | TCMLLM / Lingdan for TCM modeling an… | [Paper](https://doi.org/10.1016/j.dcmed.2025.01.007) · [Weights](https://huggingface.co/TCMLLM/Lingdan-13B-Base) · [Code](https://github.com/2020MEAI/TCMLLM) |
| **MedChatZH** | 2024 | — | MedChatZH: a fine-tuned LLM for TCM… | [Paper](https://doi.org/10.1016/j.compbiomed.2024.108290) · [Code](https://github.com/tyang816/MedChatZH) · [Weights](https://huggingface.co/tyang816/medchatzh) · [Data](https://huggingface.co/datasets/tyang816/MedChatZH) |
| **神农大模型 (ShenNong-TCM-LLM)** | 2023 | — | ShenNong-TCM-LLM, the first TCM larg… | [Weights](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM) · [Code](https://github.com/michael-wzhu/ShenNong-TCM-LLM) · [Data](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset) |

</details>

<details>
<summary>Paper or product only, no verified weights (33)</summary>

<details>
<summary>2026 · 10</summary>

- [*Digital Chinese Medicine*] **QingNangTCM** Parameter-efficient fine-tuned TCM QA and clinical reasoning model; builds the 100k-item **QnTCM_Dataset**. [Hebei North University] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.002)]
- [*ISCTIS 2026*] **Tongue–face multimodal fusion diagnosis** Tongue–face multimodal feature fusion with LLM-driven intelligent TCM diagnosis. [Xiamen University of Technology] [[DOI](https://doi.org/10.1109/ISCTIS70043.2026.11572361)]
- **Lingdan-V2** BJTU's second Lingdan TCM reasoning family (Qwen3 4B/8B/14B with CPT, SFT, and prescription GRPO). ModelScope checkpoints exist but require access requests, so they are not marked freely downloadable. [Beijing Jiaotong University] [[Code](https://github.com/TCMAI-BJTU/Lingdan-V2)] [[ModelScope](https://modelscope.cn/models/TCMAIBJTU/Lingdan-14B-R1)]
- [*JMIR Medical Informatics*] **TongueVLM** Multimodal VLM for TCM tongue diagnosis, description generation, and constitution reasoning. [[Paper](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- [*Digital Chinese Medicine*] **Qwen-TCM-Dia** Specialty fine-tuned model for TCM diarrhea care (CPT + CoT SFT) covering symptom→pathomechanism→method→formula chains. [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.003)]
- [*arXiv*] **Med-Shicheng** Lightweight master-physician experience-inheritance framework built on Tianyi; a single model internalizes 5 national masters' knowledge systems across 7 task types. [Nanjing University of Chinese Medicine et al.] [[Paper](https://arxiv.org/abs/2603.23520)] [[Code](https://github.com/NJUCM-BJUCM-TCM-AI/Med-Shicheng)]
- [*Chinese Herbal Medicines*] **HerbWise** Domain LLM for traditional herbal medicine (THM), serving herbal modernization and standardization. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.chmed.2026.02.010)]
- [*Chinese Medicine*] **GastroTCM** TCM gastroenterology LLM fine-tuned from Llama3-8B with RAG and agent scaffolding. [[Paper](https://link.springer.com/article/10.1186/s13020-025-01295-8)]
- [*arXiv*] **DongYuan** Integrative spleen–stomach disease diagnosis LLM framework combining TCM pattern differentiation with Western diagnostic reasoning. [[Paper](https://arxiv.org/abs/2603.28191)]
- [*Chinese Medicine*] **DFGLM-TCM** Dongfang Hospital / Zhipu TCM clinical system that models textbook knowledge and practitioner experience in separate modules; paper is out, weights are not. [Beijing University of Chinese Medicine, Zhipu AI] [[DOI](https://doi.org/10.1186/s13020-026-01512-y)]

</details>

<details>
<summary>2025 · 18</summary>

- [*arXiv*] **ZMT-M1** ZMT-M1 TCM LLM and the dynamic, extensible TCM-Eval benchmark platform. [Beihang University] [[Paper](https://arxiv.org/abs/2511.07148)] [[Platform](https://tcmeval.bamaidical.com)]
- [*Chinese Medicine*] **XuanHuGPT** TCM domain LLM built with parameter-efficient fine-tuning (PEFT). [Hebei North University] [[DOI](https://doi.org/10.1186/s13020-025-01200-3)]
- [*Expert Systems with Applications*] **Qibo** TCM LLM and Qibo Benchmark from Tianjin University et al.; CPT + SFT for SDT and QA. [Tianjin University, Tianjin University of Traditional Chinese Medicine] [[Published](https://doi.org/10.1016/j.eswa.2025.127672)] [[Paper](https://arxiv.org/abs/2403.16056)] [[DOI](https://doi.org/10.1016/j.eswa.2025.127672)]
- **女娲 (Nüwa / TCM-Nvwa)** Nüwa TCM LLM training stack (continual pretraining, SFT, reward modeling, RLAIF) on Ziya-LLaMA-13B. Repo ships only partial pretrain/TCM-QR/reward data and no standalone weights; GitHub created April 2025, distinct from arXiv 2411.00897. [[Code](https://github.com/synbol/TCM-Nvwa)]
- [*arXiv*] **TianHui** Domain LLM for 12 TCM scenarios (DeepSeek-R1-Distill-Qwen-14B + PT/SFT) with open code and eval scripts. [[Paper](https://arxiv.org/abs/2509.19834)] [[Code](https://github.com/JYfantast/TianHui)]
- [*Information Fusion*] **Tianyi** ~7B TCM LLM from NJUCM et al. with reading–clinic–apprenticeship training stages, TCMEval, and real-world validation. [Nanjing University of Chinese Medicine] [[Published](https://doi.org/10.1016/j.inffus.2025.103663)] [[Paper](https://arxiv.org/abs/2505.13156)] [[News](https://blog.sciencenet.cn/blog-279293-1501581.html)]
- [*IEEE BIBM 2025*] **TCM-VisResolve (TCM-VR)** Qwen2.5-VL-based TCM multimodal LLM — 163-class dried-herb recognition over 220k images plus clinical MCQs with 880k candidate answers. [Minzu University of China] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356679)]
- [*APWeb-WAIM 2025*] **TCM-R1** TCM LLM with GRPO-enhanced reasoning. [Southwest University] [[Paper](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*Computers in Biology and Medicine*] **TCM-KLLaMA** KG-fused LLM for intelligent TCM formula generation. [[DOI](https://doi.org/10.1016/j.compbiomed.2025.109887)]
- [*Chinese Medicine*] **TCM-DS** Domain LLM for medicine–food homology dietary-therapy recommendation. [Macau University of Science and Technology] [[DOI](https://doi.org/10.1186/s13020-025-01249-0)]
- [*arXiv*] **RACE-Align** RACE-Align: retrieval-augmented, CoT-style DPO alignment of a compact Qwen3-1.7B for TCM reasoning. [[arXiv](https://arxiv.org/abs/2506.02726)]
- [*IEEE ICIP 2025*] **MCM** Multi-agent collaborative multimodal TCM diagnosis framework (IEEE ICIP 2025). [Shanghai Computer Software Technology Development Center] [[Code](https://github.com/JerryMazeyu/MCM)] [[Published](https://doi.org/10.1109/icip55913.2025.11084334)]
- [*arXiv*] **Ladder-base (GRPO-TCM)** First GRPO reinforcement-learning-aligned TCM LLM, from the TCM-Ladder team. [[Paper](https://arxiv.org/abs/2510.17402)]
- [*arXiv*] **Hengqin-RA-v1** LLM and companion dataset for TCM diagnosis and treatment of rheumatoid arthritis. [[Paper](https://arxiv.org/abs/2501.02471)]
- [*Applied Sciences*] **Gen-SynDi** Knowledge-guided generative-AI framework for dual education of syndrome differentiation and disease diagnosis. [College of Korean Medicine, Wonkwang University, Iksan 54538, Republic of Korea, College of Korean Medicine, Woosuk University, Jeon-Ju 54987, Republic of Korea, Dongje Medical Co., Ltd., Daegu 42187, Republic of Korea, College of Medicine, Yeungnam University, Daegu 42415, Republic of Korea] [[DOI](https://doi.org/10.3390/app15094862)]
- [*arXiv*] **DoPI** Doctor-like proactive inquiry TCM LLM (guide + expert models); reported inquiry accuracy 84.68%. [[Paper](https://arxiv.org/abs/2507.04877)]
- [*IEEE BIBM 2025*] **ChatGLM-FGIDs-TCM** Knowledge-fused ChatGLM clinical decision-support model for functional gastrointestinal disorders (FGIDs). [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356283)]
- [*arXiv*] **BenCao** Instruction-aligned multimodal TCM assistant (ChatGPT/GPTs Store) with tongue APIs and knowledge bases (distinct from HuaTuo/BenCao). [[Paper](https://arxiv.org/abs/2510.17415)]

</details>

<details>
<summary>2024 · 4</summary>

- **大数中医 (BigDataTCM)** BigDataTCM (34B): a vertical TCM LLM co-developed by HAUT's Complexity Science institute and Apus, offering medical QA, diagnostic support and TCM knowledge services. [[Code](https://github.com/HAUT-CS/BigDataTCM)]
- [*AAAI*] **仲景（CMtMedQA 线，Yang et al.）** ZhongJing (CMtMedQA line, Yang et al.): a TCM LLM distinct from the Kang-line ZhongJingGPT—full CPT+SFT+RLHF pipeline on Ziya-LLaMA-13B over ~70K real multi-turn doctor-patient dialogues (AAAI 2024). [[Paper](https://doi.org/10.1609/aaai.v38i17.29907)] [[arXiv](https://arxiv.org/abs/2308.03549)]
- [*Computer Methods and Programs in Biomedicine Update*] **TCM-GPT** Efficient pre-training of LLMs for domain adaptation in Traditional Chinese Medicine. [[DOI](https://doi.org/10.1016/j.cmpbup.2024.100158)] [[Paper](https://arxiv.org/abs/2311.01786)]
- [*Scientific Reports*] **CPMI-ChatGLM** Parameter-efficient fine-tuning of ChatGLM with Chinese patent medicine instructions. [[DOI](https://doi.org/10.1038/s41598-024-56874-w)]

</details>

<details>
<summary>2023 · 1</summary>

- **黄帝 (HuangDi)** HuangDi: a TCM classics QA LLM built on Ziya-LLaMA-13B, pretrained on 22 TCM textbooks plus TCM web corpora and SFT-tuned with ancient-book instruction data (Library Tribune 2024). [[Code](https://github.com/Zlasejd/HuangDI)]

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
- [*Journal of the American Medical Informatics Association*] **Taiyi-2** Second Taiyi open biomedical model, moving from Qwen-7B to GLM4-9B with tighter data filters and task instructions; the official replacement for Taiyi-1. [Dalian University of Technology] [[Model](https://huggingface.co/DUTIR-BioNLP/Taiyi2-chat)] [[Code](https://github.com/DUTIR-BioNLP/Taiyi-LLM)] [[DOI](https://doi.org/10.1093/jamia/ocae037)]
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

- [*arXiv*] **Qilin-Med** Multi-stage Chinese medical LLM (CPT+SFT+DPO on Baichuan-7B) releasing the ~3GB ChiMed corpus, optionally with RAG. [[Paper](https://arxiv.org/abs/2310.09089)] [[Code](https://github.com/williamliujl/Qilin-Med)] [[Dataset](https://huggingface.co/datasets/williamliu/ChiMed)]
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
- [*arXiv*] **IvyGPT** LLaMA-based Chinese medical QA model fine-tuned with curated clinical QA and RLHF; listed as an open baseline in the CMB paper. [[Paper](https://arxiv.org/abs/2307.10512)] [[Code](https://github.com/Ivy0529/IvyGPT)]
- [*arXiv*] **DoctorGLM** Early open Chinese consultation model on ChatGLM-6B with LoRA/P-Tuning; a frequent 2023 Chinese medical baseline. [[Paper](https://arxiv.org/abs/2304.01097)] [[Code](https://github.com/xionghonglin/DoctorGLM)]
- [*arXiv*] **DISC-MedLLM** Fudan DISC conversational medical LLM on Baichuan-13B, with DISC-Med-SFT built from knowledge graphs and reconstructed consultations. [Fudan University] [[Paper](https://arxiv.org/abs/2308.14346)] [[Code](https://github.com/FudanDISC/DISC-MedLLM)] [[Model](https://huggingface.co/Flmc/DISC-MedLLM)] [[Dataset](https://huggingface.co/datasets/Flmc/DISC-Med-SFT)]
- [*arXiv*] **ClinicalGPT** BUPT clinical Chinese medical model (BLOOM-7B) fine-tuned on records, knowledge, exams, and multi-turn consults; a common CMB-era baseline. HF hosts a medicalai snapshot. [Beijing University of Posts and Telecommunications] [[Paper](https://arxiv.org/abs/2306.09968)] [[Model](https://huggingface.co/medicalai/ClinicalGPT-base-zh)]
- [*arXiv*] **ChiMed-GPT** USTC Chinese medical LLM continued from Ziya-v2 with pretraining, SFT, and RLHF for extraction, QA, and multi-turn dialogue. [University of Science and Technology of China] [[Paper](https://arxiv.org/abs/2311.06025)] [[Code](https://github.com/synlp/ChiMed-GPT)] [[Model](https://huggingface.co/SYNLP/ChiMed-GPT-1.0)]
- **ChatMed** ChatMed series of Chinese medical LLMs, including ChatMed-Consult trained on 500k+ online consultation dialogues. [[Code](https://github.com/michael-wzhu/ChatMed)]
- **ChatGLM-Med** HIT-SCIR ChatGLM-6B instruction-tuned on Chinese medical KGs, sharing data lineage with BenCao/HuaTuo; a frequent CMB baseline. [Harbin Institute of Technology] [[Code](https://github.com/SCIR-HI/Med-ChatGLM)]
- **CareGPT** Open Chinese medical LLM training stack (pretrain through DPO) with accompanying weights, often used to reproduce Chinese medical fine-tunes. [[Code](https://github.com/WangRongsheng/CareGPT)]

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

- **KAMPO LLM** Closed Japanese Kampo medical API from VARYTEX with the Japan Society for Oriental Medicine, scored on 471 specialist-training items; no public weights. [VARYTEX] [[Website](https://kampollm.varytex.co.jp/)]

</details>

<details>
<summary>Other Hugging Face sizes and GGUF (12)</summary>

- **Xinghe** — Xinghe Neijing reasoning model weights. [[Model](https://huggingface.co/zsyjsld/Xinghe1.2-9B)] [[GGUF](https://huggingface.co/zsyjsld/Xinghe1.2-9B-GGUF)]
- **ZhiFangDanTai** — ZhiFangDanTai formula-generation model weights. [[Model](https://huggingface.co/tczzx6/ZhiFangDanTai1.0)]
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
<summary>29 items; recent: 广医·岐智2.0 · 首发首展 · 华族本草</summary>

<details>
<summary>2026 · 10</summary>

- [2026.09] Guang'anmen Hospital shows **Guangyi Qizhi 2.0** at CIFTIS 2026, with AI doctor An'an covering six hospital scenes from patient service to ward management. [[Link](https://app.xinhuanet.com/news/article.html?articleId=202609101de3e66a53f7474ba7d373deaaa7e122)]
- [2026.09] Beijing University of Chinese Medicine debuts a TCM constitution-identification system and an embodied tuina robot at the CIFTIS 2026 TCM pavilion. [[Link](https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202608/t20260807_4812596.html)]
- [2026.07] Guizhou Medical University and partners launch **HuaZu BenCao**, a national ethnic-medicine AI platform built on ShuZhi QiHuang + Qwen integrating multi-ethnic materia medica classics. [[Link](https://www.gmc.edu.cn/info/1058/30267.htm)]
- [2026.07] Insightful Eye presents **Bianshi Cloud TCM** at WAIC 2026, built on a registered Bianshi multimodal model with four-diagnosis devices and assisted-care systems. [[Link](http://www.eeo.com.cn/2026/0720/965556.shtml)]
- [2026.07] Andun Health debuts a **seven-diagnosis** TCM robot at WAIC 2026, integrating face/IR face/tongue/ear/auscultation/inquiry/pulse sensing with TianHui pulse algorithms and a TCM clinical LLM. [[Link](https://www.news.cn/finance/20260720/f6a8625c1be4412d9c311a232c7a35fa/c.html)]
- [2026.07] Shanghai Seventh People's Hospital (SHUTCM) releases the **Qiyuan** TCM LLM with pretraining, domain fine-tuning, and expert RL; supports generative medical records and master-physician Agent digital twins; showcased at WAIC. [[Link](https://dwgk.shutcm.edu.cn/2026/0725/c1890a175544/page.htm)]
- [2026.06] Zhongke Wenge passes HKEX listing hearing; reports note the **DaYi JinKui** TCM LLM (with CACMS) has obtained top-tier CAICT Trusted AI certification. [[Link](https://www.ncsti.gov.cn/kjdt/xwjj/202606/t20260610_249369.html)]
- [2026.04] Affiliated Hospital of Shandong University of TCM launches the provincial AI+ TCM scenario project **ZhiHui QiHuang**. [[Link](http://ccpd.china.com.cn/2026-04/17/content_43401621.html)]
- [2026.04] Beijing University of Chinese Medicine's **XinHuo ZhongGuoYao** TCM education LLM completes national generative-AI service filing—the first publicly approved TCM-domain model of its kind. [[Link](https://regional.chinadaily.com.cn/education/cn/2026-04/22/c_1177692.htm)]
- [2026.02] Eight ministries issue the TCM Industry High-Quality Development Plan (2026–2030), calling for AI and knowledge graphs to empower classical formulas and master physicians' prescriptions. [[Link](https://www.gov.cn/zhengce/zhengceku/202602/content_7057174.htm)]

</details>

<details>
<summary>2025 · 14</summary>

- [2025.12] **ZMT-M1** scores 96.26 on a simulated national TCM practitioner exam and is piloted in 100+ clinics. [[Link](https://m.tech.china.com/redian/2025/1229/122025_1789291.html)]
- [2025.12] Gushengtang launches a “TCM Brain” product and AI digital twin of National TCM Master Shi Qi; 14 expert twins cover eight core specialties. [[Link](https://www.jjckb.cn/20251231/693ca93b14ff4f57adc359959dc0320d/c.html)]
- [2025.12] Jilin releases **ZhongXing·Changbai Qihuang 1.0**, an AI-native multimodal TCM LLM. [[Link](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- [2025.11] Five national health ministries issue AI+ healthcare guidelines that explicitly support building TCM diagnostic LLMs. [[Link](https://www.gov.cn/zhengce/zhengceku/202511/content_7047018.htm)]
- [2025.09] **ZhiFu Qihuang Tiangong** TCM AI model completes national deep-synthesis algorithm filing for four-diagnosis devices and constitution assessment. [[Link](http://zs.scbzol.com/zs/2025/0919/328624.html)]
- [2025.09] Transn's **RenDu·SuWen** passes CAICT Trusted AI TCM LLM Level 4+ evaluation. [[Link](https://zhongyi.gmw.cn/2025-09/10/content_38277329.htm)]
- [2025.09] **YiYin** classical TCM LLM goes live in Song County, Henan, combining TCM education with AI-assisted care for county clinics. [[Link](http://www.ha.xinhuanet.com/20250918/a3da94037689422dbcd1fe57fa62ef94/c.html)]
- [2025.08] NSCC-TJ and Tianjin University of TCM release **TianHe·LingShu** 2.0 (expanded beyond acupuncture to 20+ specialties) and launch a TCM intelligent-model evaluation system. [[Link](http://tj.people.com.cn/n2/2025/0809/c375366-41317410.html)]
- [2025.08] **Gushengtang** releases ten “National Master AI twins” trained on master clinicians' experience, reporting >86% pattern-differentiation accuracy. [[Link](http://sz.people.com.cn/n2/2025/0801/c202846-41310443.html)]
- [2025.07] Guang'anmen Hospital forms the **GuangYi·QiZhi** LLM agent alliance with medical consortium partners for cross-institution intelligent care. [[Link](https://www.gamyy.cn/gzb/news/big/112751.html)]
- [2025.06] **TCM Hengqin** vertical LLM is officially released. [[Link](https://www.stdaily.com/web/gdxw/2025-06/20/content_357526.html)]
- [2025.05] China Academy of Chinese Medical Sciences releases evaluation standards for TCM large models. [[Link](https://www.news.cn/politics/20250510/5e6a0b4978b44b69b67dbfb7282fd220/c.html)]
- [2025.04] Transn releases **RenDu·SuWen** TCM LLM (mixture-of-entropy architecture) for inquiry, pattern differentiation, and formula recommendation. [[Link](https://www.transn.com/about_us/consult/article/1924766101036437505)]
- [2025.03] Guang'anmen Hospital releases **GuangYi·QiZhi**, described as the first TCM hospital with integrated local compute + model + application deployment. [[Link](https://www.xinhuanet.com/tech/20250328/8b1685ad8c6f48c9bdc2add1658edac3/c.html)]

</details>

<details>
<summary>2024 · 4</summary>

- [2024.12] China UnionPay Consumer Finance with Sun Yat-sen University and GZUCMS Shenzhen Hospital release vertical TCM LLM **ZhongSi** for community clinic inquiry. [[Link](https://finance.sina.com.cn/jjxw/2024-12-16/doc-inczrzsp5791684.shtml)]
- [2024.09] Zhongke Wenge releases **DaYi JinKui** TCM LLM and health platform trained on 1,500+ TCM classics. [[Link](https://36kr.com/newsflashes/2946967562099592)]
- [2024.05] Tasly and Huawei Cloud release **ShuZhi BenCao** (Pangu language + molecular models) covering TCM R&D; later earns CAICT TCM LLM Level 4+. [[Link](https://news.pharmnet.com.cn/news/2024/05/10/591622.html)]
- [2024.03] ECNU, SHUTCM, ECUST, NMMU, Lingang Lab, and CR Jiangzhong jointly develop the **ShuZhi QiHuang** TCM LLM. The linked ECNU page is a later write-up of ShuZhi QiHuang 2.0, not the original 2024.03 release announcement. [[Link](https://pharm.ecnu.edu.cn/08/27/c43775a657447/page.htm)]

</details>

<details>
<summary>2023 · 1</summary>

- [2023.07] Nanjing Dajing TCM releases **QiHuang Wendao** LLM with large knowledge graphs and clinical data for institutional beta use. [[Link](http://js.news.cn/20230729/fa034db71a00487b819a4ad95b44673e/c.html)]

</details>


</details>

## Surveys

<details>
<summary>47 surveys, grouped by year</summary>

<details>
<summary>2026 · 22</summary>

- [*兰州大学学报(医学版)*] **从大语言模型到智能体（兰州大学学报医学版综述）** Chinese-language systematic review organized around the LLM-to-agent transition for TCM clinical assisted diagnosis and treatment (J. Lanzhou Univ. Med. Sci. 2026;52(4):49-57). [[DOI](https://doi.org/10.13885/j.issn.2097-681X.T20260032)]
- **Agentic and Knowledge-Grounded LLMs in TCM（预注册）** OSF preregistration (not a completed review) of a systematic review on agentic and knowledge-grounded LLMs in TCM: evidence mapping, text mining, and translation readiness. [[Link](https://doi.org/10.17605/osf.io/kq8jx)]
- [*International Journal of Pattern Recognition and Artificial Intelligence*] **中医大模型关键技术综述（IJPRAI）** Survey of key technologies for TCM LLMs: knowledge organization, aided diagnosis, and clinical decision support (formally published in IJPRAI, World Scientific). [[DOI](https://doi.org/10.1142/s0218001426590263)]
- [*Journal of Traditional Chinese Medical Sciences*] **AI驱动中医诊断智能化综述（JTCMS）** Survey on multimodal fusion and LLMs for intelligent four-diagnosis in TCM: applications, challenges and outlook (JTCMS). [[DOI](https://doi.org/10.1016/j.jtcms.2026.05.002)]
- [*上海中医药杂志*] **人工智能驱动下的中医智能诊疗研究进展与挑战** Chinese review structured on the six-step TCM diagnosis-treatment chain (four diagnoses, pattern differentiation, prescription, outcome prediction), contrasting supervised/unsupervised/RL/deep-learning paradigms (Shanghai J. TCM 2026;60(1)). [[DOI](https://doi.org/10.16305/j.1007-1334.2026.z20250609004)]
- [*Communications in Computer and Information Science (Springer)*] **多模态大模型驱动舌脉面诊智能化综述（Springer 书章）** The only review text dedicated to multimodal-LLM-driven tongue, pulse, and facial diagnosis in TCM (Springer CCIS book chapter; weaker peer review than journals). [[DOI](https://doi.org/10.1007/978-981-95-7299-1_15)]
- [*中华中医药学刊*] **人工智能赋能中医数字化诊断：现状与挑战（中华中医药学刊）** Short Chinese review of AI-empowered digital TCM diagnosis: applications, data-quality, interpretability, and theory-integration challenges (bibliographic record only). [[DOI](https://doi.org/10.13193/j.issn.1673-7717.2026.01.004)]
- [*Integrative Medicine Research*] **Yao et al. 2026: LLM 与循证中医整合（Scoping Review）** PRISMA scoping review (12 studies, 2022-11 to 2026-01) on integrating LLMs with evidence-based Chinese medicine. [[DOI](https://doi.org/10.1016/j.imr.2026.101349)]
- [*Journal of Pharmaceutical Analysis*] **Xu et al. 2026: 基于 LLM 的中医智能问答系统综述** Review of intelligent TCM question-answering systems based on LLMs (KG-QA to LLM-QA and RAG). [[DOI](https://doi.org/10.1016/j.jpha.2025.101406)]
- [*Artificial Intelligence Review*] **Wu et al. 2026: AI 在中药材中的应用综述** Full-stack survey of AI in TCM herbs — compounds, targets, quality control, with an LLM section. [[DOI](https://doi.org/10.1007/s10462-026-11513-w)]
- [*Information*] **Lu et al. 2026: 深度学习中医诊断方法学质量审计** Systematic review and validation-gap analysis of deep learning for TCM disease diagnosis. [[DOI](https://doi.org/10.3390/info17060554)]
- [*ACL 2026*] **LLM-Based Multi-Agent Systems for Clinical Workflows（ACL 2026，邻近）** Adjacent ACL 2026 survey of workflow-level multi-agent clinical systems with a four-layer evaluation stack; no TCM coverage but methodologically isomorphic process-evaluation claims. [[DOI](https://doi.org/10.18653/v1/2026.acl-long.2123)]
- [*Chinese Medicine*] **Han et al. 2026: LLM 在中医中的调优与临床应用（Scoping Review）** PRISMA-ScR scoping review (27 studies to 2025-05) on tuning (LoRA/CPT/RAG) and clinical application of TCM LLMs. [[DOI](https://doi.org/10.1186/s13020-026-01346-8)]
- [*Chinese Medicine*] **Guo et al. 2026: AI 与多模态数据融合推动中医现代化** Panoramic AI review (ML/DL/KG/NLP/LLM) for TCM modernization with multimodal data integration. [[DOI](https://doi.org/10.1186/s13020-025-01194-y)]
- [*Journal of Integrative Medicine*] **Deep learning in TCM（J Integr Med）** Single-technology review of deep learning in TCM: medical imaging, herbal material research, data mining (J. Integr. Med. 2026;24(4):471-480). [[DOI](https://doi.org/10.1016/j.joim.2026.03.001)]
- [*OSF Preprints*] **Cong H et al. TCM×LLM 综述（OSF 预印本）** OSF-preprint review of LLMs in TCM (not peer-reviewed; archival). [[DOI](https://doi.org/10.17605/osf.io/5z367)]
- [*Science of Traditional Chinese Medicine*] **Chen et al. 2026: LLM 在中医的下一步（叙述性综述）** Narrative review on the next step of LLMs in TCM — multimodality, agents, and clinical translation. [[DOI](https://doi.org/10.1097/st9.0000000000000109)]
- [*OSF Preprints*] **Cai R et al. TCM×LLM scoping review（OSF 预印本）** OSF-preprint scoping review of LLMs in TCM (not peer-reviewed; archival). [[DOI](https://doi.org/10.17605/osf.io/2hyeq)]
- [*Pharmacological Research - Modern Chinese Medicine*] **AI in TCM: multimodal data to pharmacology and clinical decision（PRMCM 综述）** Broad AI-in-TCM review from multimodal data integration to pharmacological research and clinical decision support (Pharmacol. Res. Mod. Chin. Med. 2026; found in the third-round scan). [[DOI](https://doi.org/10.1016/j.prmcm.2026.100842)]
- [*Research*] **AI in TCM: Unraveling Herbal Medicine's Mechanisms（Research）** Broad AI-in-TCM review arguing AI should move beyond correlational analysis toward reconstructing the biological logic of syndrome differentiation and formula compatibility (Research 2026;9:1224). [[DOI](https://doi.org/10.34133/research.1224)]
- [*Journal of Integrative Medicine*] **AI empowers the innovation of TCM（J Integr Med 评论）** Single-author perspective on AI for TCM innovation: classics mining, diagnosis standardization, drug R&D cycles (J. Integr. Med. 2026). [[DOI](https://doi.org/10.1016/j.joim.2026.05.004)]
- [*Chinese Medicine and Culture*] **AI and Big Data in TCM Standardization and Internationalization（Chin Med Cult）** Perspective on AI and big data for TCM standardization and internationalization (Chin. Med. Cult. 2026, ahead of print). [[DOI](https://doi.org/10.1097/mc9.0000000000000203)]

</details>

<details>
<summary>2025 · 15</summary>

- [*Chinese Medicine*] **古籍知识图谱×多智能体融合综述（Chin Med）** Challenges-and-prospects review of knowledge-graph construction over ancient TCM classics, first to frame multi-agent convergence in this area (Chin. Med. 2025;20:168). [[DOI](https://doi.org/10.1186/s13020-025-01226-7)]
- [*智能系统学报*] **医疗领域的大型语言模型综述（智能系统学报，邻近）** Adjacent Chinese general survey of medical LLMs (training pipeline, strategies, scenarios, challenges), a superset-context reference for TCM LLM surveys. [[DOI](https://doi.org/10.11992/tis.202405003)]
- [*智能系统学报*] **医学大语言模型的研发与应用系统综述（智能系统学报，邻近）** Adjacent systematic review of 129 medical-domain LLMs (to 2024-06) and four clinical application categories; methodologically comparable search protocol. [[DOI](https://doi.org/10.11992/tis.202410020)]
- [*中华中医药学刊*] **人工智能实现中医四诊的发展现状、问题及解决路径（中华中医药学刊）** Short Chinese review of AI-based four-diagnosis objectification: face/tongue acquisition, electronic nose, pulse sensing, and low fusion of multi-diagnosis data (bibliographic record only). [[Paper](https://www.sinomed.ac.cn/article.do?ui=2026106036)]
- [*AI Medicine*] **Zhang et al. 2025: 中医 LLM 短综述与展望** Short survey and outlook on TCM LLM models and tasks. [[DOI](https://doi.org/10.53941/aim.2025.100003)]
- [*Journal of Evidence-Based Medicine*] **Yip et al. 2025: 中西医结合 LLM 进展与挑战** Review of LLMs in integrative medicine — progress, challenges, and opportunities. [[DOI](https://doi.org/10.1111/jebm.70031)]
- [*American Journal of Chinese Medicine*] **Wang et al. 2025: AI 驱动中医诊断模型进展** Systematic review of AI-driven TCM diagnostic models (four-diagnosis objectification, pattern differentiation). [[DOI](https://doi.org/10.1142/S0192415X25500259)]
- [*Journal of Pharmaceutical Analysis*] **The integration of machine learning into TCM（J Pharm Anal）** Review of machine-learning integration into TCM along diagnostic objectification and mechanism-elucidation lines (J. Pharm. Anal. 2025;15(8):101157). [[DOI](https://doi.org/10.1016/j.jpha.2024.101157)]
- [*American Journal of Chinese Medicine*] **Shataer et al. 2025: LLM 在中医应用（State-of-the-Art Review）** State-of-the-art review scanning TCM LLM application scenarios (care, education, translation, research). [Centre for Intelligent Healthcare, Coventry University, Coventry CV1 5RW, UK] [[DOI](https://doi.org/10.1142/S0192415X25500375)]
- [*Journal of Evidence-Based Medicine*] **Ren et al. 2025: 中医大语言模型（Scoping Review）** Arksey-O'Malley scoping review (29 studies to 2024-04) covering knowledge management, assisted care, and exam accuracy. [Institute of Health Data Science Lanzhou University Lanzhou China, Institute of Global Health University of Geneva Geneva Switzerland] [[DOI](https://doi.org/10.1111/jebm.12658)]
- [*Pharmacological Research*] **Meng et al. 2025: 大模型+虚拟细胞助力中医变革** Review of large models and virtual cells aiding modern analysis of stroke treatment with TCM formulas. [[DOI](https://doi.org/10.1016/j.phrs.2025.107953)]
- [*Healthcare*] **Intelligent Question-Answering Systems in Healthcare（Healthcare，邻近）** Adjacent review (not TCM-specific): 2018-2025 healthcare QA survey with CiteSpace bibliometrics, explicitly covering TCM formula-development scenarios (Healthcare 2025). [[DOI](https://doi.org/10.3390/healthcare13182269)]
- [*Journal of Evidence-Based Medicine*] **Guo et al. 2025: GPT 能否加速中医智能诊疗（综述+实证）** Survey plus empirical analysis of whether GPTs can accelerate intelligent TCM diagnosis and treatment. [Xiyuan Hospital China Academy of Chinese Medicinal Sciences Beijing China] [[DOI](https://doi.org/10.1111/jebm.70004)]
- [*Acupuncture and Herbal Medicine*] **Chen et al. 2025: 中医大语言模型系统综述** Systematic review of 10 studies (to mid-2024) on LLMs in TCM generative tasks. [Italian National Institute of Health, Rome, Italy] [[DOI](https://doi.org/10.1097/HM9.0000000000000143)]
- [*Current Medical Science*] **AI for Spleen-Stomach Disorders in TCM（Curr Med Sci）** Single-disease-area (spleen-stomach) review of KG plus intelligent diagnosis/treatment with a symptom-syndrome-disease-formula framework (Curr. Med. Sci. 2025;45(6)). [[DOI](https://doi.org/10.1007/s11596-025-00128-x)]

</details>

<details>
<summary>2024 · 5</summary>

- [*计算机工程与应用*] **Su et al. 2024 — Review of AI in TCM diagnosis and treatment (Chinese)** Chinese-language review of three AI stages in TCM care — expert systems, ML, and deep learning — with challenges. [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2312-0400)]
- [*南京中医药大学学报*] **Li et al. 2024 — Research progress and prospects of LLMs in TCM (Chinese)** Chinese-language review of TCM LLM pipelines, frontier techniques (prompting/RAG/RLHF), and application prospects. [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1393)]
- [*Computers in Biology and Medicine*] **Tian et al. 2024: 四诊机器学习综述** Review of machine learning for TCM four diagnoses — inspection, auscultation-olfaction, inquiry, and palpation. [[DOI](https://doi.org/10.1016/j.compbiomed.2024.108074)]
- [*中国工程科学*] **Song et al. 2024: AI 辅助中医辨证关键问题与技术挑战** Strategic-study review of key issues in AI-assisted TCM syndrome differentiation — multimodal fusion, symptom association, pattern quantification and reasoning, and TCM LLMs. [[DOI](https://doi.org/10.15302/J-SSCAE-2024.02.010)]
- [*Computer Materials & Continua*] **Qu et al. 2024: 中医知识图谱综述** Review of knowledge graphs in TCM — analysis, construction, applications, and prospects. [[DOI](https://doi.org/10.32604/cmc.2024.055671)]

</details>

<details>
<summary>2021 · 1</summary>

- [*Computers in Biology and Medicine*] **Zhang et al. 2021: 计算中医诊断文献综述** Literature survey of computational TCM diagnosis — symptom acquisition, pattern modeling, and systems. [[DOI](https://doi.org/10.1016/j.compbiomed.2021.104358)]

</details>

<details>
<summary>2020 · 1</summary>

- [*Artificial Intelligence in Medicine*] **Chu et al. 2020: 中医定量知识表示模型综述** Review of quantitative knowledge representation models of TCM (ontologies, rules, statistics). [[DOI](https://doi.org/10.1016/j.artmed.2020.101810)]

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

- [*Computer Methods and Programs in Biomedicine*] **Lukman et al. 2007: 中医计算方法综述** Foundational survey of computational methods for TCM (expert systems, ML, data mining). [[DOI](https://doi.org/10.1016/j.cmpb.2007.09.008)]

</details>


</details>

## Patents

TCM LLM, knowledge-graph, RAG, inquiry, and prescription-recommendation system patents worldwide—not a dump of herbal-formula patents.

<details>
<summary>22 patents, grouped by publication year</summary>

<details>
<summary>2026 · 11</summary>

- [*CN122529089A*] **TCM dialogue generation with a large language model and long-term memory** Generates personalized TCM dialogue from a long-term memory bank and user portrait (published, not granted). [Hangzhou Wangchai Technology] [[Patent](https://patents.google.com/patent/CN122529089A/zh)]
- [*CN122436154A*] **Digital inheritance and analysis of Zhang Xichun's theory, method, formula, and herbs** Rule engine plus three-way retrieval and an LLM for Zhang Xichun school analysis (published, not granted). [Guangzhou Zhiyun Caotang Medical Technology] [[Patent](https://eureka.patsnap.com/patent/CN122436154A)]
- [*CN122025029A*] **Causal contrastive learning and LLM graph attention for TCM prescription recommendation** Heterogeneous and homogeneous symptom-herb graphs plus an LLM-enhanced causal mechanism (published, not granted). [Huzhou University] [[Patent](https://eureka.patsnap.com/patent/CN122025029A)]
- [*CN122050861A*] **TCM diagnosis-and-treatment platform combining an LLM with dual-channel retrieval** LLM plus TCM knowledge-graph dual-channel retrieval for inheriting master-physician experience and generating formulas (published, not granted). [Yueyang Hospital of Integrated Traditional Chinese and Western Medicine, SHUTCM] [[Patent](https://patents.google.com/patent/CN122050861A/zh)]
- [*CN122117314A*] **LLM-based intelligent acupuncture diagnosis agent** Acupuncture knowledge bases, graph, vector search and reranking, with an LLM agent that classifies questions and asks follow-ups (published, not granted). [Henan University of Technology] [[Patent](https://eureka.patsnap.com/patent/CN122117314A)]
- [*CN122091073A*] **Multi-task joint optimization for TCM prescription generation** A pretrained LLM predicts herb sequences and herb sets jointly, with extra weight on rare herbs (published, not granted). [Hangzhou Dianzi University] [[Patent](https://eureka.patsnap.com/patent/CN122091073A)]
- [*CN121862376A*] **Knowledge-graph and LLM system for TCM syndrome-differentiation QA** Chunks classics and cases, extracts a graph, then retrieves local and global keywords for syndrome-differentiation answers (published, not granted). [Nanjing University of Posts and Telecommunications] [[Patent](https://patents.google.com/patent/CN121862376A/zh)]
- [*CN121687367A*] **Structured evidence-subgraph RAG for TCM herb recommendation** Multi-hop evidence subgraphs plus Hopfield associative retrieval for herb recommendation, with graph constraints against hallucination (published, not granted). [Zhejiang Chinese Medical University] [[Patent](https://patents.google.com/patent/CN121687367A/zh)]
- [*CN121743505A*] **Knowledge-enhanced generation of TCM case commentaries** Retrieves knowledge-graph subgraphs, then writes case notes along etiology, treatment principles, formulas, and prognosis (published, not granted). [Zhejiang University] [[Patent](https://patents.google.com/patent/CN121743505A/zh)]
- [*CN121480736A*] **Knowledge-distillation and RL for oncology TCM prescription recommendation** Distills GPT-4o into a Qwen student, then DPO, for interpretable oncology TCM prescriptions (published, not granted). [Nanjing University of Chinese Medicine] [[Patent](https://patents.google.com/patent/CN121480736A/zh)]
- [*CN121436134A*] **Multimodal knowledge-graph construction from TCM texts and records** An LLM extracts triples from TCM texts, then fuses a real-world case layer into a multimodal graph (published, not granted). [Hangzhou Ganzhicao Technology] [[Patent](https://patents.google.com/patent/CN121436134A/zh)]

</details>

<details>
<summary>2025 · 6</summary>

- [*CN120690391B*] **Knowledge-graph recommendation of classic TCM formulas** Maps colloquial symptoms to terms, filters by constitution, and recommends classic formulas (granted). [Shunfu Technology Group] [[Patent](https://patents.google.com/patent/CN120690391B/zh)]
- [*CN120108694A*] **Knowledge-graph and case-enhanced RAG for intelligent TCM inquiry** Leiden subgraph search plus hybrid global/local recall, then a single LLM response (published, not granted). [Jiangsu University] [[Patent](https://patents.google.com/patent/CN120108694A/zh)]
- [*CN120221058A*] **Multimodal knowledge-graph and LLM system for TCM rehabilitation diagnosis** Aligns tongue, pulse, and inquiry features with knowledge-graph embeddings before a rehabilitation expert LLM (published, not granted). [Zhejiang Chinese Medical University] [[Patent](https://patents.google.com/patent/CN120221058A/zh)]
- [*CN120067279B*] **AI-LLM method and system for intelligent TCM inquiry** Multimodal inquiry fusing face/body/tongue images, speech prosody, and a disease library (granted). [Yi Mai Artificial Intelligence Medical Technology (Tianjin)] [[Patent](https://patents.google.com/patent/CN120067279B/zh)]
- [*CN119763764A*] **LLM-based Chinese-medicine prescription recommendation with soft prompts** Soft prompts and cross-attention feed patient text into an LLM for controllable herb recommendations (published, not granted). [Hangzhou Ganzhicao Technology] [[Patent](https://patents.google.com/patent/CN119763764A/zh)]
- [*CN119416782A*] **LLM method for learning famous-physician TCM formulas** Aligns classical-Chinese case terms with vernacular text using models such as Qwen (published, not granted). [Chengdu Byte Stream Technology] [[Patent](https://patents.google.com/patent/CN119416782A/zh)]

</details>

<details>
<summary>2024 · 5</summary>

- [*CN119149754A*] **LLM and knowledge-graph method for TCM formula compatibility** Pairs a TCM LLM with a knowledge graph for formula compatibility (published, not granted). [Tianjin University, Tianda Zhitu (Tianjin) Technology] [[Patent](https://patents.google.com/patent/CN119149754A/zh)]
- [*CN119092157B*] **LLM-based Chinese-materia-medica question answering** Chinese-materia-medica QA fine-tuned from Baichuan2-7B-Chat (granted February 2025). [Zhejiang University, Yangtze River Delta Wisdom Oasis Innovation Center] [[Patent](https://patents.google.com/patent/CN119092157B/zh)]
- [*CN118838996A*] **Building a TCM QA system from a large language model and a knowledge graph** Closed loop of LLM generation and knowledge-graph completion for TCM QA (published, not granted). [Beijing Institute of Technology, BIT Tangshan Research Institute] [[Patent](https://patents.google.com/patent/CN118838996A/zh)]
- [*CN118230893A*] **AI-large-model system for intelligent TCM prescription recommendation** Trains an AI large model on medical records to recommend personalized TCM prescriptions, wired into a hospital IS (published, not granted). [Hangzhou Ganzhicao Technology] [[Patent](https://patents.google.com/patent/CN118230893A/zh)]
- [*CN117828050B*] **Long-document retrieval-augmented generation for TCM question answering** Long-document RAG (expansion, recall, reranking, source citations) for TCM QA (granted July 2024). [Beijing Zhipu Huazhang Technology] [[Patent](https://patents.google.com/patent/CN117828050B/zh)]

</details>


</details>

## Papers

Methods, evaluations, and systems only. Named domain LLMs live under Open models.

<details>
<summary>Agents (11): 问诊流程、多智能体</summary>

- [*arXiv*] **DeepTCM1.0** DeepTCM1.0: 11-expert multi-agent system on DeepSeek V3.2 for interpreting TCM formula mechanisms (Guizhi Decoction case); now on arXiv after the Research Square preprint. [Chinese Medicine Guangdong Laboratory (Hengqin), Changzhi Medical College] [[Paper](https://arxiv.org/abs/2608.18103)] [[Preprint](https://doi.org/10.21203/rs.3.rs-9844166/v1)]
- [*arXiv*] **DeepRoot** Multi-agent pipeline that turns the Shen Nong Ben Cao Jing into a verified Neo4j graph for therapeutic reasoning; code and evaluation scripts are public. [[Paper](https://arxiv.org/abs/2606.15931)] [[Code](https://github.com/CarlisleMa/deeprootv1)]
- [*Journal of Pharmaceutical Analysis*] **TCM-Agent** LLM multi-agent system for network pharmacology and herbal discovery. [[Paper](https://doi.org/10.1016/j.jpha.2026.101581)] [[Code](https://github.com/AITCM/TCM-Agent)]
- [*arXiv*] **MACAT** Multi-agent culture-aware translation framework, evaluated on culture-loaded terms from TCM classics and the Analects. [[Paper](https://arxiv.org/abs/2606.01276)]
- [*Applied Sciences*] **KM-Agent** Tool-augmented agent for Korean / East Asian traditional medicine over 4,780 herb–syndrome–acupoint metadata records, evaluated on TCMBench-style sets. [[Paper](https://www.mdpi.com/2076-3417/16/7/3377)] [[Code](https://github.com/wonyung-lee/km-agent)]
- [*arXiv*] **DERM-3R** Resource-constrained multimodal multi-agent framework for TCM dermatology (recognition / representation / SDT agents). [[Paper](https://arxiv.org/abs/2604.09596)]
- [*arXiv*] **CORE-Acu** Acupuncture clinical decision support with structured reasoning traces and a knowledge-graph safety veto loop. [[Paper](https://arxiv.org/abs/2603.08321)]
- [*arXiv*] **Jingfang** LLM-based multi-agent TCM diagnosis/treatment system reporting large relative SDT gains under the authors' protocol. [[Paper](https://arxiv.org/abs/2502.04345)]
- **RenShu-AI** FastAPI + LangGraph multi-agent TCM consultation system combining GraphRAG and DeepSeek-TCM. [[Code](https://github.com/yanlinPeng-code/RenShu-AI)]
- [*Information*] **TCM compound retrieval agent** AI agent-based system for retrieving TCM compound information. [Zhengzhou University] [[DOI](https://doi.org/10.3390/info16070543)]
- [*Journal of King Saud University Computer and Information Sciences*] **DiagX-DT** Exclusionary syndrome-differentiation reasoning with CoT and an external TCM knowledge base. [[DOI](https://doi.org/10.1007/s44443-025-00123-1)]

</details>

<details>
<summary>Multimodal (4): 舌、面、脉</summary>

- [*ICASSP 2025*] **Few-shot tongue-diagnosis in-context multitask learning** Few-shot in-context multitask fine-tuning of LLMs mapping tongue images directly to constitutions. [Northeastern University] [[DOI](https://doi.org/10.1109/ICASSP49660.2025.10887764)]
- [*arXiv*] **TCDiff** Triplet cascaded diffusion model generating high-fidelity multimodal TCM EHRs, with the **TCM-SZ1** benchmark dataset. [[Paper](https://arxiv.org/abs/2508.01615)]
- **Chinese-LLaVA-Med** Chinese medical multimodal LLM based on the LLaVA architecture, with the llava-med-zh-eval benchmark and open 7B weights. [[Code](https://github.com/BUAADreamer/Chinese-LLaVA-Med)]
- **XrayGLM** Chinese multimodal medical LLM for chest X-ray interpretation. [[Code](https://github.com/WangRongsheng/XrayGLM)]

</details>

<details>
<summary>RAG / knowledge graphs (27): 检索和医案、方剂图谱</summary>

<details>
<summary>2026 · 6</summary>

- [*Communications in Computer and Information Science (Springer)*] **Hybrid Retrieval + Re-ranking TCM Prescription Generation** Hybrid retrieval with re-ranking to enhance LLM-based TCM prescription generation (Springer CCIS conference paper). [[Paper](https://doi.org/10.1007/978-981-92-3563-6_21)]
- [*arXiv*] **Evidence-Based TCM Visualization Diagnosis System** Evidence-based TCM visualization diagnosis system: Neo4j knowledge graph (241 patterns, 1,263 symptoms) with four-stage symptom matching (LLM-verified) and information-gain-driven active inquiry. [[Paper](https://arxiv.org/abs/2606.06869)]
- **Pediatric influenza Chinese patent-medicine recommender (KG + LLM)** Knowledge graph of Chinese patent medicines for pediatric influenza built from authoritative guidelines and integrated with an LLM (JMIR Preprints). [[Preprint](https://doi.org/10.2196/preprints.101648)]
- [*Frontiers in Medicine*] **Jin San Zhen KG-QA** Knowledge graph + LLM QA tool for the Jin San Zhen acupuncture school. [Guangzhou University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1755583)]
- [*Frontiers in Medicine*] **Tree-organized self-reflective retrieval for TCM QA** Tree-organized self-reflective retrieval for TCM question answering (Frontiers in Medicine 2026). [[DOI](https://doi.org/10.3389/fmed.2026.1752778)]
- [*Frontiers in Medicine*] **TCM-DiffRAG** Syndrome-differentiation RAG with a general KG, a personalized KG, and chain-of-thought. [Guangdong Institute of Intelligence Science and Technology, Zhuhai, Hangzhou Ganzhicao Technology Co., Ltd, BoardWare Information System Limited] [[Published](https://doi.org/10.3389/fmed.2026.1804478)] [[Paper](https://arxiv.org/abs/2602.22828)] [[Code](https://github.com/LiJianmin6706/Tcm_Diff_RAG)]

</details>

<details>
<summary>2025 · 12</summary>

- [*IEEE BIBM 2025*] **Chinese patent medicine knowledge system** Constructing a knowledge system for traditional Chinese patent medicine using LLMs and KGs. [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356149)]
- [*数据分析与知识发现*] **中医药标准知识问答系统** Retrieval-augmented QA system for TCM standards knowledge, built and evaluated in practice. [China Academy of Chinese Medical Sciences et al.] [[DOI](https://doi.org/10.11925/infotech.2096-3467.2024.0747)]
- [*Frontiers in Medicine*] **中医医案问答系统** A TCM case-based QA system integrating LLMs and knowledge graphs for efficient case retrieval and analysis (Front. Med. 2025). [[DOI](https://doi.org/10.3389/fmed.2024.1512329)]
- [*JMIR Medical Informatics*] **Yaoshi-RAG** Uncertain-KG RAG for medicine–food homology dietary recommendation with personalization and explainability. [[DOI](https://doi.org/10.2196/75279)]
- [*Frontiers in Pharmacology*] **TCMRD-KG** Innovative design of a rheumatology TCM knowledge graph from ancient literature. [Beijing University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fphar.2025.1535596)]
- [*Digital Chinese Medicine*] **TCMLCM** KG2T-based intelligent QA model for TCM lung cancer. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2025.03.011)]
- **TCM-Sage** Evidence-synthesis RAG assistant for TCM practitioners (hybrid vector + knowledge graph). [[Code](https://github.com/AndyZHENG0715/TCM-Sage)]
- [*Pharmacological Research*] **RAG-CPMF** Multi-LLM verification + RAG for Chinese patent medicine recommendation, with a living public CPM dataset. [[DOI](https://doi.org/10.1016/j.phrs.2025.107883)] [[Data](https://gitee.com/tcmdoc/cpm)]
- [*arXiv*] **OpenTCM** GraphRAG TCM retrieval and diagnosis system with a gynecology classics knowledge graph. [[Paper](https://arxiv.org/abs/2504.20118)] [[Code](https://github.com/OpenTCM01/OpenTCM)]
- [*IEEE BIBM*] **MRD-RAG** Multi-round diagnostic RAG simulating clinical reasoning; builds **DiagnosGraph** spanning TCM and Western medicine (876 diseases / 7,997 nodes / 37,201 triples). [[Published](https://doi.org/10.1109/bibm66473.2025.11357107)] [[Paper](https://arxiv.org/abs/2504.07724)]
- [*Interdisciplinary Sciences*] **LLM-driven TCM KG construction** LLM-driven construction and application of a TCM knowledge graph. [Henan University of Technology] [[DOI](https://doi.org/10.1007/s12539-025-00735-1)]
- [*Journal of Medical and Biological Engineering*] **LLM + RAG TCM inference** Combining LLMs with RAG for TCM inference. [Taipei City Hospital] [[DOI](https://doi.org/10.1007/s40846-025-00988-7)]

</details>

<details>
<summary>2024 · 8</summary>

- [*JMIR Medical Informatics*] **中医领域知识图谱补全** Domain knowledge graph completion and quality evaluation for Traditional Chinese Medicine. [[DOI](https://doi.org/10.2196/55090)]
- [*南京中医药大学学报*] **中医药问答大语言模型** TCM QA LLM combining RAG with P-Tuning v2 fine-tuning on ChatGLM2-6B. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1375)]
- [*计算机科学与探索*] **中医药大模型知识增强方法** Knowledge augmentation for TCM LLMs — a graph built from ~100k classical formulas preserving prescription structure. [Tianjin University] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2407082)]
- [*Methods of Information in Medicine*] **TCMSF** TCMSF: a construction framework for a TCM syndrome ancient-book knowledge graph that organizes syndrome knowledge from classical texts in a structured, semantically oriented way (Methods Inf. Med. 2024). [[DOI](https://doi.org/10.1055/a-2590-6348)]
- [*EIECC*] **TCM MLKG-RAG** TCM intelligent diagnosis based on multi-layer knowledge graph retrieval-augmented generation. [[DOI](https://doi.org/10.1109/EIECC64539.2024.10929529)]
- [*OSF Preprints（预印本）*] **RAG 增强中医问答置信度** Implementing retrieval-augmented generation to build LLM confidence in TCM (preprint). [[DOI](https://doi.org/10.31219/osf.io/ns2v3)]
- [*Electronics*] **LLM 构建中医知识图谱** Constructing Traditional Chinese Medicine knowledge graphs based on large language models. [[DOI](https://doi.org/10.3390/electronics13071395)]
- [*Database (Oxford)*] **ACUBERT** ACUBERT for meridian entity recognition and classification in acupuncture indication knowledge bases. [Nanjing KG Data Technology] [[DOI](https://doi.org/10.1093/database/baae083)]

</details>

<details>
<summary>2023 · 1</summary>

- [*计算机科学与探索*] **大模型融合知识图谱问答系统** Vertical-domain QA system deeply integrating LLMs with knowledge graphs for TCM formulas. [Tianjin University] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2308070)]

</details>


</details>

<details>
<summary>Prescription (11): 荐药、组方、药对</summary>

- [*arXiv*] **Patient-Conditioned Dual Hypergraph Reasoning** Patient-conditioned dual-hypergraph reasoning for auditable TCM prescription support, organizing symptom/tongue/pulse evidence around patterns and treatment principles (Tianjin University). [[Paper](https://arxiv.org/abs/2607.04025)]
- [*KSII Transactions on Internet and Information Systems*] **GAT+LLM TCM Prescription Generation** Intelligent TCM prescription generation combining graph attention networks with LLMs (formally published in KSII TIIS). [[DOI](https://doi.org/10.3837/tiis.2026.05.006)]
- [*Chinese Medicine*] **TCMNet** LLM-assisted disease knowledge mining with PPI networks and binding prediction for formula optimization. [Zhejiang Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1186/s13020-026-01360-w)]
- [*Digital Chinese Medicine*] **CMM-EmbedCluster** LLM + medicinal-property-theory clustering framework for Chinese materia medica, with a 567-herb property knowledge base. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2026.05.010)]
- [*IEEE Journal of Biomedical and Health Informatics*] **LLM herb–drug interaction prediction** LLM-enhanced herbal medicine–drug interaction prediction. [Shenzhen University] [[DOI](https://doi.org/10.1109/jbhi.2025.3558667)]
- [*JMIR Medical Informatics*] **Weighted-voting TCM formula classification** Weighted-voting LLM approach for TCM formula classification. [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.2196/69286)]
- [*IEEE BIBM*] **TCM-FTP** Fine-tuning LLMs for herbal prescription prediction. [[DOI](https://doi.org/10.1109/BIBM62325.2024.10822451)]
- [*JAMIA*] **PresRecST** Progressive herb-prescription recommendation following syndrome differentiation then treatment planning (JAMIA 2024); ships a public encoded TCM-Lung subset and a TCM-PD reproduction table. [[DOI](https://doi.org/10.1093/jamia/ocae066)] [[Code](https://github.com/2020MEAI/PresRecST)]
- [*IEEE BIBM*] **中医方剂 LLM 分类** Fine-tuned LLMs with refined prompt templates for TCM formula classification, using data sources such as the national medical-insurance catalog of proprietary Chinese medicines (IEEE BIBM 2023). [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385776)]
- [*IEEE Access*] **PreGenerator** TCM prescription recommendation model combining retrieval and generation. [College of Physics, Taiyuan University of Technology, Taiyuan, China, North Automatic Control Technology Institute, Taiyuan, China] [[DOI](https://doi.org/10.1109/ACCESS.2023.3316219)]
- [*IEEE BIBM*] **LLM+GNN 中医处方推荐** TCM prescription recommendation combining large language models with graph neural networks. [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385489)]

</details>

<details>
<summary>Extraction / PLM (5): NER、关系抽取、BERT 类编码器</summary>

- [*Applied Intelligence*] **KDC-NER** Knowledge-guided data augmentation + LLM fine-tuning framework for nested NER in TCM. [Jiangxi University of Chinese Medicine] [[DOI](https://doi.org/10.1007/s10489-026-07095-3)]
- [*npj Digital Medicine*] **LM extraction for complementary medicine** Language models for data extraction and risk-of-bias assessment in complementary medicine literature. [Lanzhou University] [[DOI](https://doi.org/10.1038/s41746-025-01457-w)]
- [*Scientific Reports*] **双通道知识注意力辨证模型** Dual-channel knowledge-attention NLP model for TCM syndrome differentiation, addressing rare characters and terminology extraction. [[DOI](https://doi.org/10.1038/s41598-025-96404-w)]
- [*Journal of the American Medical Informatics Association*] **LLM 腧穴定位关系抽取** Relation extraction with LLMs — a case study on acupuncture point locations. [The University of Texas MD Anderson Cancer Center , Houston, TX 77030] [[DOI](https://doi.org/10.1093/jamia/ocae233)]
- [*Frontiers in Artificial Intelligence*] **Evi-BERT** Automated information-extraction model (Evi-BERT) enhancing RCT evidence extraction for TCM. [[DOI](https://doi.org/10.3389/frai.2024.1454945)]

</details>

<details>
<summary>Evaluation (39): 基准和考试；要下载评测集走下面「数据集」</summary>

<details>
<summary>2026 · 14</summary>

- [*Future Internet (MDPI)*] **RAG+LoRA 中医执照考试推理架构** RAG+LoRA generative architecture with an 11,476-item Taiwan TCM licensing-exam dataset (2005-2025), raising accuracy from 61.0% to 89.0%+ (Future Internet, MDPI). [[DOI](https://doi.org/10.3390/fi18060280)]
- [*Frontiers in Plant Science*] **Medicinal-plant MLLM benchmark** Benchmarking multimodal LLMs for medicinal plant identification. [Shaoxing University] [[DOI](https://doi.org/10.3389/fpls.2026.1765281)]
- [*arXiv*] **LingLan** Large multi-task TCM benchmark: 5 domains, 13 subtasks, 25,624 instances. [Beijing Jiaotong University et al.] [[Paper](https://arxiv.org/abs/2602.01779)] [[Code](https://github.com/TCMAI-BJTU/LingLan)] [[Website](http://tcmnlp.com)]
- [*Journal of Evidence-Based Medicine*] **Large vs lightweight LLMs on TCM exams** Systematic comparison of large-scale vs lightweight LLMs on TCM exam questions. [First Affiliated Hospital of Henan University] [[DOI](https://doi.org/10.1111/jebm.70118)]
- [*Expert Systems with Applications*] **End-to-end TCM clinical support benchmark** Benchmark for end-to-end TCM clinical support across the full LLM care pipeline. [East China Normal University] [[DOI](https://doi.org/10.1016/j.eswa.2026.132267)]
- [*Journal of Traditional Chinese Medical Sciences*] **TCM intelligent pre-consultation clinical evaluation** Tertiary-hospital clinical evaluation of an LLM intelligent pre-consultation system using a physician–AI–patient triad model. [Beijing Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.jtcms.2026.06.002)]
- [*Frontiers in Medicine*] **TCM AI-tutor evaluation** Multimodal LLM evaluation for TCM education across cognitive levels. [Beijing University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1893231)]
- [*Scientific Reports*] **Three-LLM TCM licensing exam evaluation** Systematic evaluation of 3 LLMs (incl. Gemini) on the national TCM medical licensing examination. [Shanghai Jiao Tong University] [[DOI](https://doi.org/10.1038/s41598-026-49200-z)]
- [*arXiv*] **TongueDx2** Systematic ablation of the tongue-diagnosis DL design space (20+ model variants); TongueDx2 includes 5,109 images / 976 expert annotations. [[Paper](https://arxiv.org/abs/2607.28148)]
- [*Frontiers in Artificial Intelligence*] **TCMI-F-6D** Six-dimensional benchmark of interdisciplinary foundational competence in TCM informatics. [Anhui University of Chinese Medicine] [[DOI](https://doi.org/10.3389/frai.2026.1780967)] [[Code](https://github.com/123adf-dev/TCMI-F-6D-Benchmark)]
- [*ICIC 2026*] **TCMBenchEval** Benchmark evaluating LLMs on real clinical TCM case records (ICIC 2026). [Shantou University] [[DOI](https://doi.org/10.1007/978-981-92-3498-1_1)]
- **Med-Bench-Arena** Open evaluation platform for medical and TCM LLMs/Agents (HF/vLLM/LiteLLM, multimodal, TCM-specific metrics), from the ZhongJing team. [[Code](https://github.com/pariskang/Med-Bench-Arena)]
- [*arXiv*] **MMIR-TCM** Memory-augmented multimodal tongue diagnosis and clinical decision framework; proposes MedTCM dataset and TDEU metric. [[Paper](https://arxiv.org/abs/2607.01814)]
- [*Pattern Recognition*] **ATCMD-Bench** First agentic TCM diagnosis benchmark, evaluating LLMs through multi-agent simulated consultations. [South China University of Technology] [[DOI](https://doi.org/10.1016/j.patcog.2026.113679)]

</details>

<details>
<summary>2025 · 16</summary>

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
- [*arXiv*] **New Snow Tablets** Reveals systematic flaws of general and TCM-specific LLMs that guess formula ingredients from drug names. [[Paper](https://arxiv.org/abs/2504.03786)]
- [*Scientific Data*] **MTCMB** Multi-task TCM benchmark (~12 subsets, ~7.1k samples) covering knowledge, reasoning, formulas, and safety. [[Paper](https://arxiv.org/abs/2506.01252)] [[Code](https://github.com/Wayyuanyuan/MTCMB)] [[Published](https://doi.org/10.1038/s41597-026-07967-w)]
- [*Preprints.org（预印本）*] **GPT 台湾中医执业考试评估** GPT-3.5/GPT-4/GPT-4o performance on the Taiwan TCM licensing examination with reliability analysis (preprint). [[DOI](https://doi.org/10.20944/preprints202501.1787.v1)]
- [*IJCNN 2025*] **From Metaphor to Mechanism** LLMs decode TCM metaphor / imagistic-thinking language and map it to modern medical concepts. [Shandong Normal University,Jinan,China, China Pharmaceutical University,Nanjing,China, The University of Tokyo,Tokyo,Japan, Universiti Tunku Abdul Rahman,Perak,Malaysia] [[Paper](https://arxiv.org/abs/2503.02760)] [[Published](https://doi.org/10.1109/ijcnn64981.2025.11228098)]

</details>

<details>
<summary>2024 · 7</summary>

- [*南京中医药大学学报*] **中医标准化评估基准** Standardized TCM evaluation benchmark of 29,506 questions across 13 subjects; tests 3 general and 5 Chinese medical LLMs. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1383)]
- [*arXiv*] **TCMD** TCMD, a TCM licensing-exam multiple-choice set for LLM evaluation (paper reports ~2,851 train / 600 test). Independent check found no official GitHub or Hugging Face download. [[Paper](https://arxiv.org/abs/2406.04941)]
- [*Journal of Translational Medicine*] **LLM 中医语言文化偏差研究** Comparing LLMs developed in different countries on TCM; highlights language/cultural bias and the need for localized models. [[DOI](https://doi.org/10.1186/s12967-024-05128-4)]
- [*Research Square（预印本）*] **GPT-4 中医研究生考试评估** GPT-4 vs mainstream Chinese LLMs on a TCM postgraduate examination dataset (preprint). [China Academy of Chinese Medical Science, Changchun University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.21203/rs.3.rs-4392855/v1)]
- [*J Integr Complement Med*] **GPT vs ERNIE 中医文化背景对比研究** A culture-framed comparison of GPT versus ERNIE on TCM tasks (J. Integr. Complement. Med. 2024). [College of Engineering, Boston University, Boston, MA, USA.] [[DOI](https://doi.org/10.1089/jicm.2024.0902)]
- [*arXiv*] **ChatGPT 中医知识理解探究** Evaluating ChatGPT's comprehension of Traditional Chinese Medicine knowledge. [[Paper](https://arxiv.org/abs/2403.09164)]
- [*Chinese Medicine and Culture*] **ChatGPT 中医交互可行性研究** Feasibility and challenges of interactive AI for TCM, using ChatGPT as an example. [[DOI](https://doi.org/10.1097/MC9.0000000000000103)]

</details>

<details>
<summary>2023 · 2</summary>

- **中医新冠文献 LLM 命名实体识别** Comparative study of LLMs for named entity recognition in TCM COVID-19 literature (preprint). [[DOI](https://doi.org/10.2196/preprints.54346)]
- [*JMIR Medical Education*] **ChatGPT 针灸教育研究** Comparative study of ChatGPT as a learning tool in acupuncture education. [[DOI](https://doi.org/10.2196/47427)]

</details>


</details>

<details>
<summary>Platforms / tools (4): 编目、门户、可运行工具</summary>

- [*arXiv*] **TCMIIES** TCMIIES: a browser-based, zero-installation LLM system for structured information extraction from academic literature, aimed at TCM and other specialty researchers. [[Paper](https://arxiv.org/abs/2605.07507)]
- [*Science of Traditional Chinese Medicine*] **TCM Data Hub (YiYuan)** YiYuan LLM-driven TCM data platform. [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.1097/st9.0000000000000118)]
- [*Cell Discovery*] **神农Alpha** ShennongAlpha (Westlake University): an AI-driven sharing and collaboration platform for intelligent curation, acquisition and translation of natural-medicinal-material knowledge (Cell Discov. 2025). [[DOI](https://doi.org/10.1038/s41421-025-00776-2)] [[Website](https://shennongalpha.westlake.edu.cn/)] [[Paper](https://www.nature.com/articles/s41421-025-00776-2)] [[Code](https://github.com/shennong-program/shennongname)]
- [*IJACSA*] **草药智能配送聊天机器人** Smarter herbal medication delivery system employing an AI-powered chatbot. [[DOI](https://doi.org/10.14569/ijacsa.2023.0140358)]

</details>

<details>
<summary>Other methods (6): 对齐、提示、专科任务</summary>

- [*Translation Review*] **Beyond the Poetic Bard（中医AI翻译评论）** Beyond the Poetic Bard: a perspective on accuracy, epistemology, and medical-context limits of generative-AI translation of TCM texts (Translation Review). [[DOI](https://doi.org/10.1080/07374836.2026.2679929)]
- [*Progress in Biochemistry and Biophysics*] **Pathogenesis-reasoning CoT supervision for spleen-stomach disorders** Pathogenesis-reasoning chain-of-thought supervision replacing fixed-label classification for spleen-stomach disease syndrome recognition and multi-dimensional evaluation (Prog. Biochem. Biophys.). [[Paper](https://www.pibb.ac.cn/pibbcn/article/abstract/20260141)]
- [*arXiv*] **中医提示工程框架** Prompt-engineering framework for LLM intelligent understanding in TCM. [[Paper](https://arxiv.org/abs/2410.19451)]
- [*arXiv*] **RLAIF 中医对齐** Enhancing LLMs' TCM capabilities through reinforcement learning from AI feedback. [[Paper](https://arxiv.org/abs/2411.00897)]
- [*Digital Chinese Medicine*] **BSG 中医智能问答** Intelligent QA system for TCM based on a BSG deep-learning model (prescription and materia medica cases). [[DOI](https://doi.org/10.1016/j.dcmed.2024.04.006)]
- [*IEEE BIBM*] **中医疫病防治问答模型** LLM-based QA model for TCM epidemic prevention and treatment. [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385748)]

</details>

<details>
<summary>Before LLMs (50): 专家系统、舌脉、本体、早期编码器</summary>

<details>
<summary>2020–2022 · 16</summary>

- [*Discover Applied Sciences*] **Mathematical modeling of Chinese medicine by complex-valued five-agent network** Historical anchor: Mathematical modeling of Chinese medicine by complex-valued five-agent network. [[DOI](https://doi.org/10.1007/s42452-025-06602-4)]
- [*Lv Q et al., *Signal Transduct Target Ther* 8(1):127*] **TCMBank** Historical anchor: TCMBank. [[DOI](https://doi.org/10.1038/s41392-023-01339-1)]
- [*Interdisciplinary*] **Historical Analysis of Medical Artificial Intelligence Development in China: Research Cent** Historical anchor: Historical Analysis of Medical Artificial Intelligence Development in China: Research Cent. [[DOI](https://doi.org/10.18926/interdisciplinary/65464)]
- [*Zhang Y et al., *Acta Pharm Sin B* 13(6):2559-2571*] **ETCM v2.0** Historical anchor: ETCM v2.0. [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)]
- [*Scientific Reports*] **Discovering golden ratio in the world’s first five-agent network in ancient China** Historical anchor: Discovering golden ratio in the world’s first five-agent network in ancient China. [[DOI](https://doi.org/10.1038/s41598-023-46071-6)]
- [*BioMed Research International*] **乙肝中医 KG 问答系统** Knowledge-graph-based QA system for TCM diagnosis and treatment of viral hepatitis B. [[DOI](https://doi.org/10.1155/2022/7139904)]
- [*CCL*] **ZY-BERT** Domain TCM encoder from the TCM-SD paper (~0.4B-token corpus); weights are on cloud drive, with syndrome-differentiation fine-tune code in the repo. Not the same work as arXiv 2411.00897. [[Paper](https://arxiv.org/abs/2203.10839)] [[Published](https://aclanthology.org/2022.ccl-1.80/)] [[Code](https://github.com/Borororo/ZY-BERT)]
- [*BioMed Research International*] **TCMPR 子网术语映射处方推荐** Herb-symptom knowledge graph (~18k entities / ~100k relations) plus subnetwork term mapping and a CNN for prescription recommendation. [[DOI](https://doi.org/10.1155/2022/4845726)]
- [*Digital Health*] **Research and application of tongue and face diagnosis based on deep learning** Historical anchor: Research and application of tongue and face diagnosis based on deep learning. [[DOI](https://doi.org/10.1177/20552076221124436)]
- [*Evid. Based Complement. Alternat. Med.*] **Deep Learning Multi-label Tongue Image Analysis and Its Application in a Population Underg** Historical anchor: Deep Learning Multi-label Tongue Image Analysis and Its Application in a Population Underg. [[DOI](https://doi.org/10.1155/2022/3384209)]
- [*Digital Chinese Medicine*] **Data-driven based four examinations in TCM: a survey** Historical anchor: Data-driven based four examinations in TCM: a survey. [[DOI](https://doi.org/10.1016/j.dcmed.2022.12.004)]
- [*JMIR Medical Informatics*] **Ensemble Learning-Based Pulse Signal Recognition: Classification Model Development Study** Historical anchor: Ensemble Learning-Based Pulse Signal Recognition: Classification Model Development Study. [[DOI](https://doi.org/10.2196/28039)]
- [*IEEE Trans. Cybernetics*] **Automatic Construction of Chinese Herbal Prescriptions From Tongue Images Using CNNs and A** Historical anchor: Automatic Construction of Chinese Herbal Prescriptions From Tongue Images Using CNNs and A. [[DOI](https://doi.org/10.1109/tcyb.2019.2909925)]
- [*BMC Medical Informatics and Decision Making*] **中医临床细粒度 NER 语料** Fine-grained entity-recognition corpus built from TCM clinical records. [[DOI](https://doi.org/10.1186/s12911-020-1079-2)]
- [*IEEE ICKG*] **TCMKG** Deep-learning-based TCM knowledge graph platform. [[DOI](https://doi.org/10.1109/ICBK50248.2020.00084)]
- [*Comput. Struct. Biotechnol. J.*] **Artificial intelligence in tongue diagnosis: Using deep convolutional neural network for r** Historical anchor: Artificial intelligence in tongue diagnosis: Using deep convolutional neural network for r. [Being University of Chinese Medicine, Beijing 100029, China, Beijing University of Posts and Telecommunications, Beijing 100876, China, Beijing Normal University, Beijing 100875, China] [[DOI](https://doi.org/10.1016/j.csbj.2020.04.002)]

</details>

<details>
<summary>2010s · 19</summary>

- [*IEEE Trans. Cybernetics*] **Tooth-Marked Tongue Recognition Using Multiple Instance Learning and CNN Features** Historical anchor: Tooth-Marked Tongue Recognition Using Multiple Instance Learning and CNN Features. [[DOI](https://doi.org/10.1109/tcyb.2017.2772289)]
- [*JAMIA*] **TCM-BERT** BERT further pretrained on TCM clinical text for five-way disease classification (JAMIA 2019). CKCEST holds copyright; the full 46,205 records are not released, only splits plus drive-hosted fine-tuned weights. [[DOI](https://doi.org/10.1093/jamia/ocz164)] [[Code](https://github.com/yao8839836/tcm_bert)]
- [*Xu HY et al., *Nucleic Acids Res* 47(D1):D976-D982*] **ETCM** Historical anchor: ETCM. [[DOI](https://doi.org/10.1093/nar/gky987)]
- [*BMC Medical Informatics and Decision Making*] **An ontological framework for the formalization, organization and usage of TCM-Knowledge** Historical anchor: An ontological framework for the formalization, organization and usage of TCM-Knowledge. [[DOI](https://doi.org/10.1186/s12911-019-0760-9)]
- [*IEEE IAEAC*] **语义中医方剂知识图谱 (Miao et al. 2018)** Semantic TCM prescription knowledge graph built top-down from formula texts. [[DOI](https://doi.org/10.1109/IAEAC.2018.8577236)]
- [*CISP-BMEI*] **Constitution Identification of Tongue Image Based on CNN** Historical anchor: Constitution Identification of Tongue Image Based on CNN. [[DOI](https://doi.org/10.1109/cisp-bmei.2018.8633075)]
- [*Artificial Intelligence in Medicine*] **中医养生知识图谱 (Yu et al. 2017)** Large TCM health-preservation knowledge graph integrating terms, literature, and databases, with retrieval, visualization, and recommendation. [[DOI](https://doi.org/10.1016/j.artmed.2017.04.001)]
- [*BioMed Research International*] **Diagnostic Method of Diabetes Based on Support Vector Machine and Tongue Images** Historical anchor: Diagnostic Method of Diabetes Based on Support Vector Machine and Tongue Images. [[DOI](https://doi.org/10.1155/2017/7961494)]
- [*IEEE BIBM*] **中医期刊关系抽取 (Wang & Poon 2016)** Relation extraction from TCM journal full text to support later knowledge-graph construction. [[DOI](https://doi.org/10.1109/BIBM.2016.7822725)]
- [*Ru J et al., *J Cheminform* 6(1):13*] **TCMSP** Historical anchor: TCMSP. [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- [*Comput. Math. Methods Med.*] **Pulse Waveform Classification Using Support Vector Machine with Gaussian Time Warp Edit Di** Historical anchor: Pulse Waveform Classification Using Support Vector Machine with Gaussian Time Warp Edit Di. [Harbin Ice Flower Hospital, Harbin 150086, China] [[DOI](https://doi.org/10.1155/2014/947254)]
- [*Evid. Based Complement. Alternat. Med.*] **A disturbance rejection framework for the study of traditional Chinese medicine** Historical anchor: A disturbance rejection framework for the study of traditional Chinese medicine. [[DOI](https://doi.org/10.1155/2014/787529)]
- [*Journal of Biomedical Informatics*] **中医症状名识别** Supervised methods for symptom name recognition in free-text TCM clinical records. [[DOI](https://doi.org/10.1016/j.jbi.2013.09.008)]
- [*Xue R et al., *Nucleic Acids Res* 41(D1):D1089-D1095*] **TCMID** Historical anchor: TCMID. [[DOI](https://doi.org/10.1093/nar/gks1100)]
- [*Evid. Based Complement. Alternat. Med.*] **Automated Tongue Feature Extraction for ZHENG Classification in Traditional Chinese Medici** Historical anchor: Automated Tongue Feature Extraction for ZHENG Classification in Traditional Chinese Medici. [[DOI](https://doi.org/10.1155/2012/912852)]
- [*Journal of Biomedical Informatics*] **Text mining for traditional Chinese medical knowledge discovery: a survey** Historical anchor: Text mining for traditional Chinese medical knowledge discovery: a survey. [[DOI](https://doi.org/10.1016/j.jbi.2010.01.002)]
- [*Journal of Chinese Integrative Medicine*] **Feature extraction and recognition of traditional Chinese medicine pulse based on hemodyna** Historical anchor: Feature extraction and recognition of traditional Chinese medicine pulse based on hemodyna. [[Link](http://www.jcimjournal.com/EN/10.3736/jcim20100802)]
- [*Artificial Intelligence in Medicine*] **Development of traditional Chinese medicine clinical data warehouse for medical knowledge ** Historical anchor: Development of traditional Chinese medicine clinical data warehouse for medical knowledge . [[DOI](https://doi.org/10.1016/j.artmed.2009.07.012)]
- [*EURASIP J. Adv. Signal Process.*] **Classification of Pulse Waveforms Using Edit Distance with Real Penalty** Historical anchor: Classification of Pulse Waveforms Using Edit Distance with Real Penalty. [[DOI](https://doi.org/10.1155/2010/303140)]

</details>

<details>
<summary>2000s · 10</summary>

- [*IEEE CSIE*] **Syndrome Differentiation in Intelligent TCM Diagnosis System** Historical anchor: Syndrome Differentiation in Intelligent TCM Diagnosis System. [[DOI](https://doi.org/10.1109/csie.2009.782)]
- [*Int. J. Information Technology & Decision Making*] **Equilibrium and nonequilibrium modeling of YinYang WuXing for diagnostic decision support ** Historical anchor: Equilibrium and nonequilibrium modeling of YinYang WuXing for diagnostic decision support . [[DOI](https://doi.org/10.1142/s0219622009003521)]
- [*IEEE ITME*] **Traditional Chinese medical diagnosis based on fuzzy and certainty reasoning** Historical anchor: Traditional Chinese medical diagnosis based on fuzzy and certainty reasoning. [[DOI](https://doi.org/10.1109/itme.2008.4743874)]
- [*WWW* (demo/industrial)*] **Information retrieval and knowledge discovery on the semantic web of traditional Chinese m** Historical anchor: Information retrieval and knowledge discovery on the semantic web of traditional Chinese m. [[DOI](https://doi.org/10.1145/1367497.1367668)]
- [*Journal of Chinese Integrative Medicine*] **Establishment of a fuzzy mathematical model for syndrome differentiation of gastric cancer** Historical anchor: Establishment of a fuzzy mathematical model for syndrome differentiation of gastric cancer. [[Link](http://www.jcimjournal.com/EN/10.3736/jcim20081104)]
- [*IEEE BMEI*] **Building Clinical Data Warehouse for Traditional Chinese Medicine Knowledge Discovery** Historical anchor: Building Clinical Data Warehouse for Traditional Chinese Medicine Knowledge Discovery. [[DOI](https://doi.org/10.1109/bmei.2008.83)]
- [*IEEE SITIS*] **A Novel Computerized Method Based on Support Vector Machine for Tongue Diagnosis** Historical anchor: A Novel Computerized Method Based on Support Vector Machine for Tongue Diagnosis. [[DOI](https://doi.org/10.1109/sitis.2007.115)]
- [*Artificial Intelligence in Medicine*] **Knowledge discovery in traditional Chinese medicine: State of the art and perspectives** Historical anchor: Knowledge discovery in traditional Chinese medicine: State of the art and perspectives. [[DOI](https://doi.org/10.1016/j.artmed.2006.07.005)]
- [*Information Sciences*] **YinYang bipolar logic and bipolar fuzzy logic** Historical anchor: YinYang bipolar logic and bipolar fuzzy logic. [[DOI](https://doi.org/10.1016/j.ins.2003.05.010)]
- [*Artificial Intelligence in Medicine*] **Ontology development for unified traditional Chinese medical language system** Historical anchor: Ontology development for unified traditional Chinese medical language system. [[DOI](https://doi.org/10.1016/j.artmed.2004.01.014)]

</details>

<details>
<summary>1970s–1990s · 5</summary>

- [*Complementary Therapies in Medicine*] **A computer model of the “five elements” theory of traditional Chinese medicine** Historical anchor: A computer model of the “five elements” theory of traditional Chinese medicine. [[DOI](https://doi.org/10.1016/S0965-2299(98)80005-8)]
- [*Physica Scripta*] **Functional structure model of human body and Yinyang-Wuxing equations** Historical anchor: Functional structure model of human body and Yinyang-Wuxing equations. [[DOI](https://doi.org/10.1088/0031-8949/36/6/015)]
- [*Fuzzy Sets and Systems*] **Fuzzy match and floating threshold strategy for expert system in traditional Chinese medicine** Historical anchor: Fuzzy match and floating threshold strategy for expert systems in traditional Chinese medicine. [[DOI](https://doi.org/10.1016/0165-0114(85)90052-1)]
- [*Hospital historical archive*] **Guan Youbo liver-disease diagnosis and treatment program** Historical anchor: an early computer-based expert system encoding renowned TCM physician Guan Youbo's approach to liver disease. [[Link](https://www.bjzhongyi.com/gzb_mygs_detail/4656.html)]
- [*Computers and Biomedical Research*] **An artificial intelligence program to advise physicians regarding antimicrobial therapy** Historical anchor: An artificial intelligence program to advise physicians regarding antimicrobial therapy. [[DOI](https://doi.org/10.1016/0010-4809(73)90029-3)]

</details>


</details>

## Datasets

Grouped by use. Official sites that are down are marked “site down”; portals that are up but broken are marked “site issue”. Both stay listed with the paper or a mirror. For a longer note on benches, see [Datasets](wiki/Datasets.md) and [Benchmarks](wiki/Benchmarks.md).

<details>
<summary>Curated lists (2)</summary>

- **awesome_Chinese_medical_NLP** — Curated list of Chinese medical NLP resources: terminologies, corpora, word vectors, pretrained models, KGs, NER and QA (incl. CBLUE). [[Resources](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)]
- **CPM Chinese patent medicine dataset** — Living large-scale public Chinese patent medicine data accompanying RAG-CPMF. [[Data](https://gitee.com/tcmdoc/cpm)] [[Paper](https://doi.org/10.1016/j.phrs.2025.107883)]

</details>

<details>
<summary>Formula / extract databases (23)</summary>

- **HERB 2.0** — Evidence-centered TCM resource integrating clinical trials, meta-analyses, high-throughput experiments, literature, and a knowledge graph. [[Website](http://herb.ac.cn/v2)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11701625/)] [[DOI](https://doi.org/10.1093/nar/gkae1037)]
- **CMAUP** — BIDD landscape of multi-target activities, pathways, and diseases for useful plants including TCM herbs; 2024 update, downloadable from the official site. [[Website](https://www.bidd.group/CMAUP/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767869/)] [[DOI](https://doi.org/10.1093/nar/gkad921)]
- **BATMAN-TCM 2.0** — Known and predicted TCM ingredient–target protein interactions, with greatly expanded TTI coverage and target-to-ingredient search. [[Website](http://bionet.ncpsb.org.cn/batman-tcm/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767940/)] [[DOI](https://doi.org/10.1093/nar/gkad926)]
- **TCMBank** — Large downloadable herb–ingredient–target–disease resource with literature-mining updates after manual checks. [[Website](http://tcmbank.cn/)] [[DOI](https://doi.org/10.1038/s41392-023-01339-1)]
- **ITCM** — Integrated formula/herb/ingredient/target platform plus 1,488 pharmacotranscriptomic profiles for 496 TCM ingredients (expression data also on Synapse). [[Website](http://itcm.biotcm.net/)] [[DOI](https://doi.org/10.1093/bib/bbad027)]
- **ETCM 2.0** — Encyclopedia of TCM formulas, patent drugs, materia medica, and ingredients with target prediction and multi-scale networks; v1 site remains online. [[Website](http://www.tcmip.cn/ETCM2/front/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10326295/)] [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)]
- **DCABM-TCM** — Literature-mined blood constituents and metabolites of TCM prescriptions and herbs, with experimental detection conditions (~1,816 structured absorbed constituents). [[Website](http://bionet.ncpsb.org.cn/dcabm-tcm/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10428213/)]
- **LTM-TCM** (site down) — Symptom–prescription–plant–ingredient–target platform linking 14 source databases plus clinical and classical records (~48k formulas). Official Tasly cloud no longer resolves; verify via the paper DOI. [[Original site](http://cloud.tasly.com/#/tcm/home)] [[DOI](https://doi.org/10.1016/j.phrs.2022.106185)]
- **HIT 2.0** (site issue) — Manually curated herbal-ingredient–target activity pairs (~1,237 ingredients / 2,208 targets, 2000–2020 literature). Portal opens; the analysis backend port is currently down (marked site issue). [[Website](http://hit2.badd-cao.net/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728248/)] [[DOI](https://doi.org/10.1093/nar/gkab1011)]
- **SuperTCM** (site down) — Charité biocultural TCM resource linking drugs, botanical species, ingredients, targets, KEGG pathways, and diseases (~6,516 drugs). Official tcm.charite.de no longer resolves. [[Original site](http://tcm.charite.de/supertcm)] [[Paper](https://europepmc.org/article/MED/34656056)] [[DOI](https://doi.org/10.1016/j.biopha.2021.112315)]
- **TCMIO** — Immuno-oncology TCM database of prescriptions, herbs, ingredients, targets, and pathways, with downloads and a REST API. [[Website](http://tcmio.xielab.net/)] [[Data](http://tcmio.xielab.net/download)] [[DOI](https://doi.org/10.3389/fphar.2020.00439)]
- **SymMap 2.0** — Herb–TCM symptom–modern symptom–ingredient–target–disease maps, expanded with newer pharmacopoeia records and downloadable relationship tables. [[Website](http://www.symmap.org/)] [[Data](http://www.symmap.org/download/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323958/)]
- **YaTCM** (site down) — About 1,813 prescriptions, 6,220 herbs, and 47k natural products with target/pathway tools. Nankai site currently returns 403; verify via the open-access paper. [[Original site](http://cadd.pharmacy.nankai.edu.cn/yatcm/home)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6280608/)] [[DOI](https://doi.org/10.1016/j.csbj.2018.11.002)]
- **TCMID 2.0** (site down) — Integrative formula–herb–ingredient–target database (distinct from NUS TCM-ID). Original megabionet site is down; verify via Zenodo extract and the NAR paper. [[Original site](http://www.megabionet.org/tcmid/)] [[Data](https://zenodo.org/records/8066910)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5753259/)] [[DOI](https://doi.org/10.1093/nar/gkx1028)]
- **TCMAnalyzer** (site down) — RCDD chemo-/bioinformatics service for formula/herb/ingredient networks and scaffold search (~1,493 formulas, 618 herbs). Official rcdd.org.cn currently times out. [[Original site](http://www.rcdd.org.cn/tcmanalyzer)] [[Paper](https://pubmed.ncbi.nlm.nih.gov/29425456/)] [[DOI](https://doi.org/10.1021/acs.jcim.7b00549)]
- **TCM-Mesh** (site down) — Herb–compound–gene–disease network with toxicity/side-effect records (~6,235 herbs). Official portal currently returns 403; verify via the open paper. [[Original site](http://mesh.tcm.microbioinformatics.org/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5460194/)] [[DOI](https://doi.org/10.1038/s41598-017-03039-7)]
- **TM-MC** (site down) — KIOM literature-derived Northeast Asian medicinal-material–compound database; the 2015 release covers ~536 materials, and the 2024 2.0 paper expands to ~34k compounds. Official site currently times out. [[Original site](http://informatics.kiom.re.kr/compound/)] [[DOI](https://doi.org/10.1186/s12906-015-0758-5)] [[2.0 paper](https://doi.org/10.1186/s12906-023-04331-y)]
- **CEMTDD** (site down) — Ethnic-minority herbal–compound–target–disease resource (~621 herbs, mainly Uygur/Kazakh). Original cemtdd.com now hosts something else; verify via the PMC paper. [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627337/)] [[DOI](https://doi.org/10.18632/oncotarget.3789)]
- **TCMSP** — Herb–ingredient–target–disease networks with ADME parameters; public site is TCMSP 2.3 with downloadable relationship tables. [[Website](https://www.tcmsp-e.com/tcmsp.php)] [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- **CVDHD** (site down) — Cardiovascular herbal database of 3D compound structures, targets, and pathways for virtual screening and network pharmacology. Original Peking University site currently times out. [[Original site](http://pkuxxj.pku.edu.cn/CVDHD)] [[DOI](https://doi.org/10.1186/1758-2946-5-51)]
- **TCM Database@Taiwan** (site down) — About 20k isolated-compound 2D/3D structures from 453 TCM materials for virtual screening. Original tcm.cmu.edu.tw is unreachable; verify via the PLOS paper. [[Original site](http://tcm.cmu.edu.tw/)] [[Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0015939)] [[DOI](https://doi.org/10.1371/journal.pone.0015939)]
- **TCMGeneDIT** (site down) — Text-mined associations among TCM, genes, diseases, effects, and ingredients, with pathway and PPI links. Official NTU site no longer resolves. [[Original site](http://tcm.lifescience.ntu.edu.tw/)] [[Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2582235/)] [[DOI](https://doi.org/10.1186/1472-6882-8-58)]
- **TCM-ID** — NUS BIDD formula–herb–ingredient–target resource covering pharmacopoeia, classical, and CFDA-approved prescriptions; not the same database as TCMID 2.0. [[Website](https://www.bidd.group/TCMID/)]

</details>

<details>
<summary>Clinical structured / prescription sets (2)</summary>

- **TCM-Lung** — Pulmonary-disease cases from FAH-HUCM (14,948 processed; 4,484 encoded public rows of symptom/syndrome/method/prescription IDs). Full names on request. Not the same resource as TCMNSCLC. [[Code](https://github.com/2020MEAI/PresRecST)] [[Paper](https://doi.org/10.1093/jamia/ocae066)]
- **TCM-PD** — Yao et al. TKDE 2018 prescription topic-model set (98,334 raw / 33,765 processed symptom–herb ID pairs). CKCEST copyright, research use only. PresRecST's prescript_1195.csv is a reproduction table. [[Code](https://github.com/yao8839836/PTM)] [[DOI](https://doi.org/10.1109/TKDE.2017.2787158)]

</details>

<details>
<summary>General Chinese medical data (13)</summary>

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
<summary>East Asian traditional medicine (3)</summary>

- **Korean Medicine Embedding Dataset** — Query–positive–negatives (~113k pairs) built from Korean-medicine terms and an ontology, for embedding fine-tunes such as BGE-M3. [[Dataset](https://huggingface.co/datasets/cnupo23/korean-medicine-embedding-dataset)]
- **KNApSAcK KAMPO** — NAIST Kampo public database (~1,581 formulas, 278 crude drugs), downloadable from the NBDC life-science archive. [[Dataset](https://dbarchive.biosciencedbc.jp/data/knapsack-kampo/)] [[DOI](https://doi.org/10.1093/pcp/pcr165)]
- **OASIS (KIOM)** — KIOM traditional-medicine literature portal for Korean-medicine papers and herbal resources. [[Website](https://oasis.kiom.re.kr/)]

</details>

<details>
<summary>Books / pretraining corpora (5)</summary>

- **classical-tcm-canon** — Full-text digitizations of the TCM canon: Neijing, Nanjing, Shanghan Lun, Jingui Yaolue and warm-disease classics. [[Dataset](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)]
- **Traditional-Chinese-Medicine-Dataset-Pretrain** — High-quality TCM pretraining dataset from non-Internet sources (~1GB; clinical cases, classics, encyclopedia), 99% simplified Chinese. [[Dataset](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)]
- **TCM-Pretrain-Data-ShizhenGPT** — ShizhenGPT pretraining corpus (15B+ tokens reported in the paper — Stage-1 text 11.92B incl. 6.3B TCM, plus Stage-2 multimodal ~3.6B). [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- **TCM-Ancient-Books** — A corpus of nearly 700 TCM ancient-book texts. [[Dataset](https://github.com/xiaopangxia/TCM-Ancient-Books)]
- **ChiMed 2.0** — Upgraded Chinese medical pretraining dataset covering TCM corpora for LLM pretraining. [[Paper](https://arxiv.org/abs/2507.15275)]

</details>

<details>
<summary>Benchmarks (17)</summary>

- **TCM-RobustSDT** — TCM-RobustSDT: a robustness benchmark dataset for LLM clinical reasoning in TCM (Figshare). [[Dataset](https://doi.org/10.6084/m9.figshare.33054974)]
- **TCMEval-PA** — 328 multiple-choice items on prescription normative quality and safety auditing. [[Paper](https://doi.org/10.1038/s41597-025-06387-6)] [[Data](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[Code](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)]
- **TCM-AQA61 / CME-AQA** — Dual-view acupuncture and Tuina action-quality videos from 61 subjects each (first- and third-person), with expert categorical and continuous ratings; paired with the CME-AQA cross-view multimodal assessment framework. [[Paper](https://arxiv.org/abs/2606.28104)] [[DOI](https://doi.org/10.1109/TNSRE.2026.3705649)] [[Code](https://github.com/FrancisXZhang/cme-aqa)] [[Data](https://researchdata.durham.ac.uk/collections/r1jm214p229)]
- **LingLan** — LingLan large multi-task TCM evaluation benchmark (2026). [[Dataset](https://github.com/TCMAI-BJTU/LingLan)] [[Paper](https://arxiv.org/abs/2602.01779)]
- **ZhongJing-OMNI** — ZhongJing-OMNI multimodal TCM eval (including tongue). [[Dataset](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]
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
- **TCM-SD** — First large public TCM syndrome-differentiation text benchmark (54,152 real records, 148 syndromes, CC BY-NC-SA 4.0). Full set is in the repo folder TCM_SD_with_knowledge; Tianchi id 139034. [[Paper](https://arxiv.org/abs/2203.10839)] [[Published](https://aclanthology.org/2022.ccl-1.80/)] [[Code](https://github.com/Borororo/ZY-BERT)] [[Data](https://tianchi.aliyun.com/dataset/dataDetail?dataId=139034)]

</details>

<details>
<summary>Exam datasets (2)</summary>

- **TCM-Text-Exams** — Recent TCM licensure / graduate-exam text benchmark. [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams)]
- **Medical-LLMs-Chinese-Exam** — Chinese medical exam evaluation for medical LLMs. [[Dataset](https://github.com/jingnant/Medical-LLMs-Chinese-Exam)]

</details>

<details>
<summary>Instruction / dialogue datasets (12)</summary>

- **HSQ-TD（健身气功指令微调数据集）** — HSQ-TD: the first instruction-tuning dataset for health Qigong/wellness, with 57,843 instructions distilled from official textbooks and professional literature (ScienceDB). [[Dataset](https://doi.org/10.57760/sciencedb.35843)]
- **neijing-sft-v1.2** — ~2,009 Neijing-related instruction samples for Xinghe, with thinking/output fields. [[Dataset](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2)]
- **TCMNSCLC** — Real-world NSCLC TCM reasoning dataset with fully annotated cases (pattern differentiation / treatment method / decoction / patent medicine). [[Dataset](https://huggingface.co/datasets/zhangxinxin0428/TCMNSCLC)] [[DOI](https://doi.org/10.5281/zenodo.21027568)]
- **Traditional-Chinese-Medicine-Dataset-SFT** — High-quality TCM supervised fine-tuning dataset. [[Dataset](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]
- **TCMChat-dataset-600k** — TCMChat herbal QA and recommendation instruction data (~600k). [[Dataset](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- **TCM-Instruction-Tuning-ShizhenGPT** — ShizhenGPT multimodal SFT data (text/vision/speech/ECG etc.; ~311k items total per paper Table 3). [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- **ShenNong_TCM_Dataset** — ShenNong TCM instruction dataset. [[Dataset](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)]
- **MedChatZH** — MedChatZH TCM consultation dataset. [[Code](https://github.com/tyang816/MedChatZH)] [[Dataset](https://huggingface.co/datasets/tyang816/MedChatZH)]
- **ChatMed_Consult_Dataset** — Chinese online medical consult dataset (500k+ consults with ChatGPT replies). [[Dataset](https://huggingface.co/datasets/michaelwzhu/ChatMed_Consult_Dataset)]
- **CMtMedQA** — ZhongJing real multi-turn doctor–patient dialogues (~70k). [[Dataset](https://huggingface.co/datasets/Suprit/CMtMedQA)]
- **Baize-TCM-Corpus-V3** — ~157k TCM QA items covering theory, herbs, formulas, diagnosis, acupuncture, and clinic. [[Dataset](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3)]
- **ChP-TCM** — KnowledgeQA and PrescriptionWriting instructions built from Chinese Pharmacopoeia Vol. I. [[Data](https://github.com/QLU-NLP/BianCang/tree/main/ChP-TCM)] [[Paper](https://arxiv.org/abs/2411.11027)]

</details>

<details>
<summary>Knowledge graphs (6)</summary>

- **LingShu** — Symptom-centric contextual KG bridging TCM and biomedicine (~17.33M entities, ~39.47M relations including triples and contextual quadruples), with a portal for visualization, reasoning, and evidence-grounded QA. [[Paper](https://arxiv.org/abs/2608.20402)] [[Website](http://www.tcmkg.com/)]
- **TCM_KG** — ChatMed knowledge graph. [[Dataset](https://github.com/ywjawmw/TCM_KG)]
- **TCM-MKG** — TCM multi-dimensional knowledge graph. [[Data](https://zenodo.org/records/15395588)]
- **OpenTCM-KG** — OpenTCM gynecology classics KG (~48k entities / ~152k relations). [[Code](https://github.com/OpenTCM01/OpenTCM)] [[Paper](https://arxiv.org/abs/2504.20118)]
- **TCM-QG** — About 5,000 TCM documents and 13,000 question-answer pairs from CHIP2020, for knowledge-base expansion and question generation (CC BY-SA 4.0). [[Data](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86895)] [[Resources](http://openkg.cn/dataset/tcm-qg)]
- **TCM-NER** — 1,997 Chinese-medicine package inserts with 59,803 entities in 13 types for building a medication knowledge graph (OpenKG / CHIP, CC BY-SA 4.0). [[Data](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86819)] [[Resources](http://openkg.cn/dataset/tcm-ner)]

</details>

---

Search and filter by tag on the [project page](https://tyang816.github.io/projects/tcm/). Longer notes live in the [wiki](wiki/Home.md).
Add entries in `data/catalog.yml` and run `python3 scripts/build_readme.py`. Do not edit this README by hand.
