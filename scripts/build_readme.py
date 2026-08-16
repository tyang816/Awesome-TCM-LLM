#!/usr/bin/env python3
"""Build README.md, README_EN.md, wiki catalog pages, and data/catalog.json."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Please install PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parents[1]
CATALOG_YML = ROOT / "data" / "catalog.yml"
CATALOG_JSON = ROOT / "data" / "catalog.json"
I18N_EN_YML = ROOT / "data" / "i18n_en.yml"
README_ZH = ROOT / "README.md"
README_EN = ROOT / "README_EN.md"
WIKI_DIR = ROOT / "wiki"

SITE_ZH = "https://tyang816.github.io/zh/"
SITE_EN = "https://tyang816.github.io/"
DEFAULT_PORTAL = "https://tyang816.github.io/projects/tcm/"
PORTAL_ZH = "https://tyang816.github.io/zh/projects/tcm/"
WIKI_HOME = "https://github.com/tyang816/Awesome-TCM-LLM/wiki"

DATASET_SECTION_ORDER_ZH = [
    "公开资料整理",
    "原始书籍 / 预训练语料",
    "评测基准",
    "考试数据集",
    "指令/对话数据集",
    "知识图谱",
    "语料/指令",
]

HF_SECTION = "Hugging Face 开源模型（精选）"

SECTION_EN = {
    "公开资料整理": "Curated lists",
    "原始书籍 / 预训练语料": "Books / pretraining corpora",
    "评测基准": "Benchmarks",
    "考试数据集": "Exam datasets",
    "指令/对话数据集": "Instruction / dialogue datasets",
    "知识图谱": "Knowledge graphs",
    "Hugging Face 开源模型（精选）": "Hugging Face models (selected)",
    "语料/指令": "Corpora / instructions",
    "其他": "Other",
}

LINK_LABEL_EN = {
    "论文": "Paper",
    "代码": "Code",
    "灵丹代码": "Lingdan code",
    "模型": "Model",
    "数据集": "Dataset",
    "链接": "Link",
    "DOI": "DOI",
    "预训练数据": "Pretrain data",
    "SFT数据": "SFT data",
    "指令数据": "Instruction data",
    "网站": "Website",
    "新闻": "News",
    "数据": "Data",
    "资料": "Resources",
    "榜单": "Leaderboard",
    "平台": "Platform",
    "相关 MedCare": "Related MedCare",
    "GGUF": "GGUF",
    "JMIR": "JMIR",
    "ScienceDirect": "ScienceDirect",
    "正式发表": "Published",
    "arXiv": "arXiv",
    "预印本": "Preprint",
}

SEMANTIC_TAGS = {
    "model",
    "open-weights",
    "multimodal",
    "agent",
    "rag",
    "kg",
    "benchmark",
    "evaluation",
    "dataset",
    "sft",
    "corpus",
    "general-medical",
    "history",
    "product",
    "policy",
    "tool",
    "ancient-books",
    "herbal",
    "survey",
    "reasoning",
    "prescription",
}

# First match wins for non-model leftover papers.
PAPER_CATEGORY_RULES = [
    ("eval", lambda tags: "benchmark" in tags or "evaluation" in tags),
    ("agent", lambda tags: "agent" in tags),
    ("multimodal", lambda tags: "multimodal" in tags),
    ("rag_kg", lambda tags: "rag" in tags or "kg" in tags),
]

PAPER_LINK_KEYS = ("论文", "DOI", "正式发表", "arXiv", "Paper", "Published")
CODE_LINK_KEYS = ("代码", "Code", "灵丹代码")
WEIGHT_LINK_KEYS = ("模型", "Model", "GGUF")

# Lists longer than this nest by year inside a section fold.
FLAT_LIMIT = 12


def strip_md_bold(text: str) -> str:
    return re.sub(r"\*\*([^*]+)\*\*", r"\1", text or "")


def load_i18n_en() -> dict:
    if not I18N_EN_YML.exists():
        return {}
    data = yaml.safe_load(I18N_EN_YML.read_text(encoding="utf-8")) or {}
    return data if isinstance(data, dict) else {}


def apply_i18n(entry: dict, i18n: dict) -> dict:
    """Return a shallow copy with English fields filled from data/i18n_en.yml."""
    out = dict(entry)
    patch = i18n.get(entry.get("id")) or {}
    if isinstance(patch, str):
        patch = {"summary_en": patch}
    for key in ("summary_en", "title_en", "name_en"):
        if patch.get(key) and not out.get(key):
            out[key] = patch[key]
    if patch.get("orgs_en"):
        out["orgs"] = list(patch["orgs_en"])
    return out


def published(items: list[dict]) -> list[dict]:
    return [i for i in items if i.get("status", "published") == "published"]


def tags_of(entry: dict) -> set[str]:
    return {t for t in (entry.get("tags") or []) if isinstance(t, str)}


def year_of(entry: dict) -> int:
    try:
        return int(entry.get("year") or 0)
    except (TypeError, ValueError):
        return 0


def link_md(label: str, url: str) -> str:
    return f"[[{label}]({url})]"


def format_links(links: dict | None, lang: str = "zh") -> str:
    if not links:
        return ""
    parts = []
    for key, url in links.items():
        if not url:
            continue
        if lang == "en":
            label = LINK_LABEL_EN.get(key, key)
            if re.search(r"[\u4e00-\u9fff]", label):
                label = re.sub(r"[\u4e00-\u9fff]+", "", label).strip() or "Link"
        else:
            label = key
        parts.append(link_md(label, url))
    return (" " + " ".join(parts)) if parts else ""


def entry_blurb(entry: dict, lang: str) -> str:
    if lang == "en":
        return entry.get("summary_en") or entry.get("title_en") or ""
    return entry.get("summary_zh") or entry.get("title_zh") or entry.get("name", "")


def display_name(entry: dict, lang: str) -> str:
    if lang == "en":
        return entry.get("name_en") or entry.get("title_en") or entry.get("name", "")
    return entry.get("title_zh") or entry.get("name", "")


def format_resource_line(entry: dict, lang: str) -> str:
    bits = ["-"]
    if entry.get("venue"):
        bits.append(f"[*{entry['venue']}*]")
    bits.append(f"**{display_name(entry, lang)}**")
    blurb = entry_blurb(entry, lang)
    if blurb:
        bits.append(blurb)
    orgs = entry.get("orgs") or []
    if lang == "en":
        orgs = [o for o in orgs if not re.search(r"[\u4e00-\u9fff]", o)]
    if orgs:
        sep = ", " if lang == "en" else "，"
        bits.append(f"[{sep.join(orgs)}]")
    return " ".join(bits) + format_links(entry.get("links"), lang)


def format_news_line(entry: dict, lang: str) -> str:
    date = entry.get("date") or str(entry.get("year", ""))
    if lang == "en":
        text = entry.get("summary_en") or entry.get("name") or ""
    else:
        text = entry.get("summary_zh", "")
    line = f"- [{date}] {text}"
    links = entry.get("links") or {}
    if lang == "zh" and links.get("链接"):
        line += f" {link_md('链接', links['链接'])}"
    elif lang == "en" and (links.get("链接") or links.get("Link")):
        url = links.get("Link") or links.get("链接")
        line += f" {link_md('Link', url)}"
    else:
        line += format_links(links, lang)
    return line


def format_dataset_line(entry: dict, lang: str) -> str:
    title = display_name(entry, lang)
    return f"- {title}{format_links(entry.get('links'), lang)}"


def lang_switcher(lang: str) -> str:
    if lang == "zh":
        return "**语言 / Language:** [中文](README.md) | [English](README_EN.md)"
    return "**Language / 语言:** [English](README_EN.md) | [中文](README.md)"


def badges() -> str:
    return (
        "![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  "
        "[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) "
        "![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  "
        "![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork)"
    )


def details_block(summary: str, body_lines: list[str], open_: bool = False) -> list[str]:
    if not body_lines:
        return []
    attr = " open" if open_ else ""
    return [
        f"<details{attr}>",
        f"<summary>{summary}</summary>",
        "",
        *body_lines,
        "",
        "</details>",
        "",
    ]


def group_by_year(entries: list[dict]) -> dict[int, list[dict]]:
    by_year: dict[int, list[dict]] = defaultdict(list)
    for entry in entries:
        year = year_of(entry)
        if year:
            by_year[year].append(entry)
    return by_year


def emit_year_groups(entries: list[dict], lang: str, line_fn) -> list[str]:
    """Always fold by year so opening a section never dumps a wall of text."""
    lines: list[str] = []
    by_year = group_by_year(entries)
    for year in sorted(by_year.keys(), reverse=True):
        items = by_year[year]
        label = f"{year} · {len(items)}"
        lines += details_block(label, [line_fn(i, lang) for i in items])
    return lines


def emit_list(entries: list[dict], lang: str, line_fn) -> list[str]:
    if len(entries) <= FLAT_LIMIT:
        return [line_fn(i, lang) for i in entries]
    return emit_year_groups(entries, lang, line_fn)


def decade_bucket(year: int) -> str:
    if year >= 2020:
        return "2020–2022"
    if year >= 2010:
        return "2010s"
    if year >= 2000:
        return "2000s"
    return "1970s–1990s"


def emit_decades(entries: list[dict], lang: str, line_fn) -> list[str]:
    by_decade: dict[str, list[dict]] = defaultdict(list)
    order = ["2020–2022", "2010s", "2000s", "1970s–1990s"]
    for entry in entries:
        by_decade[decade_bucket(year_of(entry))].append(entry)
    lines: list[str] = []
    for label in order:
        items = by_decade.get(label) or []
        if not items:
            continue
        lines += details_block(f"{label} · {len(items)}", [line_fn(i, lang) for i in items])
    return lines


def fold(summary: str, body_lines: list[str]) -> list[str]:
    return details_block(summary, body_lines)


def bold_teaser(entries: list[dict], n: int = 3) -> str:
    names = []
    for entry in entries[:n]:
        text = " ".join(
            x
            for x in (
                entry.get("summary_zh"),
                entry.get("summary_en"),
                entry.get("name"),
            )
            if x
        )
        match = re.search(r"\*\*([^*]+)\*\*", text)
        names.append(match.group(1) if match else (entry.get("name") or "")[:20])
    return " · ".join(n for n in names if n)


def first_link(links: dict, keys: tuple[str, ...]) -> str | None:
    for key in keys:
        if links.get(key):
            return links[key]
    return None


def weight_url(entry: dict) -> str | None:
    links = entry.get("links") or {}
    for url in links.values():
        if url and "huggingface.co/" in url and "/datasets/" not in url:
            return url
    return first_link(links, WEIGHT_LINK_KEYS)


def is_open_weights(entry: dict) -> bool:
    return weight_url(entry) is not None


def hf_urls(entry: dict) -> set[str]:
    urls = set()
    for url in (entry.get("links") or {}).values():
        if url and "huggingface.co/" in url:
            urls.add(url.rstrip("/").lower())
    return urls


def first_org(entry: dict, lang: str) -> str:
    orgs = entry.get("orgs") or []
    if lang == "en":
        orgs = [o for o in orgs if not re.search(r"[\u4e00-\u9fff]", o)]
    if not orgs:
        return "—"
    text = orgs[0]
    if "，" in text:
        text = text.split("，", 1)[0]
    if "," in text:
        text = text.split(",", 1)[0]
    return text.strip() or "—"


def focus_labels(entry: dict, lang: str) -> str:
    tags = tags_of(entry)
    mapping = [
        ("multimodal", "多模态", "MM"),
        ("agent", "Agent", "Agent"),
        ("rag", "RAG", "RAG"),
        ("kg", "图谱", "KG"),
        ("benchmark", "评测", "Bench"),
    ]
    labels = []
    for tag, zh, en in mapping:
        if tag in tags:
            labels.append(zh if lang == "zh" else en)
    return " · ".join(labels) if labels else "—"


def compact_model_links(entry: dict, lang: str) -> str:
    links = entry.get("links") or {}
    paper = first_link(links, PAPER_LINK_KEYS)
    weight = weight_url(entry)
    code = first_link(links, CODE_LINK_KEYS)
    data = first_link(links, ("数据集", "数据", "Dataset", "Data"))
    labels = {
        "zh": ("论文", "权重", "代码", "数据"),
        "en": ("Paper", "Weights", "Code", "Data"),
    }[lang]
    parts = []
    for url, label in ((paper, labels[0]), (weight, labels[1]), (code, labels[2]), (data, labels[3])):
        if url:
            parts.append(f"[{label}]({url})")
    return " · ".join(parts) if parts else "—"


def classify_items(items: list[dict]) -> dict[str, list[dict]]:
    buckets: dict[str, list[dict]] = defaultdict(list)
    for entry in published(items):
        kind = entry.get("type")
        tags = tags_of(entry)
        year = year_of(entry)
        if kind == "news":
            buckets["news"].append(entry)
        elif kind == "survey":
            buckets["survey"].append(entry)
        elif kind == "dataset":
            buckets["dataset"].append(entry)
        elif kind == "model_hf":
            buckets["model_hf"].append(entry)
        elif kind == "resource":
            historical = "history" in tags or year < 2023
            if historical:
                buckets["history"].append(entry)
            elif "model" in tags:
                if "general-medical" in tags:
                    buckets["model_general"].append(entry)
                else:
                    buckets["model_tcm"].append(entry)
            else:
                placed = False
                for name, pred in PAPER_CATEGORY_RULES:
                    if pred(tags):
                        buckets[name].append(entry)
                        placed = True
                        break
                if not placed:
                    buckets["method"].append(entry)
    for key in buckets:
        buckets[key].sort(key=lambda x: (year_of(x), x.get("date") or "", x.get("name") or ""), reverse=True)
    return buckets


def counts_line(buckets: dict[str, list[dict]], lang: str) -> str:
    n_models = len(buckets["model_tcm"]) + len(buckets["model_general"]) + len(buckets["model_hf"])
    n_papers = sum(len(buckets[k]) for k in ("agent", "multimodal", "rag_kg", "eval", "method", "history"))
    stats = [
        (len(buckets["news"]), "新闻", "news"),
        (n_models, "模型", "models"),
        (len(buckets["survey"]), "综述", "surveys"),
        (len(buckets["dataset"]), "数据集", "datasets"),
        (n_papers, "论文/方法", "papers"),
    ]
    if lang == "zh":
        return " · ".join(f"**{n}** {label}" for n, label, _ in stats)
    return " · ".join(f"**{n}** {en}" for n, _, en in stats)


def catalog_index(buckets: dict[str, list[dict]]) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for items in buckets.values():
        for entry in items:
            if entry.get("id"):
                out[entry["id"]] = entry
    return out


def takeaway_link(entry: dict | None, lang: str) -> str:
    if not entry:
        return "—"
    name = display_name(entry, lang)
    url = weight_url(entry) or first_link(entry.get("links") or {}, PAPER_LINK_KEYS + CODE_LINK_KEYS)
    return f"**[{name}]({url})**" if url else f"**{name}**"


def takeaway_block(buckets: dict[str, list[dict]], lang: str) -> list[str]:
    idx = catalog_index(buckets)
    n_open = sum(1 for e in buckets["model_tcm"] if is_open_weights(e))
    biancang = takeaway_link(idx.get("biancang"), lang)
    zhongjing = takeaway_link(idx.get("zhongjing"), lang)
    shizhen = takeaway_link(idx.get("shizhengpt"), lang)
    chattcm = takeaway_link(idx.get("chattcm"), lang)
    shennong = takeaway_link(idx.get("shennong-tcm-llm"), lang)
    xinghe = takeaway_link(idx.get("xinghe"), lang)
    ladder = takeaway_link(idx.get("tcm-ladder"), lang)
    linglan = takeaway_link(idx.get("linglan"), lang)

    if lang == "zh":
        return [
            "## 两分钟带走",
            "",
            f"1. **能复现的中医权重大约 {n_open} 个**（点开[开源模型](#开源模型)）。新闻里的医院/公司大模型多数下不了，不要当实验底座。",
            "2. **2025 之后主线是多模态、Agent、评测**，不是再训一个 7B 问答模型。问诊工作流优先看 Agent / RAG，不要只 fine-tune。",
            "3. **考试分 ≠ 辨证/临床。** 执业试题测回忆；TCM-Ladder / LingLan / MTCMB 才接近任务评测。",
            "",
            "| 目标 | 先带走 | 为什么 |",
            "| --- | --- | --- |",
            f"| 单卡复现 | {biancang} 或 {zhongjing} | 论文 + 权重 + 代码齐 |",
            f"| 舌诊 / 四诊 | {shizhen} | Omni 开源，有配套数据 |",
            f"| 从数据训起 | {chattcm} / {shennong} | 预训练或指令数据公开 |",
            f"| 轻量本地跑 | {xinghe} | 2026，9B + GGUF |",
            f"| 做对比实验 | {ladder}、{linglan} | 任务定义清楚；更多在[数据集](#数据集) |",
            "| 写相关工作 | 2025–2026 scoping review | 先打开[综述](#综述)，不要从单篇模型论文起 |",
            "",
            "**别混：** 「仲景」有 ZhongJingGPT 与 AAAI CMtMedQA 两条线；名叫 TCM-Eval 的也不止一套。详解 [wiki/Getting-Started](wiki/Getting-Started.md)。",
            "",
        ]
    return [
        "## Two-minute takeaway",
        "",
        f"1. **About {n_open} TCM weights are actually downloadable** (open [Open models](#open-models)). Hospital/vendor models in the news usually are not baselines.",
        "2. **Since 2025 the main lines are multimodal, agents, and evaluation**—not another 7B chatbot. For inquiry workflows, start from Agent/RAG, not fine-tuning alone.",
        "3. **Exam scores ≠ pattern differentiation / clinic.** Licensing items test recall; TCM-Ladder / LingLan / MTCMB are closer to task eval.",
        "",
        "| Goal | Take this first | Why |",
        "| --- | --- | --- |",
        f"| Reproduce on one GPU | {biancang} or {zhongjing} | Paper + weights + code |",
        f"| Tongue / four diagnoses | {shizhen} | Open Omni + data |",
        f"| Train from data | {chattcm} / {shennong} | Pretrain or SFT released |",
        f"| Small local run | {xinghe} | 2026, 9B + GGUF |",
        f"| Compare models | {ladder}, {linglan} | Clear tasks; more under [Datasets](#datasets) |",
        "| Write related work | 2025–2026 scoping reviews | Open [Surveys](#surveys) first |",
        "",
        "**Don’t mix:** two “ZhongJing” lines (ZhongJingGPT vs AAAI CMtMedQA); more than one “TCM-Eval”. See [wiki/Getting-Started](wiki/Getting-Started.md).",
        "",
    ]


def model_table(entries: list[dict], lang: str) -> list[str]:
    if not entries:
        return []
    if lang == "zh":
        header = [
            "| 模型 | 年 | 特色 | 链接 |",
            "| --- | :---: | --- | --- |",
        ]
    else:
        header = [
            "| Model | Year | Focus | Links |",
            "| --- | :---: | --- | --- |",
        ]
    rows = []
    for entry in entries:
        name = display_name(entry, lang).replace("|", "/")
        year = str(year_of(entry) or "—")
        focus = focus_labels(entry, lang)
        links = compact_model_links(entry, lang)
        rows.append(f"| **{name}** | {year} | {focus} | {links} |")
    return header + rows


def build_model_section(buckets: dict[str, list[dict]], lang: str) -> list[str]:
    tcm = buckets["model_tcm"]
    general = buckets["model_general"]
    hf = buckets["model_hf"]
    open_tcm = [e for e in tcm if is_open_weights(e)]
    paper_tcm = [e for e in tcm if not is_open_weights(e)]

    title = "## 开源模型" if lang == "zh" else "## Open models"
    hint = (
        "上表是起步选择。这里是已核验可下载权重全集，以及论文/产品向与通用医疗底座。"
        if lang == "zh"
        else "The takeaway table is the starter set. Here is the full verified-weight list, plus paper/product and general-medical models."
    )
    lines = [title, "", hint, ""]
    if open_tcm:
        summary = (
            f"全部开源权重（{len(open_tcm)}）"
            if lang == "zh"
            else f"All open weights ({len(open_tcm)})"
        )
        lines += fold(summary, model_table(open_tcm, lang))

    if paper_tcm:
        summary = (
            f"全部中医模型 · 论文/产品向（{len(paper_tcm)}）"
            if lang == "zh"
            else f"All TCM models · paper/product ({len(paper_tcm)})"
        )
        lines += fold(summary, emit_list(paper_tcm, lang, format_resource_line))
    if general:
        summary = (
            f"通用中文医疗模型 · 常作底座或对照（{len(general)}）"
            if lang == "zh"
            else f"General Chinese medical models · bases/baselines ({len(general)})"
        )
        lines += fold(summary, emit_list(general, lang, format_resource_line))
    if hf:
        summary = (
            f"Hugging Face 多尺寸 / GGUF（{len(hf)}）"
            if lang == "zh"
            else f"Hugging Face extra sizes / GGUF ({len(hf)})"
        )
        lines += fold(summary, [format_dataset_line(e, lang) for e in hf])
    return lines


def build_news_section(news: list[dict], lang: str) -> list[str]:
    title = "## 新闻" if lang == "zh" else "## News"
    teaser = bold_teaser(news, 3)
    summary = (
        f"打开全部（{len(news)}）· 最新：{teaser}"
        if lang == "zh"
        else f"Open all ({len(news)}) · latest: {teaser}"
    )
    return [title, ""] + fold(summary, emit_list(news, lang, format_news_line))


def build_survey_section(surveys: list[dict], lang: str) -> list[str]:
    title = "## 综述" if lang == "zh" else "## Surveys"
    summary = (
        f"打开全部（{len(surveys)}）· 按年"
        if lang == "zh"
        else f"Open all ({len(surveys)}) · by year"
    )
    return [title, ""] + fold(summary, emit_list(surveys, lang, format_resource_line))


def build_paper_section(buckets: dict[str, list[dict]], lang: str) -> list[str]:
    specs = [
        ("agent", "Agent / 智能体", "Agents", "问诊工作流、多智能体、工具调用"),
        ("multimodal", "多模态 / 四诊", "Multimodal", "舌、面、脉与多模态融合"),
        ("rag_kg", "RAG / 知识图谱", "RAG / KG", "检索增强、医案与方剂图谱"),
        ("eval", "评测论文", "Evaluation papers", "基准与考试评估；下载评测集走「数据集」"),
        ("method", "其他方法", "Other methods", "处方、对齐、抽取等"),
        ("history", "历史锚点", "Historical anchors", "LLM 之前：专家系统、舌脉、本体"),
    ]
    title = "## 论文" if lang == "zh" else "## Papers"
    intro = (
        "模型不在这里。按方法点开一栏即可，不必按年份通读。"
        if lang == "zh"
        else "Models are not listed here. Open one method fold; no need to read by year."
    )
    lines = [title, "", intro, ""]
    for key, zh, en, hint in specs:
        items = buckets.get(key) or []
        if not items:
            continue
        heading = zh if lang == "zh" else en
        summary = f"{heading}（{len(items)}）· {hint}" if lang == "zh" else f"{heading} ({len(items)}) · {hint}"
        body = (
            emit_decades(items, lang, format_resource_line)
            if key == "history"
            else emit_list(items, lang, format_resource_line)
        )
        lines += fold(summary, body)
    return lines


def build_dataset_section(datasets: list[dict], lang: str) -> list[str]:
    title = "## 数据集" if lang == "zh" else "## Datasets"
    intro = (
        "按用途点开。对照说明见 [wiki/Datasets](wiki/Datasets.md) / [wiki/Benchmarks](wiki/Benchmarks.md)。"
        if lang == "zh"
        else "Open by use. Notes: [wiki/Datasets](wiki/Datasets.md) / [wiki/Benchmarks](wiki/Benchmarks.md)."
    )
    lines = [title, "", intro, ""]
    by_section: dict[str, list[dict]] = defaultdict(list)
    for entry in datasets:
        section = entry.get("section") or "其他"
        if section == HF_SECTION:
            continue
        by_section[section].append(entry)

    seen = set()
    for section in DATASET_SECTION_ORDER_ZH:
        entries = by_section.get(section) or []
        if not entries:
            continue
        seen.add(section)
        heading = section if lang == "zh" else SECTION_EN.get(section, section)
        summary = f"{heading}（{len(entries)}）" if lang == "zh" else f"{heading} ({len(entries)})"
        lines += fold(summary, [format_dataset_line(e, lang) for e in entries])
    for section, entries in by_section.items():
        if section in seen:
            continue
        heading = section if lang == "zh" else SECTION_EN.get(section, section)
        summary = f"{heading}（{len(entries)}）" if lang == "zh" else f"{heading} ({len(entries)})"
        lines += fold(summary, [format_dataset_line(e, lang) for e in entries])
    return lines


def footer(lang: str, portal: str) -> list[str]:
    if lang == "zh":
        return [
            "---",
            "",
            f"检索与标签筛选用[项目页]({PORTAL_ZH})。Wiki：[Home](wiki/Home.md) · [Getting Started](wiki/Getting-Started.md) · [Taxonomy](wiki/Taxonomy.md)。",
            "改条目请编辑 `data/catalog.yml`，然后 `python3 scripts/build_readme.py`（不要手改本 README）。",
            "",
        ]
    return [
        "---",
        "",
        f"Search and tag filters: [project page]({portal}). Wiki: [Home](wiki/Home.md) · [Getting Started](wiki/Getting-Started.md) · [Taxonomy](wiki/Taxonomy.md).",
        "Edit `data/catalog.yml`, then `python3 scripts/build_readme.py` (do not hand-edit this README).",
        "",
    ]


def build_readme(catalog: dict, lang: str, i18n_en: dict | None = None) -> str:
    meta = catalog.get("meta") or {}
    portal = meta.get("portal_url", DEFAULT_PORTAL)
    i18n_en = i18n_en or {}

    items = catalog.get("items") or []
    if lang == "en":
        items = [apply_i18n(i, i18n_en) for i in items]
    buckets = classify_items(items)

    if lang == "zh":
        header = [
            "# 🔥 开源中文医疗大模型",
            "",
            lang_switcher("zh"),
            "",
            badges(),
            "",
            f"中医（及部分中文医疗）大模型资源清单。{counts_line(buckets, 'zh')}。欢迎 [贡献](CONTRIBUTING.md)。",
            "",
            f"[项目页]({portal}) · [中文项目页]({PORTAL_ZH}) · [Wiki](wiki/Home.md) · [作者主页]({SITE_ZH})",
            "",
        ]
    else:
        header = [
            "# 🔥 Awesome TCM / Chinese Medical LLMs",
            "",
            lang_switcher("en"),
            "",
            badges(),
            "",
            f"Curated TCM (and related Chinese medical) LLM resources. {counts_line(buckets, 'en')}. [Contribute](CONTRIBUTING.md).",
            "",
            f"[Project page]({portal}) · [Wiki](wiki/Home.md) · [Author site]({SITE_EN})",
            "",
        ]

    lines = header
    lines += takeaway_block(buckets, lang)
    lines += build_model_section(buckets, lang)
    lines += build_news_section(buckets["news"], lang)
    lines += build_survey_section(buckets["survey"], lang)
    lines += build_paper_section(buckets, lang)
    lines += build_dataset_section(buckets["dataset"], lang)
    lines += footer(lang, portal)
    return "\n".join(lines).rstrip() + "\n"


def export_json(catalog: dict) -> dict:
    items = [
        i
        for i in catalog.get("items", [])
        if i.get("status", "published") == "published" and i.get("verified_at")
    ]
    return {
        "meta": catalog.get("meta", {}),
        "updated_at": (catalog.get("meta") or {}).get("updated_at"),
        "items": items,
    }


def _wiki_list(entries: list[dict], lang: str = "zh") -> list[str]:
    return [format_resource_line(i, lang) for i in entries]


def build_wiki_models(buckets: dict[str, list[dict]]) -> str:
    tcm = buckets["model_tcm"]
    general = buckets["model_general"]
    hf = buckets["model_hf"]
    open_tcm = [e for e in tcm if is_open_weights(e)]
    paper_tcm = [e for e in tcm if not is_open_weights(e)]
    lines = [
        "# Models",
        "",
        "本页是 README [开源模型](../README.md#开源模型) 的展开版：先给选型原则，再给完整表。",
        "",
        "## 怎么选",
        "",
        "| 场景 | 优先看 |",
        "| --- | --- |",
        "| 本地推理 / 复现论文 | 开源权重 + 代码 + 配套数据 |",
        "| 舌诊 / 四诊 | 标签含 `multimodal` 的模型（如 ShizhenGPT、TongueVLM） |",
        "| 问诊工作流 | `agent` 或配套 GraphRAG 系统，而不是单模型 |",
        "| 当底座继续微调 | 同系列 Base / Instruct，以及通用中文医疗模型 |",
        "| 只做对照实验 | 通用中文医疗栏（华佗、孙思邈等） |",
        "",
        f"中医专用 {len(tcm)} · 其中开源权重 {len(open_tcm)} · 通用医疗 {len(general)} · HF 精选 {len(hf)}。",
        "",
        "## 开源权重",
        "",
    ]
    lines += model_table(open_tcm, "zh")
    lines += ["", "## 论文或产品向（无公开权重）", ""]
    lines += _wiki_list(paper_tcm) or ["（无）"]
    lines += ["", "## 通用中文医疗模型", ""]
    lines += _wiki_list(general)
    lines += ["", "## Hugging Face 精选", ""]
    for entry in hf:
        lines.append(format_dataset_line(entry, "zh"))
    lines += ["", "返回 [[Home]] · 分类法见 [[Taxonomy]]。", ""]
    return "\n".join(lines)


def build_wiki_datasets(buckets: dict[str, list[dict]]) -> str:
    datasets = buckets["dataset"]
    by_section: dict[str, list[dict]] = defaultdict(list)
    for entry in datasets:
        section = entry.get("section") or "其他"
        if section == HF_SECTION:
            continue
        by_section[section].append(entry)
    lines = [
        "# Datasets",
        "",
        "数据集按用途分栏，与 README [数据集](../README.md#数据集) 同源。评测基准的任务对照见 [[Benchmarks]]。",
        "",
    ]
    for section in DATASET_SECTION_ORDER_ZH:
        entries = by_section.get(section) or []
        if not entries:
            continue
        lines += [f"## {section}", ""]
        for entry in entries:
            blurb = entry.get("summary_zh") or ""
            line = format_dataset_line(entry, "zh")
            if blurb and blurb not in line:
                line = f"{line} — {blurb}"
            lines.append(line)
        lines.append("")
    extra = [s for s in by_section if s not in DATASET_SECTION_ORDER_ZH]
    for section in extra:
        lines += [f"## {section}", ""]
        for entry in by_section[section]:
            lines.append(format_dataset_line(entry, "zh"))
        lines.append("")
    lines += ["返回 [[Home]]。", ""]
    return "\n".join(lines)


def build_wiki_benchmarks(buckets: dict[str, list[dict]]) -> str:
    bench_ds = [
        e
        for e in buckets["dataset"]
        if (e.get("section") == "评测基准") or "benchmark" in tags_of(e)
    ]
    bench_papers = buckets["eval"]
    lines = [
        "# Benchmarks",
        "",
        "把「可下载的评测集」和「评测论文」分开，避免和模型论文混在一起。",
        "",
        "## 评测集",
        "",
    ]
    for entry in bench_ds:
        lines.append(format_dataset_line(entry, "zh"))
    lines += ["", "## 评测与评估论文", ""]
    lines += _wiki_list(bench_papers)
    lines += [
        "",
        "## 阅读提示",
        "",
        "- 名称相近不一定是同一套：例如存在多个 **TCM-Eval**。",
        "- 考试类（执业医师 / 考研）测的是知识回忆，不等于临床辨证能力。",
        "- 多模态基准（TCM-Ladder、舌象集）需要看输入模态是否与模型匹配。",
        "",
        "返回 [[Home]] · 模型见 [[Models]]。",
        "",
    ]
    return "\n".join(lines)


def write_wiki_generated(buckets: dict[str, list[dict]]) -> None:
    WIKI_DIR.mkdir(exist_ok=True)
    mapping = {
        "Models.md": build_wiki_models(buckets),
        "Datasets.md": build_wiki_datasets(buckets),
        "Benchmarks.md": build_wiki_benchmarks(buckets),
    }
    for name, text in mapping.items():
        (WIKI_DIR / name).write_text(text, encoding="utf-8")


def main() -> None:
    if not CATALOG_YML.exists():
        print(f"Missing {CATALOG_YML}", file=sys.stderr)
        sys.exit(1)
    catalog = yaml.safe_load(CATALOG_YML.read_text(encoding="utf-8"))
    i18n_en = load_i18n_en()
    missing = [
        i["id"]
        for i in catalog.get("items", [])
        if i.get("status", "published") == "published" and i["id"] not in i18n_en
    ]
    README_ZH.write_text(build_readme(catalog, "zh"), encoding="utf-8")
    README_EN.write_text(build_readme(catalog, "en", i18n_en), encoding="utf-8")
    payload = export_json(catalog)
    CATALOG_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    zh_items = catalog.get("items") or []
    write_wiki_generated(classify_items(zh_items))
    msg = (
        f"Wrote {README_ZH.relative_to(ROOT)}, {README_EN.relative_to(ROOT)}, "
        f"{CATALOG_JSON.relative_to(ROOT)}, and wiki/{{Models,Datasets,Benchmarks}}.md "
        f"({len(payload['items'])} items; i18n_en={len(i18n_en)})"
    )
    print(msg)
    if missing:
        print(
            f"WARNING: missing English i18n for {len(missing)} ids: {', '.join(missing[:12])}"
            + ("..." if len(missing) > 12 else ""),
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
