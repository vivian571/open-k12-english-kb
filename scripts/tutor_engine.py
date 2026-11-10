#!/usr/bin/env python3
"""
Open K-12 English Heuristic Tutor CLI Engine
Powered by OmniEdu (arXiv:2609.23088) pedagogical framework.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DATA_DIR = ROOT / "data"

def load_data():
    topics = json.loads((DATA_DIR / "grammar_topics.json").read_text(encoding="utf-8"))
    cards = json.loads((DATA_DIR / "cards_samples.json").read_text(encoding="utf-8"))
    return topics, cards

def find_topic(query: str):
    topics, _ = load_data()
    q = query.lower()
    matches = []
    for ch in topics["chapters"]:
        for p in ch["points"]:
            if q in p["name"].lower() or q in ch["chapter_name"].lower():
                matches.append({"chapter": ch["chapter_name"], "point": p})
    return matches

def main():
    parser = argparse.ArgumentParser(description="K-12 English Heuristic Tutor Engine")
    sub = parser.add_subparsers(dest="cmd")

    p_search = sub.add_parser("search", help="Search grammar knowledge graph")
    p_search.add_argument("query", help="Keyword like 时态, 介词, 宾语从句")

    p_plan = sub.add_parser("plan", help="Build OmniEdu scaffolding plan for English")
    p_plan.add_argument("--question", "-q", required=True, help="Question text")
    p_plan.add_argument("--attempt", "-a", default="", help="Student attempt")
    p_plan.add_argument("--grade", "-g", default="八年级/初二", help="Grade")
    p_plan.add_argument("--mode", "-m", default="auto", choices=["auto", "english_reading", "english_writing", "math_scaffold"])

    args = parser.parse_args()
    if args.cmd == "search":
        res = find_topic(args.query)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0

    if args.cmd == "plan":
        # Forward to omniedu-tutor bootstrap
        import subprocess
        cmd = [
            "bash",
            "/home/antigravity/.gemini/skills/omniedu-tutor/scripts/bootstrap.sh",
            "plan",
            "--question", args.question,
            "--attempt", args.attempt,
            "--grade", args.grade,
            "--mode", args.mode if args.mode != "auto" else "english_reading",
        ]
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if proc.returncode == 0:
            print(proc.stdout)
        else:
            print(f"Error: {proc.stderr}", file=sys.stderr)
            return 1
        return 0

    parser.print_help()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
