# Datasets

数据集按用途分栏，与 README [数据集](../README.md#数据集) 同源。评测基准的任务对照见 [[Benchmarks]]。官网挂了的标「官网已挂」，门户在但核心功能不通的标「服务异常」。

## 公开资料整理

- **awesome_Chinese_medical_NLP** — 中文医学 NLP 公开资源整理：术语集、语料库、词向量、预训练模型、知识图谱、NER、QA 等（含 CBLUE 挑战榜） [[资料](https://github.com/GanjinZero/awesome_Chinese_medical_NLP)]
- **中成药公开数据集（RAG-CPMF）** — RAG-CPMF配套的持续更新大规模中成药公开数据 [[数据](https://gitee.com/tcmdoc/cpm)] [[论文](https://doi.org/10.1016/j.phrs.2025.107883)]
- **内蒙古自治区民族药目录** — 内蒙古自治区医疗保障局公开的民族药目录PDF（蒙医成方为主）。文件名为2023年12月25日的政府公开稿，正文标题为内蒙古自治区民族药目录，备注写明目录内民族药按乙类管理。这是医保收载目录，不是蒙药研究型成分库；2026年发布的蒙医药知识库平台未见可打开的网址。 [[目录](https://ylbzj.nmg.gov.cn/zwgk/zfxxgk/fdzdgknr/bmwj/202312/P020231225623619008689.pdf)]

## 中药组方 / 提取物

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
- **LTM-TCM 中西医分子表型链接库**（官网已挂） — 整合十四个权威库与临床/古籍记录的症状–方剂–植物–成分–靶点平台（约4.8万方）；官网cloud.tasly.com域名已无法解析，核验走论文DOI [[原网站](http://cloud.tasly.com/#/tcm/home)] [[DOI](https://doi.org/10.1016/j.phrs.2022.106185)]
- **HIT 2.0 草药成分靶点库**（服务异常） — 人工审核的草药成分–靶点活性对（约1237成分/2208靶点），覆盖2000–2020文献；门户可打开，分析后端端口当前不通 [[网站](http://hit2.badd-cao.net/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC8728248/)] [[DOI](https://doi.org/10.1093/nar/gkab1011)]
- **SuperTCM 中药生物文化数据库**（官网已挂） — Charité团队整合药典与多源数据的中药–物种–成分–靶点–通路–疾病库（约6516味药）；官网tcm.charite.de已无法解析 [[原网站](http://tcm.charite.de/supertcm)] [[论文](https://europepmc.org/article/MED/34656056)] [[DOI](https://doi.org/10.1016/j.biopha.2021.112315)]
- **TCMIO 中医药免疫肿瘤学数据库** — 面向免疫肿瘤的中药/方剂–成分–靶点–通路库，提供浏览、下载与REST API [[网站](http://tcmio.xielab.net/)] [[数据](http://tcmio.xielab.net/download)] [[DOI](https://doi.org/10.3389/fphar.2020.00439)]
- **Sowa Rigpa Materia Medica Dataset** — Data in Brief 公开的藏医（Sowa Rigpa）常用本草拉丁学名数据集。论文写明从《四部医典》等经典和嘎务多吉本草分类中选取约700种常用药物，给出藏文、Wylie转写和拉丁学名，补充材料随文发布。作者单位包括甘肃中医药大学藏医学院、青海民族大学药学院和成都中医药大学民族医药学术传承创新研究中心。 [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC7689029/)] [[DOI](https://doi.org/10.1016/j.dib.2020.106498)]
- **SymMap 2.0 症状映射中医药数据库** — 草药–中医症状–西医症状–成分–靶点–疾病整合库，2.0按新版药典扩草药/证候并开放关系表下载 [[网站](http://www.symmap.org/)] [[数据](http://www.symmap.org/download/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6323958/)]
- **傣药基原植物数据库**（服务异常） — 中国科学院西双版纳热带植物园在植物园联盟平台上的傣药基原植物库（傣医）。首页版权为2018年，简介写明傣医四塔、五蕴与解药理论。物种列表地址返回跳转提示，匿名状态下未见可浏览的物种清单。 [[网站](https://espc.cubg.cn/daim/index/index.html)]
- **YaTCM 中药方剂–成分–靶点库**（官网已挂） — 约1813首方、6220味药、4.7万天然产物及靶点/通路分析工具；南开官网当前403，核验走开放论文 [[原网站](http://cadd.pharmacy.nankai.edu.cn/yatcm/home)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC6280608/)] [[DOI](https://doi.org/10.1016/j.csbj.2018.11.002)]
- **TCMID 2.0 中医药整合数据库**（官网已挂） — 上海团队的方剂–草药–成分–靶点整合库（与NUS的TCM-ID不是同一库）；官网megabionet已不可达，公开核验走Zenodo摘录与NAR论文 [[原网站](http://www.megabionet.org/tcmid/)] [[数据](https://zenodo.org/records/8066910)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5753259/)] [[DOI](https://doi.org/10.1093/nar/gkx1028)]
- **TCMAnalyzer 中药化学信息学分析平台**（官网已挂） — 中山大学RCDD的方剂/药材/成分网络分析与骨架检索服务（约1493方、618味药）；官网rcdd.org.cn当前超时 [[原网站](http://www.rcdd.org.cn/tcmanalyzer)] [[论文](https://pubmed.ncbi.nlm.nih.gov/29425456/)] [[DOI](https://doi.org/10.1021/acs.jcim.7b00549)]
- **香港浸会大学中药方剂图像数据库** — 香港浸会大学中医药学院的方剂图像库，公开浏览方剂组成、功用、主治和图像。浏览页显示约182首，访问计数自2017年11月起。在线查阅，不是方剂表批量下载。 [[网站](https://library.hkbu.edu.hk/electronic/libdbs/cmfid/)]
- **TCM-Mesh 中药网络药理学分析库**（官网已挂） — 草药–化合物–基因–疾病网络与毒副作用记录（约6235味药）；官网当前403，核验走开放论文 [[原网站](http://mesh.tcm.microbioinformatics.org/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC5460194/)] [[DOI](https://doi.org/10.1038/s41598-017-03039-7)]
- **TM-MC 东北亚传统药物成分库**（官网已挂） — 韩国韩医学研究院从文献抽取的东北亚药材–化合物库；2015初版约536种药材，2024的2.0扩到约3.4万化合物；官网当前超时 [[原网站](http://informatics.kiom.re.kr/compound/)] [[DOI](https://doi.org/10.1186/s12906-015-0758-5)] [[2.0论文](https://doi.org/10.1186/s12906-023-04331-y)]
- **CEMTDD 中国少数民族传统药物数据库**（官网已挂） — 以新疆维吾尔/哈萨克等民族药为主的草药–化合物–靶点–疾病库（约621草药）；原域名cemtdd.com已改作他用，核验走PMC论文 [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC4627337/)] [[DOI](https://doi.org/10.18632/oncotarget.3789)]
- **TCMSP 中药系统药理学数据库** — 草药–成分–靶点–疾病网络与ADME参数平台，现行公开站为TCMSP 2.3，提供草药/分子/靶点关系表下载 [[网站](https://www.tcmsp-e.com/tcmsp.php)] [[DOI](https://doi.org/10.1186/1758-2946-6-13)]
- **香港浸会大学中药材图像数据库** — 香港浸会大学中医药学院的中药材图像库。图书馆页面写明收录常用中药材420余种，包括来源、产地、性状、性味功效和高清图像，可按中文名、拉丁名和英文名检索。2013年上线，可公开在线浏览，不是批量下载包。 [[网站](https://library.hkbu.edu.hk/electronic/libdbs/mmd/)]
- **CVDHD 心血管病本草数据库**（官网已挂） — 面向心血管病的本草化合物三维结构、靶点与通路库，用于虚拟筛选与网络药理；原北大站点当前超时 [[原网站](http://pkuxxj.pku.edu.cn/CVDHD)] [[DOI](https://doi.org/10.1186/1758-2946-5-51)]
- **TCM Database@Taiwan 中药三维结构库**（官网已挂） — 453味药材中约2万个分离化合物的2D/3D结构库，面向虚拟筛选；原站tcm.cmu.edu.tw已不可达，核验走PLOS论文页 [[原网站](http://tcm.cmu.edu.tw/)] [[论文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0015939)] [[DOI](https://doi.org/10.1371/journal.pone.0015939)]
- **TCMGeneDIT 中药–基因–疾病文本挖掘库**（官网已挂） — 从文献挖掘中药、基因、疾病、功效与成分关联，并接入通路与PPI；官网tcm.lifescience.ntu.edu.tw已无法解析 [[原网站](http://tcm.lifescience.ntu.edu.tw/)] [[论文](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2582235/)] [[DOI](https://doi.org/10.1186/1472-6882-8-58)]
- **TCM-ID 中医药信息数据库（NUS BIDD）** — 新加坡BIDD维护的方剂–药材–成分–靶点库，含药典/经典方与CFDA批准方；与TCMID 2.0不是同一资源 [[网站](https://www.bidd.group/TCMID/)]

## 临床结构化 / 处方

- **古今医案云平台** — 中国中医科学院中医药信息研究所的医案检索、结构化与挖掘平台。该所2026年9月20日新闻写明，现行资源已形成110余万条高质量结构化古今医案，另有1963万条科研分析数据，注册用户约5.3万人。需注册或机构登录，未见公开批量下载。部分院校试用页仍写约50万条，与这一口径不同。 [[网站](https://www.yiankb.com/)]
- **TCM-Lung 肺系病辨证处方编码集** — 河南中医药大学一附院肺系病案处理后 14948 条，仓库公开 4484 条编码（症状/证候/治法/处方 ID）；全名需邮件申请。与 TCMNSCLC 不是同一份数据 [[代码](https://github.com/2020MEAI/PresRecST)] [[论文](https://doi.org/10.1093/jamia/ocae066)]
- **TCM-PD / PTM 方剂–症状推荐集** — Yao 等 TKDE 2018 处方主题模型配套数据：原始 98334 首、预处理 33765 首（症状–中药 ID）；CKCEST 版权、仅研究使用。PresRecST 的 prescript_1195.csv 即此集复现表 [[代码](https://github.com/yao8839836/PTM)] [[DOI](https://doi.org/10.1109/TKDE.2017.2787158)]

## 通用中文医疗

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

## 东亚传统医学

- **韩医领域嵌入对比学习数据** — 从韩医术语与本体构造的query–positive–negatives（约11.3万对），用于BGE-M3等检索微调 [[数据集](https://huggingface.co/datasets/cnupo23/korean-medicine-embedding-dataset)]
- **KampoDB** — 富山大学和汉医药学综合研究所维护的汉方作用机制库，整合处方、生药、天然化合物与靶蛋白，含已知相互作用和对接预测。关于页当前统计为汉方298首、生药180种、天然化合物3002个、蛋白或基因62906个、对接结果3063505条。2018年 Scientific Reports 论文为首篇描述；站点新闻写明2021年7月15日改版。 [[网站](https://wakanmoview.inm.u-toyama.ac.jp/kampo/)] [[关于](https://wakanmoview.inm.u-toyama.ac.jp/kampo/about/)] [[DOI](https://doi.org/10.1038/s41598-018-29516-1)]
- **韩医药素材银行药材目录 (KMMB)** — 韩国韩医药振兴院韩医药素材银行的在库药材检索。打开的药材页写明检索结果共691条，字段有药材名、异名、学名、基原植物和反应酶。振兴院事业文件记载2016年1月1日由天然物物质银行与韩方生物素材银行合并为本事业。 [[药材目录](https://kminfra.nikom.or.kr/kmmb/module/herbs/index.do?menu_idx=11)]
- **KMCRIC** — 庆熙大学韩医药融合研究信息中心的数据门户。数据中心页列出循证韩医文献库（收录2010年起的系统评价、随机对照试验和机制研究）、基于 Natural Standard 的韩药相互作用库、依据2008年WHO西太区标准穴位制作的取穴视频，以及庆熙大学与忠北大学药学院合作的生药更新库。中心长介绍写明2013年起任该中心所长。 [[数据中心](https://www.kmcric.com/database/data_main)] [[中心介绍](https://www.kmcric.com/about/head_of_centre)]
- **药用植物综合信息数据库 (MPDB)** — 医薬基盤·健康·营养研究所药用植物资源研究中心的汉方与生药综合图鉴。首页写明收录药用植物、生药、成分与基因、栽培和内部形态，并对国内流通的模型生药做了实测；页脚版权为2012–2025，资助来自厚生劳动科学研究费。另有可打开的汉方处方列表和日本药局方收载生药列表。 [[网站](https://mpdb.nibn.go.jp/)] [[汉方列表](https://mpdb.nibn.go.jp/mpdb-bin/list_data.cgi?category=syohou&lang=)] [[药局方生药](https://mpdb.nibn.go.jp/mpdb-bin/list_data.cgi?category=jplist&lang=ja)]
- **TradMPD** — 富山大学和汉医药学综合研究所的传统医药数据库。英文说明页写明由文部科学省区域创新集群计划于2008–2012年资助，收录生药基原、性味归经与汉方组成、适应及文献；处方文献一万余篇。和汉药实验文库含近80个化合物，以及80种生药热水提取物和80个汉方提取物的化学与生物测定，2024年起提供生物测定下载。 [[网站](https://dentomed.toyama-wakan.net/en/)] [[说明](https://dentomed.toyama-wakan.net/index_en)]
- **KNApSAcK KAMPO 汉方处方与生药库** — 奈良先端大整理的汉方公开库（约1581处方、278生药），生命科学数据库档案可下载 [[数据集](https://dbarchive.biosciencedbc.jp/data/knapsack-kampo/)] [[DOI](https://doi.org/10.1093/pcp/pcr165)]
- **OASIS 韩国传统医学信息门户** — 韩国韩医学研究院的传统医学文献与资源门户，可检索韩医论文与本草资料 [[网站](https://oasis.kiom.re.kr/)]
- **KTKP Traditional Medicine** — 韩国知识产权部的传统知识门户中的韩医部分。英文介绍写明数据库于2005–2007年以韩国传统医学文献编成，2007年12月开始检索服务。介绍页当前结构计数为药材5500、处方7103、病证12500，并关联功效、主治、方药和专利分类号。 [[介绍](https://koreantk.com/ktkp2014/about/introduction.page)] [[药材](https://koreantk.com/ktkp2014/medicine/list-by-act-part.page)] [[处方](https://koreantk.com/ktkp2014/prescription/list-by-index.page)] [[病证](https://koreantk.com/ktkp2014/disease/list-by-index.page)]
- **EKAT** — 日本东洋医学会EBM委员会的汉方治疗证据报告。官网写明2007年起免费公开并持续更新，把在售汉方制剂的随机对照试验和荟萃分析做成结构化摘要；煎剂因品质不明不收，试验限于1986年以后、与市售制剂同品质者。有日文版和英文版，大韩韩医学会另有韩语译本。 [[网站](https://www.jsom.or.jp/ebm/ekat/)]
- **ETHMEDmmm** — 富山大学和汉医药学综合研究所民族药物资料馆的生药标本库。首页表格写明和汉药461种、8942点，日文公开始于2000年4月；同站另有英文和汉药以及尤纳尼、泰药、阿育吠陀、印度尼西亚生药分库。最终更新说明为2018年3月30日的第7版。 [[网站](https://ethmed.toyama-wakan.net/)]

## 原始书籍 / 预训练语料

- **中医经典全文语料（内经/伤寒/金匮/温病等 115 部）** — 中医经典全文数字化语料：内经、难经、伤寒论、金匮要略及温病经典 [[数据集](https://huggingface.co/datasets/wangekxy/classical-tcm-canon)]
- **高质量中医预训练数据集（医案/典籍/百科等）** — 非网络来源高质量中医预训练数据集（约 1GB），含临床案例、名家典籍、医学百科等，99% 简体中文 [[数据集](https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain)]
- **ShizhenGPT 中医预训练语料（论文报告共 15B+ tokens：Stage1 文本 11.92B 含 6.3B 中医语料，Stage2 多模态约 3.6B）** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT)]
- **700 项中医药古籍文本** — 中医药古籍文本语料合集，收录近 700 项古籍文本 [[数据集](https://github.com/xiaopangxia/TCM-Ancient-Books)]
- **ChiMed 2.0 中文医疗预训练数据集（覆盖中医语料）** [[论文](https://arxiv.org/abs/2507.15275)]
- **国医典藏（中国中医古籍数字资源库）** — 中国中医科学院中医药信息研究所/图书馆的中医古籍图文库，现行入口为第4版站点。公开介绍收录先秦至清末民国医药典籍，可见口径为2500余种至3000余种，支持基本、高级和后控检索以及图文对照。校园网或注册查阅，不是公开批量下载。 [[网站](https://gydc-v4.cintcm.cn/)]
- **国家中医药古籍数字图书馆** — 中国中医科学院中医药信息研究所自2022年起建设的古籍与传统知识发布门户，设古典医籍、民国文献、版本目录等分馆，并链出国医典藏等阅读系统。门户页可打开；读全文需进入分馆，不是公开批量下载。 [[网站](http://www.cintcm.com/)]
- **中华医典（商业电子丛书，第6版为网页版）** — 商业电子丛书《中华医典》的现行销售站（飞熊科技）。站点写明收录古籍1156部、约4.5亿字，2000年获得国家电子出版物提名奖，裘沛然编审并题名。第6版是网页版，购买注册后使用，不是公开下载。 [[网站](https://www.zhyd1999.com/)]

## 评测基准

- **TCM-RobustSDT** — 中医临床推理LLM鲁棒性基准数据集（Figshare） [[数据集](https://doi.org/10.6084/m9.figshare.33054974)]
- **中药处方审核评测基准** — 328道处方规范性与合理性选择题，面向中药处方安全审核评测 [[论文](https://doi.org/10.1038/s41597-025-06387-6)] [[数据](https://doi.org/10.6084/m9.figshare.29651261.v3)] [[代码](https://github.com/zhuyan166/TCMEval/tree/main/evaluation/TCMEval-PA)]
- **TCM-AQA61 / CME-AQA 针灸推拿动作质量评估** — 针灸（A）与推拿（T）各 61 名受试者的第一人称+第三人称同步视频，两位中医师标注分类与连续指标；配套跨视角多模态评估框架 CME-AQA [[论文](https://arxiv.org/abs/2606.28104)] [[DOI](https://doi.org/10.1109/TNSRE.2026.3705649)] [[代码](https://github.com/FrancisXZhang/cme-aqa)] [[数据](https://researchdata.durham.ac.uk/collections/r1jm214p229)]
- **LingLan（灵兰秘典）大规模多任务中医评测基准 (2026)** [[数据集](https://github.com/TCMAI-BJTU/LingLan)] [[论文](https://arxiv.org/abs/2602.01779)]
- **ZhongJing-OMNI 中医多模态评测（含舌诊）** [[数据集](https://huggingface.co/datasets/CMLM/ZhongJing-OMNI)]
- **TongueDx 远程舌诊多标签数据集** — 面向远程舌诊的公开图像集：5109 张、4650 名受试者，8 个二分类舌象属性（淡、边尖红、红点、瘀斑、裂纹、齿痕、厚苔、黄苔），并带年龄和性别。仓库可下。与后续消融论文 TongueDx2 不是同一篇。 [[数据集](https://github.com/tonguedx/tonguedx)] [[论文](https://arxiv.org/abs/2501.03053)]
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

## 考试数据集

- **TCM-Text-Exams 近年中医执业/考研真题文本基准** [[数据集](https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams)]
- **医疗大模型中文考试评估** [[数据集](https://github.com/jingnant/Medical-LLMs-Chinese-Exam)]

## 指令/对话数据集

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

## 知识图谱

- **本草典开放数据（本草、方剂、证型、腧穴）** — 本草典编辑部发布的双语中医药种子数据，CC BY-SA 4.0，可直接下载 JSON。2026年4月17日生成的 v1 写明本草365条、方剂112条、证型84条、腧穴208条，另有经络、舌脉和关系图谱。同一页的覆盖说明写标准本草约530味中已收335味。这是编辑项目词表，不是国家标准。 [[网站](https://bencaodian.org/zh/about/data/)] [[数据](https://bencaodian.org/data/v1/herbs.json)]
- **灵枢症状中心上下文知识图谱** — 北交大等症状中心中西医桥接图谱（导出约1733万实体、3947万关系，含三元组+上下文四元组），门户提供可视化、推理与有据问答 [[论文](https://arxiv.org/abs/2608.20402)] [[网站](http://www.tcmkg.com/)]
- **ChatMed 知识图谱** [[数据集](https://github.com/ywjawmw/TCM_KG)]
- **TCM-MKG 中医药多维知识图谱** [[数据](https://zenodo.org/records/15395588)]
- **OpenTCM 妇科古籍知识图谱（约 4.8 万实体 / 15.2 万关系）** [[代码](https://github.com/OpenTCM01/OpenTCM)] [[论文](https://arxiv.org/abs/2504.20118)]
- **中医证候本体与疾病–证候–方剂关联平台**（服务异常） — 中国中医科学院中药研究所等建设的证候本体平台。iMeta 2023论文写明整理319个证候、8045种疾病和1359首方剂，并关联基因、疾病与方剂。论文页可核；前台页面当前没有可读的证候内容。与 ETCM 同在 tcmip.cn，但是独立证候系统。未见免登录的整库镜像。 [[网站](http://www.tcmip.cn/Syndrome/front/)] [[论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC10989962/)]
- **中医临床诊疗术语 第3部分：治法** — 现行国家标准《中医临床诊疗术语 第3部分：治法》，2023年3月17日发布并实施。国家标准全文公开系统提供在线预览和下载。这是治法术语标准页，不是独立词表数据包。 [[网站](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E8BBBAB76E1AF1498C5DA5DFBB2194EC)]
- **中医临床诊疗术语 第1部分：疾病** — 现行国家标准《中医临床诊疗术语 第1部分：疾病》，2023年3月17日发布并实施，主管部门为国家中医药局。国家标准全文公开系统提供在线预览和下载。证候部分和治法部分另有独立全文页。 [[网站](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=7377FB06FF43DC321BB6A4BF7DAA7F39)]
- **TCM-QG 中医文献问题生成（CHIP2020）** — 约 5000 篇中医文本、1.3 万问答对，用来补知识库和自动提问（CC BY-SA 4.0） [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86895)] [[资料](http://openkg.cn/dataset/tcm-qg)]
- **TCM-NER 中药说明书实体识别（OpenKG / CHIP）** — 1997 篇中药说明书、13 类实体共 59803 个标注，用来自动构建用药知识图谱（CC BY-SA 4.0） [[数据](https://tianchi.aliyun.com/dataset/dataDetail?dataId=86819)] [[资料](http://openkg.cn/dataset/tcm-ner)]
- **中医临床诊疗术语 第2部分：证候** — 现行国家标准《中医临床诊疗术语 第2部分：证候》，2021年11月26日发布并实施。国家标准全文公开系统提供在线预览和下载。这是证候术语标准页，不是独立词表数据包。 [[网站](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C71A9DAD24CB1252F12439D1F045DA6A)]
- **中医病证分类与代码** — 现行国家标准《中医病证分类与代码》，2021年10月11日发布并实施，替代 GB/T 15657-1995，主管部门为国家中医药局。国家标准全文公开系统提供在线预览和下载。这是标准全文页，不是独立的机器可读代码包。 [[网站](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=41FD9D06E5BE4F84EA1D8D07101BED2C)]
- **经穴名称与定位** — 现行国家标准《经穴名称与定位》，2021年11月26日发布并实施，主管部门为国家中医药局。国家标准全文公开系统提供在线预览和下载。这是标准全文页，不是单独打包的穴位词表。 [[网站](https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=397548AE7248D3D87DD15E0AB8107185)]
- **中医药知识服务平台** — 中国中医科学院中医药信息研究所维护的知识服务首页，面向知识检索、知识图谱和疾病画像。同一信息所的中医学专业知识服务系统关于页写明，2019年起受中国工程科技知识中心委托建设专业知识服务，汇聚病证、方剂、中药与文献资源。首页可打开；高校试用说明要求校园网注册登录，未见公开批量下载。 [[网站](https://www.tcmkb.cn/)]
- **ICD-11 传统医学病情补充章** — WHO 对 ICD-11 补充章 Traditional Medicine Conditions 的官方说明。该章用于发病数据的可选双编码，不用于死亡报告。当前模块 I 覆盖源于古代中国、现用于中国、日本、韩国及其他地区的传统医学病情。本页是章节说明，具体编码在 ICD-11 浏览器中查阅，页面公开。 [[网站](https://www.who.int/standards/classifications/frequently-asked-questions/traditional-medicine)]
- **WHO 西太平洋区标准针灸穴位定位** — WHO 西太平洋区办事处2008年出版、2009年重印的穴位定位标准。IRIS 记录写明包含体表定位方法和361个穴位，用于教学、科研、临床、出版和学术交流，并提供英文 PDF。中国、日本、韩国专家参与定位协调。记录页公开。 [[网站](https://iris.who.int/handle/10665/353407)]

返回 [[Home]]。
