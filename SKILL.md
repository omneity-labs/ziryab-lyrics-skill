---
name: ziryab-lyrics-api
description: Use this skill when Codex needs to call Omneity/Sawalni Ziryab rhyme and lyrics APIs for Sawtone-backed rhyme scoring, rhyme search, lyric word replacement suggestions, or lyric/stanza rhyme-structure analysis. Trigger for tasks mentioning Ziryab, Sawtone rhyme APIs, rhyme score, rhyme search, lyric replacements, songwriting suggestions, common-lyrics vocabulary, multilingual rhyme indexes, or lyrics scoring.
---

# Ziryab Lyrics API

## Core Workflow

Use Ziryab for live Sawtone-backed rhyme and lyric analysis through `https://api.sawalni.com`.

1. Keep credentials out of files. Read the bearer token from `ZIRYAB_API_TOKEN`; if a user provides a token inline, use it only for the current call and do not persist it.
2. Prefer the bundled script for repeatable calls:
   - `scripts/ziryab_client.py score --pair night light --pair time song --include-ipa --include-components`
   - `scripts/ziryab_client.py search rain --language eng_Latn --vocabulary common-lyrics --top-k 10 --include-ipa`
   - `scripts/ziryab_client.py suggest "I keep my heart above the rain" --target rain --include-components`
   - `scripts/ziryab_client.py lyric-score lyrics.txt --include-internal-rhymes`
3. Use `common-lyrics` for songwriting workflows unless the user asks for a broader or raw vocabulary.
4. Use `eng_Latn` by default. For multilingual work, pass an explicit supported index such as `fra_Latn`, `arb_Arab`, or `ary_Arab`.
5. When presenting results, summarize the useful candidates and include numeric scores only when they help the user compare options.

Note: This skill requires getting an API key at https://api.sawalni.com/api-keys and setting it as `ZIRYAB_API_TOKEN`. This can be done via editing ~/.zshrc and adding `export ZIRYAB_API_TOKEN=o-123..`.

## Capabilities

- **Rhyme scoring**: Score explicit word pairs and optionally request IPA and component scores.
- **Rhyme search**: Search vocabulary-backed rhyme candidates for a query word.
- **Lyric replacements**: Suggest context-aware replacements for a target word in a line.
- **Lyric scoring**: Analyze stanza rhyme scheme, line endings, overall score, and optional internal rhymes.

## API Reference

Read `references/api.md` when request/response fields, endpoint paths, or examples are needed.

## Implementation Notes

- The API is metered on input bytes; avoid sending unnecessary text.
- Vocabulary-backed routes require a supported language index.
- Treat failures as diagnostic: report status code, endpoint, and response body summary, but never print bearer tokens.
