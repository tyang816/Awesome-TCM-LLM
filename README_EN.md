# 🔥 Open TCM Models, Data, Papers, and Patents

**Language / 语言:** [English](README_EN.md) | [中文](README.md)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  ![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork) [![中文门户](https://img.shields.io/badge/中医资源-门户-blue)](https://tyang816.github.io/zh/projects/tcm/) [![Project](https://img.shields.io/badge/Project-tyang816.github.io-informational)](https://tyang816.github.io/projects/tcm/)

Open TCM models, datasets, papers, and patents, plus a few related Chinese medical resources. Right now: 87 news items, 117 models, 83 surveys, 73 patents, 203 datasets, 437 method papers, and 450 TCM–AI supervisors. [PRs welcome](CONTRIBUTING.md).

[Project page](https://tyang816.github.io/projects/tcm/) · [Chinese catalog](https://tyang816.github.io/zh/projects/tcm/) · [Wiki](wiki/Home.md) · [Homepage](https://tyang816.github.io/)

## Start here

Only about 21 TCM checkpoints are actually public; they are under [Open models](#open-models). Hospital and company releases in the news usually ship no weights, so they make poor experimental baselines.

Recent work has expanded into multimodal models, agents, and clinical reasoning evaluation. Compare examination knowledge, syndrome classification, and prescription tasks separately; TCM-Ladder, LingLanMedBench, and MTCMB offer complementary evaluation resources.

| If you want to… | Try | Note |
| --- | --- | --- |
| Get a model running | **[BianCang](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)**, **[仲景 (ZhongJing)](https://huggingface.co/CMLM/ZhongjingGPT1_13B)** | Paper, weights, and code |
| Build TCM inquiry | **[MedChatZH](https://github.com/tyang816/MedChatZH)** | Comes with consult dialogues |
| Tongue / four diagnoses | **[ShizhenGPT](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)** | Multimodal; weights and data are public |
| Train further | **[ChatTCM](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)**, **[神农大模型 (ShenNong-TCM-LLM)](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)** | Pretrain or instruction data is released |
| Stay small | **[Xinghe](https://huggingface.co/zsyjsld/Xinghe1.2-9B)** | 9B, GGUF available |
| Run a comparison | **[TCM-Ladder](https://arxiv.org/abs/2505.24063)**, **[LingLanMedBench](https://arxiv.org/abs/2602.01779v2)** | Tasks are spelled out; more under [Datasets](#datasets) |
| Write related work | Recent scoping reviews | Skim [Surveys](#surveys) before individual model papers |
| Find a supervisor | [Supervisors](#supervisors) | Universities, industry, and hospitals |

Same name does not mean the same project. ZhongJingGPT is not the AAAI CMtMedQA line, and more than one benchmark is called TCM-Eval. [Getting Started](wiki/Getting-Started.md) if that is confusing.

## Supervisors

By region, then by university, hospital, or company.

<details>
<summary>Beijing (80)</summary>

<details>
<summary>Beijing University of Chinese Medicine (24)</summary>

- **Jianxin Chen** Professor and doctoral supervisor in the School of Life Sciences, Beijing University of Chinese Medicine. Works on TCM data mining and integrative AI, including SymMap, and recruits 2026 doctoral students in TCM informatics and big data. [School of Life Sciences, Beijing University of Chinese Medicine] [[Homepage](https://shengming.bucm.edu.cn/jyjx/yjs/dsfc/584c26a2af124c56841daf796c2d24c4.htm)] [[Admissions](https://shengming.bucm.edu.cn/docs/2026-03/094923d029c745a7aa5b3f7493ee8d2c.pdf)]
- **Jincheng Guo** Professor and doctoral supervisor in the School of Traditional Chinese Medicine, Beijing University of Chinese Medicine. Works on TCM bioinformatics, digital twins, and agents, including HERB and POINT, and jointly recruits 2026 doctoral students with Zhao Yi of the Chinese Academy of Sciences. [School of Traditional Chinese Medicine, Beijing University of Chinese Medicine] [[Homepage](https://jichu.bucm.edu.cn/xygk/jxkyjg/yjstpt/zyxxxyjzx/szdw22/b1fbbc5c520c4cd88e780576f381dc05.htm)] [[Admissions](https://shengming.bucm.edu.cn/docs/2026-03/445adae3d9514d6580b200fb317f602c.pdf)]
- **Xiaohong Gu** Professor and doctoral supervisor at Beijing University of Chinese Medicine, and dean of the Institute of TCM Epidemic Diseases. Works on warm-disease theory and digital inheritance of master physicians, and co-developed the Tianyi TCM model. [Beijing University of Chinese Medicine] [[Homepage](https://jichu.bucm.edu.cn/xygk/jxkyjg/jys/wbjys/szdw6/220d8b80aef84862a6355b25dfef5f29.htm)] [[News](https://www.njucm.edu.cn/2025/0910/c6754a160459/page.htm)]
- **Bing Xu** Professor, doctoral supervisor, and vice dean of the School of Chinese Materia Medica at Beijing University of Chinese Medicine. Works on intelligent TCM manufacturing, built the iTCM system, and leads construction of the Xinhuo Zhongguoyao model. [School of Chinese Materia Medica, Beijing University of Chinese Medicine] [[Homepage](https://infopharm.bucm.edu.cn/kxyj/yjdw/31874.htm)] [[News](https://zhongyao.bucm.edu.cn/yyxw/57d9fb0a8af1496b88ca404e51e4e7d1.htm)]
- **Xiaoqing Zhang** Doctoral supervisor in the School of Life Sciences, Beijing University of Chinese Medicine. Works on AI for quantitative TCM syndrome differentiation, head-and-face inspection, and intelligent TCM devices. [School of Life Sciences, Beijing University of Chinese Medicine] [[Homepage](https://shengming.bucm.edu.cn/jyjx/yjs/dsfc/31df29a5d6b04e539b7a90e1bff9d2bc.htm)] [[Admissions](https://shengming.bucm.edu.cn/docs/2026-03/9f61983b960a443ea888399d6d5b09d5.pdf)]
- **Zhisheng Wu** Researcher and doctoral supervisor at Beijing University of Chinese Medicine, leading intelligent Chinese-medicine manufacturing. Works on manufacturing measurement and the intelligent-manufacturing platform. [Beijing University of Chinese Medicine] [[Homepage](https://infopharm.bucm.edu.cn/kxyj/yjdw/44025.htm)]
- **Yun Wang** Researcher, doctoral supervisor, and chair of the Department of Chinese Medicine Informatics, Beijing University of Chinese Medicine. Works on information fusion, intelligent property-based design, large models, and knowledge graphs. [School of Chinese Materia Medica, Beijing University of Chinese Medicine] [[Homepage](https://zhongyao.bucm.edu.cn/szdw/sssds/szzyxssds/f55f7fd12b174137b01a59dd3d256dd1.htm)]
- **Yanling Zhang** Researcher and doctoral supervisor in the School of Chinese Materia Medica, Beijing University of Chinese Medicine. Works from virtual screening to AI formula design. [School of Chinese Materia Medica, Beijing University of Chinese Medicine] [[Homepage](https://zhongyao.bucm.edu.cn/szdw/bssds/szzyx_20220622170829152708/a2c5cdca5e504f91b7f702a883bdd762.htm)]
- **Mei Zhang** Researcher and doctoral supervisor at Beijing University of Chinese Medicine. Develops digital olfactory-diagnosis devices for objective TCM smelling and syndrome differentiation. [Beijing University of Chinese Medicine] [[Homepage](https://zhongyao.bucm.edu.cn/szdw/bssds/zyfxxbsds_20220622170729411401/d86a8ba8fa764445b796a6f218c2a79d.htm)]
- **Ji Wang** Professor, doctoral supervisor, and executive deputy dean of the National Institute of TCM Constitution and Preventive Medicine. Works on constitution, artificial intelligence, and digital health. [Beijing University of Chinese Medicine] [[Homepage](https://tizhi.bucm.edu.cn/szdw/jsjj/2efe37af25e147e5af41ad78f80c669f.htm)]
- **Zhengjun Zhang** Dean of the School of Data Science and Artificial Intelligence, Beijing University of Chinese Medicine. Uses big data and systems pharmacology to connect syndrome differentiation with precision medication. [School of Data Science and Artificial Intelligence, Beijing University of Chinese Medicine] [[News](http://finance.people.com.cn/n1/2026/0817/c1004-40781088.html)]
- **Xu Wang** Associate researcher and master's supervisor at Beijing University of Chinese Medicine. Uses images and AI for multimodal tongue, face, and brain syndrome analysis. [School of Life Sciences, Beijing University of Chinese Medicine] [[Homepage](https://shengming.bucm.edu.cn/jyjx/yjs/dsfc/ede8719994ab4d14904fd1e3f67bc5cd.htm)]
- **Yanjiang Qiao** Professor and doctoral supervisor at Beijing University of Chinese Medicine. Works on Chinese-medicine informatics, property data, and intelligent manufacturing. [Beijing University of Chinese Medicine] [[Homepage](https://infopharm.bucm.edu.cn/kxyj/yjdw/31864.htm)]
- **Xin Niu** Second-class professor and doctoral supervisor at Beijing University of Chinese Medicine. Digitizes the four examinations and developed pulse and combined-examination devices. [School of Traditional Chinese Medicine, Beijing University of Chinese Medicine] [[Homepage](https://www.ais.cn/mentor/mentorDetail/e9bed53e-5e3b-11ec-b045-a85e45a23623)]
- **Xuezhi Yang** Professor at Beijing University of Chinese Medicine. Leads a portable device that combines inspection, listening, inquiry, and palpation. [Beijing University of Chinese Medicine] [[Homepage](https://www.bucm.edu.cn/bzyyw/10779fdcfccf41a5b46e1f58530374ab.htm)]
- **Qi Wang** Academician of the Chinese Academy of Engineering and National TCM Master at Beijing University of Chinese Medicine. Built the TCM constitution identification system and its digital monitoring. [Beijing University of Chinese Medicine] [[Homepage](https://kgyjzzx.bucm.edu.cn/kjcg/zhcg/b523b0ce71924f8ea8ff5352b2252f0f.htm)]
- **Jing Guan** Associate professor of Chinese diagnostics and master's supervisor at Beijing University of Chinese Medicine. Works on objective tongue diagnosis and intelligent tongue-diagnosis devices. [School of Traditional Chinese Medicine, Beijing University of Chinese Medicine] [[Homepage](https://jichu.bucm.edu.cn/yjsjy/dsjs/zyzdx/78a37699a21e462bad60e04054b85890.htm)]
- **Xingguang Ma** Professor and graduate supervisor at the School of Management, Beijing University of Chinese Medicine. Works on Chinese-medicine databases, famous-doctor case mining, and tongue-image recognition. [School of Management, Beijing University of Chinese Medicine] [[Homepage](https://sm.bucm.edu.cn/szdw/ywds/880e3600089f422e8e747b9eeb6da0f6.htm)]
- **Xinyuan Shi** Professor and doctoral supervisor at Beijing University of Chinese Medicine. Works on Chinese-medicine informatics, in-process quality control, and near-infrared quantitative models. [School of Chinese Materia Medica, Beijing University of Chinese Medicine] [[Homepage](https://infopharm.bucm.edu.cn/kxyj/yjdw/31867.htm)]
- **Nan Li** Associate researcher and master's supervisor at Beijing University of Chinese Medicine. Works on in-process quality control for Chinese-medicine production. [School of Chinese Materia Medica, Beijing University of Chinese Medicine] [[Homepage](https://infopharm.bucm.edu.cn/kxyj/yjdw/index.htm)]
- **Wuzhen Qi** Lecturer at Beijing University of Chinese Medicine. Builds intelligent-manufacturing instruments, spectral sensors, and critical-quality-attribute detection for Chinese medicine. [School of Chinese Materia Medica, Beijing University of Chinese Medicine] [[Homepage](https://infopharm.bucm.edu.cn/kxyj/yjdw/77133.htm)]
- **Xingxing Dai** Senior experimentalist at Beijing University of Chinese Medicine. Works on processing equipment, intelligent sensory evaluation, and digitized in-process quality. [School of Chinese Materia Medica, Beijing University of Chinese Medicine] [[Homepage](https://sysglzx.bucm.edu.cn/zxgk/jsdw/710b407f00ea4135b3d0d4612168b9a0.htm)]
- **Cong Yan** Professor and doctoral supervisor at Beijing University of Chinese Medicine. Leads embodied-intelligence tuina robots that replay famous doctors' techniques with an expert model. [School of Life Sciences, Beijing University of Chinese Medicine] [[Homepage](https://shengming.bucm.edu.cn/jyjx/yjs/dsfc/553c4da4cd0943208218068860bff928.htm)]
- **Shuzhen Guo** Professor and doctoral supervisor at Beijing University of Chinese Medicine. Works on integrative pharmacology and is a co-corresponding author of BATMAN-TCM 2.0. [School of Traditional Chinese Medicine, Beijing University of Chinese Medicine] [[Homepage](https://jichu.bucm.edu.cn/xygk/jxkyjg/syzx/kysyzx/szdw28/9c337b804aed4160aaa36a33703db7da.htm)]

</details>

<details>
<summary>China Academy of Chinese Medical Sciences (20)</summary>

- **Haiyu Xu** Chief researcher at the China Academy of Chinese Medical Sciences and director of the Integrative Chinese Medicine Research Center. Works on integrative pharmacology and TCM big data, including ETCM and SoFDA, and recruits 2026 doctoral students in TCM AI at Liaoning University of Traditional Chinese Medicine. [Institute of Chinese Materia Medica, China Academy of Chinese Medical Sciences] [[Homepage](https://www.icmm.ac.cn/zjjj/sxyjyd/content_128.html)] [[Admissions](https://gjhzjlc.lnutcm.edu.cn/liaoningzhongyiyaodaxue2026nianshenqing-kaohejishuobolianduboshiyanjiushengzhaoshengzhuanyemuluxueshuxuewei.pdf)]
- **Baoyan Liu** Chief researcher at the China Academy of Chinese Medical Sciences. Works on clinical-outcome evaluation and TCM big data, contributes to Lingdan-V2, and collaborates with Gushengtang on TCM models and real-world data. [China Academy of Chinese Medical Sciences] [[Profile](https://www.ch-s.wtcmaw.events/%E5%8F%82%E4%BC%9A%E5%8D%95%E4%BD%8D/%E4%B8%BB%E5%B8%AD%E5%9B%A2/speaker-bio-%E5%88%98%E4%BF%9D%E5%BB%B6)] [[Paper](https://arxiv.org/abs/2610.14705)] [[News](https://www.gstzy.cn/news/detail/10/14073.html)]
- **Tong Yu** Researcher and master's supervisor at the Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences. Works on TCM knowledge graphs, terminology, and vertical models. [Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences] [[Homepage](http://www.cintcm.ac.cn/tutor.thtml?id=8370)]
- **Qi Yu** Researcher and master's supervisor at the Institute of Information on Traditional Chinese Medicine. Works on digital inheritance of master physicians, clinical knowledge bases, and TCM AI. [Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences] [[Homepage](http://www.cintcm.ac.cn/tutor.thtml?id=8272)]
- **Jinghua Li** Researcher, doctoral supervisor, and director of the Intelligent R&D Center for Great Health at the Institute of Information on Traditional Chinese Medicine. Works on clinical decision support, medical-case platforms, and four-diagnosis robots. [Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences] [[Homepage](http://www.cintcm.ac.cn/tutor.thtml?id=8351)]
- **Haiyan Li** Researcher and doctoral supervisor at the Institute of Information on Traditional Chinese Medicine. Works on large-model recommendation of Chinese patent medicines and the Yiyuan TCM model. [Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences] [[Homepage](http://www.cintcm.ac.cn/tutor.thtml?id=8065)]
- **Bing Li** Researcher at the Institute of Chinese Materia Medica and deputy director of the Digital Materia Medica Center. Works on knowledge graphs of medical classics, classic-text models, and clinical decision support. [Institute of Chinese Materia Medica, China Academy of Chinese Medical Sciences] [[Homepage](https://wenxian.sdutcm.edu.cn/info/1040/2352.htm)]
- **Yanqiong Zhang** Researcher, doctoral supervisor, and director of the Research Center for TCM Property Theory. Uses omics data and biological networks to study Chinese-medicine actions and rational use. [Institute of Chinese Materia Medica, China Academy of Chinese Medical Sciences] [[Homepage](https://zhongyao.bucm.edu.cn/szdw/bssds/lczyxbsds_20220622170829152708/a055bcd9f9a04c558a83f4a9c8c28ede.htm)]
- **Hongjun Yang** Vice president, researcher, and doctoral supervisor at the China Academy of Chinese Medical Sciences. Works on integrative pharmacology, the TCM inheritance platform, and AI4TCM. [China Academy of Chinese Medical Sciences] [[Homepage](https://www.merc.ac.cn/zykx/detail.html?contentId=89&id=13)]
- **Nanyue Wang** Researcher and doctoral supervisor at the Experimental Research Center, China Academy of Chinese Medical Sciences. Works on four-diagnosis devices and AI integration of the four examinations. [Experimental Research Center, China Academy of Chinese Medical Sciences] [[Homepage](https://www.merc.ac.cn/zykx/detail.html?contentId=11&id=13)]
- **Yan Zhu** Associate researcher and master's supervisor at the Institute of Information on Traditional Chinese Medicine. Works on TCM terminology, ontologies, and formula data mining. [Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences] [[Homepage](http://www.cintcm.ac.cn/tutor.thtml?id=8343)]
- **Tiancai Wen** Senior engineer and doctoral supervisor at the TCM Data Center, China Academy of Chinese Medical Sciences. Works on real-world record mining and decision support. [TCM Data Center, China Academy of Chinese Medical Sciences] [[Homepage](http://www.cintcm.ac.cn/tutor.thtml?id=8372)]
- **Junwen Wang** Researcher and doctoral supervisor at the Institute of Basic Theory for Chinese Medicine. Works on intelligent assisted Chinese diagnosis and equipment. [Institute of Basic Theory for Chinese Medicine, China Academy of Chinese Medical Sciences] [[Homepage](https://www.ibtcm.ac.cn/zjds-detail.thtml?contentId=8342)]
- **Shilin Chen** Chief professor at Chengdu University of Traditional Chinese Medicine and chief researcher at the China Academy of Chinese Medical Sciences. Founded herbgenomics and built the Bencao Think Tank industry model. [Chengdu University of Traditional Chinese Medicine, China Academy of Chinese Medical Sciences] [[News](https://academics.casad.cas.cn/xshd/kxyjsqylt/2024/d180c/202507/t20250731_5078674.html)]
- **Yufeng Zhao** Researcher, doctoral supervisor, and deputy director of the Chinese-medicine data center at the China Academy of Chinese Medical Sciences. Analyzes real-world Chinese-medicine data. [Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences] [[Homepage](http://www.cintcm.ac.cn/tutor.thtml?id=8349)]
- **Shuo Yang** Researcher and master's supervisor at the China Academy of Chinese Medical Sciences. Works on syndrome ontologies, evidence-based knowledge representation, and digitization. [Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences] [[Homepage](http://www.cintcm.ac.cn/tutor.thtml?id=8353)]
- **Junhong Gao** Researcher, doctoral supervisor, and director of the needling-technique lab at the Institute of Acupuncture and Moxibustion. Studies acupuncture mechanisms and develops acupuncture equipment. [Institute of Acupuncture and Moxibustion, China Academy of Chinese Medical Sciences] [[Homepage](https://www.acuworld.ac.cn/info_content_ds.jsp?id=922)]
- **Peijing Rong** Chief researcher, doctoral supervisor, and deputy director of the Institute of Acupuncture and Moxibustion. Leads brain-representation research on meridians, including a meridian knowledge graph. [Institute of Acupuncture and Moxibustion, China Academy of Chinese Medical Sciences] [[Homepage](http://www.acuworld.ac.cn/info_content.jsp?id=1583)]
- **Luqi Huang** President and researcher of the China Academy of Chinese Medical Sciences. Works on molecular pharmacognosy and molecular identification of Chinese medicines. [China Academy of Chinese Medical Sciences] [[Homepage](https://www.nrc.ac.cn/rcyjy/rcdw/yjy/eb9d33d888a14d189c75d46fc19ced5b.htm)]
- **Yuan Yuan** Chief researcher and doctoral supervisor at the China Academy of Chinese Medical Sciences. Works on identification of Chinese medicines and molecular pharmacognosy. [China Academy of Chinese Medical Sciences] [[Homepage](https://www.nrc.ac.cn/rcyjy/rcdw/yjy/6c76223ab0574c35a0e8e0e35ab67249.htm)]

</details>

<details>
<summary>Tsinghua University (5)</summary>

- **Shao Li** Professor and doctoral supervisor at Tsinghua University, and director of the Beijing Institute for TCM Interdisciplinary Research. Works on network pharmacology and AI for TCM, including cancer and other complex diseases, and recruits postdocs and professional doctoral students. [Department of Automation, Tsinghua University, Beijing Institute for TCM Interdisciplinary Research, Tsinghua University] [[Homepage](https://www.tcm-x.tsinghua.edu.cn/info/1512/2662.htm)] [[Admissions](https://www.tcm-x.tsinghua.edu.cn/zszp.htm)]
- **Maosong Sun** Professor and doctoral supervisor in the Department of Computer Science and Technology at Tsinghua University, and executive vice dean of the Institute for Artificial Intelligence. Works on natural language processing and large models; his group collaborates with Gushengtang on TCM models. [Department of Computer Science and Technology, Tsinghua University, Institute for Artificial Intelligence, Tsinghua University] [[Homepage](https://nlp.csai.tsinghua.edu.cn/staff/sms/)] [[News](https://www.gstzy.cn/news/detail/10/14076.html)]
- **Peng Zhang** Associate researcher in the Department of Automation, Tsinghua University, and deputy director of the Beijing Institute for TCM Interdisciplinary Research. Co-developed the digestive TCM model GastroTCM. [Department of Automation, Tsinghua University, Beijing Institute for TCM Interdisciplinary Research, Tsinghua University] [[Homepage](https://www.tcm-x.tsinghua.edu.cn/kydw.htm)]
- **Guoan Luo** Professor of chemistry at Tsinghua University. Proposed system-to-system research for Chinese medicine and works on chromatographic fingerprints. [Department of Chemistry, Tsinghua University] [[Homepage](https://www.chem.tsinghua.edu.cn/info/1089/1941.htm)]
- **Qionglin Liang** Tenured professor and doctoral supervisor at Tsinghua University. Works on Chinese-medicine modernization, mass-spectrometry multi-omics, and organ-chip analysis. [Department of Chemistry, Tsinghua University] [[Homepage](https://www.chem.tsinghua.edu.cn/info/1095/2735.htm)]

</details>

<details>
<summary>University of Science and Technology Beijing (3)</summary>

- **Dezheng Zhang** Professor and doctoral supervisor at the University of Science and Technology Beijing. Works on TCM knowledge graphs and assisted diagnosis; his group released the Zhang Zhongjing TCM model and he is a distinguished professor at Henan University of Chinese Medicine. [School of Computer and Communication Engineering, University of Science and Technology Beijing] [[Homepage](https://faculty.ustb.edu.cn/DezhengZhang/zh_CN/index.htm)] [[News](https://news.ustb.edu.cn/info/1087/67760.htm)]
- **Aziguli Wulamu** Professor and doctoral supervisor in the School of Computer and Communication Engineering, University of Science and Technology Beijing. Works on multimodal inspection, TCM clinical decision support, and TCM language models. [School of Computer and Communication Engineering, University of Science and Technology Beijing] [[Homepage](https://it.xju.edu.cn/info/1327/2835.htm)] [[News](https://news.ustb.edu.cn/info/1981/67772.htm)]
- **Yonghong Xie** Associate professor and master's supervisor at the University of Science and Technology Beijing. Co-developed the Zhang Zhongjing TCM model and TCM knowledge graphs. [School of Computer and Communication Engineering, University of Science and Technology Beijing] [[Homepage](https://faculty.ustb.edu.cn/YonghongXie/zh_CN/index.htm)]

</details>

<details>
<summary>China Academy of Chinese Medical Sciences (2)</summary>

- **Yongzhong Cheng** Chief physician and doctoral supervisor at Wangjing Hospital. Leads an intelligent bone-setting surgical robot for TCM orthopedics. [Wangjing Hospital, China Academy of Chinese Medical Sciences] [[News](https://zyj.beijing.gov.cn/sy/rdzt/bjyyjkxtzyygzlyfgc/202501/P020250124625181340715.pdf)]
- **Minshan Feng** Chief physician and doctoral supervisor at Wangjing Hospital. Presented a vertical model of master-physician experience for cervical spondylosis. [Wangjing Hospital, China Academy of Chinese Medical Sciences] [[Admissions](https://yanjiusheng.bucm.edu.cn/docs/2024-12/c2448d698eca42848387882e725da184.pdf)]

</details>

<details>
<summary>China Academy of Chinese Medical Sciences (2)</summary>

- **Hao Xu** Chief researcher of the China Academy of Chinese Medical Sciences and vice president of Xiyuan Hospital. Uses deep networks for master-physician knowledge bases and assisted care. [Xiyuan Hospital, China Academy of Chinese Medical Sciences] [[News](https://xyhospital.com/Html/News/Articles/21500.html)]
- **Bo Pang** Vice president and doctoral supervisor at Xiyuan Hospital. Oversees information systems and the hospital's digital-twin consultation room. [Xiyuan Hospital, China Academy of Chinese Medical Sciences] [[Homepage](https://www.xyhospital.com/Html/News/Articles/22270.html)]

</details>

<details>
<summary>China-Japan Friendship Hospital (2)</summary>

- **Shiyu Du** Director of gastroenterology and doctoral supervisor at China-Japan Friendship Hospital. Corresponding author of the spleen-stomach model GastroTCM. [China-Japan Friendship Hospital] [[Homepage](https://www.zryhyy.com.cn/zryh/c100442/zjxx.shtml)]
- **Xianbo Zuo** Director of big-data research at China-Japan Friendship Hospital. Works on the hospital's trusted data space and disease-specific models. [China-Japan Friendship Hospital] [[Homepage](https://www.zryhyy.com.cn/zryh/c105700/zjxx.shtml)]

</details>

<details>
<summary>Beijing University of Chinese Medicine (2)</summary>

- **Changyong Luo** Master’s supervisor at Dongfang Hospital, Beijing University of Chinese Medicine. Works on TCM AI for epidemic and chronic disease and led the Tianyi TCM model. [Dongfang Hospital, Beijing University of Chinese Medicine] [[Homepage](https://www.dongfangyy.com.cn/Html/News/Articles/13293.html)] [[Paper](https://doi.org/10.1016/j.inffus.2025.103663)]
- **Hongcai Shang** President of Dongfang Hospital, Beijing University of Chinese Medicine, and a doctoral supervisor. Works on intelligent inspection and TCM clinical decision support. [Dongfang Hospital, Beijing University of Chinese Medicine] [[Homepage](https://dongfangyy.com.cn/Html/News/Articles/12504.html)]

</details>

<details>
<summary>Peking University (2)</summary>

- **Pengfei Tu** Professor and doctoral supervisor at Peking University and director of its modern Chinese-medicine research center. Identifies herb targets and chemical isomers with quantum-chemical calculation. [School of Pharmaceutical Sciences, Peking University] [[Homepage](https://dnm.bjmu.edu.cn/szdw_20180110150803713087/trywhxyjs_20180110150803713087/192678.htm)]
- **Kewu Zeng** Researcher and doctoral supervisor at Peking University. Uses proteomics to identify direct targets of Chinese-medicine constituents. [School of Pharmaceutical Sciences, Peking University] [[Homepage](https://dnm.bjmu.edu.cn/szdw_20180110150803713087/trywhxyjs_20180110150803713087/192684.htm)]

</details>

<details>
<summary>Beijing University of Technology (2)</summary>

- **Xinfeng Zhang** Associate professor and master's supervisor at Beijing University of Technology. Works on tongue-image segmentation, multi-label classification, and multimodal tongue perception. [Faculty of Information Technology, Beijing University of Technology] [[Homepage](https://sist.bjut.edu.cn/info/1517/4319_2.htm)]
- **Yiheng Cai** Professor and doctoral supervisor at Beijing University of Technology. Works on full-dimension tongue capture, color standardization for inspection, and intelligent tongue-diagnosis systems. [Faculty of Information Technology, Beijing University of Technology] [[Homepage](https://sist.bjut.edu.cn/info/1426/2320.htm)]

</details>

<details>
<summary>National Center for Protein Sciences (Beijing) (2)</summary>

- **Zhongyang Liu** Associate researcher and master's supervisor at the National Center for Protein Sciences in Beijing. Uses artificial intelligence and knowledge graphs for drug discovery and is a co-corresponding author of BATMAN-TCM 2.0. [National Center for Protein Sciences (Beijing)] [[Homepage](https://i-share.ncpsb.org.cn/genee/post/176)]
- **Dong Li** Researcher and doctoral supervisor at the National Center for Protein Sciences in Beijing. Mines life-omics data and is a co-corresponding author of BATMAN-TCM 2.0. [National Center for Protein Sciences (Beijing)] [[Homepage](http://i-share.ncpsb.org.cn/genee/post/172)]

</details>

<details>
<summary>China Academy of Chinese Medical Sciences (1)</summary>

- **Zhen Liu** Party secretary of Guang'anmen Hospital. Leads work on four-diagnosis and syndrome-differentiation models and the release of Guangyi Qizhi. [Guang'anmen Hospital, China Academy of Chinese Medical Sciences] [[News](https://www.gamyy.cn/gzb/news/big/115621.html)]

</details>

<details>
<summary>Chinese Academy of Sciences (1)</summary>

- **Yang Wu** Associate researcher and project lead at the Institute of Computing Technology. Builds Chinese-medicine data platforms including HERB, SymMap, and POINT. [Institute of Computing Technology, Chinese Academy of Sciences] [[Homepage](https://www.ict.ac.cn/sourcedb/cn/jssrck/202211/t20221101_6543064.html)]

</details>

<details>
<summary>Zhongke Wenge (1)</summary>

- **Lei Wang** Researcher at the Institute of Automation, Chinese Academy of Sciences, and chairman of Zhongke Wenge. Co-developed the TCM model Dayi Jinkui with the China Academy of Chinese Medical Sciences. [Zhongke Wenge, Institute of Automation, Chinese Academy of Sciences] [[News](https://news.sciencenet.cn/htmlnews/2025/5/544108.shtm)] [[Website](https://tcm.wenge.com/)]

</details>

<details>
<summary>Transn (1)</summary>

- **Enpei He** Founder, chairman, and CEO of Transn. The company released the Rendu model and the Chuanshen Suwen TCM model. [Transn] [[Homepage](https://www.transn.com/mobile/about_us/intro)]

</details>

<details>
<summary>Beijing University of Chinese Medicine (1)</summary>

- **Chunling Liu** Director of digital and smart-hospital development at Dongzhimen Hospital. Leads the hospital's digital integration work. [Dongzhimen Hospital, Beijing University of Chinese Medicine] [[News](https://yxb.dzmyy.com.cn/Html/News/Articles/18348.html)]

</details>

<details>
<summary>Beijing Jiaotong University (1)</summary>

- **Xuezhong Zhou** Professor, doctoral supervisor, and chair of the Department of Artificial Intelligence at Beijing Jiaotong University. Works on TCM knowledge graphs, large language models, and clinical AI; the group released Lingdan and Lingdan-V2. [School of Computer Science and Technology, Beijing Jiaotong University] [[Homepage](https://faculty.bjtu.edu.cn/8029/)] [[Paper](https://arxiv.org/abs/2610.14705)] [[Code](https://github.com/TCMAI-BJTU/Lingdan-V2)]

</details>

<details>
<summary>CapitalBio Jingfang (1)</summary>

- **Yue Yang** Chair of CapitalBio Jingfang. Leads the Molecular Herbalism model and uses pathway data to screen Chinese formulas and evaluate activity. [CapitalBio Jingfang] [[News](http://www.zj.chinanews.com.cn/jzkzj/2025-12-24/detail-iheyfaae0556576.shtml)]

</details>

<details>
<summary>Beijing Tongrentang Research Institute (1)</summary>

- **Zhibin Wang** President of the Beijing Tongrentang Research Institute. Works on bioactivity assays and quality control of Chinese medicines. [Beijing Tongrentang Research Institute] [[Homepage](https://zhongyao.bucm.edu.cn/szdw/sssds/zyylx_20220622164850036668/75851.htm)]

</details>

<details>
<summary>Beihang University (1)</summary>

- **Zeming Liu** Associate professor in the School of Computer Science, Beihang University. Leads key technologies for professional TCM language models. [School of Computer Science, Beihang University] [[Homepage](https://teacher.buaa.edu.cn/liuzeming/zh_CN/kyxm/206021/content/6796.htm)]

</details>

<details>
<summary>Beijing University of Posts and Telecommunications (1)</summary>

- **Guangyu Wang** Researcher at Beijing University of Posts and Telecommunications. Corresponding author of TCM-GPT, a domain-adaptive TCM pretraining model. [Beijing University of Posts and Telecommunications] [[News](https://news.qq.com/rain/a/20250110A03RJT00)]

</details>

<details>
<summary>CapitalBio (1)</summary>

- **Jing Cheng** Chair and president of CapitalBio. Builds the Molecular Herbalism Chinese-medicine model and digitized tongue diagnosis. [CapitalBio] [[Homepage](https://www.capitalbio.com/about/45.html)]

</details>

<details>
<summary>Chinese PLA General Hospital (1)</summary>

- **Xiaohe Xiao** Joint doctoral supervisor at the Chinese PLA General Hospital. The listed direction is mechanisms of Chinese medicines based on precision network pharmacology. [Chinese PLA General Hospital] [[Admissions](https://yanjiusheng.bucm.edu.cn/docs/2026-01/f524a5d2c485489ab2be485be376a2b3.pdf)]

</details>

<details>
<summary>Capital Medical University (1)</summary>

- **Baoli Liu** Executive vice president and doctoral supervisor at Beijing Hospital of Traditional Chinese Medicine. Corresponding author of the diarrhea model Qwen-TCM-Dia. [Beijing Hospital of Traditional Chinese Medicine, Capital Medical University] [[Homepage](https://www.bjzhongyi.com/gzb_team_detail/13893.html)]

</details>

<details>
<summary>Capital Normal University (1)</summary>

- **Bowen Hao** Associate professor in the School of Management, Capital Normal University. His group released ZhiFangDanTai, a graph-retrieval model for TCM formulas. [School of Management, Capital Normal University] [[Homepage](https://glxy.cnu.edu.cn/szdw/zrjs/ggsyglzy_05f39083c56d46acbb48d86628e8cc70/index.htm)] [[Paper](https://arxiv.org/abs/2509.05867)]

</details>


</details>

<details>
<summary>Tianjin (28)</summary>

<details>
<summary>Tianjin University of Traditional Chinese Medicine (13)</summary>

- **Junhua Zhang** Professor and doctoral supervisor at Tianjin University of Traditional Chinese Medicine, and executive deputy director of the Haihe Laboratory of Modern Chinese Medicine. Works on evidence-based TCM and released the evidence-review agent AireviewAgent. [Institute of Traditional Chinese Medicine, Tianjin University of Traditional Chinese Medicine, Haihe Laboratory of Modern Chinese Medicine] [[Homepage](https://institute.tjutcm.edu.cn/info/1049/2127.htm)] [[News](https://www.tjutcm.edu.cn/info/1047/1971.htm)]
- **Zhaopeng Meng** Professor and doctoral supervisor at Tianjin University, and former vice president of Tianjin University of Traditional Chinese Medicine. Works on AI for TCM, including TCM language models, question answering, and four-diagnosis devices. [Tianjin University, Tianjin University of Traditional Chinese Medicine] [[Homepage](https://kjc.gyu.edu.cn/info/1008/2020.htm)] [[News](https://yuyanwenhua.tjutcm.edu.cn/info/1036/1916.htm)]
- **Peng Zhou** Associate professor and doctoral supervisor at Tianjin University. Builds intelligent TCM diagnostic devices and TCM big-data systems, and founded Yimai AI. [Tianjin University, Tianjin University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.tjutcm.edu.cn/info/1105/1456.htm)]
- **Pengwei Zhuang** Faculty member at Tianjin University of Traditional Chinese Medicine. Works on knowledge-graph enhancement for the Haihe Qibo formula model. [Tianjin University of Traditional Chinese Medicine] [[Paper](http://fcst.ceaj.org/CN/10.3778/j.issn.1673-9418.2407082)]
- **Zhifeng Yu** Professor, doctoral supervisor, and director of Chinese diagnostics at Tianjin University of Traditional Chinese Medicine. Uses tongue-capture systems to analyze tongue color, shape, and body in insomnia. [School of Traditional Chinese Medicine, Tianjin University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.tjutcm.edu.cn/info/1106/1262.htm)]
- **Yimin Wang** Professor of Chinese-medicine engineering and doctoral and master's supervisor at Tianjin University of Traditional Chinese Medicine. Uses image capture for standardized tongue diagnosis. [Tianjin University of Traditional Chinese Medicine] [[Homepage](https://institute.tjutcm.edu.cn/info/1049/2124.htm)]
- **Xiaozuo Lu** Professor and doctoral supervisor at Tianjin University of Traditional Chinese Medicine. Studies how pulse graphs form and builds Chinese diagnostic instruments. [Tianjin University of Traditional Chinese Medicine] [[Homepage](http://www.tjlnrdx.cn/system/2019/08/22/012340534.shtml)]
- **Zheng Li** Dean and professor at Tianjin University of Traditional Chinese Medicine. Works on digital twins for Chinese-medicine manufacturing, machine vision in drying, and green intelligent pharmaceutics. [College of Pharmaceutical Engineering of Traditional Chinese Medicine, Tianjin University of Traditional Chinese Medicine] [[Homepage](https://zygc.tjutcm.edu.cn/info/1276/2593.htm)]
- **Wenlong Li** Doctoral supervisor at Tianjin University of Traditional Chinese Medicine. Uses near-infrared process analysis across decoction, alcohol precipitation, chromatography, and formulation units. [College of Pharmaceutical Engineering of Traditional Chinese Medicine, Tianjin University of Traditional Chinese Medicine] [[Homepage](https://zygc.tjutcm.edu.cn/info/1107/2597.htm)]
- **Yang Yu** Assistant researcher at Tianjin University of Traditional Chinese Medicine. Co-supervises machine-vision modeling and digital twins for drying processes. [College of Pharmaceutical Engineering of Traditional Chinese Medicine, Tianjin University of Traditional Chinese Medicine] [[Homepage](https://zygc.tjutcm.edu.cn/info/1276/2593.htm)]
- **Xingfang Pan** Professor at Tianjin University of Traditional Chinese Medicine. Leads a national key R&D project on acupuncture robot technology and systems. [Tianjin University of Traditional Chinese Medicine] [[Homepage](https://www.tjutcm.edu.cn/info/1039/1393.htm)]
- **Haiyan Ren** Faculty member and master's project supervisor at Tianjin University of Traditional Chinese Medicine. Works on intelligent Chinese medicine, computational acupuncture, and robot capture of needling techniques. [School of Traditional Chinese Medicine, Tianjin University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.tjutcm.edu.cn/info/1105/1243.htm)]
- **Xiumei Gao** President and professor of Tianjin University of Traditional Chinese Medicine. Studies multi-component, multi-target formula compatibility. [Tianjin University of Traditional Chinese Medicine] [[Homepage](https://institute.tjutcm.edu.cn/szdw/gxmjs.htm)]

</details>

<details>
<summary>Tasly (6)</summary>

- **Wenjia Wang** Leads Tasly’s Shuzhi Bencao TCM model and contributes to Lingdan-V2. [Tasly] [[News](https://www.taslypharma.com/tsl/41063.jhtml)] [[Paper](https://arxiv.org/abs/2610.14705)]
- **Kaijing Yan** Chairman of Tasly Pharmaceutical Group. Released the Shuzhi Bencao language model and the digital-Chinese-medicine program. [Tasly] [[News](http://www.news.cn/20240509/a76f15aae0544defad943093214cd38b/c.html)]
- **Shuiping Zhou** Executive dean of the Tasly Research Institute. Uses Shuzhi Bencao to generate new formulas and screen natural products. [Tasly] [[News](https://www.yicai.com/news/102185086.html)]
- **Jing Su** General manager of Tasly Digital Chinese Medicine. Builds TCM agents and clinical decision support from Shuzhi Bencao. [Tasly] [[News](http://tjtfea.com/News/202603/2026030514254819.htm)]
- **Haoshu Xiong** Advanced-manufacturing technology manager at Tasly. Works on Chinese-medicine process detection, quality digitization, and intelligent production lines. [Tasly] [[News](http://www.banyuetan.org/ppgs/detail/20190508/1000200033137571557301637982839273_1.html)]
- **Shunnan Zhang** Vice general manager of Tasly Pharmaceutical Group. Leads its digital Chinese-medicine and intelligent-manufacturing system. [Tasly] [[News](https://www.vbdata.cn/1518965213)]

</details>

<details>
<summary>Tianjin University (3)</summary>

- **Xin Wang** Professor and doctoral supervisor in the College of Intelligence and Computing, Tianjin University. Works on knowledge graphs and large models, and co-developed the TCM model Qibo with Tianjin University of Traditional Chinese Medicine. [College of Intelligence and Computing, Tianjin University] [[Homepage](https://cic.tju.edu.cn/info/1114/2744.htm)] [[Group](http://www.tjudb.cn/dbgroup/Xin_Wang_zh)] [[Paper](https://doi.org/10.1016/j.eswa.2025.127672)]
- **Yu Wang** Professor and doctoral supervisor in the College of Intelligence and Computing, Tianjin University. Co-developed the proactive TCM consultation system DoPI. [College of Intelligence and Computing, Tianjin University] [[Homepage](https://faculty.tju.edu.cn/wangyu_ai/zh_CN/index.htm)]
- **Xuemin Wang** Associate professor at Tianjin University and director of its Chinese-medicine engineering laboratory. Builds pulse collectors and combined inspection, listening, inquiry, and palpation systems. [School of Precision Instruments and Optoelectronics Engineering, Tianjin University] [[News](https://news.tju.edu.cn/info/1012/345719.htm)]

</details>

<details>
<summary>National Supercomputing Center in Tianjin (2)</summary>

- **Xiangfei Meng** Chief scientist at the National Supercomputing Center in Tianjin. Advances the Tianhe TCM model and hospital collaborations. [National Supercomputing Center in Tianjin] [[News](https://www.nscc-tj.cn/xwxq.php?id=626)]
- **Hao Fu** Head of data intelligence at the National Supercomputing Center in Tianjin. Presented Tianhe Lingshu 2.0 for TCM reasoning across specialties. [National Supercomputing Center in Tianjin] [[News](https://epaper.tianjinwe.com/tjrb/h5/html5/2025-08/28/content_143090_2563267.htm)]

</details>

<details>
<summary>Tianda Zhitu (2)</summary>

- **Yongzhe Jia** Founder and general manager of Tianda Zhitu. Leads industrial deployment of the Haihe Qibo TCM model. [Tianda Zhitu] [[News](https://epaper.tianjinwe.com/tjrb/h5/html5/2024-05/27/content_143078_848091.htm)]
- **Dawei Xu** Technical director of Tianda Zhitu. Works on Haihe Qibo and knowledge-enhanced formula models. [Tianda Zhitu] [[News](https://www.tjnk.gov.cn/NKQZF/XXDT856/nkyw/202401/t20240107_6501701.html)]

</details>

<details>
<summary>Yimai Artificial Intelligence Medical Technology (Tianjin) (1)</summary>

- **Peng Zhou** Chair of Yimai Artificial Intelligence Medical Technology in Tianjin. Builds tongue, pulse, and other four-examination devices. [Yimai Artificial Intelligence Medical Technology (Tianjin)] [[Homepage](https://www.tianzhongyimai.com/NewsStd_739.html)]

</details>

<details>
<summary>Nankai University (1)</summary>

- **Gang Bai** Professor and doctoral supervisor at Nankai University. Uses systems biology and network regulation to parse Chinese formulas. [College of Pharmacy, Nankai University] [[Homepage](https://pharmacy.nankai.edu.cn/info/1011/1293.htm)]

</details>


</details>

<details>
<summary>Hebei (5)</summary>

<details>
<summary>Hebei University of Chinese Medicine (2)</summary>

- **Shaoxian Wang** Shijiazhuang. Professor and doctoral supervisor at Hebei University of Chinese Medicine. The listed direction is syndrome foundations and digital-intelligent Chinese diagnosis. [Hebei University of Chinese Medicine] [[Homepage](http://static.hhkaobo.com/upload/editor/ba712818-4047-4a3c-a62d-eb12188f7339.pdf)]
- **Chaoyi Fang** Shijiazhuang. Professor and doctoral supervisor at Hebei University of Chinese Medicine. His team built a four-examination device and trains AI diagnostic models. [Hebei University of Chinese Medicine] [[Homepage](http://static.hhkaobo.com/upload/editor/ba712818-4047-4a3c-a62d-eb12188f7339.pdf)]

</details>

<details>
<summary>Hebei North University (1)</summary>

- **Xuming Tong** First author of the TCM models XuanHuGPT and QingNangTCM at Hebei North University. [Hebei North University] [[Paper](https://link.springer.com/article/10.1186/s13020-025-01200-3)]

</details>

<details>
<summary>Hebei University (1)</summary>

- **Hanqing Zhao** Baoding. Master's supervisor and director of the Chinese-medicine informatics laboratory at Hebei University. Works on objective tongue and pulse diagnosis, Chinese-medicine models, and knowledge graphs. [Hebei University] [[Homepage](https://zyxy.hbu.edu.cn/info/1037/2368.htm)]

</details>

<details>
<summary>Hebei Provincial Hospital of Traditional Chinese Medicine (1)</summary>

- **Yanru Du** Vice president and doctoral supervisor at Hebei Provincial Hospital of Traditional Chinese Medicine. Works on the Li Diangui prescription model and the spleen-stomach model Dongyuan. [Hebei Provincial Hospital of Traditional Chinese Medicine] [[Homepage](https://www.hbszyy.cn/html/product/2013-5-28/273.html)]

</details>


</details>

<details>
<summary>Shanxi (4)</summary>

<details>
<summary>Shanxi University of Chinese Medicine (3)</summary>

- **Jihong Yang** Taiyuan. Professor and doctoral supervisor at Shanxi University of Chinese Medicine. Digitizes classical texts and builds machine-learning syndrome models. [Shanxi University of Chinese Medicine] [[Homepage](https://yjsb.sxtcm.edu.cn/info/1708/4743.htm)]
- **Chenhui Du** Taiyuan. Professor and doctoral supervisor at Shanxi University of Chinese Medicine. Uses metabolomics and network pharmacology to study the active substances of Shanxi medicines. [Shanxi University of Chinese Medicine] [[Homepage](https://yjsb.sxtcm.edu.cn/info/1708/4736.htm)]
- **Xuemei Qin** Taiyuan. Professor and doctoral supervisor at Shanxi University of Chinese Medicine. Uses metabolomics, chemometrics, and network pharmacology to evaluate Chinese-medicine quality. [Shanxi University of Chinese Medicine] [[Homepage](https://yjsb.sxtcm.edu.cn/info/1708/4741.htm)]

</details>

<details>
<summary>North University of China (1)</summary>

- **Zhidong Zhang** Taiyuan. Professor and doctoral supervisor at North University of China, and master's supervisor at Shanxi University of Chinese Medicine. Builds digital Chinese-medicine sensors, a four-examination device, and an intelligent moxibustion robot. [North University of China] [[Homepage](https://6y.nuc.edu.cn/info/1025/28296.htm)]

</details>


</details>

<details>
<summary>Inner Mongolia (8)</summary>

<details>
<summary>Inner Mongolia University (3)</summary>

- **Feilong** Professor and doctoral supervisor at Inner Mongolia University. Leads the Mongolian-medicine knowledge base, clinical assistance, and language model. [Inner Mongolia University] [[Homepage](https://ccs.imu.edu.cn/info/1034/2019.htm)]
- **Guanglai Gao** Hohhot. Doctoral supervisor at Inner Mongolia University. Works on artificial intelligence and Mongolian-language processing, and is an inventor on a knowledge-graph Mongolian-medicine language model. [College of Computer Science, Inner Mongolia University] [[Homepage](https://ccs.imu.edu.cn/info/1034/2028.htm)]
- **Hui Zhang** Hohhot. Master's supervisor at Inner Mongolia University. Works on Mongolian speech and text recognition and joined a Mongolian-medicine language model. [College of Computer Science, Inner Mongolia University] [[Homepage](https://ccs.imu.edu.cn/info/1021/1888.htm)]

</details>

<details>
<summary>Inner Mongolia Minzu University (2)</summary>

- **Chunsheng Zhang** Tongliao. Master's supervisor at Inner Mongolia Minzu University. Leads data mining of Mongolian formulas with association rules, decision trees, and clustering. [Inner Mongolia Minzu University] [[Homepage](http://school.freekaoyan.com/neimenggu/imun/daoshi/2021/06-24/16245408291512706.shtml)]
- **Suyalatu Zhang** Tongliao. Master's supervisor at Inner Mongolia Minzu University. Uses laser-induced breakdown spectroscopy with machine learning and deep networks to distinguish Mongolian medicinal materials. [Inner Mongolia Minzu University] [[Homepage](http://school.freekaoyan.com/neimenggu/imun/daoshi/2021/06-24/16245398151512483.shtml)]

</details>

<details>
<summary>Inner Mongolia Medical University (1)</summary>

- **Bao Hashen** Hohhot. Doctoral and master's supervisor at Inner Mongolia Medical University. Built databases of classical Mongolian medical literature, formulas, and clinical cases. [Institute of Mongolian Medicine, Inner Mongolia Medical University] [[Homepage](https://www.ais.cn/mentor/mentorDetail/3f3173ff-5e3c-11ec-b045-a85e45a23623)]

</details>

<details>
<summary>Inner Mongolia Institute of Chinese and Mongolian Medicine (1)</summary>

- **Minhui Li** Hohhot. Doctoral and master's supervisor at the Inner Mongolia Institute of Chinese and Mongolian Medicine. Uses remote sensing to plan cultivation of Mongolian and Chinese medicinal plants. [Inner Mongolia Institute of Chinese and Mongolian Medicine] [[Homepage](https://www.kczg.org.cn/xuezhe/details?id=214141)]

</details>

<details>
<summary>Baotou Medical College (1)</summary>

- **Agula** Baotou. Doctoral supervisor at Baotou Medical College. Gave a public lecture on artificial intelligence in Chinese and Mongolian medicine. [Baotou Medical College] [[Homepage](https://www.btmc.edu.cn/info/1003/10449.htm)]

</details>


</details>

<details>
<summary>Liaoning (8)</summary>

<details>
<summary>Liaoning University of Traditional Chinese Medicine (3)</summary>

- **Jinhong Leng** Doctoral supervisor in the First Clinical College, Liaoning University of Traditional Chinese Medicine. Recruits students in TCM artificial intelligence. [First Clinical College, Liaoning University of Traditional Chinese Medicine] [[Admissions](https://gjhzjlc.lnutcm.edu.cn/liaoningzhongyiyaodaxue2026nianshenqing-kaoheboshiyanjiushengzhaoshengzhuanyemuluzhuanyexuewei.pdf)]
- **Xiangxuan Zhao** Doctoral supervisor in the School of Basic Medical Sciences, Liaoning University of Traditional Chinese Medicine. Works on TCM artificial intelligence. [School of Basic Medical Sciences, Liaoning University of Traditional Chinese Medicine] [[Admissions](https://gjhzjlc.lnutcm.edu.cn/liaoningzhongyiyaodaxue2026nianshenqing-kaohejishuobolianduboshiyanjiushengzhaoshengzhuanyemuluxueshuxuewei.pdf)]
- **Tie Qiao** Associate professor, master's supervisor, and lead of the TCM AI discipline at Liaoning University of Traditional Chinese Medicine. Works on standardized tongue-image capture and algorithm evaluation. [Liaoning University of Traditional Chinese Medicine] [[Homepage](https://www.lnutcm.edu.cn/info/2231/55271.htm)]

</details>

<details>
<summary>Northeastern University (1)</summary>

- **Wenjun Qin** Professor and doctoral supervisor at Northeastern University. Leads an acupuncture-robot project and a needling-technique database with a human acupoint knowledge graph. [College of Computer Science and Engineering, Northeastern University] [[Homepage](https://faculty.neu.edu.cn/tanwenjun/zh_CN/index.htm)]

</details>

<details>
<summary>Chinese Academy of Sciences (1)</summary>

- **Xinmiao Liang** Researcher and doctoral supervisor at the Dalian Institute of Chemical Physics. Proposed the herbal materials-ome and built a library of standard Chinese-medicine components. [Dalian Institute of Chemical Physics, Chinese Academy of Sciences] [[Homepage](https://mccm.dicp.ac.cn/info/1106/1204.htm)]

</details>

<details>
<summary>Shenyang Pharmaceutical University (1)</summary>

- **Yongxue Guo** Professor, vice dean, and master's supervisor at Shenyang Pharmaceutical University. Works on process analytical technology and new Chinese-medicine manufacturing methods. [School of Pharmaceutical Engineering, Shenyang Pharmaceutical University] [[Homepage](https://grs.syphu.edu.cn/info/1103/7177.htm)]

</details>

<details>
<summary>Affiliated Hospital of Liaoning University of Traditional Chinese Medicine (1)</summary>

- **Zhe Zhang** Deputy director of the Chinese-medicine innovation center at the Affiliated Hospital of Liaoning University of Traditional Chinese Medicine. Connects a tongue-diagnosis app and upgrades tongue-diagnosis products. [Affiliated Hospital of Liaoning University of Traditional Chinese Medicine] [[Homepage](https://www.lnutcm.edu.cn/info/1031/44221.htm)]

</details>

<details>
<summary>Second Affiliated Hospital of Liaoning University of Traditional Chinese Medicine (1)</summary>

- **Guoxin Li** Shenyang. Doctoral supervisor at the Second Affiliated Hospital of Liaoning University of Traditional Chinese Medicine. The listed direction includes integrative clinical medicine and artificial intelligence. [Second Affiliated Hospital of Liaoning University of Traditional Chinese Medicine] [[Homepage](https://www.lnpatcm.com/product/170.html)]

</details>


</details>

<details>
<summary>Jilin (4)</summary>

<details>
<summary>Changchun University of Chinese Medicine (3)</summary>

- **Xiangyang Leng** President and professor at Changchun University of Chinese Medicine. Leads the AI-plus-TCM program and the co-release of Zhongxing Changbai Qihuang. [Changchun University of Chinese Medicine] [[News](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- **Rui Chen** Changchun. Professor and doctoral and master's supervisor at Changchun University of Chinese Medicine. Works on Chinese diagnostics and pulse studies. [School of Basic Medical Sciences, Changchun University of Chinese Medicine] [[Homepage](https://ccucm.teacher.360eol.com/teacherBasic/preview?teacherId=28019)]
- **Zifeng Pi** Changchun. Professor and doctoral and master's supervisor at Changchun University of Chinese Medicine. Uses network pharmacology in Chinese-medicine analysis. [School of Pharmacy, Changchun University of Chinese Medicine] [[Homepage](https://ccucm.teacher.360eol.com/teacherBasic/preview?teacherId=28131)]

</details>

<details>
<summary>Jilin Business and Technology College (1)</summary>

- **Jia Zhao** Vice president and professor at Jilin Business and Technology College. Led development of the multimodal TCM model Zhongxing Changbai Qihuang. [Jilin Business and Technology College] [[News](https://jl.chinadaily.com.cn/a/202512/21/WS6947b1c2a310942cc4997b6e.html)]

</details>


</details>

<details>
<summary>Heilongjiang (4)</summary>

<details>
<summary>Heilongjiang University of Chinese Medicine (4)</summary>

- **Chaosheng Yan** Professor, graduate supervisor, and dean of the School of Medical Information Engineering, Heilongjiang University of Chinese Medicine. Works on medical AI and knowledge graphs of TCM classics. [School of Medical Information Engineering, Heilongjiang University of Chinese Medicine] [[Homepage](https://rwyglxy.hljucm.net/info/1276/3122.htm)]
- **Xijun Wang** Professor and doctoral supervisor at Heilongjiang University of Chinese Medicine. Works on serum pharmacochemistry and formula-syndrome metabolomics. [Heilongjiang University of Chinese Medicine] [[Homepage](https://kjc.hljucm.net/info/1097/1129.htm)]
- **Hui Sun** Doctoral supervisor at Heilongjiang University of Chinese Medicine. Analyzes in-vivo constituents of Chinese medicines and their quality standards. [Heilongjiang University of Chinese Medicine] [[Homepage](https://yjsy.hljucm.net/info/1292/6818.htm)]
- **Xiuhong Wu** Second-class professor and doctoral supervisor at Heilongjiang University of Chinese Medicine. Studies quality markers and identification of Chinese medicines with formula-syndrome metabolomics. [Heilongjiang University of Chinese Medicine] [[Homepage](https://yjsy.hljucm.net/info/1292/6818.htm)]

</details>


</details>

<details>
<summary>Shanghai (45)</summary>

<details>
<summary>Shanghai University of Traditional Chinese Medicine (21)</summary>

- **Jie Li** Professor in the School of TCM Artificial Intelligence, Shanghai University of Traditional Chinese Medicine. Leads work on TCM models, multimodal agents, and digital Chinese-medicine R&D. [School of TCM Artificial Intelligence, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://aishutcm.shutcm.edu.cn/2026/0327/c7887a172347/page.htm)] [[Admissions](https://yjsy.shutcm.edu.cn/_upload/article/files/f9/d9/0c9d59b941d3b1bb03c93fc8aa1c/a33367af-8441-476a-9ca6-74e1abc59992.pdf)]
- **Xiaojuan Hu** Master’s supervisor in the School of TCM Artificial Intelligence, Shanghai University of Traditional Chinese Medicine. Works on intelligent TCM diagnosis and treatment. [School of TCM Artificial Intelligence, Shanghai University of Traditional Chinese Medicine] [[Admissions](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **Liping Tu** Master’s supervisor in the School of TCM Artificial Intelligence, Shanghai University of Traditional Chinese Medicine. Works on informatization and intelligent TCM diagnosis. [School of TCM Artificial Intelligence, Shanghai University of Traditional Chinese Medicine] [[Admissions](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **Jijia Sun** Master’s supervisor in the School of TCM Artificial Intelligence, Shanghai University of Traditional Chinese Medicine. Works on AI for computational drug discovery. [School of TCM Artificial Intelligence, Shanghai University of Traditional Chinese Medicine] [[Admissions](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **Shaoxiong Li** Master’s supervisor in the School of TCM Artificial Intelligence, Shanghai University of Traditional Chinese Medicine. Works on medical intelligent algorithms and hardware. [School of TCM Artificial Intelligence, Shanghai University of Traditional Chinese Medicine] [[Admissions](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **Guangyong Zheng** Master’s supervisor at the Institute of Interdisciplinary Science, Shanghai University of Traditional Chinese Medicine. Works on AI for Chinese-medicine pharmacology. [Institute of Interdisciplinary Science, Shanghai University of Traditional Chinese Medicine] [[Admissions](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **Dong Lu** Master’s supervisor at the Institute of Interdisciplinary Science, Shanghai University of Traditional Chinese Medicine. Works on AI and drug design for Chinese medicine. [Institute of Interdisciplinary Science, Shanghai University of Traditional Chinese Medicine] [[Admissions](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **Xiaoqing Guan** Master’s supervisor at the Institute of Interdisciplinary Science, Shanghai University of Traditional Chinese Medicine. Works on big data and AI for drug discovery. [Institute of Interdisciplinary Science, Shanghai University of Traditional Chinese Medicine] [[Admissions](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **Jiatuo Xu** Professor, doctoral supervisor, and director of the TCM Information Science and Technology Center, Shanghai University of Traditional Chinese Medicine. Leads intelligent tongue-diagnosis systems. [Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157325/page.htm)]
- **Yiqin Wang** Professor and doctoral supervisor at Shanghai University of Traditional Chinese Medicine. Works on objective tongue, pulse, face, and inquiry diagnosis. [Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157327/page.htm)]
- **Fufeng Li** Professor and doctoral supervisor at Shanghai University of Traditional Chinese Medicine. Works on standardized face-diagnosis images, feature recognition, and intelligent mirrors. [Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157323/page.htm)]
- **Haixia Yan** Professor and master's supervisor at Shanghai University of Traditional Chinese Medicine. Works on objective pulse diagnosis and pulse-wave risk models. [Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157316/page.htm)]
- **Yiming Hao** Researcher and master's supervisor at Shanghai University of Traditional Chinese Medicine. Works on objective four examinations for chronic disease and tongue-coating metabolomics. [School of Traditional Chinese Medicine, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157321/page.htm)]
- **Zhaoxia Xu** Researcher and doctoral supervisor at Shanghai University of Traditional Chinese Medicine. Analyzes tongue-image parameters and edited a monograph on tongue diagnosis. [School of Traditional Chinese Medicine, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157324/page.htm)]
- **Rui Guo** Researcher and master's supervisor at Shanghai University of Traditional Chinese Medicine. Works on objective pulse diagnosis and intelligent tongue-diagnosis devices. [School of Traditional Chinese Medicine, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157318/page.htm)]
- **Ji Cui** Associate professor and master's supervisor at Shanghai University of Traditional Chinese Medicine. Works on array-based three-dimensional pulse graphs and digitized four examinations. [School of Basic Medical Sciences, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157317/page.htm)]
- **Peng Qian** Senior experimentalist and master's supervisor at Shanghai University of Traditional Chinese Medicine. Builds automatically pressure-adjusted pulse collectors and objective four-examination methods. [Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157320/page.htm)]
- **Wenchao Tang** Professor at Shanghai University of Traditional Chinese Medicine. Builds optical-force sensing for manual acupuncture dose and leads evaluation of Chinese-medicine models. [College of Artificial Intelligence in Chinese Medicine, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zt.shutcm.edu.cn/2021/1019/c3352a137223/page.htm)]
- **Tangyi Liu** Associate professor and master's supervisor at Shanghai University of Traditional Chinese Medicine. Developed electroacupuncture devices for needling techniques, single-point resistance detection, and technique-simulation capture. [College of Acupuncture and Tuina, Shanghai University of Traditional Chinese Medicine] [[Homepage](http://school.freekaoyan.com/sh/shutcm/daoshi/2021/01-23/16113955791334845.shtml)]
- **Weidong Zhang** Professor and doctoral supervisor at Shanghai University of Traditional Chinese Medicine. Studies bioactive substances in Chinese formulas and uses artificial intelligence to parse formula mechanisms. [Institute of Interdisciplinary Integrative Medicine Research, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://iiimr.shutcm.edu.cn/2019/0426/c4069a174532/page.htm)]
- **Huayuan Yang** Shanghai. Professor at Shanghai University of Traditional Chinese Medicine. Uses artificial intelligence for a tuina robot that imitates one-finger meditation technique and locates lesions. [Shanghai University of Traditional Chinese Medicine] [[Homepage](https://www.shutcm.edu.cn/2023/0921/c751a155057/page.htm)]

</details>

<details>
<summary>Shanghai University of Traditional Chinese Medicine (5)</summary>

- **Xinlin Chen** President of Longhua Hospital, Shanghai University of Traditional Chinese Medicine. Leads a multimodal TCM diagnosis agent and the hospital digital program. [Longhua Hospital, Shanghai University of Traditional Chinese Medicine] [[News](https://www.shanghai.gov.cn/gwk/search/content/441f95ac30e7432fa24730c79128df5c)]
- **Ping Liu** Vice president, chief physician, and doctoral supervisor at Longhua Hospital. Leads a project on famous-doctor syndrome-differentiation models. [Longhua Hospital, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://www.longhua.net/info/2921/64701.htm)]
- **Liang Dong** Director of the information center at Longhua Hospital. Connects the famous-doctor thinking model with an information platform for chain-of-thought annotation. [Longhua Hospital, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://www.longhua.net/info/1021/87312.htm)]
- **Yuelai Chen** Then president of Longhua Hospital. Advanced AI pre-consultation from tongue, face, and pulse images and a clinical decision-support platform. [Longhua Hospital, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://www.longhua.net/info/1028/2519.htm)]
- **Liang Zhu** Vice president of Longhua Hospital. Represents the hospital in medical-model validation while the hospital builds a formula-syndrome model and four-examination pattern recognition. [Longhua Hospital, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://www.longhua.net/info/1021/76211.htm)]

</details>

<details>
<summary>East China University of Science and Technology (5)</summary>

- **Tong Ruan** Professor and doctoral supervisor at East China University of Science and Technology. Works on medical models and knowledge graphs, including a TCM graph for prescription support. [School of Information Science and Engineering, East China University of Science and Technology] [[Homepage](https://faculty.ecust.edu.cn/cise/rt/main.htm)]
- **Yun Tang** Professor and doctoral supervisor in the School of Pharmacy, East China University of Science and Technology. Works on AI drug design, network pharmacology, and the TCM consultation model MedChatZH. [School of Pharmacy, East China University of Science and Technology] [[Homepage](https://pharmacy.ecust.edu.cn/2008/1203/c2795a29378/page.htm)] [[Paper](https://pubmed.ncbi.nlm.nih.gov/38503097/)]
- **Jianjun Yan** Associate professor and master's supervisor at East China University of Science and Technology. Works on pulse devices, tongue-image segmentation, and TCM signal analysis. [East China University of Science and Technology] [[Homepage](https://mech.ecust.edu.cn/2019/0516/c11271a90164/page.htm)]
- **Huiqun Yu** Professor and doctoral supervisor at East China University of Science and Technology. Co-developed the TCM consultation model MedChatZH. [School of Computer Science and Engineering, East China University of Science and Technology] [[Homepage](https://cise.ecust.edu.cn/2026/0615/c16487a191279/page.htm)]
- **Guisheng Fan** Associate researcher and doctoral supervisor at East China University of Science and Technology. Co-developed the TCM consultation model MedChatZH. [School of Computer Science and Engineering, East China University of Science and Technology] [[Homepage](https://cise.ecust.edu.cn/_t250/2011/0615/c7766a55144/page.htm)]

</details>

<details>
<summary>Shanghai University of Traditional Chinese Medicine (2)</summary>

- **Weian Yuan** Vice president and doctoral supervisor at Shuguang Hospital. Leads a full-lifecycle clinical-trial platform and virtual trials. [Shuguang Hospital, Shanghai University of Traditional Chinese Medicine] [[Homepage](https://zyyyjy.gdpu.edu.cn/info/1082/1370.htm)]
- **Min Fang** Professor at Shanghai University of Traditional Chinese Medicine and director of the tuina institute at Shuguang Hospital. Leads a tuina bionic-hand robot, spinal assessment, acupoint-stimulation exoskeletons, and intelligent depression diagnosis. [Shuguang Hospital, Shanghai University of Traditional Chinese Medicine] [[News](http://www.thepaper.cn/newsDetail_forward_31847870)]

</details>

<details>
<summary>Shanghai University of Traditional Chinese Medicine (2)</summary>

- **Dan Hu** President of Shanghai Seventh People’s Hospital. The hospital released the Qiyuan TCM model with Shanghai University of Traditional Chinese Medicine and the Shanghai Artificial Intelligence Laboratory. [Shanghai Seventh People’s Hospital, Shanghai University of Traditional Chinese Medicine] [[News](http://sh.news.cn/20260719/ef7034ccc6394653825f97a21452738e/c.html)]
- **Yipeng Zeng** Master's supervisor at the Seventh People's Hospital of Shanghai University of Traditional Chinese Medicine. The listed direction includes pulse diagnosis and endocrine-metabolic disease. [Seventh People's Hospital, Shanghai University of Traditional Chinese Medicine] [[Admissions](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]

</details>

<details>
<summary>Chinese Academy of Sciences (2)</summary>

- **Dean Guo** Researcher at the Shanghai Institute of Materia Medica and director of the national engineering center for Chinese-medicine standardization. Works on analysis, quality standards, and a quality-testing database. [Shanghai Institute of Materia Medica, Chinese Academy of Sciences] [[Homepage](http://www.caim.org.cn/info_content_ds.jsp?id=10009)]
- **Kaixian Chen** Researcher and doctoral supervisor at the Shanghai Institute of Materia Medica. Works on computer-aided drug design, with Chinese materia medica among the admission directions. [Shanghai Institute of Materia Medica, Chinese Academy of Sciences] [[Homepage](https://people.ucas.ac.cn/~0009438)]

</details>

<details>
<summary>East China Normal University (2)</summary>

- **Honglin Li** Dean of the School of Pharmacy and doctoral supervisor at East China Normal University. Works on AI for drug design. The university and partners released the Shuzhi Qihuang TCM model. [School of Pharmacy, East China Normal University, Lingang Laboratory] [[Homepage](https://pharm.ecnu.edu.cn/46547/list.htm)] [[News](https://www.ecnu.edu.cn/info/1426/65503.htm)]
- **Xiaoling Wang** Professor in the School of Computer Science, East China Normal University. Leads key technologies for a TCM education model and co-developed ShenNong. [School of Computer Science and Technology, East China Normal University] [[Homepage](https://faculty.ecnu.edu.cn/_s16/wxl2/main.psp)] [[Code](https://github.com/michael-wzhu/ShenNong-TCM-LLM)]

</details>

<details>
<summary>Shanghai University of Traditional Chinese Medicine (1)</summary>

- **Shengyi Feng** Master’s supervisor at Yueyang Hospital of Integrated Traditional Chinese and Western Medicine. Works on AI for TCM orthopedics and rehabilitation. [Yueyang Hospital of Integrated Traditional Chinese and Western Medicine, Shanghai University of Traditional Chinese Medicine] [[Admissions](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]

</details>

<details>
<summary>Shanghai Jiao Tong University (1)</summary>

- **Lizhuang Ma** Chair professor and doctoral supervisor in the School of Computer Science, Shanghai Jiao Tong University. Works on intelligent diagnosis that joins Chinese and Western medical information, including complexion and syndrome recognition. [School of Computer Science, Shanghai Jiao Tong University] [[Homepage](https://cs.sjtu.edu.cn/jiaoshiml/malizhuang.html)]

</details>

<details>
<summary>Shanghai University of Engineering Science (1)</summary>

- **Chunming Xia** Professor and doctoral supervisor at Shanghai University of Engineering Science. Works on pulse-signal acquisition and objective four examinations. [Shanghai University of Engineering Science] [[Homepage](https://seee.sues.edu.cn/56/93/c23926a218771/page.htm)]

</details>

<details>
<summary>Shanghai Daosheng Medical Technology (1)</summary>

- **Chunqing Li** Chair of Shanghai Daosheng Medical Technology. Builds four-examination and pulse devices and leads standards for Chinese diagnostic equipment. [Shanghai Daosheng Medical Technology] [[Homepage](https://www.acfic.org.cn/ztzlhz/2022bzcxdh/2022bzcxdh_4/202209/t20220913_313004.html)]

</details>

<details>
<summary>Tongji University (1)</summary>

- **Haofen Wang** Researcher and doctoral supervisor at Tongji University. Works on knowledge graphs and dialogue systems, and supervises the Zhongjing TCM model. [Tongji University] [[Homepage](https://faculty.tongji.edu.cn/wanghaofen/zh_CN/index.htm)] [[Code](https://github.com/pariskang/CMLM-ZhongJing)]

</details>

<details>
<summary>Fudan University (1)</summary>

- **Wenqiang Zhang** Researcher and doctoral supervisor in the School of Computer Science, Fudan University. Supervises the Zhongjing GPT line and TCM diagnosis robots. [School of Computer Science, Fudan University] [[Homepage](https://iipl.fudan.edu.cn/70/e4/c45863a684260/page.htm)]

</details>


</details>

<details>
<summary>Jiangsu (21)</summary>

<details>
<summary>Nanjing University of Chinese Medicine (11)</summary>

- **Kongfa Hu** Vice president and doctoral supervisor at Nanjing University of Chinese Medicine, and dean of the provincial AI school. Works on TCM AI, knowledge graphs, and large models, including tongue diagnosis, syndrome differentiation, and a Jiangsu TCM vertical model. [School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine] [[Homepage](https://xxjs.njucm.edu.cn/2026/0424/c465a167934/pagem.htm)] [[News](http://xxjs.njucm.edu.cn/2025/0908/c467a160307/page.htm)]
- **Zuojian Zhou** Professor and doctoral supervisor at Nanjing University of Chinese Medicine, and lead of the TCM artificial-intelligence cross-discipline. Works on TCM AI, health IoT, and intelligent devices. [School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine] [[Homepage](https://xxjs.njucm.edu.cn/2018/0928/c465a43551/pagem.htm)]
- **Peng Cao** Researcher at Nanjing University of Chinese Medicine. His group co-developed the Tianyi TCM model with Gu Xiaohong and collaborators at Beijing University of Chinese Medicine. [Nanjing University of Chinese Medicine] [[News](https://www.njucm.edu.cn/2025/0910/c6754a160459/page.htm)] [[Paper](https://doi.org/10.1016/j.inffus.2025.103663)]
- **Feng Gao** Doctoral supervisor in the School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine. Works on machine learning and TCM AI. [School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine] [[Admissions](https://gra.njucm.edu.cn/_upload/article/files/8f/0a/bd6170cd44ad94f0d3108af24abe/aff48fcb-3589-4b90-a66d-c93ec91ba0d1.pdf)]
- **Haiyan Li** Doctoral supervisor in the School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine. Works on machine learning and TCM AI. [School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine] [[Admissions](https://gra.njucm.edu.cn/_upload/article/files/8f/0a/bd6170cd44ad94f0d3108af24abe/aff48fcb-3589-4b90-a66d-c93ec91ba0d1.pdf)]
- **Wanjun Gu** Doctoral supervisor in the School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine. Works on bioinformatics and TCM big data. [School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine] [[Admissions](https://gra.njucm.edu.cn/_upload/article/files/8f/0a/bd6170cd44ad94f0d3108af24abe/aff48fcb-3589-4b90-a66d-c93ec91ba0d1.pdf)]
- **Tao Yang** Professor and master's supervisor in the School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine. Works on TCM AI, multimodal tongue diagnosis, and medical-case knowledge graphs. [School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine] [[Homepage](https://xxjs.njucm.edu.cn/2021/0305/c449a71318/pagem.htm)]
- **Tianshu Wang** Associate professor and master's supervisor at Nanjing University of Chinese Medicine. Works on TCM AI, visual recognition, and whole-body inspection. [School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine] [[Homepage](http://xxjs.njucm.edu.cn/2024/0409/c465a125588/page.htm)]
- **Caiyan Dai** Associate professor and master's supervisor at Nanjing University of Chinese Medicine. Works on intelligent image processing, TCM network models, and inspection-data capture. [School of Artificial Intelligence and Information Technology, Nanjing University of Chinese Medicine] [[Homepage](http://xxjs.njucm.edu.cn/2024/0409/c465a125589/page.htm)]
- **Youbing Xia** Doctoral supervisor at Nanjing University of Chinese Medicine and chair of the digital-intelligent acupuncture committee of the China Association of Acupuncture-Moxibustion. Builds acupuncture knowledge graphs, an intelligent assistance system, and an acupuncture model. [Nanjing University of Chinese Medicine, Nanjing Medical University] [[Homepage](https://bmei.njmu.edu.cn/2025/1107/c11345a293500/page.htm)]
- **Tiancheng Xu** Distinguished professor at Nanjing University of Chinese Medicine. Proposed digital meridians and works on intelligent acupuncture robots, point localization, technique replay, and deqi force feedback. [Nanjing University of Chinese Medicine] [[Homepage](https://zgze.cbpt.cnki.net/portal/journal/portal/client/news/zgze_b164694d-d190-4244-838a-908efa219f6e)]

</details>

<details>
<summary>Dajing TCM (3)</summary>

- **Wenyou Li** Founder and chairman of Dajing TCM. The company released the Qihuang Wendao TCM model for assisted care, using knowledge graphs and clinical data. [Dajing TCM] [[News](https://www.vbdata.cn/1518996221)]
- **Jing Zhao** Co-founder and vice general manager of Dajing TCM, and an industry professor and graduate supervisor at Nanjing University of Chinese Medicine. Leads research on Qihuang Wendao and university–hospital collaboration. [Dajing TCM, Nanjing University of Chinese Medicine] [[News](https://www.vbdata.cn/1518996221)]
- **Qi Wang** Technical director of Dajing TCM. Leads the Qihuang Wendao training path and pulse, tongue, and face devices. [Dajing TCM] [[News](http://js.news.cn/20230729/fa034db71a00487b819a4ad95b44673e/c.html)]

</details>

<details>
<summary>China Pharmaceutical University (2)</summary>

- **Yinyin Wang** Associate researcher and master's supervisor at China Pharmaceutical University. Uses AI and multi-omics to study formula mechanisms, compatibility, and meridian tropism. [School of Traditional Chinese Pharmacy, China Pharmaceutical University] [[Homepage](http://zyxy.cpu.edu.cn/ab/53/c19966a240467/page.htm)]
- **Xiaobin Jia** Professor and doctoral supervisor at China Pharmaceutical University. Works on intelligent Chinese pharmacy, using AI and graph neural networks for material basis and compatibility. [School of Traditional Chinese Pharmacy, China Pharmaceutical University] [[Homepage](https://zyxy.cpu.edu.cn/ab/47/c19965a240455/page.htm)]

</details>

<details>
<summary>Nanjing University (1)</summary>

- **Qi Huang** Professor and doctoral supervisor in the School of Information Management, Nanjing University. Co-developed the TCM classics model Huangdi. [School of Information Management, Nanjing University] [[Homepage](https://im.nju.edu.cn/info/1099/33751.htm)]

</details>

<details>
<summary>Kanion Pharmaceutical (1)</summary>

- **Wei Xiao** Chair of Kanion Pharmaceutical and director of the national key laboratory for Chinese-medicine process control and intelligent manufacturing. Advances industrial large models and geo-authentic herb traceability. [Kanion Pharmaceutical] [[Homepage](https://www.kanion.com/about/about_us.htm)]

</details>

<details>
<summary>Jiangsu Province Academy of Traditional Chinese Medicine (1)</summary>

- **Ding Qu** Doctoral supervisor at Jiangsu Province Academy of Traditional Chinese Medicine. Works on AI for innovative Chinese-medicine formulations. [Jiangsu Province Academy of Traditional Chinese Medicine] [[Admissions](https://gra.njucm.edu.cn/_upload/article/files/69/4f/90badc1f4e238ef01e08cf30e770/caac9243-df3c-4435-8167-f3f4d2f44416.pdf)]

</details>

<details>
<summary>Jiangsu Province Hospital of Chinese Medicine (1)</summary>

- **Ting Wu** Doctoral supervisor at Jiangsu Province Hospital of Chinese Medicine. Works on AI classification of pain functional imaging and nanomedicine. [Jiangsu Province Hospital of Chinese Medicine] [[Admissions](https://gra.njucm.edu.cn/_upload/article/files/69/4f/90badc1f4e238ef01e08cf30e770/caac9243-df3c-4435-8167-f3f4d2f44416.pdf)]

</details>

<details>
<summary>Xiyuan Hospital Suzhou (1)</summary>

- **Bing Wu** Director of hematology at Xiyuan Hospital Suzhou. Leads the Ye Tianshi blood-syndrome decision-support model. [Xiyuan Hospital Suzhou] [[News](https://www.xyhospital.com/Html/News/Articles/22524.html)]

</details>


</details>

<details>
<summary>Zhejiang (16)</summary>

<details>
<summary>Zhejiang University (7)</summary>

- **Yiyu Cheng** Professor and doctoral supervisor in the College of Pharmaceutical Sciences, Zhejiang University. Works on AI for the pharmaceutical industry, intelligent manufacturing, and quality analysis. [College of Pharmaceutical Sciences, Zhejiang University] [[Homepage](https://person.zju.edu.cn/chengyy)]
- **Haibin Qu** Professor, doctoral supervisor, and director of the Institute of Pharmaceutical Informatics, Zhejiang University. Works on Chinese-medicine creation, process analysis, and pharmaceutical big data. [College of Pharmaceutical Sciences, Zhejiang University] [[Homepage](http://www.cps.zju.edu.cn/59113/list.htm)]
- **Jie Liao** Researcher and doctoral supervisor at Zhejiang University, leading the TCM direction of the Future Health Laboratory. Works on Chinese-medicine systems biology and TCM AI. [Zhejiang University] [[Homepage](https://yrd.zju.edu.cn/2026/0326/c90460a3144544/page.htm)]
- **Yi Wang** Professor and doctoral supervisor in the College of Pharmaceutical Sciences, Zhejiang University. Works on bioactive constituents of Chinese medicine, high-content screening, and systems pharmacology. [College of Pharmaceutical Sciences, Zhejiang University] [[Homepage](https://person.zju.edu.cn/yiwang)]
- **Xuesong Liu** Researcher and doctoral supervisor at Zhejiang University. Works on intelligent pharmaceutical manufacturing, near-infrared online detection, and whole-process quality control. [College of Pharmaceutical Sciences, Zhejiang University] [[Homepage](http://www.cps.zju.edu.cn/59114/list.htm)]
- **Yong Chen** Researcher and doctoral supervisor at Zhejiang University. Works on advanced manufacturing technology for Chinese medicine. [College of Pharmaceutical Sciences, Zhejiang University] [[Homepage](http://www.cps.zju.edu.cn/59114/list.htm)]
- **Xingchu Gong** Associate professor and doctoral supervisor at Zhejiang University. Works on Chinese-medicine quality control, manufacturing processes, and equipment. [College of Pharmaceutical Sciences, Zhejiang University] [[Homepage](https://person.zju.edu.cn/gongxc)]

</details>

<details>
<summary>Zhejiang Chinese Medical University (4)</summary>

- **Xiaohui Fan** Qiushi Distinguished Professor and doctoral supervisor at Zhejiang University, and vice president of Zhejiang Chinese Medical University. His TCM+X group works on AI for TCM and released TCMChat. [College of Pharmaceutical Sciences, Zhejiang University, Zhejiang Chinese Medical University] [[Homepage](https://person.zju.edu.cn/fanxh)] [[Paper](https://doi.org/10.1016/j.phrs.2024.107530)] [[Code](https://github.com/ZJUFanLab/TCMChat)]
- **Xiaobo Lai** Professor, doctoral supervisor, and vice dean at Zhejiang Chinese Medical University. Works on intelligent TCM and medical-imaging AI. [Zhejiang Chinese Medical University] [[Homepage](https://yjxx.zcmu.edu.cn/info/1071/9229.htm)]
- **Shuyuan Lin** Associate professor at Zhejiang Chinese Medical University and director of a joint TCM AI engineering center. Built the classical-formula consultation system Xuanqi Wendui with large models and knowledge graphs. [Zhejiang Chinese Medical University] [[Homepage](https://xhhos.com/department/doctor/5/30/233)]
- **Yuejun Zhou** Professor, chief physician, and master's supervisor at Zhejiang Chinese Medical University, and director of Chinese diagnostics. Studies tongue-based syndrome differentiation. [Zhejiang Chinese Medical University] [[Homepage](https://jc.zcmu.edu.cn/info/1164/3346.htm)]

</details>

<details>
<summary>WeDoctor (1)</summary>

- **Jieyuan Liao** Founder and chairman of WeDoctor. Built an AI Chinese-medicine platform that turns master-physician experience into granule prescriptions. [WeDoctor] [[News](https://www.cls.cn/detail/1661807)]

</details>

<details>
<summary>Hangzhou Hospital of Traditional Chinese Medicine (1)</summary>

- **Yonghua Zhang** Chief physician and doctoral supervisor at Hangzhou Hospital of Traditional Chinese Medicine. His team built the Zhang Yonghua sleep agent. [Hangzhou Hospital of Traditional Chinese Medicine] [[Homepage](https://zyy.lanews.com.cn/content/2022-02/17/content_9341799.htm)]

</details>

<details>
<summary>Zhejiang Gongshang University (1)</summary>

- **Yi Zhuang** Professor in the School of Computer Science, Zhejiang Gongshang University. First author of the TCM formula model TCM-KLLaMA. [School of Computer Science, Zhejiang Gongshang University] [[Homepage](https://scie.zjgsu.edu.cn/zh-hans/node/400)]

</details>

<details>
<summary>Zhejiang Provincial Hospital of Chinese Medicine (1)</summary>

- **Hongbo Chen** Chief physician and head of nephrology at Zhejiang Provincial Hospital of Chinese Medicine. The department hosts an engineering center for key AI technologies and equipment, including famous-doctor digital-twin robots. [Zhejiang Provincial Hospital of Chinese Medicine] [[Homepage](https://www.zjhtcm1931.cn/departmentInfo/54)]

</details>

<details>
<summary>Maijing (1)</summary>

- **Junang Ma** Chair of Maijing. Builds a vertical Chinese-medicine model, prescription assistance, and a tongue-and-face image library. [Maijing] [[News](https://www.vbdata.cn/51488)]

</details>


</details>

<details>
<summary>Anhui (12)</summary>

<details>
<summary>Anhui University of Chinese Medicine (6)</summary>

- **Xuemei Zhou** Professor, master's supervisor, and chair of basic Chinese medicine at Anhui University of Chinese Medicine. Her diagnostics team built an AI tongue-diagnosis training and assessment platform. [Anhui University of Chinese Medicine] [[Homepage](https://gjjk.ahtcm.edu.cn/info/1033/1970.htm)]
- **Jili Hu** Hefei. Associate professor and master's supervisor at Anhui University of Chinese Medicine. Uses large language models and knowledge graphs for intelligent Chinese diagnosis, and classifies tongue images. [School of Medical Information Engineering, Anhui University of Chinese Medicine] [[Homepage](https://xxgc.ahtcm.edu.cn/info/1821/53543.htm)]
- **Lei Yu** Hefei. Professor and doctoral supervisor at Anhui University of Chinese Medicine. Recruits in Chinese-medicine informatics, medical big data, and artificial intelligence for intelligent diagnosis. [Anhui University of Chinese Medicine] [[Homepage](https://xxgc.ahtcm.edu.cn/info/1821/56223.htm)]
- **Hongxing Kan** Hefei. Dean, professor, and doctoral supervisor at Anhui University of Chinese Medicine. Works on Chinese-medicine data mining and medical big data and artificial intelligence. [School of Medical Information Engineering, Anhui University of Chinese Medicine] [[Homepage](https://xxgc.ahtcm.edu.cn/info/1821/53623.htm)]
- **Jianhua Shu** Hefei. Professor and master's supervisor at Anhui University of Chinese Medicine. Leads a knowledge-graph and large-model system for intelligent diagnosis based on Xin'an physicians. [Anhui University of Chinese Medicine] [[Homepage](https://yjsb.ahtcm.edu.cn/info/2071/41961.htm)]
- **Yinfeng Yang** Hefei. Associate professor, master's supervisor, and lead of the artificial-intelligence major at Anhui University of Chinese Medicine. Uses AI to screen Chinese-medicine constituents and optimize formulas. [Anhui University of Chinese Medicine] [[Homepage](https://yjsb.ahtcm.edu.cn/info/2521/47781.htm)]

</details>

<details>
<summary>iFlytek (3)</summary>

- **Jiafeng Zhou** Vice president of iFlytek. Works with Beijing University of Chinese Medicine on the Xinhuo Zhongguoyao education model. [iFlytek] [[News](https://zhongyao.bucm.edu.cn/yyxw/57d9fb0a8af1496b88ca404e51e4e7d1.htm)]
- **Ke Wang** Vice president of iFlytek. Took part in the release and later development of the Xinhuo Zhongguoyao education model. [iFlytek] [[News](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)]
- **Li Li** Dean of iFlytek's higher-education institute. Works with universities on the Xinhuo Zhongguoyao model. [iFlytek] [[News](https://zhongyao.bucm.edu.cn/yyxw/1b48fd51feea43a2964b2a19f0ae4916.htm)]

</details>

<details>
<summary>Hefei University of Technology (1)</summary>

- **Jun Gao** Professor and doctoral supervisor at Hefei University of Technology. Co-developed the tongue-diagnosis model TongueVLM. [School of Computer Science and Information Engineering, Hefei University of Technology] [[Homepage](https://ci.hfut.edu.cn/info/1134/13735.htm)]

</details>

<details>
<summary>First Affiliated Hospital of Anhui University of Chinese Medicine (1)</summary>

- **Ling Xin** Hefei. Senior engineer, master's supervisor, and director of the clinical research data center at the First Affiliated Hospital of Anhui University of Chinese Medicine. Works on Chinese-medicine informatization, medical big data, and digital inheritance. [First Affiliated Hospital of Anhui University of Chinese Medicine] [[Homepage](https://yjsb.ahtcm.edu.cn/info/2071/42051.htm)]

</details>

<details>
<summary>Second Affiliated Hospital of Anhui University of Chinese Medicine (1)</summary>

- **Changwu Dong** Professor, doctoral supervisor, and president of the Second Affiliated Hospital of Anhui University of Chinese Medicine. Works on objective four diagnoses and multimodal tongue diagnosis. [Second Affiliated Hospital of Anhui University of Chinese Medicine] [[Homepage](https://yjsb.ahtcm.edu.cn/info/1501/30891.htm)]

</details>


</details>

<details>
<summary>Fujian (13)</summary>

<details>
<summary>Xiamen University (8)</summary>

- **Zhiming Luo** Associate professor and doctoral supervisor at Xiamen University. Works on temporal graphs of disease progression, clinical text extraction, and TCM evaluation platforms. [School of Informatics, Xiamen University] [[Homepage](https://faculty.xmu.edu.cn/luozhiming/zh_CN/index.htm)]
- **Yanhui Wang** Professor and master's supervisor at Xiamen University School of Medicine. Works on clinical tongue diagnosis and tongue-diagnosis support systems. [School of Medicine, Xiamen University] [[Homepage](https://xah.xmu.edu.cn/info/1625/2795.htm)]
- **Shaoliang Zhang** Assistant professor at Xiamen University School of Medicine. Works on digitized Chinese diagnosis, tongue-image analysis, and pulse signals. [School of Medicine, Xiamen University] [[Homepage](https://med.xmu.edu.cn/info/1238/4637.htm)]
- **Kuanqi He** Associate professor at Xiamen University School of Medicine. Applies tongue diagnosis clinically and studies syndrome elements, formulas, constitution, and tongue images. [School of Medicine, Xiamen University] [[Homepage](https://med.xmu.edu.cn/info/1237/4641.htm)]
- **Xiaoyang Huang** Assistant professor in the School of Informatics at Xiamen University. Works on in-the-wild tongue detection, color-cast correction, and tongue-coating separation. [School of Informatics, Xiamen University] [[Homepage](https://scholar.xmu.edu.cn/Authors/Index?id=HuangXiaoYang)]
- **Songzhi Su** Associate professor and master's supervisor in artificial intelligence at Xiamen University, and founder of Guanjianzai. Works on language models, intelligent Chinese diagnosis, and an all-in-one four-examination device. [Guanjianzai (Xiamen), Xiamen University] [[Homepage](https://iai.xmu.edu.cn/team/PI/PI2024/jcll/zndmtjs.htm)] [[News](https://news.qq.com/rain/a/20240914A05NEU00)]
- **Shaozi Li** Xiamen. Professor and doctoral supervisor at Xiamen University, and doctoral supervisor in Chinese diagnostics at Fujian University of Traditional Chinese Medicine. Works on intelligent science and intelligent Chinese-medicine information processing. [Xiamen University] [[Homepage](https://imt.xmu.edu.cn/info/1003/1182.htm)]
- **Kunhong Liu** Xiamen. Professor and doctoral supervisor at Xiamen University. Works on tongue-diagnosis artificial intelligence, data mining, and health-care big data. [Xiamen University] [[Homepage](https://cdmc.xmu.edu.cn/info/1010/1055.htm)]

</details>

<details>
<summary>Fujian University of Traditional Chinese Medicine (4)</summary>

- **Disheng Feng** Master’s supervisor in the School of Pharmacy, Fujian University of Traditional Chinese Medicine. Works on artificial intelligence and metabolomics. [School of Pharmacy, Fujian University of Traditional Chinese Medicine] [[Admissions](https://static.kaoyan.cn/file/2025/09/22/681e4fb4056d67fff4ae7ff9501397da.pdf)]
- **Yongjing Liu** Master’s supervisor in the School of Pharmacy, Fujian University of Traditional Chinese Medicine. Works on artificial intelligence and metabolomics. [School of Pharmacy, Fujian University of Traditional Chinese Medicine] [[Admissions](https://static.kaoyan.cn/file/2025/09/22/681e4fb4056d67fff4ae7ff9501397da.pdf)]
- **Xuejuan Lin** Doctoral supervisor at Fujian University of Traditional Chinese Medicine. The listed direction is acquisition and standardization of four-examination information. [College of Traditional Chinese Medicine, Fujian University of Traditional Chinese Medicine] [[Admissions](http://static.hhkaobo.com/upload/editor/f2e35d52-e85d-4e6b-a133-fa3eefd53cc9.pdf)]
- **Candong Li** Fuzhou. Professor and doctoral supervisor at Fujian University of Traditional Chinese Medicine, and chief scientist at the Xinhuangpu joint innovation institute. Works on Chinese medical diagnosis. [Fujian University of Traditional Chinese Medicine] [[Homepage](https://www.jiicm.com/info/1078/1241.htm)]

</details>

<details>
<summary>Fuyao University of Science and Technology (1)</summary>

- **Zhengzhong Zhu** Professor and doctoral supervisor at Fuyao University of Science and Technology. Co-corresponding author of Zhongjing GPT, working on health and TCM models. [Fuyao University of Science and Technology] [[Homepage](https://cs.fyust.edu.cn/szdw/jsdw/zzz.htm)]

</details>


</details>

<details>
<summary>Jiangxi (13)</summary>

<details>
<summary>Jiangxi University of Chinese Medicine (11)</summary>

- **Jianqiang Du** Corresponding author of DualKAG-ShenNong, a knowledge-graph retrieval model for TCM consultation, at the Jiangxi key laboratory for TCM AI. [Jiangxi University of Chinese Medicine] [[Paper](http://cea.ceaj.org/CN/Y2026/V62/I9/133)]
- **Xinyou Zhang** Professor and doctoral supervisor at Jiangxi University of Chinese Medicine. Mines data on herb properties and formula compatibility. [College of Intelligent Medicine and Information Engineering, Jiangxi University of Chinese Medicine] [[Homepage](https://jsj.jxutcm.edu.cn/info/1071/1913.htm)]
- **Qing Ye** Faculty member at Jiangxi University of Chinese Medicine. Works on Chinese-medicine knowledge graphs. [Jiangxi University of Chinese Medicine] [[Homepage](https://jsj.jxutcm.edu.cn/info/1036/1277.htm)]
- **Yanchen Zhu** Faculty member at Jiangxi University of Chinese Medicine. Works on Chinese-medicine images. [College of Intelligent Medicine and Information Engineering, Jiangxi University of Chinese Medicine] [[Homepage](https://jsj.jxutcm.edu.cn/info/1071/1917.htm)]
- **Ming Yang** Vice president and doctoral supervisor at Jiangxi University of Chinese Medicine. Digitizes Chinese-medicine equipment with multispectral and hyperspectral imaging and machine vision. [Jiangxi University of Chinese Medicine] [[Homepage](https://www.jiicm.com/info/1017/1179.htm)]
- **Zhenfeng Wu** Director of the Key Laboratory of Modern Preparation of TCM, Ministry of Education. Leads the laboratory and joins collaboration on intelligent Chinese-medicine manufacturing. [Jiangxi University of Chinese Medicine] [[Homepage](https://www.catcm.org.cn/139/202407/4051.html)]
- **Helin Zhang** Nanchang. Associate professor and master's supervisor at Jiangxi University of Chinese Medicine. Works on objective color diagnosis and automatic classification of tongue body and coating. [Jiangxi University of Chinese Medicine] [[Homepage](https://jsj.jxutcm.edu.cn/info/1071/1977.htm)]
- **Wangping Xiong** Nanchang. Professor and master's supervisor at Jiangxi University of Chinese Medicine. Mines Chinese-medicine data and leads knowledge-graph monitoring of patent-medicine use. [Jiangxi University of Chinese Medicine] [[Homepage](https://jsj.jxutcm.edu.cn/info/1071/1914.htm)]
- **Bin Nie** Nanchang. Professor and master's supervisor at Jiangxi University of Chinese Medicine. Works on Chinese-medicine data analysis and health big data and artificial intelligence. [Jiangxi University of Chinese Medicine] [[Homepage](https://jsj.jxutcm.edu.cn/info/1071/1921.htm)]
- **Diyao Wu** Nanchang. Associate professor and master's supervisor at Jiangxi University of Chinese Medicine. Works on Chinese-medicine informatics and clinical decision-support models. [Jiangxi University of Chinese Medicine] [[Homepage](https://jsj.jxutcm.edu.cn/info/1071/1928.htm)]
- **Qinglin Zha** Nanchang. Professor and master's supervisor at Jiangxi University of Chinese Medicine. Uses big data and artificial intelligence for health management and preventive care. [Jiangxi University of Chinese Medicine] [[Homepage](https://jcyxy.jxutcm.edu.cn/info/5171/21081.htm)]

</details>

<details>
<summary>China Resources Jiangzhong (2)</summary>

- **Yicheng Fei** Deputy director of advanced manufacturing research at China Resources Jiangzhong. Builds industrial agents that digitize Chinese-medicine production experience. [China Resources Jiangzhong] [[News](https://www.jinantimes.com.cn/news-99-11066075.html)]
- **Zhijian Zhong** General manager of the Wanli manufacturing base at China Resources Jiangzhong. Runs an intelligent solid-dosage line, online granulation detection, and AI visual inspection. [China Resources Jiangzhong] [[News](https://www.jinantimes.com.cn/news-99-11066075.html)]

</details>


</details>

<details>
<summary>Shandong (20)</summary>

<details>
<summary>Shandong University of Traditional Chinese Medicine (11)</summary>

- **Benzheng Wei** Professor, doctoral supervisor, and dean of the School of Medical Information Engineering, Shandong University of Traditional Chinese Medicine. Works on medical AI, TCM image analysis, and intelligent diagnosis. [School of Medical Information Engineering, Shandong University of Traditional Chinese Medicine] [[Homepage](https://zxxy.sdutcm.edu.cn/info/1109/2430.htm)]
- **Hui Sheng** Associate professor, master's supervisor, and vice dean at Shandong University of Traditional Chinese Medicine. Works on health big data and intelligent TCM. [School of Medical Information Engineering, Shandong University of Traditional Chinese Medicine] [[Homepage](https://zxxy.sdutcm.edu.cn/info/1109/2445.htm)]
- **Hui Cao** Second-class professor and doctoral supervisor at Shandong University of Traditional Chinese Medicine. Works on intelligent Chinese medicine and medical data mining. [College of Medical Information Engineering, Shandong University of Traditional Chinese Medicine] [[Homepage](https://zxxy.sdutcm.edu.cn/info/1086/1972.htm)]
- **Dejian Wei** Associate professor and master's supervisor at Shandong University of Traditional Chinese Medicine. Works on intelligent Chinese medicine and medical information processing. [College of Medical Information Engineering, Shandong University of Traditional Chinese Medicine] [[Homepage](https://zxxy.sdutcm.edu.cn/info/1109/2439.htm)]
- **Shujian Zhang** Professor at Shandong University of Traditional Chinese Medicine. Leads a knowledge graph of meridian brain representation and visceral regulation, reorganizing meridian literature with language models and deep learning. [Institute of Chinese Medical Literature and Culture, Shandong University of Traditional Chinese Medicine] [[Homepage](https://wenxian.sdutcm.edu.cn/info/1042/1234.htm)]
- **Jian Ren** Professor and doctoral supervisor at Shandong University of Traditional Chinese Medicine. The listed direction is digital and empirical research on the four examinations. [College of Traditional Chinese Medicine, Shandong University of Traditional Chinese Medicine] [[Homepage](https://zyxyx.sdutcm.edu.cn/info/1075/5703.htm)]
- **Xiaorui Cheng** Distinguished professor and doctoral supervisor at Shandong University of Traditional Chinese Medicine, also recruiting master's students. Directions include Chinese-medicine pharmacology and network pharmacology. [Shandong University of Traditional Chinese Medicine] [[Homepage](https://cxyjy.sdutcm.edu.cn/info/1253/2588.htm)]
- **Jing Liu** Jinan. Professor and doctoral supervisor at Shandong University of Traditional Chinese Medicine. Works on intelligent Chinese medicine and medical image analysis. [School of Medical Information Engineering, Shandong University of Traditional Chinese Medicine] [[Homepage](https://zxxy.sdutcm.edu.cn/info/1109/2433.htm)]
- **Wanli Xu** Jinan. Associate professor and master's supervisor at Shandong University of Traditional Chinese Medicine. Studies tongue diagnosis, pulse diagnosis, and their relation to syndromes. [College of Traditional Chinese Medicine, Shandong University of Traditional Chinese Medicine] [[Homepage](https://zyxyx.sdutcm.edu.cn/info/1082/5763.htm)]
- **Kuixing Zhang** Jinan. Professor at Shandong University of Traditional Chinese Medicine, director of biomedical engineering, and lead of the provincial key discipline in Chinese-medicine artificial intelligence. [School of Medical Information Engineering, Shandong University of Traditional Chinese Medicine] [[Homepage](https://zxxy.sdutcm.edu.cn/info/1109/2436.htm)]
- **Ming Li** Jinan. Professor at Shandong University of Traditional Chinese Medicine and deputy director of the graduate office. Leads the discipline of healthcare big data. [School of Medical Information Engineering, Shandong University of Traditional Chinese Medicine] [[Homepage](https://zxxy.sdutcm.edu.cn/info/1109/2432.htm)]

</details>

<details>
<summary>Qilu University of Technology (Shandong Academy of Sciences) (3)</summary>

- **Wenpeng Lu** Professor and doctoral supervisor at Qilu University of Technology (Shandong Academy of Sciences), leading the NLP and cognitive computing group. Works on medical LLMs and agents and released the TCM model BianCang. [Qilu University of Technology (Shandong Academy of Sciences)] [[Homepage](https://nlp.qlu.edu.cn/wenpeng_lu/)] [[Paper](https://arxiv.org/abs/2411.11027)] [[Code](https://github.com/QLU-NLP/BianCang)]
- **Yinglong Wang** Professor and doctoral supervisor at Qilu University of Technology (Shandong Academy of Sciences). Works on medical AI and high-performance computing; the group released the TCM model BianCang. [Qilu University of Technology (Shandong Academy of Sciences)] [[Homepage](https://bdi.qlu.edu.cn/2021/1222/c10714a176991/page.htm)] [[Code](https://github.com/QLU-NLP/BianCang)]
- **Hongjiao Guan** Associate professor and master's supervisor at Qilu University of Technology. Works on medical language models and BianCang evaluation for syndrome differentiation and prescriptions. [Qilu University of Technology (Shandong Academy of Sciences)] [[Paper](http://jsxb.scsc.cn/introlist_76/794.html)]

</details>

<details>
<summary>Affiliated Hospital of Shandong University of Traditional Chinese Medicine (2)</summary>

- **Hualiang Deng** President of the Affiliated Hospital of Shandong University of Traditional Chinese Medicine. Leads the provincial Zhihui Qihuang model for master-physician experience and primary care. [Affiliated Hospital of Shandong University of Traditional Chinese Medicine] [[News](http://ccpd.china.com.cn/2026-04/17/content_43401621.html)]
- **Xianghua Qi** Jinan. Doctoral supervisor at the Affiliated Hospital of Shandong University of Traditional Chinese Medicine. Founded systematic pulse differentiation and leads an intelligent pulse-diagnosis device. [Affiliated Hospital of Shandong University of Traditional Chinese Medicine] [[Homepage](https://www.sdutcm.edu.cn/info/1003/9618.htm)]

</details>

<details>
<summary>China Resources Dong-E-E-Jiao (1)</summary>

- **Fengli Ding** Chief information officer of China Resources Dong-E-E-Jiao. Builds a tonic-domain AI model and uses digital terminals for TCM constitution identification. [China Resources Dong-E-E-Jiao] [[News](https://cn.chinadaily.com.cn/a/202607/23/WS6a61a78ca310d709c2fbf393.html)]

</details>

<details>
<summary>Harbin Institute of Technology (1)</summary>

- **Dianhui Chu** Professor and doctoral supervisor at Harbin Institute of Technology, Weihai. Leads the Tiangong medical-model training platform for TCM consultation, syndrome differentiation, and diet therapy. [Harbin Institute of Technology, Weihai] [[Homepage](https://software.hit.edu.cn/12762/list.htm)]

</details>

<details>
<summary>Shandong University (1)</summary>

- **Hengchang Zang** Researcher and doctoral supervisor at Shandong University. Works on advanced oral Chinese-medicine manufacturing, near-infrared process analysis, and quality visualization for continuous manufacturing. [School of Pharmaceutical Sciences, Shandong University] [[Homepage](https://kltredp.sdu.edu.cn/rcpy/PItdjj.htm)]

</details>

<details>
<summary>Buchang Pharmaceuticals (1)</summary>

- **Lian Shu** General manager of information construction at Buchang Pharmaceuticals. Covers business-finance integration, warehouse execution, and production-line robots for Chinese-medicine manufacturing. [Buchang Pharmaceuticals] [[News](https://articles.e-works.net.cn/700/article153015.htm)]

</details>


</details>

<details>
<summary>Henan (12)</summary>

<details>
<summary>Henan University of Chinese Medicine (7)</summary>

- **Yulong Xu** Associate professor and master's supervisor at Henan University of Chinese Medicine. Uses latent structure models and machine learning for syndrome rules. [Henan University of Chinese Medicine] [[Homepage](https://glxy.hactcm.edu.cn/info/1062/10540.htm)]
- **Jiarui Wu** Doctoral supervisor at Henan University of Chinese Medicine. The listed direction is antitumor mechanisms of Chinese medicines based on precision network pharmacology. [School of Pharmacy, Henan University of Chinese Medicine] [[Admissions](https://yjsy.hactcm.edu.cn/images/Userfiles/file_20250506_6388212460132763432631524.pdf)]
- **Changhai Wang** Zhengzhou. Associate professor and master's supervisor at Henan University of Chinese Medicine. Works on objective four examinations, syndrome data mining, and Chinese diagnostics. [Henan University of Chinese Medicine] [[Homepage](https://zyxy.hactcm.edu.cn/info/1110/2735.htm)]
- **Hao Dang** Zhengzhou. Associate professor and master's supervisor at Henan University of Chinese Medicine. Works on Chinese-medicine artificial intelligence, tongue and pulse diagnosis, knowledge graphs, and data mining. [Henan University of Chinese Medicine] [[Homepage](https://cs.haut.edu.cn/info/1541/8594.htm)]
- **Zhiying Che** Zhengzhou. Professor and doctoral supervisor at Henan University of Chinese Medicine. Works on intelligent syndrome informatization and artificial intelligence for the four examinations. [Henan University of Chinese Medicine] [[Homepage](https://zyxy.hactcm.edu.cn/info/2008/27315.htm)]
- **Xuekun Song** Zhengzhou. Master's supervisor in the school of information technology at Henan University of Chinese Medicine. Works on computational biomedical informatics. [Henan University of Chinese Medicine] [[Homepage](https://glxy.hactcm.edu.cn/info/1062/8030.htm)]
- **Suxiang Feng** Zhengzhou. Professor and doctoral supervisor at Henan University of Chinese Medicine. Works on intelligent Chinese-medicine analysis, multi-omics, and quality evaluation. [Henan University of Chinese Medicine] [[Homepage](https://kxy.hactcm.edu.cn/kytd/zyzlpjyxyyfsys.htm)]

</details>

<details>
<summary>Henan University of Technology (2)</summary>

- **Peng Li** Professor, doctoral supervisor, and dean of the Institute of Complexity Science, Henan University of Technology. Works on TCM AI, tongue images, and pre-disease modeling. [Henan University of Technology] [[Homepage](https://computer.haut.edu.cn/info/1042/10906.htm)]
- **Lei Lyu** Professor and doctoral supervisor at Henan University of Technology. Works on 3D tongue perception and visual quality analysis of Chinese medicinal materials. [Henan University of Technology] [[Homepage](https://cs.haut.edu.cn/info/1541/5754.htm)]

</details>

<details>
<summary>Zhengzhou University (2)</summary>

- **Hongying Zan** Professor and doctoral supervisor at Zhengzhou University. Her laboratory developed the Zhongjing TCM model line. [School of Computer and Artificial Intelligence, Zhengzhou University] [[Homepage](https://www5.zzu.edu.cn/nlp/info/1004/1169.htm)]
- **Yuxiang Jia** Associate professor and master's supervisor at Zhengzhou University. Corresponding author of the AAAI Zhongjing paper. [School of Computer and Artificial Intelligence, Zhengzhou University] [[Homepage](https://www5.zzu.edu.cn/nlp/info/1004/1157.htm)]

</details>

<details>
<summary>First Affiliated Hospital of Henan University of Chinese Medicine (1)</summary>

- **Mingjun Zhu** Professor and Qihuang Scholar at the First Affiliated Hospital of Henan University of Chinese Medicine. Leads digital TCM chronic-disease control and TCM big data, and takes part in the university’s digital TCM institute. [First Affiliated Hospital of Henan University of Chinese Medicine] [[Homepage](https://www.hnzhy.com/TDoctors-3.html)] [[News](http://www.ha.xinhua.org/20260817/ef25dd0c98e94a94be25f0f3b064ee1c/c.html)]

</details>


</details>

<details>
<summary>Hubei (15)</summary>

<details>
<summary>Hubei University of Chinese Medicine (12)</summary>

- **Shaowu Shen** Researcher, doctoral supervisor, and executive dean of the TCM Big Data and Knowledge Engineering Institute, Hubei University of Chinese Medicine. [Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11342.htm)]
- **Dan Xie** Professor and master's supervisor at Hubei University of Chinese Medicine. Works on medical artificial intelligence, data mining, and natural language processing. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11262.htm)]
- **Wenping Deng** Faculty member at Hubei University of Chinese Medicine. Works on Chinese-medicine informatization and standards. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11272.htm)]
- **Yong Xiao** Wuhan. Senior experimentalist and master's supervisor at Hubei University of Chinese Medicine, and vice dean of its institute for Chinese-medicine big-data knowledge engineering. Works on information standards and big data. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11282.htm)]
- **Kai Chang** Wuhan. Senior experimentalist and master's supervisor at Hubei University of Chinese Medicine. Works on Chinese-medicine standards, informatization, and artificial intelligence. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11312.htm)]
- **Rui Xiao** Wuhan. Associate professor and master's supervisor at Hubei University of Chinese Medicine. Works on natural language processing, big-data analysis, and artificial intelligence. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11802.htm)]
- **Yan Wang** Wuhan. Associate professor and master's supervisor at Hubei University of Chinese Medicine. Works on data mining, intelligent optimization, standards, informatization, and bioinformatics. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11332.htm)]
- **Jian Chang** Wuhan. Associate professor and master's supervisor at Hubei University of Chinese Medicine. Works on intelligent pharmacy, big-data analysis, and blockchain-based intelligent IoT. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/14162.htm)]
- **Wenjiao Fu** Wuhan. Associate professor and master's supervisor at Hubei University of Chinese Medicine. Works on Chinese-medicine data processing, standards, and informatization. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11792.htm)]
- **Xiaohong Cai** Wuhan. Associate professor, master's supervisor, and director of the medical information engineering section at Hubei University of Chinese Medicine. Works on Chinese-medicine informatization and data mining. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11302.htm)]
- **Li Ma** Wuhan. Professor and master's supervisor at Hubei University of Chinese Medicine. Leads the Chinese-medicine big-data center and works on analysis and evidence-based decisions. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11252.htm)]
- **Hua Guan** Wuhan. Senior experimentalist and master's supervisor at Hubei University of Chinese Medicine. Works on Chinese-medicine big-data analysis and natural language processing. [School of Information Engineering, Hubei University of Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1491/11322.htm)]

</details>

<details>
<summary>Hubei Provincial Hospital of Traditional Chinese Medicine (2)</summary>

- **Fei Xiao** Director of the information center at Hubei Provincial Hospital of Traditional Chinese Medicine. Advances the fusion of Chinese medicine and AI, medical data mining, and digital inheritance. [Hubei Provincial Hospital of Traditional Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1661/13882.htm)]
- **Jing Sun** Deputy director of the information center at Hubei Provincial Hospital of Traditional Chinese Medicine. Works on intelligent medical data mining, digital inheritance, and AI in diagnosis and research. [Hubei Provincial Hospital of Traditional Chinese Medicine] [[Homepage](https://xxy.hbucm.edu.cn/info/1661/13882.htm)]

</details>

<details>
<summary>Wuhan Hospital of Traditional Chinese Medicine (1)</summary>

- **Miao Sun** Director of the information center at Wuhan Hospital of Traditional Chinese Medicine. Presented the Han-school bone-injury dataset and agent. [Wuhan Hospital of Traditional Chinese Medicine] [[News](https://xxy.hbucm.edu.cn/info/1661/13042.htm)]

</details>


</details>

<details>
<summary>Hunan (17)</summary>

<details>
<summary>Hunan University of Chinese Medicine (14)</summary>

- **Shaoliang Peng** Doctoral supervisor in the School of Traditional Chinese Medicine, Hunan University of Chinese Medicine. Works on bioinformatics and artificial intelligence. [School of Traditional Chinese Medicine, Hunan University of Chinese Medicine] [[Admissions](http://static.hhkaobo.com/upload/editor/7a445106-62d0-4b9e-86b1-25e9fed5229f.pdf)]
- **Junfeng Yan** Professor and doctoral supervisor at Hunan University of Chinese Medicine. Works on TCM artificial intelligence and computational Chinese medicine. [Hunan University of Chinese Medicine] [[Homepage](https://xxgc.hnucm.edu.cn/info/1036/2517.htm)]
- **Changfa Wei** Professor and master's supervisor at Hunan University of Chinese Medicine. Works on intelligent TCM assistance, large models, and knowledge-graph question answering. [School of Information Science and Engineering, Hunan University of Chinese Medicine] [[Homepage](https://xxgc.hnucm.edu.cn/info/1036/3990.htm)]
- **Hao Liang** Associate professor and doctoral supervisor at Hunan University of Chinese Medicine. Supervises intelligent inspection, stained-coating recognition, and lower-cost tongue-diagnosis devices. [Hunan University of Chinese Medicine] [[Homepage](https://kczx.hnucm.edu.cn/info/1005/2198.htm)]
- **Changsong Ding** Dean, professor, and doctoral supervisor at Hunan University of Chinese Medicine. Studies Chinese-medicine big data and computable formula effects. [School of Informatics, Hunan University of Chinese Medicine] [[Homepage](https://xxgc.hnucm.edu.cn/info/1036/2522.htm)]
- **Xiaoxia Xiao** Professor and master's supervisor at Hunan University of Chinese Medicine. Works on machine vision and intelligent Chinese diagnostic devices. [School of Informatics, Hunan University of Chinese Medicine] [[Homepage](https://xxgc.hnucm.edu.cn/info/1036/3987.htm)]
- **Qingping Liu** Associate professor and master's supervisor at Hunan University of Chinese Medicine. Works on clinical decision support, data mining, and knowledge discovery for Chinese medicine. [School of Informatics, Hunan University of Chinese Medicine] [[Homepage](https://xxgc.hnucm.edu.cn/info/1036/3985.htm)]
- **Cheng Yan** Professor and doctoral supervisor at Hunan University of Chinese Medicine. Works on Chinese-medicine informatics, bioinformatics, and artificial intelligence. [School of Informatics, Hunan University of Chinese Medicine] [[Homepage](https://xxgc.hnucm.edu.cn/info/1036/3989.htm)]
- **Yang Li** Faculty member at Hunan University of Chinese Medicine. Works on Chinese-medicine information processing. [School of Informatics, Hunan University of Chinese Medicine] [[Homepage](https://xxgc.hnucm.edu.cn/info/1036/6061.htm)]
- **Wanghua Liu** Doctoral supervisor at Hunan University of Chinese Medicine. The listed direction is digitizing four-examination information and intelligent syndrome differentiation. [School of Traditional Chinese Medicine, Hunan University of Chinese Medicine] [[Admissions](http://static.hhkaobo.com/upload/editor/7a445106-62d0-4b9e-86b1-25e9fed5229f.pdf)]
- **Mengzhou Xie** Doctoral supervisor at Hunan University of Chinese Medicine. The listed direction is objective four examinations in Chinese diagnostics. [School of Traditional Chinese Medicine, Hunan University of Chinese Medicine] [[Admissions](https://static.kaoyan.cn/file/2025/01/22/a5b4ec5e68ea0f116b85c64554c9f6a0.pdf)]
- **Mi Liu** Changsha. Professor, doctoral supervisor, and vice dean of acupuncture, tuina, and rehabilitation at Hunan University of Chinese Medicine. Develops intelligent Chinese rehabilitation equipment and digital acupuncture teaching. [School of Acupuncture, Tuina and Rehabilitation, Hunan University of Chinese Medicine] [[Homepage](https://zjtn.hnucm.edu.cn/info/1101/2793.htm)]
- **Zhixi Hu** Changsha. Professor, doctoral supervisor, and discipline lead in Chinese diagnostics at Hunan University of Chinese Medicine. Works on diagnostic instruments and holds patents on pulse monitoring and rehabilitation wearables. [Hunan University of Chinese Medicine] [[Homepage](https://dfzyxk.hnucm.edu.cn/info/1027/1351.htm)]
- **Xiaoqing Zhou** Changsha. Second-class professor and doctoral supervisor at Hunan University of Chinese Medicine. Works on digital Chinese diagnosis and quantitative tongue-coating diagnosis. [School of Traditional Chinese Medicine, Hunan University of Chinese Medicine] [[Homepage](https://zyxy.hnucm.edu.cn/info/1124/4872.htm)]

</details>

<details>
<summary>Jishou University (1)</summary>

- **Kaiqing Zhou** Jishou. Master's supervisor at Jishou University. Leads a knowledge base and intelligent decision system for stomach-disease diagnosis in Xiangxi Tujia and Miao medicine. [College of Computer Science and Engineering, Jishou University] [[Homepage](https://cse.jsu.edu.cn/yjsjy/dsjj/7ee92686c2c44467988ea549cc4dc868.htm)]

</details>

<details>
<summary>AthenaEyes (1)</summary>

- **Jianhua Qiu** Founder and chairman of AthenaEyes. The company released the multimodal Bianshi model for inquiry, tongue and face diagnosis, and the four TCM examinations. [AthenaEyes] [[News](https://www.a-eye.cn/news_list/296.html)] [[Website](https://www.a-eye.cn/)]

</details>

<details>
<summary>Hunan University (1)</summary>

- **Qiaokang Liang** Professor and doctoral supervisor at Hunan University. Leads an acupuncture-robot project on force, vision, and tactile sensing and control. [College of Artificial Intelligence and Robotics, Hunan University] [[Homepage](https://robotics.hnu.edu.cn/info/1176/3095.htm)]

</details>


</details>

<details>
<summary>Guangdong (30)</summary>

<details>
<summary>Guangzhou University of Chinese Medicine (10)</summary>

- **Nenggui Xu** Professor and doctoral supervisor at Guangzhou University of Chinese Medicine, and director of the South China Acupuncture Research Center. Leads AI research on acupuncture for encephalopathy. [South China Acupuncture Research Center, Guangzhou University of Chinese Medicine] [[Homepage](https://scrcam.gzucm.edu.cn/info/1101/1488.htm)]
- **Yi Zhao** Doctoral supervisor in the School of Medical Information Engineering, Guangzhou University of Chinese Medicine. Recruits students in TCM artificial intelligence. [School of Medical Information Engineering, Guangzhou University of Chinese Medicine] [[Admissions](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **Dong Cao** Doctoral supervisor in the School of Medical Information Engineering, Guangzhou University of Chinese Medicine. Recruits students in TCM artificial intelligence. [School of Medical Information Engineering, Guangzhou University of Chinese Medicine] [[Admissions](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **Wu Zhou** Doctoral supervisor in the School of Medical Information Engineering, Guangzhou University of Chinese Medicine. Works on intelligent tongue and face diagnosis and objective TCM syndromes. [School of Medical Information Engineering, Guangzhou University of Chinese Medicine] [[Admissions](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **Hui Li** Doctoral supervisor in the School of Basic Medical Sciences, Guangzhou University of Chinese Medicine. Works on the theoretical basis and application of TCM artificial intelligence. [School of Basic Medical Sciences, Guangzhou University of Chinese Medicine] [[Admissions](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **Xinlin Chen** Doctoral supervisor in the School of Basic Medical Sciences, Guangzhou University of Chinese Medicine. Works on TCM big-data statistics and individualized evaluation. [School of Basic Medical Sciences, Guangzhou University of Chinese Medicine] [[Admissions](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **Chuanquan Lin** Doctoral supervisor at the Science and Technology Innovation Center, Guangzhou University of Chinese Medicine. Works on AI and the modernization of TCM diagnosis and treatment. [Science and Technology Innovation Center, Guangzhou University of Chinese Medicine] [[Admissions](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **Shaoyang Men** Associate professor and doctoral supervisor at Guangzhou University of Chinese Medicine. Works on intelligent TCM diagnosis and medical signal processing. [School of Medical Information Engineering, Guangzhou University of Chinese Medicine] [[Homepage](https://ygxy.gzucm.edu.cn/info/1241/2551.htm)]
- **Xiufeng Liu** Professor and master's supervisor at Guangzhou University of Chinese Medicine. Works on TCM knowledge graphs, classic-text organization, and TCM AI. [School of Medical Information Engineering, Guangzhou University of Chinese Medicine] [[Homepage](https://ygxy.gzucm.edu.cn/info/1241/2551.htm)]
- **Hudan Pan** Professor at Guangzhou University of Chinese Medicine. Works on multimodal data for rheumatic disease and an integrative Chinese–Western model. [Guangzhou University of Chinese Medicine] [[News](https://www.cntcm.com.cn/content/202406/14/c251936.html)]

</details>

<details>
<summary>Guangdong Laboratory of Traditional Chinese Medicine (4)</summary>

- **Liang Liu** Academician of the Chinese Academy of Engineering and director of the Guangdong Laboratory of Traditional Chinese Medicine (Hengqin Laboratory). The lab works on syndrome differentiation, diagnostic devices, and the Hengqin TCM model. [Guangdong Laboratory of Traditional Chinese Medicine, Guangzhou University of Chinese Medicine] [[Jobs](https://www.gzucm.edu.cn/info/1461/117451.htm)]
- **Yong Liang** Doctoral supervisor at the Guangdong Laboratory of Traditional Chinese Medicine (Hengqin Laboratory). Recruits 2026 students in TCM artificial intelligence through Guangzhou University of Chinese Medicine. [Guangdong Laboratory of Traditional Chinese Medicine, Guangzhou University of Chinese Medicine] [[Admissions](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **Hua Zhou** Deputy director of the Guangdong Laboratory of Traditional Chinese Medicine. Leads the intelligent automation platform for new Chinese medicines and digital diagnosis infrastructure. [Guangdong Laboratory of Traditional Chinese Medicine, Guangdong Provincial Hospital of Chinese Medicine] [[News](https://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/dtxx/content/post_3807664.html)]
- **Shengda Luo** Researcher at the Guangdong Laboratory of Traditional Chinese Medicine. Presented Hengqin-R1, syndrome reasoning, and agents for combined Chinese and Western medication. [Guangdong Laboratory of Traditional Chinese Medicine] [[News](https://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/dtxx/content/post_3807664.html)]

</details>

<details>
<summary>Huawei Cloud (2)</summary>

- **Nan Qiao** General manager of Huawei Cloud AI scientific computing. Presented question answering, generation, and natural-product calculation for Shuzhi Bencao. [Huawei Cloud] [[News](https://news.qq.com/rain/a/20240515A04TAH00)]
- **Pengcheng Yang** Leads application development for the Shuzhi Bencao model. Uses the language and computation models for formula screening. [Huawei Cloud] [[News](https://bbs.huaweicloud.com/blogs/448824)]

</details>

<details>
<summary>Gushengtang (2)</summary>

- **Xiang Zheng** Vice president of Gushengtang, responsible for the national-master AI twins and the TCM Brain. [Gushengtang] [[News](https://www.gstzy.cn/news/detail/10/13791.html)]
- **Zhongkai Hu** Chief technology officer of Gushengtang, responsible for the TCM model, clinical data, and deployment in care settings. [Gushengtang] [[News](https://www.gstzy.cn/news/detail/10/13791.html)]

</details>

<details>
<summary>Guangdong University of Technology (2)</summary>

- **Zhaoshui He** Professor and doctoral supervisor at Guangdong University of Technology. Leads the national key R&D project on acupuncture robots, covering point localization, insertion, and lifting-thrusting-twirling. [School of Automation, Guangdong University of Technology] [[Homepage](https://www.gdut.edu.cn/info/1709/18526.htm)]
- **Jing Guo** Associate professor and master's supervisor at Guangdong University of Technology. Leads a subproject of the acupuncture-robot program on capturing, analyzing, and replaying needling techniques. [School of Automation, Guangdong University of Technology] [[Homepage](https://teacher.gdut.edu.cn/guojing1/zh_CN/index.htm)]

</details>

<details>
<summary>Guangzhou Pharmaceutical Holdings (2)</summary>

- **Xiaojun Li** Chair of Guangzhou Pharmaceutical Holdings. Advances an AI Chinese-medicine model that starts from medicinal-plant cultivation. [Guangzhou Pharmaceutical Holdings] [[News](https://news.dayoo.com/guangzhou/202609/22/139995_55006504.htm)]
- **Haifeng Liang** Chief information officer of Guangzhou Pharmaceutical Holdings and vice president of its digital-economy institute. Covers drug traceability, intelligent manufacturing, and artificial intelligence. [Guangzhou Pharmaceutical Holdings] [[News](http://event.d1net.com/cioyy2024/)]

</details>

<details>
<summary>South China University of Technology (1)</summary>

- **Guihua Wen** Professor at South China University of Technology and lead of the Guangdong AI TCM engineering team. Works on interpretable tongue diagnosis, constitution identification, and intelligent TCM care. [School of Computer Science and Engineering, South China University of Technology] [[Homepage](https://www2.scut.edu.cn/cs/2017/0629/c22284a328095/page.htm)]

</details>

<details>
<summary>Harbin Institute of Technology (1)</summary>

- **David Zhang** Doctoral supervisor in computer science at Harbin Institute of Technology, Shenzhen. Works on computerized tongue and pulse diagnosis as biometric inspection. [School of Computer Science and Technology, Harbin Institute of Technology, Shenzhen] [[Homepage](https://csen.hitsz.edu.cn/info/1023/1904.htm)]

</details>

<details>
<summary>Guangdong Provincial Hospital of Chinese Medicine (1)</summary>

- **Zhimin Yang** Vice president, professor, chief physician, and doctoral supervisor at Guangdong Provincial Hospital of Chinese Medicine. Works on Chinese-medicine health-state identification and portable tongue and pulse devices. [Guangdong Provincial Hospital of Chinese Medicine] [[Homepage](https://www.jiicm.com/info/1017/1177.htm)]

</details>

<details>
<summary>Merchants Union Consumer Finance (1)</summary>

- **Yangqing Zhang** General manager of Merchants Union Consumer Finance. Initiated the Zhongsi TCM model. [Merchants Union Consumer Finance] [[News](http://finance.people.com.cn/n1/2025/0430/c1004-40471496.html)]

</details>

<details>
<summary>Jinan University (1)</summary>

- **Ronghua Zhang** Professor and doctoral supervisor at Jinan University, and director of the Guangdong Key Laboratory of TCM Informatization. [Jinan University] [[Homepage](https://zyxy.jnu.edu.cn/2021/0903/c6333a646617/page.htm)]

</details>

<details>
<summary>Shenzhen University (1)</summary>

- **Le Ouyang** Associate professor and doctoral supervisor at Shenzhen University. Works with Shenzhen Hospital of Traditional Chinese Medicine on an intelligent TCM consultation model. [Shenzhen University] [[Homepage](https://iip.szu.edu.cn/info/1017/1231.htm)]

</details>

<details>
<summary>Tencent Health (1)</summary>

- **Peng Yan** Vice president of Tencent Health. Partners with Jinyao Darentang on large-model delivery of TCM services and integrated question answering. [Tencent Health] [[News](https://www.pharm.com.cn/content/details59_1561.html)]

</details>

<details>
<summary>The Chinese University of Hong Kong (1)</summary>

- **Benyou Wang** Assistant professor, doctoral supervisor, and Presidential Young Fellow at the School of Data Science, The Chinese University of Hong Kong, Shenzhen. Builds medical multimodal models; the group released the TCM model ShizhenGPT. [School of Data Science, The Chinese University of Hong Kong, Shenzhen] [[Homepage](http://www.slai.edu.cn/zh-hans/teacher/208)] [[Paper](https://arxiv.org/abs/2508.14706)] [[Group](https://freedomintelligence.github.io/people/)] [[Code](https://github.com/FreedomIntelligence/ShizhenGPT)]

</details>


</details>

<details>
<summary>Guangxi (9)</summary>

<details>
<summary>Guangxi University of Chinese Medicine (5)</summary>

- **Xin Deng** Doctoral supervisor at Ruikang Clinical Medical College, Guangxi University of Chinese Medicine. Works on TCM for chronic liver disease and cancer, and on TCM artificial intelligence. [Ruikang Clinical Medical College, Guangxi University of Chinese Medicine] [[Admissions](https://www.gxtcmu.edu.cn/upload/yjsy/contentmanage/article/file/2025/11/25/%E5%B9%BF%E8%A5%BF%E4%B8%AD%E5%8C%BB%E8%8D%AF%E5%A4%A7%E5%AD%A62026%E5%B9%B4%E5%8D%9A%E5%A3%AB%E7%A0%94%E7%A9%B6%E7%94%9F%E6%8B%9B%E7%94%9F%E4%B8%93%E4%B8%9A%E7%9B%AE%E5%BD%95%EF%BC%88%E5%8F%91%E5%B8%83%E5%AE%98%E7%BD%91%EF%BC%89.pdf)]
- **Hua Zhu** Nanning. Doctoral and master's supervisor at Guangxi University of Chinese Medicine. Supervises image recognition, spectroscopy, and data-mining identification of Zhuang and Yao decoction pieces. [Guangxi University of Chinese Medicine] [[Homepage](https://www.gxtcmu.edu.cn/yjsy/dsdw1/sssds/1056zyxss/content_45370)]
- **Wenfang Ma** Nanning. Master's supervisor at Guangxi University of Chinese Medicine. Uses neural networks for spectrum-effect analysis of Zhuang medicines and sets quality standards for Zhuang and Yao medicines. [School of Pharmacy, Guangxi University of Chinese Medicine] [[Homepage](https://www.gxtcmu.edu.cn/yxy/kstd/zyjdjys/szdw11/content_47017)]
- **Zuliang Zhou** Nanning. Master's supervisor at Guangxi University of Chinese Medicine. Leads a Zhuang-medicine lexical corpus and collation of ancient Zhuang medical texts. [School of Basic Medical Sciences, Guangxi University of Chinese Medicine] [[Homepage](https://www.gxtcmu.edu.cn/jcyxy/jysjs/ygwjys/szdw8/content_47715)]
- **Ning Song** Nanning. Master's supervisor at Guangxi University of Chinese Medicine. Digitizes teaching of Zhuang visual diagnosis and mines famous doctors' herb use. [College of Zhuang Medicine, Guangxi University of Chinese Medicine] [[Homepage](https://www.gxtcmu.edu.cn/zyyxy/jysjs/zyjcjys/szdw1/content_46931)]

</details>

<details>
<summary>Guangxi International Zhuang Medicine Hospital (2)</summary>

- **Guodong Huang** Nanning. President and doctoral supervisor of Guangxi International Zhuang Medicine Hospital. The hospital runs a local model for checkup interpretation, AI tongue identification, and remote four-examination devices, and is building a Zhuang visual-diagnosis platform. [Guangxi International Zhuang Medicine Hospital] [[Homepage](https://www.gxtcmu.edu.cn/xwzx/xyxw/fsdw/content_89250)]
- **Hanru Huang** Nanning. Doctoral and master's supervisor at Guangxi International Zhuang Medicine Hospital. Leads the engineering research center for AI in Zhuang and Yao medicine. [Guangxi International Zhuang Medicine Hospital] [[Homepage](https://www.gxtcmu.edu.cn/msmy/myi/content_64198)]

</details>

<details>
<summary>Nanning Normal University (1)</summary>

- **Yuzhong Peng** Nanning. Professor and master's supervisor at Nanning Normal University. Applies intelligent computing and machine learning in biomedicine and joins Guangxi Chinese-medicine cross-innovation. [Nanning Normal University] [[Homepage](https://www.gxtcmu.edu.cn/yjsy/dsdw1/sssds/1053ggws/content_68640)]

</details>

<details>
<summary>First Affiliated Hospital of Guangxi University of Chinese Medicine (1)</summary>

- **Jinming Huang** Nanning. Master's supervisor at the First Affiliated Hospital of Guangxi University of Chinese Medicine. Co-leads the engineering research center for AI in Zhuang and Yao medicine. [First Affiliated Hospital of Guangxi University of Chinese Medicine] [[Homepage](https://www.gxtcmu.edu.cn/xwzx/xyxw/fsdw/content_14649)]

</details>


</details>

<details>
<summary>Hainan (1)</summary>

<details>
<summary>Hainan Medical University (1)</summary>

- **Aimin Gong** Haikou. Vice dean and doctoral and master's supervisor at Hainan Medical University. Uses machine vision and machine learning to build Chinese syndrome-diagnosis models. [Hainan Medical University] [[Homepage](https://www.muhn.edu.cn/zyxy/info/1412/8735.htm)]

</details>


</details>

<details>
<summary>Chongqing (4)</summary>

<details>
<summary>重庆中医药学院 (3)</summary>

- **张伟** Associate professor in the Medical Informatics teaching group at Chongqing College of Traditional Chinese Medicine; teaches foundations of TCM AI and works on TCM knowledge graphs and large language models. [[Homepage](https://www.cqctcm.edu.cn/tsxy/2023/1220/c820a2307/page.htm)]
- **叶华群** Senior engineer in the Medical Informatics teaching group at Chongqing College of Traditional Chinese Medicine; teaches foundations of smart medical language, with research in TCM big data and intelligent information processing. [[Homepage](https://www.cqctcm.edu.cn/tsxy/2023/1220/c820a2307/page.htm)]
- **王秋杰** Director of the Medical Informatics teaching group at Chongqing College of Traditional Chinese Medicine and a council member of the CACMS Information Society AI branch; teaches foundations of TCM AI and works on healthcare data analysis. [[Homepage](https://www.cqctcm.edu.cn/tsxy/2023/1220/c820a2307/page.htm)]

</details>

<details>
<summary>Southwest University (1)</summary>

- **Li Li** Professor and doctoral supervisor at Southwest University. Corresponding author of the TCM model TCM-R1. [College of Computer and Information Science, Southwest University] [[Homepage](https://cis.swu.edu.cn/info/1184/4082.htm)]

</details>


</details>

<details>
<summary>Sichuan (7)</summary>

<details>
<summary>Chengdu University of Traditional Chinese Medicine (7)</summary>

- **Chuanbiao Wen** Doctoral supervisor at Chengdu University of Traditional Chinese Medicine. His group builds high-quality datasets for TCM AI models and TCM AIGC; the dataset was selected for the national AI medical-device challenge. [Chengdu University of Traditional Chinese Medicine] [[Admissions](https://zyd.cdutcm.edu.cn/yjs/dsfc/bsyjsds)] [[News](https://www.cdutcm.edu.cn/info/1074/138321.htm)] [[Forum](https://www.cdutcm.edu.cn/info/1074/136241.htm)]
- **Wei Chen** Chair professor at Chengdu University of Traditional Chinese Medicine. His group released Bencao Zhiku, a large model covering the Chinese-medicine industrial chain, from genomes and ingredient–target links to knowledge graphs. [Chengdu University of Traditional Chinese Medicine] [[News](https://www.cdutcm.edu.cn/info/1080/4591.htm)]
- **Fang Zeng** Professor, doctoral supervisor, and president of Chengdu University of Traditional Chinese Medicine. Works on acupuncture effects and AI-assisted clinical decisions, including large models for acupoint combination. [Chengdu University of Traditional Chinese Medicine] [[Homepage](https://www.cdutcm.edu.cn/info/1004/1005.htm)] [[News](https://www.cdutcm.edu.cn/info/1075/138561.htm)]
- **Tao Jiang** Professor, doctoral supervisor, and dean of the School of Intelligent Medicine, Chengdu University of Traditional Chinese Medicine. Contributed to the Tianhui TCM model and intelligent TCM devices. [School of Intelligent Medicine, Chengdu University of Traditional Chinese Medicine] [[Paper](https://arxiv.org/abs/2509.19834)]
- **Dexian Wang** Associate professor and master's supervisor at Chengdu University of Traditional Chinese Medicine. Works on intelligent acupuncture prescription recommendation. [Chengdu University of Traditional Chinese Medicine] [[Homepage](https://www.ntu.edu.cn/2026/1008/c8083a300123/page.htm)]
- **Chunjie Wu** Researcher and doctoral supervisor at Chengdu University of Traditional Chinese Medicine. Digitally evaluates decoction-piece appearance and built an intelligent sensory-analysis platform. [School of Pharmacy, Chengdu University of Traditional Chinese Medicine] [[Homepage](https://www.cscsh.com/kj/198805.html)]
- **Yi Zhang** Chengdu. Doctoral supervisor at Chengdu University of Traditional Chinese Medicine. Leads a literature database covering Tibetan, Dai, Yi, and Miao medicine, and the team built a geographic platform for Tibetan medical classics. [Chengdu University of Traditional Chinese Medicine] [[Homepage](https://www.cdutcm.edu.cn/info/1080/52121.htm)] [[News](http://hgxy.hunnu.edu.cn/info/1175/5651.htm)]

</details>


</details>

<details>
<summary>Guizhou (13)</summary>

<details>
<summary>Guizhou University of Traditional Chinese Medicine (10)</summary>

- **Quan Xie** Executive dean and professor of the School of Information Engineering, Guizhou University of Traditional Chinese Medicine. Leads full-chain TCM corpora for vertical models. [School of Information Engineering, Guizhou University of Traditional Chinese Medicine] [[Homepage](https://xxgc.gzy.edu.cn/info/1289/3160.htm)]
- **Chenggang Hu** Guiyang. Master's supervisor and vice dean of the Miao Medicine Institute at Guizhou University of Traditional Chinese Medicine. Led digitization of the specimen hall and a Guizhou medicinal-resource database. [School of Pharmacy, Guizhou University of Traditional Chinese Medicine] [[Homepage](https://yaoxue.gzy.edu.cn/info/1458/3599.htm)]
- **Hong Jiang** Guiyang. Master's supervisor at Guizhou University of Traditional Chinese Medicine. Teaches Miao pharmacy and advises the Miao-medicine AI project Miaohui Zhiyun. [School of Pharmacy, Guizhou University of Traditional Chinese Medicine] [[Homepage](https://yaoxue.gzy.edu.cn/info/1383/3020.htm)]
- **Wenbo Cheng** Guiyang. Master's supervisor at Guizhou University of Traditional Chinese Medicine. Recruits in artificial intelligence and advises the Miao-medicine AI project Miaohui Zhiyun. [School of Information Engineering, Guizhou University of Traditional Chinese Medicine] [[Homepage](https://yjs.gzy.edu.cn/info/2034/2631.htm)]
- **Yun Zhang** Guiyang. Master's supervisor at Guizhou University of Traditional Chinese Medicine. Uses machine learning on noncoding RNA and deep learning on medicinal-plant small RNA. [Guizhou University of Traditional Chinese Medicine] [[Homepage](https://xxgc.gzy.edu.cn/info/1196/1464.htm)]
- **Hongguan Jiao** Guiyang. Master's supervisor at Guizhou University of Traditional Chinese Medicine. Joins international Chinese-medicine information standards and analysis of Miao medical literature. [Guizhou University of Traditional Chinese Medicine] [[Homepage](https://xxgc.gzy.edu.cn/info/1196/1464.htm)]
- **Qiaoqiao Xiao** Guiyang. Master's supervisor at Guizhou University of Traditional Chinese Medicine. Builds gene-function databases of medicinal plants with bioinformatics. [School of Pharmacy, Guizhou University of Traditional Chinese Medicine] [[Homepage](https://yaoxue.gzy.edu.cn/info/1458/3695.htm)]
- **Zhenghong Guo** Guiyang. Master's supervisor at Guizhou University of Traditional Chinese Medicine. Uses computation and bioinformatics to analyze active constituents of Miao and other ethnic medicines. [School of Pharmacy, Guizhou University of Traditional Chinese Medicine] [[Homepage](https://yaoxue.gzy.edu.cn/info/1458/3571.htm)]
- **Renmin Wang** Guiyang. Associate professor and master's supervisor at Guizhou University of Traditional Chinese Medicine. Recruits in electronic information and artificial intelligence. [Guizhou University of Traditional Chinese Medicine] [[Homepage](https://yjs.gzy.edu.cn/info/2034/2631.htm)]
- **Guangying Du** Guiyang. Master's supervisor at Guizhou University of Traditional Chinese Medicine. Recruits in artificial intelligence and medicinal resources, and joins knowledge-graph analysis of Miao medicine. [Guizhou University of Traditional Chinese Medicine] [[Homepage](https://yjs.gzy.edu.cn/info/2034/2631.htm)]

</details>

<details>
<summary>Guizhou Medical University (2)</summary>

- **Lei Tang** Party secretary of Guizhou Medical University and executive director of the national key laboratory for bioactive constituents of Chinese medicine. Led the release of the ethnic-medicine model Huazu Bencao. [Guizhou Medical University] [[News](https://www.stdaily.com/web/gdxw/2026-08/03/content_558608.html)]
- **Ningxian Yang** Guiyang. Young doctoral supervisor at Guizhou Medical University. Uses artificial intelligence to evaluate antimicrobial peptides and develops distinctive food-medicine resources. [Guizhou Medical University] [[Homepage](https://fnh.gmc.edu.cn/info/1006/2194.htm)]

</details>

<details>
<summary>Guiyang Daosheng Health Industry (1)</summary>

- **Jianfeng Zhang** Guiyang. Researcher at Guiyang Daosheng Health Industry and master's supervisor at Guizhou University of Traditional Chinese Medicine. Evaluates processing quality of Chinese and ethnic medicines and does network analysis. [Guiyang Daosheng Health Industry] [[Homepage](https://yaoxue.gzy.edu.cn/info/1458/3562.htm)]

</details>


</details>

<details>
<summary>Yunnan (9)</summary>

<details>
<summary>Yunnan University of Chinese Medicine (6)</summary>

- **Peixin Guo** Professor and doctoral supervisor at Yunnan University of Chinese Medicine. Uses AI, scientific computing, and multi-omics for secondary development of classical formulas. [Yunnan University of Chinese Medicine] [[Homepage](https://www.ynucm.edu.cn/info/1045/178391.htm)]
- **Chao Zhang** Kunming. Doctoral supervisor at Yunnan University of Chinese Medicine. At the provincial key laboratory for Dai and Yi medicine, he is responsible for literature, empirical-formula, and hospital-preparation databases. [Yunnan University of Chinese Medicine] [[Homepage](https://dym.ynucm.edu.cn/info/1011/1049.htm)]
- **Zigang Qian** Kunming. Doctoral supervisor at Yunnan University of Chinese Medicine. Built a DNA-barcode identification database and website for Dai and Yi medicinal materials. [Yunnan University of Chinese Medicine] [[Homepage](https://dym.ynucm.edu.cn/info/1011/1049.htm)]
- **Weibo Wen** Kunming. Professor and doctoral and master's supervisor at Yunnan University of Chinese Medicine. Uses data mining for clinical cohorts and develops ethnic medicines. [Yunnan University of Chinese Medicine] [[Homepage](https://mbfzsys.ynucm.edu.cn/info/1020/1049.htm)]
- **Yanqiu Luo** Kunming. Master's supervisor at Yunnan University of Chinese Medicine. Compiled catalogs of Yi and Dai medical classics and leads rescue of Yi medical texts. [Yunnan University of Chinese Medicine] [[Homepage](https://dym.ynucm.edu.cn/info/1013/1167.htm)]
- **Qinghua Chen** Kunming. Master's supervisor at Yunnan University of Chinese Medicine and a reserve lead in Dai medicine. Joined the Dai disease-syndrome classification codes and clinical terminology. [Yunnan University of Chinese Medicine] [[Homepage](https://dym.ynucm.edu.cn/info/1013/1167.htm)]

</details>

<details>
<summary>Yunnan Baiyao Group (3)</summary>

- **Wuzhou Wan** President of the central research institute at Yunnan Baiyao. Speaks on AI-enabled research from innovative drugs to intelligent Chinese medicine. [Yunnan Baiyao Group] [[Homepage](https://www.yunnanbaiyao.com.cn/view/ynbyPc/1/92/view/9201.html)]
- **Shaochun Li** Digital strategy scientist, general manager of the digital-technology company, and chief information officer at Yunnan Baiyao. Leads the Leigong Chinese-medicine model. [Yunnan Baiyao Group] [[News](http://www.datayuan.cn/article/22489.htm)]
- **Qiqiang Fan** Lead at Yunnan Baiyao Digital Technology. Works on lighthouse-factory digitization and Industry 4.0 upgrades. [Yunnan Baiyao Group] [[Homepage](https://www.yunnanbaiyao.com.cn/view/ynbyPc/1/92/view/8368.html)]

</details>


</details>

<details>
<summary>Tibet (3)</summary>

<details>
<summary>Tibet University (3)</summary>

- **Yongcuo** Lhasa. Doctoral and master's supervisor at Tibet University. Extracts entity relations from Tibetan-medicine literature for knowledge graphs. [School of Information Science and Technology, Tibet University] [[Homepage](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-5-860.html)]
- **Nima Zhaxi** Lhasa. Doctoral and master's supervisor at Tibet University. Joins relation extraction from Tibetan-medicine literature and digitization of Tibetan classical texts. [School of Information Science and Technology, Tibet University] [[Admissions](http://static.hhkaobo.com/upload/editor/fd7e90b8-9745-4ca6-97cc-d7fd16d332d2.pdf)]
- **Sicen Wang** Lhasa. Doctoral supervisor at Tibet University. With Minzu University of China, uses AI models to screen anti-fibrotic Tibetan medicines. [Tibet University] [[Homepage](https://www.muc.edu.cn/info/1052/36678.htm)]

</details>


</details>

<details>
<summary>Shaanxi (3)</summary>

<details>
<summary>Shaanxi University of Chinese Medicine (2)</summary>

- **Yongyi Wen** Professor and master's supervisor at Shaanxi University of Chinese Medicine. Works on digitizing TCM literature, knowledge graphs, information extraction, and language models. [Shaanxi University of Chinese Medicine] [[Homepage](http://yzb.sntcm.edu.cn/xjsds/rwglhy/0453gjzwjy/113981.htm)]
- **Ying Hou** Xianyang. Master's supervisor at Shaanxi University of Chinese Medicine. Works on intelligent health care and Chinese-medicine management. [Shaanxi University of Chinese Medicine] [[Homepage](http://yzb.sntcm.edu.cn/xjsds/rwglhy/1005z2zylglh/113986.htm)]

</details>

<details>
<summary>Northwest University (1)</summary>

- **Yonghua Wang** Professor at the bioinformatics center of Northwest University. Built the traditional Chinese medicine systems pharmacology database TCMSP. [Northwest University] [[Homepage](https://life.nwafu.edu.cn/yjsjy/yjsgl/070cf28723284d418f42b14c1175437b.htm)]

</details>


</details>

<details>
<summary>Gansu (2)</summary>

<details>
<summary>Gansu University of Chinese Medicine (1)</summary>

- **Xiaojie Jin** Lanzhou. Associate professor and doctoral supervisor at Gansu University of Chinese Medicine. Works on Chinese-medicine cheminformatics and computer-aided drug discovery. [School of Pharmacy, Gansu University of Chinese Medicine] [[Homepage](https://yxx.gszy.edu.cn/html/cid/83.html?page=1)]

</details>

<details>
<summary>Gansu Provincial Hospital of Traditional Chinese Medicine (1)</summary>

- **Zhiming Zhang** Lanzhou. President and doctoral supervisor at Gansu Provincial Hospital of Traditional Chinese Medicine. Advances digital tongue diagnosis and AI-assisted inspection. [Gansu Provincial Hospital of Traditional Chinese Medicine] [[Homepage](https://xxxy.xzhmu.edu.cn/info/1005/2985.htm)]

</details>


</details>

<details>
<summary>Qinghai (2)</summary>

<details>
<summary>Qinghai University (2)</summary>

- **Ze Zhou** Xining. Master's supervisor at the College of Tibetan Medicine, Qinghai University. Leads a Tibetan medicinal-plant image library and a Tibetan-formula database. [College of Tibetan Medicine, Qinghai University] [[Homepage](https://zyxy.qhu.edu.cn/szdw/qnjstd/29957.htm)]
- **Duojie** Xining. Master's supervisor at the College of Tibetan Medicine, Qinghai University. Joins digitization of Tibetan medical literature and deep processing of classical texts. [College of Tibetan Medicine, Qinghai University] [[Homepage](https://zyxy.qhu.edu.cn/kxyj/yjxm/27856.htm)]

</details>


</details>

<details>
<summary>Ningxia (3)</summary>

<details>
<summary>Ningxia Medical University (3)</summary>

- **Wenxue Zhang** Yinchuan. Master's supervisor at Ningxia Medical University. Works on Chinese-medicine informatics, formula data mining, and medical knowledge graphs. [Ningxia Medical University] [[Homepage](https://www.nxmu.edu.cn/lxy/info/1051/1123.htm)]
- **Deren Yang** Yinchuan. Master's supervisor at Ningxia Medical University. Works on Chinese-medicine informatics. [Ningxia Medical University] [[Homepage](https://www.nxmu.edu.cn/lxy/info/1051/1122.htm)]
- **Yaogeng Chen** Yinchuan. Master's supervisor at Ningxia Medical University. Works on medical data mining and teaches Chinese-medicine informatics. [Ningxia Medical University] [[Homepage](https://www.nxmu.edu.cn/lxy/info/1051/1120.htm)]

</details>


</details>

<details>
<summary>Xinjiang (3)</summary>

<details>
<summary>Xinjiang Medical University (2)</summary>

- **Murat Hamit** Urumqi. Master's supervisor at Xinjiang Medical University. Built data-mining diagnosis for Uyghur abnormal-humor disease, a Uyghur-herb image library, and image classification for Kazakh esophageal cancer. [College of Medical Engineering, Xinjiang Medical University] [[Homepage](http://school.freekaoyan.com/xj/xjmu/zhuanye/2016/01-31/1454243071480819.shtml)]
- **Chuanbo Yan** Urumqi. Associate professor and master's supervisor at Xinjiang Medical University. Works on Uyghur-herb image retrieval and SVM and neural-network classification of Kazakh esophageal-cancer images. [College of Medical Engineering, Xinjiang Medical University] [[Homepage](https://xjyy.cbpt.cnki.net/portal/journal/portal/client/paper/a87ac666d8ff75c2aa5aa85b3c52f76d)]

</details>

<details>
<summary>Xinjiang University (1)</summary>

- **Jingjing Xia** Urumqi. Master's supervisor at Xinjiang University. Uses mid-infrared spectroscopy and chemometrics to assess chicory seed used in Uyghur medicine, with machine learning and convolutional networks in the research direction. [College of Pharmacy, Xinjiang University] [[Homepage](https://imm.xju.edu.cn/info/1059/1372.htm)]

</details>


</details>

<details>
<summary>Hong Kong (9)</summary>

<details>
<summary>Hong Kong Baptist University (5)</summary>

- **Aiping Lyu** Vice president of Hong Kong Baptist University and chair professor in the School of Chinese Medicine. Works on TCM translation and systems medicine, and on combining TCM with artificial intelligence and data science. [School of Chinese Medicine, Hong Kong Baptist University] [[Homepage](https://endowed-professorships.hkbu.edu.hk/zh-hk/endowed-professors/professor-lyu-aiping.html)] [[News](https://jumc.jju.edu.cn/info/1049/6997.htm)]
- **Ge Zhang** Chair professor and associate dean at the School of Chinese Medicine, Hong Kong Baptist University. Leads AI-driven aptamer discovery. [School of Chinese Medicine, Hong Kong Baptist University] [[Homepage](https://scholars.hkbu.edu.hk/en/persons/ZHANGGE/)]
- **Liang Tian** Associate professor of physics at Hong Kong Baptist University. Works on TCM data mining and AI platforms for network pharmacology and quality control. [Hong Kong Baptist University] [[Homepage](https://scholars.hkbu.edu.hk/en/persons/LIANGTIAN/)]
- **Lu Zhang** Professor at Hong Kong Baptist University. Builds a biomedical AI agent for Chinese-medicine treatment of gastrointestinal cancer. [Hong Kong Baptist University] [[Homepage](https://research.hkbu.edu.hk/sc/1-1-1-scheme/projects)]
- **Furong Zhu** Professor at Hong Kong Baptist University. Uses near-infrared spectroscopy and AI to identify the authenticity and quality of Chinese medicinal materials. [Hong Kong Baptist University] [[Homepage](https://research.hkbu.edu.hk/sc/1-1-1-scheme/projects)]

</details>

<details>
<summary>The Chinese University of Hong Kong (2)</summary>

- **Guoliang Xing** Professor of information engineering at The Chinese University of Hong Kong. His team built OpenTCM, a graph-retrieval model for TCM knowledge and diagnosis. [The Chinese University of Hong Kong] [[News](https://www.ie.cuhk.edu.hk/prof-guoliang-xing-and-prof-hongkai-chens-team-win-best-paper-award-at-bigcom-2025-for-innovative-traditional-chinese-medicine-ai-system/)]
- **陈鸿凯** Research Assistant Professor in Information Engineering at CUHK and a corresponding author of OpenTCM, a GraphRAG-based TCM knowledge retrieval and diagnosis system. [[Homepage](https://www.ie.cuhk.edu.hk/faculty/chen-hongkai/)] [[Paper](https://arxiv.org/abs/2504.20118)]

</details>

<details>
<summary>The University of Hong Kong (2)</summary>

- **Jiangang Shen** Professor in the School of Chinese Medicine, The University of Hong Kong. Uses AI to recognize TCM pulse patterns and their links to constitution. [School of Chinese Medicine, The University of Hong Kong] [[Homepage](https://eventregscm.hku.hk/Views/People/ProfessorJiangangShen.html)]
- **Yibin Feng** Professor and director of the School of Chinese Medicine, The University of Hong Kong. Uses network pharmacology, omics, and AI to study TCM treatment principles. [School of Chinese Medicine, The University of Hong Kong] [[Homepage](https://www.med.hku.hk/en/teaching-and-learning/postgraduate/rpg/projects/ai-assisted-investigation-to-understand-the-treatment-principle-of-chinmed)]

</details>


</details>

<details>
<summary>Macao (4)</summary>

<details>
<summary>University of Macau (2)</summary>

- **Jiahong Lu** Associate professor and associate dean of the Institute of Chinese Medical Sciences, University of Macau. Uses AI to screen Chinese-medicine molecules against Alzheimer's disease. [Institute of Chinese Medical Sciences, University of Macau] [[News](https://www.um.edu.mo/zh-hant/news-and-press-releases/presss-release/detail/63849/)]
- **Yuanjia Hu** Professor at the Institute of Chinese Medical Sciences, University of Macau. Uses network pharmacology to identify quality-control markers of Chinese medicines and neural networks to generate molecular libraries. [Institute of Chinese Medical Sciences, University of Macau] [[Homepage](https://repository.um.edu.mo/profile/yuanjiahu)]

</details>

<details>
<summary>Macau University of Science and Technology (2)</summary>

- **Zitian Han** Professor at Macau University of Science and Technology. Corresponding author of TCM-DS, a model for medicinal-and-edible formula recommendation. [Macau University of Science and Technology] [[Homepage](https://fie.must.edu.mo/id-848/person/view/id-448.html)]
- **Ting Li** Professor at the State Key Laboratory of Quality Research in Chinese Medicines, Macau University of Science and Technology, and vice dean of its institute for interdisciplinary AI. Applies artificial intelligence to Chinese-medicine mechanisms and drug discovery. [Macau University of Science and Technology] [[Profile](https://wm-fs2.must.edu.mo/group1/M00/0B/62/rBCDo2ohKsOAL4esAAMyNfTO-Ng912.pdf)]

</details>


</details>

<details>
<summary>Taiwan (7)</summary>

<details>
<summary>China Medical University (3)</summary>

- **Lun-Chien Lo** Professor of Chinese medicine diagnostics at China Medical University and chair of the Taiwan Association of Chinese Medical Diagnostics. [School of Chinese Medicine, China Medical University] [[Homepage](http://webap.cmu.edu.tw/TchEportfolio/index_1/lclo)]
- **Hen-Hong Chang** Professor of Chinese medicine diagnostics at China Medical University. Works on instruments that assist traditional Chinese diagnosis. [School of Chinese Medicine, China Medical University] [[Homepage](https://webap.cmu.edu.tw/TchEportfolio/index_1/tcmchh55)]
- **Sheng-Teng Huang** Professor and chair of the School of Chinese Medicine at China Medical University, and director of the Chinese medicine department at its hospital. Develops AI for clinical teaching in Chinese medicine. [School of Chinese Medicine, China Medical University] [[Homepage](http://webap.cmu.edu.tw/TchEportfolio/index_1/sthuang)] [[News](https://chmed.cmu.edu.tw/news/293/)]

</details>

<details>
<summary>Chang Gung University (3)</summary>

- **Sien-Hung Yang** Professor and chair of traditional Chinese medicine at Chang Gung University. Collaborates with electrical engineering on deep-learning tongue segmentation and constitution identification. [School of Traditional Chinese Medicine, Chang Gung University] [[Homepage](https://pure.lib.cgu.edu.tw/en/persons/sien-hung-yang)]
- **Jiann-Der Lee** Professor of electrical engineering at Chang Gung University. Uses deep learning for tongue segmentation, constitution identification, and depression screening from tongue images. [Department of Electrical Engineering, Chang Gung University] [[Homepage](https://pure.lib.cgu.edu.tw/en/persons/jiann-der-lee-3/)]
- **Geng-Hao Liu** Assistant professor and director of the premedical program in traditional Chinese medicine at Chang Gung University. Specializes in pulse diagnosis, acupuncture, and Chinese medical diagnosis. [School of Traditional Chinese Medicine, Chang Gung University] [[Homepage](https://pure.lib.cgu.edu.tw/en/persons/geng-hao-liu-2)]

</details>

<details>
<summary>National Dong Hwa University (1)</summary>

- **Shijing Yan** Professor and head of the Artificial Intelligence Laboratory in computer science at National Dong Hwa University. Works with Tzu Chi Hospital on deep-learning analysis of tongue images and pulse signals. [Department of Computer Science and Information Engineering, National Dong Hwa University] [[News](https://www.csie.ndhu.edu.tw/uncategorized/csie_ai_in_chinese_medicine_ch/)]

</details>


</details>

<details>
<summary>Japan (3)</summary>

<details>
<summary>Chiba University (2)</summary>

- **Toshiya Nakaguchi** Professor and deputy director of the Center for Frontier Medical Engineering at Chiba University. Works on medical image analysis and computer-aided diagnosis, and takes part in Kampo tongue-image research. [Center for Frontier Medical Engineering, Chiba University] [[Homepage](https://www.cfme.chiba-u.jp/en/staff/detail.php?index=nakaguchi)] [[Forum](https://www.m.chiba-u.jp/class/wakan/tongue2021/)]
- **Takao Namiki** Specially appointed professor at Chiba University. Leads Kampo tongue-image research and work toward tongue-diagnosis standards. [Chiba University] [[Homepage](https://www.m.chiba-u.jp/class/wakan/outline/staff.html)] [[Forum](https://www.m.chiba-u.jp/class/wakan/tongue2021/)]

</details>

<details>
<summary>Kitasato University Kitasato Institute Hospital (1)</summary>

- **Tadaaki Kawanabe** Deputy director at Kitasato University Kitasato Institute Hospital. Uses machine learning to quantify Kampo tongue findings and built a tongue-image database of healthy subjects. [Kitasato University Kitasato Institute Hospital] [[Homepage](https://nrid.nii.ac.jp/en/nrid/1000040445523/)]

</details>


</details>

<details>
<summary>Korea (5)</summary>

<details>
<summary>Wonkwang University (2)</summary>

- **Won-Yung Lee** Professor at Wonkwang University College of Korean Medicine. Works on herbal network pharmacology and an AI model that predicts interactions between herbal and chemical drugs. [College of Korean Medicine, Wonkwang University] [[News](https://www.wku.ac.kr/%ec%9d%b4%ec%9b%90%ec%9c%b5-%ea%b5%90%ec%88%98-%ec%97%b0%ea%b5%ac%ed%8c%80-%ed%95%9c%ec%95%bd-%ed%95%a9%ec%84%b1%ec%9d%98%ec%95%bd%ed%92%88-%ec%83%81%ed%98%b8%ec%9e%91%ec%9a%a9-%ec%98%88%ec%b8%a1-ai.html)]
- **Jungtae Leem** Researcher at Wonkwang University College of Korean Medicine. Studies how pulse-diagnosis devices are used in teaching Korean medical diagnostics. [College of Korean Medicine, Wonkwang University] [[Paper](https://jkom.org/journal/view.php?number=5266)]

</details>

<details>
<summary>Kyung Hee University (2)</summary>

- **Yeon-Cheol Park** Associate professor of acupuncture at Kyung Hee University College of Korean Medicine. Leads a Korean-medicine omics and AI lab using big data and machine learning for diagnosis. [College of Korean Medicine, Kyung Hee University] [[Homepage](https://kmoa.khu.ac.kr/members)]
- **Yeonhak Kim** Adjunct professor at Pusan National University School of Korean Medicine and research fellow at Kyung Hee University. Applies multi-omics and artificial intelligence to Korean medicine. [Pusan National University School of Korean Medicine, Kyung Hee University] [[Homepage](https://kmoa.khu.ac.kr/members)]

</details>

<details>
<summary>Daegu Gyeongbuk Institute of Science and Technology (1)</summary>

- **Chang-Eop Kim** Associate professor at Daegu Gyeongbuk Institute of Science and Technology. Uses machine learning to formalize Korean-medicine theory and studies herbal network pharmacology. [Daegu Gyeongbuk Institute of Science and Technology] [[Homepage](https://scholar.dgist.ac.kr/researcher/0b0c2fa5-3add-421e-95cc-aeb8f8beb679)]

</details>


</details>

<details>
<summary>Singapore (1)</summary>

<details>
<summary>National University of Singapore (1)</summary>

- **Yu Zong Chen** Tenured professor of pharmacy at the National University of Singapore. Maintains the TCM-ID Chinese medicine database and uses machine learning to study herbal medicines. [Department of Pharmacy, National University of Singapore] [[Homepage](https://bidd.group/)]

</details>


</details>

<details>
<summary>United States (1)</summary>

<details>
<summary>University of Missouri (1)</summary>

- **Dong Xu** Professor at the University of Missouri. Uses deep learning to analyze tongue images and released the multimodal Chinese-medicine benchmark TCM-Ladder. [University of Missouri] [[Homepage](https://bondlsc.missouri.edu/labs/dong-xu/)]

</details>


</details>

<details>
<summary>Australia (1)</summary>

<details>
<summary>Western Sydney University (1)</summary>

- **Xian Zhou** Senior research fellow at the NICM Health Research Institute, Western Sydney University. Uses machine learning to characterize synergy and antagonism among herbal bioactive molecules, and supervises graduate students. [NICM Health Research Institute, Western Sydney University] [[Homepage](https://researchers.westernsydney.edu.au/en/persons/phoebe-zhou/)]

</details>


</details>

<details>
<summary>Other (5)</summary>

<details>
<summary>TCM Online (2)</summary>

- **Jian He** Founder and CEO of TCM Online. Built the Yiyin TCM model from a decade of master-physician course data. [TCM Online] [[News](https://www.vbdata.cn/1519007974)]
- **Yi Ren** Chief technology officer of TCM Online. Leads deployment and fine-tuning of the TCM model. [TCM Online] [[News](https://www.vbdata.cn/1519007974)]

</details>

<details>
<summary>南洋理工大学 (1)</summary>

- **Christopher Khoo** Associate professor at NTU's Wee Kim Wee School of Communication and Information; leads the Polyglot Asian Medicine Knowledge Graph of traditional and herbal medicines in maritime Southeast Asia. [[Homepage](https://blogs.ntu.edu.sg/chriskhoo/2023/06/polyglot-medicine-knowledge-graph/)] [[Link](https://kgraph.sg/polyglot/)] [[Paper](https://doi.org/10.1007/978-981-99-8088-8_1)]

</details>

<details>
<summary>Andun Health (1)</summary>

- **Weimin Bai** Founder and chairman of Andun Health. Released the seven-diagnosis TCM robot and a TCM language model. [Andun Health] [[News](https://www.xinhuanet.com/finance/20260720/f6a8625c1be4412d9c311a232c7a35fa/c.html)]

</details>

<details>
<summary>Zhifu Qihuang (1)</summary>

- **Kun Li** Founder and chairman of Zhifu Qihuang. Leads four-diagnosis devices and the Tiangong TCM model. [Zhifu Qihuang] [[News](http://business.china.com.cn/2025-12/16/content_43307776.shtml)]

</details>


</details>

## Open models

The table above is a shortlist. Expand the folds for public checkpoints, paper-only models, general Chinese medical bases, closed products, and Kampo/Korean-medicine work.

<details>
<summary>Public weights (21)</summary>

| Model | Year | Org | Focus | Links |
| --- | :---: | --- | --- | --- |
| **ZhiFangDanTai** | 2026 | Capital Normal University | RAG · KG | [Paper](https://arxiv.org/abs/2509.05867) · [Weights](https://huggingface.co/tczzx6/ZhiFangDanTai1.0) · [Data](https://huggingface.co/datasets/tczzx6/ZhiFangDanTai1.0) |
| **Lingdan-V2** | 2026 | Beijing Jiaotong University | Rx · Reason | [Paper](https://arxiv.org/abs/2610.14705) · [Weights](https://huggingface.co/TCMLLM/Lingdan-8B-R1) · [Code](https://github.com/TCMAI-BJTU/Lingdan-V2) |
| **Xinghe** | 2026 | Xinghe-TCM | Reason · Classics | [Weights](https://huggingface.co/zsyjsld/Xinghe1.2-9B) · [Data](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2) |
| **仲景 (ZhongJing)** | 2026 | — | ZhongJingGPT is an expert-knowledge-… | [Paper](https://doi.org/10.26599/TST.2025.9010046) · [Weights](https://huggingface.co/CMLM/ZhongjingGPT1_13B) · [Code](https://github.com/pariskang/CMLM-ZhongJing) |
| **中医体质 Qwen3-8B 量化权重** | 2026 | — | Quantized Qwen3-8B weights for tradi… | [Weights](https://huggingface.co/chenhaodev/tcm-constitution-qwen3-8b-gguf) |
| **TCM-Qwen3.5-9B-SFT-R2** | 2026 | Xxiao2023 (Hugging Face) | Reason | [Weights](https://huggingface.co/Xxiao2023/TCM-Qwen3.5-9B-SFT-R2) |
| **TCM-Qwen2.5-7B-SFT** | 2026 | — | A traditional Chinese medicine super… | [Weights](https://huggingface.co/Xxiao2023/TCM-Qwen2.5-7B-SFT-V1) |
| **Qwen3.5-9B 中医继续预训练** | 2026 | — | Full weights after continued pretrai… | [Weights](https://huggingface.co/arthur789/qwen3.5-9b-tcm-cpt) |
| **MiMo-9B-TCM-Andrology-LoRA** | 2026 | johnson (Hugging Face) | Rx | [Weights](https://huggingface.co/johnson/MiMo-9B-TCM-Andrology-LoRA) · [Data](https://huggingface.co/datasets/johnson/TCM-Andrology-EMR) |
| **Fu-TCM-9B** | 2026 | fudanxai (Hugging Face account) | The fudanxai account hosts 9.41B BF1… | [Weights](https://huggingface.co/fudanxai/Fu-TCM-9B) · [Data](https://huggingface.co/datasets/fudanxai/Fu_TCM) |
| **Fu-TCM-27B** | 2026 | — | MM | [Paper](https://arxiv.org/abs/2610.38333) · [Weights](https://huggingface.co/fudanxai/Fu-TCM-27B) · [Data](https://huggingface.co/datasets/fudanxai/Fu_TCM) |
| **Baize-TCM-LLM** | 2025 | Institute of Chinese Materia Medica | ICMM Baize TCM QA models on Qwen3 (0… | [Weights](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model) · [Data](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3) |
| **BianCang** | 2025 | Qilu University of Technology | BianCang TCM LLM series (IEEE JBHI)… | [Paper](https://arxiv.org/abs/2411.11027) · [Weights](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct) · [Code](https://github.com/QLU-NLP/BianCang) |
| **ViTCM-LLM** | 2025 | Tsinghua Shenzhen International Graduate School | MM · RAG | [Paper](https://doi.org/10.1109/bibm66473.2025.11357113) · [Weights](https://huggingface.co/Mark-CHAE/ViTCM-LLM) · [Code](https://github.com/jw-chae/ViTCM_LLM) |
| **TCM-VisResolve (TCM-VR)** | 2025 | Yunnan Minzu University | MM | [Paper](https://doi.org/10.1109/BIBM66473.2025.11356679) · [Weights](https://huggingface.co/dylanyang963/TCM-VR) |
| **ShizhenGPT** | 2025 | The Chinese University of Hong Kong | MM | [Paper](https://arxiv.org/abs/2508.14706) · [Weights](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni) · [Code](https://github.com/FreedomIntelligence/ShizhenGPT) |
| **TCMLLM / Lingdan** | 2024 | Beijing Jiaotong University | TCMLLM / Lingdan for TCM modeling an… | [Paper](https://doi.org/10.1016/j.dcmed.2025.01.007) · [Weights](https://huggingface.co/TCMLLM/Lingdan-13B-Base) · [Code](https://github.com/2020MEAI/TCMLLM) |
| **TCMChat** | 2024 | — | Generative TCM LLM built via pre-tra… | [Paper](https://doi.org/10.1016/j.phrs.2024.107530) · [Weights](https://huggingface.co/ZJUFanLab/TCMChat-600k) · [Code](https://github.com/ZJUFanLab/TCMChat) · [Data](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k) |
| **MedChatZH** | 2024 | — | Baichuan-7B adapted for TCM consulta… | [Paper](https://doi.org/10.1016/j.compbiomed.2024.108290) · [Code](https://github.com/tyang816/MedChatZH) · [Weights](https://huggingface.co/tyang816/medchatzh) · [Data](https://huggingface.co/datasets/tyang816/MedChatZH) |
| **ChatTCM** | 2024 | — | SylvanL open TCM LLM (Qwen2-7B conti… | [Weights](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain) |
| **神农大模型 (ShenNong-TCM-LLM)** | 2023 | — | ShenNong-TCM-LLM, the first TCM larg… | [Weights](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM) · [Code](https://github.com/michael-wzhu/ShenNong-TCM-LLM) · [Data](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset) |

</details>

<details>
<summary>Paper or product only, no verified weights (50)</summary>

<details>
<summary>2026 · 15</summary>

- [*Digital Chinese Medicine*] **QingNangTCM** GLM-4-9B-Chat adapted with P-Tuning v2 for TCM question answering and clinical reasoning; trained with the 100,000-entry QnTCM_Dataset. [Hebei North University] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.002)]
- [*ISCTIS 2026*] **Tongue–face multimodal fusion diagnosis** Tongue–face multimodal feature fusion with LLM-driven intelligent TCM diagnosis. [Xiamen University of Technology] [[DOI](https://doi.org/10.1109/ISCTIS70043.2026.11572361)]
- **砭石云中医** Bianshi Yun Zhongyi is Wisdom Eye's TCM application on its filed multimodal Bianshi model, using a symptom-to-formula knowledge graph for four-diagnostic capture and decision support. [[Website](https://www.a-eye.cn/news_list/420.html)] [[Website](https://www.a-eye.cn/news_list/356.html)]
- **岐元** Qiyuan is the Seventh People's Hospital of Shanghai's TCM model, trained with pretraining, domain fine-tuning, and expert reinforcement learning, for generative records and famous-doctor agent twins. [[News](https://finance.sina.com.cn/jjxw/2026-07-26/doc-inikassr0678770.shtml)]
- [*Information Fusion*] **Tianyi** 7.6-billion-parameter TCM LLM from NJUCM et al. with reading–clinic–apprenticeship training stages, TCMEval, and real-world validation (Information Fusion, February 2026). [Nanjing University of Chinese Medicine] [[Published](https://doi.org/10.1016/j.inffus.2025.103663)] [[Paper](https://arxiv.org/abs/2505.13156)] [[News](https://blog.sciencenet.cn/blog-279293-1501581.html)]
- **华族本草** Huazu Bencao is an ethnic-medicine model led by Guizhou Medical University, using Shuzhi Qihuang and Qwen to connect multi-ethnic classics and a knowledge graph across ingredient screening, formulation, quality control, and teaching. [[Website](https://www.gmc.edu.cn/info/1059/30300.htm)] [[News](https://www.news.cn/tech/20260804/f973d6fa9de640328fec0194c63335a3/c.html)]
- [*JMIR Medical Informatics*] **TongueVLM** Multimodal VLM for TCM tongue diagnosis, description generation, and constitution reasoning. JMIR page blocked; OpenAlex lists HFUT and Anhui University of Chinese Medicine et al. [Hefei University of Technology, Anhui University of Chinese Medicine et al.] [[Paper](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- [*APWeb-WAIM 2025*] **TCM-R1** TCM LLM with GRPO-enhanced reasoning. [Southwest University] [[Paper](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*世界科学技术-中医药现代化*] **TCM Classic-Translator（中医古籍今译）** TCM Classic-Translator is a LoRA model for classical-to-modern TCM translation, trained on Huangdi Neijing and Shanghan Lun parallels with commentary augmentation. BLEU-4, ROUGE-1, ROUGE-2, and ROUGE-L are 39.3534, 55.0474, 35.8099, and 54.6551. [[DOI](https://doi.org/10.11842/wst.20250916005)]
- [*Digital Chinese Medicine*] **Qwen-TCM-Dia** Qwen2.5-based model for TCM diarrhea care, using two-stage LoRA for continued domain pretraining and chain-of-thought instruction tuning across symptoms, pathogenesis, treatment principles, and prescriptions. [Beijing Hospital of TCM, Capital Medical University, Beijing University of Chinese Medicine et al.] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.003)]
- [*arXiv*] **Med-Shicheng** Extends Tianyi's staged training approach on Qwen2.5-1.5B-Base with continued pretraining, supervised fine-tuning, and KTO; models five physicians' expertise across seven tasks. [Nanjing University of Chinese Medicine et al.] [[Paper](https://arxiv.org/abs/2603.23520)] [[Code](https://github.com/NJUCM-BJUCM-TCM-AI/Med-Shicheng)]
- [*Chinese Herbal Medicines*] **HerbWise** Domain LLM for traditional herbal medicine (THM), serving herbal modernization and standardization. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.chmed.2026.02.010)]
- [*Chinese Medicine*] **GastroTCM** TCM gastroenterology LLM fine-tuned from Llama3-8B with RAG and agent scaffolding. Chinese Medicine paper from Tsinghua TCM-X and China-Japan Friendship Hospital et al. [Tsinghua University, China-Japan Friendship Hospital et al.] [[Paper](https://link.springer.com/article/10.1186/s13020-025-01295-8)]
- [*arXiv*] **DongYuan** Integrative spleen–stomach disease diagnosis LLM framework combining TCM pattern differentiation with Western diagnostic reasoning. arXiv PDF authors at Hebei Provincial Hospital of TCM and CASIA et al. [Hebei Provincial Hospital of Traditional Chinese Medicine, Institute of Automation, Chinese Academy of Sciences et al.] [[Paper](https://arxiv.org/abs/2603.28191)]
- [*Chinese Medicine*] **DFGLM-TCM** Dongfang Hospital / Zhipu TCM clinical system that models textbook knowledge and practitioner experience in separate modules. The paper is out. The code and the training and validation datasets are not public; qualified researchers can request them from the corresponding author. [Beijing University of Chinese Medicine, Zhipu AI] [[DOI](https://doi.org/10.1186/s13020-026-01512-y)]

</details>

<details>
<summary>2025 · 23</summary>

- **薪火中国药** Xinhuo Zhongguoyao is an education TCM model led by Beijing University of Chinese Medicine for study, teaching, research, administration, and international communication, and it received generative-AI service filing in 2026. [[Website](https://www.bucm.edu.cn/xwgl/6762cbff37ae4939829bbd3efae96225.htm)] [[Website](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)] [[News](https://www.beijing.gov.cn/fuwu/lqfw/gggs/202604/t20260423_4605343.html)]
- [*arXiv*] **ZMT-M1** ZMT-M1 TCM LLM and the dynamic, extensible TCM-Eval benchmark platform. [Beihang University] [[Paper](https://arxiv.org/abs/2511.07148)] [[Platform](https://tcmeval.bamaidical.com)]
- [*Chinese Medicine*] **XuanHuGPT** ChatGLM2-6B adapted to TCM using parameter-efficient fine-tuning with LoRA and P-Tuning v2. [Hebei North University] [[DOI](https://doi.org/10.1186/s13020-025-01200-3)]
- **张仲景中医药大模型** The Zhang Zhongjing TCM model, released by Henan University of Chinese Medicine and the University of Science and Technology Beijing, covers syndrome differentiation, syndrome-element recommendation, classical formulas, and formula analysis for clinical decision support. [[Website](https://hactcm.edu.cn/info/1022/211754.htm)] [[Website](https://news.ustb.edu.cn/info/1981/67772.htm)]
- **广医·岐智** Guangyi Qizhi is Guang'anmen Hospital's TCM service model for triage, pre-consultation, charting, and syndrome-formula advice; version 2.0 adds an agent doctor and the system has completed algorithm filing. [[Website](https://www.gamyy.cn/gzb/news/big/110133.html)] [[Website](https://www.gamyy.cn/gzb/news/big/114632.html)] [[News](https://www.gamyy.cn/gzb/news/big/113898.html)]
- [*Expert Systems with Applications*] **Qibo** TCM LLM and Qibo Benchmark from Tianjin University et al.; CPT + SFT for SDT and QA. [Tianjin University, Tianjin University of Traditional Chinese Medicine] [[Published](https://doi.org/10.1016/j.eswa.2025.127672)] [[Paper](https://arxiv.org/abs/2403.16056)] [[DOI](https://doi.org/10.1016/j.eswa.2025.127672)]
- **女娲 (Nüwa / TCM-Nvwa)** A TCM training stack on Ziya-LLaMA-13B: continued pretraining, supervised fine-tuning, a reward model, and RLAIF. The repository includes part of the pretraining, question-answer, and reward data. The weights are not released on their own. [[Code](https://github.com/synbol/TCM-Nvwa)]
- [*arXiv*] **TianHui** Domain LLM for 12 TCM scenarios (DeepSeek-R1-Distill-Qwen-14B + PT/SFT) with open code and eval scripts. arXiv PDF authors at Chengdu University of TCM. [Chengdu University of Traditional Chinese Medicine] [[Paper](https://arxiv.org/abs/2509.19834)] [[Code](https://github.com/JYfantast/TianHui)]
- **固生堂中医大脑** Gushengtang TCM Brain connects national-physician AI avatars to the hospital information system for history taking, record drafting, syndrome support, and prescription support with traceable rationale. [[Website](https://www.gstzy.cn/news/detail/10/14076.html)] [[Website](https://www.gstzy.cn/news/detail/10/14125.html)]
- **众星·长白岐黄** Zhongxing Changbai Qihuang is a multimodal reasoning TCM model from Changchun University of Chinese Medicine and partner universities, with a family health assistant and a Jipai doctor assistant. [[Website](https://www.jlbtc.edu.cn/info/1042/93113.htm)] [[News](https://news.cnjiwang.com/jwyc/202512/4006547.html)]
- **伊尹中医经典大模型** The Yiyin classic TCM model from Zhongyi Online is trained on medical canons and classical prescriptions, shows its syndrome-reasoning steps, and supports primary-care clinics in Song County. [[News](https://www.cntcm.com.cn/content/202509/17/c284139.html)]
- **任度·素问** Rendu Suwen is Transn's TCM model on its Rendu base and moH architecture, offering proactive consultation, syndrome analysis, and formula suggestions, and it passed CAICT's TCM large-model evaluation at level 4+. [[Website](https://www.transn.com/about_us/consult/article/1965645664716955649)]
- **中医横琴 (Hengqin-R1)** Hengqin-R1 is the Guangdong Provincial Laboratory of TCM's vertical reasoning model, combining fine-tuning, reinforcement learning, and a knowledge graph for syndrome reasoning, combined Chinese-Western medication agents, and objective four diagnostics. [[Website](https://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/dtxx/content/post_3807664.html)] [[Website](https://www.gzucm.edu.cn/info/1621/109561.htm)]
- [*Computers in Biology and Medicine*] **TCM-KLLaMA** KG-fused LLM for intelligent TCM formula generation. PubMed 40056842 lists Zhejiang Gongshang University and Hangzhou First People's Hospital (Westlake University School of Medicine). [Zhejiang Gongshang University, Hangzhou First People's Hospital, Westlake University School of Medicine] [[DOI](https://doi.org/10.1016/j.compbiomed.2025.109887)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/40056842)]
- [*Chinese Medicine*] **TCM-DS** DeepSeek-LLM-7B adapted with LoRA and retrieval-augmented generation (RAG) for dietary-therapy recommendations based on medicine-food homology. [Macau University of Science and Technology] [[DOI](https://doi.org/10.1186/s13020-025-01249-0)]
- [*arXiv*] **RACE-Align** RACE-Align: retrieval-augmented, CoT-style DPO alignment of a compact Qwen3-1.7B for TCM reasoning. arXiv PDF authors at ShanghaiTech, Henan University, and Liaoning University of TCM. [ShanghaiTech University, Henan University, Liaoning University of Traditional Chinese Medicine] [[arXiv](https://arxiv.org/abs/2506.02726)]
- [*IEEE ICIP 2025*] **MCM** Multi-agent collaborative multimodal TCM diagnosis framework (IEEE ICIP 2025). [Shanghai Computer Software Technology Development Center] [[Code](https://github.com/JerryMazeyu/MCM)] [[Published](https://doi.org/10.1109/icip55913.2025.11084334)]
- [*arXiv*] **Ladder-base (GRPO-TCM)** First GRPO reinforcement-learning-aligned TCM LLM, from the TCM-Ladder team. arXiv PDF authors at University of Missouri and Shanghai University of TCM et al. [University of Missouri, Shanghai University of Traditional Chinese Medicine et al.] [[Paper](https://arxiv.org/abs/2510.17402)]
- [*arXiv*] **Hengqin-RA-v1** LLM and companion dataset for TCM diagnosis and treatment of rheumatoid arthritis. arXiv has withdrawn the preprint because the authorship and affiliation could not be verified; the author line now lists Yishen Liu. [[Paper](https://arxiv.org/abs/2501.02471)]
- [*Applied Sciences*] **Gen-SynDi** Knowledge-guided generative-AI framework for dual education of syndrome differentiation and disease diagnosis. [College of Korean Medicine, Wonkwang University, Iksan 54538, Republic of Korea, College of Korean Medicine, Woosuk University, Jeon-Ju 54987, Republic of Korea, Dongje Medical Co., Ltd., Daegu 42187, Republic of Korea, College of Medicine, Yeungnam University, Daegu 42415, Republic of Korea] [[DOI](https://doi.org/10.3390/app15094862)]
- [*arXiv*] **DoPI** Proactive inquiry system combining guidance and expert models; DoPI-7B achieves 84.68% final diagnostic accuracy in the paper's simulated-consultation evaluation. [Tianjin University, The Chinese University of Hong Kong et al.] [[Paper](https://arxiv.org/abs/2507.04877)]
- [*IEEE BIBM 2025*] **ChatGLM-FGIDs-TCM** Knowledge-fused ChatGLM clinical decision-support model for functional gastrointestinal disorders (FGIDs). [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356283)]
- [*arXiv*] **BenCao** Instruction-aligned multimodal TCM assistant (ChatGPT/GPTs Store) with tongue APIs and knowledge bases (distinct from HuaTuo/BenCao). arXiv HTML authors at University of Missouri and Shanghai University of TCM et al. [University of Missouri, Shanghai University of Traditional Chinese Medicine et al.] [[Paper](https://arxiv.org/abs/2510.17415)]

</details>

<details>
<summary>2024 · 10</summary>

- **智赋岐黄天功** Zhifu Qihuang Tiangong is a TCM model from Zhifu Qihuang and Harbin Institute of Technology, trained on cases and famous-doctor formulas for several syndrome systems, and it backs four-diagnostic constitution reports under algorithm filing. [[Website](https://qihuang-ai.com/ai-platform/tiangong)] [[Website](https://qihuang-ai.com/about)]
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
<summary>2024 · 5</summary>

- [*arXiv*] **明医 (MING)** MING: a Chinese medical consultation LLM using a sparse mixture of low-rank adapter experts (MING-MoE) for medical multi-task learning (arXiv 2024). [[Paper](https://arxiv.org/abs/2404.09027)] [[Related MedCare](https://aclanthology.org/2024.findings-emnlp.619/)] [[Code](https://github.com/MediaBrain-SJTU/MING)]
- [*JAMIA*] **Taiyi** DUTIR bilingual biomedical LLM on Qwen-7B for QA, doctor–patient dialogue, report generation, and information extraction (JAMIA 2024). [Dalian University of Technology] [[DOI](https://doi.org/10.1093/jamia/ocae037)] [[Code](https://github.com/DUTIR-BioNLP/Taiyi-LLM)] [[Model](https://huggingface.co/DUTIR-BioNLP/Taiyi-LLM)]
- [*arXiv*] **HuatuoGPT-o1** HuatuoGPT medical complex-reasoning model trained with verifiable problems and a medical verifier. The repository lists 7B, 8B, and 70B checkpoints. [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[Paper](https://arxiv.org/abs/2412.18925)] [[Code](https://github.com/FreedomIntelligence/HuatuoGPT-o1)] [[Model](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-7B)]
- [*arXiv*] **HuatuoGPT-Vision** HuatuoGPT multimodal medical model that injects visual knowledge at scale; a common Chinese medical vision baseline. [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[Paper](https://arxiv.org/abs/2406.19280)] [[Code](https://github.com/FreedomIntelligence/HuatuoGPT-Vision)] [[Model](https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B-Qwen2.5VL)]
- [*arXiv*] **Apollo** FreedomIntelligence multilingual medical LLM (including Chinese) with ApolloCorpus and XMedBench. [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[Paper](https://arxiv.org/abs/2403.03640)] [[Code](https://github.com/FreedomIntelligence/Apollo)] [[Model](https://huggingface.co/FreedomIntelligence/Apollo-7B)]

</details>

<details>
<summary>2023 · 20</summary>

- [*arXiv*] **Qilin-Med** Multi-stage Chinese medical LLM (CPT+SFT+DPO on Baichuan-7B) releasing the ~3GB ChiMed corpus, optionally with RAG. arXiv PDF authors at Peking University and HKUST (Guangzhou) et al. [Peking University, Hong Kong University of Science and Technology (Guangzhou) et al.] [[Paper](https://arxiv.org/abs/2310.09089)] [[Code](https://github.com/williamliujl/Qilin-Med)] [[Dataset](https://huggingface.co/datasets/williamliu/ChiMed)]
- [*arXiv*] **BenCao (formerly HuaTuo)** BenCao, first called HuaTuo, is an instruction-tuned medical model from HIT SCIR, trained with Chinese medical knowledge. The 2023 paper is HuaTuo. The same group later published a knowledge-tuning paper in ACM TKDD in February 2025. [Harbin Institute of Technology] [[Paper](https://arxiv.org/abs/2304.06975)] [[Link](https://arxiv.org/abs/2309.04175)] [[Link](https://doi.org/10.1145/3686807)] [[Code](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)]
- **BianQue-2** Second BianQue open consultation model with stronger multi-turn questioning; a common CMB baseline. [South China University of Technology, Guangdong Key Laboratory of Digital Twin Humans] [[Code](https://github.com/scutcyr/BianQue)] [[Model](https://huggingface.co/scutcyr/BianQue-2)]
- [*arXiv*] **BianQue** Chinese proactive health LLM for everyday living spaces (BianQue). [South China University of Technology, Guangdong Key Laboratory of Digital Twin Humans] [[Code](https://github.com/scutcyr/BianQue)] [[Paper](https://arxiv.org/abs/2310.15896)]
- **孙思邈 (Sunsimiao)** Sunsimiao Chinese medical LLM; Sunsimiao-7B fine-tuned from Qwen2-7B on curated medical data, reaching 30B-level SOTA on CMB-Exam. [[Code](https://github.com/X-D-Lab/Sunsimiao)]
- **QiZhenGPT** Chinese clinical QA model for drugs, diseases, procedures, and labs (QiZhenGPT). [Zhejiang University] [[Code](https://github.com/CMKRG/QiZhenGPT)]
- **WiNGPT2** Winning Health open medical LLM on Qwen for medical QA, record understanding, and multi-turn consults; 7B/14B weights are public. [Winning Health] [[Model](https://huggingface.co/winninghealth/WiNGPT2-14B-Chat)] [[7B](https://huggingface.co/winninghealth/WiNGPT2-7B-Chat)]
- [*arXiv*] **HuatuoGPT-II** Second HuatuoGPT generation with one-stage medical adaptation; 7B/13B use Baichuan2 backbones and remain a standard Chinese medical baseline. [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[Paper](https://arxiv.org/abs/2311.09774)] [[Code](https://github.com/FreedomIntelligence/HuatuoGPT-II)] [[Model](https://huggingface.co/FreedomIntelligence/HuatuoGPT2-7B)]
- [*EMNLP findings*] **HuaTuoGPT** Large language model trained on Chinese medical corpora (HuaTuoGPT). [The Chinese University of Hong Kong, Shenzhen, Shenzhen Institute of Big Data] [[DOI](https://doi.org/10.18653/v1/2023.findings-emnlp.725)] [[Paper](https://aclanthology.org/2023.findings-emnlp.725/)] [[Code](https://github.com/FreedomIntelligence/HuatuoGPT)]
- [*arXiv*] **SoulChat** SCUT mental-health dialogue LLM from the same lab as BianQue; a common Chinese health-conversation baseline. [South China University of Technology, Guangdong Key Laboratory of Digital Twin Humans] [[Paper](https://arxiv.org/abs/2311.00273)] [[Code](https://github.com/scutcyr/SoulChat)] [[Model](https://huggingface.co/scutcyr/SoulChat)]
- **PULSE** OpenMEDLab Chinese medical LLM. PULSE-7b is fine-tuned from bloomz-7b1-mt and PULSE-20b from InternLM-20B, for exams, report reading, record structuring, and simulated diagnosis. [Shanghai AI Laboratory] [[Code](https://github.com/openmedlab/PULSE)] [[Model](https://huggingface.co/OpenMEDLab/PULSE-7bv5)]
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

- **iFlytek Spark Medical** iFlytek Spark Medical X1, released in March 2025 and used in Xiaoyi. The reported tests draw on Xiaoyi, Zhiyi Assistant, and other real clinical settings. [iFlytek] [[Website](https://www.xunfeihealthcare.com/)] [[News](https://www.cn-healthcare.com/article/20250303/wap-content-585822.html)]
- **Ant Afu** On 5 July 2024, Alipay released a multimodal medical model at the World Artificial Intelligence Conference, built on Bailing and able to read medicines, reports, and images. On 15 December 2025 its health app AQ was renamed Ant Afu; users can photograph skin, lab reports, and medicine boxes. [Ant Group] [[Website](https://www.antafu.com/)] [[Press](https://www.antgroup.com/news-media/press-releases/1720166400000)] [[News](https://www.antgroup.com/news-media/press-releases/1765785600000)]
- **Tencent Hunyuan Medical** Closed Tencent Health medical LLM on Hunyuan for QA, triage, records, and imaging; announced by Tencent Jarvis Lab, no public weights. [Tencent] [[Website](https://healthcare.tencent.com/)] [[News](https://healthcare.tencent.com/news/1603)]
- [*Sci China Life Sci*] **PanGu Drug Model** Closed Huawei Cloud / SIMM molecule foundation model (~1.7B small molecules) for property prediction, generation, and optimization; later used under Shuzhi Bencao. [Huawei Cloud, Shanghai Institute of Materia Medica, CAS] [[DOI](https://doi.org/10.1007/s11427-022-2239-y)] [[Website](https://www.huaweicloud.com/cases/pgyw.html)]

</details>

<details>
<summary>Kampo / Korean-medicine models and systems (1)</summary>

- **KAMPO LLM** Official site still live. Closed Kampo API from VARYTEX with the Japan Society for Oriental Medicine; page reports 97.4% (Pro) and 92.1% (Flash) on 471 specialist-training items; no public weights. [VARYTEX, Japan Society for Oriental Medicine] [[Website](https://kampollm.varytex.co.jp/)]

</details>

<details>
<summary>Other Hugging Face sizes and GGUF (11)</summary>

- **Xinghe** — Xinghe Neijing reasoning model weights. [[Model](https://huggingface.co/zsyjsld/Xinghe1.2-9B)] [[GGUF](https://huggingface.co/zsyjsld/Xinghe1.2-9B-GGUF)]
- **ZhongJing** — ZhongJing GPT weights. [[ZhongjingGPT1_13B](https://huggingface.co/CMLM/ZhongjingGPT1_13B)] [[ZhongJing-2-1.8B](https://huggingface.co/CMLL/ZhongJing-2-1_8b)]
- **Baize** — Baize TCM LLM weights. [[Model](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model)] [[8B-16bit](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit)]
- **ShizhenGPT** — ShizhenGPT multimodal weight series. [[7B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-LLM)] [[7B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-VL)] [[7B-Omni](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[32B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-LLM)] [[32B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-VL)]
- **BianCang** — BianCang open-weight series. [[Qwen2.5-7B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)] [[Qwen2.5-14B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-14B-Instruct)]
- **medchatzh** — MedChatZH weights. [[medchatzh](https://huggingface.co/tyang816/medchatzh)]
- **TCMChat** — TCMChat weights. [[TCMChat-600k](https://huggingface.co/ZJUFanLab/TCMChat-600k)]
- **Lingdan** — Lingdan / TCMLLM weights. [[Lingdan-13B-Base](https://huggingface.co/TCMLLM/Lingdan-13B-Base)] [[Lingdan-13B-PR](https://huggingface.co/TCMLLM/Lingdan-13B-PR)]
- **ChatTCM-7B-SFT** — ChatTCM full-parameter SFT checkpoint. [[Model](https://huggingface.co/SylvanL/ChatTCM-7B-SFT)]
- **ChatTCM** — ChatTCM pretrained weights. [[ChatTCM-7B-Pretrain](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)]
- **ShenNong-TCM-LLM** — ShenNong-TCM-LLM weights. [[ShenNong-TCM-LLM](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]

</details>

## News

<details>
<summary>87 items; recent: 岐元 · 李强签署国务院令公布《中医药传统知识保护 · TCMQA</summary>

<details>
<summary>2026 · 52</summary>

- [2026.11.09] China News Service reported on 9 November 2026 that Shanghai Seventh People's Hospital made its first CIIE appearance and presented the Qiyuan TCM model, along with an AI face-diagnosis agent and the teaching robot Xiaoqi. Qiyuan was already released in July 2026; this item covers the exhibition, not a first launch. [[Link](https://www.chinanews.com.cn/jk/2026/11-09/10729099.shtml)]
- [2026.11.09] Xinhua reported from Beijing on 9 November 2026 that Premier Li Qiang signed a State Council decree (Guo Ling No. 850) promulgating the Regulation on the Protection of Traditional Chinese Medicine Traditional Knowledge. The regulation has 32 articles, including a protection database and a protection list, and takes effect on 1 January 2027. [[Link](https://www.news.cn/politics/leaders/20261109/115bf875b154445787539419282ce542/c.html)] [[Link](https://www.gov.cn/yaowen/liebiao/202611/content_7085599.htm)] [[Link](https://www.gov.cn/zhengce/zhengceku/202611/content_7085592.htm)]
- [2026.11.05] Beijing News, carrying a 5 November 2026 report, said the fifth Wenzhi TCM clinical conference in Shenzhen on 1 November formally released TCMQA, a 38,279-item exam-style benchmark with a licensed-physician baseline. Materials are on Hugging Face. This catalog already lists the benchmark; this entry is the release notice. The report does not equate exam scores with clinical bianzheng skill. [[Link](https://www.bjnews.com.cn/detail/1793844088129508.html)]
- [2026.11.05] A 5 November People’s Daily Online interview discusses the separate TCM track in the Data Elements competition, expert agents and high-quality dataset construction; it supplies leads rather than downloadable data. [[Link](https://finance.people.com.cn/n1/2026/1105/c1004-40828489.html)]
- [2026.11.05] Wenge announced on 5 November 2026 that TCM-BEST4SDT, a Bianzheng Lunzhi evaluation benchmark built with the China Academy of Chinese Medical Sciences, was published online in Scientific Data. The report describes 600 samples and 27 dimensions, with data and code released. This catalog already lists the benchmark; this entry is the publication notice. [[Link](https://www.wenge.com/site/a/202611/05/1070720261105103301.html)]
- [2026.11.04] Beijing’s health authority reports on 4 November about the 30 October meeting on structured TCM knowledge, trusted AI datasets and Xiyuan Hospital’s oncology data system. No public data package accompanies the report. [[Link](https://wjw.beijing.gov.cn/xwzx_20031/jcdt/202611/t20261104_4931739.html)]
- [2026.11.03] The Shanxi Provincial Health Commission and the Shanxi Development and Reform Commission issued the Shanxi 15th Five-Year Plan for TCM Development (Jin Wei Zhongyiyao Keji Fa [2026] No. 3; dated 28 October 2026 and posted on the provincial health commission website on 3 November). The plan aims, by 2030, to make decisive progress toward a strong TCM province, using scientific innovation, digital-intelligence transformation, and TCM–Western collaboration to strengthen Shanxi’s TCM brand. A dedicated chapter supports digital-intelligence empowerment, including a trusted TCM data space and high-quality AI datasets, uses of multimodal large models in assisted decision-making, record quality control, inheritance of renowned physicians’ experience, and new-drug research, plus smart TCM hospitals and grassroots intelligent assisted diagnosis. The official full-text page was opened in this pass. This is a provincial plan, not a model release. [[Link](https://wjw.shanxi.gov.cn/tzgg/zcwj/202611/t20261103_10251747.shtml)]
- [2026.11.03] The People's Government of Shandong Province issued the Shandong 15th Five-Year Plan for TCM Development (Lu Zheng Fa [2026] No. 23; dated 23 October 2026 and published on 3 November). The plan adopts a 'six names and four modernizations' strategy, including making TCM smarter, and aims for universal access to TCM services by 2030. Official tasks include digitizing ancient texts, training talent in digital and intelligent applications, and promoting digital and intelligent empowerment of TCM. This is a provincial plan, not a model release. [[Link](http://www.shandong.gov.cn/art/2026/11/3/art_267492_89889.html)] [[Link](http://www.shandong.gov.cn/art/2026/11/3/art_306404_21741.html)]
- [2026.11.03] A 3 November Economic Daily report describes the 2026 global traditional-medicine AI report and Hangzhou’s Zhongyi Xiao’an robot. Its scope is AI in traditional medicine broadly, not a count of TCM LLMs. [[Link](https://www.digitalchina.gov.cn/2026/szzg/xyzx/202611/t20261103_5389002.htm)]
- [2026.11.02] The Guangdong Provincial Health Commission, the Guangdong Administration of Traditional Chinese Medicine, and the Guangdong Development and Reform Commission issued the Guangdong 15th Five-Year Plan for TCM Development (Yue Wei [2026] No. 4; dated 8 October 2026 and posted on the provincial TCM administration website on 2 November). The plan is framed around Western-Chinese collaboration, digital and intelligent transformation, and Guangdong-Hong Kong-Macao cooperation, and aims for universal access to quality TCM services by 2030. A dedicated chapter supports TCM large-model and agent development, high-quality datasets, digital platforms and knowledge graphs, and smart TCM hospitals. This is a provincial plan, not a model release. [[Link](http://szyyj.gd.gov.cn/zwgk/gsgg/content/post_4974266.html)]
- [2026.10.28] The General Department of the National Administration of Traditional Chinese Medicine and the General Office of the National Health Commission issued a notice on promoting grassroots TCM appropriate techniques (Guo Zhongyiyao Zong Yizheng Fa [2026] No. 8; dated 14 October 2026 and posted on the NATCM website and, via Xinhua, on the Chinese government portal on 28 October). The notice calls for a national-provincial-city-county promotion network, basically complete coverage of county promotion centers by 2030, and priority rollout of at least 15 techniques in six categories. It also sets out digital support for the work and exploratory use of AI tools for teaching, assisted diagnosis, and quality control. This is a grassroots service-capacity policy, not a product launch. [[Link](http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39042.html)] [[Link](https://www.gov.cn/lianbo/202610/content_7084413.htm)]
- [2026.10.27] Ifeng Finance reported on 31 October 2026 that Tianji Yiqi said its on-device model Yiqi TCM AI finished debugging and went live on 27 October, and can run fully offline for constitution assessment and similar uses. This is a company release reprinted by media; this page has not independently verified clinical effects or deployment scale. The model is not the ETCM herbal database. [[Link](https://news.10jqka.com.cn/20261031/c681322899.shtml)]
- [2026.10.26] Thirteen Fujian departments, led by the Provincial Health Commission and the Provincial TCM Administration, issued Several Measures on Improving the Quality of Chinese Medicines and Promoting High-Quality Development of the TCM Industry (Min Wei Gui [2026] No. 4; dated 15 October 2026, posted on the provincial health commission website on 26 October, and valid through 31 December 2030). The measures implement State Council General Office document No. 11 of 2025 and cover protection of Fujian geo-authentic herbs, standardized cultivation, industrial clusters, and TCM industry upgrading, including faster intelligent retrofitting of manufacturers, stepwise development of smart factories, and an informatized traceability system. The official webpage and the public PDF were opened in this pass. This is a provincial industry-quality policy, not a product launch. [[Link](https://wjw.fujian.gov.cn/xxgk/fgwj/zxwj/202610/t20261026_7240705.htm)] [[PDF](https://wjw.fujian.gov.cn/xxgk/fgwj/zxwj/202610/P020261026658500638498.pdf)]
- [2026.10.24] Guang'anmen Hospital reported on 24 October 2026 on TCM AI exhibits at the 17-18 October World Traditional Medicine Conference, including Guangyi Qizhi, Hangzhou Hospital of TCM's embodied robot Xiao'an, and Zhongke Yunzhen's Miaowu Qihuang. Visit counts and agreement rates in the report come from exhibitors and should not be read as formal benchmark results. [[Link](https://www.gamyy.cn/gzb/news/trends/118061.html)]
- [2026.10.22] An official interpretation posted on 22 October 2026 by the Hubei Provincial Health Commission states that, with the consent of the provincial people's government, the provincial health commission, development and reform commission, and TCM administration jointly issued the Hubei 15th Five-Year Plan for TCM Development on 19 September 2026. The interpretation says the plan aims for universal access to TCM services by 2030 and includes digital-intelligence empowerment and standards, continuing smart-hospital construction, deeper use of data resources, and TCM artificial intelligence. The official interpretation page was opened in this pass; the plan-text link listed on the same site returned 404 and was not used as a source. This is a provincial plan, not a model release. [[Link](https://wjw.hubei.gov.cn/zfxxgk/zc/zcjd_1/202610/t20261022_6037633.shtml)]
- [2026.10.21] Zhitong Finance reported on 21 October 2026 that Yidu Technology launched the evidence-based TCM agent Xiaohuangqi at the 2026 World Traditional Medicine Conference, covering guideline retrieval, assisted bianzheng, formula lookup and term translation, with answers said to cite sources. Item counts and hospital use come from the company and have not been independently verified here. [[Link](https://www.zhitongcaijing.com/content/detail/1509924.html)]
- [2026.10.20] Sichuan Observation reported on 20 October 2026 that the province issued its 15th Five-Year TCM development plan, calling for TCM digital platforms, large models for renowned-physician intelligent diagnosis, grassroots decision-support pilots, and high-quality datasets. This is a planning document, not a model launch. [[Link](https://cbgc.scol.com.cn/news/8074897)]
- [2026.10.18] A Beijing Daily report carried on 27 October 2026 by the Beijing science and technology portal said that on 18 October, at the Beijing outcomes session of the 2026 World Traditional Medicine Conference, the Beijing Digital TCM Industry Development Institute released the agent Shu Xiaohe, using local compute and a self-owned knowledge base for Chinese and English TCM services. [[Link](https://www.ncsti.gov.cn/kjdt/xwjj/202610/t20261027_259363.html)]
- [2026.10.18] A 19 October 2026 Phoenix Tech reprint said Transn Suwen and Mingyi Online jointly released a Fan Jiping digital twin on 18 October at the World Traditional Medicine Conference, built on Transn's Suwen TCM model from cases and teaching materials. This is a single-physician twin launch; the report does not present independently verified clinical trial results. [[Link](https://tech.ifeng.com/c/8xLt1uquwDi)]
- [2026.10.16] China News of TCM reports on 16 October that Wuhan Hospital of TCM traded a Hanpai orthopaedics data product involving 168,000 structured records, 3,600 empirical formulas and diagnostic reasoning; this is licensed circulation. [[Link](https://www.cntcm.com.cn/content/202610/16/c505880.html)]
- [2026.10.09] The General Office of the People's Government of Hunan Province issued the Hunan 15th Five-Year Plan for TCM Development (Xiang Zheng Ban Fa [2026] No. 53, dated 9 October 2026). The plan aims for universal access to TCM services by 2030 and sets nine groups of tasks, including faster digital and intelligent empowerment of TCM, smart TCM hospitals, shared prescriptions and data connectivity, AI-assisted diagnosis and intelligent dispensing at the grassroots, and high-quality dataset development. The provincial TCM administration's official interpretation was posted on the Hunan government portal on 11 November 2026. This is a provincial plan, not a model release. [[Link](https://www.hunan.gov.cn/hnszf/xxgk/wjk/szfbgt/202610/t20261023_34087538.html)] [[Link](http://www.hunan.gov.cn/hnszf/xxgk/jd/bmjd/202611/t20261111_34099599.html)]
- [2026.10.09] Reports say Nanjing University of Chinese Medicine released the LingSu Aihu TCM nursing model on 9 October; 27 member hospitals are the first sites. [[Link](https://finance.sina.com.cn/jjxw/2026-10-10/doc-iniutqmk0582279.shtml)]
- [2026.09.24] China News of TCM reports on 24 September on registration of Guang’anmen’s chronic-gastritis dataset and a trusted data space for disease-specific TCM research; the report provides no public download. [[Link](https://www.cntcm.com.cn/content/202609/24/c505607.html)]
- [2026.09.22] Dayoo reported on 22 September 2026 that Guangdong Provincial Hospital of Chinese Medicine presented its veteran-physician model matrix at the second Guangdong AI application conference, saying the Xuan Guowei dermatology model had been in use since June 2025. Figures such as "over 95% accuracy" and 2,917 assisted decisions come from the hospital and are not external trial results. The matrix launch was reported earlier. [[Link](https://news.dayoo.com/guangzhou/202609/22/139995_55006505.htm)]
- [2026.09.21] China Traditional Chinese Medicine News reported on 30 September 2026 that a digital TCM and data-element pilot meeting was held in Chongqing on 20-21 September. The piece is a meeting round-up covering AI, data elements and application scenarios, not a new model debut. [[Link](https://www.cntcm.com.cn/content/202609/30/c505658.html)]
- [2026.09.19] China News Service reports that the formula-syndrome model opened for access on 19 September, covering assisted care, research mining, and training, with planned deployment at Longhua Hospital. [[Link](https://www.chinanews.com.cn/jk/2026/09-19/10699553.shtml)]
- [2026.09.15] Jiemian reported that on 15 September, at the seventh pavilion-exchange and TCM development conference in Hangzhou, Transn Suwen launched a Hundred Physicians Twin plan to build digital twins for 100 veteran TCM doctors on its Suwen model. This is a plan announcement; the report does not list a complete roster or independently verified agreement rates. [[Link](https://www.jiemian.com/article/15106308.html)]
- [2026.09.07] MIIT and five other departments issued document 204 of 2026 on 7 September 2026, listing Chinese materia medica among historical classic industries and calling for an AI empowerment guide, high-quality datasets, large-model analysis of traditional crafts, smart pharmacies, and industrial process knowledge graphs. [[Link](https://www.miit.gov.cn/jgsj/xfpgys/wjfb/art/2026/art_ece6902ba0b24ad2806e670618f17a9f.html)] [[Link](http://www.news.cn/politics/20260907/1d0ae2bfeb1f4d0fb58f7611ba77a3c3/c.html)]
- [2026.09] Guang'anmen Hospital shows **Guangyi Qizhi 2.0** at CIFTIS 2026, with AI doctor An'an covering six hospital scenes from patient service to ward management. [[Link](https://app.xinhuanet.com/news/article.html?articleId=202609101de3e66a53f7474ba7d373deaaa7e122)]
- [2026.09] Beijing University of Chinese Medicine debuts a TCM constitution-identification system and an embodied tuina robot at the CIFTIS 2026 TCM pavilion. [[Link](https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202608/t20260807_4812596.html)]
- [2026.08.27] The university site says the Qian Xiaoxing medical model was released on 27 August 2026, trained on TCM literature, expert experience, and clinical data for diagnosis support, constitution identification, wellness advice, and medication guidance. [[Link](https://www.gzy.edu.cn/info/1501/12735.htm)]
- [2026.08] Southern Finance reports that Guangzhou University of Chinese Medicine continued-trains a general model on about 2 billion TCM tokens into the Xinglin teaching model, now piloted in three core courses. [[Link](https://m.21jingji.com/article/20260824/herald/ef692f3ceba10c36edd3952f4d5ca892.html)]
- [2026.07.29] Guizhou Medical University and partners launch **HuaZu BenCao**, a national ethnic-medicine AI platform built on ShuZhi QiHuang + Qwen integrating multi-ethnic materia medica classics. [[Link](https://www.gmc.edu.cn/info/1058/30267.htm)]
- [2026.07.28] Eleven ministries, led by the National Administration of Traditional Chinese Medicine, issued the TCM Action Plan under the Healthcare Strengthening Program (Guo Zhongyiyao Yizheng Fa [2026] No. 6; dated 11 July 2026 and posted on official sites on 28 July). The plan aims, by 2030, to complete a grassroots TCM service network and improve digital and intelligent conditions. Among seven actions, it calls for faster hospital informatization, continued development of smart TCM hospitals, and exploratory use of medical AI for assisted diagnosis in grassroots TCM services and the inheritance of renowned physicians' experience. [[Link](https://www.gov.cn/zhengce/zhengceku/202607/content_7076920.htm)] [[Link](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-07-28/38433.html)]
- [2026.07.24] Shanghai Seventh People's Hospital (SHUTCM) releases the **Qiyuan** TCM LLM with pretraining, domain fine-tuning, and expert RL; supports generative medical records and master-physician Agent digital twins; showcased at WAIC. [[Link](https://dwgk.shutcm.edu.cn/2026/0725/c1890a175544/page.htm)]
- [2026.07.23] After State Council approval (Guo Han [2026] No. 71), the National Administration of Traditional Chinese Medicine and the National Development and Reform Commission issued the 15th Five-Year Plan for the Revitalization and Development of Traditional Chinese Medicine (Guo Zhongyiyao Guicai Fa [2026] No. 8) on 23 July 2026. The plan sets the goal that everyone should have access to TCM services by 2030 and lists ten priority tasks, including accelerating digital and intelligent empowerment and standards. The official Q&A states that AI and other new technologies should be used to mine and transmit the TCM heritage. This is a national five-year plan, not a product launch. [[Link](https://www.gov.cn/zhengce/zhengceku/202607/content_7076394.htm)] [[Link](http://www.natcm.gov.cn/guicaisi/zhengcewenjian/2026-07-22/38398.html)] [[Link](https://www.news.cn/20260723/d6c2ca040e534b9186271da832c4ec6b/c.html)]
- [2026.07.03] A China Women's News report carried on 6 July 2026 by the Beijing Municipal Health Commission said the Digital TCM Forum of the 2026 Global Digital Economy Conference was held in Beijing on 3 July. The forum released agent technical requirements and related standards, 16 digital TCM application cases, and launched the Beijing TCM track of the Data Element competition. [[Link](https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202607/t20260706_4748255.html)]
- [2026.07] Xinhua reports that in July 2026 the national medical AI pilot base released five results in Henan, including a meridian-diagnosis model, an esophageal-cancer model, a TCM dataset, a Chinese-medicine R&D model, and a famous-doctor agent. [[Link](http://www.ha.xinhuanet.com/20260928/c8569fe1fbdb4ebc81053d86c6d93682/c.html)]
- [2026.07] Insightful Eye presents **Bianshi Cloud TCM** at WAIC 2026, built on a registered Bianshi multimodal model with four-diagnosis devices and assisted-care systems. [[Link](http://www.eeo.com.cn/2026/0720/965556.shtml)]
- [2026.07] Andun Health debuts a **seven-diagnosis** TCM robot at WAIC 2026, integrating face, infrared face, tongue, ear, auscultation, inquiry, and pulse. The page cites a 235-billion-parameter TCM model and does not mention TianHui. [[Link](https://www.news.cn/finance/20260720/f6a8625c1be4412d9c311a232c7a35fa/c.html)]
- [2026.06] Zhongke Wenge passes HKEX listing hearing; reports note the **DaYi JinKui** TCM LLM (with CACMS) has obtained top-tier CAICT Trusted AI certification. [[Link](https://www.ncsti.gov.cn/kjdt/xwjj/202606/t20260610_249369.html)]
- [2026.05] Beijing University of Chinese Medicine says XinHuo ZhongGuoYao appeared at the 2026 World Digital Education Conference and its Q&A edition is on the national smart-education platform. [[Link](https://zhongyao.bucm.edu.cn/yyxw/fb4b320d30c34e358de28a637c9f6f2c.htm)]
- [2026.04.24] The General Office of the People's Government of Zhejiang Province issued the Zhejiang 15th Five-Year Plan for TCM Development (Zhe Zheng Ban Fa [2026] No. 14, dated 24 April 2026). The plan aims, by 2030, to basically complete a pioneering province for TCM modernization with nationally leading TCM AI applications, and it coordinates service, industry, science and technology, talent, culture, governance, and digital-intelligence modernization. One headline indicator is that the share of TCM medical institutions applying medical large models should reach 100% by 2030, and the plan calls for Zhejiang to become an important source of TCM AI development. This is a provincial plan, not a model release. [[Link](https://zjjcmspublicnew.oss-cn-hangzhou-zwynet-d01-a.internet.cloud.zj.gov.cn/cms_files/filemanager/1567290/attach/20266/054C52CACC6589E4F1917D8B993978B9.pdf)] [[Link](https://tradeinservices.mofcom.gov.cn/article/zcfb/zcfg/202607/200234.html)] [[Link](https://itc.zcmu.edu.cn/202607132.pdf)]
- [2026.04.21] Beijing University of Chinese Medicine's **XinHuo ZhongGuoYao** TCM education LLM completes national generative-AI service filing—the first publicly approved TCM-domain model of its kind. [[Link](https://regional.chinadaily.com.cn/education/cn/2026-04/22/c_1177692.htm)]
- [2026.04] Affiliated Hospital of Shandong University of TCM launches the provincial AI+ TCM scenario project **ZhiHui QiHuang**. [[Link](http://ccpd.china.com.cn/2026-04/17/content_43401621.html)]
- [2026.03.17] China News of Traditional Chinese Medicine reported that on 17 March 2026 Li Haiyan said the Yiyuan TCM model is being tried for case structuring, intelligent inquiry, prescription recommendation, and rational use of Chinese patent medicines. [[Link](https://www.cntcm.com.cn/content/202603/20/c501417.html)]
- [2026.03] Shanghai University of TCM says its formula-syndrome multimodal model was selected as a stage result of a national AI application pilot base. [[Link](https://kjrw.shutcm.edu.cn/2026/0330/c805a172392/page.htm)]
- [2026.02] Eight ministries issue the TCM Industry High-Quality Development Plan (2026–2030), calling for AI and knowledge graphs to empower classical formulas and master physicians' prescriptions. [[Link](https://www.gov.cn/zhengce/zhengceku/202602/content_7057174.htm)]
- [2026.01.09] Science and Technology Daily reports that on 9 January Guangdong Provincial Hospital of Chinese Medicine launched a matrix of famous-doctor decision models; dermatology and cardiovascular models are already in clinical use. [[Link](https://www.stdaily.com/web/gdxw/2026-01/12/content_460323.html)]
- [2026.01] Xinhua reports that on 24 December 2025 Henan's health commission showed a meridian-assisted diagnosis model and the Yuyao multimodal Shennong materia medica model for herb identification, authentication, assay, and origin tracing. [[Link](http://www.ha.xinhuanet.com/20260105/b91d84bacd1c46389a007e0cc201962d/c.html)]
- [2026.01] Chengdu University of TCM said Wen Chuanbiao's team project, a high-quality TCM AI-model dataset numbered 2025-AISJK-02013, was selected for the 2025 MIIT and NMPA AI medical-device challenge list. [[Link](https://www.cdutcm.edu.cn/info/1074/138321.htm)]
- [2026.01] TCM Congbao says its Suwen content-generation algorithm was included in the 14th CAC deep-synthesis filing batch. [[Link](https://www.tcmbrain.com/?list_43/180.html)]

</details>

<details>
<summary>2025 · 29</summary>

- [2025.12.20] Jilin releases **ZhongXing·Changbai Qihuang 1.0**, an AI-native multimodal TCM LLM. [[Link](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- [2025.12] **ZMT-M1** scores 96.26 on a simulated national TCM practitioner exam and is piloted in 100+ clinics. [[Link](https://m.tech.china.com/redian/2025/1229/122025_1789291.html)]
- [2025.12] Guang'anmen Hospital reports that Guangyi Qizhi completed national deep-synthesis algorithm filing and describes itself as the first TCM hospital to do so. [[Link](https://www.gamyy.cn/gzb/news/big/114632.html)]
- [2025.12] Gushengtang launches a “TCM Brain” and an AI twin of National TCM Master Shi Qi, with 14 expert twins released. The eight-specialty claim is from a different story, not this page. [[Link](https://www.jjckb.cn/20251231/693ca93b14ff4f57adc359959dc0320d/c.html)]
- [2025.11.02] USTB said that on 2 November 2025 in Zhengzhou it jointly released the Qihuang Acupuncture model, which turns four-diagnostic readings into acupuncture prescriptions. [[Link](https://news.ustb.edu.cn/info/1087/72015.htm)]
- [2025.11] Five national health ministries issue AI+ healthcare guidelines that explicitly support building TCM diagnostic LLMs. [[Link](https://www.gov.cn/zhengce/zhengceku/202511/content_7047018.htm)]
- [2025.10.26] China Economic Net reports the 26 October release of Idiom-Hypertension, an integrated Chinese-Western model for hypertension care. [[Link](https://www.ce.cn/cysc/yy/hydt/202510/t20251027_2541616.shtml)]
- [2025.10.21] Science and Technology Daily reports the CTA clinical-research agent, fine-tuned from Qwen2.5-14B for trial protocols, data management, and statistics. [[Link](https://www.stdaily.com/web/gdxw/2025-10/21/content_418966.html)]
- [2025.09.18] **YiYin** classical TCM LLM goes live in Song County, Henan, combining TCM education with AI-assisted care for county clinics. [[Link](http://www.ha.xinhuanet.com/20250918/a3da94037689422dbcd1fe57fa62ef94/c.html)]
- [2025.09.12] Guang'anmen Hospital said that on 12 September 2025, at the CIFTIS forum, it released Guangyi Qizhi 2.0 and the AI doctor An'an, already shown on outpatient guidance and pre-consultation screens. [[Link](https://www.gamyy.cn/gzb/news/big/113898.html)]
- [2025.09] **ZhiFu Qihuang Tiangong** TCM AI model completes national deep-synthesis algorithm filing for four-diagnosis devices and constitution assessment. [[Link](http://zs.scbzol.com/zs/2025/0919/328624.html)]
- [2025.09] The evaluated model on this page is **Chuanshen Suwen**, which passed CAICT Trusted AI TCM LLM Level 4+. The text says Transn built it on the Rendu base model. [[Link](https://zhongyi.gmw.cn/2025-09/10/content_38277329.htm)]
- [2025.09] The China Academy of Chinese Medical Sciences said that at CIFTIS on 10-14 September 2025 its intelligent-science center showed the Dayi Jinkui LLM and multi-turn inquiry system, plus tongue-diagnosis and mobile TCM testing units. [[Link](https://www.cacms.ac.cn/news_dynamic/detail/5080.html)]
- [2025.08.09] NSCC-TJ and Tianjin University of TCM release **TianHe·LingShu** 2.0 (expanded beyond acupuncture to 20+ specialties) and launch a TCM intelligent-model evaluation system. [[Link](http://tj.people.com.cn/n2/2025/0809/c375366-41317410.html)]
- [2025.08.06] Hubei Daily reported that on 6 August 2025 Hubei University of Chinese Medicine, Hubei Shizhen Laboratory, and Transn signed a cooperation agreement centered on the Chuanshen Suwen TCM model. [[Link](https://news.hubeidaily.net/mobile/c_4393128.html)]
- [2025.08.01] **Gushengtang** releases ten “National Master AI twins” trained on master clinicians' experience. The page reports expert-simulation consistency above 86%, not pattern-differentiation accuracy. [[Link](http://sz.people.com.cn/n2/2025/0801/c202846-41310443.html)]
- [2025.07] Guang'anmen Hospital forms the **GuangYi·QiZhi** LLM agent alliance with medical consortium partners for cross-institution intelligent care. [[Link](https://www.gamyy.cn/gzb/news/big/112751.html)]
- [2025.06.19] **TCM Hengqin** vertical LLM is officially released. [[Link](https://www.stdaily.com/web/gdxw/2025-06/20/content_357526.html)]
- [2025.06.18] The National Data Administration listed a Chengdu University of TCM case that uses a large model to segment and tag 996 classical books and ChatGLM-6B to link TCM terms into graphs such as point-organ relations. [[Link](https://www.nda.gov.cn/sjj/ywpd/szkjyjcss/0618/20250618095629525611799_pc.html)]
- [2025.06.06] Nanjing University of Chinese Medicine said that on 6 June 2025 it released Lingshan TCM Model (Xiao Xingren) and Sushan Chinese Materia Medica Model (Sushan Zhisiti) for clinical, teaching, and research use. [[Link](https://xxjs.njucm.edu.cn/2025/0529/c445a156198/pagem.htm)]
- [2025.05.17] Sichuan Online reported on 17 May 2025 that Chengdu Sport University and Zhongke Shiyu released the Huanshu sports-medicine TCM model and agent, aimed at competitive sport, public health and teaching, including exercise prescriptions and seasonal health plans. This page has not verified weights or a public API. [[Link](https://sichuan.scol.com.cn/ggxw/202505/82968100.html)]
- [2025.05.10] Beijing University of Chinese Medicine said that on 10 May 2025 it released Xinhuo Zhongguoyao Zhisiti 1.0, a education model of more than 70 billion parameters built on iFlytek Spark and DeepSeek. [[Link](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)]
- [2025.05.10] China Academy of Chinese Medical Sciences releases evaluation standards for TCM large models. [[Link](https://www.news.cn/politics/20250510/5e6a0b4978b44b69b67dbfb7282fd220/c.html)]
- [2025.04.11] Ifeng reported that on 11 April 2025, at the Huawei Cloud ecosystem conference, Jiuwei Health released the Jiuwei Shennong TCM agent on the Pangu model for drug R&D, formula optimization, and clinical support. [[Link](https://biz.ifeng.com/c/8iTNRXVw44k)]
- [2025.04] Transn releases **RenDu·SuWen** TCM LLM (mixture-of-entropy architecture) for inquiry, pattern differentiation, and formula recommendation. [[Link](https://www.transn.com/about_us/consult/article/1924766101036437505)]
- [2025.03.28] Guang'anmen Hospital releases **GuangYi·QiZhi**, described as the first TCM hospital with integrated local compute + model + application deployment. [[Link](https://www.xinhuanet.com/tech/20250328/8b1685ad8c6f48c9bdc2add1658edac3/c.html)]
- [2025.03.13] Xinhua reported that on 13 March 2025 Huang Huang's team at Nanjing University of Chinese Medicine and Hangzhou Maijing Health released an AI system that combines an LLM and a knowledge graph to operationalize formula-person matching. [[Link](http://www.js.xinhuanet.com/20250314/aa816bb98d1041afa0fa7bca45583d1b/c.html)]
- [2025.03] Hefei Yunzhen said it released the Yunzhen Huayi TCM model on its TongueLMM tongue model and DeepSeek-R1 for syndrome differentiation, constitution assessment, and report generation. [[Link](https://www.ai-tongue.com/pages/news/2025/04/9a6f1920-4819-406e-8d1f-6ba0b838a7f8.html)]
- [2025.01.08] On 8 January 2025, the University of Science and Technology Beijing and Henan University of Chinese Medicine released Zhang Zhongjing TCM Large Model 1.0 for syndrome differentiation, syndrome-element recommendation, classical formulas, and formula analysis. [[Link](https://news.ustb.edu.cn/info/1087/67760.htm)]

</details>

<details>
<summary>2024 · 5</summary>

- [2024.12] China UnionPay Consumer Finance with Sun Yat-sen University and GZUCMS Shenzhen Hospital release vertical TCM LLM **ZhongSi** for community clinic inquiry. [[Link](https://finance.sina.com.cn/jjxw/2024-12-16/doc-inczrzsp5791684.shtml)]
- [2024.11] ECNU, Shanghai University of Traditional Chinese Medicine, East China University of Science and Technology, Naval Medical University, Lingang Laboratory, and CR Jiangzhong built **ShuZhi QiHuang**. Version 1.0 came out on 19 January 2024. On 25 November 2024 they introduced version 2.0 at a forum in Shanghai. [[Link](https://pharm.ecnu.edu.cn/08/27/c43775a657447/page.htm)]
- [2024.09] Zhongke Wenge releases **DaYi JinKui** TCM LLM and a health platform trained on 1,500+ TCM classics and a large set of clinical cases. [[Link](https://36kr.com/newsflashes/2946967562099592)]
- [2024.07.19] The National Administration of Traditional Chinese Medicine and the National Data Administration issued document 6 of 2024 on promoting digital TCM, including data-element development, TCM large models, and smart services. The document is dated 19 July 2024. [[Link](http://www.natcm.gov.cn/bangongshi/zhengcewenjian/2024-08-14/34672.html)]
- [2024.05.10] Tasly and Huawei Cloud release **ShuZhi BenCao** on Pangu language and molecular models. This page does not mention a CAICT Level 4+ evaluation. [[Link](https://www.taslypharma.com/tsl/40931.jhtml)]

</details>

<details>
<summary>2023 · 1</summary>

- [2023.07.29] Nanjing Dajing TCM releases **QiHuang Wendao** LLM with large knowledge graphs and clinical data for institutional beta use. [[Link](http://js.news.cn/20230729/fa034db71a00487b819a4ad95b44673e/c.html)]

</details>


</details>

## Surveys

<details>
<summary>83 surveys, grouped by year</summary>

<details>
<summary>2026 · 36</summary>

- [*兰州大学学报(医学版)*] **从大语言模型到智能体（兰州大学学报医学版综述）** Chinese-language systematic review organized around the LLM-to-agent transition for TCM clinical assisted diagnosis and treatment (J. Lanzhou Univ. Med. Sci. 2026;52(4):49-57). [[DOI](https://doi.org/10.13885/j.issn.2097-681X.T20260032)]
- **Agentic and Knowledge-Grounded LLMs in TCM（预注册）** A review plan registered on OSF in July 2026. It will look at agentic and knowledge-grounded language models in TCM through evidence maps, text mining, and whether they are ready for clinical use. The review is still underway. [[Link](https://doi.org/10.17605/osf.io/kq8jx)]
- [*International Journal of Pattern Recognition and Artificial Intelligence*] **中医大模型关键技术综述（IJPRAI）** Survey of key technologies for TCM LLMs: knowledge organization, aided diagnosis, and clinical decision support (formally published in IJPRAI, World Scientific). [Guangdong Provincial Hospital of Traditional Chinese Medicine, Guangdong University Of Finances and Economics, Guangdong University of Finance] [[DOI](https://doi.org/10.1142/s0218001426590263)]
- [*Journal of Traditional Chinese Medical Sciences*] **AI驱动中医诊断智能化综述（JTCMS）** Survey on multimodal fusion and LLMs for intelligent four-diagnosis in TCM: applications, challenges and outlook (JTCMS). [[DOI](https://doi.org/10.1016/j.jtcms.2026.05.002)]
- [*上海中医药杂志*] **人工智能驱动下的中医智能诊疗研究进展与挑战** Chinese review structured on the six-step TCM diagnosis-treatment chain (four diagnoses, pattern differentiation, prescription, outcome prediction), contrasting supervised/unsupervised/RL/deep-learning paradigms (Shanghai J. TCM 2026;60(1)). [[DOI](https://doi.org/10.16305/j.1007-1334.2026.z20250609004)]
- [*Chinese Science Bulletin*] **面向临床的中西药联用安全性数智评价** A clinical framework for safety of combined Chinese and western drugs: prediction, risk detection, mechanism checks, and decision support before and during use. [[DOI](https://doi.org/10.1360/csb-2026-0084)]
- [*Communications in Computer and Information Science (Springer)*] **多模态大模型驱动舌脉面诊智能化综述（Springer 书章）** The only review text dedicated to multimodal-LLM-driven tongue, pulse, and facial diagnosis in TCM (Springer CCIS book chapter; weaker peer review than journals). [Chinese Academy of Social Sciences, Institute of Ethnology and Anthropology, University of Chinese Academy of Social Sciences] [[DOI](https://doi.org/10.1007/978-981-95-7299-1_15)]
- [*中华中医药学刊*] **人工智能赋能中医数字化诊断：现状与挑战（中华中医药学刊）** A short essay on what AI can do for digital TCM diagnosis, and on data quality, explanations, and joining the models to TCM theory. Published in Chinese Archives of Traditional Chinese Medicine. [[DOI](https://doi.org/10.13193/j.issn.1673-7717.2026.01.004)]
- [*Chinese Medicine*] **中医为何需要可解释人工智能** Argues that TCM AI is limited by a mismatch between statistical models and syndrome-based reasoning, so explanations are required. [[DOI](https://doi.org/10.1186/s13020-026-01455-4)]
- [*Healthcare*] **东亚传统医学如何进入国际卫生信息标准** Scoping review of English reports from January 2016 to March 2026 on how Korean medicine, TCM, and Kampo concepts are mapped into mainstream health-informatics standards. [[DOI](https://doi.org/10.3390/healthcare14183011)]
- [*Integrative Medicine Research*] **Yao et al. 2026: LLM 与循证中医整合（Scoping Review）** PRISMA scoping review (12 studies, 2022-11 to 2026-01) on integrating LLMs with evidence-based Chinese medicine. [University of Geneva, Gansu University of Traditional Chinese Medicine, Lanzhou University] [[DOI](https://doi.org/10.1016/j.imr.2026.101349)]
- [*Journal of Pharmaceutical Analysis*] **Xu et al. 2026: 基于 LLM 的中医智能问答系统综述** Review of intelligent TCM question-answering systems based on LLMs (KG-QA to LLM-QA and RAG). [Tianjin haihe hospital] [[DOI](https://doi.org/10.1016/j.jpha.2025.101406)]
- [*Engineering*] **XiangShu Omics: A Framework Based on the Spatio–Temporal Field Rhythms of Human Life and Systems Intelligence Methodology** This review says it is the first to systematically construct XiangShu omics, and states that its large model integrates large language models grounded in the classical logic of principle, method, formula, and medicine, such as Shu-Zhi Qihuang. [[DOI](https://doi.org/10.1016/j.eng.2026.02.018)]
- [*Artificial Intelligence Review*] **Wu et al. 2026: AI 在中药材中的应用综述** Full-stack survey of AI in TCM herbs — compounds, targets, quality control, with an LLM section. [Northeastern University, First Hospital of China Medical University, China Medical University, Liaoning University] [[DOI](https://doi.org/10.1007/s10462-026-11513-w)]
- [*Medical Review*] **Wang et al. 2026: 重思中医大模型评测** Argues that TCM LLM evaluation still lacks a quality floor: unfiltered classics and web text can contain outdated advice, and a single case is not a benchmark. [[DOI](https://doi.org/10.1515/mr-2026-0006)]
- [*Chinese Medicine*] **Wang et al. 2026: 人工智能在中医药研发中的发展与应用综述** A review published on 8 January 2026 in Chinese Medicine by Wang, Luo, and colleagues on the development and application of AI in TCM research and development, covering drug design, manufacturing, and market access, plus limitations and future directions. [[DOI](https://doi.org/10.1186/s13020-025-01288-7)] [[Paper](https://link.springer.com/article/10.1186/s13020-025-01288-7)]
- [*Chinese Herbal Medicines*] **Sun et al. 2026: 生成模型在中医药中的进展与应用** Reviews advances and applications of generative models in traditional Chinese medicine. [[DOI](https://doi.org/10.1016/j.chmed.2026.08.013)]
- [*Information*] **Lu et al. 2026: 深度学习中医诊断方法学质量审计** Systematic review and validation-gap analysis of deep learning for TCM disease diagnosis. [[DOI](https://doi.org/10.3390/info17060554)]
- [*ACL 2026*] **LLM-Based Multi-Agent Systems for Clinical Workflows（ACL 2026，邻近）** Adjacent ACL 2026 survey of workflow-level multi-agent clinical systems with a four-layer evaluation stack; no TCM coverage but methodologically isomorphic process-evaluation claims. [Sanford Health, University of Massachusetts Lowell, University of Massachusetts Amherst] [[DOI](https://doi.org/10.18653/v1/2026.acl-long.2123)]
- [*Chinese Medicine*] **Han et al. 2026: LLM 在中医中的调优与临床应用（Scoping Review）** PRISMA-ScR scoping review (27 studies to 2025-05) on tuning (LoRA/CPT/RAG) and clinical application of TCM LLMs. [Jining Traditional Chinese Medicine Hospital] [[DOI](https://doi.org/10.1186/s13020-026-01346-8)]
- [*Chinese Medicine*] **Guo et al. 2026: AI 与多模态数据融合推动中医现代化** Panoramic AI review (ML/DL/KG/NLP/LLM) for TCM modernization with multimodal data integration. [Ningbo College of Health Sciences, Shenzhen Second People's Hospital, Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1186/s13020-025-01194-y)]
- [*Chinese Medicine and Culture*] **From Empirical Wisdom to Computational Intelligence: A Knowledge-Data Dual-Driven Paradigm for Modernizing Traditional Chinese Medicine** The paper proposes a knowledge–data dual-driven paradigm that turns implicit traditional Chinese medicine experience into computable structure with large-scale knowledge graphs and TCM-specific large language models, and digitizes the four examinations into a multimodal TCM phenomics. [[DOI](https://doi.org/10.1097/mc9.0000000000000198)]
- [*Science of Traditional Chinese Medicine*] **Dong et al. 2026: 中医处方推荐计算方法综述** Reviews computational herbal-prescription recommendation and how it can support TCM clinical decisions. [[DOI](https://doi.org/10.1097/st9.0000000000000110)]
- [*Journal of Integrative Medicine*] **Deep learning in TCM（J Integr Med）** Single-technology review of deep learning in TCM: medical imaging, herbal material research, data mining (J. Integr. Med. 2026;24(4):471-480). [[DOI](https://doi.org/10.1016/j.joim.2026.03.001)]
- [*OSF Registries*] **Cong H et al. 中医古籍知识挖掘范围综述（OSF 预注册）** A scoping-review plan registered on OSF on 15 April 2026. It will map how knowledge graphs, large language models, and the two together are used to draw knowledge out of TCM classics, following PRISMA-ScR. The review is still underway. [[DOI](https://doi.org/10.17605/osf.io/5z367)]
- [*Science of Traditional Chinese Medicine*] **Chen et al. 2026: LLM 在中医的下一步（叙述性综述）** Narrative review on the next step of LLMs in TCM — multimodality, agents, and clinical translation. [[DOI](https://doi.org/10.1097/st9.0000000000000109)]
- [*OSF Registries*] **Cai R et al. 中医辨证分类范围综述（OSF 预注册）** A scoping-review plan registered on OSF on 3 April 2026. It will map how large language models do TCM syndrome differentiation, syndrome elements, and syndrome reasoning, and will be written to PRISMA-ScR. The review is still underway. [[DOI](https://doi.org/10.17605/osf.io/2hyeq)]
- [*Intelligence-Based Medicine*] **Artificial intelligence: A catalyst for the modernization of traditional Chinese medicine** This scoping review searched PubMed, Web of Science, and CNKI through 2025 and states that deep learning and large language models show promising accuracy on tongue-image analysis and syndrome differentiation, in some studies approaching expert-level performance. [[DOI](https://doi.org/10.1016/j.ibmed.2026.100415)]
- [*Journal of Advanced Research*] **AI-driven multi-scale target analysis of traditional Chinese medicine: From the pharmacological effects of single compounds to the synergistic mechanisms of formulae** This review of multi-scale traditional Chinese medicine target analysis lists the development of TCM-specific large language models among its future directions, in order to decode TCM pharmacological logic. [[DOI](https://doi.org/10.1016/j.jare.2026.03.050)]
- [*Pharmacological Research - Modern Chinese Medicine*] **AI in TCM: multimodal data to pharmacology and clinical decision（PRMCM 综述）** An English review that runs from multimodal data and pharmacology to clinical decisions. Pharmacological Research - Modern Chinese Medicine, 2026. [Saveetha University] [[DOI](https://doi.org/10.1016/j.prmcm.2026.100842)]
- [*Research*] **AI in TCM: Unraveling Herbal Medicine's Mechanisms（Research）** Broad AI-in-TCM review arguing AI should move beyond correlational analysis toward reconstructing the biological logic of syndrome differentiation and formula compatibility (Research 2026;9:1224). [Zhejiang Chinese Medical University] [[DOI](https://doi.org/10.34133/research.1224)]
- [*Journal of Integrative Medicine*] **AI empowers the innovation of TCM（J Integr Med 评论）** Single-author perspective on AI for TCM innovation: classics mining, diagnosis standardization, drug R&D cycles (J. Integr. Med. 2026). [[DOI](https://doi.org/10.1016/j.joim.2026.05.004)]
- [*Chinese Medicine and Culture*] **AI and Big Data in TCM Standardization and Internationalization（Chin Med Cult）** An essay on how AI and big data can help standardize traditional Chinese medicine and carry it abroad. Chinese Medicine and Culture, 2026, volume 9, issue 3. [[DOI](https://doi.org/10.1097/mc9.0000000000000203)]
- [*Science of Traditional Chinese Medicine*] **2026: 面向中医药证据知情决策的数字智能循证** Discusses digital intelligent evidence-based methods for evidence-informed decisions in Chinese medicine. [University of Geneva] [[DOI](https://doi.org/10.1097/st9.0000000000000105)]
- [*Science of Traditional Chinese Medicine*] **2026: 数字化与智能化时代的中医药机遇与挑战** Discusses opportunities and challenges for TCM as AI moves from expert systems to deep learning and large language models. [[DOI](https://doi.org/10.1097/st9.0000000000000102)]
- [*Digital Chinese Medicine*] **2026: 中医智能诊断的跨学科融合与发展趋势** Discusses interdisciplinary integration and development trends of intelligent diagnosis in TCM. [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.001)]

</details>

<details>
<summary>2025 · 28</summary>

- [*协和医学杂志*] **陈子佳 et al. 2025: 大语言模型在中医药领域的应用、挑战与前景** A 2025 review in Medical Journal of Peking Union Medical College Hospital on LLM applications in TCM diagnosis, consultation, and formula research, together with challenges in values and misuse, interpretability, technical gaps, and regulatory access. [[DOI](https://doi.org/10.12290/xhyxzz.2024-0315)] [[Paper](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2024-0315)]
- [*Pharmaceuticals*] **评估药物–草药相互作用的人工智能工具** Review of artificial-intelligence models and tools for assessing drug–herb interactions. [[DOI](https://doi.org/10.3390/ph18030282)]
- [*iScience*] **计算机辅助穴位定位系统综述** Systematic review of traditional algorithms and deep learning for acupoint localization across anatomical regions. [[DOI](https://doi.org/10.1016/j.isci.2025.113708)]
- [*Chinese Medicine*] **肿瘤治疗中的草药–化学药相互作用** Review of herb–drug interactions in oncology, covering pharmacodynamic and pharmacokinetic mechanisms and risk prediction. [[DOI](https://doi.org/10.1186/s13020-025-01156-4)]
- [*Chinese Medicine*] **深度学习穴位定位综述** Review of deep-learning acupoint localization, grouped by body region, architecture, strategy, and image modality, including datasets and metrics. [[DOI](https://doi.org/10.1186/s13020-025-01173-3)]
- [*中华中医药学刊*] **杨乐乐 et al. 2025: 大语言模型在中医药领域的应用展望思考** Yang, Zhu, and colleagues review medical LLMs and discuss potential TCM uses in research, knowledge mining, and assisted diagnosis, along with risks, countermeasures, and future directions. [Leipzig University] [[DOI](https://doi.org/10.13193/j.issn.1673-7717.2025.02.004)]
- [*中华中医药学刊*] **叶桦 et al. 2025: 大语言模型赋能中医药传承：前沿进展与应用展望** A November 2025 online-first Chinese review of LLMs for TCM inheritance, covering data mining, clinical decision support, and cultural transmission, plus challenges and outlook. The journal page does not provide a DOI. [[Paper](https://zyhs.cbpt.cnki.net/portal/journal/portal/client/paper/3e19461f3fb08c22b2659ea83eb41d5a)]
- [*Chinese Medicine*] **古籍知识图谱×多智能体融合综述（Chin Med）** Challenges-and-prospects review of knowledge-graph construction over ancient TCM classics, first to frame multi-agent convergence in this area (Chin. Med. 2025;20:168). [[DOI](https://doi.org/10.1186/s13020-025-01226-7)]
- [*智能系统学报*] **医疗领域的大型语言模型综述（智能系统学报，邻近）** Adjacent Chinese general survey of medical LLMs (training pipeline, strategies, scenarios, challenges), a superset-context reference for TCM LLM surveys. [[DOI](https://doi.org/10.11992/tis.202405003)]
- [*智能系统学报*] **医学大语言模型的研发与应用系统综述（智能系统学报，邻近）** Adjacent systematic review of 129 medical-domain LLMs (to 2024-06) and four clinical application categories; methodologically comparable search protocol. [[DOI](https://doi.org/10.11992/tis.202410020)]
- [*上海中医药杂志*] **刘嘉艺 et al. 2025: 生成式人工智能在中医药标准化研究中的应用前景与挑战** A 2025 review in Shanghai Journal of Traditional Chinese Medicine on generative AI for TCM standardization, covering health services, quality improvement, information management, and intelligent diagnosis, plus prospects and challenges. [[DOI](https://doi.org/10.16305/j.1007-1334.2025.z20241121005)] [[Paper](https://shzyyzz.shzyyzz.com/zh/article/doi/10.16305/j.1007-1334.2025.z20241121005/)]
- [*中华中医药学刊*] **人工智能实现中医四诊的发展现状、问题及解决路径（中华中医药学刊）** Reviews where AI stands across the four TCM examinations. Inspection photographs the face, tongue, sublingual vessels, lips, and eyes and quantifies them with segmentation and color models; auscultation and olfaction capture abnormal sounds and odors and analyze them with neural networks and electronic noses. Published in Chinese Archives of Traditional Chinese Medicine, 2025, 43(11). [[Paper](https://www.sinomed.ac.cn/article.do?ui=2026106036)]
- [*AI Medicine*] **Zhang et al. 2025: 中医 LLM 短综述与展望** Short survey and outlook on TCM LLM models and tasks. [Northeastern University] [[DOI](https://doi.org/10.53941/aim.2025.100003)]
- [*Journal of Evidence-Based Medicine*] **Yip et al. 2025: 中西医结合 LLM 进展与挑战** Review of LLMs in integrative medicine — progress, challenges, and opportunities. [Hong Kong Baptist University, Guangdong-Hongkong-Macau Joint Laboratory of Collaborative Innovation for Environmental Quality] [[DOI](https://doi.org/10.1111/jebm.70031)]
- [*Acta Materia Medica*] **Yin et al. 2025: 数据挖掘、大模型与多模态融合的中医AI综述** Reviews AI for TCM across data mining, large language models, and multimodal fusion, aimed at multi-component herbal formulas. [[DOI](https://doi.org/10.15212/amm-2025-0045)]
- [*American Journal of Chinese Medicine*] **Wang et al. 2025: AI 驱动中医诊断模型进展** Overview of AI-driven TCM diagnostic models (four-diagnosis objectification, pattern differentiation). [[DOI](https://doi.org/10.1142/S0192415X25500259)]
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
<summary>2024 · 7</summary>

- [*Engineering*] **系统论框架下整合人工智能与中医药整体物质基础研究（框架综述）** Zeng Jingqi and corresponding author Jia Xiaobin publish a framework review in Engineering (2024, 40(9)) proposing a System Function Decoding Model (SFDM) that connects AI to holistic material-basis research in TCM. It organizes five top-down dimensions and a bottom-up element–structure–function path, and it looks ahead to an end-to-end component-syndrome model and an oral-formulation IVIVC mechanism model. This is not a systematic review; neither technical scheme is implemented or quantitatively evaluated here. The license is CC BY-NC-ND 4.0. The official Chinese version is 25 pages. [[DOI](https://doi.org/10.1016/j.eng.2024.04.009)] [[Paper](https://www.engineering.org.cn/engi/CN/10.1016/j.eng.2024.04.009)]
- [*中草药*] **萧文科 et al. 2024: 中医药大语言模型的关键技术与构建策略** A 2024 monograph-style review in Chinese Traditional and Herbal Drugs on data handling, RAG, mixture of experts, RLHF, distillation, and training or evaluation methods for TCM LLMs, with construction strategies and application scenarios. [[DOI](https://doi.org/10.7501/j.issn.0253-2670.2024.17.001)] [[Paper](http://www.tiprpress.com/zcy/article/pdf/20241701)]
- [*计算机工程与应用*] **Su et al. 2024 — Review of AI in TCM diagnosis and treatment (Chinese)** Chinese-language review of three AI stages in TCM care — expert systems, ML, and deep learning — with challenges. [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2312-0400)]
- [*南京中医药大学学报*] **Li et al. 2024: Research progress and application prospects of large language models in TCM** Chinese-language review of TCM LLM pipelines, frontier techniques (prompting/RAG/RLHF), and application prospects. [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1393)]
- [*Computers in Biology and Medicine*] **Tian et al. 2024: 四诊机器学习综述** Review of machine learning for TCM four diagnoses — inspection, auscultation-olfaction, inquiry, and palpation. [Northeastern University, Ningbo University] [[DOI](https://doi.org/10.1016/j.compbiomed.2024.108074)]
- [*中国工程科学*] **Song et al. 2024: AI 辅助中医辨证关键问题与技术挑战** Strategic-study review of key issues in AI-assisted TCM syndrome differentiation — multimodal fusion, symptom association, pattern quantification and reasoning, and TCM LLMs. [Shanghai University of Engineering Science, Digital China Health (China), Zhejiang Lab] [[DOI](https://doi.org/10.15302/J-SSCAE-2024.02.010)]
- [*Computer Materials & Continua*] **Qu et al. 2024: 中医知识图谱综述** Review of knowledge graphs in TCM — analysis, construction, applications, and prospects. [Beijing Forestry University] [[DOI](https://doi.org/10.32604/cmc.2024.055671)]

</details>

<details>
<summary>2023 · 3</summary>

- [*Chinese Medicine*] **中医药与天然产物中的机器学习：现状与展望** Ma, Liu, and Li (co-first), with corresponding authors Li and Wang, publish a narrative review in Chinese Medicine on machine learning in TCM and natural-product research, describe their team’s coronary-syndrome-element model, and call for combining machine learning, TCM theory, and computational biology. This is not a systematic review; table accuracies come from cited papers. No new code or data are presented. The license is CC BY 4.0. [[DOI](https://doi.org/10.1186/s13020-023-00741-9)] [[Paper](https://cmjournal.biomedcentral.com/articles/10.1186/s13020-023-00741-9)]
- [*Annals of Translational Medicine*] **中医四诊人工智能研究现状与趋势的科学计量研究** Tian, corresponding author Hongwu Wang and colleagues publish a scientometric study in Annals of Translational Medicine (2023, 11(3)) that uses Web of Science, VOSviewer, and CiteSpace to analyze AI literature on the four TCM diagnostic methods. The text reports 136 eligible studies from 2007–2022. This is not a systematic review and has no PRISMA. The license is CC BY-NC-ND 4.0. The official version is 16 pages, DOI 10.21037/atm-22-6431. It is not the same paper as the existing catalog entry surv-tian2024. [[DOI](https://doi.org/10.21037/atm-22-6431)] [[Paper](https://atm.amegroups.org/article/view/109099)]
- [*Current Opinion in Structural Biology*] **中药计算毒性研究小综述** Mini-review of in silico toxicity studies of traditional Chinese herbal medicine. [[DOI](https://doi.org/10.1016/j.sbi.2023.102588)]

</details>

<details>
<summary>2022 · 1</summary>

- [*Frontiers in Pharmacology*] **人工智能在补充替代医学中的应用：系统性范围综述** Chu, corresponding author Youn and colleagues follow JBI and PRISMA-ScR to map AI applications in complementary and alternative medicine. Searching three English databases, they include 32 papers, mainly on acupuncture, tongue and lip diagnosis, and herbal medicine. This is a systematic scoping review, not a meta-analysis. Counts in the text, flowchart, and Table 1 are not fully consistent. No new code or data are presented. The license is CC BY. [[DOI](https://doi.org/10.3389/fphar.2022.826044)] [[Paper](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.826044/full)]

</details>

<details>
<summary>2021 · 2</summary>

- [*Frontiers in Pharmacology*] **人工智能、深度学习与云计算用于中西医诊治类风湿关节炎** Wang and Hou (co-first), with corresponding authors Zhang and Wang, publish a narrative review in Frontiers in Pharmacology on proposed uses of AI, deep learning, and cloud computing for rheumatoid arthritis in traditional and Western medicine, and they offer a conceptual model. This is not a systematic review and not a deployed clinical system. No new code or data are presented. The license is CC BY. [[DOI](https://doi.org/10.3389/fphar.2021.765435)] [[Paper](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2021.765435/full)]
- [*Computers in Biology and Medicine*] **Zhang et al. 2021: 计算中医诊断文献综述** Literature survey of computational TCM diagnosis — symptom acquisition, pattern modeling, and systems. [[DOI](https://doi.org/10.1016/j.compbiomed.2021.104358)]

</details>

<details>
<summary>2020 · 1</summary>

- [*Artificial Intelligence in Medicine*] **Chu et al. 2020: 中医定量知识表示模型综述** Review of quantitative knowledge representation models of TCM (ontologies, rules, statistics). [Xidian University, Xi'an Polytechnic University, Guangdong Polytechnic Normal University, CM Hospital] [[DOI](https://doi.org/10.1016/j.artmed.2020.101810)]

</details>

<details>
<summary>2019 · 1</summary>

- [*Engineering*] **中药安全性研究：方法、应用与展望** Review of why TCM toxicity is hard to study: multi-component formulas and unpredictable drug–body interactions, unlike chemical or biological drugs. [[DOI](https://doi.org/10.1016/j.eng.2018.11.019)]

</details>

<details>
<summary>2018 · 1</summary>

- [*Journal of Clinical and Translational Hepatology*] **中药肝损伤与药物性肝损伤的比较（叙述性综述）** Jing and corresponding author Teschke publish a 2018 narrative review in the Journal of Clinical and Translational Hepatology comparing herb-induced liver injury, including Chinese herbal medicines, with chemical drug-induced liver injury in epidemiology, clinical features, and RUCAM grading. This is not a systematic review; the main comparison tables restate existing cohorts. There are wording and number conflicts between the abstract and Table 4, and between the text and Table 6 / Figure 2. The license is CC BY-NC 4.0. [[DOI](https://doi.org/10.14218/JCTH.2017.00033)] [[Paper](https://www.xiahepublishing.com/ArticleFullText.aspx?sid=2&jid=1&id=10.14218%2fJCTH.2017.00033)]

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
<summary>73 patents, grouped by publication year</summary>

<details>
<summary>2026 · 33</summary>

- [*CN122531762A*] **基于生成式模拟医案构建的定制化中医处方推荐大模型** A rule engine enumerates structured TCM features, an LLM turns them into simulated cases, and those cases fine-tune a customized prescription model (published, not granted). [[Patent](https://patents.google.com/patent/CN122531762A/zh)]
- [*CN122529089A*] **TCM dialogue generation with a large language model and long-term memory** Generates personalized TCM dialogue from a long-term memory bank and user portrait (published, not granted). [Hangzhou Wangchai Technology] [[Patent](https://patents.google.com/patent/CN122529089A/zh)]
- [*CN122508432A*] **一种面向中医药知识图谱的综合质量评估方法** Sends a small sample to a TCM-tuned large model for a preliminary quality check of a TCM knowledge graph (published, not granted). [[Patent](https://patents.google.com/patent/CN122508432A/zh)]
- [*CN122599028A*] **一种基于AI大模型的中医天地岁人四维辨证辅助诊疗系统** Combines multi-site pressure-level pulse signals, temporal rhythm encoding and constitution classification for herb/acupoint recommendations. Published 18 August 2026 and listed Pending; this is a disclosed technical proposal. [Gaobele Biotech Guangzhou Co ltd] [[Patent](https://patents.google.com/patent/CN122599028A/zh)]
- [*CN122436154A*] **Digital inheritance and analysis of Zhang Xichun's theory, method, formula, and herbs** Rule engine plus three-way retrieval and an LLM for Zhang Xichun school analysis (published, not granted). [Guangzhou Zhiyun Caotang Medical Technology] [[Patent](https://eureka.patsnap.com/patent/CN122436154A)]
- [*CN122436116A*] **基于知识图谱与大语言模型的脾胃学派理法方药分析系统** Combines a spleen-stomach school knowledge graph, vector retrieval, and an LLM for formula selection, safety checks, and prescription writing (published, not granted). [[Patent](https://patents.google.com/patent/CN122436116A/zh)]
- [*CN122436251A*] **一种融合时空特征的针灸推理模型构建方法、系统及设备** Aligns four-examination and course features, retrieves past acupuncture plans, and uses a fine-tuned LLM with chain-of-thought for an explainable plan (published, not granted). [[Patent](https://patents.google.com/patent/CN122436251A/zh)]
- [*CN121436110B*] **一种基于知识图谱的中医垂域大模型的训练方法** Uses syndrome/symptom keyword sets, confusable tuples and contextual disambiguation to prepare pretraining text. The A publication’s timeline records the B grant on 31 July 2026; technical description here is based on A because B text was not retrieved. [Daan Health Technology Beijing Co ltd] [[Grant](https://patents.google.com/patent/CN121436110B/zh)] [[Publication](https://patents.google.com/patent/CN121436110A/zh)]
- [*CN122364665A*] **一种基于大语言模型的中医古籍症状标准化处理方法** An LLM finds candidate symptom spans in sliced classical TCM texts and maps them into a standard symptom semantic field (published, not granted). [[Patent](https://patents.google.com/patent/CN122364665A/zh)]
- [*CN122135923A*] **辅助诊断结果和参考处方生成方法、装置、介质及计算机设备** Recalls case records and treatment rationales through vector and text paths, four routes in all, then a large model drafts TCM diagnosis, syndrome pattern, a Western diagnosis, and a herbal prescription. Published on 2 June 2026 and not yet granted. [[Patent](https://eureka.patsnap.com/patent/CN122135923A)]
- [*CN122245713A*] **基于大语言模型的中医智能问诊方法及系统** Intent is parsed from multimodal inquiry data, then dual-path retrieval over TCM knowledge produces the consultation result (published, not granted). [[Patent](https://patents.google.com/patent/CN122245713A/zh)]
- [*CN120913881B*] **基于多模态中医大语言模型的数据分析方法、系统、终端及介质** Trains a multimodal TCM large model on tongue images, speech, and inquiry text, then outputs a preliminary TCM analysis. Granted on 12 June 2026. [[Patent](https://eureka.patsnap.com/patent/CN120913881B)]
- [*CN122135936A*] **一种面向中医方剂推荐的知识图谱大模型问答方法及系统** Encodes a case with a Chinese instruction LLM, fuses it with a dynamic TCM knowledge graph, and returns formula recommendations as answers (published, not granted). [[Patent](https://patents.google.com/patent/CN122135936A/zh)]
- [*CN122025029A*] **Causal contrastive learning and LLM graph attention for TCM prescription recommendation** Heterogeneous and homogeneous symptom-herb graphs plus an LLM-enhanced causal mechanism (published, not granted). [Huzhou University] [[Patent](https://eureka.patsnap.com/patent/CN122025029A)]
- [*CN122050861A*] **TCM diagnosis-and-treatment platform combining an LLM with dual-channel retrieval** LLM plus TCM knowledge-graph dual-channel retrieval for inheriting master-physician experience and generating formulas (published, not granted). [Yueyang Hospital of Integrated Traditional Chinese and Western Medicine, SHUTCM, Shanghai Skin Disease Hospital] [[Patent](https://patents.google.com/patent/CN122050861A/zh)]
- [*CN120913769B*] **基于多模态大模型的中医舌诊药饮推荐方法** A multimodal model turns a tongue image into a condition description and a medicinal-drink recommendation. Published on 7 November 2025 and granted on 29 May 2026. [[Patent](https://patents.google.com/patent/CN120913769B/zh)]
- [*CN122117314A*] **LLM-based intelligent acupuncture diagnosis agent** Acupuncture knowledge bases, graph, vector search and reranking, with an LLM agent that classifies questions and asks follow-ups (published, not granted). [Henan University of Technology] [[Patent](https://eureka.patsnap.com/patent/CN122117314A)]
- [*CN121436111B*] **一种基于多模态数据融合的中医智能辨证模型训练系统及方法** Organizes diagnosis through symptom chains, pattern-factor scores, logical combinations and contradiction checks. Granted 15 May 2026 and listed Active. The claims concern structured reasoning, not a released LLM checkpoint. [Daan Health Technology Beijing Co ltd] [[Patent](https://patents.google.com/patent/CN121436111B/zh)]
- [*CN122091073A*] **Multi-task joint optimization for TCM prescription generation** A pretrained LLM predicts herb sequences and herb sets jointly, with extra weight on rare herbs (published, not granted). [Hangzhou Dianzi University] [[Patent](https://eureka.patsnap.com/patent/CN122091073A)]
- [*CN122050683A*] **一种基于图注意力网络与大语言模型的中药处方生成方法** Herbal prescription generation is cast as multi-label classification, with graph attention and an LLM modeling drug synergy and contraindications. Published on 15 May 2026. [[Patent](https://patents.google.com/patent/CN122050683A/zh)]
- [*CN121862376A*] **Knowledge-graph and LLM system for TCM syndrome-differentiation QA** Chunks classics and cases, extracts a graph, then retrieves local and global keywords for syndrome-differentiation answers (published, not granted). [Nanjing University of Posts and Telecommunications] [[Patent](https://patents.google.com/patent/CN121862376A/zh)]
- [*CN121687367A*] **Structured evidence-subgraph RAG for TCM herb recommendation** Multi-hop evidence subgraphs plus Hopfield associative retrieval for herb recommendation, with graph constraints against hallucination (published, not granted). [Zhejiang Chinese Medical University] [[Patent](https://patents.google.com/patent/CN121687367A/zh)]
- [*CN121743505A*] **Knowledge-enhanced generation of TCM case commentaries** Retrieves knowledge-graph subgraphs, then writes case notes along etiology, treatment principles, formulas, and prognosis (published, not granted). [Zhejiang University] [[Patent](https://patents.google.com/patent/CN121743505A/zh)]
- [*CN121709160A*] **一种基于视觉语言模型的中医舌诊智能分析方法** Fine-tunes Qwen-VL with tongue-diagnosis prompts so a tongue image yields structured color and coating labels plus a natural-language reading (published, not granted). [[Patent](https://patents.google.com/patent/CN121709160A/zh)]
- [*CN121480736A*] **Knowledge-distillation and RL for oncology TCM prescription recommendation** Distills GPT-4o into a Qwen student, then DPO, for interpretable oncology TCM prescriptions (published, not granted). [Nanjing University of Chinese Medicine] [[Patent](https://patents.google.com/patent/CN121480736A/zh)]
- [*CN121524286A*] **一种心血管疾病的基于针灸诊疗知识图谱的智能问答系统** Builds a cardiovascular acupuncture knowledge graph and sends hits to a cloud LLM for wording; if retrieval fails, the LLM answers with a caution (published, not granted). [[Patent](https://patents.google.com/patent/CN121524286A/zh)]
- [*CN121562809A*] **一种基于动态语义分块、知识图谱与多跳路径规划的中医大语言模型AI题库智能生成方法及系统** Chunks TCM text, plans multi-hop paths on a knowledge graph, and trains a large model to generate a TCM question bank (published, not granted). [[Patent](https://patents.google.com/patent/CN121562809A/zh)]
- [*CN121460056A*] **一种基于人工智能的方剂配制方法、系统、介质和设备** An LLM maps case entities to disease and syndrome, drafts a formula, scores it, and regenerates from structured advice until the score passes (published, not granted). [[Patent](https://patents.google.com/patent/CN121460056A/zh)]
- [*CN121460113A*] **一种基于中医语言大模型的中医智能分析方法及系统** LoRA-tunes a TCM language model that maps syndrome and chief complaint to a formula (published, not granted). [[Patent](https://patents.google.com/patent/CN121460113A/zh)]
- [*CN121393746A*] **基于大语言模型的经络辨证与针灸方案生成方法及系统** Multi-source clinical data are quantified and cleaned, then a meridian-syndrome knowledge base and an LLM generate acupuncture plans. Published on 23 January 2026. [[Patent](https://patents.google.com/patent/CN121393746A/zh)]
- [*CN121281871A*] **基于医学大语言模型多智能体的中医药临床数据自动化处理系统** Coordinates task-understanding and data-governance agents with a clinical processing toolkit for TCM outcome research. Published 6 January 2026; Google Patents lists Pending. [[Patent](https://patents.google.com/patent/CN121281871A/zh)]
- [*CN121331451A*] **一种融合舌象、心率及文本的多模态健康状态评估方法** Takes tongue image as the main signal, adds heart rate and self-reported text, and prompts DeepSeek to write a health-status assessment (published, not granted). [[Patent](https://patents.google.com/patent/CN121331451A/zh)]
- [*CN121436134A*] **Multimodal knowledge-graph construction from TCM texts and records** An LLM extracts triples from TCM texts, then fuses a real-world case layer into a multimodal graph (published, not granted). [Hangzhou Ganzhicao Technology] [[Patent](https://patents.google.com/patent/CN121436134A/zh)]

</details>

<details>
<summary>2025 · 25</summary>

- [*CN121210613A*] **基于检索增强生成的针灸大模型构建方法、系统及装置** An acupuncture LLM answers questions from vector-retrieved knowledge snippets and, for diagnosis requests, retrieves treatment entries from an acupuncture-plan library. Published on 26 December 2025. [[Patent](https://patents.google.com/patent/CN121210613A/zh)]
- [*CN120690391B*] **Knowledge-graph recommendation of classic TCM formulas** Maps colloquial symptoms to terms, filters by constitution, and recommends classic formulas. Granted on 16 December 2025. [Shunfu Technology Group] [[Patent](https://patents.google.com/patent/CN120690391B/zh)]
- [*CN121212280A*] **一种基于大语言模型的人-信息-物理三元数据融合中药制造知识图谱构建系统、电子设备及存储介质** An LLM extracts triples from manufacturing text under TCM term and relation constraints, then a human-cyber-physical ontology assembles a manufacturing knowledge graph. Published on 25 December 2025. [[Patent](https://patents.google.com/patent/CN121212280A/zh)]
- [*CN121096596A*] **一种基于多模态大语言模型的中医临床辅助决策系统和方法** Tongue-image features are fused with clinical text, similar cases are retrieved, and a multimodal LLM drafts syndrome, diagnosis, herbal prescription, and reasoning. Published on 9 December 2025. [[Patent](https://patents.google.com/patent/CN121096596A/zh)]
- [*CN121034544A*] **融合动态知识图谱的针灸大模型辨证方法及调理优化系统** A dynamically updated acupuncture knowledge graph is combined with time-series clinical features, graph attention, and reinforcement learning to differentiate syndromes and draft acupuncture plans. Published on 28 November 2025. [[Patent](https://patents.google.com/patent/CN121034544A/zh)]
- [*CN120998428A*] **大小模型协同中药方剂优化方法、系统、终端及存储介质** A formula-optimization LLM proposes a macro revision, a smaller pharmacologic model traces constituent herbs, and the two are merged into a final formula. Published on 20 November 2025 and not yet granted. [[Patent](https://patents.google.com/patent/CN120998428A/zh)]
- [*CN120809097A*] **基于大语言模型的中医五音疗疾个性化音乐生成系统及其构建方法** An LLM first performs TCM syndrome differentiation, then generates personalized five-tone therapy music under tonal constraints. Published on 17 October 2025. [[Patent](https://patents.google.com/patent/CN120809097A/zh)]
- [*CN120674039A*] **针灸穴位推荐方法及其模型获取方法、装置、设备及介质** Trains a language model on medical records so symptoms map to acupuncture points, then applies parameter tuning and policy optimization (published, not granted). [[Patent](https://patents.google.com/patent/CN120674039A/zh)]
- [*CN120337029A*] **一种基于大模型的中药分类方法** Entities from multi-source herbal data are mapped to modern pharmacological indicators, then a pretrained large model is adaptively fine-tuned to classify herbs. Published on 18 July 2025. [[Patent](https://patents.google.com/patent/CN120337029A/zh)]
- [*CN120299726A*] **一种基于大模型智能体协作规划的中医诊断场景模拟方法** Turns unstructured case records into structured knowledge, then patient, doctor, assistant, and expert agents collaborate to simulate a TCM diagnostic encounter. Published on 11 July 2025 and not yet granted. [[Patent](https://eureka.patsnap.com/patent/CN120299726A)]
- [*CN120108651A*] **基于胸肺科中医问诊报告大语言模型的中医方剂推荐方法和系统** Shared knowledge domains fine-tune a chest-and-lung TCM inquiry LLM that outputs constitution and symptom parameters and recommends food-medicine formulas. Published on 5 June 2025. [[Patent](https://patents.google.com/patent/CN120108651A/zh)]
- [*CN120108694A*] **Knowledge-graph and case-enhanced RAG for intelligent TCM inquiry** Leiden subgraph search plus hybrid global/local recall, then a single LLM response (published, not granted). [Jiangsu University] [[Patent](https://patents.google.com/patent/CN120108694A/zh)]
- [*CN120216657A*] **基于大语言模型的中药药物警戒问答系统的构建方法** A Chinese-materia-medica knowledge base trains the pharmacovigilance RAG model PV-RAG to answer natural-language safety questions. Published on 27 June 2025. [[Patent](https://patents.google.com/patent/CN120216657A/zh)]
- [*CN120221058A*] **Multimodal knowledge-graph and LLM system for TCM rehabilitation diagnosis** Aligns tongue, pulse, and inquiry features with knowledge-graph embeddings before a rehabilitation expert LLM (published, not granted). [Zhejiang Chinese Medical University] [[Patent](https://patents.google.com/patent/CN120221058A/zh)]
- [*CN120067279B*] **AI-LLM method and system for intelligent TCM inquiry** Multimodal inquiry fusing face, body, and tongue images, speech prosody, and a disease library. Granted on 27 June 2025. [Yi Mai Artificial Intelligence Medical Technology (Tianjin)] [[Patent](https://patents.google.com/patent/CN120067279B/zh)]
- [*CN120148827A*] **一种基于大模型的心血管疾病医疗决策支持方法** A pretrained large model fuses TCM syndrome knowledge with a Western pathology graph and proposes cardiovascular decisions that include Western drugs, Chinese herbal formulas, and non-drug measures. Published on 13 June 2025 and not yet granted. [[Patent](https://eureka.patsnap.com/patent/CN120148827A)]
- [*CN119941636A*] **中医药多模态LLM训练方法及其应用** Extracts tongue-coating and pulse features, fuses them with text by cross-modal attention, and trains a multimodal TCM large language model. Published on 6 May 2025. [[Patent](https://patents.google.com/patent/CN119941636A/zh)]
- [*CN119811630A*] **应用大语言模型的泌尿科中医问诊结果预测方法和系统** An LLM predicts core lesion keywords from urological TCM inquiry text and adjusts its parameters from recorded feedback. Published on 11 April 2025. [[Patent](https://patents.google.com/patent/CN119811630A/zh)]
- [*CN119905208A*] **基于多源特征融合的中医方剂智能推荐方法、介质和设备** Blends content-based recommendation, collaborative filtering, and an LLM reading of symptom text to rank personalized formulas (published, not granted). [[Patent](https://patents.google.com/patent/CN119905208A/zh)]
- [*CN119763764A*] **LLM-based Chinese-medicine prescription recommendation with soft prompts** Soft prompts and cross-attention feed patient text into an LLM for controllable herb recommendations (published, not granted). [Hangzhou Ganzhicao Technology] [[Patent](https://patents.google.com/patent/CN119763764A/zh)]
- [*CN119811698A*] **一种基于OCR识别和大模型的中药方数据解析方法及装置** Handwritten herbal prescriptions are OCR'd into prompts on incompatibility, dosage, and administration, which a large model scores into an overall judgment. Published on 11 April 2025. [[Patent](https://patents.google.com/patent/CN119811698A/zh)]
- [*CN119416782A*] **LLM method for learning famous-physician TCM formulas** Aligns classical-Chinese case terms with vernacular text using models such as Qwen (published, not granted). [Chengdu Byte Stream Technology] [[Patent](https://patents.google.com/patent/CN119416782A/zh)]
- [*CN119517372A*] **一种基于大语言模型的中医问答系统及方法** A dataset built from TCM literature trains an LLM that takes a user's medical question and returns a dialogue answer. Published on 27 February 2025. [[Patent](https://patents.google.com/patent/CN119517372A/zh)]
- [*CN119446558A*] **一种基于大语言模型的中医知识图谱生成方法及系统** A model trained on herbal and consultation data visualizes treatment options for a patient and is updated from outcome ratings. Published on 17 February 2025. [[Patent](https://patents.google.com/patent/CN119446558A/zh)]
- [*CN119252469A*] **一种用于智能中医系统的大语言模型的构建方法** Labeled tongue images and historical records train a tongue-inquiry model used to construct an LLM for an intelligent TCM system. Published on 7 January 2025. [[Patent](https://patents.google.com/patent/CN119252469A/zh)]

</details>

<details>
<summary>2024 · 15</summary>

- [*CN119149754A*] **LLM and knowledge-graph method for TCM formula compatibility** Pairs a TCM LLM with a knowledge graph for formula compatibility (published, not granted). [Tianjin University, Tianda Zhitu (Tianjin) Technology] [[Patent](https://patents.google.com/patent/CN119149754A/zh)]
- [*CN119069137A*] **利用AI大模型进行舌象分析的方法及装置** Uses a large model to read tongue images by constitution, symptoms, and an overall interpretation (published, not granted). [[Patent](https://patents.google.com/patent/CN119069137A/zh)]
- [*CN119092157B*] **LLM-based Chinese-materia-medica question answering** Chinese-materia-medica QA fine-tuned from Baichuan2-7B-Chat. Granted on 7 February 2025. [Zhejiang University, Yangtze River Delta Wisdom Oasis Innovation Center] [[Patent](https://patents.google.com/patent/CN119092157B/zh)]
- [*CN119049664A*] **基于AI大模型的中医元气充盈智能健康管理系统** Converts wearable signals into TCM terms and passes them to a TCM large model (published; deemed withdrawn on 6 February 2026). [[Patent](https://patents.google.com/patent/CN119049664A/zh)]
- [*CN119049665A*] **基于AI大模型智能人体域网的中医六经辨证智能对话健康管理系统** A six-meridian TCM dialogue system over a body-area network and a large model (published; deemed withdrawn on 6 February 2026). [[Patent](https://patents.google.com/patent/CN119049665A/zh)]
- [*CN118899077A*] **一种基于多模态大模型的中医舌诊分析系统及方法** TongueAI builds tongue- and face-image readings, multi-turn questions, and constitution-reasoning data, then instruction-tunes TongueLMM for those three tasks. Published on 8 November 2024. [[Patent](https://patents.google.com/patent/CN118899077A/zh)]
- [*CN118838996A*] **Building a TCM QA system from a large language model and a knowledge graph** Closed loop of LLM generation and knowledge-graph completion for TCM QA (published, not granted). [Beijing Institute of Technology, BIT Tangshan Research Institute] [[Patent](https://patents.google.com/patent/CN118838996A/zh)]
- [*CN118430833A*] **一种基于大语言模型的中医知识深度挖掘方法** Retrieval augmentation and model fine-tuning are trained together so the system can explain TCM terms and syndromes and suggest treatment from a patient query (published, not granted). [[Patent](https://patents.google.com/patent/CN118430833A/zh)]
- [*CN117828050B*] **Long-document retrieval-augmented generation for TCM question answering** Long-document RAG for TCM question answering, with expansion, recall, reranking, and source citations. Published on 5 April 2024 and granted on 9 July 2024. [Beijing Zhipu Huazhang Technology] [[Patent](https://patents.google.com/patent/CN117828050B/zh)]
- [*CN118280556A*] **一种基于计算视觉与大语言模型辅助中医诊疗的系统** An LLM handles spoken inquiry while computer vision converts patient images into findings that are retrieved and fed back to the LLM for TCM decision support (published, not granted). [[Patent](https://patents.google.com/patent/CN118280556A/zh)]
- [*CN118230893A*] **AI-large-model system for intelligent TCM prescription recommendation** Trains an AI large model on medical records to recommend personalized TCM prescriptions, wired into a hospital IS (published, not granted). [Hangzhou Ganzhicao Technology] [[Patent](https://patents.google.com/patent/CN118230893A/zh)]
- [*CN118098506A*] **一种基于大语言模型的针灸辅助诊疗和模型评价的方法** ChatGLM3-6B is fine-tuned on labeled symptoms, points, and operations to propose acupuncture plans, which are scored by sentence similarity (published, not granted). [[Patent](https://patents.google.com/patent/CN118098506A/zh)]
- [*CN118070907A*] **一种基于大语言模型的中医客服回复系统** Synonym-augmented TCM text trains a Transformer LLM that is fine-tuned to parse customer requests and draft replies; the application was granted as CN118070907B on 2024-07-09. [[Patent](https://patents.google.com/patent/CN118070907A/zh)]
- [*CN117786590A*] **以大语言模型为先验的智能中医系统** An LLM rewrites patient diagnostic text, which is then semantically interpreted to predict TCM syndromes and causes and to suggest treatment. Published on 1 April 2024. [[Patent](https://patents.google.com/patent/CN117786590A/zh)]
- [*CN117493579A*] **一种基于大语言模型的中医知识图谱构建方法** An LLM extracts named entities and relations from TCM text, merges similar entities, and builds a TCM knowledge graph (published, not granted). [[Patent](https://patents.google.com/patent/CN117493579A/zh)]

</details>


</details>

## Papers

Methods, evaluations, and systems only. Named domain LLMs live under Open models.

<details>
<summary>Agents (19): 问诊流程、多智能体</summary>

<details>
<summary>2026 · 11</summary>

- [*arXiv*] **Evidence-Based TCM Visualization Diagnosis System** Uses a symptom–pattern knowledge graph, symptom matching and information-gain question selection for visualized TCM consultation; the inquiry policy is illustrated through case walkthroughs. [[Paper](https://arxiv.org/abs/2606.06869)]
- [*arXiv*] **DeepTCM1.0** DeepTCM1.0: 11-expert multi-agent system on DeepSeek V3.2 for interpreting TCM formula mechanisms (Guizhi Decoction case); now on arXiv after the Research Square preprint. [Chinese Medicine Guangdong Laboratory (Hengqin), Changzhi Medical College] [[Paper](https://arxiv.org/abs/2608.18103)] [[Preprint](https://doi.org/10.21203/rs.3.rs-9844166/v1)]
- [*arXiv*] **DeepRoot** Multi-agent pipeline that turns the Shen Nong Ben Cao Jing into a verified Neo4j graph for therapeutic reasoning; code and evaluation scripts are public. [[Paper](https://arxiv.org/abs/2606.15931)] [[Code](https://github.com/CarlisleMa/deeprootv1)]
- [*Studies in Health Technology and Informatics*] **韩医CPX场景自动生成** LLM plus retrieval-augmented generation and multimodal cues to automate traditional Korean medicine CPX scenarios; validated by 10 experts. [[DOI](https://doi.org/10.3233/shti260671)]
- [*arXiv*] **TCMScience** An autonomous TCM research agent that separates language-model proposals from execution and release authority. [[Paper](https://arxiv.org/abs/2610.24601)]
- [*Journal of Pharmaceutical Analysis*] **TCM-Agent** LLM multi-agent system for network pharmacology and herbal discovery. [[Paper](https://doi.org/10.1016/j.jpha.2026.101581)] [[Code](https://github.com/AITCM/TCM-Agent)]
- [*arXiv*] **MACAT** Multi-agent culture-aware translation framework, evaluated on culture-loaded terms from TCM classics and the Analects. [[Paper](https://arxiv.org/abs/2606.01276)]
- [*Applied Sciences*] **KM-Agent** Tool-augmented agent for Korean / East Asian traditional medicine over 4,780 herb–syndrome–acupoint metadata records, evaluated on TCMBench-style sets. MDPI/OpenAlex authors at Wonkwang University and Pusan National University et al. [Wonkwang University, Pusan National University et al.] [[Paper](https://www.mdpi.com/2076-3417/16/7/3377)] [[Code](https://github.com/wonyung-lee/km-agent)]
- [*arXiv*] **DERM-3R** Resource-constrained multimodal multi-agent framework for TCM dermatology (recognition / representation / SDT agents). [[Paper](https://arxiv.org/abs/2604.09596)]
- [*arXiv*] **CORE-Acu** Acupuncture clinical decision support with structured reasoning traces and a knowledge-graph safety veto loop. [[Paper](https://arxiv.org/abs/2603.08321)]
- [*Engineering Applications of Artificial Intelligence*] **AcuModel / AcuAgent** Combines AcuModel, an acupuncture knowledge graph, semantic routing and rule constraints for follow-up inquiry and acupuncture reasoning. Project documentation and samples are public; full weights and training data require an author request. [[DOI](https://doi.org/10.1016/j.engappai.2026.116139)] [[Resources](https://github.com/mosheng555/AcuModel-And-AcuAgent)]

</details>

<details>
<summary>2025 · 7</summary>

- [*arXiv*] **Jingfang** Multi-agent TCM consultation and treatment system combining Ten Questions Song-guided inquiry, syndrome classification, and two-stage prescription retrieval. [[Paper](https://arxiv.org/abs/2502.04345)]
- [*中医杂志*] **基于雅意大模型的中医智能预问诊** Liu et al. fine-tune YAYI 2-30B with DeepSpeed ZeRO-3 and couple it to a weighted symptom-graph agent. On the simulated tests, practitioner-exam accuracy is 94.09%, licensed Chinese-pharmacy exam accuracy 78.00%, symptom-term recognition 87.50%, and meridian recognition 68.80%. In the clinical test, syndrome accuracy is 88.33%, with fewer turns and less time than attending physicians. [[DOI](https://doi.org/10.13288/j.11-2166/r.2025.09.005)] [[Paper](https://link.cnki.net/doi/10.13288/j.11-2166/r.2025.09.005)]
- **RenShu-AI** FastAPI + LangGraph multi-agent TCM consultation system combining GraphRAG and DeepSeek-TCM. [[Code](https://github.com/yanlinPeng-code/RenShu-AI)]
- [*Information*] **TCM compound retrieval agent** AI agent-based system for retrieving TCM compound information. [Zhengzhou University] [[DOI](https://doi.org/10.3390/info16070543)]
- [*Journal of King Saud University Computer and Information Sciences*] **DiagX-DT** Exclusionary syndrome-differentiation reasoning with CoT and an external TCM knowledge base. [[DOI](https://doi.org/10.1007/s44443-025-00123-1)]
- [*proceedings-article*] **An Intelligent TCM Diagnosis System with Localized LLMs and Modular Multimodal Reasoning Enhanced by RAG** The locally deployed system uses four agents for inspection, listening, inquiry, and palpation, coordinated by modular component processing and multimodal retrieval-augmented generation, and a central reasoning module turns tongue images, voice, pulse, and symptoms into a diagnosis and health advice. [Hosei University, Fuzhou University, Hong Kong Polytechnic University, Beihang University] [[DOI](https://doi.org/10.1109/cyberscitech68397.2025.00061)]
- [*Neurocomputing*] **AcuGPT-Agent** Combines a specialized LLM, an infertility-acupuncture knowledge graph and routing across specialist knowledge bases; EvalAcu assesses domain knowledge and task performance. [[DOI](https://doi.org/10.1016/j.neucom.2025.131116)]

</details>

<details>
<summary>2024 · 1</summary>

- [*대한한의학회지*] **Pilot Development of a 'Clinical Performance Examination (CPX) Practicing Chatbot' Utilizing Prompt Engineering** The authors turned a National Institute of Korean Medicine standardized-patient scenario into text and used role prompting and few-shot prompting with GPT-4 to build a Korean-medicine CPX practice chatbot; internal scoring found relatively high correctness and compliance, with confidentiality and naturalness still needing improvement. [Gachon University, Pusan National University] [[DOI](https://doi.org/10.13048/jkm.24013)]

</details>


</details>

<details>
<summary>Multimodal (32): 舌、面、脉</summary>

<details>
<summary>2026 · 12</summary>

- [*BMC Medical Informatics and Decision Making*] **脉波与语音联合筛查冠心病和心衰** Shanghai University of Traditional Chinese Medicine and collaborators treat the radial pulse wave as pulse diagnosis and the voice as auscultation, to screen for coronary artery disease and heart failure. They recorded 553 people (healthy, coronary disease, and heart failure) and checked the model on another 194. [[DOI](https://doi.org/10.1186/s12911-026-03518-w)]
- [*Sensors*] **红外热像面部穴位两级定位** A two-stage detector and regressor that localizes facial acupoints on multi-pose infrared thermal images, using bone-proportional cun and TCM anatomical rules. [[DOI](https://doi.org/10.3390/s26144498)]
- [*Journal of Traditional Chinese Medicine*] **空腹过程的寸关尺脉图定量** Records Left Cun, Right Cun, and Right Guan pulses in 51 healthy adults before fasting (day 0), during fasting (day 4), and after fasting (day 7). [[DOI](https://doi.org/10.19852/j.cnki.jtcm.2026.02.019)]
- [*arXiv*] **白睛异常分割（HD-DinoMoE）** Segments scleral-surface anomalies with a hierarchical mixture-of-experts network, to quantify TCM inspection of the whites of the eyes. [[Paper](https://arxiv.org/abs/2606.04888)]
- [*Medicine in Novel Technology and Devices*] **基于中医脉诊矩阵的客观脉象分析** Objective pulse analysis with a TCM pulse matrix. The authors argue that current waveform definitions and objectification standards are incomplete. [[DOI](https://doi.org/10.1016/j.medntd.2026.100429)]
- [*IEEE Journal of Biomedical and Health Informatics*] **可控 Transformer 面诊** A controllable Transformer for several traditional Chinese medicine facial-inspection tasks at once. IEEE Journal of Biomedical and Health Informatics, 2026. [[DOI](https://doi.org/10.1109/jbhi.2026.3706751)]
- [*proceedings-article*] **Multimodal TCM Seven-Emotion Recognition: A Three-Modality Joint Consultation Framework Based on LLMs and Cross-Attention Fusion** The seven-emotion framework reached a macro F1 of 87.6% on 10,593 IEMOCAP samples, then used a frozen large language model to turn the neural predictions into traditional Chinese medicine syndrome-differentiation reports. [Zhejiang University of Technology] [[DOI](https://doi.org/10.1145/3829441.3829486)]
- [*Lecture Notes in Computer Science Medical Image Computing and Computer Assisted Interventi*] **MLLM-Enhanced Region-Aware Bidirectional Evidence-Based Model for Tongue Diagnosis** A multimodal large-model method for region-aware, bidirectional evidence-based tongue diagnosis. [[DOI](https://doi.org/10.1007/978-3-032-38098-2_44)]
- [*arXiv*] **LingLan多模态辨证大模型** A multimodal TCM diagnosis model over the four examinations. Not the LingLan benchmark paper (arXiv 2602.01779). [[Paper](https://arxiv.org/abs/2609.25715)]
- [*Chinese Medicine*] **GNN-BERT 的症状–穴位推荐** Models symptom–acupoint compatibility with a heterogeneous graph and a fine-tuned BERT, for acupoint recommendation. [[DOI](https://doi.org/10.1186/s13020-026-01458-1)]
- [*arXiv*] **Alpha-TCM: A Nine-Layer Framework for TCM-Guided Multimodal Inference and Structured-Prior Auditing** Liu and Wang propose a nine-layer TCM-oriented system architecture that keeps semantics, multimodal acquisition, quality, knowledge priors, probabilistic inference, longitudinal updating, decisions, language interaction, and human governance distinct, and they audit the knowledge-evidence interface of layers 1-5 on synthetic data. The authors state that this is a system-design contribution and a synthetic prototype; it does not validate TCM theory or support clinical diagnostic or treatment claims. [[Paper](https://arxiv.org/abs/2610.38754)]
- [*Studies in Rhythm Engineering Cognitive Neuroscience and Artificial Intelligence*] **AI Tongue Diagnosis: Expert System with LLMs for Abdominal Disease Detection Through Mobile App** A mobile tongue-diagnosis expert system that uses large language models to detect abdominal disease. [[DOI](https://doi.org/10.1007/978-3-032-19966-9_2)]

</details>

<details>
<summary>2025 · 11</summary>

- [*Biomedical and Environmental Sciences*] **贫血女性舌面图像特征分析与风险筛查模型构建** Hongyuan Fu, Yi Chun, and Yahan Zhang (equal contribution), with corresponding authors Yongzhi Li and Xu Jiatuo, publish a methods paper in Biomedical and Environmental Sciences (2025, 38(8)) that enrolls 533 women aged 20–49 at Shuguang Hospital and uses color and texture features of face and tongue images to screen for anemia. LASSO selects 19 of 62 indicators; an ANN reaches test AUC 0.849 and accuracy 0.781, and a fused ResNet50V2 model reaches AUC 0.846 and accuracy 0.818. The official journal PDF can be downloaded; no printed Creative Commons license was seen, and no code or original images are provided. DOI 10.3967/bes2025.047. [[DOI](https://doi.org/10.3967/bes2025.047)] [[Paper](https://www.besjournal.com/en/article/doi/10.3967/bes2025.047)]
- [*Chinese Medicine*] **Liu 等：双中心舌象深度学习中医体质识别模型** Liu and Fan (co-first) and corresponding author Zhang prospectively collect 1,374 tongue images at Dongzhimen and Guang’anmen Hospitals and fuse traditional and deep features to recognize five constitutions. Accuracy figures in the abstract and Table 5 are inconsistent in print, while the AUC values 0.948 and 0.898 appear in both places and should be recorded together. The paper does not give a code repository. This is distinct from TongueNet, chen2025-tongue-analysis, and other constitution entries. [[DOI](https://doi.org/10.1186/s13020-025-01126-w)] [[Paper](https://cmjournal.biomedcentral.com/articles/10.1186/s13020-025-01126-w)]
- [*Frontiers in Physiology*] **Chen 等：面向中医辅助诊断的深度学习自动化舌象分析系统** Chen, Chen, Zhou, Zhu, He, and corresponding author Zhang present an integrated tongue-diagnosis system with acquisition hardware, semi-supervised segmentation, color correction, and feature classification, using 2,738 clinical cases. The authors report a Dice of 0.967 for U2net-MT tongue-body segmentation; the paper does not give a code repository, and training versus test image counts are not clearly stated. This is distinct from TongueNet and TongueDx/TongueDx2. [[DOI](https://doi.org/10.3389/fphys.2025.1559389)] [[Paper](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1559389/full)]
- [*Frontiers in Physiology*] **TongueNet：面向中医舌诊的多模态融合与多标签分类模型（Yang 等）** Yang, Dong, Lin, and corresponding author Lü propose TongueNet, a multimodal model that fuses tongue images with text for multi-label classification of disease nature and location. Training used 4,815 Roboflow-collected tongue images. The authors report 89.12% accuracy and an F1 of 48.07% for disease nature; the paper does not give a code repository. The Inner Mongolia Autonomous Region Hospital of Traditional Chinese Medicine, Inner Mongolia Medical University, and Inner Mongolia University should be distinguished. [[DOI](https://doi.org/10.3389/fphys.2025.1527751)] [[Paper](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1527751/full)]
- [*Scientific Reports*] **脉诊机器学习识别妊娠与冠心病** A portable MEMS/CMOS pulse device records healthy women, women with coronary heart disease, and women in the first trimester, then machine learning separates pregnancy from coronary heart disease. [[DOI](https://doi.org/10.1038/s41598-025-19780-3)]
- [*IEEE BIBM 2025*] **用大模型构建中医舌诊本体** Uses a large language model to help construct a TCM tongue-diagnosis ontology. [[DOI](https://doi.org/10.1109/bibm66473.2025.11356313)]
- [*Lecture Notes in Electrical Engineering*] **智能脉诊：信号处理与深度学习** Signal processing and deep learning for health-status classification from TCM pulse signals. [[DOI](https://doi.org/10.1007/978-981-95-1999-6_19)]
- [*ICASSP 2025*] **Few-shot tongue-diagnosis in-context multitask learning** Few-shot in-context multitask fine-tuning of LLMs mapping tongue images directly to constitutions. [Northeastern University] [[DOI](https://doi.org/10.1109/ICASSP49660.2025.10887764)]
- [*International Conference on Digital Transformation and Management*] **多通道桡动脉信号的脉象识别** A convolutional network reads common pulse patterns from multichannel radial-artery signals after denoising and feature extraction. The sample size and the recordings are not public. [[DOI](https://doi.org/10.1145/3795546.3795575)]
- [*Medical Engineering & Physics*] **TPC-GCN：中医脉象分类** Improved SMOTE augments pulse samples, multi-domain features are extracted, and a graph convolutional network classifies TCM pulse patterns. [[DOI](https://doi.org/10.1016/j.medengphy.2025.104401)]
- [*arXiv*] **TCDiff** Triplet cascaded diffusion model generating high-fidelity multimodal TCM EHRs, with the **TCM-SZ1** benchmark dataset. [[Paper](https://arxiv.org/abs/2508.01615)]

</details>

<details>
<summary>2024 · 5</summary>

- [*IEEE ECBIOS*] **高血压的中医面色分类** A classification model for TCM facial-color diagnosis of hypertension. [[DOI](https://doi.org/10.1109/ecbios61468.2024.10885481)]
- [*Digital Chinese Medicine*] **面色与体型的中医体质图像辨识** Full-body standing photos of healthy people, labeled with the Constitution in Chinese Medicine Questionnaire. Complexion and body shape come from a color space and local binary patterns; a dual-branch network adds deep features from the whole-body image; a random forest then identifies the constitution. Accuracy 0.842, precision 0.868, F1 0.790. [[DOI](https://doi.org/10.1016/j.dcmed.2024.09.002)]
- [*Bioengineering*] **面向糖尿病的中医脉诊卷积神经网络** Data processing so a convolutional network can read TCM pulse signals for diabetes, addressing the low repeatability of fingertip pulse diagnosis. [[DOI](https://doi.org/10.3390/bioengineering11060561)]
- [*IEEE ITNEC*] **统计特征与 MobileViT 的中医面色分类** Statistical features and MobileViT for automatic TCM facial-complexion classification. [[DOI](https://doi.org/10.1109/itnec60942.2024.10733073)]
- **Chinese-LLaVA-Med** Chinese medical multimodal LLM based on the LLaVA architecture, with the llava-med-zh-eval benchmark and open 7B weights. [[Code](https://github.com/BUAADreamer/Chinese-LLaVA-Med)]

</details>

<details>
<summary>2023 · 4</summary>

- [*Frontiers in Physiology*] **Shi 等：基于舌象的肺癌风险预警模型** Shi and Guo (co-first), Chun, Liu, Liu, Tu, and corresponding author Xu build a lung-cancer risk model from TFDA-1 tongue images of 862 participants. With tongue images only, a random forest reached author-reported accuracy of 0.679±0.048 and AUC 0.752±0.051; the data are not public for project-confidentiality reasons. This should be kept distinct from other tongue-diagnosis entries and does not change the person page for Xu Jiatuo. [[DOI](https://doi.org/10.3389/fphys.2023.1154294)] [[Paper](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2023.1154294/full)]
- [*BMC Complementary Medicine and Therapies*] **桡动脉脉搏波识别多囊卵巢综合征** Machine learning on radial pulse-wave parameters separates polycystic ovary syndrome from healthy controls in 459 subjects, as a step toward objective TCM pulse diagnosis. [[DOI](https://doi.org/10.1186/s12906-023-04249-5)]
- [*Phenomics*] **仿生设备采集中医脉象的规程** A protocol for digitizing TCM pulse information with bionic pulse-diagnosis equipment. [[DOI](https://doi.org/10.1007/s43657-023-00104-2)]
- **XrayGLM** Chinese multimodal medical LLM for chest X-ray interpretation. [[Code](https://github.com/WangRongsheng/XrayGLM)]

</details>


</details>

<details>
<summary>RAG / knowledge graphs (69): 检索和医案、方剂图谱</summary>

<details>
<summary>2026 · 18</summary>

- [*Communications in Computer and Information Science (Springer)*] **Hybrid Retrieval + Re-ranking TCM Prescription Generation** Hybrid retrieval with re-ranking to enhance LLM-based TCM prescription generation (Springer CCIS conference paper). [Shandong University, Shandong Academy of Sciences] [[Paper](https://doi.org/10.1007/978-981-92-3563-6_21)]
- **Pediatric influenza Chinese patent-medicine recommender (KG + LLM)** Knowledge graph of Chinese patent medicines for pediatric influenza built from authoritative guidelines and integrated with an LLM (JMIR Preprints). [[Preprint](https://doi.org/10.2196/preprints.101648)]
- [*BMC Medical Informatics and Decision Making*] **将韩医院电子病历转换到 OMOP CDM：方法与意义** Park, corresponding author Lee and colleagues convert electronic records from Wonkwang University Gwangju Korean Medicine Hospital to OMOP CDM 5.3, producing the WKTKM resource of 88,449 patients and extending KIOM terminology for Korean-medicine-specific concepts. Patient data cannot be shared; ETL code is on GitHub and mapping rules are in the supplement. This is a methodological proof of concept, not an efficacy trial. The license is CC BY 4.0. [[DOI](https://doi.org/10.1186/s12911-026-03418-z)] [[Paper](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-026-03418-z)] [[Code](https://github.com/ManYoungPark/KCDM_OMOP)]
- [*Frontiers in Medicine*] **Jin San Zhen KG-QA** Knowledge graph + LLM QA tool for the Jin San Zhen acupuncture school. [Guangzhou University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1755583)]
- [*兰州大学学报(医学版)*] **融合知识图谱与大语言模型的中医证据构建方法** Zhang, Wen, and colleagues propose a knowledge-graph and LLM method for structuring, grading, and dynamically updating multi-source TCM evidence in a digital evidence-based-medicine setting, with a feasibility check on an existing evidence-ecosystem platform. [[DOI](https://doi.org/10.13885/j.issn.2097-681X.T20260017)] [[Paper](https://cjournal.hep.com.cn/1000-2812/CN/10.13885/j.issn.2097-681X.T20260017)]
- [*IEEE BigComp 2026*] **知识图谱增强的中医问答大模型** Knowledge-graph-enhanced large language models for TCM question answering. [[DOI](https://doi.org/10.1109/bigcomp68355.2026.00029)]
- [*Frontiers in Medicine*] **Tree-organized self-reflective retrieval for TCM QA** Tree-organized self-reflective retrieval for TCM question answering (Frontiers in Medicine 2026). [[DOI](https://doi.org/10.3389/fmed.2026.1752778)]
- [*arXiv*] **TCMaster: Confidence-Aware Querying and Workload-Guided Physical Design for Multi-Source Traditional Chinese Medicine Knowledge Graphs** Chen Zheng and colleagues at Tsinghua University, Beijing University of Chinese Medicine, and the Guangdong Provincial Laboratory of Traditional Chinese Medicine present TCMaster, a confidence-aware query and physical-design method for multi-source TCM knowledge graphs. The system integrates pharmacopoeias, prescriptions, molecular databases, and LLM-extracted micro-semantics into a property graph with about 221,000 entities and 723,000 base edges, and it rewrites Cypher queries under provenance-level edge confidence. The authors report retrieval speedups on Neo4j and a 20.0 percentage-point gain in TCMbench QA accuracy from graph retrieval. Scale and scores are author-reported. [[Paper](https://arxiv.org/abs/2609.25712)]
- [*Journal of King Saud University - Computer and Information Sciences*] **TCMKG: Knowledge-Grounded question answering in Traditional Chinese Medicine via dynamic prompt evolution framework** TCMKG used expert-guided prompting on the Xin'an medical-case corpus to build a traditional Chinese medicine knowledge graph of 37,192 entities and 130,030 relations, with information-extraction precision 0.89, recall 0.88, and F1 0.88. [Anhui University of Traditional Chinese Medicine, Hefei University] [[DOI](https://doi.org/10.1007/s44443-026-00743-1)]
- [*Digital Chinese Medicine*] **TCM-HyperRAG** Higher-order knowledge hypergraphs for TCM diagnosis and prescription recommendation, with traceable evidence passed to a backbone model. [[DOI](https://doi.org/10.1016/j.dcmed.2026.08.004)]
- [*Frontiers in Medicine*] **TCM-DiffRAG** Syndrome-differentiation RAG with a general KG, a personalized KG, and chain-of-thought. [Guangdong Institute of Intelligence Science and Technology, Zhuhai, Hangzhou Ganzhicao Technology Co., Ltd, BoardWare Information System Limited] [[Published](https://doi.org/10.3389/fmed.2026.1804478)] [[Paper](https://arxiv.org/abs/2602.22828)] [[Code](https://github.com/LiJianmin6706/Tcm_Diff_RAG)]
- [*Frontiers in Pharmacology*] **TCM-CoT-RAG** Retrieval-augmented generation with chain-of-thought for TCM rheumatology decisions. [[DOI](https://doi.org/10.3389/fphar.2026.1884526)]
- [*Neural Networks*] **LLM-SDaT** A knowledge-informed LLM framework for TCM syndrome differentiation. [[DOI](https://doi.org/10.1016/j.neunet.2026.108812)]
- [*世界科学技术-中医药现代化*] **KG-IMHRE（赵炳南流派可解释多跳检索增强问答）** KG-IMHRE guides an LLM with subgraph mining and dynamic retrieval queries over the Zhao Bingnan dermatology school graph. On that benchmark it scores 85.2 on multiple choice, 45.78 on open questions, and 73.38 overall. [[DOI](https://doi.org/10.11842/wst.20250706001)]
- [*ISBCB 2026*] **GraphRAG-TCM: A Hybrid Retrieval-Augmented Generation System for Traditional Chinese Medicine Clinical Decision Support** Wang, Ren, and colleagues present a hybrid retrieval-augmented generation system for TCM clinical decision support at ISBCB 2026, combining vector retrieval, lexical retrieval, and knowledge-graph traversal. Title, authors, and DOI were verified via Crossref. [[DOI](https://doi.org/10.1145/3820664.3820702)] [[Paper](https://dl.acm.org/doi/10.1145/3820664.3820702)]
- [*proceedings-article*] **Construction of a Knowledge Graph for Functional Specification Standards of Traditional Chinese Medicine Information Systems Based on Large Language Models** Using 22 group-standard documents on functional specifications for traditional Chinese medicine information systems, the authors constrained DeepSeek with CRISPE prompts to extract entities and relations and then applied rule-based constraints to build a knowledge graph. [Hubei University of Chinese Medicine] [[DOI](https://doi.org/10.1145/3833450.3833480)]
- [*International Conference on Optics, Electronics, and Communication Engineering (*] **A knowledge-enhanced prescription generation model for TCM syndrome differentiation via multilevel memory retrieval** The prescription model retrieves similar cases with weighted BM25 and adds a drug knowledge graph from the Compendium of Materia Medica plus the eighteen incompatibilities and eighteen antagonisms, then passes that evidence to a large language model; experiments used the CCL2025 traditional Chinese medicine benchmark. [Chengdu Medical College, First Affiliated Hospital of Chengdu Medical College] [[DOI](https://doi.org/10.1117/12.3123588)]
- [*Journal of Visualized Experiments*] **A Study on An Intelligent Diagnosis and Treatment Assistant System For Acupuncture in Diminished Ovarian Reserve Based on A Knowledge Graph** Using large language models plus manual annotation on 82 acupuncture texts and clinical data, the authors built a graph of 16,558 entities and 80,084 relations; on 90 patients with diminished ovarian reserve, diagnostic agreement with experts was 86.7%. [Nanjing University of Chinese Medicine, Xuzhou Medical College, Nanjing General Hospital of Nanjing Military Command, Nanjing University] [[DOI](https://doi.org/10.3791/71182)]

</details>

<details>
<summary>2025 · 31</summary>

- [*Journal of Translational Medicine*] **DHerbKB：面向慢性肾脏病饮食管理与毒性中药控制的知识库** Corresponding authors Wang and Chen and colleagues present DHerbKB, a knowledge base that combines chronic-kidney-disease dietary principles with information on toxic Chinese medicines and offers an online recommendation system. It includes nutrition data on 8,725 foods and several classes of toxic herbal items. A 128-session evaluation with non-specialist users is an author-reported usability check. The system is at https://dherbkb.hywanglab.org.cn/. The license is CC BY-NC-ND 4.0. [[DOI](https://doi.org/10.1186/s12967-025-07178-8)] [[Paper](https://translational-medicine.biomedcentral.com/articles/10.1186/s12967-025-07178-8)] [[Link](https://dherbkb.hywanglab.org.cn/)]
- [*上海中医药杂志*] **融合大语言模型与知识图谱的抑郁症中西医结合智能问答系统** Tan Ping, with corresponding authors Liu Huina and Wei Changfa, publish a methods paper in Shanghai Journal of Traditional Chinese Medicine (2025, 59(7)) that turns the integrative guideline on depression into a Neo4j knowledge graph of 303 entities and 436 relations, then uses template matching and ChatGLM4 to generate traceable answers. On 20 questions, five experts give overall scores of 64.25 for template matching, 80.25 for ChatGLM4 alone, and 83.63 for the combined system. A 32-case outpatient demonstration is qualitative; no open code or graph is provided. The official journal PDF can be downloaded; no printed Creative Commons license was seen. [[DOI](https://doi.org/10.16305/j.1007-1334.2025.z20240925004)] [[Paper](https://shzyyzz.shzyyzz.com/zh/article/doi/10.16305/j.1007-1334.2025.z20240925004/)]
- [*世界科学技术-中医药现代化*] **阿尔茨海默病指南知识库问答（ChatGLM3）** LangChain grounds ChatGLM3-6B on a local library of Alzheimer guidelines and textbooks endorsed by the Chinese Association of Integrative Medicine and the Chinese Medical Association. Against bare ChatGLM3-6B, factual-accuracy wins are 88.09% and completeness wins 85.71%. [[DOI](https://doi.org/10.11842/wst.20240329007)]
- [*世界科学技术-中医药现代化*] **监督微调结合检索增强的中医知识问答** ChatGLM3 is supervised-fine-tuned with PissA and then wrapped in RAG. Reported scores are BLEU 14.5830 and ROUGE-1 34.6730; with RAG the TCM item-bank F rises to 0.6398 from a 0.2654 ChatGLM3 baseline. [[DOI](https://doi.org/10.11842/wst.20241121002)]
- [*Journal of Pharmaceutical Analysis*] **可解释图神经网络量化中药配伍** Interpretable graph neural networks quantify herb compatibility on a multidimensional TCM knowledge graph. Medicinal properties are virtual nodes. The study assesses herbal pieces in 6,080 formulas and checks 215 COVID-19 formulas. [[DOI](https://doi.org/10.1016/j.jpha.2025.101342)] [[arXiv](https://arxiv.org/abs/2411.11474)]
- [*IEEE ICCBDAI 2025*] **动态知识图谱与大模型的中医生理建模** Connects dynamic knowledge graphs with large language models for TCM physiological modeling. [[DOI](https://doi.org/10.1109/iccbdai66607.2025.11388184)]
- [*IEEE BIBM 2025*] **Chinese patent medicine knowledge system** Constructing a knowledge system for traditional Chinese patent medicine using LLMs and KGs. [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356149)]
- [*CCIS*] **中医问诊中的大模型与知识图谱** Case study of integrating large language models with knowledge graphs in TCM consultation. [[DOI](https://doi.org/10.1007/978-981-96-1809-5_28)]
- [*CCIS*] **中医药知识图谱问答系统** An intelligent TCM question-answering system that joins a knowledge graph with large language models. [[DOI](https://doi.org/10.1007/978-981-96-1809-5_26)]
- [*数据分析与知识发现*] **中医药标准知识问答系统** Retrieval-augmented QA system for TCM standards knowledge, built and evaluated in practice. [China Academy of Chinese Medical Sciences et al.] [[DOI](https://doi.org/10.11925/infotech.2096-3467.2024.0747)]
- [*Frontiers in Medicine*] **中医医案问答系统** A TCM case-based QA system integrating LLMs and knowledge graphs for efficient case retrieval and analysis (Front. Med. 2025). [[DOI](https://doi.org/10.3389/fmed.2024.1512329)]
- [*JMIR Medical Informatics*] **Yaoshi-RAG** Uncertain-KG RAG for medicine–food homology dietary recommendation with personalization and explainability. [[DOI](https://doi.org/10.2196/75279)]
- [*Frontiers in Pharmacology*] **TCMRD-KG** Innovative design of a rheumatology TCM knowledge graph from ancient literature. [Beijing University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fphar.2025.1535596)]
- [*Digital Chinese Medicine*] **TCMLCM** KG2TRAG-based intelligent QA model for TCM lung cancer. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2025.03.011)]
- [*Journal of Pharmaceutical Analysis*] **TCMKD 中医药知识发现平台** A proofread platform of syndromes, formulas, Chinese patent drugs, medicinal materials, ingredients, targets, and diseases, with mining, enrichment, and network analysis. https://cbcb.cdutcm.edu.cn/TCMKD/ [[DOI](https://doi.org/10.1016/j.jpha.2025.101297)] [[Website](https://cbcb.cdutcm.edu.cn/TCMKD/)]
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
- [*International Conference on Biomedical and Intelligent Systems*] **Jiezhai Gong 妇产科医案知识图谱** A Neo4j knowledge graph of Jiezhai Gong's obstetric and gynecological case records. [[DOI](https://doi.org/10.1145/3745034.3745089)]
- [*Proceedings of the 2nd International Conference on Machine Learning and Automation, CONF-M*] **Chinese Medicine Question Answering Robot Based on RAG and Self-Built Dataset** Builds a traditional Chinese medicine question-answering robot with retrieval-augmented generation and a self-built dataset. [[DOI](https://doi.org/10.4108/eai.21-11-2024.2354617)]
- [*计算机工程与应用*] **ChatTCM（苑中旭等）：融合思维链与知识图谱的中医问答模型** Yuan et al. present a TCM QA method that fine-tunes an LLM and couples it with a textbook-derived knowledge graph and chain-of-thought interaction. This is a distinct publication from the existing SylvanL/ChatTCM weights. BLEU, ROUGE, and accuracy figures are author-reported. [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2408-0101)] [[Paper](http://cea.ceaj.org/CN/10.3778/j.issn.1002-8331.2408-0101)]
- [*JAMIA*] **AcuKG** A knowledge graph of medical acupuncture built with entity recognition, relation extraction, and ontology mapping. [[DOI](https://doi.org/10.1093/jamia/ocaf179)]
- [*Communications in Computer and Information Science Health Information Processing. Evaluati*] **A TCM Syndrome Differentiation Thinking Method Based on Chain of Thought and Knowledge Retrieval Augmentation** CotKE-TCM prompts a large language model with chain-of-thought and retrieves similar cases, generated TCM knowledge, and clinical experience for syndrome differentiation, tested on the CHIP 2024 track. [ANTA Group] [[DOI](https://doi.org/10.1007/978-981-96-4298-4_3)]

</details>

<details>
<summary>2024 · 15</summary>

- [*上海中医药杂志*] **基于 GPTs 的中医知识图谱实体和关系抽取研究** He Yuhao, corresponding author Li Ming and colleagues publish a methods paper in Shanghai Journal of Traditional Chinese Medicine (2024, 58(8)) that uses custom GPTs on ChatGPT 4.0 to extract entities and relations from 351 formulas in Zhonghua Yifang, loads them into Neo4j, and compares the result with CasRel and GPLinker based on bert-Chinese. Total P, R, and F1 for the GPTs are 97.44%, 98.09%, and 97.48%. The experiment was completed by overseas collaborators; no open GPT, prompts, or annotations are provided. The official version is 58(8):1–6, DOI 10.16305/j.1007-1334.2024.2401070. The official journal PDF can be downloaded; no printed Creative Commons license was seen. [[DOI](https://doi.org/10.16305/j.1007-1334.2024.2401070)] [[Paper](https://shzyyzz.shzyyzz.com/zh/article/doi/10.16305/j.1007-1334.2024.2401070/)]
- [*中国数字医学*] **循证中医指南 PICO 知识图谱问答** Cui et al. use ERNIE Bot to extract PICO triples from a polycystic-ovary guideline, store 248 nodes and 337 relations in Neo4j, and draft 12 question classes with 24 templates for a guideline QA system. [[Paper](https://www.zgszyx.org.cn/CN/Y2024/V19/I5/20)]
- [*IEEE BIBM 2024*] **名老中医针灸医案知识图谱** Builds a knowledge graph of famous acupuncturists' cases by extracting information with a large language model. [[DOI](https://doi.org/10.1109/bibm62325.2024.10821904)]
- [*JMIR Medical Informatics*] **中医领域知识图谱补全** Domain knowledge graph completion and quality evaluation for Traditional Chinese Medicine. [Zhejiang Chinese Medical University, Guangdong Provincial Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2196/55090)]
- [*南京中医药大学学报*] **中医药问答大语言模型** TCM QA LLM combining RAG with P-Tuning v2 fine-tuning on ChatGLM2-6B. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1375)]
- [*计算机科学与探索*] **中医药大模型知识增强方法** Knowledge augmentation for TCM LLMs — a graph built from ~100k classical formulas preserving prescription structure. [Tianjin University] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2407082)]
- [*Methods of Information in Medicine*] **TCMSF** TCMSF: a construction framework for a TCM syndrome ancient-book knowledge graph that organizes syndrome knowledge from classical texts in a structured, semantically oriented way (Methods Inf. Med. 2024). [[DOI](https://doi.org/10.1055/a-2590-6348)]
- [*IEEE International Conference on Medical Artificial Intelligence (MedAI)*] **TCMRD-KG: Design and Development of a Rheumatism Knowledge Graph Based on Ancient Chinese Literature** TCMRD-KG is described as the first rheumatism-specific knowledge graph built from ancient traditional Chinese medicine books, with entity labeling that combines automatic annotation by mainstream large language models and manual review. [Beijing University of Chinese Medicine, China Academy of Chinese Medical Sciences, Guang’anmen Hospital, Institute of Basic Theory for Chinese Medicine] [[DOI](https://doi.org/10.1109/medai62885.2024.00083)]
- [*Computational and Structural Biotechnology Journal*] **TCMM 中药现代化统一数据库** A unified database aimed at modernization of traditional Chinese medicine and therapeutic innovation. [[DOI](https://doi.org/10.1016/j.csbj.2024.04.016)]
- [*EIECC*] **TCM MLKG-RAG** TCM intelligent diagnosis based on multi-layer knowledge graph retrieval-augmented generation. [University of Science and Technology of China] [[DOI](https://doi.org/10.1109/EIECC64539.2024.10929529)]
- [*OSF Preprints（预印本）*] **RAG 增强中医问答置信度** Implementing retrieval-augmented generation to build LLM confidence in TCM (preprint). [[DOI](https://doi.org/10.31219/osf.io/ns2v3)]
- [*arXiv*] **Prompt-RAG: Pioneering Vector Embedding-Free Retrieval-Augmented Generation in Niche Domains, Exemplified by Korean Medicine** Prompt-RAG, which does not use vector embeddings, outperformed ChatGPT and vector-embedding retrieval-augmented generation on relevance and informativeness in a Korean-medicine question-answering chatbot. [Gachon University, Stanford Medicine, Stanford University] [[Paper](https://arxiv.org/abs/2401.11246)]
- [*Phytomedicine*] **PresRecRF** Fuses a molecular knowledge graph with TCM semantic representations from large models, and predicts both herbs and dosages. Code and data are on GitHub. [[DOI](https://doi.org/10.1016/j.phymed.2024.156116)] [[Code](https://github.com/2020MEAI/PresRecRF)]
- [*Electronics*] **LLM 构建中医知识图谱** Constructing Traditional Chinese Medicine knowledge graphs based on large language models. [[DOI](https://doi.org/10.3390/electronics13071395)]
- [*Database (Oxford)*] **ACUBERT** ACUBERT for meridian entity recognition and classification in acupuncture indication knowledge bases. [Nanjing KG Data Technology] [[DOI](https://doi.org/10.1093/database/baae083)]

</details>

<details>
<summary>2023 · 5</summary>

- [*Frontiers of Information Technology & Electronic Engineering*] **知识引导的中医荐药（FITEE）** Graph-attention herb recommendation guided by a knowledge graph mined from TCM literature and prescriptions, with formula-theory signals added in the prediction layer. [[DOI](https://doi.org/10.1631/FITEE.2200662)]
- [*IEEE ICIEA*] **温病文献的 BERT 命名实体识别** BERT named-entity recognition for warm-disease texts in traditional Chinese medicine. [[DOI](https://doi.org/10.1109/iciea58696.2023.10241595)]
- [*计算机科学与探索*] **大模型融合知识图谱问答系统** Vertical-domain QA system deeply integrating LLMs with knowledge graphs for TCM formulas. [Tianjin University] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2308070)]
- [*Computers in Biology and Medicine*] **《伤寒论》问题意图分类（TinyBERT-CNN）** Classifies the intent of questions about the Treatise on Febrile Diseases with a TinyBERT and convolutional network. [[DOI](https://doi.org/10.1016/j.compbiomed.2023.107075)]
- [*世界科学技术-中医药现代化*] **MMKGQA（海洋中药知识图谱问答）** MMKGQA answers marine Chinese materia medica questions from the MMKG graph using Aho-Corasick and Word2Vec. On a questionnaire corpus, mean precision, recall, and F1 are 97.93%, 83.41%, and 89.10%. It is not an LLM system. [[DOI](https://doi.org/10.11842/wst.20220514002)]

</details>


</details>

<details>
<summary>Prescription (39): 荐药、组方、药对</summary>

<details>
<summary>2026 · 16</summary>

- [*arXiv*] **Patient-Conditioned Dual Hypergraph Reasoning** Patient-conditioned dual-hypergraph reasoning for auditable TCM prescription support, organizing symptom/tongue/pulse evidence around patterns and treatment principles (Tianjin University). [[Paper](https://arxiv.org/abs/2607.04025)]
- [*KSII Transactions on Internet and Information Systems*] **GAT+LLM TCM Prescription Generation** Intelligent TCM prescription generation combining graph attention networks with LLMs (formally published in KSII TIIS). [[DOI](https://doi.org/10.3837/tiis.2026.05.006)]
- [*Aging and Disease*] **Precious3GPT 用于中药来源抗衰老配方的筛选与设计** Galkin, Ren, and corresponding author Zhavoronkov present a computational proof of concept in Aging and Disease: they cross Precious3GPT-generated aging omics signatures with BATMAN-TCM2 to screen or design anti-aging TCM formulas, and they release a multi-agent workflow and datasets. Cross-species analysis yields 13 genes and 34 multi-tissue compounds, 20 of which appear in Huashan Wuzi Dan. The paper does not experimentally or clinically validate these formulas. Three printed figure captions are misaligned with the figures. The PDF states a Creative Commons Attribution license. [[DOI](https://doi.org/10.14336/AD.2024.1697)] [[Paper](https://www.aginganddisease.org/EN/10.14336/AD.2024.1697)] [[Code](https://github.com/Insilico-org/TCMxPlore)]
- [*世界科学技术-中医药现代化*] **知识蒸馏中医辨证论治模型** GPT-4o distills TCM case records into syndrome-differentiation instructions, then LoRA-tunes Qwen2.5-7B. The paper reports more readable reasoning while keeping prescription accuracy. No brand name or public weights. [[DOI](https://doi.org/10.11842/wst.20250422007)]
- [*arXiv*] **理法方药对齐的中医处方生成** Four-stage alignment for TCM prescription generation covering auditable li-fa-fang-yao reasoning, follow-up adjustment, and contraindications such as the eighteen antagonisms. [[Paper](https://arxiv.org/abs/2609.25755)]
- [*Expert Systems with Applications*] **异构网络预测中药毒性** Predicts traditional Chinese medicine toxicity with a heterogeneous network. [[DOI](https://doi.org/10.1016/j.eswa.2025.129969)]
- [*CCIS*] **多阶段学习的中医处方推荐大模型** A large language model for TCM prescription recommendation trained in multiple stages. [[DOI](https://doi.org/10.1007/978-981-92-0291-1_11)]
- [*Evidence-Based Chinese Medicine and Technology Assessment*] **中西药相互作用专论库** Evidence-based monographs of Chinese herb–drug interactions for a clinical decision-support database. Evidence-Based Chinese Medicine and Technology Assessment, 2026. [[DOI](https://doi.org/10.26599/ecmta.2026.9570040)] [[Website](https://www.imgateway.net)]
- [*Frontiers in Pharmacology*] **中药复方剂量调整方法** A method for adjusting the dosage of traditional Chinese medicine formulas, moving from empirical practice toward more precise use. Frontiers in Pharmacology, 2026. [[DOI](https://doi.org/10.3389/fphar.2026.1815285)]
- [*Pharmacological Research - Modern Chinese Medicine*] **中药化合物的多监管安全评价机器学习框架** Random-forest safety scoring of 127 bioactive compounds from 24 herbs, drawn from TCMSP, TCMID, PubChem, and ChEMBL, with separate weights for FDA, EMA, and CFDA priorities. [[DOI](https://doi.org/10.1016/j.prmcm.2026.100772)]
- [*Zenodo*] **UniTCM** A reverse-pharmacology platform that links formulas and diseases to molecular findings, with layers for standardization, clinical discovery, molecular analysis, systems checks, and tools. [[Code](https://doi.org/10.5281/zenodo.21711675)] [[Website](https://unitcm.qfxulab.com/)]
- [*Chinese Medicine*] **TCMNet** LLM-assisted disease knowledge mining with PPI networks and binding prediction for formula optimization. [Zhejiang Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1186/s13020-026-01360-w)]
- [*Current Molecular Pharmacology*] **TCMDATA** An R package for target-oriented network pharmacology and AI-assisted interpretation in traditional Chinese medicine. Current Molecular Pharmacology, 2026. [[Code](https://github.com/YuLab-SMU/TCMDATA)] [[DOI](https://doi.org/10.1016/j.cmp.2026.09.003)]
- [*Frontiers in Pharmacology*] **MSAT：中药物不良反应预测** A heterogeneous graph neural network trained on FAERS spontaneous reports to predict adverse reactions associated with Chinese materia medica. Frontiers in Pharmacology, 2026. [[DOI](https://doi.org/10.3389/fphar.2026.1774128)]
- [*Mathematics*] **LLM-Driven Unsupervised Discovery of Semantic Decision Dimensions for Dynamic Scheduling and Intelligent Systems: A Traditional Chinese Medicine Case Study** DeepSeek-V3.2 induced 458 raw labels from 12,163 traditional Chinese medicine herb records and 64,107 short sentences, merged into 22 semantic categories; Qwen3-Embedding-8B found average internal coherence above 60% for 19 concepts, and experts rated reasonableness 4.64 on a 1-to-5 scale. [Changchun University of Chinese Medicine, Shandong University of Arts, Tsinghua University] [[DOI](https://doi.org/10.3390/math14152681)]
- [*Digital Chinese Medicine*] **CMM-EmbedCluster** LLM + medicinal-property-theory clustering framework for Chinese materia medica, with a 567-herb property knowledge base. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2026.05.010)]

</details>

<details>
<summary>2025 · 11</summary>

- [*IEEE Journal of Biomedical and Health Informatics*] **LLM herb–drug interaction prediction** LLM-enhanced herbal medicine–drug interaction prediction. [Shenzhen University] [[DOI](https://doi.org/10.1109/jbhi.2025.3558667)]
- [*IEEE BIBM*] **方剂推荐中的剂量预测** Predicts doses while recommending a traditional Chinese medicine formula, using a diffusion model and a heterogeneous hierarchical network. IEEE BIBM, 2025. [[DOI](https://doi.org/10.1109/bibm66473.2025.11357222)]
- [*Chinese Medicine*] **强化学习的可解释中医处方推荐** Reinforcement learning for explainable traditional Chinese medicine prescription recommendation, using implicit preferences from a smaller language model. Chinese Medicine, 2025. [[DOI](https://doi.org/10.1186/s13020-025-01250-7)]
- [*Scientific Reports*] **图注意力网络预测中药相互作用** Graph attention networks predict interactions among traditional Chinese medicines. [[DOI](https://doi.org/10.1038/s41598-025-00725-9)]
- [*arXiv*] **可解释框架量化中医症状–方药对应** A model trained on ancient and classical formula records quantifies the TCM mapping from symptom patterns to individualized herbal therapy, for comparison with modern biomedicine. [[Paper](https://arxiv.org/abs/2507.11176)]
- [*IEEE BIBM 2025*] **医学知识增强的双层对齐中药处方推荐** Medical-knowledge-enhanced dual-level alignment network for herbal prescription recommendation. [[DOI](https://doi.org/10.1109/bibm66473.2025.11356282)]
- [*JMIR Medical Informatics*] **Weighted-voting TCM formula classification** Weighted-voting LLM approach for TCM formula classification. [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.2196/69286)]
- [*IEEE International Conference on Bioinformatics and Biomedicine (BIBM)*] **Two-Stage Chain-of-Thought Fine-Tuning for TCM Medication Decision-Making in Nsclc** For non-small-cell lung cancer, the two-stage chain-of-thought fine-tuning improved prescription generation and proprietary-Chinese-medicine recommendation by 1.2% and 6.1% over the baseline. [China Academy of Chinese Medical Sciences, Qinghai Normal University, Chinese Academy of Social Sciences, Institute of Ethnology and Anthropology] [[DOI](https://doi.org/10.1109/bibm66473.2025.11356901)]
- [*IEEE JBHI*] **TEmbed-DDI：中西药相互作用标注** Annotates cross-domain drug interactions with large language models and bidirectional networks, and adds a Chinese-medicine interaction evaluation. [[DOI](https://doi.org/10.1109/jbhi.2025.3563289)]
- [*proceedings-article*] **Dynamic Disease Tracking and Personalized Prescription Recommendation Using Large Language Model in Traditional Chinese Medicine** The system connects multi-turn consultation and temporal analysis to a large language model for personalized traditional Chinese medicine prescriptions, and on 1,000 insomnia cases it improved initial-case inference, diagnostic accuracy, and adaptability. [National Central University, National Taiwan University of Science and Technology, Research Center for Humanities and Social Sciences, Academia Sinica] [[DOI](https://doi.org/10.1109/iccbe65177.2025.11255949)]
- [*IEEE Transactions on Computational Biology and Bioinformatics*] **AN-IHP：注意力网络预测配伍禁忌药对** Attention networks predict incompatible herb pairs in traditional Chinese medicine. [[DOI](https://doi.org/10.1109/tcbbio.2024.3498094)]

</details>

<details>
<summary>2024 · 5</summary>

- [*Analytical Chemistry*] **质谱机器学习预测中药毒性** Machine learning on mass spectra predicts the toxicity of traditional Chinese medicines. [[DOI](https://doi.org/10.1021/acs.analchem.4c05311)]
- [*Computer Methods in Biomechanics and Biomedical Engineering*] **复方煎煮时长分类** Classifies how long a traditional Chinese medicine compound should be decocted, using multi-dimensional features. Computer Methods in Biomechanics and Biomedical Engineering, 2024. [[DOI](https://doi.org/10.1080/10255842.2024.2302225)]
- [*IEEE BIBM*] **TCM-FTP** Fine-tuning LLMs for herbal prescription prediction. [[DOI](https://doi.org/10.1109/BIBM62325.2024.10822451)]
- [*JAMIA*] **PresRecST** Progressive herb-prescription recommendation following syndrome differentiation then treatment planning (JAMIA 2024); ships a public encoded TCM-Lung subset and a TCM-PD reproduction table. [[DOI](https://doi.org/10.1093/jamia/ocae066)] [[Code](https://github.com/2020MEAI/PresRecST)]
- [*IEEE International Conference on Computer and Communication Engineering Technolo*] **A Study of Automated Data Mining of Medication Rules in Traditional Chinese Medicine Prescriptions Based on Large Language Model** Through interactive questioning, a large language model ran frequency, clustering, and Apriori association analyses on traditional Chinese medicine prescriptions for osteoporosis, and the automated results were highly similar to manual SPSS statistics. [Jinan University] [[DOI](https://doi.org/10.1109/ccet62233.2024.10837914)]

</details>

<details>
<summary>2023 · 7</summary>

- [*中国药房*] **生成式人工智能 GPT-4 驱动的中药处方生成研究** Chen Qitao, corresponding author Xia Lizhen and colleagues publish a short methods paper in China Pharmacy (2023, 34(23)) that sends pharmacopoeia and Chinese materia medica text to GPT-4 and a web-connected model to generate 30 herbal prescriptions, then has three same-hospital experts grade them blindly. Table 2 mean scores are 3.756 for expert consensus, 3.622 for GPT-4, and 3.501 for the connected model, with all pairwise P>0.05; a Turing test is reported as 138/270 (51.11%). The word “training” in the text does not mean parameter updates or fine-tuning. No code or prescription data are released, and no printed Creative Commons license was seen. [[DOI](https://doi.org/10.6039/j.issn.1001-0408.2023.23.02)] [[Paper](https://journal.china-pharmacy.com/zh/article/doi/10.6039/j.issn.1001-0408.2023.23.02/)]
- [*中国实验方剂学杂志*] **改良 Transformer 的冠心病证候要素诊断与处方模型** Li Hongzheng, corresponding author Wang Jie and colleagues publish a methods paper in Chinese Journal of Experimental Traditional Medical Formulae (2023, 29(1)) that uses syndrome elements as an intermediary and builds a modified Transformer with multi-head attention, compound embeddings, and dropout, trained on 8,030 Wang Jie case records, with a qualitative comparison of 100 real prescriptions. The abstract gives no numeric accuracy for those 100 cases; the 93% and 96.46% figures cited in the text belong to earlier work. A Song et al. review once misprinted the volume as 9(1); the official pagination is 29(1):148–154. The official journal PDF can be downloaded; no printed Creative Commons license was seen. [[DOI](https://doi.org/10.13422/j.cnki.syfjx.20221347)] [[Paper](https://www.syfjxzz.com/cn/article/doi/10.13422/j.cnki.syfjx.20221347)] [[Link](https://aipresc.xiaobaishiji.com/)]
- [*arXiv*] **深度强化学习的序贯中药治疗规划** Plans sequential herbal prescriptions across visits for chronic disease with deep reinforcement learning, rather than a single prescription. [[Paper](https://arxiv.org/abs/2304.12828)]
- [*Chinese Medicine*] **喜炎平严重不良事件的投影重要性** Uses variable-importance-for-projection scores to see how age and herb-drug combinations contribute to the severity of adverse events linked to Xiyanping injection. Chinese Medicine, 2023. [[DOI](https://doi.org/10.1186/s13020-023-00718-8)]
- [*IEEE BIBM*] **中医方剂 LLM 分类** Fine-tuned LLMs with refined prompt templates for TCM formula classification, using data sources such as the national medical-insurance catalog of proprietary Chinese medicines (IEEE BIBM 2023). [Leipzig University, Changchun University of Chinese Medicine, Liaoning Technical University, Sichuan Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385776)]
- [*IEEE Access*] **PreGenerator** TCM prescription recommendation model combining retrieval and generation. [College of Physics, Taiyuan University of Technology, Taiyuan, China, North Automatic Control Technology Institute, Taiyuan, China] [[DOI](https://doi.org/10.1109/ACCESS.2023.3316219)]
- [*IEEE BIBM*] **LLM+GNN 中医处方推荐** TCM prescription recommendation combining large language models with graph neural networks. [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385489)]

</details>


</details>

<details>
<summary>Extraction / PLM (11): NER、关系抽取、BERT 类编码器</summary>

- [*世界科学技术-中医药现代化*] **杏林-NER (XingLin-NER)** XingLin-NER is a generative NER framework that instruction-tunes structured and reasoning prompts for variable TCM clinical terms, scored with TCM-BERT semantic similarity. It is an extraction method, not a general TCM chat model. [[DOI](https://doi.org/10.11842/wst.20250327010)]
- [*Scientific Reports*] **中医命名实体识别的知识蒸馏** Knowledge distillation for named-entity recognition in traditional Chinese medicine, moving the skill into a smaller model. Scientific Reports, 2026. [[DOI](https://doi.org/10.1038/s41598-026-56313-y)]
- [*Artificial Intelligence in Medicine*] **中医临床命名实体与关系联合识别** Joint named-entity and relation extraction for traditional Chinese medicine clinical text, with a character-level convolutional recurrent network. Artificial Intelligence in Medicine, 2026. [[DOI](https://doi.org/10.1016/j.artmed.2026.103372)]
- [*proceedings-article*] **Named Entity Recognition in Traditional Chinese medicine Literature Data for Obesity Based on Large Language Models** For named-entity recognition in traditional Chinese medicine obesity literature, prompt-optimized DeepSeek-R1 reached an F1-score of 0.927 on the test set. [Hubei University of Chinese Medicine] [[DOI](https://doi.org/10.1145/3833450.3833478)]
- [*Applied Intelligence*] **KDC-NER** Knowledge-guided data augmentation + LLM fine-tuning framework for nested NER in TCM. [Jiangxi University of Chinese Medicine] [[DOI](https://doi.org/10.1007/s10489-026-07095-3)]
- [*npj Digital Medicine*] **LM extraction for complementary medicine** Language models for data extraction and risk-of-bias assessment in complementary medicine literature. [Lanzhou University] [[DOI](https://doi.org/10.1038/s41746-025-01457-w)]
- [*Scientific Reports*] **双通道知识注意力辨证模型** Dual-channel knowledge-attention NLP model for TCM syndrome differentiation, addressing rare characters and terminology extraction. [[DOI](https://doi.org/10.1038/s41598-025-96404-w)]
- [*Lecture Notes on Data Engineering and Communications Technologies*] **中医药专利关系抽取** Relation extraction over TCM patents with a large language model and diversified semantic interaction. [[DOI](https://doi.org/10.1007/978-3-032-10344-4_1)]
- [*Scientific Reports*] **中医病历嵌套实体识别** Recognizes nested entities in traditional Chinese medicine electronic medical records, such as a symptom and the body site it belongs to. Scientific Reports, 2025. [[DOI](https://doi.org/10.1038/s41598-025-22283-w)]
- [*Journal of the American Medical Informatics Association*] **LLM 腧穴定位关系抽取** Relation extraction with LLMs — a case study on acupuncture point locations. [The University of Texas MD Anderson Cancer Center , Houston, TX 77030] [[DOI](https://doi.org/10.1093/jamia/ocae233)]
- [*Frontiers in Artificial Intelligence*] **Evi-BERT** Automated information-extraction model (Evi-BERT) enhancing RCT evidence extraction for TCM. [[DOI](https://doi.org/10.3389/frai.2024.1454945)]

</details>

<details>
<summary>Evaluation (80): 基准和考试；要下载评测集走下面「数据集」</summary>

<details>
<summary>2026 · 44</summary>

- [*Future Internet (MDPI)*] **RAG+LoRA 中医执照考试推理架构** RAG+LoRA generative architecture with an 11,476-item Taiwan TCM licensing-exam dataset (2005-2025), raising accuracy from 61.0% to 89.0%+ (Future Internet, MDPI). [Chung Shan Medical University Hospital, Chung Shan Medical University] [[DOI](https://doi.org/10.3390/fi18060280)]
- [*Scientific Data*] **辨证论治大模型基准数据集** Scientific Data benchmark for evaluating syndrome differentiation and treatment in large language models. [[DOI](https://doi.org/10.1038/s41597-026-07587-4)]
- [*arXiv*] **证伪导向的可审计辨证协议** A model-agnostic falsification protocol for auditable syndrome differentiation on the public 200-case TCMEval-SDT set. [[Paper](https://arxiv.org/abs/2610.18298)]
- [*Frontiers in Plant Science*] **Medicinal-plant MLLM benchmark** Benchmarking multimodal LLMs for medicinal plant identification. [Shaoxing University] [[DOI](https://doi.org/10.3389/fpls.2026.1765281)]
- [*Frontiers in Medical Technology*] **胸痹/冠心病的中西医数据治理** For chest bi syndrome and coronary heart disease, a FHIR and SNOMED CT data system with 9 subsets and 352 elements, 42.6% of them TCM-specific, plus a 128-rule trigger engine. A prospective controlled study enrolled 972 people. [[DOI](https://doi.org/10.3389/fmedt.2026.1759773)]
- [*Digital Chinese Medicine*] **知识图谱增强的长尾证候辨证** Knowledge-graph-enhanced long-tail learning for traditional Chinese medicine syndrome differentiation. [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.005)]
- [*Journal of Evidence-Based Medicine*] **中医证候诊断标准适用性评价指南** A Delphi guideline for judging whether TCM syndrome diagnostic criteria are usable: 5 domains and 25 items, scored on a 5-point scale. Domains are accessibility, readability, implementability, acceptability, and overall evaluation. [[DOI](https://doi.org/10.1111/jebm.70153)]
- [*Journal of Evidence-Based Medicine*] **Large vs lightweight LLMs on TCM exams** Systematic comparison of large-scale vs lightweight LLMs on TCM exam questions. [First Affiliated Hospital of Henan University] [[DOI](https://doi.org/10.1111/jebm.70118)]
- [*Journal of Traditional Chinese Medical Sciences*] **TCM intelligent pre-consultation clinical evaluation** Tertiary-hospital clinical evaluation of an LLM intelligent pre-consultation system using a physician–AI–patient triad model. [Beijing Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.jtcms.2026.06.002)]
- [*Frontiers in Medicine*] **TCM AI-tutor evaluation** Multimodal LLM evaluation for TCM education across cognitive levels. [Beijing University of Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1893231)]
- [*Scientific Reports*] **Three-LLM TCM licensing exam evaluation** Systematic evaluation of 3 LLMs (incl. Gemini) on the national TCM medical licensing examination. [Shanghai Jiao Tong University] [[DOI](https://doi.org/10.1038/s41598-026-49200-z)]
- [*Guidelines and Standards of Chinese Medicine*] **中医大模型临床实践评测方法** Builds a clinical-practice evaluation for TCM large language models, arguing that Western medical benchmarks do not fit. [[DOI](https://doi.org/10.1097/gscm.0000000000000123)]
- [*npj Digital Medicine*] **中医场景中医疗大模型的提示词效应** Evaluates 16 models on TCM and shows that prompt effects depend on the model, which complicates reliable deployment. [[DOI](https://doi.org/10.1038/s41746-026-03397-5)]
- [*JMIR Formative Research*] **5-LLM TCM clinical decision comparison** Comparative study of 5 LLMs for TCM clinical decision-making. [Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.2196/80167)]
- [*arXiv*] **TongueDx2** Systematic ablation of the tongue-diagnosis DL design space (20+ model variants); TongueDx2 includes 5,109 images / 976 expert annotations. [[Paper](https://arxiv.org/abs/2607.28148)]
- [*arXiv*] **TCMQA** The paper reports 38,279 questions and 101 practitioners. The current HF release documents 33,872 qa rows and 5,250 doctor-annotated rows with 102 practitioners and 15,151 responses. Configurations overlap, so their counts must not be summed as unique questions. Pin the release; CC BY-NC-SA 4.0. [[Paper](https://arxiv.org/abs/2609.33014)] [[Dataset](https://huggingface.co/datasets/TechTCM/TCMQA)]
- [*Frontiers in Artificial Intelligence*] **TCMI-F-6D** Six-dimensional benchmark of interdisciplinary foundational competence in TCM informatics. [Anhui University of Chinese Medicine] [[DOI](https://doi.org/10.3389/frai.2026.1780967)] [[Code](https://github.com/123adf-dev/TCMI-F-6D-Benchmark)]
- [*arXiv*] **TCMClinicalReason-Bench** 2,000 multicenter EHR cases testing whether a model can reason from pathogenesis and syndrome to treatment principle and prescription. [[Paper](https://arxiv.org/abs/2610.04215)]
- [*ICIC 2026*] **TCMBenchEval** Benchmark evaluating LLMs on real clinical TCM case records (ICIC 2026). [Shantou University] [[DOI](https://doi.org/10.1007/978-981-92-3498-1_1)]
- [*WISE 2025*] **TCM-Eval (WISE 2025)** Multi-dimensional TCM evaluation framework from Tianjin University, its Fuzhou joint institute, Tianjin University of Chinese Medicine and its First Teaching Hospital, and Tianjin International Engineering Institute (WISE 2025). A different work from the ZMT-M1 TCM-Eval (arXiv 2511.07148) despite the identical name. [Tianjin University, International Joint Institute of Tianjin University, Tianjin University of Traditional Chinese Medicine, First Teaching Hospital of Tianjin University of Traditional Chinese Medicine, Tianjin International Engineering Institute] [[DOI](https://doi.org/10.1007/978-981-95-7251-9_15)]
- [*Scientific Data*] **TCM-BEST4SDT** 600 evaluation items: 300 syndrome-differentiation-and-treatment cases and 100 questions each on TCM knowledge, medical ethics, and content safety; 27 evaluation dimensions. [[DOI](https://doi.org/10.6084/m9.figshare.30615956)] [[Paper](https://arxiv.org/abs/2512.02816)] [[Code](https://github.com/DYJG-research/TCM-BEST4SDT)] [[Published](https://doi.org/10.1038/s41597-026-07587-4)]
- [*Communications Medicine*] **TCM-3CEval** Three-axis TCM LLM evaluation: core knowledge, classics comprehension, and clinical decision-making. [[Paper](https://arxiv.org/abs/2503.07041)] [[Published](https://doi.org/10.1038/s43856-026-01631-5)]
- [*Frontiers in Medicine*] **Supporting postgraduate exam preparation with large language models: implications for traditional Chinese medicine education** On the 2023 Chinese postgraduate examination for traditional Chinese medicine, Ernie Bot scored 50.30% and ChatGLM 46.67%, both above the passing score, with the highest scores in the medical humanities module. [Beijing University of Chinese Medicine, Dongzhimen Hospital Affiliated to Beijing University of Chinese Medicine, Changchun University of Chinese Medicine, Leipzig University] [[DOI](https://doi.org/10.3389/fmed.2025.1667104)]
- [*JMIR*] **STC-NF：中医症状术语两段式规范化** Split-then-concatenate normalization of TCM symptom terms from electronic records: 12 fine-grained semantic labels, three named-entity recognizers, and a two-stage deep-learning model. [[DOI](https://doi.org/10.2196/85825)]
- **Med-Bench-Arena** Open evaluation platform for medical and TCM LLMs/Agents (HF/vLLM/LiteLLM, multimodal, TCM-specific metrics), from the ZhongJing team. [[Code](https://github.com/pariskang/Med-Bench-Arena)]
- [*Scientific Data*] **MTCMB** Multi-task TCM benchmark with 12 datasets and 7,100 samples covering knowledge, reasoning, formulas, and safety (Scientific Data 2026). [[Paper](https://arxiv.org/abs/2506.01252)] [[Code](https://github.com/Wayyuanyuan/MTCMB)] [[Published](https://doi.org/10.1038/s41597-026-07967-w)]
- [*arXiv*] **MMIR-TCM** Memory-augmented multimodal tongue diagnosis and clinical decision framework; proposes MedTCM dataset and TDEU metric. [[Paper](https://arxiv.org/abs/2607.01814)]
- [*arXiv*] **LingLanMedBench** LingLanMedBench (formerly LingLanMiDian): 25,620 expert-verified items across 13 subtasks and five domains. Each subtask has a 400-item Hard subset selected from its full set. [Beijing Jiaotong University et al.] [[Paper](https://arxiv.org/abs/2602.01779v2)] [[Code](https://github.com/TCMAI-BJTU/LingLan)] [[Website](http://tcmnlp.com)]
- [*arXiv*] **Learning from Expert-Corrected Misdiagnoses: A Self-Evolving Consultation Agent for Traditional Chinese Medicine after Failed Treatment** Wang, Lin, and colleagues introduce TCM-MisDx, an 820-case interactive benchmark of consultations after failed treatment, and TCM-SEA, a self-evolving consultation agent. The authors report a composite score rise from 61.8 to 65.5 on a sealed test set and a lower therapeutic-momentum rate. Figures are author-reported; no independent dataset download is provided in the paper. [[Paper](https://arxiv.org/abs/2610.40663)]
- [*Brain Behavior and Immunity Integrative*] **Large language models vs traditional Chinese medicine clinical reasoning: Analysis of a single migraine case study** On one standardized migraine case, nine large language models were compared with two traditional Chinese medicine physicians and a published case response, scored blindly by 32 experts; GPT o3, Qwen 3, and Gemini 2.5 Pro matched or exceeded selected comparators in some domains, while Aya Expanse 32B scored lower. [Harvard University, Massachusetts General Hospital] [[DOI](https://doi.org/10.1016/j.bbii.2026.100192)]
- [*arXiv*] **Large Language Models Versus Physicians in Traditional Chinese Medicine: A Real-World Clinical Case Evaluation** From 349 de-identified outpatient cases at 62 hospitals, the authors used 60 cases to compare 16 large language models with 60 practicing traditional Chinese medicine physicians, scored blindly by five senior experts across nine diagnostic and therapeutic dimensions. [University of Missouri, Seventh People's Hospital of Shanghai, Yunnan University of Traditional Chinese Medicine, Northwestern University] [[Paper](https://arxiv.org/abs/2609.17544)]
- [*JMIR Formative Research*] **Korean Medical Consultation With Open-Weight Large Language Models: Pilot Comparative Evaluation of Retrieval-Augmented Generation With Metadata Filtering** An open-weight LLM chatbot for Korean medical consultation, comparing retrieval-augmented generation with metadata filtering. [[DOI](https://doi.org/10.2196/72604)]
- [*Frontiers in Medicine*] **Knowledge-guided adaptive educational support for traditional Chinese medicine using large language models and knowledge graphs: integrating Confucian educational principles** The intelligent traditional Chinese medicine tutor links a large language model to a knowledge graph from the Golden Mirror of Medicine; of 125 student volunteers, 102 questionnaires were analyzed, and the integrated system produced higher immediate post-test scores than the large-language-model-only group and the self-study group. [Anhui University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1943401)]
- [*AI Engineering*] **Knowledge of Chatbots on Oriental Medicine-Based Theory and Practice of Acupuncture Is Inferior to That on Western Medicine-Based Acupuncture-Transmitted Infections** Compares five free chatbots (ChatGPT, Claude, Copilot, Gemini, and Perplexity) and three subscribed ones (ChatGPT, Claude, and Perplexity) on 2,528 oriental-medicine acupuncture theory items and 100 acupuncture-infection items. The median theory score was 75%, below 86% on the infection items. [National Chung Hsing University, Tung Wah College, The University of Hong Kong, Fuke Fengze Chinese Medicine Clinic] [[DOI](https://doi.org/10.53941/aieng.2026.100004)]
- [*medRxiv*] **KampoBench** Physician-reviewed Kampo consultation benchmark: 74 scenarios and 310 dialogue-level criteria, scoring application rather than exam recall. [[DOI](https://doi.org/10.64898/2026.10.07.26365005)]
- [*ICIC 2026*] **GraphRAG or Fine-Tuning? Evaluating Knowledge Integration via Manually Extracted Graphs in Traditional Chinese Medicine** Tong, Lin, and Cai compare GraphRAG over a manually extracted TCM knowledge graph with fine-tuning at ICIC 2026 (LNCS). Title, authors, and the 15 July 2026 online publication date were verified via Crossref. [[DOI](https://doi.org/10.1007/978-981-92-3495-0_22)] [[Paper](https://link.springer.com/10.1007/978-981-92-3495-0_22)]
- [*arXiv*] **Fu-TCM: a multimodal large language model that learns traditional Chinese medicine diagnostic reasoning** Paper introducing the Fu-TCM multimodal diagnostic-reasoning framework and Bianzheng-Grounded Policy Optimization. The authors report that Fu-TCM-27B leads six TCM text, vision, and syndrome-differentiation benchmarks on macro-average accuracy. The internally built Fu-bianzheng and related benches are not independently released. [[Paper](https://arxiv.org/abs/2610.38333)]
- [*Terminology International Journal of Theoretical and Applied Issues in Specializ*] **From readable to executable** Using the same three prompts for each sampled term, the authors tested with ChatGPT-4o whether the WHO 2007 and 2022 traditional Chinese medicine terminology standards give enough explicit information for auditable selection among coexisting English variants. [University of Malaya] [[DOI](https://doi.org/10.1075/term.00097.yu)]
- [*proceedings-article*] **Evaluating Semantic Fidelity and Cohesion in NMT and LLM-based Translation of Traditional Chinese Medicine Classics** For English translation of traditional Chinese medicine classics, DeepSeek exceeded Google Translate and ChatGPT-5 on BERTScore semantic fidelity to the human reference, while ChatGPT-5 produced more semantically coherent text across sentences. [Northwestern Polytechnical University, Air Force Engineering University] [[DOI](https://doi.org/10.1109/icnlp69856.2026.11528039)]
- [*Current Bioinformatics*] **Evaluating Large Language Models for Query Refinement in Systematic Review Retrieval of Traditional Chinese Medicine** The authors tested GPT-4o, GPT-5, DeepSeek-V3, and DeepSeek-R1 under six prompts for literature retrieval in CNKI, Wanfang, PubMed, and Embase on psoriasis, COVID-19, and type 2 diabetes; the deduplicated gold-standard set contained 182 records (50, 74, and 58). [China Academy of Chinese Medical Sciences, Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2174/0115748936492177260915061800)]
- [*Expert Systems with Applications*] **DCB (Dynamic TCM Clinical Benchmark)** Builds dialogues from 205 clinical cases and introduces misleading symptom or diagnostic statements to evaluate inquiry, syndrome differentiation, prescription, and analysis. [East China Normal University] [[DOI](https://doi.org/10.1016/j.eswa.2026.132267)]
- [*JMIR Formative Research*] **ChatGPT、DeepSeek与医师针灸方案对照** Compares ChatGPT, DeepSeek, and physician-generated acupuncture treatment plans. [[DOI](https://doi.org/10.2196/95851)]
- [*arXiv*] **AcupunctureBench** Tan Wenjun and colleagues at Northeastern University introduce AcupunctureBench, a multimodal benchmark for generative models in acupuncture, covering text, image, and video, with 58,526 questions and 1,216 video samples. The authors report evaluating 14 large language models, 14 large multimodal models, and 4 video foundation models, and they released a dedicated evaluation website. Counts and scores are author-reported. An anonymous, manually gated Hugging Face repository without a dataset card was not added as a separate public dataset. [[Paper](https://arxiv.org/abs/2611.05399)] [[Link](https://acupunctureeval.daytime001.xin)]
- [*Pattern Recognition*] **ATCMD-Bench** First agentic TCM diagnosis benchmark, evaluating LLMs through multi-agent simulated consultations. [South China University of Technology] [[DOI](https://doi.org/10.1016/j.patcog.2026.113679)]

</details>

<details>
<summary>2025 · 19</summary>

- [*Expert Systems with Applications*] **针灸大模型驯化与生成评估 (Taming LLMs for Acupuncture)** Taming LLMs for acupuncture & moxibustion diagnosis, with generation quality evaluated at the semantic-similarity level. [[DOI](https://doi.org/10.1016/j.eswa.2024.125920)]
- [*JMIR Medical Informatics*] **辨证思维评测 (Syndrome Differentiation Thinking)** Method-development study evaluating and improving LLMs' TCM syndrome-differentiation thinking ability. [[DOI](https://doi.org/10.2196/75103)]
- [*Bulletin of the World Health Organization*] **国际疾病分类与传统医学数据缺口** Discusses data gaps for traditional medicine in the International Statistical Classification of Diseases. [[DOI](https://doi.org/10.2471/blt.25.293540)]
- [*BMC Medical Informatics and Decision Making*] **中医症状的细粒度实体与关系抽取** Fine-grained extraction of nested symptom entities and relations from semi-structured TCM records, avoiding the loss from coarse labels. [[DOI](https://doi.org/10.1186/s12911-025-03257-4)]
- [*UbiComp Companion 2025*] **TCM misinformation detection evaluation** Evaluates large language models on TCM knowledge and misinformation detection. [Tsinghua University] [[DOI](https://doi.org/10.1145/3714394.3756275)]
- [*JMIR Formative Research*] **TCM stroke LLM benchmark** Quantitative benchmark study of LLMs in the TCM stroke domain. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2196/81545)]
- [*Frontiers in Pharmacology*] **TCM guideline adherence evaluation** Content-analysis evaluation of LLM adherence to clinical practice guidelines in Chinese medicine. [Lanzhou University] [[DOI](https://doi.org/10.3389/fphar.2025.1649041)]
- [*CCL 2025*] **TCM-TBOSD 辨证论治评测** CCL 2025 shared task. Qilu University of Technology and the Affiliated Hospital of Shandong University of Traditional Chinese Medicine built TCM-TBOSD from de-identified records: 1,500 cases, 10 syndromes, 4 diseases, and 381 herbs. The prescription field lists herb names and, as the paper states, excludes doses. The repository has baseline code and a confidentiality form; the case table is not in the file listing. [[Paper](https://aclanthology.org/2025.ccl-2.45/)] [[PDF](https://aclanthology.org/2025.ccl-2.45.pdf)] [[Code](https://github.com/QLU-NLP/TCM-Syndrome-and-Disease-Differentiation-and-Prescription-Recommendation)]
- [*NeurIPS 2025*] **TCM-Ladder** Multimodal TCM benchmark with 52,169 question-answer pairs and image, audio, and video data (NeurIPS 2025). [[Paper](https://arxiv.org/abs/2505.24063)] [[Code](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[Leaderboard](https://tcmladder.com)] [[Published](https://proceedings.neurips.cc/paper_files/paper/2025/file/cbdd26a4490f5a8dad0d732508714029-Paper-Datasets_and_Benchmarks_Track.pdf)]
- [*arXiv*] **TCM-5CEval** Five-dimension TCM evaluation with 2,260 questions from 30 courses; cyclic option rotations test sensitivity to answer position. [[Paper](https://arxiv.org/abs/2511.13169)]
- [*npj Digital Medicine*] **TCM LLM acupuncture clinical evaluation** Real-case evaluation of 7 general LLMs vs licensed acupuncturists on SDT, point selection, needling, and herbs (*npj Digital Medicine*). [[DOI](https://doi.org/10.1038/s41746-025-01845-2)]
- [*JMIR Formative Research*] **Performance Assessment of ChatGPT-4.0 and ChatGLM Series in Traditional Chinese Medicine for Metabolic Associated Fatty Liver Disease: Comparative Study** The authors gave medical records of 87 metabolic-dysfunction-associated fatty-liver-disease cases treated with traditional Chinese medicine to ChatGPT-4.0, ChatGLM4, ChatGLM4 with a knowledge base, and ChatGLM3-6B, comparing syndrome differentiation, confusion of Chinese and Western concepts, and treatment-plan text. [Second Military Medical University, Chinese People's Liberation Army] [[DOI](https://doi.org/10.2196/66503)]
- [*arXiv*] **New Snow Tablets** Reveals systematic flaws of general and TCM-specific LLMs that guess formula ingredients from drug names. [[Paper](https://arxiv.org/abs/2504.03786)]
- [*JMIR Medical Education*] **GPT-4 作答台湾中医师执照考试** GPT-4 answered 480 items from the 2022 Taiwan TCM licensing examination and was compared with two licensed TCM doctors, using direct answers and explain-then-answer. Overall accuracy was 43.9% for the model, versus 70% and 78.4% for the two doctors. About 55.3% of the errors came from misunderstanding TCM concepts. This compares exam recall with licensed practitioners; it does not separately score syndrome judgment, prescription rationality, and safety checks. [[DOI](https://doi.org/10.2196/58897)] [[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11939018/)]
- [*Preprints.org（预印本）*] **GPT 台湾中医执业考试评估** GPT-3.5/GPT-4/GPT-4o performance on the Taiwan TCM licensing examination with reliability analysis (preprint). [[DOI](https://doi.org/10.20944/preprints202501.1787.v1)]
- [*J Integr Complement Med*] **GPT vs ERNIE 中医文化背景对比研究** Looks at how cultural background changes the way GPT and ERNIE handle the national TCM licensing exam. Journal of Integrative and Complementary Medicine, 2025. [College of Engineering, Boston University, Boston, MA, USA.] [[DOI](https://doi.org/10.1089/jicm.2024.0902)]
- [*IJCNN 2025*] **From Metaphor to Mechanism** LLMs decode TCM metaphor / imagistic-thinking language and map it to modern medical concepts. [Shandong Normal University,Jinan,China, China Pharmaceutical University,Nanjing,China, The University of Tokyo,Tokyo,Japan, Universiti Tunku Abdul Rahman,Perak,Malaysia] [[Paper](https://arxiv.org/abs/2503.02760)] [[Published](https://doi.org/10.1109/ijcnn64981.2025.11228098)]
- [*arXiv*] **Conveying Imagistic Thinking in Traditional Chinese Medicine Translation: A Prompt Engineering and LLM-Based Evaluation Framework** From four foundational passages of Huangdi Neijing, prompt scaffolding guided DeepSeek V3.1 to convey metaphor and metonymy; ChatGPT 5 Pro and Gemini 2.5 Pro then simulated three reader types and scored human, baseline, and prompt-adjusted translations on five cognitive dimensions, with the prompt-adjusted translations best on all five. [[Paper](https://arxiv.org/abs/2512.01198)]
- [*The Electronic Library*] **Contemporary technological value of ancient Chinese medical books: an empirical patent citation analysis using large language models** Large language models recognized traditional Chinese medicine entities and classified citation intent in patents; 72.9% of the patent citations showed low knowledge integration, and Systematic Differentiation of Warm Diseases ranked highest in technological impact. [Wuhan University, China Academy of Chinese Medical Sciences, Nanjing University] [[DOI](https://doi.org/10.1108/el-06-2025-0221)]

</details>

<details>
<summary>2024 · 13</summary>

- [*Big Data Mining and Analytics*] **MedBench：中文医学大语言模型综合评测基准（相邻工作）** Liu and Hu (co-first), with corresponding author Zhang, present a 2024 Chinese medical LLM benchmark and cloud platform in Big Data Mining and Analytics, with 300,901 questions across 43 clinical specialties and with question-answer isolation and cyclic shuffling. This is not a TCM- or herbal-medicine-specific benchmark. The correct DOI is 10.26599/BDMA.2024.9020044, which is not the 9020014 identifier that has appeared in some lists, and it is not LingLanMedBench or the same-named AAAI benchmark. The license is CC BY 4.0. [[DOI](https://doi.org/10.26599/BDMA.2024.9020044)] [[Paper](https://www.sciopen.com/article/10.26599/BDMA.2024.9020044)] [[Link](https://medbench.opencompass.org.cn)]
- [*arXiv*] **用《伤寒论》检验八纲表里辨证** Using empirical records from the Shanghan Lun, treats the exterior–interior pair of the Eight Principles as dimensionality reduction and tests whether it carries the most symptom information, is the most abstract, and helps formula choice. [[Paper](https://arxiv.org/abs/2409.19531)]
- [*SCIS-ISIS*] **汉方问诊虚拟病人** A virtual patient for Kampo medical interviews, intended to support empathy and the pathological concepts used in Kampo. [[DOI](https://doi.org/10.1109/scisisis61014.2024.10759962)]
- [*南京中医药大学学报*] **中医标准化评估基准** Standardized TCM evaluation benchmark of 29,506 questions across 13 subjects; tests 3 general and 5 Chinese medical LLMs. [Chengdu University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1383)]
- [*arXiv*] **Utilizing Large Language Models for Named Entity Recognition in Traditional Chinese Medicine against COVID-19 Literature: Comparative Study** The authors assembled 389 articles on traditional Chinese medicine against COVID-19 and manually annotated 48 of them with six entity types; under fuzzy match ChatGPT beat BERT question-answering models on 5 of 6 tasks, while exact match reversed that pattern, and none of GPT-4's F1 scores on herb, target, or research method exceeded 0.5. [Institute of Basic Theory for Chinese Medicine, GESIS - Leibniz Institute for the Social Sciences, University of Bonn] [[Paper](https://arxiv.org/abs/2408.13501)]
- [*arXiv*] **TCMD** TCMD, a TCM licensing-exam multiple-choice set for LLM evaluation (paper reports ~2,851 train / 600 test). Independent check found no official GitHub or Hugging Face download. [[Paper](https://arxiv.org/abs/2406.04941)]
- [*Integrative Medicine Research*] **TCM-BERT-CNN 整体证候分类** BERT and a convolutional network that map symptoms to multiple syndromes, using expert knowledge from public guidelines and textbooks and ten-fold cross-validation. [[DOI](https://doi.org/10.1016/j.imr.2023.101019)]
- [*IEEE International Conference on Medical Artificial Intelligence (MedAI)*] **Reunderstanding of the Classification of Syndromes in the Traditional Chinese Medicine Classic “Shang Han Lun” Based on Large Language Models** From ten selected Three-Yang passages in Shang Han Lun, Chinese and English ChatGLM 4.0 and ChatGPT-4.0 reclassified cases by modern medical consensus; among the four outputs, Chinese ChatGLM 4.0 was closest to the original Three-Yang grouping and English ChatGLM 4.0 diverged the most. [Beijing University of Chinese Medicine, China Academy of Chinese Medical Sciences, Wangjing Hospital of China Academy of Chinese Medical Sciences, Institute of Basic Theory for Chinese Medicine] [[DOI](https://doi.org/10.1109/medai62885.2024.00052)]
- [*Journal of Translational Medicine*] **LLM 中医语言文化偏差研究** Comparing LLMs developed in different countries on TCM; highlights language/cultural bias and the need for localized models. [Zhujiang Hospital, Southern Medical University, Shanghai Jiao Tong University, Shanghai First People's Hospital] [[DOI](https://doi.org/10.1186/s12967-024-05128-4)]
- [*Research Square（预印本）*] **GPT-4 中医研究生考试评估** GPT-4 vs mainstream Chinese LLMs on a TCM postgraduate examination dataset (preprint). [China Academy of Chinese Medical Science, Changchun University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.21203/rs.3.rs-4392855/v1)]
- [*대한한의학회지*] **Development of an LLM-based CPX Practicing Chatbot for Korean Medicine Education: Implementation of Automated Scoring and Feedback Generation Framework** In the Korean-medicine CPX practice chatbot, Claude-3.5-Sonnet scored every sample with perfect quantitative accuracy and averaged 43.2 seconds, faster than GPT-4. [Gachon University, Pusan National University] [[DOI](https://doi.org/10.13048/jkm.24067)]
- [*arXiv*] **ChatGPT 中医知识理解探究** Evaluating ChatGPT's comprehension of Traditional Chinese Medicine knowledge. [[Paper](https://arxiv.org/abs/2403.09164)]
- [*Chinese Medicine and Culture*] **ChatGPT 中医交互可行性研究** Feasibility and challenges of interactive AI for TCM, using ChatGPT as an example. [[DOI](https://doi.org/10.1097/MC9.0000000000000103)]

</details>

<details>
<summary>2023 · 4</summary>

- [*World Journal of Traditional Chinese Medicine*] **中医脉诊重测信度与评分者一致性** Test–retest reliability and inter-rater agreement of TCM pulse diagnosis by two practitioners on 300 participants. [[DOI](https://doi.org/10.4103/2311-8571.388728)]
- **中医新冠文献 LLM 命名实体识别** Comparative study of LLMs for named entity recognition in TCM COVID-19 literature (preprint). [[DOI](https://doi.org/10.2196/preprints.54346)]
- [*Studies in Health Technology and Informatics*] **ICD-11 传统医学章与 SNOMED CT 的本体对照** Compares traditional medicine entries in ICD-11 Chapter 26 with SNOMED CT in order to build a traditional-medicine ontology. [[DOI](https://doi.org/10.3233/shti230249)]
- [*JMIR Medical Education*] **ChatGPT 针灸教育研究** Comparative study of ChatGPT as a learning tool in acupuncture education. [Seoul National University Hospital] [[DOI](https://doi.org/10.2196/47427)]

</details>


</details>

<details>
<summary>Platforms / tools (8): 编目、门户、可运行工具</summary>

- [*arXiv*] **TCMIIES** TCMIIES: a browser-based, zero-installation LLM system for structured information extraction from academic literature, aimed at TCM and other specialty researchers. [[Paper](https://arxiv.org/abs/2605.07507)]
- [*GitHub*] **tcm-cli** A terminal tool for asking TCM questions in natural language, including formula composition, syndrome questions, and compatibility checks. It needs Python 3.10 or newer and an LLM API key. Local data can be pulled for herbs, formulas, TCMSP, TCMID, and related sets. MIT license. The repository was created in February 2026. [[Code](https://github.com/tigerneil/tcm-cli)]
- [*Science of Traditional Chinese Medicine*] **TCM Data Hub (YiYuan)** YiYuan LLM-driven TCM data platform. [CAMS / Peking Union Medical College] [[DOI](https://doi.org/10.1097/st9.0000000000000118)]
- [*Cell Discovery*] **神农Alpha** ShennongAlpha (Westlake University): an AI-driven sharing and collaboration platform for intelligent curation, acquisition and translation of natural-medicinal-material knowledge (Cell Discov. 2025). [[DOI](https://doi.org/10.1038/s41421-025-00776-2)] [[Website](https://shennongalpha.westlake.edu.cn/)] [[Paper](https://www.nature.com/articles/s41421-025-00776-2)] [[Code](https://github.com/shennong-program/shennongname)]
- [*GitHub*] **pro_TCMLLM** A P-Tuning script that trains ChatGLM-6B on the ShenNong instruction files. The active command uses prefix length 128, learning rate 2e-2, the ShenNong train and test files, 3,000 steps, batch size 4, gradient accumulation 2, and fp16. The repository was created in November 2025. [[Code](https://github.com/GT-Kai/TCMLLM)] [[Link](https://github.com/GT-Kai/TCMLLM/blob/main/BaseModels/ChatGLM-6B/ptuning/train.sh)]
- [*IEEE BIBM 2025*] **DMease** An AI assistant for TCM doctors diagnosing and treating diabetes mellitus. [[DOI](https://doi.org/10.1109/bibm66473.2025.11356320)]
- [*IEEE International Conference on Computational Intelligence and Applications (IC*] **IC-BERT: An Instruction Classifier Model Alleviates the Hallucination of Large Language Models in Traditional Chinese Medicine** IC-BERT uses a BERT text filter to limit which questions a traditional Chinese medicine large language model may answer, so as to reduce fabricated facts when questions fall outside its capability. [Hainan University] [[DOI](https://doi.org/10.1109/iccia62557.2024.10719061)]
- [*IJACSA*] **草药智能配送聊天机器人** Smarter herbal medication delivery system employing an AI-powered chatbot. [University of the Cordilleras, Naresuan University Hospital, Catanduanes State University] [[DOI](https://doi.org/10.14569/ijacsa.2023.0140358)]

</details>

<details>
<summary>Other methods (33): 对齐、提示、专科任务</summary>

<details>
<summary>2026 · 8</summary>

- [*Translation Review*] **Beyond the Poetic Bard（中医AI翻译评论）** Beyond the Poetic Bard: a perspective on accuracy, epistemology, and medical-context limits of generative-AI translation of TCM texts (Translation Review). [[DOI](https://doi.org/10.1080/07374836.2026.2679929)]
- [*Progress in Biochemistry and Biophysics*] **Pathogenesis-reasoning CoT supervision for spleen-stomach disorders** Pathogenesis-reasoning chain-of-thought supervision replacing fixed-label classification for spleen-stomach disease syndrome recognition and multi-dimensional evaluation (Prog. Biochem. Biophys.). [[Paper](https://www.pibb.ac.cn/pibbcn/article/abstract/20260141)]
- [*Expert Systems with Applications*] **针灸临床决策中的大模型补偿机制** Studies compensation mechanisms of large language models in acupuncture clinical decision-making. [[DOI](https://doi.org/10.1016/j.eswa.2025.130870)]
- [*Journal of Integrative Medicine*] **肺磨玻璃结节的中医症状风险模型** Assesses how pulmonary ground-glass nodules may progress, combining imaging with traditional Chinese medicine symptoms. Journal of Integrative Medicine, 2026. [[DOI](https://doi.org/10.1016/j.joim.2026.01.002)]
- [*Chinese Medicine*] **大模型连接中医知识与临床实践** Discusses how large language models can link implicit TCM knowledge with syndrome-based clinical practice. [[DOI](https://doi.org/10.1186/s13020-026-01489-8)]
- [*GitHub*] **吴鞠通温病技能** A warm-disease skill set drawn from Wenbing Tiaobian, Yiyi Bingshu, Wu Jutong's case records, and Wenre Jingwei, set beside six-meridian formula patterns. The repository description lists 359 cases and 22 warm-disease formulas, using sanjiao and wei-qi-ying-xue. [[Code](https://github.com/jangviktor-web/wujutong)]
- [*Biomedical Signal Processing and Control*] **Generating interpretable clinical reasoning chains in TCM via group relative policy optimization and multi-dimensional rewards** Generates interpretable traditional Chinese medicine clinical reasoning chains with group relative policy optimization and multi-dimensional rewards. [[DOI](https://doi.org/10.1016/j.bspc.2026.111275)]
- [*Digital Chinese Medicine*] **Fine-Med-Mental-T&P: a dual-track approach for high-quality instructional datasets of mental disorders in traditional Chinese medicine** Fine-Med-Mental-T&P used DeepSeek-V3 to draft and Qwen3-32B to rewrite answers, screening 16,000 theory instructions from textbooks and guidelines and 4,000 practice instructions from more than 600 real case seeds, for 20,000 instruction pairs on traditional Chinese medicine mental disorders. [Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.004)]

</details>

<details>
<summary>2025 · 15</summary>

- [*Journal of Global Health*] **Ahn 等：世卫组织传统、补充与整合医学全球研究优先领域及与大语言模型的对照** Ahn, Zhou, Jiang, Kerr, Zhu, Song, and joint senior author Rudan use the CHNRI method to have experts score research ideas in traditional, complementary, and integrative medicine, and they compare the list with ChatGPT-4o, Claude 3.5, and Grok 3. Fifty-three people responded, 34 scored, and 157 ideas were collected. This is a research-priority consensus, not a trial of efficacy. [[DOI](https://doi.org/10.7189/jogh.15.04336)] [[Paper](https://jogh.org/2025/jogh-15-04336)]
- [*Frontiers in Pharmacology*] **CNN 预测急性缺血性卒中中医热证类型（预试验）** Yu, corresponding authors Zhu and Song and colleagues use a convolutional network on a 193-case large-artery atherosclerotic acute ischemic stroke cohort at Xuanwu Hospital, combining TCM syndrome features and laboratory values to predict heat versus non-heat syndrome. After dropping incomplete records, 123 cases remain. On the test set, combined features reach accuracy and F1 of 0.95; AUC is 0.91 in the text and 0.90 in Figure 3C. The authors describe this as a preliminary study. The data are not public, and no code is given. The license is CC BY. [[DOI](https://doi.org/10.3389/fphar.2025.1601601)] [[Paper](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1601601/full)]
- [*PLoS ONE*] **Li 等：计算机与手法选穴辅助膝骨关节炎物理治疗的随机对照试验方案** Li, corresponding author Ahmad and colleagues publish a study protocol comparing Acugraph computer-aided point selection with manual point selection as an adjunct to physiotherapy for mild-to-moderate knee osteoarthritis. The planned sample is 50 patients and 12 sessions. This is a protocol, not trial results, and the paper reports no measured outcomes. The existing survey surv-acupoint-cad already warns against treating this paper as a completed trial. [[DOI](https://doi.org/10.1371/journal.pone.0313761)] [[Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0313761)]
- [*CCIS*] **面向辨证的大模型微调** Fine-tunes large language models for TCM syndrome differentiation. [[DOI](https://doi.org/10.1007/978-981-96-4298-4_4)]
- [*世界科学技术-中医药现代化*] **轻量化中医药古籍大语言模型（LoRA）** Shanghan Lun QA pairs from GPT-4, plus ShenNong and cMedQA2, are used to LoRA-tune five base models and to compare full LoRA with 8-bit and 4-bit QLoRA on Qwen-7B-Chat. That model gains 17.61 BLEU and 21.4 ROUGE-L over its base. No separate model name. [[DOI](https://doi.org/10.11842/wst.20241014001)]
- [*情报科学*] **融合证素知识的中医证候术语映射** Maps clinical wordings of TCM syndromes onto standard syndrome names with syndrome-element knowledge. Information Science, 2025, volume 43, issue 7. [[Paper](https://journal12.magtechjournal.com/jwk3_qbkx/CN/Y2025/V43/I7/48)]
- [*JMIR Formative Research*] **胰腺癌病历的证型识别** Identifies TCM syndrome types from free text in electronic records of people with pancreatic cancer. JMIR Formative Research, 2025. [[DOI](https://doi.org/10.2196/70602)] [[Code](https://github.com/wangzaimieyoutou/PCSD_Bert)]
- [*Combinatorial Chemistry & High Throughput Screening*] **痛经辨证的机器学习模型** A machine-learning model for traditional Chinese medicine syndrome differentiation in dysmenorrhea. Combinatorial Chemistry and High Throughput Screening, 2025. [[DOI](https://doi.org/10.2174/0113862073293191240212091028)]
- [*IEEE JBHI*] **用大模型理解中医：机制探索与创新应用** An LLM method for mechanism exploration and downstream application in TCM. [[DOI](https://doi.org/10.1109/jbhi.2025.3631841)]
- [*北京中医药大学学报*] **基于大语言模型与文本嵌入计算的中医证素辨证自动化方法** Instr-MT-TCM, an instruction-tuned TCM embedding model, is paired with an LLM for syndrome-element differentiation. On 1,793 real cases the joint method reaches mean F1 0.927 versus 0.512 for manual labels, and is applied to 48 prostate-cancer cases. [[Paper](https://xb.bucm.edu.cn/zh/article/doi/10.3969/j.issn.1006-2157.2025.08.018/)]
- [*IET*] **基于Llama3的中医大模型** Fine-tunes Llama 3, Phi-3.5, and Mistral on TCM data to improve Chinese TCM language coverage. [[DOI](https://doi.org/10.1049/icp.2025.1017)]
- [*Bioengineering*] **儿童多动症推拿的特征选择** Selects features and predicts pediatric tuina choices for children with attention deficit hyperactivity disorder. Bioengineering, 2025. [[DOI](https://doi.org/10.3390/bioengineering12101012)]
- [*CCIS*] **中医大模型指令微调** Instruction fine-tuning of large language models for TCM. [[DOI](https://doi.org/10.1007/978-981-96-1809-5_34)]
- [*SPIE*] **TCMHP** A large language model for TCM health preservation (preventive care). [[DOI](https://doi.org/10.1117/12.3068496)]
- [*ACAIB 2025*] **BioBERT-HDI：草药与化学药相互作用预测** BioBERT predicts herb–drug interactions from the literature and is compared with other machine-learning models. [[DOI](https://doi.org/10.1145/3760269.3760325)]

</details>

<details>
<summary>2024 · 7</summary>

- [*Studies in Health Technology and Informatics*] **将 OMOP 通用数据模型应用于传统东亚医学数据集的可行性** Jiyun Cha, Eun Kyoung Ahn, Young-Heum Yoon, and Man Young Park publish a three-page MEDINFO 2023 short paper in Studies in Health Technology and Informatics (2024, pp. 1349–1351) that extracts items from Korean-medicine clinical guidelines on facial palsy, dysmenorrhea, and stroke and maps them to OMOP CDM 6.0. Of 52 deduplicated items, 42 are general clinical information and 10 are TEAM-specific; all map at table level, while three cannot be placed in existing fields at field level. The license is CC BY-NC 4.0, DOI 10.3233/SHTI231189. This is not the same paper as park2026-tkm-omop. [[DOI](https://doi.org/10.3233/SHTI231189)] [[Paper](https://ebooks.iospress.nl/doi/10.3233/SHTI231189)]
- [*JAMIA*] **灵丹 JAMIA：面向临床推理的中医知识编码** JAMIA paper on Lingdan, a TCM large language model for encoding domain knowledge in clinical reasoning tasks. Distinct from the later Digital Chinese Medicine prescription-evaluation paper. [[DOI](https://doi.org/10.1093/jamia/ocae087)]
- [*Heliyon*] **多囊卵巢证型的多标签预测** Compares feature selection and multi-label models for predicting traditional Chinese medicine patterns in polycystic ovary syndrome. Heliyon, 2024. [[DOI](https://doi.org/10.1016/j.heliyon.2024.e35283)]
- [*Chinese Journal of Pharmacovigilance*] **中药肝损伤不良反应的风险信号** Uses adverse-reaction monitoring data to look for new risk signals and susceptibility factors in traditional Chinese medicine–induced liver injury. The journal page publishes the article and does not release case rows. [[Paper](https://zgywjj.magtechjournal.com/EN/10.19803/j.1672-8629.20230779)] [[PDF](https://zgywjj.magtechjournal.com/EN/article/downloadArticleFile.do?attachType=PDF&id=3442)]
- [*arXiv*] **中医提示工程框架** Prompt-engineering framework for LLM intelligent understanding in TCM. [[Paper](https://arxiv.org/abs/2410.19451)]
- [*arXiv*] **RLAIF 中医对齐** Enhancing LLMs' TCM capabilities through reinforcement learning from AI feedback. [[Paper](https://arxiv.org/abs/2411.00897)]
- [*Digital Chinese Medicine*] **BSG 中医智能问答** Intelligent QA system for TCM based on a BSG deep-learning model (prescription and materia medica cases). [Hunan University of Traditional Chinese Medicine, Central South University] [[DOI](https://doi.org/10.1016/j.dcmed.2024.04.006)]

</details>

<details>
<summary>2023 · 3</summary>

- [*中国工程科学*] **新时代中医药发展现状与思考（战略述评）** Xue Xiaojuan and colleagues, with corresponding author Zhang Boli, publish a 2023 strategic review and policy recommendations in Strategic Study of CAE (25(5)), based on the CAE consulting project on TCM development strategy in the new era. The paper reviews theory, clinical evaluation, resources, intelligent manufacturing, and international promotion, and offers six recommendations. This is not a systematic review and not a new algorithm or clinical trial. Unpaywall records the license as CC BY-NC-ND. [[DOI](https://doi.org/10.15302/J-SSCAE-2023.05.007)] [[Paper](https://www.engineering.org.cn/sscae/CN/10.15302/J-SSCAE-2023.05.007)]
- [*Military Medical Research*] **中西医有机结合临床实践指南编制方法（立场与指南）** Jin and colleagues, with corresponding authors Zeng and Shang, publish a 2023 position paper and methodological standard in Military Medical Research on writing clinical practice guidelines that organically integrate TCM and Western medicine. A stock-take of 54 published integrative guidelines finds that only 5.6% clearly frame clinical questions in an integrative way. This is neither a systematic review nor a clinical trial. The license is CC BY 4.0. [[DOI](https://doi.org/10.1186/s40779-023-00481-9)] [[Paper](https://mmrjournal.biomedcentral.com/articles/10.1186/s40779-023-00481-9)]
- [*IEEE BIBM*] **中医疫病防治问答模型** LLM-based QA model for TCM epidemic prevention and treatment. [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385748)]

</details>


</details>

<details>
<summary>Before LLMs (146): 专家系统、舌脉、本体、早期编码器</summary>

<details>
<summary>2020–2022 · 61</summary>

- [*Discover Applied Sciences*] **Mathematical modeling of Chinese medicine by complex-valued five-agent network** Historical anchor: Mathematical modeling of Chinese medicine by complex-valued five-agent network. [National Cheng Kung University] [[DOI](https://doi.org/10.1007/s42452-025-06602-4)]
- [*Lv Q et al., *Signal Transduct Target Ther* 8(1):127*] **TCMBank** Historical anchor: TCMBank. [[DOI](https://doi.org/10.1038/s41392-023-01339-1)]
- [*Interdisciplinary*] **Historical Analysis of Medical Artificial Intelligence Development in China: Research Cent** Historical anchor: Historical Analysis of Medical Artificial Intelligence Development in China: Research Cent. [Okayama University of Science, Okayama University] [[DOI](https://doi.org/10.18926/interdisciplinary/65464)]
- [*Zhang Y et al., *Acta Pharm Sin B* 13(6):2559-2571*] **ETCM v2.0** Historical anchor: ETCM v2.0. [Shanghai Institute of Materia Medica, Guiyang Medical University] [[DOI](https://doi.org/10.1016/j.apsb.2023.03.012)]
- [*Scientific Reports*] **Discovering golden ratio in the world’s first five-agent network in ancient China** Historical anchor: Discovering golden ratio in the world’s first five-agent network in ancient China. [National Cheng Kung University] [[DOI](https://doi.org/10.1038/s41598-023-46071-6)]
- [*Frontiers in Psychology*] **Lai 等：基于语音与 ResNet 识别气虚质与平和质** Lai, Guan, Men, Shang, and corresponding author Zhang use 720 voice spectrograms from 48 participants and ResNet34 to distinguish qi-deficiency and balanced constitutions. The authors report 81.5% accuracy and an AUC of 0.85, and they point to code at GitHub GYT0704/Voice_Classification. This is distinct from voice-constitution-acoustic and constitution-tap. [[DOI](https://doi.org/10.3389/fpsyg.2022.1043955)] [[Paper](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1043955/full)]
- [*Frontiers in Oncology*] **机器学习预后模型：中药对Ⅰ–Ⅲ期结直肠癌复发转移的影响** Tang and Gao (co-first), with corresponding author Yang, retrospectively include 558 patients with stage I–III colorectal cancer after curative surgery, compare four machine-learning methods for internal validation of 3- and 5-year recurrence or metastasis, and add TCM intervention and syndrome type. Code is posted on Gitee. Figures for the 5-year intervention model in the text and Table 3 are inconsistent. The license is CC BY. [[DOI](https://doi.org/10.3389/fonc.2022.1044344)] [[Paper](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2022.1044344/full)] [[Code](https://gitee.com/doctortangmo/TCM-CRC-prognostic-model)]
- [*Frontiers in Pharmacology*] **双路径体外试验评价中药注射剂线粒体毒性** Shen, corresponding authors Feng and Ma and colleagues use a HepG2 glucose/galactose ATP assay and an HCT116 respiration-deficient proliferation assay to screen 35 TCM injections. Xiyanping, Dengzhanhuasu, Shuanghuanglian, and Yinzhihuang meet the authors’ mitochondrial-toxicity criteria, and rutin, baicalin, scutellarin, and forsythin are suggested as candidate constituents. This is an in-vitro screen, not a clinical trial. The license is CC BY. [[DOI](https://doi.org/10.3389/fphar.2022.1039235)] [[Paper](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.1039235/full)]
- [*Frontiers in Pharmacology*] **结构–活性与机器学习识别潜在保肝中药** He, corresponding authors Xie and Wang and colleagues use machine learning to predict hepatoprotective activity of TCM constituents and, with efficacy-class and property clustering, propose 12 potentially hepatoprotective herbs. A voting model reaches 0.871 accuracy on a 178-compound test set. Nine of the 12 herbs already have animal or cell-experiment support in the literature. This is computational prediction plus literature checking, not a new clinical trial. The license is CC BY. [[DOI](https://doi.org/10.3389/fphar.2022.969979)] [[Paper](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.969979/full)]
- [*Chinese Medicine*] **用人工智能筛选中西药联用中的肝毒性化合物** Chen, corresponding authors Zhao and Shang and colleagues collect 2,035 compounds and compare nine machine-learning methods and a deep belief network for screening hepatotoxicity of individual compounds used in combined Chinese and Western medicines. Random-forest accuracy is 0.838 on the training set and 0.767 on the test set; the deep belief network’s test accuracy is 82.2%. Data are available on request, and no code is given. The license is CC BY 4.0. [[DOI](https://doi.org/10.1186/s13020-022-00617-4)] [[Paper](https://cmjournal.biomedcentral.com/articles/10.1186/s13020-022-00617-4)]
- [*Engineering*] **利用证候要素架构中医人工智能诊疗模型（观点评论）** Wang Jie, Duan Lian, Li Hongzheng, Liu Jinlei, and Chen Hengwen publish a Views & Comments piece in Engineering (2022, 8(1)) arguing that syndrome elements can serve as a hub for TCM AI diagnostic models that combine rule ensembles, guideline symptom scores, graph-convolution knowledge graphs, and small-sample data, using eight coronary syndrome elements as an example. This is not a systematic review and reports neither training-set size nor test accuracy. The license is CC BY-NC-ND 4.0. It is not the same paper as the later modified-Transformer article by the same group in Chinese Journal of Experimental Traditional Medical Formulae. [[DOI](https://doi.org/10.1016/j.eng.2021.06.014)] [[Paper](https://www.engineering.org.cn/engi/CN/10.1016/j.eng.2021.06.014)]
- [*ICMLC*] **神经网络判别经方方名** A neural network trained on 261 formulae and 173 herbs extracted from the Shanghan Lun and the Synopsis of Prescriptions of the Golden Chamber. Given only the medicinal composition, it names the classical formula, and it is tested on modified formulae from different meridians. [[DOI](https://doi.org/10.1145/3529836.3529897)]
- [*Journal of Healthcare Engineering*] **按中医问诊思路做的证候辨证** Syndrome differentiation that follows TCM inquiry, aimed at consultation systems that ask too little and ignore inquiry principles. [[DOI](https://doi.org/10.1155/2022/6553017)]
- [*AAAI*] **多模态中医体质端到端评估** End-to-end TCM constitution assessment from face and tongue images, pulse and voice, and inquiry text. [[DOI](https://doi.org/10.1609/aaai.v36i11.21727)]
- [*Frontiers in Pharmacology*] **喜炎平联用药物与疑似过敏** A nested case-control study in a national medical-insurance sample on concomitant drugs and suspected allergic reactions with Xiyanping injection. Frontiers in Pharmacology, 2022. [[DOI](https://doi.org/10.3389/fphar.2022.883407)]
- [*BioMed Research International*] **乙肝中医 KG 问答系统** Knowledge-graph-based QA system for TCM diagnosis and treatment of viral hepatitis B. [First Affiliated Hospital of Henan University] [[DOI](https://doi.org/10.1155/2022/7139904)]
- [*Evidence-Based Complementary and Alternative Medicine*] **上海 2 型糖尿病问诊证候识别** Recognizes traditional Chinese medicine syndromes of type 2 diabetes from inquiry information collected in Shanghai. 2022. [[DOI](https://doi.org/10.1155/2022/2843218)]
- [*Digital Chinese Medicine*] **《伤寒论》知识图谱** Constructs a knowledge graph of the Treatise on Febrile Diseases and reports an application. [[DOI](https://doi.org/10.1016/j.dcmed.2022.12.006)]
- [*Digital Chinese Medicine*] **《伤寒论》异构图与图卷积表示** Builds a heterogeneous graph of the Treatise on Febrile Diseases and learns node representations with a graph convolutional network. [[DOI](https://doi.org/10.1016/j.dcmed.2022.12.007)]
- [*CCL*] **ZY-BERT** Domain TCM encoder from the TCM-SD paper (~0.4B-token corpus); weights are on cloud drive, with syndrome-differentiation fine-tune code in the repo. Not the same work as arXiv 2411.00897. [[Paper](https://arxiv.org/abs/2203.10839)] [[Published](https://aclanthology.org/2022.ccl-1.80/)] [[Code](https://github.com/Borororo/ZY-BERT)]
- [*World Health Organization*] **WHO 中医药国际标准术语** The World Health Organization's 2022 terminology standard for traditional Chinese medicine, so clinics, policy, and records can share the same concepts. The publications page offers a PDF for checking Chinese and English wording of patterns and the four examinations. [[Website](https://www.who.int/publications/i/item/9789240042322)] [[PDF](https://iris.who.int/bitstream/handle/10665/352306/9789240042322-eng.pdf)]
- [*BioMed Research International*] **TCMPR 子网术语映射处方推荐** Herb-symptom knowledge graph (~18k entities / ~100k relations) plus subnetwork term mapping and a CNN for prescription recommendation. [[DOI](https://doi.org/10.1155/2022/4845726)]
- [*Digital Health*] **Research and application of tongue and face diagnosis based on deep learning** Historical anchor: Research and application of tongue and face diagnosis based on deep learning. [[DOI](https://doi.org/10.1177/20552076221124436)]
- [*Journal of Ethnopharmacology*] **MGCN** Multi-graph convolutional prescription model on the Treatise on Cold Damage. Symptom features are aggregated on state-element and syndrome graphs, then an MLP predicts the herb set. [[DOI](https://doi.org/10.1016/j.jep.2022.115109)]
- [*Neural Networks*] **KDHR** Knowledge-driven herb recommendation by multi-layer graph-convolution fusion over a TCM knowledge graph. Code is public. [[DOI](https://doi.org/10.1016/j.neunet.2021.11.010)] [[Code](https://github.com/Rao-Yulong/KDHR)]
- [*Chinese Acupuncture & Moxibustion*] **GB/T 12346-2021 经穴名称与定位解读** Explains what changed in GB/T 12346-2021, Nomenclature and Location of Meridian Points, relative to the 2006 edition, including terms, definitions, body regions, and bone-proportional cun. [[DOI](https://doi.org/10.13703/j.0255-2930.20220117-k0001)]
- [*Evid. Based Complement. Alternat. Med.*] **Deep Learning Multi-label Tongue Image Analysis and Its Application in a Population Underg** Historical anchor: Deep Learning Multi-label Tongue Image Analysis and Its Application in a Population Underg. [[DOI](https://doi.org/10.1155/2022/3384209)]
- [*Digital Chinese Medicine*] **Data-driven based four examinations in TCM: a survey** Historical anchor: Data-driven based four examinations in TCM: a survey. [Beijing University of Civil Engineering and Architecture, University of Maryland, Baltimore, Shandong University] [[DOI](https://doi.org/10.1016/j.dcmed.2022.12.004)]
- [*Frontiers in Physiology*] **用舌象和脉象区分疾病性与非疾病性疲劳** Shi, corresponding author Xu and colleagues collect tongue and pulse data at Shuguang Hospital and use four classifiers to distinguish disease-related from non-disease fatigue. The roughly 85% accuracy in the abstract comes from tongue and pulse plus age and BMI; with tongue and pulse alone, logistic regression accuracy is about 67%. The data are not public, and no code is given. The license is CC BY. [[DOI](https://doi.org/10.3389/fphys.2021.708742)] [[Paper](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2021.708742/full)]
- [*BMC Medical Informatics and Decision Making*] **层次注意力网络检测中药处方中的功效特异药组** Chen and Liu (co-first) distill TCM prescriptions with a hierarchical attention network and then use Apriori to mine efficacy-specific herb groups. Across 13 test efficacies, overall mean accuracy after distillation is about 15.57%–23.83%, higher than the undistilled control. The gold standard comes from the internet and confirmation by one expert. Tables 1 and 2 carry unrelated footnotes. The license is CC BY 4.0. [[DOI](https://doi.org/10.1186/s12911-021-01411-2)] [[Paper](https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-021-01411-2)]
- [*JMIR Medical Informatics*] **远程监督的中医跨度实体抽取** Span-level named-entity extraction for traditional Chinese medicine, trained with distant supervision. JMIR Medical Informatics, 2021. [[DOI](https://doi.org/10.2196/28219)]
- [*Biomedical Signal Processing and Control*] **自适应神经模糊推理的中医睡眠障碍诊断** Uses an adaptive neuro-fuzzy inference system to diagnose sleep disorders in a traditional Chinese medicine setting. [[DOI](https://doi.org/10.1016/j.bspc.2021.102942)]
- [*Zenodo*] **经方按症状排序（平人）** Matches the pattern expected by a formula in the Shanghan zabing lun with the patient's present pattern and scores the fit from 0% to 100%. The method is implemented as the online program Pingren. Inputs are the book's own words for symptoms and course. Released December 2021, CC BY 4.0. [[DOI](https://doi.org/10.5281/zenodo.5804283)] [[Data](https://zenodo.org/records/5804283)]
- [*Scientific Reports*] **湖北中药注射剂自发报告** Analyzes spontaneous adverse-reaction reports for traditional Chinese medicine injections in Hubei from 2014 to 2019. Scientific Reports, 2021. [[DOI](https://doi.org/10.1038/s41598-021-88339-9)]
- [*Evidence-Based Complementary and Alternative Medicine*] **基于知识图谱的中成药处方监测** A prescription-monitoring program for Chinese patent medicines built on a knowledge graph. Evidence-Based Complementary and Alternative Medicine, 2021. [[DOI](https://doi.org/10.1155/2021/9970063)]
- [*Scientific Reports*] **台湾草药不良反应报告系统（1998–2016）** A system for reporting and evaluating adverse reactions to herbal medicine in Taiwan, covering 1998–2016. [[DOI](https://doi.org/10.1038/s41598-021-00704-w)]
- [*IEEE ICSGEA*] **中药处方剂量分配的模糊分析** Fuzzy analysis of how doses are allocated inside a traditional Chinese medicine prescription. [[DOI](https://doi.org/10.1109/icsgea53208.2021.00138)]
- [*Communications in Computer and Information Science*] **中医病历症状规范化的自动方法** Automated methods for normalizing symptom names in traditional Chinese medicine records. [[DOI](https://doi.org/10.1007/978-3-030-78615-1_42)]
- [*Journal of Pharmacopuncture*] **《温热经纬》与《伤寒论》方剂网络** Network analysis of herbal formulas from Wenre Jingwei and the Shanghan Lun. [[DOI](https://doi.org/10.3831/kpi.2021.24.3.138)]
- [*ISAIMS*] **Wasserstein GAN 扩充腕部脉象** Wasserstein GAN augmentation of wrist-pulse signals for traditional Chinese medicine. [[DOI](https://doi.org/10.1145/3500931.3501003)]
- [*Journal of Biomedical Informatics*] **KeMRE：中药说明书的知识增强关系抽取** Knowledge-enhanced relation extraction from Chinese medicine instruction texts. [[DOI](https://doi.org/10.1016/j.jbi.2021.103834)]
- [*Frontiers in Pharmacology*] **ICD-10 疾病与汉方寒热虚实的对应** At a Kampo clinic, relates ICD-10 diagnoses of patients aged 20 or older, seen from October 2014 through June 2019, to ICD-11 traditional-medicine modules such as heat–cold and excess–deficiency. [[DOI](https://doi.org/10.3389/fphar.2021.751403)]
- [*JMIR Medical Informatics*] **Ensemble Learning-Based Pulse Signal Recognition: Classification Model Development Study** Historical anchor: Ensemble Learning-Based Pulse Signal Recognition: Classification Model Development Study. [[DOI](https://doi.org/10.2196/28039)]
- [*IEEE Trans. Cybernetics*] **Automatic Construction of Chinese Herbal Prescriptions From Tongue Images Using CNNs and A** Historical anchor: Automatic Construction of Chinese Herbal Prescriptions From Tongue Images Using CNNs and A. [South China University of Technology, Guangdong General Hospital] [[DOI](https://doi.org/10.1109/tcyb.2019.2909925)]
- [*Mathematical Biosciences and Engineering*] **基于高维特征的高精度脉诊分类** Ching-Han Huang, Yu-Min Wang, and corresponding author Shana Smith publish a methods paper in Mathematical Biosciences and Engineering (2020, 17(6)) that extracts 71-dimensional features from ANSWatch pulse signals and uses principal-component analysis plus an artificial neural network to distinguish 10 pulse types. Twenty-seven principal components explaining 95% of variance reach a mean accuracy of 98.2%. The official version is downloadable under CC BY 4.0; no code or raw data are provided. DOI 10.3934/mbe.2020353. [[DOI](https://doi.org/10.3934/mbe.2020353)] [[Paper](https://www.aimspress.com/article/doi/10.3934/mbe.2020353)]
- [*Frontiers in Neuroscience*] **静息态功能连接预测原发性痛经针刺疗效** Yu and Xie (equal contribution), with corresponding authors Liang and Yang, randomize 54 patients with primary dysmenorrhea to true or sham acupuncture and analyze 35. True acupuncture significantly reduces pain; sham acupuncture does not. Leave-one-out regression uses eight baseline functional-connectivity features. The text and Figure 5 do not consistently match pain-change values and change rates. The license is CC BY. [[DOI](https://doi.org/10.3389/fnins.2020.559191)] [[Paper](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2020.559191/full)] [[Code](https://github.com/cdutcmysy/ROIwise_FC_mancova)]
- [*ICCIA*] **计算机视觉的中医面色识别** Deep learning finds 68 facial landmarks, segments regions such as the ting, cheeks, and mingtang, then reads TCM complexion from color histograms. [[DOI](https://doi.org/10.1109/iccia49625.2020.00029)]
- [*Sensors*] **穴位皮肤阻抗的手机脉诊** Feasibility study of TCM pulse diagnosis on a smartphone by measuring skin impedance at acupoints, approximating fingertip pressure over the artery. [[DOI](https://doi.org/10.3390/s20164618)]
- [*World Journal of Traditional Chinese Medicine*] **用自然语言处理挖掘《伤寒论》** Text mining and analysis of the Treatise on Febrile Diseases with natural language processing. [[DOI](https://doi.org/10.4103/wjtcm.wjtcm_28_19)]
- [*JMIR Medical Informatics*] **模仿肺癌中医辨证的端到端模型** End-to-end models trained to imitate traditional Chinese medicine syndrome differentiation in lung cancer diagnosis. [[DOI](https://doi.org/10.2196/17821)]
- [*Integrative Cancer Therapies*] **对 ICD-11 第26章传统医学条目的增补建议** Argues that ICD-11 Chapter 26, drawn from the WHO international standard terminologies, should keep the adopted patterns and add essential patterns that are still missing. [[DOI](https://doi.org/10.1177/1534735420908334)]
- [*BMC Bioinformatics*] **从文献为抗抑郁药不良反应寻找中药替代** Literature-based search for TCM alternatives that may lessen adverse reactions of western drugs, with depression treatment as the case. [[DOI](https://doi.org/10.1186/s12859-020-03735-8)]
- [*JMIR Medical Informatics*] **人工智能中医辅助诊断系统验证** Validation of an artificial-intelligence assistive diagnostic system for traditional Chinese medicine. JMIR Medical Informatics, 2020. [[DOI](https://doi.org/10.2196/17608)]
- [*Frontiers in Pharmacology*] **乳腺癌中医证型的神经网络区分** Uses a neural network and clustering to separate traditional Chinese medicine patterns in people with breast cancer. Frontiers in Pharmacology, 2020. [[DOI](https://doi.org/10.3389/fphar.2020.00670)]
- [*Journal of Ethnopharmacology*] **中药心脏不良反应的文献计量与关联规则** Bibliometrics and association rules for cardiac adverse reactions attributed to Chinese materia medica. [[DOI](https://doi.org/10.1016/j.jep.2020.112582)]
- [*BMC Medical Informatics and Decision Making*] **中医临床细粒度 NER 语料** Fine-grained entity-recognition corpus built from TCM clinical records. [Chengdu University of Information Technology] [[DOI](https://doi.org/10.1186/s12911-020-1079-2)]
- [*IEEE ICKG*] **TCMKG** Deep-learning-based TCM knowledge graph platform. [University of Electronic Science and Technology of China] [[DOI](https://doi.org/10.1109/ICBK50248.2020.00084)]
- [*Chinese Medicine*] **SiPA：同时预测中药相互作用** SiPA predicts several interactions at once so the TCM network among constituents, targets, and diseases can be expanded. [[DOI](https://doi.org/10.1186/s13020-020-00369-z)]
- [*arXiv*] **SMGCN** Syndrome-aware multi-graph convolution for herb recommendation. Besides the symptom–herb graph, it adds symptom and herb co-occurrence graphs, fuses an implicit syndrome vector, then ranks herbs. [[Paper](https://arxiv.org/abs/2002.08575)]
- [*Journal of Integrative Medicine*] **PIPE-11：落地 ICD-11 传统医学章的临床决策支持** Pattern Identification and Prescription Expert-11, a decision-support system for putting the ICD-11 traditional medicine chapter into computable pattern identification and prescription. [[DOI](https://doi.org/10.1016/j.joim.2020.08.003)]
- [*Comput. Struct. Biotechnol. J.*] **Artificial intelligence in tongue diagnosis: Using deep convolutional neural network for r** Historical anchor: Artificial intelligence in tongue diagnosis: Using deep convolutional neural network for r. [Being University of Chinese Medicine, Beijing 100029, China, Beijing University of Posts and Telecommunications, Beijing 100876, China, Beijing Normal University, Beijing 100875, China] [[DOI](https://doi.org/10.1016/j.csbj.2020.04.002)]

</details>

<details>
<summary>2010s · 67</summary>

- **北京中医药大学《中医入门》中国大学MOOC课程（王彤）** A China University MOOC introductory course on traditional Chinese medicine, taught by Wang Tong of Beijing University of Chinese Medicine. It introduces TCM through medical anecdotes, methods, theory, and practice. The official course page was opened in this pass. The current term runs from 28 September 2026 to 20 January 2027; the platform also records an earlier offering from October 2019. This is a formal university open course, not a marketing clip. [[Link](https://www.icourse163.org/course/BUCM-1206405809)]
- **北京中医药大学《中医基础理论》中国大学MOOC课程（马淑然）** A China University MOOC course on Fundamental Theories of Traditional Chinese Medicine, taught by Ma Shuran of Beijing University of Chinese Medicine and aimed at TCM students and general learners. It covers yin-yang and the five phases, visceral manifestation and meridians, qi, blood and body fluids, etiology and pathogenesis, and treatment principles. The official course page was opened in this pass. The current term runs from 14 September 2026 to 20 January 2027; the platform also records an earlier offering from October 2019. This is a formal university open course, not a marketing clip. [[Link](https://www.icourse163.org/course/BUCM-1206410812)]
- [*PLOS Computational Biology*] **用机器学习预测中药归经** Wang, corresponding author Tang and colleagues collect 646 herbs and their constituents’ molecular fingerprints and ADME features from TCMID, and they predict meridian tropism at the herb and compound levels. The abstract’s highest accuracy is 0.83; in Table 2 the highest balanced accuracy for compound-level random forests is 0.67. Code is posted on GitHub. The license is CC BY. [[DOI](https://doi.org/10.1371/journal.pcbi.1007249)] [[Paper](https://doi.org/10.1371/journal.pcbi.1007249)] [[Code](https://github.com/herb-medicne/meridian-prediction)]
- [*European Journal of Integrative Medicine*] **舌、声、脉联合的中医体质辨识** TCM constitution diagnosis that combines tongue, voice, and pulse indices. [[DOI](https://doi.org/10.1016/j.eujim.2019.04.001)]
- [*arXiv*] **脉搏压力波与妊娠的机器学习对应** Deep learning relates the pulse pressure wave to pregnancy. The paper reports 84% accuracy and an AUC of 91%. The signal is the pressure wave, not the TCM pulse qualities of position, rate, shape, and force. [[Paper](https://arxiv.org/abs/1910.01726)]
- [*IEEE Trans. Cybernetics*] **Tooth-Marked Tongue Recognition Using Multiple Instance Learning and CNN Features** Historical anchor: Tooth-Marked Tongue Recognition Using Multiple Instance Learning and CNN Features. [Shanghai University, Shanghai University of Engineering Science] [[DOI](https://doi.org/10.1109/tcyb.2017.2772289)]
- [*JAMIA*] **TCM-BERT** BERT further pretrained on TCM clinical text for five-way disease classification (JAMIA 2019). CKCEST holds copyright; the full 46,205 records are not released, only splits plus drive-hosted fine-tuned weights. [[DOI](https://doi.org/10.1093/jamia/ocz164)] [[Code](https://github.com/yao8839836/tcm_bert)]
- [*Neurocomputing*] **IHPreten：配伍禁忌药对预测** A supervised model with attribute regularization that predicts incompatible herb pairs in traditional Chinese medicine. [[DOI](https://doi.org/10.1016/j.neucom.2019.02.017)]
- [*Xu HY et al., *Nucleic Acids Res* 47(D1):D976-D982*] **ETCM** Historical anchor: ETCM. [[DOI](https://doi.org/10.1093/nar/gky987)]
- [*BMC Medical Informatics and Decision Making*] **An ontological framework for the formalization, organization and usage of TCM-Knowledge** Historical anchor: An ontological framework for the formalization, organization and usage of TCM-Knowledge. [Leipzig University] [[DOI](https://doi.org/10.1186/s12911-019-0760-9)]
- [*IEEE Access*] **ANDERATION：反社区发现用于中药配伍禁忌** Anti-community detection, using a node's degree and its inner-to-outer degree ratio, applied to herb incompatibility in TCM. [[DOI](https://doi.org/10.1109/access.2019.2934227)]
- [*ACM CIKM*] **配伍禁忌药对的监督学习框架** A supervised learning framework for incompatible herb pairs, a 2018 conference paper in the same line as the later IHPreten model. [[DOI](https://doi.org/10.1145/3269206.3269241)]
- [*IEEE IAEAC*] **语义中医方剂知识图谱 (Miao et al. 2018)** Semantic TCM prescription knowledge graph built top-down from formula texts. [Communication University of China, Academy of Broadcasting Science] [[DOI](https://doi.org/10.1109/IAEAC.2018.8577236)]
- [*arXiv*] **糖尿病证候的多实例多任务卷积网络** Treats a diabetic patient's record as a one-dimensional image and symptoms as pixels. A multi-instance multi-task convolutional network finds relevant symptoms and maps them to syndromes. [[Paper](https://arxiv.org/abs/1812.07764)]
- [*arXiv*] **由多尺度面容生成中药处方** A convolutional model that builds an herbal prescription from multi-scale facial features, rather than from symptoms alone. [[Paper](https://arxiv.org/abs/1812.06847)]
- [*BioMed Research International*] **桡动脉脉搏波的高血压机器学习分类** Machine-learning comparison of radial pulse waves from 450 people with hypertension and 479 healthy people, as an objective reference for TCM pulse diagnosis. [[DOI](https://doi.org/10.1155/2018/2964816)]
- [*BMC Medical Informatics and Decision Making*] **中药不良反应信号的决策树分类** Decision-tree classification for signal detection in traditional Chinese medicine pharmacovigilance. BMC Medical Informatics and Decision Making, 2018. [[DOI](https://doi.org/10.1186/s12911-018-0599-5)]
- [*CISP-BMEI*] **Constitution Identification of Tongue Image Based on CNN** Historical anchor: Constitution Identification of Tongue Image Based on CNN. [Beijing University of Technology] [[DOI](https://doi.org/10.1109/cisp-bmei.2018.8633075)]
- [*Journal of Biomedical Semantics*] **自动构建中文症状知识库** Corresponding author Ruan and colleagues automatically build a Chinese symptom knowledge base from eight medical websites, three Chinese encyclopedias, and 250,000 electronic records from Shanghai Shuguang Hospital, and they link it to UMLS. The results section reports 135,485 entities and 26,821 symptoms (including 3,968 TCM symptoms); the conclusion writes 135,484. For the electronic-record CRF, only precision is given. The knowledge base was released as linked open data. The license is CC BY 4.0. A previously listed Datahub dataset URL now redirects to a generic publications page and is not used as a source here. [[DOI](https://doi.org/10.1186/s13326-017-0145-x)] [[Paper](https://jbiomedsem.biomedcentral.com/articles/10.1186/s13326-017-0145-x)]
- [*InTech*] **妊娠禁忌中药概述** A book chapter surveying Chinese medicines that are contraindicated in pregnancy. [[DOI](https://doi.org/10.5772/67066)]
- [*Artificial Intelligence in Medicine*] **中医养生知识图谱 (Yu et al. 2017)** Large TCM health-preservation knowledge graph integrating terms, literature, and databases, with retrieval, visualization, and recommendation. [[DOI](https://doi.org/10.1016/j.artmed.2017.04.001)]
- [*Nucleic Acids Research*] **PharmMapper** Upload a 3D molecular structure and get possible protein targets. The 2017 update covers 23,236 proteins, with 16,159 druggable pharmacophore models and 51,431 ligandable ones, clustered from the 1 January 2016 PDB snapshot. Useful when a herb constituent has a structure but no measured target. [[Website](https://www.lilab-ecust.cn/pharmmapper/)] [[About](https://www.lilab-ecust.cn/pharmmapper/help.php)] [[DOI](https://doi.org/10.1093/nar/gkx374)]
- [*China Journal of Chinese Materia Medica*] **GB/T 31774 与 ISO 18668 中药编码对照** Compares the Chinese national coding standard GB/T 31774-2015 with ISO 18668 parts 1–4 for Chinese medicines. [[DOI](https://doi.org/10.19540/j.cnki.cjcmm.20170426.003)]
- [*BioMed Research International*] **Diagnostic Method of Diabetes Based on Support Vector Machine and Tongue Images** Historical anchor: Diagnostic Method of Diabetes Based on Support Vector Machine and Tongue Images. [[DOI](https://doi.org/10.1155/2017/7961494)]
- [*Journal of Integrative Medicine*] **高血压患者的寸口脉与脉搏波** Compares TCM wrist pulse-taking with pulse-waveform analysis and hemodynamics in people with hypertension. [[DOI](https://doi.org/10.1016/s2095-4964(16)60233-9)]
- [*Frontiers in Pharmacology*] **附子毒性成分指数** Weights aconitine, mesaconitine, and hypaconitine by minimum lethal dose and defines a toxic-constituents index for aconite, instead of adding the three diester-alkaloid contents directly. Frontiers in Pharmacology, 2016. [[DOI](https://doi.org/10.3389/fphar.2016.00164)]
- [*arXiv*] **舌、面与舌下融合识别糖尿病** Fuses tongue, face, and sublingual images to detect diabetes and impaired glucose regulation. Earlier work used only one of these views. [[Paper](https://arxiv.org/abs/1604.03443)]
- [*Chinese Journal of Electronics*] **模糊支持向量机的中医面色识别** After cheek segmentation, a fuzzy support vector machine with color modeling recognizes TCM facial complexion and reduces the effect of outliers. [[DOI](https://doi.org/10.1049/cje.2016.05.013)]
- [*Journal of Traditional Chinese Medical Sciences*] **彩色人脸特征的中医体质分类** Color face images of 5,150 people, with face detection and landmarks, used to classify TCM constitution from facial features. [[DOI](https://doi.org/10.1016/j.jtcms.2016.12.001)]
- [*International Symposium on Computer, Consumer and Control*] **九层卷积网络的腕部脉象分类** A 9-layer convolutional network classifies TCM wrist-pulse signals without handcrafted features. The recordings are not public. [[DOI](https://doi.org/10.1109/is3c.2016.101)]
- [*IEEE BIBM*] **中医期刊关系抽取 (Wang & Poon 2016)** Relation extraction from TCM journal full text to support later knowledge-graph construction. [The University of Sydney] [[DOI](https://doi.org/10.1109/BIBM.2016.7822725)]
- [*Physica A*] **《伤寒论》的复杂网络模型** A complex-network model of the Treatise on Cold Damage. [[DOI](https://doi.org/10.1016/j.physa.2016.03.115)]
- **北京中医药大学《中药安全用药导论》中国大学MOOC课程（张冰等）** A China University MOOC course on the safe use of Chinese medicines, taught by Zhang Bing, Lin Zhijian, and Zhang Xiaomeng of Beijing University of Chinese Medicine. It covers pharmacovigilance, recognition of adverse reactions, and safety issues of commonly used Chinese patent medicines. The course description states that it was recognized as a 2017 national-level quality online open course. The official course page was opened in this pass. The current term runs from 7 September to 14 December 2026; the platform also records an earlier offering from October 2015. This is a formal university open course, not a marketing clip. [[Link](https://www.icourse163.org/course/BUCM-387003)]
- [*BMC Complementary and Alternative Medicine*] **腕部关脉物理量与高血压关联的预试验** Lee, corresponding author Kim and colleagues analyze the association of guan-position pulse-wave physical quantities with hypertension, and their predictive value, in 393 Korean women aged 46–73. This is a pilot: only 52 hypertension cases, classes are imbalanced, and sensitivity for the hypertension class is very low. It should not be merged with other pulse-and-hypertension entries. The license is CC BY 4.0. [[DOI](https://doi.org/10.1186/s12906-015-0756-7)] [[Paper](https://bmccomplementalternmed.biomedcentral.com/articles/10.1186/s12906-015-0756-7)]
- [*Evidence-Based Complementary and Alternative Medicine*] **希尔伯特–黄变换与随机森林的冠心病脉象识别** Hilbert–Huang energy and sample entropy of TCM pulse signals, classified with a random forest to separate coronary heart disease from healthy people. [[DOI](https://doi.org/10.1155/2015/895749)]
- [*China Journal of Chinese Materia Medica*] **含反药的附子处方关联规则** Association-rule analysis of aconite prescriptions that contain incompatible herbs, comparing regions and compatibility features. [[DOI](https://doi.org/10.4268/cjcmm20150639)]
- [*PLOS ONE*] **共形预测与随机森林用于慢性疲劳中医证素多标签学习** Wang, corresponding author Yang and colleagues apply conformal prediction and random forests to 736 chronic-fatigue cases for multi-label classification of four syndrome elements, and they compare conformal naive Bayes, conformal k-NN, and ML-KNN. The highest subset accuracy is 0.9959, but only leave-one-out cross-validation is used. Data are provided in the supplement. The license is CC BY. [[DOI](https://doi.org/10.1371/journal.pone.0099565)] [[Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0099565)]
- [*IEEE BIBM*] **视频面部特征的中医望神分类** Classifies TCM spirit inspection from facial features in video. The videos are not public. [[DOI](https://doi.org/10.1109/bibm.2014.6999314)]
- [*arXiv*] **用伽马密度拟合中医脉图** Fits Chinese pulse waveforms with collective gamma density functions to produce quantitative classification indices. [[Paper](https://arxiv.org/abs/1402.6649)]
- [*IEEE CIBCB*] **深度卷积网络分析腕部脉波** Shannon energy envelope and the Hilbert transform extract the wrist pulse, then a deep convolutional network recognizes it for TCM pulse diagnosis. [[DOI](https://doi.org/10.1109/cibcb.2014.6845525)]
- [*Evidence-Based Complementary and Alternative Medicine*] **小波包分形维的闻诊** Turns traditional Chinese medicine listening into a computable syndrome task with wavelet-packet fractal dimension and a support vector machine. 2014. [[DOI](https://doi.org/10.1155/2014/502348)]
- [*International Journal of Pattern Recognition and Artificial Intelligence*] **均匀色空间的中医面色识别** Recognizes TCM facial complexion in a uniform Lab color space. The face images are not public. [[DOI](https://doi.org/10.1142/s0218001414500086)]
- [*IEEE ICCA*] **冠心病、其他心血管病与健康人的脉象参数** Pressure-sensor pulse recordings from 251 people: 102 with coronary heart disease, 94 with other cardiovascular disease, and 55 healthy people. The recordings are not public. [[DOI](https://doi.org/10.1109/icca.2014.6871077)]
- [*Evidence-Based Complementary and Alternative Medicine*] **中风患者韩医四诊的观察者一致性** Two clinicians independently examined 168 hospitalized stroke patients with Korean-medicine pattern identification. AC1 was 0.66–0.89 for pulse, 0.66–0.95 for inspection, 0.67–0.88 for listening and smelling, and 0.62–0.94 for inquiry. [Korea Institute of Oriental Medicine] [[DOI](https://doi.org/10.1155/2014/465471)]
- [*BioMed Research International*] **中医面色的定性与定量分析** Computerized qualitative and quantitative recognition of facial color and gloss, reducing the subjectivity of experience-based face diagnosis. [[DOI](https://doi.org/10.1155/2014/207589)]
- [*Journal of Biomedical Informatics*] **中医症状名识别** Supervised methods for symptom name recognition in free-text TCM clinical records. [Sichuan Agricultural University, Beihua University] [[DOI](https://doi.org/10.1016/j.jbi.2013.09.008)]
- [*Ru J et al., *J Cheminform* 6(1):13*] **TCMSP** Historical anchor: TCMSP. [North West Agriculture and Forestry University, Northwest A&F University, Dalian University of Technology, Dalian University] [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- [*Comput. Math. Methods Med.*] **Pulse Waveform Classification Using Support Vector Machine with Gaussian Time Warp Edit Di** Historical anchor: Pulse Waveform Classification Using Support Vector Machine with Gaussian Time Warp Edit Di. [Harbin Ice Flower Hospital, Harbin 150086, China] [[DOI](https://doi.org/10.1155/2014/947254)]
- [*Evid. Based Complement. Alternat. Med.*] **A disturbance rejection framework for the study of traditional Chinese medicine** Historical anchor: A disturbance rejection framework for the study of traditional Chinese medicine. [Cleveland State University] [[DOI](https://doi.org/10.1155/2014/787529)]
- [*Journal of Alternative and Complementary Medicine*] **用声学特征辨体质** Uses acoustic features of the voice to identify constitutions in traditional Chinese medicine. Journal of Alternative and Complementary Medicine, 2013. [[DOI](https://doi.org/10.1089/acm.2012.0478)]
- [*Evidence-Based Complementary and Alternative Medicine*] **方剂网络中的十八反与十九畏** A network of 362 TCM formulas, plus chemical space and metabolism space, used to examine the eighteen antagonisms and nineteen mutual inhibitors. [[DOI](https://doi.org/10.1155/2013/352145)]
- [*Xue R et al., *Nucleic Acids Res* 41(D1):D1089-D1095*] **TCMID** Historical anchor: TCMID. [Shanghai Jiao Tong University, Shanghai Mental Health Center] [[DOI](https://doi.org/10.1093/nar/gks1100)]
- [*BMC Complementary and Alternative Medicine*] **面像、体型、声音和问卷融合的四象体质辨识** KIOM fused face images, body shape, voice, and questionnaires from 2,973 patients at 23 Korean-medicine clinics to classify Sasang constitution. Test accuracy was 64.0% for men and 55.2% for women. The images and questionnaires are not publicly posted. [Korea Institute of Oriental Medicine] [[DOI](https://doi.org/10.1186/1472-6882-12-85)]
- [*Bioinformation*] **基于结构相似的中药心血管毒性预测软件** Structure-similarity software for predicting cardiovascular toxicity of traditional Chinese medicine. [[DOI](https://doi.org/10.6026/973206300080110)]
- [*BMC Complementary and Alternative Medicine*] **唇色的中医望诊分类** Classifies lip color for traditional Chinese medicine inspection with multi-class support vector machines. BMC Complementary and Alternative Medicine, 2012. [[DOI](https://doi.org/10.1186/1472-6882-12-127)]
- [*Evid. Based Complement. Alternat. Med.*] **Automated Tongue Feature Extraction for ZHENG Classification in Traditional Chinese Medici** Historical anchor: Automated Tongue Feature Extraction for ZHENG Classification in Traditional Chinese Medici. [[DOI](https://doi.org/10.1155/2012/912852)]
- [*China Journal of Chinese Materia Medica*] **胸痹处方中的十八反关联规则** Association-rule mining of the eighteen incompatible medicaments inside chest-pain prescriptions. [[DOI](https://doi.org/10.4268/cjcmm20112434)]
- [*Chinese Medicine*] **用关联开放数据整合传统医药与现代药学研究（评论）** Corresponding author Samwald and colleagues publish a 2010 commentary in Chinese Medicine that uses the search for potentially antidepressant TCM plants as a use case for linked open data. The authors manually encode 76 assertions and interlink them with an RDF version of TCMGeneDIT. This is a commentary plus a small prototype, not a completed drug-discovery study. The license is CC BY 2.0. [[DOI](https://doi.org/10.1186/1749-8546-5-43)] [[Paper](https://cmjournal.biomedcentral.com/articles/10.1186/1749-8546-5-43)]
- [*BMC Bioinformatics*] **DMIM 药物网络与共模块分析（李梢等）：揭示中医方剂组合规则** Corresponding author Li Shao, with Zhang, Jiang, Wei, and Zhang, present DMIM, building a herb network from 3,865 collaterals-related formulas and discussing multi-layer co-modules with Liuwei Dihuang Wan as an example. In vitro tests report IC50 values of 3.2 μM for vitexicarpin and 3.4 μM for timosaponin A-III (author-reported). This should not be merged with the same-year drugCIPHER paper, TCMSP, HERB, or the 2026 DeepTCM entry. The Li Shao person page was not changed. [[DOI](https://doi.org/10.1186/1471-2105-11-S11-S6)] [[Paper](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-11-S11-S6)]
- [*PLoS ONE*] **drugCIPHER（Zhao、李梢）：关联药理空间与基因组空间的药物靶点推断框架** Zhao and Li Shao present drugCIPHER, a 2010 general pharmacology framework that uses linear regression to relate drug-treatment and chemical similarity to proximity on a protein-interaction network and thereby infer targets at a genome-wide scale. Later TCM reviews cite the method. It should not be merged with TCMSP or the 2026 DeepTCM entry already in this catalog. [[DOI](https://doi.org/10.1371/journal.pone.0011764)] [[Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0011764)]
- [*Chinese Medicine*] **语义网用于中医药数据协调（社论）** Corresponding author Cheung and Chen publish a 2010 editorial in Chinese Medicine arguing for Semantic Web representation and harmonization of Chinese and Western medical data. The text cites DartGrid and states that the China Academy of Chinese Medical Sciences ontology has more than 8,000 classes and 50,000 instances, which differs from the author-reported figures in the 2007 system paper already in this catalog. This is a short editorial with no new data or evaluation. The license is CC BY 2.0. [[DOI](https://doi.org/10.1186/1749-8546-5-2)] [[Paper](https://cmjournal.biomedcentral.com/articles/10.1186/1749-8546-5-2)]
- [*BMC Complementary and Alternative Medicine*] **冠心病问诊的多标签学习** Models inquiry-based diagnosis of coronary heart disease in traditional Chinese medicine with multi-label learning. BMC Complementary and Alternative Medicine, 2010. [[DOI](https://doi.org/10.1186/1472-6882-10-37)]
- [*BMC Bioinformatics*] **中医病历症状名自动规范化** Automatically maps symptom names in TCM electronic records onto a unified terminology, so mining can use clinical records rather than only manually extracted formulas. [[DOI](https://doi.org/10.1186/1471-2105-11-40)]
- [*Journal of Biomedical Informatics*] **Text mining for traditional Chinese medical knowledge discovery: a survey** Historical anchor: Text mining for traditional Chinese medical knowledge discovery: a survey. [University of Bradford] [[DOI](https://doi.org/10.1016/j.jbi.2010.01.002)]
- [*Journal of Chinese Integrative Medicine*] **Feature extraction and recognition of traditional Chinese medicine pulse based on hemodyna** Historical anchor: Feature extraction and recognition of traditional Chinese medicine pulse based on hemodyna. [[Link](http://www.jcimjournal.com/EN/10.3736/jcim20100802)]
- [*Artificial Intelligence in Medicine*] **Development of traditional Chinese medicine clinical data warehouse for medical knowledge ** Historical anchor: Development of traditional Chinese medicine clinical data warehouse for medical knowledge . [Guang’anmen Hospital] [[DOI](https://doi.org/10.1016/j.artmed.2009.07.012)]
- [*EURASIP J. Adv. Signal Process.*] **Classification of Pulse Waveforms Using Edit Distance with Real Penalty** Historical anchor: Classification of Pulse Waveforms Using Edit Distance with Real Penalty. [[DOI](https://doi.org/10.1155/2010/303140)]

</details>

<details>
<summary>2000s · 13</summary>

- [*Evidence-Based Complementary and Alternative Medicine*] **用面部几何特征区分四象体质** Selects distances, angles, and distance ratios from facial photographs to distinguish Sasang constitution. The abstract counts 1,225 distance features, 61,250 angle features, and 749,700 ratio features. The photographs are not public. [Korea Institute of Oriental Medicine] [[DOI](https://doi.org/10.1093/ecam/nep065)]
- [*IEEE CSIE*] **Syndrome Differentiation in Intelligent TCM Diagnosis System** Historical anchor: Syndrome Differentiation in Intelligent TCM Diagnosis System. [Xiamen University] [[DOI](https://doi.org/10.1109/csie.2009.782)]
- [*Int. J. Information Technology & Decision Making*] **Equilibrium and nonequilibrium modeling of YinYang WuXing for diagnostic decision support ** Historical anchor: Equilibrium and nonequilibrium modeling of YinYang WuXing for diagnostic decision support . [[DOI](https://doi.org/10.1142/s0219622009003521)]
- [*IEEE ITME*] **Traditional Chinese medical diagnosis based on fuzzy and certainty reasoning** Historical anchor: Traditional Chinese medical diagnosis based on fuzzy and certainty reasoning. [Memorial University of Newfoundland] [[DOI](https://doi.org/10.1109/itme.2008.4743874)]
- [*WWW* (demo/industrial)*] **Information retrieval and knowledge discovery on the semantic web of traditional Chinese m** Historical anchor: Information retrieval and knowledge discovery on the semantic web of traditional Chinese m. [[DOI](https://doi.org/10.1145/1367497.1367668)]
- [*Journal of Chinese Integrative Medicine*] **Establishment of a fuzzy mathematical model for syndrome differentiation of gastric cancer** Historical anchor: Establishment of a fuzzy mathematical model for syndrome differentiation of gastric cancer. [[Link](http://www.jcimjournal.com/EN/10.3736/jcim20081104)]
- [*IEEE BMEI*] **Building Clinical Data Warehouse for Traditional Chinese Medicine Knowledge Discovery** Historical anchor: Building Clinical Data Warehouse for Traditional Chinese Medicine Knowledge Discovery. [Guang’anmen Hospital] [[DOI](https://doi.org/10.1109/bmei.2008.83)]
- [*BMC Bioinformatics*] **面向中医药的语义电子科研** Corresponding author Chen and colleagues describe a TCM e-science system based on ontologies, semantic views, and grid services, including DartMapping, DartSearch, DartQuery, and DartFlow. They report an ontology of more than 20,000 classes and 100,000 instances and a system linked to more than 50 databases and 800 services (author-reported). This is a system description without an independent quantitative evaluation. The license is CC BY 2.0. [[DOI](https://doi.org/10.1186/1471-2105-8-S3-S6)] [[Paper](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-8-S3-S6)]
- [*World Health Organization*] **WHO 西太区传统医学术语** The World Health Organization Western Pacific terminology for traditional medicine, the 2007 predecessor of the 2022 Chinese-medicine terminology. The PDF is on IRIS. [[Website](https://iris.who.int/handle/10665/206952)] [[PDF](https://iris.who.int/server/api/core/bitstreams/24400634-2d52-4dde-bbb1-d28ee2c6fd42/content)]
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
<summary>Curated lists (6)</summary>

- **针灸临床实践指南数据集** — A dataset of acupuncture clinical practice guidelines, released to make the guidelines easier to use in clinic. [[Paper](https://doi.org/10.1038/s41597-026-08112-3)]
- **CPM Chinese patent medicine dataset** — Living large-scale public Chinese patent medicine data accompanying RAG-CPMF. [[Data](https://gitee.com/tcmdoc/cpm)] [[Paper](https://doi.org/10.1016/j.phrs.2025.107883)]
- **awesome_Chinese_medical_NLP** — Curated list of Chinese medical NLP resources: terminologies, corpora, word vectors, pretrained models, KGs, NER and QA (incl. CBLUE). [[Resources](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)]
- **内蒙古自治区民族药目录** — Public ethnic-medicine catalogue PDF from the Inner Mongolia Healthcare Security Administration, mainly finished Mongolian formulas. The government filename is dated 25 December 2023. The extracted text is titled the Inner Mongolia ethnic-medicine catalogue and notes that listed drugs are managed as class B. It is a reimbursement list, not a research compound database. [[Catalogue](https://ylbzj.nmg.gov.cn/zwgk/zfxxgk/fdzdgknr/bmwj/202312/P020231225623619008689.pdf)]
- **中医药中英术语数据集** — A Chinese–English terminology dataset for traditional Chinese medicine, published in China Scientific Data. [[Paper](https://doi.org/10.11922/csdata.2021.0009.zh)]
- **中医体质量表计分代码** — SAS code, SPSS syntax, and an Excel test sheet for scoring the Constitution in Chinese Medicine Questionnaire. Released January 2021, CC BY 4.0. [[DOI](https://doi.org/10.5281/zenodo.4431679)] [[Data](https://zenodo.org/records/4431679)]

</details>

<details>
<summary>Formula / extract databases (46)</summary>

- **中药扰动转录组图谱** — Harmonized transcriptomic atlas of traditional Chinese medicine perturbations, assembled from public treatment experiments. [[Paper](https://doi.org/10.1038/s41597-026-06988-9)]
- **中药化学成分毒性实验库** — Literature-derived in vivo and in vitro toxicity experiments for chemical constituents of traditional Chinese medicines, including Naoyanghua, Banmao, croton, Yangjinhua, Fuzi, and Qingfen. Fields cover route, species, indicators such as LD50, toxic dose, target organ, pathology, and PMID. [[Dataset](https://doi.org/10.57760/sciencedb.015ml)]
- **中医世家** — An online reader for TCM classics, herbs, formulas, and case records. The formula index has 25,425 entries, browsable by initial character or pinyin, and the herb index has 11,307 entries. [[Website](https://www.zysjw.com.cn/)] [[Link](https://www.zysjw.com.cn/zhongyaofang/index.html)] [[Herbs](https://www.zysjw.com.cn/zhongyaocai/index.html)]
- **TCMToxDB** — A toxicity database that separates toxic effects of formulas, herbs, and ingredients, and gathers targets for specific toxic manifestations. Five herb–target and ingredient–target prediction algorithms are included. Site: https://www.sdu-idea.cn/TCMToxDB. [[Paper](https://doi.org/10.1093/database/baag019)] [[Website](https://www.sdu-idea.cn/TCMToxDB)]
- **TCMDI** — Benchmark for predicting contraindicated interactions between traditional Chinese medicines and drugs. [[Dataset](https://github.com/hellowangqian/TCMDI)]
- **TCM-QM** — Gas-phase DFT descriptors for 3,196 TCM-related molecules, with 16,918 deduplicated herb–molecule provenance links. [[Dataset](https://zenodo.org/records/22173180)]
- **TCM-MS2Link** — AI-ready dataset joining curated herb–compound links (TCM-MolLink) with MS/MS spectra. [[Dataset](https://doi.org/10.57760/sciencedb.31921)]
- **Cross-linguistic TCM Formula Names** — Cross-linguistic table of TCM formula names in Chinese, Japanese Kampo, Korean Han medicine, and English, compiled from official formularies and clinical references in Taiwan. [[Dataset](https://zenodo.org/records/18724305)]
- **CHM-315** — Fine-grained Chinese herbal-medicine image set with 315 categories and 126,000 images, 400 images per category. [[Dataset](https://doi.org/10.6084/m9.figshare.32745123)]
- **Baize TCM Botanical Origin Images** — Medicinal-plant origin images for Baize Traditional Chinese Medicine, covering habitats, original plants, and medicinal parts, with Chinese and Latin identification based on the Chinese Pharmacopoeia, Flora of China, and the Engler system. [[Dataset](https://doi.org/10.57760/sciencedb.41638)]
- **古代经典名方关键信息表** — Official key-information tables for ancient classic formulas, not patient records. The notices cover 7 formulas in 2020, 25 including Zhuye Shigao Tang in 2023, and 43 including Xuanfu Daizhe Tang in 2025. The 2025 table gives source, processing, and gram doses. In Xuanfu Daizhe Tang, licorice is dry-fried (41.40 g) and pinellia is Qing Ban Xia (34.50 g). The decoction uses 2000 mL of water, reduces to 1200 mL, removes the marc, boils again to 600 mL, and is taken warm at 200 mL three times a day. [[2020](http://www.natcm.gov.cn/kejisi/zhengcewenjian/2020-11-10/18132.html)] [[2023](http://www.natcm.gov.cn/kejisi/gongzuodongtai/2023-07-28/31404.html)] [[2025](http://www.natcm.gov.cn/kejisi/gongzuodongtai/2025-02-12/35831.html)] [[2025PDF](https://www.nmpa.gov.cn/directory/web/nmpa/images/1739501159108056814.pdf)]
- **传统方剂—疾病关系标注语料** — Annotated corpus of traditional formula–disease relations in biomedical articles. Formulas are herb combinations prepared under traditional medicine principles. [[Paper](https://doi.org/10.1038/s41597-025-04377-2)]
- **TCMP-300** — Image dataset of traditional Chinese medicinal plants for plant recognition. [[Paper](https://doi.org/10.1038/s41597-025-05522-7)] [[Code](https://github.com/winycg/TCMP-300)]
- **NPASS** — A database of measured activity for natural products. This version lists 204,023 natural products, 48,940 source organisms, 8,764 targets, and 1,048,756 activity records, with values drawn from ChEMBL and the literature. Species records were also taken from TCM-ID, TCMID, TCMSP, and TM-MC. The 2026 update appeared in Nucleic Acids Research in November 2025. [[Website](https://bidd.group/NPASS/)] [[About](https://bidd.group/NPASS/about.php)] [[DOI](https://doi.org/10.1093/nar/gkaf1196)]
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
- **治法–处方与药材剂量表** — The repository readme describes 23 treatment methods, more than 400 subcategories, 4,174 common medicinal materials with doses and sources, and more than 900 classic formulas, with 21 feature categories. Files include Treatment.csv and a treatment–prescription workbook. [[Dataset](https://github.com/lin-haust/TCM-prescription-datasets)]
- **TCM-Suite** — A site that joins herb identification with network pharmacology. The Watson section currently lists 6,692 formulas, 7,322 herbs, 704,321 compounds, 19,319 proteins, and 15,437 diseases. Holmes identifies herbs with marker genes. Described in iMeta in 2022. [[Website](https://tcm-suite.geneis.cn/)] [[DOI](https://doi.org/10.1002/imt2.47)]
- **SymMap 2.0** — Maps among herbs, TCM symptoms, modern symptoms, ingredients, targets, and diseases. The site is now version 2.0, updated with the 2020 Chinese Pharmacopoeia, and the relationship tables can be downloaded. The footer is dated 2022. [[Website](http://www.symmap.org/)] [[Data](http://www.symmap.org/download/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323958/)]
- **LTM-TCM** (site down) — Links 14 TCM databases with clinical records and classical books across symptoms, prescriptions, plants, ingredients, and targets: 1,928 symptoms, 48,126 prescriptions, 9,122 plants, 34,967 ingredients, and 13,109 targets. cloud.tasly.com does not resolve on this check. [[Original site](http://cloud.tasly.com/#/tcm/home)] [[DOI](https://doi.org/10.1016/j.phrs.2022.106185)]
- **HIT 2.0** (site issue) — Manually curated herbal-ingredient–target activity pairs (~1,237 ingredients / 2,208 targets, 2000–2020 literature). Portal opens; the analysis backend port is currently down (marked site issue). [[Website](http://hit2.badd-cao.net/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728248/)] [[DOI](https://doi.org/10.1093/nar/gkab1011)]
- **SuperTCM** (site down) — Charité resource of 6,516 TCM drugs, 5,372 botanical species, 55,772 active ingredients, 543 targets, 254 KEGG pathways, and 8,634 diseases. tcm.charite.de does not resolve on this check. [[Original site](http://tcm.charite.de/supertcm)] [[Paper](https://europepmc.org/article/MED/34656056)] [[DOI](https://doi.org/10.1016/j.biopha.2021.112315)]
- **TCMIO** — Immuno-oncology TCM database of prescriptions, herbs, ingredients, targets, and pathways, with downloads and a REST API. [[Website](http://tcmio.xielab.net/)] [[Data](http://tcmio.xielab.net/download)] [[DOI](https://doi.org/10.3389/fphar.2020.00439)]
- **Sowa Rigpa Materia Medica Dataset** — Open Data in Brief table of Latin identifications for commonly used Sowa Rigpa materia medica. The paper says about 700 commonly used items were selected from the Four Medical Treatises and Gawé Dorjé’s classification, with Tibetan script, Wylie transliteration, and Latin names; the supplement is published with the article. The authors are at the School of Tibetan Medicine, Gansu University of Chinese Medicine, the University of Wisconsin-Madison, and the College of Pharmacy at Qinghai Nationalities University. The data-source location is the ethnic-medicine center at Chengdu University of Traditional Chinese Medicine. [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC7689029/)] [[DOI](https://doi.org/10.1016/j.dib.2020.106498)]
- **傣药基原植物数据库** (site issue) — Dai medicinal-plant source database on the Chinese Union of Botanical Gardens platform, from Xishuangbanna Tropical Botanical Garden, CAS. The home page is copyrighted 2018 and describes Dai medicine’s four towers, five aggregates, and antidote theory. The species-list URL returns a redirect notice, and no anonymously browsable species catalogue was confirmed. [[Website](https://espc.cubg.cn/daim/index/index.html)]
- **YaTCM** (site down) — 1,813 prescriptions, 6,220 herbs, and 47,696 natural products, with target and pathway tools. The Nankai site returned 403 on this check. [[Original site](http://cadd.pharmacy.nankai.edu.cn/yatcm/home)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC6280608/)] [[DOI](https://doi.org/10.1016/j.csbj.2018.11.002)]
- **TCMID 2.0** (site down) — East China Normal University's database of formulas, herbs, ingredients, and targets. The data and the paper are on Zenodo and in Nucleic Acids Research. It is a different database from NUS TCM-ID. megabionet.org/tcmid timed out on this check. [[Original site](http://www.megabionet.org/tcmid/)] [[Data](https://zenodo.org/records/8066910)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5753259/)] [[DOI](https://doi.org/10.1093/nar/gkx1028)]
- **TCMAnalyzer** (site down) — Sun Yat-sen University toolkit for scaffold search of bioactive ingredients and for networks of molecules, targets, pathways, and diseases. rcdd.org.cn timed out on this check. [[Original site](http://www.rcdd.org.cn/tcmanalyzer)] [[Paper](https://pubmed.ncbi.nlm.nih.gov/29420025/)] [[DOI](https://doi.org/10.1021/acs.jcim.7b00549)]
- **中药方剂图像数据库** — Formula image library from the School of Chinese Medicine, Hong Kong Baptist University, openly browsing composition, actions, indications, and images. The browse page shows about 182 formulas, and the public counter starts in November 2017. It is an online reference, not a bulk formula-table download. [[Website](https://library.hkbu.edu.hk/electronic/libdbs/cmfid/)]
- **TCM-Mesh** (site down) — Network-pharmacology resource with 6,235 herbs, 383,840 compounds, 14,298 genes, 6,204 diseases, 163,221 side-effect records, and 71 toxicity records. The old site returned 403 on this check. [[Original site](http://mesh.tcm.microbioinformatics.org/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5460194/)] [[DOI](https://doi.org/10.1038/s41598-017-03039-7)]
- **TM-MC** — KIOM's literature-derived database of Northeast Asian medicinal materials and compounds. The 2015 release covers about 536 materials, and the 2024 version 2.0 expands to about 34,000 compounds. The old address says the data and services have moved to tm-mc.kr. [[Website](https://tm-mc.kr)] [[Original site](http://informatics.kiom.re.kr/compound/)] [[DOI](https://doi.org/10.1186/s12906-015-0758-5)] [[2.0 paper](https://doi.org/10.1186/s12906-023-04331-y)]
- **CEMTDD** — An herbal–compound–target–disease resource centered on Uygur and Kazakh medicines. The paper reports about 621 herbs. [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627337/)] [[DOI](https://doi.org/10.18632/oncotarget.3789)]
- **TCMSP** — A pharmacology site for herb ingredients, targets, diseases, and ADME numbers. The site now keeps version 2.3 beside the newer 9.0.1, and the relationship tables can be downloaded. [[Website](https://www.tcmsp-e.com/tcmsp.php)] [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- **中药材图像数据库** — Chinese medicinal-material image library from the School of Chinese Medicine, Hong Kong Baptist University. The library page states more than 420 commonly used crude drugs, with source, origin, morphology, properties, indications, and high-resolution images, searchable by Chinese, Latin, and English names. It has been online since 2013 and is openly browsable, not a bulk download. [[Website](https://library.hkbu.edu.hk/electronic/libdbs/mmd/)]
- **CVDHD** (site down) — 3D structures of 35,230 natural products from cardiovascular herbs, docked to 2,395 target proteins, with related diseases, pathways, and clinical biomarkers. The original Peking University site timed out on this check. [[Original site](http://pkuxxj.pku.edu.cn/CVDHD)] [[DOI](https://doi.org/10.1186/1758-2946-5-51)]
- **TCM Database@Taiwan** (site down) — More than 20,000 pure compounds isolated from 453 TCM ingredients, each in 2D and 3D, for virtual screening. tcm.cmu.edu.tw timed out on this check. [[Original site](http://tcm.cmu.edu.tw/)] [[Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0015939)] [[DOI](https://doi.org/10.1371/journal.pone.0015939)]
- **TCMGeneDIT** (site down) — Text-mined links among TCM, genes, diseases, effects, and ingredients, joined to pathways and protein interactions. tcm.lifescience.ntu.edu.tw does not resolve on this check. [[Original site](http://tcm.lifescience.ntu.edu.tw/)] [[Paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2584015/)] [[DOI](https://doi.org/10.1186/1472-6882-8-58)]
- **TCM-ID** — NUS BIDD formula–herb–ingredient–target resource covering pharmacopoeia, classical, and CFDA-approved prescriptions; not the same database as TCMID 2.0. [[Website](https://www.bidd.group/TCMID/)]

</details>

<details>
<summary>Clinical structured / prescription sets (12)</summary>

- **赵汉青门诊处方（2025）** — De-identified 2025 internal-medicine outpatient prescriptions from Zhao Hanqing: 122 patients, 335 prescriptions, and 5,951 herb rows with gram doses. 75 are initial visits and 260 are follow-ups. Routes: 315 oral decoctions, 8 oral dissolved, 8 external washes, and 4 external uses. Dosing is twice daily in 333 prescriptions and three times daily in 2. Herb-name rows containing processing marks, which can overlap: stir-fried 412, honey-fried 341, bran 289, vinegar 164, ginger 154, wine 89, calcined 67, prepared 63, and processed Pinellia (Fa Ban Xia) 99. CC BY 4.0. The repository describes the clinic as Beijing Heniantang Hospital. [[Dataset](https://doi.org/10.5281/zenodo.21947836)] [[Code](https://github.com/zhhqtt/zhao-hanqing-tcm-dataset-2025)]
- **胆石症中医证候代谢组** — Serum and urine metabolomics for two TCM syndromes in cholelithiasis: liver qi stagnation and liver-gallbladder damp-heat. [[Paper](https://doi.org/10.1038/s41597-025-06537-w)]
- **汉派中医骨伤诊疗数据集** — Wuhan Hospital of TCM’s licensed Hanpai orthopaedics data product reportedly covers 168,000 structured records, 3,600 formulas and reasoning chains. A marketplace transaction is reported; an anonymous bulk download was not found. [[News](https://www.cntcm.com.cn/content/202610/16/c505880.html)]
- **广安门医院慢性胃炎数据集** — A disease-specific TCM dataset registered in 2026 for research and model adaptation. Access is described through internal use, collaborative research and licensed products. No dataset-specific sample count or public download is provided; hospital-wide totals are not its size. [[News](https://www.cntcm.com.cn/content/202609/24/c505607.html)]
- **古今医案云平台** — Case search, structuring, and mining platform of the Institute of Information on Traditional Chinese Medicine, China Academy of Chinese Medical Sciences. An institute news item on 2026-09-20 states that the current resource holds more than 1.1 million structured historical and modern cases, plus 19.63 million analysis records, with about 53,000 registered users. Registration or institutional login is required, and no public bulk download was found. Some campus trial notes still say about 500,000 cases. [[Website](https://www.yiankb.com/)]
- **TCMCPD** — Structured case-derived tables: 4,895 patients, 12,900 visits, 703 herbs, 11,879 visit–syndrome links, and 63,192 visit–herb rows. Dose units are mostly grams (61,386), plus 1,067 qian, 364 pieces, 240 tablets, 69 liang, 64 fen, and 2 millilitres. Rows also link symptoms, ingredients, and targets, with Neo4j files. Full copyrighted case texts are not redistributed. The describing manuscript is a Research Square preprint. [[Dataset](https://doi.org/10.5281/zenodo.20929034)]
- **TCM4NSCLC** — 3,790 non-small-cell lung cancer case records from one senior TCM physician, including repeat visits, for syndrome differentiation, prescription, and real-world research. [[Paper](https://doi.org/10.1038/s41597-026-07912-x)]
- **TCM-Andrology-EMR** — The card reports 67,073 visits, 25,103 patients and 26,923 complete examples in patient-grouped JSONL splits. Doses are absent and tongue/pulse fields are sparse. The author states no IRB review or patient consent; this is a resource index entry with unresolved provenance and reuse grounds. [[Dataset](https://huggingface.co/datasets/johnson/TCM-Andrology-EMR)]
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
<summary>East Asian traditional medicine (21)</summary>

- **东亚医学协会针灸经络图版库** — Previously existing resource; original launch year unconfirmed. Historical meridian illustrations from five works are arranged side by side by meridian. Useful for edition comparison and image/text source discovery; this is not an annotated VQA dataset, and bulk-download/training rights are unverified. [[Website](https://aeam.jp/keiraku/)]
- **东亚医学协会医学古典文本** — Previously existing resource; original launch year unconfirmed. The association’s official index links seven medical classics. A checked Shanghan Lun PDF has 79 extractable-text pages and identifies its Zhao Kaimei edition basis. Edition and reuse terms must be checked per text. [[Website](https://aeam.jp/koten/)] [[Link](https://aeam.jp/wp/wp-content/uploads/2024/03/shanghanlun.pdf)]
- **VTM-TDA Benchmark** — A FAIR computational benchmark of Vietnamese traditional medicine digitized from Do Tat Loi's pharmacopoeia, with 724 harmonized botanical entities and 1,635 historical prescriptions. [[Dataset](https://zenodo.org/records/23075405)]
- **TreeProbe** — Tibetan-medicine benchmark for measuring cultural bias in large language models. [[Paper](https://arxiv.org/abs/2608.00640)]
- **Korean Medicine Embedding Dataset** — Query–positive–negatives (~113k pairs) built from Korean-medicine terms and an ontology, for embedding fine-tunes such as BGE-M3. [[Dataset](https://huggingface.co/datasets/cnupo23/korean-medicine-embedding-dataset)]
- **KampoBench** — Physician-reviewed Kampo consultation benchmark with 74 scenarios and 310 dialogue-level criteria. [[Paper](https://doi.org/10.64898/2026.10.07.26365005)]
- **HerbPairIAM** — Data and model artifacts for attributing adverse-reaction signals to components of multi-component Kampo medicines, with a zip archive and README on Zenodo. [[Dataset](https://zenodo.org/records/19326537)]
- **健康成人韩医诊察数据集** — A traditional Korean medicine examination protocol, built from the literature and three rounds of expert review, with healthy-adult examination data collected over four years. [[Paper](https://doi.org/10.3390/healthcare12090918)]
- **VietMedKG** — Knowledge graph and benchmark for traditional Vietnamese medicine. [[Dataset](https://github.com/HySonLab/VietMedKG)]
- **Polyglot Asian Medicine Knowledge Graph** — A 2023 public knowledge-graph portal of Asian traditional and herbal medicines, currently focused on Chinese materia medica and expanding to Malay and Southeast Asian drugs, linking names, scientific names, plant parts, textual sources, and geography. [[Data](https://kgraph.sg/polyglot/)] [[Paper](https://doi.org/10.1007/978-981-99-8088-8_1)]
- **京都大学富士川文库数字古医书** — Kyoto University’s digitized historical medical collection includes Chinese/Japanese medical books and medical-history materials. Its digitization was completed in April 2018, with an IIIF collaboration with Keio. Useful for edition/image/OCR research; holdings totals are not cleaned TCM text counts. [[Website](https://rmda.kulib.kyoto-u.ac.jp/collection/fujikawa)]
- **KampoDB** — Kampo mechanism database maintained by the Institute of Natural Medicine, University of Toyama. It links formulas, crude drugs, natural compounds, and target proteins, including known interactions and docking predictions. The about page currently lists 298 Kampo formulas, 180 crude drugs, 3,002 natural compounds, 62,906 proteins or genes, and 3,063,505 docking results. The 2018 Scientific Reports paper is the citation; the site news records a renewal on 15 July 2021. [[Website](https://wakanmoview.inm.u-toyama.ac.jp/kampo/)] [[About](https://wakanmoview.inm.u-toyama.ac.jp/kampo/about/)] [[DOI](https://doi.org/10.1038/s41598-018-29516-1)]
- **韩医药素材银行药材目录 (KMMB)** — Korean Medicine Material Bank at the National Institute for Korean Medicine Development. On 1 January 2016 it was formed by merging the natural-substance bank and the herbal biomaterial bank. The herb page lists 691 items, with name, synonym, scientific name, botanical source, and reacting enzymes. [[Herbs](https://kminfra.nikom.or.kr/kmmb/module/herbs/index.do?menu_idx=11)]
- **KMCRIC** — Data portal of the Korean Medicine Convergence Research Information Center at Kyung Hee University. The data-center page lists an evidence-based Korean-medicine literature set of systematic reviews, RCTs, and mechanism studies published since 2010; an herb-interaction set based on Natural Standard; acupoint videos made from the 2008 WHO Western Pacific standard locations; and a crude-drug update built with the Kyung Hee and Chungbuk pharmacy faculties. The director’s biography says the directorship began in 2013. [[Data](https://www.kmcric.com/database/data_main)] [[About](https://www.kmcric.com/about/head_of_centre)]
- **药用植物综合信息数据库 (MPDB)** — Comprehensive medicinal-plant database of the NIBIOHN Research Center for Medicinal Plant Resources. The home page describes medicinal plants, crude drugs, constituents and genes, cultivation, and internal morphology, plus measured data for representative crude drugs in Japanese circulation. The footer copyright is 2012–2025, funded by a MHLW research grant. Separate Kampo-formula and Japanese Pharmacopoeia crude-drug lists are online. [[Website](https://mpdb.nibn.go.jp/)] [[Formulas](https://mpdb.nibn.go.jp/mpdb-bin/list_data.cgi?category=syohou&lang=)] [[Crude drugs](https://mpdb.nibn.go.jp/mpdb-bin/list_data.cgi?category=jplist&lang=ja)]
- **TradMPD** (site down) — Traditional Medical and Pharmaceutical Database at the University of Toyama Institute of Natural Medicine. A MEXT regional innovation cluster grant supported it in 2008–2012. It covers crude-drug identity, properties, Kampo composition and indications, and more than 10,000 Kampo papers. The Wakanyaku Library holds nearly 80 compounds plus chemical and bioassay data for hot-water extracts of 80 crude drugs and 80 Kampo extracts, with bioassay downloads from 2024. The database site returned 503 on this check; the institute portal still lists the address. [[Website](https://dentomed.toyama-wakan.net/en/)] [[About](https://dentomed.toyama-wakan.net/index_en)]
- **KNApSAcK KAMPO** — NAIST Kampo public database (~1,581 formulas, 278 crude drugs), downloadable from the NBDC life-science archive. [[Dataset](https://dbarchive.biosciencedbc.jp/data/knapsack-kampo/)] [[DOI](https://doi.org/10.1093/pcp/pcr165)]
- **OASIS (KIOM)** — KIOM traditional-medicine literature portal for Korean-medicine papers and herbal resources. The Korean-medicine paper search went online in June 2007 and was rebuilt as a traditional-medicine portal in July 2009. [[Website](https://oasis.kiom.re.kr/)]
- **KTKP Traditional Medicine** — Korean-medicine slice of the Korean Traditional Knowledge Portal, run for the Ministry of Intellectual Property. The English introduction says the database was compiled from traditional Korean medicine literature in 2005–2007 and opened for search in December 2007. The same page currently counts 5,500 herbs, 7,103 prescriptions, and 12,500 diseases, linked to effects, indications, formulas, and patent classes. [[About](https://koreantk.com/ktkp2014/about/introduction.page)] [[Herbs](https://koreantk.com/ktkp2014/medicine/list-by-act-part.page)] [[Formulas](https://koreantk.com/ktkp2014/prescription/list-by-index.page)] [[Patterns](https://koreantk.com/ktkp2014/disease/list-by-index.page)]
- **EKAT** — Evidence Reports of Kampo Treatment, a structured-abstract database from the Japan Society for Oriental Medicine EBM committee. The site says it has been free and updated since 2007. It covers RCTs and meta-analyses of Kampo products still on the market, limited to reports since 1986 that used the same quality as marketed products; decoctions are excluded because product quality is unknown. Japanese and English editions are provided, and the Association of Korean Medicine has a Korean translation. [[Website](https://www.jsom.or.jp/ebm/ekat/)]
- **ETHMEDmmm** (site down) — Ethnomedicine specimen database of the Museum of Materia Medica at the University of Toyama. The home-page table lists 461 kinds and 8,942 Japanese–Chinese crude-drug specimens, opened in Japanese in April 2000. The same site also has an English crude-drug list and separate Unani, Thai, Ayurvedic, and Indonesian collections. The latest note is a version-7 rebuild on 30 March 2018. The site returned 503 on this check; the institute portal still lists the address. [[Website](https://ethmed.toyama-wakan.net/)]

</details>

<details>
<summary>Books / pretraining corpora (17)</summary>

- **数字中医校书郎（CMETA）** — Previously existing resource; original launch year unconfirmed. A collaborative TCM textual-editing archive with multiple Shanghan Lun versions, Jingui and case records, image comparison and Markdown/TXT export controls. Google login is required; export was not tested behind login. Original editorial work is CC BY 4.0; external images have separate terms. [[Website](https://cmeta.lctseng.csie.org/)]
- **中国哲学书电子化计划·黄帝内经** — Previously existing resource; original launch year unconfirmed. Chapter-organized Huangdi Neijing text with related edition facsimiles. English translations are labeled AI/user-produced and should not be treated as expert-validated translation gold data. Bulk export licensing was not verified. [[Website](https://ctext.org/huangdi-neijing)]
- **中华古籍智慧化服务平台** — Previously existing resource; original launch year unconfirmed. The National Library of China’s general classics portal offers full-text, edition and knowledge search plus OCR, punctuation and comparison tools. Medical works are a subset; whole-platform totals are not TCM corpus counts. Bulk text export is unverified. [[Website](https://guji.nlc.cn/)]
- **中医药智慧数字图书馆** — Previously existing resource; original launch year unconfirmed. CACMS’s library portal indexes Republican-era books and journals, reprinted classics, rare-book facsimiles and ethnic-medicine books. The homepage and category links are accessible with registration/login available; full-text entitlements and bulk downloads are unverified. [[Website](https://tsg.cintcm.cn/)]
- **上海中医药大学馆藏古籍库** — Previously existing resource; original launch year unconfirmed. SHUTCM’s library describes high-resolution scans of rare medical classics, above 600 DPI. Access explicitly requires the campus network or institutional VPN; this is an institutional edition-image resource rather than a public corpus download. [[About](https://lib.shutcm.edu.cn/Home/dbdetails/0eb195a0-b9ca-4248-ae41-c356a772cd96)]
- **tc_medical_base** — Clause-level corpus of five classical TCM texts totaling 3,569 clauses with sentence-BERT embeddings: Song-edition Shanghan Lun, Guilin Shanghan Zabing Lun, Jingui Yuhan Jing, Jingui Yaolue, and Fu Qingzhu Nüke. [[Dataset](https://huggingface.co/datasets/huckiyang/tc_medical_base)]
- **classical-tcm-canon** — Full-text digitizations of the TCM canon: Neijing, Nanjing, Shanghan Lun, Jingui Yaolue and warm-disease classics. [[Dataset](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)]
- **Tao-Shanghan-Corpus** — A downloadable Shanghan Lun corpus that keeps clauses, commentaries, and textual variants apart. Version 1.0, released 11 August 2026, has 681 clause records, including 398 canonical clauses, 2,958 aligned commentaries, and 616 variants. CC BY 4.0. [[DOI](https://doi.org/10.5281/zenodo.21889089)] [[Data](https://zenodo.org/records/21889089)]
- **TCM Ancient-to-Modern Open Metadata** — Public metadata for a controlled classical-to-modern TCM corpus: 9,610 indexed records, frozen splits, edition provenance and hashes, plus ten independent demonstration pairs. Experimental passages, reference translations and teacher traces are withheld; this is not 9,610 downloadable training pairs. [[Dataset](https://huggingface.co/datasets/xs12345/TCM-Ancient-Modern-Open)] [[Code](https://github.com/xiesi1234/R1-TCM-Translator)]
- **TCM-Pretrain-Data-ShizhenGPT** — ShizhenGPT pretraining corpus. The paper reports 15B+ tokens — Stage 1 text 11.92B including 6.3B TCM, and Stage 2 multimodal data of 3.8B tokens in the main text and 3.84B in the appendix. [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- **ChiMed 2.0** — Upgraded Chinese medical pretraining dataset covering TCM corpora for LLM pretraining. [[Paper](https://arxiv.org/abs/2507.15275)]
- **国医典藏** — Image-and-text library of historical Chinese medical books from the Institute of Information on Traditional Chinese Medicine and its library, CACMS. The current entry is the version-4 site. Public descriptions put the holdings at roughly 2,500 to 3,000 titles from pre-Qin through the late Qing and Republican periods, with basic, advanced, and controlled-vocabulary search and image-text viewing. Access is by campus network or registration, not a public bulk download. [[Website](https://gydc-v4.cintcm.cn/)]
- **Traditional-Chinese-Medicine-Dataset-Pretrain** — High-quality TCM pretraining dataset from non-Internet sources (~1GB; clinical cases, classics, encyclopedia), 99% simplified Chinese. [[Dataset](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)]
- **国家中医药古籍数字图书馆** — Ancient-book and traditional-knowledge portal started in 2022 by the Institute of Information on Traditional Chinese Medicine, CACMS. It has halls for classical texts, Republican-era documents, and bibliographic catalogs, and links out to reading systems including Guoyi Diancang. The portal opens; full text is reached through the sub-libraries and is not a public bulk download. [[Website](http://www.cintcm.com/)]
- **TCM-Ancient-Books** — A corpus of nearly 700 TCM ancient-book texts. [[Dataset](https://github.com/xiaopangxia/TCM-Ancient-Books)]
- **中医笈成** — A TCM classics project begun in 2009 with searchable canonical, diagnostic, materia-medica, formula and case texts, a public GitLab collection and source downloads. Editorial work on public-domain texts is declared CC0; original explanatory pages are CC BY 4.0, with image/page exceptions. [[Website](https://jicheng.tw/tcm/book/)] [[Link](https://jicheng.tw/tcm/download.html)] [[Link](https://jicheng.tw/tcm/copyright.html)]
- **中华医典** — Commercial sales site (Feixiong Technology) for the Zhonghua Yidian electronic collection. The site states 1,156 classical titles and about 450 million characters, a 2000 national electronic-publication nomination, and Qiu Peiran as editorial reviewer and title writer. Edition 6 is a web version used after purchase and registration, not a public download. [[Website](https://www.zhyd1999.com/)]

</details>

<details>
<summary>Benchmarks (33)</summary>

- **TCM-RobustSDT** — TCM-RobustSDT: a robustness benchmark dataset for LLM clinical reasoning in TCM (Figshare). [[Dataset](https://doi.org/10.6084/m9.figshare.33054974)]
- **辨证论治基准数据集** — Scientific Data benchmark for syndrome differentiation and treatment with large language models. [[Paper](https://doi.org/10.1038/s41597-026-07587-4)]
- **病理标注舌象数据集** — Tongue-image dataset with pathological annotations for AI-assisted TCM diagnosis. [[Paper](https://doi.org/10.62762/bish.2026.303296)]
- **病机思维链证候识别数据** — Syndrome-manifestation cases with gold labels and model predictions, built under pathogenesis reasoning chain-of-thought supervision. [[Dataset](https://doi.org/10.57760/sciencedb.35044)]
- **WHO TCM Terminology LLM Evaluation Set** — Evaluation set for using large language models as judges of TCM terminology, containing 376 contrasts from the 2022 WHO International Standard Terminologies on Traditional Chinese Medicine. [[Dataset](https://zenodo.org/records/21852353)]
- **TongueBench** — 2,694 tongue images and 22 labels; compares nine multimodal models, three prompting strategies and repeated-output stability. Image data and an inference/scoring demo are available. [[DOI](https://doi.org/10.3389/frai.2026.1943004)] [[Code](https://github.com/mengyiha/TongueBench-Open)] [[Dataset](https://zenodo.org/records/20701288)]
- **TCMClinicalReason-Bench** — 2,000 multicenter records for reasoning from pathogenesis to prescription. [[Paper](https://arxiv.org/abs/2610.04215)]
- **TCM-DiagCommit** — TCM-SD-derived benchmark with 1,834 source cases, 148 syndrome labels and 23,842 task rows; fixed three-stage evidence disclosure tests syndrome discrimination, evidence use and commit/acquire/defer/abstain decisions. Data and scoring code are available. [[Paper](https://arxiv.org/abs/2610.37243)] [[Code](https://github.com/Ethan-ai637/TCM-DiagCommit)] [[Dataset](https://github.com/Ethan-ai637/TCM-DiagCommit/tree/main/data)]
- **TCM-BEST4SDT** — 600 evaluation items: 300 syndrome-differentiation-and-treatment cases and 100 questions each on TCM knowledge, medical ethics, and content safety; 27 evaluation dimensions. [[Dataset](https://github.com/DYJG-research/TCM-BEST4SDT)] [[Paper](https://arxiv.org/abs/2512.02816)] [[Published](https://doi.org/10.1038/s41597-026-07587-4)]
- **TCM-AQA61 / CME-AQA** — Synchronized first- and third-person videos of acupuncture and Tuina, 61 subjects each. Two experienced TCM physical therapists assessed every subject independently, then reconciled disagreements. Paired with the CME-AQA cross-view assessment framework. [[Paper](https://arxiv.org/abs/2606.28104)] [[DOI](https://doi.org/10.1109/TNSRE.2026.3705649)] [[Code](https://github.com/FrancisXZhang/cme-aqa)] [[Data](https://researchdata.durham.ac.uk/collections/r1jm214p229)]
- **TCM Term Prompt-Language Responses** — 972 model responses for 18 TCM terms across six general-purpose models, three prompt languages (Chinese, English, and Malay), and three runs, with WHO 2007 and 2022 terminology references. [[Dataset](https://zenodo.org/records/22208549)]
- **MTCMB** — Multi-task TCM benchmark with 12 datasets and 7,100 samples covering knowledge, reasoning, formulas, and safety (Scientific Data 2026). [[Dataset](https://github.com/Wayyuanyuan/MTCMB)] [[Paper](https://arxiv.org/abs/2506.01252)] [[Published](https://doi.org/10.1038/s41597-026-07967-w)]
- **LingLanMedBench** — LingLanMedBench (formerly LingLanMiDian): 25,620 expert-verified items across 13 subtasks and five domains. Each subtask has a 400-item Hard subset selected from its full set. [[Dataset](https://github.com/TCMAI-BJTU/LingLan)] [[Paper](https://arxiv.org/abs/2602.01779v2)]
- **TongueProjectTCM Color Classification** — TongueProjectTCM tongue-image set whose card lists images and integer labels, with 807 training and 121 validation examples. [[Dataset](https://huggingface.co/datasets/TongueProjectTCM/color-classification-opensource)]
- **TongueDx** — Public remote-tongue dataset: 5,109 images from 4,650 subjects, eight binary attributes (pale, red tip/side, red spots, ecchymosis, cracks, tooth marks, thick fur, yellow fur), plus age and sex. The repository is downloadable. This is not the later TongueDx2 ablation paper. [[Dataset](https://github.com/tonguedx/tonguedx)] [[Paper](https://arxiv.org/abs/2501.03053)]
- **TongueAtlas-4K** — A 4,000-image clinical tongue benchmark with certified TCM expert labels for 22 appearance categories, released for MIRNet (AAAI 2026, to appear). The Zenodo record is restricted. [[Dataset](https://zenodo.org/records/17557646)]
- **TCMEval-SDT** — TCMEval-SDT: a benchmark of 300 syndrome-diagnosis cases (web, classical texts, hospital records) for evaluating TCM syndrome-differentiation reasoning, with FAIR metadata (Sci. Data 2025). [[DOI](https://doi.org/10.1038/s41597-025-04772-9)] [[Paper](https://www.nature.com/articles/s41597-025-04772-9)] [[Code](https://github.com/zhuyan166/TCMEval)]
- **TCMEval-PA** — 328 multiple-choice items on prescription normative quality and safety auditing. [[Paper](https://doi.org/10.1038/s41597-025-06387-6)] [[Data](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[Code](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)]
- **TCM-Vision-Benchmark** — TCM vision benchmark (herb recognition / inspection, ~7k items). [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Vision-Benchmark)]
- **TCM-Tongue** — 6,719 standardized tongue images with 20-class multi-label pathology annotations and detection baselines. [[Paper](https://arxiv.org/abs/2507.18288)] [[Data](https://doi.org/10.5061/dryad.1c59zw48r)] [[Code](https://github.com/btbuIntelliSense/Intelligent-tongue-diagnosis-detection-dataset)]
- **TCM-Ladder** — Multimodal TCM benchmark with 52,169 question-answer pairs and image, audio, and video data (NeurIPS 2025). [[Dataset](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[Leaderboard](https://tcmladder.com)] [[Paper](https://arxiv.org/abs/2505.24063)] [[Published](https://proceedings.neurips.cc/paper_files/paper/2025/file/cbdd26a4490f5a8dad0d732508714029-Paper-Datasets_and_Benchmarks_Track.pdf)]
- **TCM-Eval** — Dynamic, extensible TCM evaluation platform. [[Paper](https://arxiv.org/abs/2511.07148)] [[Platform](https://tcmeval.bamaidical.com)]
- **TCM-5CEval** — Five-dimension TCM evaluation with 2,260 questions from 30 courses; cyclic option rotations test sensitivity to answer position. [[Paper](https://arxiv.org/abs/2511.13169)]
- **TCM-3CEval** — Three-axis eval: core knowledge, classics, clinical decisions. [[Paper](https://arxiv.org/abs/2503.07041)]
- **SYD_NK 内科证候测试集** — 366 TCM internal-medicine test items. Each item is a syndrome name plus a first-person symptom narrative. The card says the text was cleaned from an internal-medicine textbook and checked by TCM students. Apache-2.0. [[Dataset](https://huggingface.co/datasets/XiaoEnn/Syndrome_Differentiation_NK_test)]
- **MetaAcuPoint** — 900 synthetic RGB hand images from MetaHuman avatars in Unreal Engine, with bone-attached sockets for five hand acupoints used in Korean medicine. [[Paper](https://doi.org/10.3390/healthcare13233093)]
- **Chinese Drug Name Overreliance Set** — Experiment data for the paper on whether LLMs over-rely on names to identify ingredients of Chinese drugs, linked from the dataset card to arXiv:2504.03786. [[Dataset](https://huggingface.co/datasets/med-llm/tcm-llm-overrely-on-names)]
- **AcuSim** — Synthetic dataset for localising cervicocranial acupuncture points, built because expert annotation is costly and limits detector training. [[Paper](https://doi.org/10.1038/s41597-025-04934-9)]
- **ZhongJing-OMNI** — ZhongJing-OMNI multimodal TCM eval (including tongue). [[Dataset](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]
- **TCMBench** — TCMBench: a comprehensive benchmark for evaluating LLMs in traditional Chinese medicine (arXiv 2024). [[Dataset](https://github.com/ywjawmw/TCMBench)] [[Paper](https://arxiv.org/abs/2406.01126)]
- **HWTCMBench** — HWTCMBench TCM capability evaluation set. [[Dataset](https://huggingface.co/datasets/Monor/hwtcm)]
- **CMMLU Traditional Chinese Medicine** — CMMLU Traditional Chinese Medicine test split; the card shows a 185-example load and the file traditional_chinese_medicine.json. [[Dataset](https://huggingface.co/datasets/shuyuej/CMMLU-Traditional-Chinese-Medicine-Benchmark)]
- **TCM-SD** — First large public TCM syndrome-differentiation text benchmark (54,152 real records, 148 syndromes, CC BY-NC-SA 4.0). Full set is in the repo folder TCM_SD_with_knowledge; Tianchi id 139034. [[Paper](https://arxiv.org/abs/2203.10839)] [[Published](https://aclanthology.org/2022.ccl-1.80/)] [[Code](https://github.com/Borororo/ZY-BERT)] [[Data](https://tianchi.aliyun.com/dataset/dataDetail?dataId=139034)]

</details>

<details>
<summary>Exam datasets (8)</summary>

- **TCMQA** — The paper reports 38,279 questions and 101 practitioners. The current HF release documents 33,872 qa rows and 5,250 doctor-annotated rows with 102 practitioners and 15,151 responses. Configurations overlap, so their counts must not be summed as unique questions. Pin the release; CC BY-NC-SA 4.0. [[Paper](https://arxiv.org/abs/2609.33014)] [[Dataset](https://huggingface.co/datasets/TechTCM/TCMQA)]
- **TCMLE** — Chinese TCM practitioner licensing question bank with 7,956 items: 2,700 assistant-practitioner and 5,256 practitioner questions, including past papers and mocks. [[Dataset](https://huggingface.co/datasets/Bolin97/TCMLE)]
- **TCM-Text-Exams** — Recent TCM licensure / graduate-exam text benchmark. [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams)]
- **Taiwan TCM Examination MCQ** — Past national TCM exam questions from Taiwan's Ministry of Examination; the README gives ROC years 96–111 excluding 110, and the repository file is basic theory of traditional Chinese medicine.csv. [[Dataset](https://huggingface.co/datasets/Liavan/Traditional-Chinese-Medicine-Multiple_choice_question)]
- **TCM Humanities MCQ** — Multiple-choice questions on medical humanities, ethics, and physician regulations, curated by the Traditional Chinese Medicine Language Model Team; the card marks the size as under 1,000. [[Dataset](https://huggingface.co/datasets/TCMLM/TCM_Humanities)]
- **Medical-LLMs-Chinese-Exam** — Chinese medical exam evaluation for medical LLMs. [[Dataset](https://github.com/jingnant/Medical-LLMs-Chinese-Exam)]
- **JTB Taiwan TCM Exam Questions** — JTB Tech compilation of Taiwan Ministry of Examination TCM questions for ROC years 90–113, covering TCM internal medicine, basic medicine, and clinical medicine. [[Dataset](https://huggingface.co/datasets/JTBTechnology/tcm_exam_questions)]
- **2023 Pharmacist Licensure Examination TCM Track** — TCM Pharmacy track items from the 2023 Chinese National Pharmacist Licensure Examination; the card says they were collected online and points to FreedomIntelligence/HuatuoGPT-II. [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/2023_Pharmacist_Licensure_Examination-TCM_track)]

</details>

<details>
<summary>Instruction / dialogue datasets (22)</summary>

- **HSQ-TD（健身气功指令微调数据集）** — HSQ-TD: the first instruction-tuning dataset for health Qigong/wellness, with 57,843 instructions distilled from official textbooks and professional literature (ScienceDB). [[Dataset](https://doi.org/10.57760/sciencedb.35843)]
- **neijing-sft-v1.2** — ~2,009 Neijing-related instruction samples for Xinghe, with thinking/output fields. [[Dataset](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2)]
- **TriCM-DF Acupuncture Corpus** — Expert-verified instruction corpus for TCM models, instantiated for acupuncture across consensus, experiential, and perception tables; the repository releases text, not the image or video files. [[Dataset](https://huggingface.co/datasets/Shutcm-TCME/TriCMDF)]
- **TCMNSCLC** — Real-world NSCLC TCM reasoning dataset with fully annotated cases (pattern differentiation / treatment method / decoction / patent medicine). [[Dataset](https://huggingface.co/datasets/zhangxinxin0428/TCMNSCLC)] [[DOI](https://doi.org/10.5281/zenodo.21027568)]
- **TCM Medical Case Commentary Generation** — Generation set for TCM medical-case commentary, with 510 standardized source cases and 2,550 training and test instances compiled from gynecological classics. [[Dataset](https://doi.org/10.57760/sciencedb.j00133.00679)]
- **Gancao-TCM-Instruct** — Public Gancao-TCM-Instruct release with 25,000 cases and 125,000 samples covering disease diagnosis, syndrome diagnosis, treatment selection, base-formula selection, and herb selection. [[Dataset](https://huggingface.co/datasets/GancaoDoctorAI/gancao-tcm-instruct)]
- **Fu_TCM** — The repository contains Fu_bianzheng.json, Fu_text.json, Fu_vision.json and image files (505 files total). It tags Apache-2.0 but lacks provenance, sample counts and annotation documentation; modern atlas names occur in image filenames, so underlying image permissions remain unverified. [[Dataset](https://huggingface.co/datasets/fudanxai/Fu_TCM)]
- **tw-tcm** — minyichen/tw-tcm card lists 8,145 training examples with question, answer, source, and think fields. [[Dataset](https://huggingface.co/datasets/minyichen/tw-tcm)]
- **hwtcm-deepseek-r1-distill-data** — Haiwei AI Team's DeepSeek-distilled TCM reasoning QA set built from web text. The authors state that it was not manually reviewed. [[Dataset](https://huggingface.co/datasets/Monor/hwtcm-deepseek-r1-distill-data)]
- **TCM-Instruction-Tuning-ShizhenGPT** — ShizhenGPT multimodal SFT data (text/vision/speech/ECG etc.; ~311k items total per paper Table 3). [[Dataset](https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT)]
- **TCM Knowledge Q&A** — Science Data Bank set of 6,157 question-answer pairs built from classic Chinese medicine literature. [[Dataset](https://doi.org/10.57760/sciencedb.j00133.00565)]
- **Baize-TCM-Corpus-V3** — ~157k TCM QA items covering theory, herbs, formulas, diagnosis, acupuncture, and clinic. [[Dataset](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3)]
- **中医药知识问答实验数据** — Traditional Chinese medicine question-answering set plus the knowledge graph, prompt-engineering code, and experiment outputs. [[Dataset](https://doi.org/10.57760/sciencedb.j00133.00319)]
- **hwtcm-sft-v1** — Haiwei AI Team's 7,096-example TCM instruction set. Text from websites, forums, and books was converted to QA and scored for expertise, safety, and fluency. [[Dataset](https://huggingface.co/datasets/Monor/hwtcm-sft-v1)]
- **Traditional-Chinese-Medicine-Dataset-SFT** — High-quality TCM supervised fine-tuning dataset. [[Dataset](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT)]
- **TCM_19W_DataSet-SFT (part)** — The card describes a partial non-web TCM instruction-tuning set, released as TCM19W_Part1.json. [[Dataset](https://huggingface.co/datasets/cduoduo/TCM_19W_DataSet-SFT)]
- **TCMChat-dataset-600k** — TCMChat herbal QA and recommendation instruction data (~600k). [[Dataset](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k)]
- **ChP-TCM** — KnowledgeQA and PrescriptionWriting instructions built from Chinese Pharmacopoeia Vol. I. [[Data](https://github.com/QLU-NLP/BianCang/tree/main/ChP-TCM)] [[Paper](https://arxiv.org/abs/2411.11027)]
- **ShenNong_TCM_Dataset** — ShenNong TCM instruction dataset. [[Dataset](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset)]
- **MedChatZH** — MedChatZH TCM consultation dataset. [[Code](https://github.com/tyang816/MedChatZH)] [[Dataset](https://huggingface.co/datasets/tyang816/MedChatZH)]
- **ChatMed_Consult_Dataset** — Chinese online-consultation set of 110,113 pairs. The questions come from consultation sites and the answers were written by GPT-3.5. [[Dataset](https://huggingface.co/datasets/michaelwzhu/ChatMed_Consult_Dataset)]
- **CMtMedQA** — ZhongJing real multi-turn doctor–patient dialogues (~70k). [[Dataset](https://huggingface.co/datasets/Suprit/CMtMedQA)]

</details>

<details>
<summary>Knowledge graphs (24)</summary>

- **本草典开放数据** — Bilingual TCM seed data from the Bencao Dian editorial group, released under CC BY-SA 4.0 as directly downloadable JSON. Version 1, generated on 17 April 2026, lists 365 herb records, 112 formulas, 84 patterns, and 208 acupoints, plus meridians, tongue and pulse entries, and a relation graph. A coverage note on the same page says 335 of about 530 standard materia medica items are included. This is an editorial vocabulary, not a national standard. [[Website](https://bencaodian.org/zh/about/data/)] [[Data](https://bencaodian.org/data/v1/herbs.json)]
- **医宗金鉴知识三元组** — 25,571 knowledge triples extracted from the Golden Mirror of Medicine, covering medicinals, formulas, diseases, acupoints, and theory across 1,105 relation types. [[Dataset](https://doi.org/10.57760/sciencedb.013fv)]
- **TCMEFO** — Formal ontology for traditional Chinese medicine efficacy, providing a hierarchical computable framework over concepts, relations, and herbal-medicine instances. [[Dataset](https://doi.org/10.6084/m9.figshare.32677743)]
- **TCM Disease-Pattern-Symptom-Herb KG v2** — Version 2.0 semantic knowledge graph linking diseases, patterns, symptoms, and herbs, released as node and edge CSV files. [[Dataset](https://zenodo.org/records/18173423)]
- **LingShu** — Symptom-centric contextual KG bridging TCM and biomedicine (~17.33M entities, ~39.47M relations including triples and contextual quadruples), with a portal for visualization, reasoning, and evidence-grounded QA. [[Paper](https://arxiv.org/abs/2608.20402)] [[Website](http://www.tcmkg.com/)]
- **Chinese Herbal Efficacy Relations** — Structured herb–efficacy relations converted from classical TCM efficacy wording for knowledge-graph construction, formula-efficacy prediction, and herb–symptom association. [[Dataset](https://zenodo.org/records/18207409)]
- **TCM-MKG** — Open multidimensional TCM knowledge graph of terminology, herbal pieces, and medicinal properties. The companion paper uses interpretable graph neural networks on 6,080 formulas, with a check on 215 COVID-19 formulas. [[Data](https://zenodo.org/records/15395588)] [[Paper](https://doi.org/10.1016/j.jpha.2025.101342)]
- **OpenTCM-KG** — OpenTCM gynecology classics KG (~48k entities / ~152k relations). [[Code](https://github.com/OpenTCM01/OpenTCM)] [[Paper](https://arxiv.org/abs/2504.20118)]
- **AcuKG** — Knowledge graph of medical acupuncture assembled from guidelines, literature, trials, and ontology mapping. [[Paper](https://doi.org/10.1093/jamia/ocaf179)]
- **五部伤寒书知识图谱** — A knowledge graph drawn from Shanghan Lun, Shanghan Leifang, Shanghan Xuanjie, Shanghan Lun Qianzhu, and Shanghan Jiushi Lun. It has 26,771 nodes and 8,272 relations in CSV files that can be loaded into Neo4j. Released on ScienceDB in 2024. [[DOI](https://doi.org/10.57760/sciencedb.j00133.00432)]
- **中药异构网络结构集** — Heterogeneous biomedical graphs that include herb–target, herb–symptom, herb–herb, and symptom–symptom networks, together with protein–protein interaction networks. [[Paper](https://doi.org/10.1016/j.dib.2024.110962)]
- **DragonTCM** — A TCM knowledge base derived from American Dragon and Penner’s work. The card reports 1,119 conditions, 2,580 formulas, 1,044 herbs, and 28,735 relations. The authors note automatic AI parsing may introduce inaccuracies; license is CC-BY-NC-4.0. [[Data](https://huggingface.co/datasets/f-galkin/DragonTCM)]
- **TCM_KG** — A TCM knowledge graph built with Neo4j community edition. The sample query starts from the symptom node for constipation and returns its neighbors. [[Dataset](https://github.com/ywjawmw/TCM_KG)]
- **SoFDA** (site issue) — Syndrome-ontology platform built by the Institute of Chinese Materia Medica, CACMS, and collaborators. The iMeta 2023 paper describes 319 curated syndromes, 8,045 diseases, and 1,359 formulas, linked to genes, diseases, and formulas. The paper page checks out; the front page currently shows no readable syndrome content. It shares the tcmip.cn host with ETCM but is a separate syndrome system. No anonymous full-database mirror was found. [[Website](http://www.tcmip.cn/Syndrome/front/)] [[Paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10989962/)]
- **GB/T 16751.3-2023** — Current national standard Clinic terminology of traditional Chinese medical diagnosis and treatment — Part 3: Therapeutic methods, issued and effective on 17 March 2023. The official full-text disclosure system offers online preview and download. This is the therapeutic-method standard page, not a separate vocabulary dump. [[Website](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E8BBBAB76E1AF1498C5DA5DFBB2194EC)]
- **GB/T 16751.1-2023** — Current national standard Clinic terminology of traditional Chinese medical diagnosis and treatment — Part 1: Diseases, issued and effective on 17 March 2023, under the National Administration of Traditional Chinese Medicine. The official full-text disclosure system offers online preview and download. Syndrome and therapeutic-method parts have their own full-text pages. [[Website](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=7377FB06FF43DC321BB6A4BF7DAA7F39)]
- **TCM-QG** — Question-generation data from TCM texts: 3,500 documents, with one to four human-written question-answer pairs each. The license is CC BY-NC 2.0. [[Data](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86895)] [[Resources](http://openkg.cn/dataset/tcm-qg)]
- **TCM-NER** — Named-entity data from Chinese medicine package inserts, for a medication knowledge graph. The license is CC BY-NC 2.0. [[Data](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86819)] [[Resources](http://openkg.cn/dataset/tcm-ner)]
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
