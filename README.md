# Ziryab Lyrics API Skill

A specialized skill for interacting with the **Ziryab Rhymes & Lyrics API** by Omneity Labs. This skill enables advanced phonetic analysis, rhyme scoring, and songwriting assistance using Sawtone-backed embeddings.

## 🚀 Overview

The Ziryab Lyrics API provides deep phonetic insights into lyrics and poetry. Unlike traditional rhyming dictionaries that rely on exact suffix matching, Ziryab uses machine learning models to score rhymes based on phonetic similarity across a wide array of languages.

## 🛠 Features

- **Rhyme Scoring**: Quantify the phonetic similarity between any two words.
- **Rhyme Search**: Find the best rhyming candidates from curated vocabularies like `common-lyrics`.
- **Lyric Replacements**: Get context-aware suggestions for words in a line that maintain rhyme and meter.
- **Full Lyric Analysis**: Analyze stanzas for rhyme schemes, internal rhymes, and average rhyme quality.

## 💡 Fun Ideas for Use

### 1. The "Lyric Polisher" Bot
Feed a rough draft of a song into Codex. Ask it to "Ziryab-analyze" the verses. It can identify where rhymes are weak (low `rhyme_score`) and suggest replacements that fit the mood but sound better together.

### 2. Multi-genre Songwriting Assistant
Switch vocabularies to see how suggestions change. Use `common-lyrics` for a natural pop feel, or use `raw` for more obscure, avant-garde poetry.

### 3. Cross-Language Rhyme Exploration
Ever wondered what rhymes with an English word in Arabic or French? Use the `search` endpoint across different language indices like `arb_Arab` or `fra_Latn` to find interesting cross-lingual phonetic matches.

### 4. Rap/Poetry Scheme Visualizer
Submit a full stanza to the `lyric-score` endpoint. Use the returned `scheme` and `internal_rhymes` data to generate a color-coded map of the rhyme structure, highlighting hidden internal rhymes that aren't immediately obvious.

### 5. Automatic Paraphraser that Rhymes
Ask Codex to rewrite a famous poem or song snippet while maintaining the original rhyme scheme. It can use `suggest-replacements` to find words that preserve the "sound" of the original while changing the meaning.

## ⚙️ Setup

1. **Get an API Key**: Visit [api.sawalni.com/api-keys](https://api.sawalni.com/api-keys).
2. **Set Environment Variable**:
   ```bash
   export ZIRYAB_API_TOKEN='your-token-here'
   ```
3. **Run the Client**:
   ```bash
   python scripts/ziryab_client.py search "fire" --language eng_Latn --top-k 5
   ```

---
*Powered by Sawtone & Omneity Labs.*

Visit (Omneity Labs)[https://omneitylabs.com]
