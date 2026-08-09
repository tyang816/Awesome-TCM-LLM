# 🔥 Awesome TCM / Chinese Medical LLMs

**Language / 语言:** [English](README_EN.md) | [中文](README.md)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  ![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork)

Curated open resources for Traditional Chinese Medicine (and related Chinese medical) LLMs — news, papers, models, benchmarks, and datasets. Contributions welcome.

**Links:** [Project page (EN)](https://tyang816.github.io/projects/tcm/) · [Project page (ZH)](https://tyang816.github.io/zh/projects/tcm/) · [Author site (EN)](https://tyang816.github.io/) · [Author site (ZH)](https://tyang816.github.io/zh/)

> The project page supports search and tag filters. Data is sourced from the same `data/catalog.yml` as this README. English blurbs live in `data/i18n_en.yml`.

## 📰 News
- [2026.07] Shanghai Seventh People's Hospital (SHUTCM) releases the **Qiyuan** TCM LLM with pretraining, domain fine-tuning, and expert RL; supports generative medical records and master-physician Agent digital twins; showcased at WAIC. [[Link](https://dwgk.shutcm.edu.cn/2026/0725/c1890a175544/page.htm)]
- [2026.07] Guizhou Medical University and partners launch **HuaZu BenCao**, a national ethnic-medicine AI platform built on ShuZhi QiHuang + Qwen integrating multi-ethnic materia medica classics. [[Link](https://www.gmc.edu.cn/info/1058/30267.htm)]
- [2026.07] Andun Health debuts a **seven-diagnosis** TCM robot at WAIC 2026, integrating face/IR face/tongue/ear/auscultation/inquiry/pulse sensing with TianHui pulse algorithms and a TCM clinical LLM. [[Link](https://www.news.cn/finance/20260720/f6a8625c1be4412d9c311a232c7a35fa/c.html)]
- [2026.07] Insightful Eye presents **Bianshi Cloud TCM** at WAIC 2026, built on a registered Bianshi multimodal model with four-diagnosis devices and assisted-care systems. [[Link](http://www.eeo.com.cn/2026/0720/965556.shtml)]
- [2026.06] Zhongke Wenge passes HKEX listing hearing; reports note the **DaYi JinKui** TCM LLM (with CACMS) has obtained top-tier CAICT Trusted AI certification. [[Link](https://www.ncsti.gov.cn/kjdt/xwjj/202606/t20260610_249369.html)]
- [2026.04] Beijing University of Chinese Medicine's **XinHuo ZhongGuoYao** TCM education LLM completes national generative-AI service filing—the first publicly approved TCM-domain model of its kind. [[Link](https://regional.chinadaily.com.cn/education/cn/2026-04/22/c_1177692.htm)]
- [2026.04] Affiliated Hospital of Shandong University of TCM launches the provincial AI+ TCM scenario project **ZhiHui QiHuang**. [[Link](http://ccpd.china.com.cn/2026-04/17/content_43401621.html)]
- [2026.02] Eight ministries issue the TCM Industry High-Quality Development Plan (2026–2030), calling for AI and knowledge graphs to empower classical formulas and master physicians' prescriptions. [[Link](https://www.gov.cn/zhengce/zhengceku/202602/content_7057174.htm)]
- [2025.12] Jilin releases **ZhongXing·Changbai Qihuang 1.0**, an AI-native multimodal TCM LLM. [[Link](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- [2025.12] Gushengtang launches a “TCM Brain” product and AI digital twin of National TCM Master Shi Qi; 14 expert twins cover eight core specialties. [[Link](https://www.jjckb.cn/20251231/693ca93b14ff4f57adc359959dc0320d/c.html)]
- [2025.12] **ZMT-M1** scores 96.26 on a simulated national TCM practitioner exam and is piloted in 100+ clinics. [[Link](https://m.tech.china.com/redian/2025/1229/122025_1789291.html)]
- [2025.11] Five national health ministries issue AI+ healthcare guidelines that explicitly support building TCM diagnostic LLMs. [[Link](https://www.gov.cn/zhengce/zhengceku/202511/content_7047018.htm)]
- [2025.09] Transn's **RenDu·SuWen** passes CAICT Trusted AI TCM LLM Level 4+ evaluation. [[Link](https://zhongyi.gmw.cn/2025-09/10/content_38277329.htm)]
- [2025.09] **ZhiFu Qihuang Tiangong** TCM AI model completes national deep-synthesis algorithm filing for four-diagnosis devices and constitution assessment. [[Link](http://zs.scbzol.com/zs/2025/0919/328624.html)]
- [2025.09] **YiYin** classical TCM LLM goes live in Song County, Henan, combining TCM education with AI-assisted care for county clinics. [[Link](http://www.ha.xinhuanet.com/20250918/a3da94037689422dbcd1fe57fa62ef94/c.html)]
- [2025.08] **Gushengtang** releases ten “National Master AI twins” trained on master clinicians' experience, reporting >86% pattern-differentiation accuracy. [[Link](http://sz.people.com.cn/n2/2025/0801/c202846-41310443.html)]
- [2025.08] NSCC-TJ and Tianjin University of TCM release **TianHe·LingShu** 2.0 (expanded beyond acupuncture to 20+ specialties) and launch a TCM intelligent-model evaluation system. [[Link](http://tj.people.com.cn/n2/2025/0809/c375366-41317410.html)]
- [2025.07] Guang'anmen Hospital forms the **GuangYi·QiZhi** LLM agent alliance with medical consortium partners for cross-institution intelligent care. [[Link](https://www.gamyy.cn/gzb/news/big/112751.html)]
- [2025.06] **TCM Hengqin** vertical LLM is officially released. [[Link](https://www.stdaily.com/web/gdxw/2025-06/20/content_357526.html)]
- [2025.05] China Academy of Chinese Medical Sciences releases evaluation standards for TCM large models. [[Link](https://www.news.cn/politics/20250510/5e6a0b4978b44b69b67dbfb7282fd220/c.html)]
- [2025.04] Transn releases **RenDu·SuWen** TCM LLM (mixture-of-entropy architecture) for inquiry, pattern differentiation, and formula recommendation. [[Link](https://www.transn.com/about_us/consult/article/1924766101036437505)]
- [2025.03] Guang'anmen Hospital releases **GuangYi·QiZhi**, described as the first TCM hospital with integrated local compute + model + application deployment. [[Link](https://www.xinhuanet.com/tech/20250328/8b1685ad8c6f48c9bdc2add1658edac3/c.html)]
- [2024.12] China UnionPay Consumer Finance with Sun Yat-sen University and GZUCMS Shenzhen Hospital release vertical TCM LLM **ZhongSi** for community clinic inquiry. [[Link](https://finance.sina.com.cn/jjxw/2024-12-16/doc-inczrzsp5791684.shtml)]
- [2024.09] Zhongke Wenge releases **DaYi JinKui** TCM LLM and health platform trained on 1,500+ TCM classics. [[Link](https://36kr.com/newsflashes/2946967562099592)]
- [2024.05] Tasly and Huawei Cloud release **ShuZhi BenCao** (Pangu language + molecular models) covering TCM R&D; later earns CAICT TCM LLM Level 4+. [[Link](https://news.pharmnet.com.cn/news/2024/05/10/591622.html)]
- [2024.03] ECNU, SHUTCM, ECUST, NMMU, Lingang Lab, and CR Jiangzhong jointly develop the **ShuZhi QiHuang** TCM LLM.
- [2023.07] Nanjing Dajing TCM releases **QiHuang Wendao** LLM with large knowledge graphs and clinical data for institutional beta use. [[Link](http://js.news.cn/20230729/fa034db71a00487b819a4ad95b44673e/c.html)]

## 📚 Resources

### 2026
- **CORE-Acu** Acupuncture clinical decision support with structured reasoning traces and a knowledge-graph safety veto loop. [[Paper](https://arxiv.org/abs/2603.08321)]
- **DERM-3R** Resource-constrained multimodal multi-agent framework for TCM dermatology (recognition / representation / SDT agents). [[Paper](https://arxiv.org/abs/2604.09596)]
- [*Chinese Medicine*] **GastroTCM** TCM gastroenterology LLM fine-tuned from Llama3-8B with RAG and agent scaffolding. [[Paper](https://link.springer.com/article/10.1186/s13020-025-01295-8)]
- **MMIR-TCM** Memory-augmented multimodal tongue diagnosis and clinical decision framework; proposes MedTCM dataset and TDEU metric. [[Paper](https://arxiv.org/abs/2607.01814)]
- [*Digital Chinese Medicine*] **Qwen-TCM-Dia** Specialty fine-tuned model for TCM diarrhea care (CPT + CoT SFT) covering symptom→pathomechanism→method→formula chains. [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.003)]
- **TCM-Agent** LLM multi-agent system for network pharmacology and herbal discovery. [[Paper](https://doi.org/10.1016/j.jpha.2026.101581)] [[Code](https://github.com/AITCM/TCM-Agent)]
- [*Frontiers in Medicine*] **TCM-DiffRAG** Syndrome-differentiation RAG with a general KG, a personalized KG, and chain-of-thought. [[Published](https://doi.org/10.3389/fmed.2026.1804478)] [[Paper](https://arxiv.org/abs/2602.22828)] [[Code](https://github.com/LiJianmin6706/Tcm_Diff_RAG)]
- [*JMIR Medical Informatics*] **TongueVLM** Multimodal VLM for TCM tongue diagnosis, description generation, and constitution reasoning. [[Paper](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- **Xinghe** Qwen3.5-9B reasoning TCM model grounded in the *Neijing*, with explicit CoT pattern differentiation and safety boundaries. [[Model](https://huggingface.co/zsyjsld/Xinghe1.2-9B)] [[GGUF](https://huggingface.co/zsyjsld/Xinghe1.2-9B-GGUF)] [[Dataset](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2)]
- **LingLan** Large multi-task TCM benchmark: 5 domains, 13 subtasks, 25,624 instances. [Beijing Jiaotong University et al.] [[Paper](https://arxiv.org/abs/2602.01779)] [[Code](https://github.com/TCMAI-BJTU/LingLan)] [[Website](http://tcmnlp.com)]
- [*Pattern Recognition*] **ATCMD-Bench** First agentic TCM diagnosis benchmark, evaluating LLMs through multi-agent simulated consultations. [South China University of Technology] [[DOI](https://doi.org/10.1016/j.patcog.2026.113679)]
- [*Expert Systems with Applications*] **End-to-end TCM clinical support benchmark** Benchmark for end-to-end TCM clinical support across the full LLM care pipeline. [East China Normal University] [[DOI](https://doi.org/10.1016/j.eswa.2026.132267)]
- [*Digital Chinese Medicine*] **QingNangTCM** Parameter-efficient fine-tuned TCM QA and clinical reasoning model; builds the 100k-item **QnTCM_Dataset**. [Hebei North University] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.002)]
- [*Chinese Herbal Medicines*] **HerbWise** Domain LLM for traditional herbal medicine (THM), serving herbal modernization and standardization. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.chmed.2026.02.010)]
- **Med-Shicheng** Lightweight master-physician experience-inheritance framework built on Tianyi; a single model internalizes 5 national masters' knowledge systems across 7 task types. [Nanjing University of Chinese Medicine et al.] [[Paper](https://arxiv.org/abs/2603.23520)] [[Code](https://github.com/NJUCM-BJUCM-TCM-AI/Med-Shicheng)]
- **DongYuan** Integrative spleen–stomach disease diagnosis LLM framework combining TCM pattern differentiation with Western diagnostic reasoning. [[Paper](https://arxiv.org/abs/2603.28191)]
- **MACAT** Multi-agent culture-aware translation framework, evaluated on culture-loaded terms from TCM classics and the Analects. [[Paper](https://arxiv.org/abs/2606.01276)]
- **TongueDx2** Systematic ablation of the tongue-diagnosis DL design space (20+ model variants); TongueDx2 includes 5,109 images / 976 expert annotations. [[Paper](https://arxiv.org/abs/2607.28148)]
- **Med-Bench-Arena** Open evaluation platform for medical and TCM LLMs/Agents (HF/vLLM/LiteLLM, multimodal, TCM-specific metrics), from the ZhongJing team. [[Code](https://github.com/pariskang/Med-Bench-Arena)]
- [*ICIC 2026*] **TCMBenchEval** Benchmark evaluating LLMs on real clinical TCM case records (ICIC 2026). [Shantou University] [[DOI](https://doi.org/10.1007/978-981-92-3498-1_1)]
- [*ISCTIS 2026*] **Tongue–face multimodal fusion diagnosis** Tongue–face multimodal feature fusion with LLM-driven intelligent TCM diagnosis. [Xiamen University of Technology] [[DOI](https://doi.org/10.1109/ISCTIS70043.2026.11572361)]
- [*Frontiers in Artificial Intelligence*] **TCMI-F-6D** Six-dimensional benchmark of interdisciplinary foundational competence in TCM informatics. [Anhui University of Chinese Medicine] [[DOI](https://doi.org/10.3389/frai.2026.1780967)] [[Code](https://github.com/123adf-dev/TCMI-F-6D-Benchmark)]
- [*Frontiers in Medicine*] **Jin San Zhen KG-QA** Knowledge graph + LLM QA tool for the Jin San Zhen acupuncture school. [Guangzhou University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1755583)]
- [*Applied Intelligence*] **KDC-NER** Knowledge-guided data augmentation + LLM fine-tuning framework for nested NER in TCM. [Jiangxi University of Chinese Medicine] [[DOI](https://doi.org/10.1007/s10489-026-07095-3)]
- [*Digital Chinese Medicine*] **CMM-EmbedCluster** LLM + medicinal-property-theory clustering framework for Chinese materia medica, with a 567-herb property knowledge base. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2026.05.010)]
- [*Chinese Medicine*] **TCMNet** LLM-assisted disease knowledge mining with PPI networks and binding prediction for formula optimization. [Zhejiang Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1186/s13020-026-01360-w)]
- [*Science of Traditional Chinese Medicine*] **TCM Data Hub (YiYuan)** YiYuan LLM-driven TCM data platform. [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.1097/st9.0000000000000118)]
- [*Journal of Traditional Chinese Medical Sciences*] **TCM intelligent pre-consultation clinical evaluation** Tertiary-hospital clinical evaluation of an LLM intelligent pre-consultation system using a physician–AI–patient triad model. [Beijing Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.jtcms.2026.06.002)]
- [*Scientific Reports*] **Three-LLM TCM licensing exam evaluation** Systematic evaluation of 3 LLMs (incl. Gemini) on the national TCM medical licensing examination. [Shanghai Jiao Tong University] [[DOI](https://doi.org/10.1038/s41598-026-49200-z)]
- [*Frontiers in Medicine*] **TCM AI-tutor evaluation** Multimodal LLM evaluation for TCM education across cognitive levels. [Beijing University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1893231)]
- [*Journal of Evidence-Based Medicine*] **Large vs lightweight LLMs on TCM exams** Systematic comparison of large-scale vs lightweight LLMs on TCM exam questions. [First Affiliated Hospital of Henan University] [[DOI](https://doi.org/10.1111/jebm.70118)]
- [*Frontiers in Plant Science*] **Medicinal-plant MLLM benchmark** Benchmarking multimodal LLMs for medicinal plant identification. [Shaoxing University] [[DOI](https://doi.org/10.3389/fpls.2026.1765281)]
- **Patient-Conditioned Dual Hypergraph Reasoning** Patient-conditioned dual-hypergraph reasoning for auditable TCM prescription support, organizing symptom/tongue/pulse evidence around patterns and treatment principles (Tianjin University). [[Paper](https://arxiv.org/abs/2607.04025)]
- **Evidence-Based TCM Visualization Diagnosis System** Evidence-based TCM visualization diagnosis system: Neo4j knowledge graph (241 patterns, 1,263 symptoms) with four-stage symptom matching (LLM-verified) and information-gain-driven active inquiry. [[Paper](https://arxiv.org/abs/2606.06869)]
- **TCMIIES** TCMIIES: a browser-based, zero-installation LLM system for structured information extraction from academic literature, aimed at TCM and other specialty researchers. [[Paper](https://arxiv.org/abs/2605.07507)]
- [*Communications in Computer and Information Science (Springer)*] **Hybrid Retrieval + Re-ranking TCM Prescription Generation** Hybrid retrieval with re-ranking to enhance LLM-based TCM prescription generation (Springer CCIS conference paper). [[Paper](https://doi.org/10.1007/978-981-92-3563-6_21)]
- **DeepTCM1.0** DeepTCM1.0: a multi-expert AI agent built on general LLMs for interpreting the mechanisms of TCM compound formulas (Research Square preprint). [[Link](https://doi.org/10.21203/rs.3.rs-9844166/v1)]
- [*KSII Transactions on Internet and Information Systems*] **GAT+LLM TCM Prescription Generation** Intelligent TCM prescription generation combining graph attention networks with LLMs (formally published in KSII TIIS). [[DOI](https://doi.org/10.3837/tiis.2026.05.006)]
- [*生物化学与生物物理进展*] **病机推理CoT监督（脾胃病）** Pathogenesis-reasoning chain-of-thought supervision replacing fixed-label classification for spleen-stomach disease syndrome recognition and multi-dimensional evaluation (Prog. Biochem. Biophys.). [[DOI](https://doi.org/10.3724/j.pibb.2026.0141)]
- **儿童流感中成药推荐系统（KG+LLM）** Knowledge graph of Chinese patent medicines for pediatric influenza built from authoritative guidelines and integrated with an LLM (JMIR Preprints). [[Link](https://doi.org/10.2196/preprints.101648)]
- [*Translation Review*] **Beyond the Poetic Bard（中医AI翻译评论）** Beyond the Poetic Bard: a perspective on accuracy, epistemology, and medical-context limits of generative-AI translation of TCM texts (Translation Review). [[DOI](https://doi.org/10.1080/07374836.2026.2679929)]
- [*Future Internet (MDPI)*] **RAG+LoRA 中医执照考试推理架构** RAG+LoRA generative architecture with an 11,476-item Taiwan TCM licensing-exam dataset (2005-2025), raising accuracy from 61.0% to 89.0%+ (Future Internet, MDPI). [[DOI](https://doi.org/10.3390/fi18060280)]
- [*Frontiers in Medicine*] **树状自反思检索中医问答** Tree-organized self-reflective retrieval for TCM question answering (Frontiers in Medicine 2026). [[DOI](https://doi.org/10.3389/fmed.2026.1752778)]

### 2025
- **BenCao** Instruction-aligned multimodal TCM assistant (ChatGPT/GPTs Store) with tongue APIs and knowledge bases (distinct from HuaTuo/BenCao). [[Paper](https://arxiv.org/abs/2510.17415)]
- **ChatTCM** Fully open TCM LLM from pretraining data through released weights. [[Model](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)] [[Pretrain data](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)] [[SFT data](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]
- [*Journal of King Saud University Computer and Information Sciences*] **DiagX-DT** Exclusionary syndrome-differentiation reasoning with CoT and an external TCM knowledge base. [[DOI](https://doi.org/10.1007/s44443-025-00123-1)]
- **DoPI** Doctor-like proactive inquiry TCM LLM (guide + expert models); reported inquiry accuracy 84.68%. [[Paper](https://arxiv.org/abs/2507.04877)]
- [*IEEE ICIP 2025*] **MCM** Multi-agent collaborative multimodal TCM diagnosis framework (IEEE ICIP 2025). [Shanghai Computer Software Technology Development Center] [[Code](https://github.com/JerryMazeyu/MCM)] [[Published](https://doi.org/10.1109/icip55913.2025.11084334)]
- [*Scientific Data*] **MTCMB** Multi-task TCM benchmark (~12 subsets, ~7.1k samples) covering knowledge, reasoning, formulas, and safety. [[Paper](https://arxiv.org/abs/2506.01252)] [[Code](https://github.com/Wayyuanyuan/MTCMB)] [[Published](https://doi.org/10.1038/s41597-026-07967-w)]
- **OpenTCM** GraphRAG TCM retrieval and diagnosis system with a gynecology classics knowledge graph. [[Paper](https://arxiv.org/abs/2504.20118)] [[Code](https://github.com/OpenTCM01/OpenTCM)]
- [*Pharmacological Research*] **RAG-CPMF** Multi-LLM verification + RAG for Chinese patent medicine recommendation, with a living public CPM dataset. [[DOI](https://doi.org/10.1016/j.phrs.2025.107883)] [[Data](https://gitee.com/tcmdoc/cpm)]
- **ShizhenGPT** Multimodal TCM LLM supporting the four diagnoses (inspection, auscultation-olfaction, inquiry, palpation). [The Chinese University of Hong Kong, Shenzhen et al.] [[Paper](https://arxiv.org/abs/2508.14706)] [[Code](https://github.com/FreedomIntelligence/ShizhenGPT)] [[Model](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[Pretrain data](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)] [[Instruction data](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- [*npj Digital Medicine*] **TCM LLM acupuncture clinical evaluation** Real-case evaluation of 7 general LLMs vs licensed acupuncturists on SDT, point selection, needling, and herbs (*npj Digital Medicine*). [[DOI](https://doi.org/10.1038/s41746-025-01845-2)]
- [*Communications Medicine*] **TCM-3CEval** Three-axis TCM LLM evaluation: core knowledge, classics comprehension, and clinical decision-making. [[Paper](https://arxiv.org/abs/2503.07041)] [[Published](https://doi.org/10.1038/s43856-026-01631-5)]
- **TCM-5CEval** Five-dimension deep evaluation extending TCM-3CEval with materia medica and non-drug therapies. [[Paper](https://arxiv.org/abs/2511.13169)]
- **TCM-BEST4SDT** Case benchmark for syndrome differentiation and treatment (knowledge / ethics / safety / SDT). [[DOI](https://doi.org/10.6084/m9.figshare.30615956)] [[Paper](https://arxiv.org/abs/2512.02816)] [[Code](https://github.com/DYJG-research/TCM-BEST4SDT)]
- [*Computers in Biology and Medicine*] **TCM-KLLaMA** KG-fused LLM for intelligent TCM formula generation. [[DOI](https://doi.org/10.1016/j.compbiomed.2025.109887)]
- [*NeurIPS 2025*] **TCM-Ladder** First large multimodal TCM QA benchmark with 52,000+ items (NeurIPS 2025). [[Paper](https://arxiv.org/abs/2505.24063)] [[Code](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[Leaderboard](https://tcmladder.com)]
- [*APWeb-WAIM 2025*] **TCM-R1** TCM LLM with GRPO-enhanced reasoning. [Southwest University] [[Paper](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*Pharmacological Research*] **TCMChat** Generative TCM LLM built via pre-training and supervised fine-tuning, released with the 600k-sample TCMChat-600k dialogue dataset (Pharmacol. Res. 2024). [[Paper](https://doi.org/10.1016/j.phrs.2024.107530)] [[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1043661824004754)] [[Code](https://github.com/ZJUFanLab/TCMChat)] [[Model](https://huggingface.co/ZJUFanLab/TCMChat-600k)] [[Dataset](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- [*IEEE BIBM 2025*] **ViTCM-LLM** Qwen2.5-VL + RAG tongue multimodal clinical framework; MedTCM dataset and TDEU metric (precursor to MMIR-TCM). [[DOI](https://doi.org/10.1109/bibm66473.2025.11357113)] [[Code](https://github.com/jw-chae/ViTCM_LLM)] [[Model](https://huggingface.co/Mark-CHAE/ViTCM-LLM)]
- [*JMIR Medical Informatics*] **Yaoshi-RAG** Uncertain-KG RAG for medicine–food homology dietary recommendation with personalization and explainability. [[DOI](https://doi.org/10.2196/75279)]
- **RenShu-AI** FastAPI + LangGraph multi-agent TCM consultation system combining GraphRAG and DeepSeek-TCM. [[Code](https://github.com/yanlinPeng-code/RenShu-AI)]
- [*Tsinghua Science and Technology*] **仲景 (ZhongJing)** ZhongJingGPT, an expert-knowledge-guided TCM LLM combining vertical-domain fine-tuning with cognitive-psychology insights and multi-scenario TCM knowledge instructions (Tsinghua Sci. Technol. 2025). [[Paper](https://doi.org/10.26599/TST.2025.9010046)] [[Code](https://github.com/pariskang/CMLM-ZhongJing)] [[Model](https://huggingface.co/CMLM/ZhongjingGPT1_13B)]
- [*Information Fusion*] **Tianyi** ~7B TCM LLM from NJUCM et al. with reading–clinic–apprenticeship training stages, TCMEval, and real-world validation. [Nanjing University of Chinese Medicine] [[Published](https://doi.org/10.1016/j.inffus.2025.103663)] [[Paper](https://arxiv.org/abs/2505.13156)] [[News](https://blog.sciencenet.cn/blog-279293-1501581.html)]
- **TianHui** Domain LLM for 12 TCM scenarios (DeepSeek-R1-Distill-Qwen-14B + PT/SFT) with open code and eval scripts. [[Paper](https://arxiv.org/abs/2509.19834)] [[Code](https://github.com/JYfantast/TianHui)]
- [*Expert Systems with Applications*] **Qibo** TCM LLM and Qibo Benchmark from Tianjin University et al.; CPT + SFT for SDT and QA. [Tianjin University, Tianjin University of Traditional Chinese Medicine] [[Published](https://doi.org/10.1016/j.eswa.2025.127672)] [[Paper](https://arxiv.org/abs/2403.16056)] [[DOI](https://doi.org/10.1016/j.eswa.2025.127672)]
- [*IEEE Journal of Biomedical and Health Informatics*] **BianCang** BianCang TCM LLM series (IEEE JBHI); 14B open-weight release in Dec 2025. [Qilu University of Technology] [[Paper](https://arxiv.org/abs/2411.11027)] [[Code](https://github.com/QLU-NLP/BianCang)] [[Model](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)] [[DOI](https://doi.org/10.1109/jbhi.2025.3612415)]
- **ZMT-M1** ZMT-M1 TCM LLM and the dynamic, extensible TCM-Eval benchmark platform. [Beihang University] [[Paper](https://arxiv.org/abs/2511.07148)] [[Platform](https://tcmeval.bamaidical.com)]
- **Baize-TCM-LLM** ICMM Baize TCM QA models on Qwen3 (0.6B/8B) with ~157k LoRA-tuning examples. [Institute of Chinese Materia Medica, CACMS] [[Model](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model)] [[Dataset](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3)]
- [*IEEE Journal of Biomedical and Health Informatics*] **ZhiFangDanTai** GraphRAG + LLM fine-tuning for interpretable formula generation (sovereign–minister–assistant–courier, efficacy, contraindications) with open weights. [[Paper](https://arxiv.org/abs/2509.05867)] [[DOI](https://doi.org/10.1109/jbhi.2025.3607819)] [[Model](https://huggingface.co/tczzx6/ZhiFangDanTai1.0)]
- [*Cell Discovery*] **神农Alpha** ShennongAlpha (Westlake University): an AI-driven sharing and collaboration platform for intelligent curation, acquisition and translation of natural-medicinal-material knowledge (Cell Discov. 2025). [[DOI](https://doi.org/10.1038/s41421-025-00776-2)] [[Website](https://shennongalpha.westlake.edu.cn/)] [[Paper](https://www.nature.com/articles/s41421-025-00776-2)] [[Code](https://github.com/shennong-program/shennongname)]
- **Jingfang** LLM-based multi-agent TCM diagnosis/treatment system reporting large relative SDT gains under the authors' protocol. [[Paper](https://arxiv.org/abs/2502.04345)]
- [*Chinese Medicine*] **XuanHuGPT** TCM domain LLM built with parameter-efficient fine-tuning (PEFT). [Hebei North University] [[DOI](https://doi.org/10.1186/s13020-025-01200-3)]
- [*Chinese Medicine*] **TCM-DS** Domain LLM for medicine–food homology dietary-therapy recommendation. [Macau University of Science and Technology] [[DOI](https://doi.org/10.1186/s13020-025-01249-0)]
- [*IEEE BIBM 2025*] **TCM-VisResolve (TCM-VR)** Qwen2.5-VL-based TCM multimodal LLM — 163-class dried-herb recognition over 220k images plus clinical MCQs with 880k candidate answers. [Minzu University of China] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356679)]
- [*IEEE BIBM 2025*] **ChatGLM-FGIDs-TCM** Knowledge-fused ChatGLM clinical decision-support model for functional gastrointestinal disorders (FGIDs). [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356283)]
- [*UbiComp Companion 2025*] **TCM misinformation detection evaluation** Safety evaluation framework with 3,000+ TCM exam items × 4 paradigms, covering wrong-option, misleading, and fabrication detection. [Tsinghua University] [[DOI](https://doi.org/10.1145/3714394.3756275)]
- [*ICASSP 2025*] **Few-shot tongue-diagnosis in-context multitask learning** Few-shot in-context multitask fine-tuning of LLMs mapping tongue images directly to constitutions. [Northeastern University] [[DOI](https://doi.org/10.1109/ICASSP49660.2025.10887764)]
- [*WISE 2025*] **TCM-Eval (WISE 2025)** Multi-dimensional TCM evaluation framework (WISE 2025); a different work from the ZMT-M1 TCM-Eval (arXiv 2511.07148) despite the identical name. [Tianjin International Joint Academy of Biomedicine] [[DOI](https://doi.org/10.1007/978-981-95-7251-9_15)]
- [*Frontiers in Pharmacology*] **TCMRD-KG** Innovative design of a rheumatology TCM knowledge graph from ancient literature. [Beijing University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fphar.2025.1535596)]
- [*IEEE BIBM 2025*] **Chinese patent medicine knowledge system** Constructing a knowledge system for traditional Chinese patent medicine using LLMs and KGs. [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356149)]
- [*Digital Chinese Medicine*] **TCMLCM** KG2T-based intelligent QA model for TCM lung cancer. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2025.03.011)]
- [*IEEE Journal of Biomedical and Health Informatics*] **LLM herb–drug interaction prediction** LLM-enhanced herbal medicine–drug interaction prediction. [Shenzhen University] [[DOI](https://doi.org/10.1109/jbhi.2025.3558667)]
- [*JMIR Formative Research*] **TCM stroke LLM benchmark** Quantitative benchmark study of LLMs in the TCM stroke domain. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2196/81545)]
- [*JMIR Formative Research*] **5-LLM TCM clinical decision comparison** Comparative study of 5 LLMs for TCM clinical decision-making. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.2196/80167)]
- [*Frontiers in Pharmacology*] **TCM guideline adherence evaluation** Content-analysis evaluation of LLM adherence to clinical practice guidelines in Chinese medicine. [Lanzhou University] [[DOI](https://doi.org/10.3389/fphar.2025.1649041)]
- [*JMIR Medical Informatics*] **Weighted-voting TCM formula classification** Weighted-voting LLM approach for TCM formula classification. [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.2196/69286)]
- [*Journal of Medical and Biological Engineering*] **LLM + RAG TCM inference** Combining LLMs with RAG for TCM inference. [Taipei City Hospital] [[DOI](https://doi.org/10.1007/s40846-025-00988-7)]
- [*Frontiers in Medicine*] **中医医案问答系统** A TCM case-based QA system integrating LLMs and knowledge graphs for efficient case retrieval and analysis (Front. Med. 2025). [[DOI](https://doi.org/10.3389/fmed.2024.1512329)]
- [*Interdisciplinary Sciences*] **LLM-driven TCM KG construction** LLM-driven construction and application of a TCM knowledge graph. [Henan University of Technology] [[DOI](https://doi.org/10.1007/s12539-025-00735-1)]
- [*npj Digital Medicine*] **LM extraction for complementary medicine** Language models for data extraction and risk-of-bias assessment in complementary medicine literature. [Lanzhou University] [[DOI](https://doi.org/10.1038/s41746-025-01457-w)]
- [*Information*] **TCM compound retrieval agent** AI agent-based system for retrieving TCM compound information. [Zhengzhou University] [[DOI](https://doi.org/10.3390/info16070543)]
- [*IEEE BIBM*] **MRD-RAG** Multi-round diagnostic RAG simulating clinical reasoning; builds **DiagnosGraph** spanning TCM and Western medicine (876 diseases / 7,997 nodes / 37,201 triples). [[Published](https://doi.org/10.1109/bibm66473.2025.11357107)] [[Paper](https://arxiv.org/abs/2504.07724)]
- **Ladder-base (GRPO-TCM)** First GRPO reinforcement-learning-aligned TCM LLM, from the TCM-Ladder team. [[Paper](https://arxiv.org/abs/2510.17402)]
- **TCDiff** Triplet cascaded diffusion model generating high-fidelity multimodal TCM EHRs, with the **TCM-SZ1** benchmark dataset. [[Paper](https://arxiv.org/abs/2508.01615)]
- **New Snow Tablets** Reveals systematic flaws of general and TCM-specific LLMs that guess formula ingredients from drug names. [[Paper](https://arxiv.org/abs/2504.03786)]
- [*IJCNN 2025*] **From Metaphor to Mechanism** LLMs decode TCM metaphor / imagistic-thinking language and map it to modern medical concepts. [[Paper](https://arxiv.org/abs/2503.02760)] [[Published](https://doi.org/10.1109/ijcnn64981.2025.11228098)]
- **TCM-Sage** Evidence-synthesis RAG assistant for TCM practitioners (hybrid vector + knowledge graph). [[Code](https://github.com/AndyZHENG0715/TCM-Sage)]
- [*Expert Systems with Applications*] **针灸大模型驯化与生成评估 (Taming LLMs for Acupuncture)** Taming LLMs for acupuncture & moxibustion diagnosis, with generation quality evaluated at the semantic-similarity level. [[DOI](https://doi.org/10.1016/j.eswa.2024.125920)]
- [*JMIR Medical Informatics*] **辨证思维评测 (Syndrome Differentiation Thinking)** Method-development study evaluating and improving LLMs' TCM syndrome-differentiation thinking ability. [[DOI](https://doi.org/10.2196/75103)]
- [*Applied Sciences*] **Gen-SynDi** Knowledge-guided generative-AI framework for dual education of syndrome differentiation and disease diagnosis. [[DOI](https://doi.org/10.3390/app15094862)]
- **Hengqin-RA-v1** LLM and companion dataset for TCM diagnosis and treatment of rheumatoid arthritis. [[Paper](https://arxiv.org/abs/2501.02471)]
- [*数据分析与知识发现*] **中医药标准知识问答系统** Retrieval-augmented QA system for TCM standards knowledge, built and evaluated in practice. [China Academy of Chinese Medical Sciences et al.] [[DOI](https://doi.org/10.11925/infotech.2096-3467.2024.0747)]
- [*Scientific Reports*] **双通道知识注意力辨证模型** Dual-channel knowledge-attention NLP model for TCM syndrome differentiation, addressing rare characters and terminology extraction. [[DOI](https://doi.org/10.1038/s41598-025-96404-w)]
- [*Preprints.org（预印本）*] **GPT 台湾中医执业考试评估** GPT-3.5/GPT-4/GPT-4o performance on the Taiwan TCM licensing examination with reliability analysis (preprint). [[DOI](https://doi.org/10.20944/preprints202501.1787.v1)]
- [*arXiv*] **RACE-Align** RACE-Align: retrieval-augmented, CoT-style DPO alignment of a compact Qwen3-1.7B for TCM reasoning. [[arXiv](https://arxiv.org/abs/2506.02726)]
- [*Discover Applied Sciences*] **Mathematical modeling of Chinese medicine by complex-valued five-agent network** Historical anchor: Mathematical modeling of Chinese medicine by complex-valued five-agent network. [[DOI](https://doi.org/10.1007/s42452-025-06602-4)]

### 2024
- **Chinese-LLaVA-Med** Chinese medical multimodal LLM based on the LLaVA architecture, with the llava-med-zh-eval benchmark and open 7B weights. [[Code](https://github.com/BUAADreamer/Chinese-LLaVA-Med)]
- [*Computers in Biology and Medicine*] **MedChatZH** MedChatZH: a fine-tuned LLM for TCM consultation dialogues, released with open dataset and weights (Comput. Biol. Med. 2024). [[Paper](https://doi.org/10.1016/j.compbiomed.2024.108290)] [[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0010482524003743)] [[Dataset](https://huggingface.co/datasets/tyang816/MedChatZH)] [[Model](https://huggingface.co/tyang816/medchatzh)] [[Code](https://github.com/tyang816/MedChatZH)]
- [*Digital Chinese Medicine*] **TCMLLM / Lingdan** TCMLLM / Lingdan for TCM modeling and prescription recommendation. [Beijing Jiaotong University] [[Paper](https://doi.org/10.1016/j.dcmed.2025.01.007)] [[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2589377725000072)] [[Code](https://github.com/2020MEAI/TCMLLM)] [[Lingdan code](https://github.com/TCMAI-BJTU/LingdanLLM)] [[Model](https://huggingface.co/TCMLLM/Lingdan-13B-Base)]
- **大数中医 (BigDataTCM)** BigDataTCM (34B): a vertical TCM LLM co-developed by HAUT's Complexity Science institute and Apus, offering medical QA, diagnostic support and TCM knowledge services. [[Code](https://github.com/HAUT-CS/BigDataTCM)]
- **明医 (MING)** MING: a Chinese medical consultation LLM using a sparse mixture of low-rank adapter experts (MING-MoE) for medical multi-task learning (arXiv 2024). [[Paper](https://arxiv.org/abs/2404.09027)] [[Related MedCare](https://aclanthology.org/2024.findings-emnlp.619/)] [[Code](https://github.com/MediaBrain-SJTU/MING)]
- [*ACM Trans. Knowl. Discov. Data*] **BenCao (formerly HuaTuo)** Instruction-tuned Chinese medical LLM (BenCao / formerly HuaTuo). [Harbin Institute of Technology] [[Paper](https://arxiv.org/pdf/2309.04175.pdf)] [[Code](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)]
- [*Computer Methods and Programs in Biomedicine Update*] **TCM-GPT** Efficient pre-training of LLMs for domain adaptation in Traditional Chinese Medicine. [[DOI](https://doi.org/10.1016/j.cmpbup.2024.100158)] [[Paper](https://arxiv.org/abs/2311.01786)]
- [*Scientific Reports*] **CPMI-ChatGLM** Parameter-efficient fine-tuning of ChatGLM with Chinese patent medicine instructions. [[DOI](https://doi.org/10.1038/s41598-024-56874-w)]
- [*IEEE BIBM*] **TCM-FTP** Fine-tuning LLMs for herbal prescription prediction. [[DOI](https://doi.org/10.1109/BIBM62325.2024.10822451)]
- [*Journal of the American Medical Informatics Association*] **LLM 腧穴定位关系抽取** Relation extraction with LLMs — a case study on acupuncture point locations. [[DOI](https://doi.org/10.1093/jamia/ocae233)]
- [*Journal of Translational Medicine*] **LLM 中医语言文化偏差研究** Comparing LLMs developed in different countries on TCM; highlights language/cultural bias and the need for localized models. [[DOI](https://doi.org/10.1186/s12967-024-05128-4)]
- [*Electronics*] **LLM 构建中医知识图谱** Constructing Traditional Chinese Medicine knowledge graphs based on large language models. [[DOI](https://doi.org/10.3390/electronics13071395)]
- [*JMIR Medical Informatics*] **中医领域知识图谱补全** Domain knowledge graph completion and quality evaluation for Traditional Chinese Medicine. [[DOI](https://doi.org/10.2196/55090)]
- [*Chinese Medicine and Culture*] **ChatGPT 中医交互可行性研究** Feasibility and challenges of interactive AI for TCM, using ChatGPT as an example. [[DOI](https://doi.org/10.1097/MC9.0000000000000103)]
- [*Frontiers in Artificial Intelligence*] **Evi-BERT** Automated information-extraction model (Evi-BERT) enhancing RCT evidence extraction for TCM. [[DOI](https://doi.org/10.3389/frai.2024.1454945)]
- [*EIECC*] **TCM MLKG-RAG** TCM intelligent diagnosis based on multi-layer knowledge graph retrieval-augmented generation. [[DOI](https://doi.org/10.1109/EIECC64539.2024.10929529)]
- [*Methods of Information in Medicine*] **TCMSF** TCMSF: a construction framework for a TCM syndrome ancient-book knowledge graph that organizes syndrome knowledge from classical texts in a structured, semantically oriented way (Methods Inf. Med. 2024). [[DOI](https://doi.org/10.1055/a-2590-6348)]
- **ChatGPT 中医知识理解探究** Evaluating ChatGPT's comprehension of Traditional Chinese Medicine knowledge. [[Paper](https://arxiv.org/abs/2403.09164)]
- **中医提示工程框架** Prompt-engineering framework for LLM intelligent understanding in TCM. [[Paper](https://arxiv.org/abs/2410.19451)]
- **RLAIF 中医对齐** Enhancing LLMs' TCM capabilities through reinforcement learning from AI feedback. [[Paper](https://arxiv.org/abs/2411.00897)]
- **TCMD** TCMD, a TCM QA dataset for evaluating large language models. [[Paper](https://arxiv.org/abs/2406.04941)]
- [*Digital Chinese Medicine*] **BSG 中医智能问答** Intelligent QA system for TCM based on a BSG deep-learning model (prescription and materia medica cases). [[DOI](https://doi.org/10.1016/j.dcmed.2024.04.006)]
- [*Database (Oxford)*] **ACUBERT** ACUBERT for meridian entity recognition and classification in acupuncture indication knowledge bases. [[DOI](https://doi.org/10.1093/database/baae083)]
- [*计算机科学与探索*] **中医药大模型知识增强方法** Knowledge augmentation for TCM LLMs — a graph built from ~100k classical formulas preserving prescription structure. [Tianjin University] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2407082)]
- [*南京中医药大学学报*] **中医标准化评估基准** Standardized TCM evaluation benchmark of 29,506 questions across 13 subjects; tests 3 general and 5 Chinese medical LLMs. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1383)]
- [*南京中医药大学学报*] **中医药问答大语言模型** TCM QA LLM combining RAG with P-Tuning v2 fine-tuning on ChatGLM2-6B. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1375)]
- [*Research Square（预印本）*] **GPT-4 中医研究生考试评估** GPT-4 vs mainstream Chinese LLMs on a TCM postgraduate examination dataset (preprint). [[DOI](https://doi.org/10.21203/rs.3.rs-4392855/v1)]
- [*OSF Preprints（预印本）*] **RAG 增强中医问答置信度** Implementing retrieval-augmented generation to build LLM confidence in TCM (preprint). [[DOI](https://doi.org/10.31219/osf.io/ns2v3)]
- [*AAAI*] **仲景（CMtMedQA 线，Yang et al.）** ZhongJing (CMtMedQA line, Yang et al.): a TCM LLM distinct from the Kang-line ZhongJingGPT—full CPT+SFT+RLHF pipeline on Ziya-LLaMA-13B over ~70K real multi-turn doctor-patient dialogues (AAAI 2024). [[Paper](https://doi.org/10.1609/aaai.v38i17.29907)] [[arXiv](https://arxiv.org/abs/2308.03549)]
- [*J Integr Complement Med*] **GPT vs ERNIE 中医文化背景对比研究** A culture-framed comparison of GPT versus ERNIE on TCM tasks (J. Integr. Complement. Med. 2024). [[DOI](https://doi.org/10.1089/jicm.2024.0902)]

### 2023
- **ChatMed** ChatMed series of Chinese medical LLMs, including ChatMed-Consult trained on 500k+ online consultation dialogues. [[Code](https://github.com/michael-wzhu/ChatMed)]
- **XrayGLM** Chinese multimodal medical LLM for chest X-ray interpretation. [[Code](https://github.com/WangRongsheng/XrayGLM)]
- [*EMNLP findings*] **HuaTuoGPT** Large language model trained on Chinese medical corpora (HuaTuoGPT). [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[DOI](https://doi.org/10.18653/v1/2023.findings-emnlp.725)] [[Paper](https://aclanthology.org/2023.findings-emnlp.725/)] [[Code](https://github.com/FreedomIntelligence/HuatuoGPT)]
- **QiZhenGPT** Chinese clinical QA model for drugs, diseases, procedures, and labs (QiZhenGPT). [Zhejiang University] [[Code](https://github.com/CMKRG/QiZhenGPT)]
- **孙思邈 (Sunsimiao)** Sunsimiao Chinese medical LLM; Sunsimiao-7B fine-tuned from Qwen2-7B on curated medical data, reaching 30B-level SOTA on CMB-Exam. [[Code](https://github.com/X-D-Lab/Sunsimiao)]
- [*arXiv*] **BianQue** Chinese proactive health LLM for everyday living spaces (BianQue). [South China University of Technology, Guangdong Key Laboratory of Digital Twin Humans] [[Code](https://github.com/scutcyr/BianQue)] [[Paper](https://arxiv.org/abs/2310.15896)]
- **神农大模型 (ShenNong-TCM-LLM)** ShenNong-TCM-LLM, the first TCM large language model, released with the ShenNong_TCM_Dataset and open weights. [[Code](https://github.com/michael-wzhu/ShenNong-TCM-LLM)] [[Dataset](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)] [[Model](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]
- **黄帝 (HuangDi)** HuangDi: a TCM classics QA LLM built on Ziya-LLaMA-13B, pretrained on 22 TCM textbooks plus TCM web corpora and SFT-tuned with ancient-book instruction data (Library Tribune 2024). [[Code](https://github.com/Zlasejd/HuangDI)]
- [*计算机科学与探索*] **大模型融合知识图谱问答系统** Vertical-domain QA system deeply integrating LLMs with knowledge graphs for TCM formulas. [Tianjin University] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2308070)]
- [*JMIR Medical Education*] **ChatGPT 针灸教育研究** Comparative study of ChatGPT as a learning tool in acupuncture education. [[DOI](https://doi.org/10.2196/47427)]
- [*IEEE BIBM*] **中医疫病防治问答模型** LLM-based QA model for TCM epidemic prevention and treatment. [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385748)]
- [*IEEE BIBM*] **中医方剂 LLM 分类** Fine-tuned LLMs with refined prompt templates for TCM formula classification, using data sources such as the national medical-insurance catalog of proprietary Chinese medicines (IEEE BIBM 2023). [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385776)]
- [*IEEE BIBM*] **LLM+GNN 中医处方推荐** TCM prescription recommendation combining large language models with graph neural networks. [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385489)]
- [*IJACSA*] **草药智能配送聊天机器人** Smarter herbal medication delivery system employing an AI-powered chatbot. [[DOI](https://doi.org/10.14569/ijacsa.2023.0140358)]
- [*IEEE Access*] **PreGenerator** TCM prescription recommendation model combining retrieval and generation. [[DOI](https://doi.org/10.1109/ACCESS.2023.3316219)]
- **中医新冠文献 LLM 命名实体识别** Comparative study of LLMs for named entity recognition in TCM COVID-19 literature (preprint). [[DOI](https://doi.org/10.2196/preprints.54346)]
- [*Scientific Reports*] **Discovering golden ratio in the world’s first five-agent network in ancient China** Historical anchor: Discovering golden ratio in the world’s first five-agent network in ancient China. [[DOI](https://doi.org/10.1038/s41598-023-46071-6)]
- [*Interdisciplinary*] **Historical Analysis of Medical Artificial Intelligence Development in China: Research Cent** Historical anchor: Historical Analysis of Medical Artificial Intelligence Development in China: Research Cent. [[DOI](https://doi.org/10.18926/interdisciplinary/65464)]
- [*Zhang Y et al., *Acta Pharm Sin B* 13(6):2559-2571*] **ETCM v2.0** Historical anchor: ETCM v2.0. [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)]
- [*Lv Q et al., *Signal Transduct Target Ther* 8(1):127*] **TCMBank** Historical anchor: TCMBank. [[DOI](https://doi.org/10.1038/s41392-023-01339-1)]

### 2022
- [*BioMed Research International*] **乙肝中医 KG 问答系统** Knowledge-graph-based QA system for TCM diagnosis and treatment of viral hepatitis B. [[DOI](https://doi.org/10.1155/2022/7139904)]
- [*Evid. Based Complement. Alternat. Med.*] **Deep Learning Multi-label Tongue Image Analysis and Its Application in a Population Underg** Historical anchor: Deep Learning Multi-label Tongue Image Analysis and Its Application in a Population Underg. [[DOI](https://doi.org/10.1155/2022/3384209)]
- [*Digital Health*] **Research and application of tongue and face diagnosis based on deep learning** Historical anchor: Research and application of tongue and face diagnosis based on deep learning. [[DOI](https://doi.org/10.1177/20552076221124436)]
- [*Digital Chinese Medicine*] **Data-driven based four examinations in TCM: a survey** Historical anchor: Data-driven based four examinations in TCM: a survey. [[DOI](https://doi.org/10.1016/j.dcmed.2022.12.004)]

### 2021
- [*JMIR Medical Informatics*] **Ensemble Learning-Based Pulse Signal Recognition: Classification Model Development Study** Historical anchor: Ensemble Learning-Based Pulse Signal Recognition: Classification Model Development Study. [[DOI](https://doi.org/10.2196/28039)]
- [*IEEE Trans. Cybernetics*] **Automatic Construction of Chinese Herbal Prescriptions From Tongue Images Using CNNs and A** Historical anchor: Automatic Construction of Chinese Herbal Prescriptions From Tongue Images Using CNNs and A. [[DOI](https://doi.org/10.1109/tcyb.2019.2909925)]

### 2020
- [*IEEE ICKG*] **TCMKG** Deep-learning-based TCM knowledge graph platform. [[DOI](https://doi.org/10.1109/ICBK50248.2020.00084)]
- [*BMC Medical Informatics and Decision Making*] **中医临床细粒度 NER 语料** Fine-grained entity-recognition corpus built from TCM clinical records. [[DOI](https://doi.org/10.1186/s12911-020-1079-2)]
- [*Comput. Struct. Biotechnol. J.*] **Artificial intelligence in tongue diagnosis: Using deep convolutional neural network for r** Historical anchor: Artificial intelligence in tongue diagnosis: Using deep convolutional neural network for r. [[DOI](https://doi.org/10.1016/j.csbj.2020.04.002)]

### 2019
- [*BMC Medical Informatics and Decision Making*] **An ontological framework for the formalization, organization and usage of TCM-Knowledge** Historical anchor: An ontological framework for the formalization, organization and usage of TCM-Knowledge. [[DOI](https://doi.org/10.1186/s12911-019-0760-9)]
- [*IEEE Trans. Cybernetics*] **Tooth-Marked Tongue Recognition Using Multiple Instance Learning and CNN Features** Historical anchor: Tooth-Marked Tongue Recognition Using Multiple Instance Learning and CNN Features. [[DOI](https://doi.org/10.1109/tcyb.2017.2772289)]
- [*Xu HY et al., *Nucleic Acids Res* 47(D1):D976-D982*] **ETCM** Historical anchor: ETCM. [[DOI](https://doi.org/10.1093/nar/gky987)]

### 2018
- [*CISP-BMEI*] **Constitution Identification of Tongue Image Based on CNN** Historical anchor: Constitution Identification of Tongue Image Based on CNN. [[DOI](https://doi.org/10.1109/cisp-bmei.2018.8633075)]

### 2017
- [*BioMed Research International*] **Diagnostic Method of Diabetes Based on Support Vector Machine and Tongue Images** Historical anchor: Diagnostic Method of Diabetes Based on Support Vector Machine and Tongue Images. [[DOI](https://doi.org/10.1155/2017/7961494)]

### 2014
- [*Evid. Based Complement. Alternat. Med.*] **A disturbance rejection framework for the study of traditional Chinese medicine** Historical anchor: A disturbance rejection framework for the study of traditional Chinese medicine. [[DOI](https://doi.org/10.1155/2014/787529)]
- [*Comput. Math. Methods Med.*] **Pulse Waveform Classification Using Support Vector Machine with Gaussian Time Warp Edit Di** Historical anchor: Pulse Waveform Classification Using Support Vector Machine with Gaussian Time Warp Edit Di. [[DOI](https://doi.org/10.1155/2014/947254)]
- [*Ru J et al., *J Cheminform* 6(1):13*] **TCMSP** Historical anchor: TCMSP. [[DOI](https://doi.org/10.1186/1758-2946-6-13)]

### 2013
- [*Journal of Biomedical Informatics*] **中医症状名识别** Supervised methods for symptom name recognition in free-text TCM clinical records. [[DOI](https://doi.org/10.1016/j.jbi.2013.09.008)]
- [*Xue R et al., *Nucleic Acids Res* 41(D1):D1089-D1095*] **TCMID** Historical anchor: TCMID. [[DOI](https://doi.org/10.1093/nar/gks1100)]

### 2012
- [*Evid. Based Complement. Alternat. Med.*] **Automated Tongue Feature Extraction for ZHENG Classification in Traditional Chinese Medici** Historical anchor: Automated Tongue Feature Extraction for ZHENG Classification in Traditional Chinese Medici. [[DOI](https://doi.org/10.1155/2012/912852)]

### 2010
- [*Artificial Intelligence in Medicine*] **Development of traditional Chinese medicine clinical data warehouse for medical knowledge ** Historical anchor: Development of traditional Chinese medicine clinical data warehouse for medical knowledge . [[DOI](https://doi.org/10.1016/j.artmed.2009.07.012)]
- [*Journal of Biomedical Informatics*] **Text mining for traditional Chinese medical knowledge discovery: a survey** Historical anchor: Text mining for traditional Chinese medical knowledge discovery: a survey. [[DOI](https://doi.org/10.1016/j.jbi.2010.01.002)]
- [*Journal of Chinese Integrative Medicine*] **Feature extraction and recognition of traditional Chinese medicine pulse based on hemodyna** Historical anchor: Feature extraction and recognition of traditional Chinese medicine pulse based on hemodyna. [[Link](http://www.jcimjournal.com/EN/10.3736/jcim20100802)]
- [*EURASIP J. Adv. Signal Process.*] **Classification of Pulse Waveforms Using Edit Distance with Real Penalty** Historical anchor: Classification of Pulse Waveforms Using Edit Distance with Real Penalty. [[DOI](https://doi.org/10.1155/2010/303140)]

### 2009
- [*Int. J. Information Technology & Decision Making*] **Equilibrium and nonequilibrium modeling of YinYang WuXing for diagnostic decision support ** Historical anchor: Equilibrium and nonequilibrium modeling of YinYang WuXing for diagnostic decision support . [[DOI](https://doi.org/10.1142/s0219622009003521)]
- [*IEEE CSIE*] **Syndrome Differentiation in Intelligent TCM Diagnosis System** Historical anchor: Syndrome Differentiation in Intelligent TCM Diagnosis System. [[DOI](https://doi.org/10.1109/csie.2009.782)]

### 2008
- [*Journal of Chinese Integrative Medicine*] **Establishment of a fuzzy mathematical model for syndrome differentiation of gastric cancer** Historical anchor: Establishment of a fuzzy mathematical model for syndrome differentiation of gastric cancer. [[Link](http://www.jcimjournal.com/EN/10.3736/jcim20081104)]
- [*IEEE ITME*] **Traditional Chinese medical diagnosis based on fuzzy and certainty reasoning** Historical anchor: Traditional Chinese medical diagnosis based on fuzzy and certainty reasoning. [[DOI](https://doi.org/10.1109/itme.2008.4743874)]
- [*WWW* (demo/industrial)*] **Information retrieval and knowledge discovery on the semantic web of traditional Chinese m** Historical anchor: Information retrieval and knowledge discovery on the semantic web of traditional Chinese m. [[DOI](https://doi.org/10.1145/1367497.1367668)]
- [*IEEE BMEI*] **Building Clinical Data Warehouse for Traditional Chinese Medicine Knowledge Discovery** Historical anchor: Building Clinical Data Warehouse for Traditional Chinese Medicine Knowledge Discovery. [[DOI](https://doi.org/10.1109/bmei.2008.83)]

### 2007
- [*IEEE SITIS*] **A Novel Computerized Method Based on Support Vector Machine for Tongue Diagnosis** Historical anchor: A Novel Computerized Method Based on Support Vector Machine for Tongue Diagnosis. [[DOI](https://doi.org/10.1109/sitis.2007.115)]

### 2006
- [*Artificial Intelligence in Medicine*] **Knowledge discovery in traditional Chinese medicine: State of the art and perspectives** Historical anchor: Knowledge discovery in traditional Chinese medicine: State of the art and perspectives. [[DOI](https://doi.org/10.1016/j.artmed.2006.07.005)]

### 2004
- [*Information Sciences*] **YinYang bipolar logic and bipolar fuzzy logic** Historical anchor: YinYang bipolar logic and bipolar fuzzy logic. [[DOI](https://doi.org/10.1016/j.ins.2003.05.010)]
- [*Artificial Intelligence in Medicine*] **Ontology development for unified traditional Chinese medical language system** Historical anchor: Ontology development for unified traditional Chinese medical language system. [[DOI](https://doi.org/10.1016/j.artmed.2004.01.014)]

### 1998
- [*Complementary Therapies in Medicine*; 80005-8)*] **A computer model of the “five elements” theory of traditional Chinese medicine** Historical anchor: A computer model of the “five elements” theory of traditional Chinese medicine. [[DOI](https://doi.org/10.1016/S0965-2299(98)]

### 1987
- [*Physica Scripta*] **Functional structure model of human body and Yinyang-Wuxing equations** Historical anchor: Functional structure model of human body and Yinyang-Wuxing equations. [[DOI](https://doi.org/10.1088/0031-8949/36/6/015)]

### 1985
- [*Fuzzy Sets and Systems*; 90052-1)*] **Fuzzy match and floating threshold strategy for expert system in traditional Chinese medic** Historical anchor: Fuzzy match and floating threshold strategy for expert system in traditional Chinese medic. [[DOI](https://doi.org/10.1016/0165-0114(85)]

### 1979
- [*医院史料：*] **关幼波肝病诊疗程序（肝病专家系统）** Historical anchor: 关幼波肝病诊疗程序（肝病专家系统）. [[Link](https://www.bjzhongyi.com/gzb_mygs_detail/4656.html)]

### 1973
- [*Computers and Biomedical Research*; 90029-3)*] **An artificial intelligence program to advise physicians regarding antimicrobial therapy** Historical anchor: An artificial intelligence program to advise physicians regarding antimicrobial therapy. [[DOI](https://doi.org/10.1016/0010-4809(73)]

## 📑 Surveys
- [*Chinese Medicine*] **Han et al. 2026: LLM 在中医中的调优与临床应用（Scoping Review）** PRISMA-ScR scoping review (27 studies to 2025-05) on tuning (LoRA/CPT/RAG) and clinical application of TCM LLMs. [[DOI](https://doi.org/10.1186/s13020-026-01346-8)]
- [*Integrative Medicine Research*] **Yao et al. 2026: LLM 与循证中医整合（Scoping Review）** PRISMA scoping review (12 studies, 2022-11 to 2026-01) on integrating LLMs with evidence-based Chinese medicine. [[DOI](https://doi.org/10.1016/j.imr.2026.101349)]
- [*Journal of Pharmaceutical Analysis*] **Xu et al. 2026: 基于 LLM 的中医智能问答系统综述** Review of intelligent TCM question-answering systems based on LLMs (KG-QA to LLM-QA and RAG). [[DOI](https://doi.org/10.1016/j.jpha.2025.101406)]
- [*Science of Traditional Chinese Medicine*] **Chen et al. 2026: LLM 在中医的下一步（叙述性综述）** Narrative review on the next step of LLMs in TCM — multimodality, agents, and clinical translation. [[DOI](https://doi.org/10.1097/st9.0000000000000109)]
- [*Chinese Medicine*] **Guo et al. 2026: AI 与多模态数据融合推动中医现代化** Panoramic AI review (ML/DL/KG/NLP/LLM) for TCM modernization with multimodal data integration. [[DOI](https://doi.org/10.1186/s13020-025-01194-y)]
- [*Artificial Intelligence Review*] **Wu et al. 2026: AI 在中药材中的应用综述** Full-stack survey of AI in TCM herbs — compounds, targets, quality control, with an LLM section. [[DOI](https://doi.org/10.1007/s10462-026-11513-w)]
- [*Information*] **Lu et al. 2026: 深度学习中医诊断方法学质量审计** Systematic review and validation-gap analysis of deep learning for TCM disease diagnosis. [[DOI](https://doi.org/10.3390/info17060554)]
- **Agentic and Knowledge-Grounded LLMs in TCM（预注册）** OSF preregistration (not a completed review) of a systematic review on agentic and knowledge-grounded LLMs in TCM: evidence mapping, text mining, and translation readiness. [[Link](https://doi.org/10.17605/osf.io/kq8jx)]
- [*International Journal of Pattern Recognition and Artificial Intelligence*] **中医大模型关键技术综述（IJPRAI）** Survey of key technologies for TCM LLMs: knowledge organization, aided diagnosis, and clinical decision support (formally published in IJPRAI, World Scientific). [[DOI](https://doi.org/10.1142/s0218001426590263)]
- [*Journal of Traditional Chinese Medical Sciences*] **AI驱动中医诊断智能化综述（JTCMS）** Survey on multimodal fusion and LLMs for intelligent four-diagnosis in TCM: applications, challenges and outlook (JTCMS). [[DOI](https://doi.org/10.1016/j.jtcms.2026.05.002)]
- [*兰州大学学报(医学版)*] **从大语言模型到智能体（兰州大学学报医学版综述）** Chinese-language systematic review organized around the LLM-to-agent transition for TCM clinical assisted diagnosis and treatment (J. Lanzhou Univ. Med. Sci. 2026;52(4):49-57). [[DOI](https://doi.org/10.13885/j.issn.2097-681X.T20260032)]
- [*上海中医药杂志*] **人工智能驱动下的中医智能诊疗研究进展与挑战** Chinese review structured on the six-step TCM diagnosis-treatment chain (four diagnoses, pattern differentiation, prescription, outcome prediction), contrasting supervised/unsupervised/RL/deep-learning paradigms (Shanghai J. TCM 2026;60(1)). [[DOI](https://doi.org/10.16305/j.1007-1334.2026.z20250609004)]
- [*Communications in Computer and Information Science (Springer)*] **多模态大模型驱动舌脉面诊智能化综述（Springer 书章）** The only review text dedicated to multimodal-LLM-driven tongue, pulse, and facial diagnosis in TCM (Springer CCIS book chapter; weaker peer review than journals). [[DOI](https://doi.org/10.1007/978-981-95-7299-1_15)]
- [*Research*] **AI in TCM: Unraveling Herbal Medicine's Mechanisms（Research）** Broad AI-in-TCM review arguing AI should move beyond correlational analysis toward reconstructing the biological logic of syndrome differentiation and formula compatibility (Research 2026;9:1224). [[DOI](https://doi.org/10.34133/research.1224)]
- [*Journal of Integrative Medicine*] **Deep learning in TCM（J Integr Med）** Single-technology review of deep learning in TCM: medical imaging, herbal material research, data mining (J. Integr. Med. 2026;24(4):471-480). [[DOI](https://doi.org/10.1016/j.joim.2026.03.001)]
- [*Journal of Integrative Medicine*] **AI empowers the innovation of TCM（J Integr Med 评论）** Single-author perspective on AI for TCM innovation: classics mining, diagnosis standardization, drug R&D cycles (J. Integr. Med. 2026). [[DOI](https://doi.org/10.1016/j.joim.2026.05.004)]
- [*Chinese Medicine and Culture*] **AI and Big Data in TCM Standardization and Internationalization（Chin Med Cult）** Perspective on AI and big data for TCM standardization and internationalization (Chin. Med. Cult. 2026, ahead of print). [[DOI](https://doi.org/10.1097/mc9.0000000000000203)]
- [*中华中医药学刊*] **人工智能赋能中医数字化诊断：现状与挑战（中华中医药学刊）** Short Chinese review of AI-empowered digital TCM diagnosis: applications, data-quality, interpretability, and theory-integration challenges (bibliographic record only).
- [*ACL 2026*] **LLM-Based Multi-Agent Systems for Clinical Workflows（ACL 2026，邻近）** Adjacent ACL 2026 survey of workflow-level multi-agent clinical systems with a four-layer evaluation stack; no TCM coverage but methodologically isomorphic process-evaluation claims. [[DOI](https://doi.org/10.18653/v1/2026.acl-long.2123)]
- [*Pharmacological Research - Modern Chinese Medicine*] **AI in TCM: multimodal data to pharmacology and clinical decision（PRMCM 综述）** Broad AI-in-TCM review from multimodal data integration to pharmacological research and clinical decision support (Pharmacol. Res. Mod. Chin. Med. 2026; found in the third-round scan). [[DOI](https://doi.org/10.1016/j.prmcm.2026.100842)]
- [*OSF Preprints*] **Cai R et al. TCM×LLM scoping review（OSF 预印本）** OSF-preprint scoping review of LLMs in TCM (not peer-reviewed; archival). [[DOI](https://doi.org/10.17605/osf.io/2hyeq)]
- [*OSF Preprints*] **Cong H et al. TCM×LLM 综述（OSF 预印本）** OSF-preprint review of LLMs in TCM (not peer-reviewed; archival). [[DOI](https://doi.org/10.17605/osf.io/5z367)]
- [*Journal of Evidence-Based Medicine*] **Ren et al. 2025: 中医大语言模型（Scoping Review）** Arksey-O'Malley scoping review (29 studies to 2024-04) covering knowledge management, assisted care, and exam accuracy. [[DOI](https://doi.org/10.1111/jebm.12658)]
- [*Acupuncture and Herbal Medicine*] **Chen et al. 2025: 中医大语言模型系统综述** Systematic review of 10 studies (to mid-2024) on LLMs in TCM generative tasks. [[DOI](https://doi.org/10.1097/HM9.0000000000000143)]
- [*Journal of Evidence-Based Medicine*] **Guo et al. 2025: GPT 能否加速中医智能诊疗（综述+实证）** Survey plus empirical analysis of whether GPTs can accelerate intelligent TCM diagnosis and treatment. [[DOI](https://doi.org/10.1111/jebm.70004)]
- [*American Journal of Chinese Medicine*] **Shataer et al. 2025: LLM 在中医应用（State-of-the-Art Review）** State-of-the-art review scanning TCM LLM application scenarios (care, education, translation, research). [[DOI](https://doi.org/10.1142/S0192415X25500375)]
- [*AI Medicine*] **Zhang et al. 2025: 中医 LLM 短综述与展望** Short survey and outlook on TCM LLM models and tasks. [[DOI](https://doi.org/10.53941/aim.2025.100003)]
- [*Pharmacological Research*] **Meng et al. 2025: 大模型+虚拟细胞助力中医变革** Review of large models and virtual cells aiding modern analysis of stroke treatment with TCM formulas. [[DOI](https://doi.org/10.1016/j.phrs.2025.107953)]
- [*American Journal of Chinese Medicine*] **Wang et al. 2025: AI 驱动中医诊断模型进展** Systematic review of AI-driven TCM diagnostic models (four-diagnosis objectification, pattern differentiation). [[DOI](https://doi.org/10.1142/S0192415X25500259)]
- [*Journal of Evidence-Based Medicine*] **Yip et al. 2025: 中西医结合 LLM 进展与挑战** Review of LLMs in integrative medicine — progress, challenges, and opportunities. [[DOI](https://doi.org/10.1111/jebm.70031)]
- [*Journal of Pharmaceutical Analysis*] **The integration of machine learning into TCM（J Pharm Anal）** Review of machine-learning integration into TCM along diagnostic objectification and mechanism-elucidation lines (J. Pharm. Anal. 2025;15(8):101157). [[DOI](https://doi.org/10.1016/j.jpha.2024.101157)]
- [*Chinese Medicine*] **古籍知识图谱×多智能体融合综述（Chin Med）** Challenges-and-prospects review of knowledge-graph construction over ancient TCM classics, first to frame multi-agent convergence in this area (Chin. Med. 2025;20:168). [[DOI](https://doi.org/10.1186/s13020-025-01226-7)]
- [*Current Medical Science*] **AI for Spleen-Stomach Disorders in TCM（Curr Med Sci）** Single-disease-area (spleen-stomach) review of KG plus intelligent diagnosis/treatment with a symptom-syndrome-disease-formula framework (Curr. Med. Sci. 2025;45(6)). [[DOI](https://doi.org/10.1007/s11596-025-00128-x)]
- [*中华中医药学刊*] **人工智能实现中医四诊的发展现状、问题及解决路径（中华中医药学刊）** Short Chinese review of AI-based four-diagnosis objectification: face/tongue acquisition, electronic nose, pulse sensing, and low fusion of multi-diagnosis data (bibliographic record only).
- [*Healthcare*] **Intelligent Question-Answering Systems in Healthcare（Healthcare，邻近）** Adjacent review (not TCM-specific): 2018-2025 healthcare QA survey with CiteSpace bibliometrics, explicitly covering TCM formula-development scenarios (Healthcare 2025). [[DOI](https://doi.org/10.3390/healthcare13182269)]
- [*智能系统学报*] **医疗领域的大型语言模型综述（智能系统学报，邻近）** Adjacent Chinese general survey of medical LLMs (training pipeline, strategies, scenarios, challenges), a superset-context reference for TCM LLM surveys. [[DOI](https://doi.org/10.11992/tis.202405003)]
- [*智能系统学报*] **医学大语言模型的研发与应用系统综述（智能系统学报，邻近）** Adjacent systematic review of 129 medical-domain LLMs (to 2024-06) and four clinical application categories; methodologically comparable search protocol. [[DOI](https://doi.org/10.11992/tis.202410020)]
- [*南京中医药大学学报*] **Li et al. 2024 — Research progress and prospects of LLMs in TCM (Chinese)** Chinese-language review of TCM LLM pipelines, frontier techniques (prompting/RAG/RLHF), and application prospects. [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1393)]
- [*计算机工程与应用*] **Su et al. 2024 — Review of AI in TCM diagnosis and treatment (Chinese)** Chinese-language review of three AI stages in TCM care — expert systems, ML, and deep learning — with challenges. [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2312-0400)]
- [*中国工程科学*] **Song et al. 2024: AI 辅助中医辨证关键问题与技术挑战** Strategic-study review of key issues in AI-assisted TCM syndrome differentiation — multimodal fusion, symptom association, pattern quantification and reasoning, and TCM LLMs. [[DOI](https://doi.org/10.15302/J-SSCAE-2024.02.010)]
- [*Computer Materials & Continua*] **Qu et al. 2024: 中医知识图谱综述** Review of knowledge graphs in TCM — analysis, construction, applications, and prospects. [[DOI](https://doi.org/10.32604/cmc.2024.055671)]
- [*Computers in Biology and Medicine*] **Tian et al. 2024: 四诊机器学习综述** Review of machine learning for TCM four diagnoses — inspection, auscultation-olfaction, inquiry, and palpation. [[DOI](https://doi.org/10.1016/j.compbiomed.2024.108074)]
- [*Computers in Biology and Medicine*] **Zhang et al. 2021: 计算中医诊断文献综述** Literature survey of computational TCM diagnosis — symptom acquisition, pattern modeling, and systems. [[DOI](https://doi.org/10.1016/j.compbiomed.2021.104358)]
- [*Artificial Intelligence in Medicine*] **Chu et al. 2020: 中医定量知识表示模型综述** Review of quantitative knowledge representation models of TCM (ontologies, rules, statistics). [[DOI](https://doi.org/10.1016/j.artmed.2020.101810)]
- [*Evidence-Based Complementary and Alternative Medicine*] **Zhao et al. 2015: 中医患者分类进展（ML 视角）** Review of ML-driven advances in patient classification for TCM. [[DOI](https://doi.org/10.1155/2015/376716)]
- [*Briefings in Bioinformatics*] **Gu & Chen 2013: 生物信息学遇见中医** Historical review of bioinformatics meeting TCM (omics and text mining). [[DOI](https://doi.org/10.1093/bib/bbt063)]
- [*Computer Methods and Programs in Biomedicine*] **Lukman et al. 2007: 中医计算方法综述** Foundational survey of computational methods for TCM (expert systems, ML, data mining). [[DOI](https://doi.org/10.1016/j.cmpb.2007.09.008)]

## 📚 Datasets

### Curated lists
- CPM Chinese patent medicine dataset [[Data](https://gitee.com/tcmdoc/cpm)] [[Paper](https://doi.org/10.1016/j.phrs.2025.107883)]
- awesome_Chinese_medical_NLP [[Resources](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)]

### Books / pretraining corpora
- TCM-Ancient-Books [[Dataset](https://github.com/xiaopangxia/TCM-Ancient-Books)]
- TCM-Pretrain-Data-ShizhenGPT [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- Traditional-Chinese-Medicine-Dataset-Pretrain [[Dataset](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)]
- classical-tcm-canon [[Dataset](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)]
- ChiMed 2.0 [[Paper](https://arxiv.org/abs/2507.15275)]

### Benchmarks
- LingLan [[Dataset](https://github.com/TCMAI-BJTU/LingLan)] [[Paper](https://arxiv.org/abs/2602.01779)]
- TCMEval-PA [[Paper](https://doi.org/10.1038/s41597-025-06387-6)] [[Data](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[Code](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)]
- HWTCMBench [[Dataset](https://huggingface.co/datasets/Monor/hwtcm)]
- MTCMB [[Dataset](https://github.com/Wayyuanyuan/MTCMB)] [[Paper](https://arxiv.org/abs/2506.01252)]
- TCM-3CEval [[Paper](https://arxiv.org/abs/2503.07041)]
- TCM-5CEval [[Paper](https://arxiv.org/abs/2511.13169)]
- TCM-BEST4SDT [[Dataset](https://github.com/DYJG-research/TCM-BEST4SDT)] [[Paper](https://arxiv.org/abs/2512.02816)]
- TCM-Eval [[Paper](https://arxiv.org/abs/2511.07148)] [[Platform](https://tcmeval.bamaidical.com)]
- TCM-Ladder [[Dataset](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[Leaderboard](https://tcmladder.com)] [[Paper](https://arxiv.org/abs/2505.24063)]
- TCM-Tongue [[Paper](https://arxiv.org/abs/2507.18288)] [[Data](https://doi.org/10.5061/dryad.1c59zw48r)] [[Code](https://github.com/btbuIntelliSense/Intelligent-tongue-diagnosis-detection-dataset)]
- TCM-Vision-Benchmark [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Vision-Benchmark)]
- TCMBench [[Dataset](https://github.com/ywjawmw/TCMBench)] [[Paper](https://arxiv.org/abs/2406.01126)]
- TCMEval-SDT [[DOI](https://doi.org/10.1038/s41597-025-04772-9)] [[Paper](https://www.nature.com/articles/s41597-025-04772-9)] [[Code](https://github.com/zhuyan166/TCMEval)]
- ZhongJing-OMNI [[Dataset](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]
- TCM-RobustSDT [[Dataset](https://doi.org/10.6084/m9.figshare.33054974)]

### Exam datasets
- Medical-LLMs-Chinese-Exam [[Dataset](https://github.com/jingnant/Medical-LLMs-Chinese-Exam)]
- TCM-Text-Exams [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams)]

### Instruction / dialogue datasets
- neijing-sft-v1.2 [[Dataset](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2)]
- Baize-TCM-Corpus-V3 [[Dataset](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3)]
- CMtMedQA [[Dataset](https://huggingface.co/datasets/Suprit/CMtMedQA)]
- ChatMed_Consult_Dataset [[Dataset](https://huggingface.co/datasets/michaelwzhu/ChatMed_Consult_Dataset)]
- MedChatZH [[Dataset](https://huggingface.co/datasets/tyang816/MedChatZH)]
- ShenNong_TCM_Dataset [[Dataset](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)]
- TCM-Instruction-Tuning-ShizhenGPT [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- TCMChat-dataset-600k [[Dataset](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- Traditional-Chinese-Medicine-Dataset-SFT [[Dataset](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]
- ChP-TCM [[Data](https://github.com/QLU-NLP/BianCang/tree/main/ChP-TCM)] [[Paper](https://arxiv.org/abs/2411.11027)]
- TCMNSCLC [[Dataset](https://huggingface.co/datasets/zhangxinxin0428/TCMNSCLC)] [[DOI](https://doi.org/10.5281/zenodo.21027568)]

### Knowledge graphs
- OpenTCM-KG [[Code](https://github.com/OpenTCM01/OpenTCM)] [[Paper](https://arxiv.org/abs/2504.20118)]
- TCM-MKG [[Data](https://zenodo.org/records/15395588)]
- TCM_KG [[Dataset](https://github.com/ywjawmw/TCM_KG)]

### Hugging Face models (selected)
- Xinghe [[Model](https://huggingface.co/zsyjsld/Xinghe1.2-9B)] [[GGUF](https://huggingface.co/zsyjsld/Xinghe1.2-9B-GGUF)]
- BianCang [[Qwen2.5-7B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)] [[Qwen2.5-14B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-14B-Instruct)]
- ChatTCM [[ChatTCM-7B-Pretrain](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)]
- ChatTCM-7B-SFT [[Model](https://huggingface.co/SylvanL/ChatTCM-7B-SFT)]
- Lingdan [[Lingdan-13B-Base](https://huggingface.co/TCMLLM/Lingdan-13B-Base)] [[Lingdan-13B-PR](https://huggingface.co/TCMLLM/Lingdan-13B-PR)]
- ShenNong-TCM-LLM [[ShenNong-TCM-LLM](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]
- ShizhenGPT [[7B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-LLM)] [[7B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-VL)] [[7B-Omni](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[32B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-LLM)] [[32B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-VL)]
- TCMChat [[TCMChat-600k](https://huggingface.co/ZJUFanLab/TCMChat-600k)]
- ZhongJing [[ZhongjingGPT1_13B](https://huggingface.co/CMLM/ZhongjingGPT1_13B)] [[ZhongJing-2-1.8B](https://huggingface.co/CMLL/ZhongJing-2-1_8b)]
- medchatzh [[medchatzh](https://huggingface.co/tyang816/medchatzh)]
- Baize [[Model](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model)] [[8B-16bit](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit)]
- ZhiFangDanTai [[Model](https://huggingface.co/tczzx6/ZhiFangDanTai1.0)]

### 语料/指令
- HSQ-TD（健身气功指令微调数据集） [[Dataset](https://doi.org/10.57760/sciencedb.35843)]
