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
- **TCM-DiffRAG** Syndrome-differentiation RAG with a general KG, a personalized KG, and chain-of-thought. [[Paper](https://arxiv.org/abs/2602.22828)] [[Code](https://github.com/LiJianmin6706/Tcm_Diff_RAG)]
- [*JMIR Medical Informatics*] **TongueVLM** Multimodal VLM for TCM tongue diagnosis, description generation, and constitution reasoning. [[Paper](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- **Xinghe** Qwen3.5-9B reasoning TCM model grounded in the *Neijing*, with explicit CoT pattern differentiation and safety boundaries. [[Model](https://huggingface.co/zsyjsld/Xinghe1.2-9B)] [[GGUF](https://huggingface.co/zsyjsld/Xinghe1.2-9B-GGUF)] [[Dataset](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2)]
- **LingLan** Large multi-task TCM benchmark: 5 domains, 13 subtasks, 25,624 instances. [Beijing Jiaotong University et al.] [[Paper](https://arxiv.org/abs/2602.01779)] [[Code](https://github.com/TCMAI-BJTU/LingLan)] [[Website](http://tcmnlp.com)]

### 2025
- **BenCao** Instruction-aligned multimodal TCM assistant (ChatGPT/GPTs Store) with tongue APIs and knowledge bases (distinct from HuaTuo/BenCao). [[Paper](https://arxiv.org/abs/2510.17415)]
- **ChatTCM** Fully open TCM LLM from pretraining data through released weights. [[Model](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)] [[Pretrain data](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)] [[SFT data](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]
- [*Journal of King Saud University Computer and Information Sciences*] **DiagX-DT** Exclusionary syndrome-differentiation reasoning with CoT and an external TCM knowledge base. [[DOI](https://doi.org/10.1007/s44443-025-00123-1)]
- **DoPI** Doctor-like proactive inquiry TCM LLM (guide + expert models); reported inquiry accuracy 84.68%. [[Paper](https://arxiv.org/abs/2507.04877)]
- [*IEEE ICIP 2025*] **MCM** Multi-agent collaborative multimodal TCM diagnosis framework (IEEE ICIP 2025). [Shanghai Computer Software Technology Development Center] [[Code](https://github.com/JerryMazeyu/MCM)]
- **MTCMB** Multi-task TCM benchmark (~12 subsets, ~7.1k samples) covering knowledge, reasoning, formulas, and safety. [[Paper](https://arxiv.org/abs/2506.01252)] [[Code](https://github.com/Wayyuanyuan/MTCMB)]
- **OpenTCM** GraphRAG TCM retrieval and diagnosis system with a gynecology classics knowledge graph. [[Paper](https://arxiv.org/abs/2504.20118)] [[Code](https://github.com/OpenTCM01/OpenTCM)]
- [*Pharmacological Research*] **RAG-CPMF** Multi-LLM verification + RAG for Chinese patent medicine recommendation, with a living public CPM dataset. [[DOI](https://doi.org/10.1016/j.phrs.2025.107883)] [[Data](https://gitee.com/tcmdoc/cpm)]
- **ShizhenGPT** Multimodal TCM LLM supporting the four diagnoses (inspection, auscultation-olfaction, inquiry, palpation). [The Chinese University of Hong Kong, Shenzhen et al.] [[Paper](https://arxiv.org/abs/2508.14706)] [[Code](https://github.com/FreedomIntelligence/ShizhenGPT)] [[Model](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[Pretrain data](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)] [[Instruction data](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- [*npj Digital Medicine*] **TCM LLM acupuncture clinical evaluation** Real-case evaluation of 7 general LLMs vs licensed acupuncturists on SDT, point selection, needling, and herbs (*npj Digital Medicine*). [[DOI](https://doi.org/10.1038/s41746-025-01845-2)]
- **TCM-3CEval** Three-axis TCM LLM evaluation: core knowledge, classics comprehension, and clinical decision-making. [[Paper](https://arxiv.org/abs/2503.07041)]
- **TCM-5CEval** Five-dimension deep evaluation extending TCM-3CEval with materia medica and non-drug therapies. [[Paper](https://arxiv.org/abs/2511.13169)]
- **TCM-BEST4SDT** Case benchmark for syndrome differentiation and treatment (knowledge / ethics / safety / SDT). [[Paper](https://arxiv.org/abs/2512.02816)] [[Code](https://github.com/DYJG-research/TCM-BEST4SDT)]
- [*Computers in Biology and Medicine*] **TCM-KLLaMA** KG-fused LLM for intelligent TCM formula generation. [[DOI](https://doi.org/10.1016/j.compbiomed.2025.109887)]
- [*NeurIPS 2025*] **TCM-Ladder** First large multimodal TCM QA benchmark with 52,000+ items (NeurIPS 2025). [[Paper](https://arxiv.org/abs/2505.24063)] [[Code](https://github.com/orangeshushu/TCM-Ladder)] [[Leaderboard](https://tcmladder.com)]
- [*APWeb-WAIM 2025*] **TCM-R1** TCM LLM with GRPO-enhanced reasoning. [Southwest University] [[Paper](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*Pharmacological Research*] **TCMChat** Herbal-knowledge chatbot and recommendation system. [Zhejiang University] [[Paper](https://doi.org/10.1016/j.phrs.2024.107012)] [[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1043661824004754)] [[Code](https://github.com/ZJUFanLab/TCMChat)] [[Model](https://huggingface.co/ZJUFanLab/TCMChat-600k)] [[Dataset](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- [*IEEE BIBM 2025*] **ViTCM-LLM** Qwen2.5-VL + RAG tongue multimodal clinical framework; MedTCM dataset and TDEU metric (precursor to MMIR-TCM). [[DOI](https://doi.org/10.1109/bibm66473.2025.11357113)] [[Code](https://github.com/jw-chae/ViTCM_LLM)] [[Model](https://huggingface.co/Mark-CHAE/ViTCM-LLM)]
- [*JMIR Medical Informatics*] **Yaoshi-RAG** Uncertain-KG RAG for medicine–food homology dietary recommendation with personalization and explainability. [[DOI](https://doi.org/10.2196/75279)]
- **RenShu-AI** FastAPI + LangGraph multi-agent TCM consultation system combining GraphRAG and DeepSeek-TCM. [[Code](https://github.com/yanlinPeng-code/RenShu-AI)]
- [*Tsinghua Science and Technology*] **ZhongJing** Open TCM large language model (ZhongJing). [Fuyao University of Science and Technology, Health Yangtze River Delta Research Institute, Fudan University, Tongji University] [[Paper](https://doi.org/10.26599/TST.2025.9010046)] [[Code](https://github.com/pariskang/CMLM-ZhongJing)] [[Model](https://huggingface.co/CMLM/ZhongjingGPT1_13B)]
- [*Information Fusion*] **Tianyi** ~7B TCM LLM from NJUCM et al. with reading–clinic–apprenticeship training stages, TCMEval, and real-world validation. [Nanjing University of Chinese Medicine] [[Paper](https://arxiv.org/abs/2505.13156)] [[News](https://kjc.njucm.edu.cn/2025/0910/c3750a160492/page.htm)]
- **TianHui** Domain LLM for 12 TCM scenarios (DeepSeek-R1-Distill-Qwen-14B + PT/SFT) with open code and eval scripts. [[Paper](https://arxiv.org/abs/2509.19834)] [[Code](https://github.com/JYfantast/TianHui)]
- [*Expert Systems with Applications*] **Qibo** TCM LLM and Qibo Benchmark from Tianjin University et al.; CPT + SFT for SDT and QA. [Tianjin University, Tianjin University of Traditional Chinese Medicine] [[Paper](https://arxiv.org/abs/2403.16056)] [[DOI](https://doi.org/10.1016/j.eswa.2025.127672)]
- [*IEEE Journal of Biomedical and Health Informatics*] **BianCang** BianCang TCM LLM series (IEEE JBHI); 14B open-weight release in Dec 2025. [Qilu University of Technology] [[Paper](https://arxiv.org/abs/2411.11027)] [[Code](https://github.com/QLU-NLP/BianCang)] [[Model](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)] [[DOI](https://doi.org/10.1109/jbhi.2025.3612415)]
- **ZMT-M1** ZMT-M1 TCM LLM and the dynamic, extensible TCM-Eval benchmark platform. [Beihang University] [[Paper](https://arxiv.org/abs/2511.07148)] [[Platform](https://tcmeval.bamaidical.com)]
- **Baize-TCM-LLM** ICMM Baize TCM QA models on Qwen3 (0.6B/8B) with ~157k LoRA-tuning examples. [Institute of Chinese Materia Medica, CACMS] [[Model](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model)] [[Dataset](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3)]
- [*IEEE Journal of Biomedical and Health Informatics*] **ZhiFangDanTai** GraphRAG + LLM fine-tuning for interpretable formula generation (sovereign–minister–assistant–courier, efficacy, contraindications) with open weights. [[Paper](https://arxiv.org/abs/2509.05867)] [[DOI](https://doi.org/10.1109/jbhi.2025.3607819)] [[Model](https://huggingface.co/tczzx6/ZhiFangDanTai1.0)]
- [*Cell Discovery*] **ShenNong Alpha** ShenNong Alpha herbal/materia medica foundation model. [Westlake University] [[Website](https://shennongalpha.westlake.edu.cn/)] [[Paper](https://www.nature.com/articles/s41421-025-00776-2)] [[Code](https://github.com/shennong-program/shennongname)]
- **Jingfang** LLM-based multi-agent TCM diagnosis/treatment system reporting large relative SDT gains under the authors' protocol. [[Paper](https://arxiv.org/abs/2502.04345)]

### 2024
- **Chinese-LLaVA-Med** Chinese medical multimodal large language model. [[Code](https://github.com/BUAADreamer/Chinese-LLaVA-Med)]
- [*Computers in Biology and Medicine*] **MedChatZH** Chinese TCM consultation dialogue LLM. [[Paper](https://doi.org/10.1016/j.compbiomed.2024.108163)] [[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0010482524003743)] [[Dataset](https://huggingface.co/datasets/tyang816/MedChatZH)] [[Model](https://huggingface.co/tyang816/medchatzh)] [[Code](https://github.com/tyang816/MedChatZH)]
- [*Digital Chinese Medicine*] **TCMLLM / Lingdan** TCMLLM / Lingdan for TCM modeling and prescription recommendation. [Beijing Jiaotong University] [[Paper](https://doi.org/10.1016/j.dcmed.2025.01.007)] [[ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2589377725000072)] [[Code](https://github.com/2020MEAI/TCMLLM)] [[Lingdan code](https://github.com/TCMAI-BJTU/LingdanLLM)] [[Model](https://huggingface.co/TCMLLM/Lingdan-13B-Base)]
- **BigDataTCM** Vertical TCM domain large language model. [Henan University of Technology] [[Code](https://github.com/HAUT-CS/BigDataTCM)]
- **MING** Chinese medical consultation LLM (MING). [Shanghai Jiao Tong University] [[Paper](https://arxiv.org/abs/2404.09027)] [[Related MedCare](https://aclanthology.org/2024.findings-emnlp.619/)] [[Code](https://github.com/MediaBrain-SJTU/MING)]
- [*ACM Trans. Knowl. Discov. Data*] **BenCao (formerly HuaTuo)** Instruction-tuned Chinese medical LLM (BenCao / formerly HuaTuo). [Harbin Institute of Technology] [[Paper](https://arxiv.org/pdf/2309.04175.pdf)] [[Code](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)]

### 2023
- **ChatMed** Series of Chinese medical large language models. [[Code](https://github.com/michael-wzhu/ChatMed)]
- **XrayGLM** Chinese multimodal medical LLM for chest X-ray interpretation. [[Code](https://github.com/WangRongsheng/XrayGLM)]
- [*EMNLP findings*] **HuaTuoGPT** Large language model trained on Chinese medical corpora (HuaTuoGPT). [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[Paper](https://aclanthology.org/2023.findings-emnlp.725/)] [[Code](https://github.com/FreedomIntelligence/HuatuoGPT)]
- **QiZhenGPT** Chinese clinical QA model for drugs, diseases, procedures, and labs (QiZhenGPT). [Zhejiang University] [[Code](https://github.com/CMKRG/QiZhenGPT)]
- **Sunsimiao** Chinese medical large language model (Sunsimiao). [East China University of Science and Technology] [[Code](https://github.com/X-D-Lab/Sunsimiao)]
- **BianQue** Chinese proactive health LLM for everyday living spaces (BianQue). [South China University of Technology, Guangdong Key Laboratory of Digital Twin Humans] [[Code](https://github.com/scutcyr/BianQue)]
- **ShenNong-TCM-LLM** Open TCM-focused large language model (ShenNong-TCM-LLM). [[Code](https://github.com/michael-wzhu/ShenNong-TCM-LLM)] [[Dataset](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)] [[Model](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]
- **HuangDi** QA LLM for classical TCM texts (HuangDi). [Nanjing University, Zhengzhou University] [[Code](https://github.com/Zlasejd/HuangDI)]

## 📚 Datasets

### Curated lists
- CPM Chinese patent medicine dataset [[Data](https://gitee.com/tcmdoc/cpm)] [[Paper](https://doi.org/10.1016/j.phrs.2025.107883)]
- awesome_Chinese_medical_NLP [[Resources](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)]

### Books / pretraining corpora
- TCM-Ancient-Books [[Dataset](https://github.com/xiaopangxia/TCM-Ancient-Books)]
- TCM-Pretrain-Data-ShizhenGPT [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- Traditional-Chinese-Medicine-Dataset-Pretrain [[Dataset](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)]
- classical-tcm-canon [[Dataset](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)]

### Benchmarks
- LingLan [[Dataset](https://github.com/TCMAI-BJTU/LingLan)] [[Paper](https://arxiv.org/abs/2602.01779)]
- TCMEval-PA [[Paper](https://doi.org/10.1038/s41597-025-06387-6)] [[Data](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[Code](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)]
- HWTCMBench [[Dataset](https://huggingface.co/datasets/Monor/hwtcm)]
- MTCMB [[Dataset](https://github.com/Wayyuanyuan/MTCMB)] [[Paper](https://arxiv.org/abs/2506.01252)]
- TCM-3CEval [[Paper](https://arxiv.org/abs/2503.07041)]
- TCM-5CEval [[Paper](https://arxiv.org/abs/2511.13169)]
- TCM-BEST4SDT [[Dataset](https://github.com/DYJG-research/TCM-BEST4SDT)] [[Paper](https://arxiv.org/abs/2512.02816)]
- TCM-Eval [[Paper](https://arxiv.org/abs/2511.07148)] [[Platform](https://tcmeval.bamaidical.com)]
- TCM-Ladder [[Dataset](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[Leaderboard](https://tcmladder.com)]
- TCM-Tongue [[Paper](https://arxiv.org/abs/2507.18288)] [[Data](https://doi.org/10.5061/dryad.1c59zw48r)] [[Code](https://github.com/btbuIntelliSense/Intelligent-tongue-diagnosis-detection-dataset)]
- TCM-Vision-Benchmark [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Vision-Benchmark)]
- TCMBench [[Dataset](https://github.com/ywjawmw/TCMBench)] [[Paper](https://arxiv.org/abs/2406.01126)]
- TCMEval-SDT [[Paper](https://www.nature.com/articles/s41597-025-04772-9)] [[Code](https://github.com/zhuyan166/TCMEval)]
- ZhongJing-OMNI [[Dataset](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]

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
