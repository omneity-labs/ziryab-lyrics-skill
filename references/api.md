# Ziryab Rhymes & Lyrics API Reference

Base URL: `https://api.sawalni.com`

Authentication: `Authorization: Bearer <token>`

Set an explicit `User-Agent`; Python's default urllib signature may be blocked by the edge WAF.

Supported vocabulary tiers:

| Tier | Use |
| --- | --- |
| `raw` | Full Wikilangs vocabulary for the language |
| `common` | Higher-frequency vocabulary subset |
| `common-lyrics` | Songwriting-tuned vocabulary subset |

Supported language examples: `eng_Latn`, `fra_Latn`, `arb_Arab`, `ary_Arab`.

## Rhyme Score

`POST /v1/language/rhyme/score`

Request:

```json
{
  "pairs": [["night", "light"], ["time", "song"]],
  "language": "eng_Latn",
  "include_ipa": true,
  "include_components": true
}
```

Response includes `language`, `results`, and `usage`. Each result includes `a`, `b`, `rhyme_score`, and optionally `phonetic_cosine`, `ipa_a`, `ipa_b`.

## Rhyme Search

`POST /v1/language/rhyme/search`

Request:

```json
{
  "query": "rain",
  "language": "eng_Latn",
  "vocabulary": "common-lyrics",
  "top_k": 5,
  "include_ipa": true
}
```

Response includes `language`, `query`, `results`, and `usage`. Each result includes `word`, `rhyme_score`, and may include `syllables` and `ipa`.

## Lyric Replacement Suggestions

`POST /v1/language/lyrics/suggest-replacements`

Request:

```json
{
  "line": "I keep my heart above the rain",
  "target": "rain",
  "language": "eng_Latn",
  "vocabulary": "common-lyrics",
  "top_k": 5,
  "include_components": true
}
```

Response includes `language`, `model`, `target`, `suggestions`, and `usage`. Observed suggestion fields include `word`, `total_score`, `rhyme_score`, `context_score`, `meter_score`, `frequency_score`, `frequency`, `zipf`, `rank`, and `syllables`.

## Lyric Score

`POST /v1/language/lyrics/score`

Request:

```json
{
  "text": "I walk alone beneath the night\nI chase the moon and lose the light",
  "language": "eng_Latn",
  "rhyme_threshold": 0.64,
  "include_internal_rhymes": true
}
```

Observed response fields include `language`, `model`, `scheme`, `line_endings`, `average_end_rhyme`, `pairs`, `internal_rhymes`, and `usage`.
