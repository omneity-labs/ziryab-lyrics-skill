#!/usr/bin/env python3
"""CLI client for the Ziryab Rhymes & Lyrics API.

Reads the bearer token from ZIRYAB_API_TOKEN. Never hard-code credentials here.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


BASE_URL = "https://api.sawalni.com"
TOKEN_ENV = "ZIRYAB_API_TOKEN"


class ZiryabError(RuntimeError):
    pass


def post_json(endpoint: str, payload: dict[str, Any], timeout: int = 30) -> dict[str, Any]:
    token = os.environ.get(TOKEN_ENV)
    if not token:
        raise ZiryabError(f"Missing {TOKEN_ENV}; set it for the current command.")

    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        BASE_URL + endpoint,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "ZiryabSkill/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise ZiryabError(f"HTTP {exc.code} for {endpoint}: {detail[:1000]}") from exc
    except urllib.error.URLError as exc:
        raise ZiryabError(f"Request failed for {endpoint}: {exc}") from exc


def print_json(data: dict[str, Any]) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))


def cmd_score(args: argparse.Namespace) -> None:
    pairs = args.pair or []
    payload = {
        "pairs": pairs,
        "language": args.language,
        "include_ipa": args.include_ipa,
        "include_components": args.include_components,
    }
    print_json(post_json("/v1/language/rhyme/score", payload, timeout=args.timeout))


def cmd_search(args: argparse.Namespace) -> None:
    payload = {
        "query": args.query,
        "language": args.language,
        "vocabulary": args.vocabulary,
        "top_k": args.top_k,
        "include_ipa": args.include_ipa,
    }
    print_json(post_json("/v1/language/rhyme/search", payload, timeout=args.timeout))


def cmd_suggest(args: argparse.Namespace) -> None:
    payload = {
        "line": args.line,
        "language": args.language,
        "vocabulary": args.vocabulary,
        "top_k": args.top_k,
        "include_components": args.include_components,
    }
    if args.target:
        payload["target"] = args.target
    print_json(post_json("/v1/language/lyrics/suggest-replacements", payload, timeout=args.timeout))


def cmd_lyric_score(args: argparse.Namespace) -> None:
    text = Path(args.text_file).read_text(encoding="utf-8") if args.text_file != "-" else sys.stdin.read()
    payload = {
        "text": text,
        "language": args.language,
        "rhyme_threshold": args.rhyme_threshold,
        "include_internal_rhymes": args.include_internal_rhymes,
    }
    print_json(post_json("/v1/language/lyrics/score", payload, timeout=args.timeout))


def add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--language", default="eng_Latn")
    parser.add_argument("--timeout", type=int, default=30)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Call the Ziryab Rhymes & Lyrics API.")
    sub = parser.add_subparsers(dest="command", required=True)

    score = sub.add_parser("score", help="Score one or more word pairs.")
    add_common(score)
    score.add_argument("--pair", nargs=2, action="append", metavar=("WORD_A", "WORD_B"), required=True)
    score.add_argument("--include-ipa", action="store_true")
    score.add_argument("--include-components", action="store_true")
    score.set_defaults(func=cmd_score)

    search = sub.add_parser("search", help="Search for rhyming words.")
    add_common(search)
    search.add_argument("query")
    search.add_argument("--vocabulary", default="common-lyrics", choices=["raw", "common", "common-lyrics"])
    search.add_argument("--top-k", type=int, default=10)
    search.add_argument("--include-ipa", action="store_true")
    search.set_defaults(func=cmd_search)

    suggest = sub.add_parser("suggest", help="Suggest replacements for a lyric line.")
    add_common(suggest)
    suggest.add_argument("line")
    suggest.add_argument("--target")
    suggest.add_argument("--vocabulary", default="common-lyrics", choices=["raw", "common", "common-lyrics"])
    suggest.add_argument("--top-k", type=int, default=10)
    suggest.add_argument("--include-components", action="store_true")
    suggest.set_defaults(func=cmd_suggest)

    lyric_score = sub.add_parser("lyric-score", help="Score stanza rhyme structure from a file or stdin.")
    add_common(lyric_score)
    lyric_score.add_argument("text_file", help="Path to text file, or '-' for stdin.")
    lyric_score.add_argument("--rhyme-threshold", type=float, default=0.64)
    lyric_score.add_argument("--include-internal-rhymes", action="store_true")
    lyric_score.set_defaults(func=cmd_lyric_score)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
        return 0
    except ZiryabError as exc:
        print(f"ziryab_client.py: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
