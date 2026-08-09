#!/usr/bin/env python3
"""Build README.md, README_EN.md, and data/catalog.json from data/catalog.yml."""

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

SITE_ZH = "https://tyang816.github.io/zh/"
SITE_EN = "https://tyang816.github.io/"
DEFAULT_PORTAL = "https://tyang816.github.io/projects/tcm/"
PORTAL_ZH = "https://tyang816.github.io/zh/projects/tcm/"

DATASET_SECTION_ORDER_ZH = [
    "公开资料整理",
    "原始书籍 / 预训练语料",
    "评测基准",
    "考试数据集",
    "指令/对话数据集",
    "知识图谱",
    "Hugging Face 开源模型（精选）",
    "语料/指令",
]

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
}


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
    for key in ("summary_en", "title_en", "name_en", "venue_en"):
        if patch.get(key) and not out.get(key):
            out[key] = patch[key]
    if patch.get("orgs_en"):
        out["orgs"] = list(patch["orgs_en"])
    return out


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
            # Fall back: strip leftover CJK from unmapped labels
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


def format_resource_line(entry: dict, lang: str) -> str:
    bits = ["-"]
    venue = entry.get("venue_en") if lang == "en" else None
    venue = venue or entry.get("venue")
    if venue:
        bits.append(f"[*{venue}*]")
    display_name = entry.get("name_en") if lang == "en" else None
    bits.append(f"**{display_name or entry['name']}**")
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


