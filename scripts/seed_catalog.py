#!/usr/bin/env python3
"""Generate the historical seed catalog without overwriting the live catalog."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "catalog.seed.yml"
VERIFIED = "2026-07-19"


def item(**kwargs):
    kwargs.setdefault("status", "published")
    kwargs.setdefault("verified_at", VERIFIED)
    kwargs.setdefault("tags", [])
    return kwargs


def main(output: Path = OUT, force: bool = False) -> int:
    items = []

    # ---- news ----
    news = [
        ("2026.06", "中科闻歌通过港交所上市聆讯；报道提及与中国中医科学院合作的**大医金匮**中医大模型已通过中国信通院最高级别可信AI认证", "https://www.ncsti.gov.cn/kjdt/xwjj/202606/t20260610_249369.html", ["product"], "大医金匮聆讯措辞已按核验修正"),
        ("2026.04", "北京中医药大学牵头研发的**薪火中国药**中医药教育大模型通过国家生成式人工智能服务备案，成为国内首个获批面向公众服务的中医药领域大模型", "https://regional.chinadaily.com.cn/education/cn/2026-04/22/c_1177692.htm", ["product"]),
        ("2025.12", "吉林发布**众星·长白岐黄1.0** AI原生多模态中医药大模型", "https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml", ["multimodal", "product"]),
        ("2025.12", "固生堂发布”中医大脑”产品及国医大师施杞教授AI数字分身，已累计发布14位顶级专家数字分身，覆盖八大中医核心专科", "https://www.jjckb.cn/20251231/693ca93b14ff4f57adc359959dc0320d/c.html", ["product"]),
        ("2025.12", "**智明堂ZMT-M1**在国家中医执业医师资格考试模拟测试中以96.26分获得该领域最佳成绩，已在全国100余间诊室试点应用", "https://m.tech.china.com/redian/2025/1229/122025_1789291.html", ["product"]),
        ("2025.11", "国家卫健委等五部门印发《关于促进和规范”人工智能+医疗卫生”应用发展的实施意见》，明确支撑建设中医药诊疗大模型", "https://www.gov.cn/zhengce/zhengceku/202511/content_7047018.htm", ["policy"]),
        ("2025.09", "传神语联**任度·素问**通过中国信通院可信AI中医药大模型4+级评估", "https://zhongyi.gmw.cn/2025-09/10/content_38277329.htm", ["product"]),
        ("2025.09", "**智赋岐黄天功**中医AI大模型通过国家深度合成服务算法备案，应用于中医四诊仪与体质辨识", "http://zs.scbzol.com/zs/2025/0919/328624.html", ["product"]),
        ("2025.08", "**固生堂**正式发布十大”国医AI分身”，基于国医大师及名中医临床经验构建，辨证准确性达86%以上", "http://sz.people.com.cn/n2/2025/0801/c202846-41310443.html", ["product"]),
        ("2025.06", "**中医横琴**垂类大模型正式发布", "https://www.stdaily.com/web/gdxw/2025-06/20/content_357526.html", ["product"]),
        ("2025.05", "中国中医科学院发布中医药大模型评测标准", "https://www.news.cn/politics/20250510/5e6a0b4978b44b69b67dbfb7282fd220/c.html", ["benchmark"]),
        ("2025.04", "传神语联发布**任度·素问**中医大模型，基于全自研混合熵(moH)技术架构，支持智能问诊、辨证分析、方剂推荐", "https://www.transn.com/about_us/consult/article/1924766101036437505", ["product"]),
        ("2025.03", "中国中医科学院广安门医院28日正式发布**广医·岐智**中医大模型，成为国内首家本地化部署”算力+模型+应用”一体化服务的中医医院", "https://www.xinhuanet.com/tech/20250328/8b1685ad8c6f48c9bdc2add1658edac3/c.html", ["product"]),
        ("2024.09", "中科闻歌发布**大医金匮**中医大模型及中医智能健康管理平台，基于1500余本中医典籍训练", "https://36kr.com/newsflashes/2946967562099592", ["product"]),
        ("2024.03", "华东师范大学、上海中医药大学、华东理工大学、海军军医大学、临港实验室、华润江中现代中药全国重点实验室联合开发了**数智岐黄**中医药大模型。", None, ["product"]),
    ]
    for i, row in enumerate(news):
        date, summary, url, tags = row[0], row[1], row[2], row[3]
        note = row[4] if len(row) > 4 else None
        entry = item(
            id=f"news-{date.replace('.', '')}-{i:02d}",
            name=summary.replace("**", "")[:40],
            type="news",
            year=int(date.split(".")[0]),
            date=date,
            summary_zh=summary,
            tags=tags,
            links={"链接": url} if url else {},
        )
        if note:
            entry["align_note"] = note
        items.append(entry)

    # ---- resources by year ----
    resources = [
        # 2026
        dict(id="gastro-tcm", name="GastroTCM", year=2026, venue="Chinese Medicine", summary_zh="中医消化内科大模型，基于Llama3-8B微调并结合RAG与智能体框架", tags=["model", "agent"], links={"论文": "https://link.springer.com/article/10.1186/s13020-025-01295-8"}),
        dict(id="tonguevlm", name="TongueVLM", year=2026, venue="JMIR Medical Informatics", summary_zh="中医舌诊多模态大模型，支持舌象描述生成与体质推理", tags=["multimodal", "model"], links={"论文": "https://doi.org/10.2196/87237", "JMIR": "https://medinform.jmir.org/2026/1/e87237"}, align_note="主链 DOI，JMIR 备选"),
        dict(id="mmir-tcm", name="MMIR-TCM", year=2026, summary_zh="记忆增强的多模态舌诊与临床决策框架，提出 MedTCM 数据集与 TDEU 评测指标", tags=["multimodal", "benchmark"], links={"论文": "https://arxiv.org/abs/2607.01814"}),
        dict(id="linglan", name="灵兰秘典 (LingLan)", year=2026, summary_zh="大规模多任务中医评测基准，覆盖 5 大域、13 子任务、25624 实例", orgs=["北京交通大学等"], tags=["benchmark"], links={"论文": "https://arxiv.org/abs/2602.01779", "代码": "https://github.com/TCMAI-BJTU/LingLan", "网站": "http://tcmnlp.com"}),
        dict(id="tcm-agent", name="TCM-Agent", year=2026, summary_zh="面向网络药理学与中药发现的 LLM 多智能体系统", tags=["agent"], links={"论文": "https://doi.org/10.1016/j.jpha.2026.101581", "代码": "https://github.com/AITCM/TCM-Agent"}),
        dict(id="tcm-diffrag", name="TCM-DiffRAG", year=2026, summary_zh="通用知识图谱 + 个性化知识图谱 + CoT 的辨证推理 RAG 框架", tags=["rag", "kg"], links={"论文": "https://arxiv.org/abs/2602.22828", "代码": "https://github.com/LiJianmin6706/Tcm_Diff_RAG"}),
        dict(id="core-acu", name="CORE-Acu", year=2026, summary_zh="针灸临床决策：结构化推理轨迹与知识图谱安全否决闭环", tags=["agent", "kg"], links={"论文": "https://arxiv.org/abs/2603.08321"}),
        # 2025
        dict(id="shennong-alpha", name="神农Alpha", year=2025, venue="Cell Discovery", summary_zh="中药大模型", orgs=["西湖大学"], tags=["model"], links={"网站": "https://shennongalpha.westlake.edu.cn/", "论文": "https://www.nature.com/articles/s41421-025-00776-2", "代码": "https://github.com/shennong-program/shennongname"}),
        dict(id="tcmchat", name="TCMChat", year=2025, venue="Pharmacological Research", summary_zh="中药知识聊天机器人", orgs=["浙江大学"], tags=["model", "open-weights"], links={"论文": "https://doi.org/10.1016/j.phrs.2024.107530", "ScienceDirect": "https://www.sciencedirect.com/science/article/pii/S1043661824004754", "代码": "https://github.com/ZJUFanLab/TCMChat", "模型": "https://huggingface.co/ZJUFanLab/TCMChat-600k", "数据集": "https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k"}),
        dict(id="zhongjing", name="仲景 (ZhongJing)", year=2025, venue="Tsinghua Science and Technology", summary_zh="中医大模型", orgs=["福耀科技大学，健康长三角研究院，复旦大学，同济大学"], tags=["model", "open-weights"], links={"论文": "https://doi.org/10.26599/TST.2025.9010046", "代码": "https://github.com/pariskang/CMLM-ZhongJing", "模型": "https://huggingface.co/CMLM/ZhongjingGPT1_13B"}),
        dict(id="tcm-r1", name="TCM-R1", year=2025, venue="APWeb-WAIM 2025", summary_zh="通过GRPO增强中医推理能力的大模型", orgs=["西南大学"], tags=["model"], links={"论文": "https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21"}),
        dict(id="tcm-ladder", name="TCM-Ladder", year=2025, venue="NeurIPS 2025", summary_zh="首个中医多模态问答评测基准，涵盖52000+题目", tags=["benchmark", "multimodal"], links={"论文": "https://arxiv.org/abs/2505.24063", "代码": "https://github.com/orangeshushu/TCM-Ladder", "榜单": "https://tcmladder.com"}),
        dict(id="jingfang", name="经方 (Jingfang)", year=2025, summary_zh="基于LLM的中医多智能体诊疗系统，辨证精度提升124%", tags=["agent"], links={"论文": "https://arxiv.org/abs/2502.04345"}),
        dict(id="zmt-m1", name="智明堂 (ZMT-M1)", year=2025, summary_zh="中医大模型及TCM-Eval动态可扩展评测基准", orgs=["北京航空航天大学"], tags=["model", "benchmark"], links={"论文": "https://arxiv.org/abs/2511.07148", "平台": "https://tcmeval.bamaidical.com"}),
        dict(id="shizhengpt", name="ShizhenGPT", year=2025, summary_zh="中医多模态大模型，支持望闻问切", orgs=["香港中文大学(深圳)等"], tags=["multimodal", "model", "open-weights"], links={"论文": "https://arxiv.org/abs/2508.14706", "代码": "https://github.com/FreedomIntelligence/ShizhenGPT", "模型": "https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni", "预训练数据": "https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT", "指令数据": "https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT"}),
        dict(id="dopi", name="DoPI", year=2025, summary_zh="类医生主动问诊中医大模型，引导模型+专家模型协同架构，问诊准确率84.68%", tags=["model", "agent"], links={"论文": "https://arxiv.org/abs/2507.04877"}),
        dict(id="mtcmb", name="MTCMB", year=2025, summary_zh="中医多任务评测基准，12子集约7100样本，覆盖知识/推理/方剂/安全", tags=["benchmark"], links={"论文": "https://arxiv.org/abs/2506.01252", "代码": "https://github.com/Wayyuanyuan/MTCMB"}),
        dict(id="tcm-3ceval", name="TCM-3CEval", year=2025, summary_zh="中医大模型三轴评测（核心知识、经典理解、临床决策）", tags=["benchmark"], links={"论文": "https://arxiv.org/abs/2503.07041"}),
        dict(id="opentcm", name="OpenTCM", year=2025, summary_zh="基于 GraphRAG 的中医知识检索与诊断系统，含妇科古籍知识图谱", tags=["rag", "kg", "tool"], links={"论文": "https://arxiv.org/abs/2504.20118", "代码": "https://github.com/OpenTCM01/OpenTCM"}, align_note="规范仓 OpenTCM01/OpenTCM"),
        dict(id="chattcm", name="ChatTCM", year=2025, summary_zh="从预训练数据到模型权重完全开源的中医大模型", tags=["model", "open-weights"], links={"模型": "https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain", "预训练数据": "https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain", "SFT数据": "https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT"}),
        dict(id="tcm-5ceval", name="TCM-5CEval", year=2025, summary_zh="在 TCM-3CEval 基础上扩展本草与非药物疗法的五维深度评测", tags=["benchmark"], links={"论文": "https://arxiv.org/abs/2511.13169"}),
        dict(id="tcm-best4sdt", name="TCM-BEST4SDT", year=2025, summary_zh="面向辨证论治的病例评测基准（知识/伦理/安全/SDT）", tags=["benchmark"], links={"论文": "https://arxiv.org/abs/2512.02816", "代码": "https://github.com/DYJG-research/TCM-BEST4SDT"}),
        dict(id="renshu-ai", name="仁术AI (RenShu-AI)", year=2025, summary_zh="FastAPI + LangGraph 多智能体中医问诊系统，融合 GraphRAG 与 DeepSeek-TCM", tags=["agent", "tool"], links={"代码": "https://github.com/yanlinPeng-code/RenShu-AI"}),
        # 2024
        dict(id="medchatzh", name="MedChatZH", year=2024, venue="Computers in Biology and Medicine", summary_zh="中医问诊大模型", orgs=["华东理工大学"], tags=["model", "open-weights"], links={"论文": "https://doi.org/10.1016/j.compbiomed.2024.108290", "ScienceDirect": "https://www.sciencedirect.com/science/article/pii/S0010482524003743", "数据集": "https://huggingface.co/datasets/tyang816/MedChatZH", "模型": "https://huggingface.co/tyang816/medchatzh", "代码": "https://github.com/tyang816/MedChatZH"}),
        dict(id="lingdan", name="TCMLLM / 灵丹 (Lingdan)", year=2024, venue="Digital Chinese Medicine", summary_zh="中医药大模型与处方推荐", orgs=["北京交通大学"], tags=["model", "open-weights"], links={"论文": "https://doi.org/10.1016/j.dcmed.2025.01.007", "ScienceDirect": "https://www.sciencedirect.com/science/article/pii/S2589377725000072", "代码": "https://github.com/2020MEAI/TCMLLM", "灵丹代码": "https://github.com/TCMAI-BJTU/LingdanLLM", "模型": "https://huggingface.co/TCMLLM/Lingdan-13B-Base"}),
        dict(id="ming", name="明医 (MING)", year=2024, summary_zh="中文医疗问诊大模型", orgs=["上海交通大学"], tags=["model", "general-medical"], links={"论文": "https://arxiv.org/abs/2404.09027", "相关 MedCare": "https://aclanthology.org/2024.findings-emnlp.619/", "代码": "https://github.com/MediaBrain-SJTU/MING"}, align_note="ACL anthology 619 为 MedCare，明医主论文改 arXiv"),
        dict(id="huatuo-bencao", name="本草[原名：华驼(HuaTuo)]", year=2024, venue="ACM Trans. Knowl. Discov. Data", summary_zh="基于中文医学知识的大语言模型指令微调", orgs=["哈尔滨工业大学"], tags=["model", "general-medical"], links={"论文": "https://arxiv.org/pdf/2309.04175.pdf", "代码": "https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese"}),
        dict(id="biancang", name="扁仓 (BianCang)", year=2024, summary_zh="系列中医大模型，2025.12 开源 14B 版本", orgs=["齐鲁工业大学"], tags=["model", "open-weights"], links={"论文": "https://arxiv.org/abs/2411.11027", "代码": "https://github.com/QLU-NLP/BianCang", "模型": "https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct"}),
        dict(id="bigdatatcm", name="大数中医 (BigDataTCM)", year=2024, summary_zh="中医垂直领域大模型", orgs=["河南工业大学"], tags=["model"], links={"代码": "https://github.com/HAUT-CS/BigDataTCM"}),
        dict(id="mcm", name="MCM", year=2024, summary_zh="多模态中医药问诊大模型", orgs=["上海计算机软件技术开发中心"], tags=["multimodal", "model"], links={"代码": "https://github.com/JerryMazeyu/MCM"}),
        dict(id="chinese-llava-med", name="Chinese-LLaVA-Med", year=2024, summary_zh="中文医学多模态大模型", tags=["multimodal", "general-medical"], links={"代码": "https://github.com/BUAADreamer/Chinese-LLaVA-Med"}),
        # 2023
        dict(id="huatuogpt", name="华佗GPT", year=2023, venue="EMNLP findings", summary_zh="中文医学语料训练的大型语言模型", orgs=["香港中文大学(深圳)，深圳市大数据研究院"], tags=["model", "general-medical"], links={"论文": "https://aclanthology.org/2023.findings-emnlp.725/", "代码": "https://github.com/FreedomIntelligence/HuatuoGPT"}),
        dict(id="bianque", name="扁鹊 (BianQue)", year=2023, summary_zh="中文领域生活空间主动健康大模型", orgs=["华南理工大学，广东省数字孪生人重点实验室"], tags=["model", "general-medical"], links={"代码": "https://github.com/scutcyr/BianQue"}),
        dict(id="huangdi", name="黄帝 (HuangDi)", year=2023, summary_zh="中医古籍知识问答大模型", orgs=["南京大学, 郑州大学"], tags=["model"], links={"代码": "https://github.com/Zlasejd/HuangDI"}),
        dict(id="qizhengpt", name="启真医学大模型 (QiZhenGPT)", year=2023, summary_zh="中文医疗场景、药品知识问答、优化疾病、手术、检验等", orgs=["浙江大学"], tags=["model", "general-medical"], links={"代码": "https://github.com/CMKRG/QiZhenGPT"}),
        dict(id="shennong-tcm-llm", name="神农大模型 (ShenNong-TCM-LLM)", year=2023, summary_zh="中医药大规模语言模型", tags=["model", "open-weights"], links={"代码": "https://github.com/michael-wzhu/ShenNong-TCM-LLM", "数据集": "https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset", "模型": "https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM"}),
        dict(id="sunsimiao", name="孙思邈 (Sunsimiao)", year=2023, summary_zh="中文医疗大模型", orgs=["华东理工大学"], tags=["model", "general-medical"], links={"代码": "https://github.com/X-D-Lab/Sunsimiao"}),
        dict(id="chatmed", name="ChatMed", year=2023, summary_zh="系列中文医疗大规模语言模型", tags=["model", "general-medical"], links={"代码": "https://github.com/michael-wzhu/ChatMed"}),
        dict(id="xrayglm", name="XrayGLM", year=2023, summary_zh="会看胸部X光片的中文多模态医学大模型", orgs=["澳门理工大学"], tags=["multimodal", "general-medical"], links={"代码": "https://github.com/WangRongsheng/XrayGLM"}),
    ]
    for r in resources:
        r["type"] = "resource"
        items.append(item(**r))

    # ---- datasets ----
    datasets = [
        dict(id="awesome-cmed-nlp", name="awesome_Chinese_medical_NLP", section="公开资料整理", title_zh="awesome_Chinese_medical_NLP", tags=["general-medical"], links={"资料": "https://github.com/GanjinZero/awesome_Chinese_medical_NLP"}),
        dict(id="tcm-ancient-books", name="TCM-Ancient-Books", section="原始书籍 / 预训练语料", title_zh="700 项中医药古籍文本", tags=["corpus"], links={"数据集": "https://github.com/xiaopangxia/TCM-Ancient-Books"}),
        dict(id="classical-tcm-canon", name="classical-tcm-canon", section="原始书籍 / 预训练语料", title_zh="中医经典全文语料（内经/伤寒/金匮/温病等 115 部）", tags=["corpus"], links={"数据集": "https://huggingface.co/datasets/wangekxy/classical-tcm-canon"}),
        dict(id="shizhen-pretrain", name="TCM-Pretrain-Data-ShizhenGPT", section="原始书籍 / 预训练语料", title_zh="ShizhenGPT 中医预训练语料（约 6B tokens，含图文交错数据）", tags=["corpus", "multimodal"], links={"数据集": "https://huggingface.co/datasets/FreedomIntelligence/TCM-Pretrain-Data-ShizhenGPT"}),
        dict(id="sylvanl-pretrain", name="Traditional-Chinese-Medicine-Dataset-Pretrain", section="原始书籍 / 预训练语料", title_zh="高质量中医预训练数据集（医案/典籍/百科等）", tags=["corpus"], links={"数据集": "https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-Pretrain"}),
        dict(id="ds-linglan", name="LingLan", section="评测基准", title_zh="LingLan（灵兰秘典）大规模多任务中医评测基准 (2026)", year=2026, tags=["benchmark"], links={"数据集": "https://github.com/TCMAI-BJTU/LingLan", "论文": "https://arxiv.org/abs/2602.01779"}),
        dict(id="ds-tcm-ladder", name="TCM-Ladder", section="评测基准", title_zh="TCM-Ladder 中医多模态问答评测基准 (NeurIPS 2025)", year=2025, tags=["benchmark", "multimodal"], links={"数据集": "https://github.com/orangeshushu/TCM-Ladder", "HF": "https://huggingface.co/datasets/timzzyus/TCM-Ladder", "榜单": "https://tcmladder.com"}),
        dict(id="ds-mtcmb", name="MTCMB", section="评测基准", title_zh="MTCMB 中医多任务评测基准（知识/推理/安全）", tags=["benchmark"], links={"数据集": "https://github.com/Wayyuanyuan/MTCMB", "论文": "https://arxiv.org/abs/2506.01252"}),
        dict(id="ds-tcm-3c", name="TCM-3CEval", section="评测基准", title_zh="TCM-3CEval 核心知识·经典理解·临床决策三轴评测", tags=["benchmark"], links={"论文": "https://arxiv.org/abs/2503.07041"}),
        dict(id="ds-tcm-5c", name="TCM-5CEval", section="评测基准", title_zh="TCM-5CEval 五维中医深度评测", tags=["benchmark"], links={"论文": "https://arxiv.org/abs/2511.13169"}),
        dict(id="ds-best4sdt", name="TCM-BEST4SDT", section="评测基准", title_zh="TCM-BEST4SDT 辨证论治病例评测基准", tags=["benchmark"], links={"数据集": "https://github.com/DYJG-research/TCM-BEST4SDT", "论文": "https://arxiv.org/abs/2512.02816"}),
        dict(id="ds-tcm-eval", name="TCM-Eval", section="评测基准", title_zh="TCM-Eval 动态可扩展中医评测基准", tags=["benchmark"], links={"论文": "https://arxiv.org/abs/2511.07148", "平台": "https://tcmeval.bamaidical.com"}, align_note="arxiv 链接标论文非数据集"),
        dict(id="ds-tcmbench", name="TCMBench", section="评测基准", title_zh="TCMBench 中医药大模型全面评测基准", tags=["benchmark"], links={"数据集": "https://github.com/ywjawmw/TCMBench", "论文": "https://arxiv.org/abs/2406.01126"}),
        dict(id="ds-zhongjing-omni", name="ZhongJing-OMNI", section="评测基准", title_zh="ZhongJing-OMNI 中医多模态评测（含舌诊）", tags=["benchmark", "multimodal"], links={"数据集": "https://huggingface.co/datasets/CMLM/ZhongJing-OMNI"}),
        dict(id="ds-tcm-vision", name="TCM-Vision-Benchmark", section="评测基准", title_zh="TCM-Vision-Benchmark 中医视觉评测（药材识别/望诊等，约 7k 题）", tags=["benchmark", "multimodal"], links={"数据集": "https://huggingface.co/datasets/FreedomIntelligence/TCM-Vision-Benchmark"}),
        dict(id="ds-tcmeval-sdt", name="TCMEval-SDT", section="评测基准", title_zh="TCMEval-SDT 辨证思维评测（专家标注病案）", tags=["benchmark"], links={"论文": "https://www.nature.com/articles/s41597-025-04772-9", "代码": "https://github.com/zhuyan166/TCMEval"}),
        dict(id="ds-hwtcm", name="HWTCMBench", section="评测基准", title_zh="HWTCMBench 中医能力评测集", tags=["benchmark"], links={"数据集": "https://huggingface.co/datasets/Monor/hwtcm"}),
        dict(id="ds-med-exam", name="Medical-LLMs-Chinese-Exam", section="考试数据集", title_zh="医疗大模型中文考试评估", tags=["benchmark", "general-medical"], links={"数据集": "https://github.com/jingnant/Medical-LLMs-Chinese-Exam"}),
        dict(id="ds-tcm-text-exams", name="TCM-Text-Exams", section="考试数据集", title_zh="TCM-Text-Exams 近年中医执业/考研真题文本基准", tags=["benchmark"], links={"数据集": "https://huggingface.co/datasets/FreedomIntelligence/TCM-Text-Exams"}),
        dict(id="ds-shennong", name="ShenNong_TCM_Dataset", section="指令/对话数据集", title_zh="中医药指令数据集 ShenNong_TCM_Dataset", tags=["sft"], links={"数据集": "https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset"}),
        dict(id="ds-chatmed-consult", name="ChatMed_Consult_Dataset", section="指令/对话数据集", title_zh="中文医疗在线问诊数据集 ChatMed_Consult_Dataset（50w+在线问诊+ChatGPT回复）", tags=["sft", "general-medical"], links={"数据集": "https://huggingface.co/datasets/michaelwzhu/ChatMed_Consult_Dataset"}),
        dict(id="ds-medchatzh", name="MedChatZH", section="指令/对话数据集", title_zh="MedChatZH 中医问诊数据集", tags=["sft"], links={"数据集": "https://huggingface.co/datasets/tyang816/MedChatZH"}),
        dict(id="ds-cmtmedqa", name="CMtMedQA", section="指令/对话数据集", title_zh="CMtMedQA 仲景真实多轮医患对话（约 7 万条）", tags=["sft"], links={"数据集": "https://huggingface.co/datasets/Suprit/CMtMedQA"}),
        dict(id="ds-tcmchat-600k", name="TCMChat-dataset-600k", section="指令/对话数据集", title_zh="TCMChat-dataset-600k 中药知识问答与推荐指令数据", tags=["sft"], links={"数据集": "https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k"}),
        dict(id="ds-shizhen-sft", name="TCM-Instruction-Tuning-ShizhenGPT", section="指令/对话数据集", title_zh="ShizhenGPT 多模态指令微调数据（文本/视觉/语音，约 245K）", tags=["sft", "multimodal"], links={"数据集": "https://huggingface.co/datasets/FreedomIntelligence/TCM-Instruction-Tuning-ShizhenGPT"}),
        dict(id="ds-sylvanl-sft", name="Traditional-Chinese-Medicine-Dataset-SFT", section="指令/对话数据集", title_zh="高质量中医 SFT 数据集", tags=["sft"], links={"数据集": "https://huggingface.co/datasets/SylvanL/Traditional-Chinese-Medicine-Dataset-SFT"}),
        dict(id="ds-chatmed-kg", name="TCM_KG", section="知识图谱", title_zh="ChatMed 知识图谱", tags=["kg"], links={"数据集": "https://github.com/ywjawmw/TCM_KG"}),
        dict(id="ds-opentcm-kg", name="OpenTCM-KG", section="知识图谱", title_zh="OpenTCM 妇科古籍知识图谱（约 4.8 万实体 / 15.2 万关系）", tags=["kg"], links={"代码": "https://github.com/OpenTCM01/OpenTCM", "论文": "https://arxiv.org/abs/2504.20118"}),
        dict(id="ds-tcm-mkg", name="TCM-MKG", section="知识图谱", title_zh="TCM-MKG 中医药多维知识图谱", tags=["kg"], links={"数据": "https://zenodo.org/records/15395588"}),
    ]
    for d in datasets:
        d["type"] = "dataset"
        d.setdefault("year", 2025)
        items.append(item(**d))

    # ---- HF model gallery ----
    hf_models = [
        dict(id="hf-shizhengpt", name="ShizhenGPT", title_zh="ShizhenGPT 系列", links={"7B-LLM": "https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-LLM", "7B-VL": "https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-VL", "7B-Omni": "https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni", "32B-LLM": "https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-LLM", "32B-VL": "https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-VL"}),
        dict(id="hf-biancang", name="BianCang", title_zh="扁仓 (BianCang) 系列", links={"Qwen2.5-7B-Instruct": "https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct", "Qwen2.5-14B-Instruct": "https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-14B-Instruct"}),
        dict(id="hf-tcmchat", name="TCMChat", title_zh="TCMChat", links={"TCMChat-600k": "https://huggingface.co/ZJUFanLab/TCMChat-600k"}),
        dict(id="hf-zhongjing", name="ZhongJing", title_zh="仲景", links={"ZhongjingGPT1_13B": "https://huggingface.co/CMLM/ZhongjingGPT1_13B", "ZhongJing-2-1.8B": "https://huggingface.co/CMLL/ZhongJing-2-1_8b"}),
        dict(id="hf-lingdan", name="Lingdan", title_zh="灵丹", links={"Lingdan-13B-Base": "https://huggingface.co/TCMLLM/Lingdan-13B-Base", "Lingdan-13B-PR": "https://huggingface.co/TCMLLM/Lingdan-13B-PR"}),
        dict(id="hf-medchatzh", name="medchatzh", title_zh="MedChatZH", links={"medchatzh": "https://huggingface.co/tyang816/medchatzh"}),
        dict(id="hf-shennong", name="ShenNong-TCM-LLM", title_zh="神农", links={"ShenNong-TCM-LLM": "https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM"}),
        dict(id="hf-chattcm", name="ChatTCM", title_zh="ChatTCM", links={"ChatTCM-7B-Pretrain": "https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain"}),
    ]
    for m in hf_models:
        m["type"] = "model_hf"
        m["section"] = "Hugging Face 开源模型（精选）"
        m["year"] = 2025
        m["tags"] = ["open-weights", "model"]
        items.append(item(**m))

    catalog = {
        "meta": {
            "title": "Awesome-TCM-LLM",
            "title_zh": "中医大模型资源",
            "description_zh": "开源中文医疗大模型（中医/西医）相关新闻、论文、模型与数据集精选列表。",
            "description_en": "Curated open resources for Traditional Chinese Medicine (and related Chinese medical) LLMs.",
            "repo_url": "https://github.com/tyang816/Awesome-TCM-LLM",
            "portal_url": "https://tyang816.github.io/projects/tcm/",
            "updated_at": VERIFIED,
            "catalog_version": 1,
        },
        "items": items,
    }

    output = output.resolve()
    live_catalog = (ROOT / "data" / "catalog.yml").resolve()
    if output == live_catalog and not force:
        print(
            "Refusing to overwrite data/catalog.yml with the historical seed. "
            "Pass --force only if this destructive replacement is intentional.",
            file=sys.stderr,
        )
        return 2
    if output.exists() and not force:
        print(f"Refusing to overwrite existing file: {output} (use --force)", file=sys.stderr)
        return 2

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        yaml.dump(catalog, allow_unicode=True, sort_keys=False, width=120),
        encoding="utf-8",
    )
    print(f"Wrote {output} with {len(items)} historical seed items")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUT)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    raise SystemExit(main(args.output, args.force))
