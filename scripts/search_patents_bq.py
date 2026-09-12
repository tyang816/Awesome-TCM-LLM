#!/usr/bin/env python3
"""Search Google Patents Public Data on BigQuery for TCM LLM / KG-QA / RAG filings.

Worldwide by design (CN, US, EP, WO, JP, KR, …). Needs a logged-in gcloud
account and a billing-enabled project:

    gcloud auth login
    gcloud config set project YOUR_PROJECT
    python3 scripts/search_patents_bq.py
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys

SQL = r"""
SELECT
  p.publication_number,
  p.country_code,
  p.publication_date,
  (SELECT t.text FROM UNNEST(p.title_localized) t
   WHERE t.language IN ('en', 'zh', 'ja', 'ko')
   LIMIT 1) AS title,
  ARRAY(
    SELECT a.name FROM UNNEST(p.assignee_harmonized) a LIMIT 3
  ) AS assignees
FROM `patents-public-data.patents.publications` p
WHERE p.publication_date >= @min_date
  AND (
    REGEXP_CONTAINS(
      LOWER(ARRAY_TO_STRING((SELECT ARRAY_AGG(t.text) FROM UNNEST(p.title_localized) t), ' ')),
      r'(traditional chinese medicine|\btcm\b|chinese medicine|acupuncture|tuina|kampo|한의학|漢方|中医|中藥|中药)'
    )
    OR REGEXP_CONTAINS(
      LOWER(ARRAY_TO_STRING((SELECT ARRAY_AGG(a.text) FROM UNNEST(p.abstract_localized) a), ' ')),
      r'(traditional chinese medicine|\btcm\b|chinese medicine|acupuncture|kampo|漢方|中医)'
    )
  )
  AND (
    REGEXP_CONTAINS(
      LOWER(ARRAY_TO_STRING((SELECT ARRAY_AGG(t.text) FROM UNNEST(p.title_localized) t), ' ')),
      r'(large language model|language model|\bllm\b|chatgpt|generative ai|retrieval.?augmented|\brag\b|knowledge graph|知识图谱|大语言|大模型)'
    )
    OR REGEXP_CONTAINS(
      LOWER(ARRAY_TO_STRING((SELECT ARRAY_AGG(a.text) FROM UNNEST(p.abstract_localized) a), ' ')),
      r'(large language model|\bllm\b|chatgpt|retrieval.?augmented|\brag\b|knowledge graph|知识图谱|大语言|大模型)'
    )
  )
ORDER BY p.publication_date DESC
LIMIT @limit
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-date", default="20230101", help="YYYYMMDD inclusive")
    parser.add_argument("--limit", type=int, default=80)
    parser.add_argument("--print-sql", action="store_true")
    args = parser.parse_args()

    rendered = (
        SQL.replace("@min_date", args.min_date).replace("@limit", str(args.limit))
    )
    if args.print_sql:
        print(rendered)
        return 0

    bq = shutil.which("bq")
    if not bq:
        print("bq not found. Install Google Cloud SDK, then rerun.", file=sys.stderr)
        print(rendered)
        return 1

    cmd = [
        bq,
        "query",
        "--use_legacy_sql=false",
        "--format=pretty",
        "--max_rows",
        str(args.limit),
        "--parameter",
        f"min_date:INT64:{args.min_date}",
        "--parameter",
        f"limit:INT64:{args.limit}",
        SQL,
    ]
    try:
        proc = subprocess.run(cmd, check=False)
    except OSError as exc:
        print(f"failed to run bq: {exc}", file=sys.stderr)
        print(rendered)
        return 1
    if proc.returncode != 0:
        print(
            "BigQuery query failed. Run `gcloud auth login` and "
            "`gcloud config set project YOUR_PROJECT`, then retry.\n"
            "SQL is also available via --print-sql.",
            file=sys.stderr,
        )
        return proc.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