def build_readme(catalog: dict, lang: str, i18n_en: dict | None = None) -> str:
    meta = catalog.get("meta") or {}
    portal = meta.get("portal_url", DEFAULT_PORTAL)
    i18n_en = i18n_en or {}

    def localize(entry: dict) -> dict:
        return apply_i18n(entry, i18n_en) if lang == "en" else entry

    if lang == "zh":
        lines = [
            "# 🔥 开源中文医疗大模型",
            "",
            lang_switcher("zh"),
            "",
            badges(),
            "",
            "本仓库收集了开源中文医疗大模型（中医/西医）相关的资源，包括新闻、论文、模型、数据集等，欢迎大家贡献更多资源。",
            "",
            f"**相关链接**：[项目页]({portal}) · [中文项目页]({PORTAL_ZH}) · "
            f"[作者中文主页]({SITE_ZH}) · [Author site (EN)]({SITE_EN})",
            "",
            "> 项目页支持标签筛选与搜索，数据与本 README 同源（`data/catalog.yml`）。",
            "",
            "## 收录说明",
            "",
            "- 以中医药大模型、数据集、评测、知识图谱及相关研究为主；通用医疗条目使用 `general-medical` 标签标识。",
            "- “论文公开”“代码开源”“开放权重”和“数据开放”是不同状态；请以每个条目实际提供的链接为准。",
            "- 新闻和产品条目仅记录公开信息，收录不代表项目维护者对其效果、安全性或临床适用性的认可。",
            "",
            "> **医疗免责声明：** 本目录仅用于研究与信息索引，不构成医疗建议、诊断或治疗依据。临床使用须由合格专业人员独立评估。",
            "",
            "## 📰 新闻",
        ]
        res_h, data_h = "## 📚 资源", "## 📚 数据集"
    else:
        lines = [
            "# 🔥 Awesome TCM / Chinese Medical LLMs",
            "",
            lang_switcher("en"),
            "",
            badges(),
            "",
            "Curated open resources for Traditional Chinese Medicine (and related Chinese medical) LLMs — news, papers, models, benchmarks, and datasets. Contributions welcome.",
            "",
            f"**Links:** [Project page (EN)]({portal}) · [Project page (ZH)]({PORTAL_ZH}) · "
            f"[Author site (EN)]({SITE_EN}) · [Author site (ZH)]({SITE_ZH})",
            "",
            "> The project page supports search and tag filters. Data is sourced from the same `data/catalog.yml` as this README. English blurbs live in `data/i18n_en.yml`.",
            "",
            "## Inclusion and safety",
            "",
            "- The primary scope is TCM LLMs, datasets, benchmarks, knowledge graphs, and related research; broader medical entries carry the `general-medical` tag.",
            "- Paper availability, open-source code, open weights, and open datasets are distinct. Refer to the links attached to each entry.",
            "- News and product entries document public claims only; inclusion is not an endorsement of efficacy, safety, or clinical readiness.",
            "",
            "> **Medical disclaimer:** This catalog is for research and information discovery only. It is not medical advice and must not be used as a substitute for professional diagnosis or treatment.",
            "",
            "## 📰 News",
        ]
        res_h, data_h = "## 📚 Resources", "## 📚 Datasets"

    news = [
        localize(i)
        for i in catalog["items"]
        if i.get("type") == "news" and i.get("status", "published") == "published"
    ]
    news.sort(key=lambda x: x.get("date", ""), reverse=True)
    lines.extend(format_news_line(i, lang) for i in news)

    lines += ["", res_h]
    resources = [
        localize(i)
        for i in catalog["items"]
        if i.get("type") == "resource" and i.get("status", "published") == "published"
    ]
    by_year: dict[int, list] = defaultdict(list)
    for entry in resources:
        by_year[int(entry.get("year") or 0)].append(entry)
    for year in sorted(by_year.keys(), reverse=True):
        if year == 0:
            continue
        lines += ["", f"### {year}"]
        lines.extend(format_resource_line(i, lang) for i in by_year[year])

    surveys = [
        localize(i)
        for i in catalog["items"]
        if i.get("type") == "survey" and i.get("status", "published") == "published"
    ]
    if surveys:
        surveys.sort(key=lambda x: int(x.get("year") or 0), reverse=True)
        lines += ["", "## 📑 综述" if lang == "zh" else "## 📑 Surveys"]
        lines.extend(format_resource_line(i, lang) for i in surveys)

    lines += ["", data_h]
    datasets = [
        localize(i)
        for i in catalog["items"]
        if i.get("type") in ("dataset", "model_hf")
        and i.get("status", "published") == "published"
    ]
    by_section: dict[str, list] = defaultdict(list)
    for entry in datasets:
        by_section[entry.get("section") or "其他"].append(entry)

    seen = set()
    for section in DATASET_SECTION_ORDER_ZH:
        if section not in by_section:
            continue
        seen.add(section)
        title = section if lang == "zh" else SECTION_EN.get(section, section)
        lines += ["", f"### {title}"]
        for entry in by_section[section]:
            if lang == "en":
                item_title = entry.get("title_en") or entry.get("name")
            else:
                item_title = entry.get("title_zh") or entry["name"]
            lines.append(f"- {item_title}{format_links(entry.get('links'), lang)}")

    for section, entries in by_section.items():
        if section in seen:
            continue
        title = section if lang == "zh" else SECTION_EN.get(section, section)
        lines += ["", f"### {title}"]
        for entry in entries:
            if lang == "en":
                item_title = entry.get("title_en") or entry.get("name")
            else:
                item_title = entry.get("title_zh") or entry["name"]
            lines.append(f"- {item_title}{format_links(entry.get('links'), lang)}")

    if lang == "zh":
        lines += [
            "",
            "## 参与贡献",
            "",
            "请阅读 [贡献指南](CONTRIBUTING.md)。新增或修改条目时只编辑 `data/catalog.yml` 与对应英文翻译，再运行生成与校验脚本。",
            "",
            "## 引用与许可",
            "",
            "引用信息见 [`CITATION.cff`](CITATION.cff)。仓库代码与整理内容采用 [MIT License](LICENSE)。第三方论文、模型和数据仍受各自许可约束。",
        ]
    else:
        lines += [
            "",
            "## Contributing",
            "",
            "See the [contribution guide](CONTRIBUTING.md). Edit the catalog and matching English localization, then run the generation and validation commands before opening a PR.",
            "",
            "## Citation and license",
            "",
            "Citation metadata is available in [`CITATION.cff`](CITATION.cff). Repository code and curation are provided under the [MIT License](LICENSE); third-party papers, models, and datasets retain their own licenses.",
        ]
    lines.append("")
    return "\n".join(lines)


def export_json(catalog: dict) -> dict:
    items = [
        i
        for i in catalog.get("items", [])
        if i.get("status", "published") == "published" and i.get("verified_at")
    ]
    meta = dict(catalog.get("meta") or {})
    latest_verified = max((str(i.get("verified_at")) for i in items), default=None)
    if latest_verified:
        meta["updated_at"] = latest_verified
    return {
        "meta": meta,
        "updated_at": meta.get("updated_at"),
        "items": items,
    }


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
    msg = (
        f"Wrote {README_ZH.relative_to(ROOT)}, {README_EN.relative_to(ROOT)}, "
        f"and {CATALOG_JSON.relative_to(ROOT)} ({len(payload['items'])} items; "
        f"i18n_en={len(i18n_en)})"
    )
    print(msg)
    if missing:
        print(f"WARNING: missing English i18n for {len(missing)} ids: {', '.join(missing[:12])}"
              + ("..." if len(missing) > 12 else ""), file=sys.stderr)


if __name__ == "__main__":
    main()
