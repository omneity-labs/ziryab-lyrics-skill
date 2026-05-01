# ♪ Ziryab Lyrics API Skill

A specialized skill for interacting with the **Ziryab Rhymes & Lyrics API** by Omneity Labs. This skill enables advanced phonetic analysis, rhyme scoring, and songwriting assistance using Sawtone-backed embeddings.

## Overview

The Ziryab Lyrics API provides deep phonetic insights into lyrics and poetry. Unlike traditional rhyming dictionaries that rely on exact suffix matching, Ziryab uses machine learning models to score rhymes based on phonetic similarity across a wide array of languages.

## Who Is the real Ziryab?

Ziryab was a 9th-century musician, poet, and cultural innovator whose influence reached far beyond music.

After moving from Baghdad to Cordoba, he helped shape the artistic culture of al-Andalus, influencing musical style, performance, fashion, etiquette, and courtly taste.
This project tries to pay a modest tribute for his contributions to our common human heritage.

Learn more: [Wikipedia: Ziryab](https://en.wikipedia.org/wiki/Ziryab)

## Features

- **Rhyme Scoring**: Quantify the phonetic similarity between any two words.
- **Rhyme Search**: Find the best rhyming candidates from curated vocabularies like `common-lyrics`.
- **Lyric Replacements**: Get context-aware suggestions for words in a line that maintain rhyme and meter.
- **Full Lyric Analysis**: Analyze stanzas for rhyme schemes, internal rhymes, and average rhyme quality.

## Fun Ideas for Use

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

## Setup

1. **Get an API Key**: Visit [api.sawalni.com/api-keys](https://api.sawalni.com/api-keys).
2. **Set Environment Variable**:
   ```bash
   export ZIRYAB_API_TOKEN='your-token-here'
   ```
3. **Run the Client**:
   ```bash
   python scripts/ziryab_client.py search "fire" --language eng_Latn --top-k 5
   ```

## Commercial Use

Ziryab does not use copyrighted content and is safe for commercial use.

## Examples

### Theme Prompt: Pressure to Treasure

Listen: [From Pressure To Treasure on Suno](https://suno.com/s/LN71L19rTFgUqXZR)

![Pressure to Treasure example](./pressure%20to%20treasure.png)

### Easy Listening: Goblins in the Cellar

Listen: [Goblins in the cellar on Suno](https://suno.com/s/L4QKlsT07x45GT9g)

![Goblins in the Cellar example](./goblins%20in%20the%20cellar.jpeg)

### French Track Concept: Le Dernier Bal

Listen: [Le dernier bal on Suno](https://suno.com/s/x5lSMcYTJjVXdpg4)

![Le Dernier Bal example](./le%20dernier%20bal.png)

### French Rap: Cactus dans le Desert

Listen: [Cactus dans le desert on Suno](https://suno.com/s/QgVhx0AJu0XX1J0C)

![Cactus dans le Desert example](./cactus%20dans%20le%20desert.png)


### Writing Assistant Output

![Writing help example](./writing%20help.png)

## Install From GitHub

This repository is already the full package. It includes the prompt in `SKILL.md`, the implementation in `scripts/ziryab_client.py`, API notes in `references/api.md`, and Codex metadata in `agents/openai.yaml`.

Do not copy only `SKILL.md`. Clone the entire repository into the location your editor or agent expects.

Repository URL:

```bash
https://github.com/omneity-labs/ziryab-lyrics-skill
```

### 1. Codex

Install it as a personal Codex skill by cloning into your Codex skills directory:

```bash
git clone https://github.com/omneity-labs/ziryab-lyrics-skill ~/.codex/skills/ziryab-lyrics-api
```

Then set your API token:

```bash
export ZIRYAB_API_TOKEN='your-token-here'
```

Start a new Codex session. Codex can then load the skill from `~/.codex/skills/ziryab-lyrics-api` and use the bundled client script instead of needing pasted instructions.

### 2. Claude Code

Claude Code supports personal and project skill directories. For a personal install available in every project:

```bash
git clone https://github.com/omneity-labs/ziryab-lyrics-skill ~/.claude/skills/ziryab-lyrics-api
```

For a project-local install, clone it inside the repository you are working on:

```bash
git clone https://github.com/omneity-labs/ziryab-lyrics-skill .claude/skills/ziryab-lyrics-api
```

Then set your API token:

```bash
export ZIRYAB_API_TOKEN='your-token-here'
```

Open a new Claude Code session. Claude Code will discover the skill from `.claude/skills/...` or `~/.claude/skills/...`, and the bundled `scripts/ziryab_client.py` remains available to execute.

### 3. GitHub Copilot in VS Code or on GitHub

GitHub Copilot does **not** have a global skills folder like Codex or Claude Code. Copilot only reads repository instructions from the repository you have open.

That means the proper install location is inside the project where you want Copilot to use Ziryab. The cleanest setup is to vendor this repository into that project:

```bash
cd /path/to/your-project
git submodule add https://github.com/omneity-labs/ziryab-lyrics-skill .ai/ziryab-lyrics-api
```

Then add a repository instruction file at `.github/copilot-instructions.md` or an `AGENTS.md` file in the project root that tells Copilot to:

- use `.ai/ziryab-lyrics-api/SKILL.md` for Ziryab workflow guidance
- run `.ai/ziryab-lyrics-api/scripts/ziryab_client.py` for live API calls
- read `.ai/ziryab-lyrics-api/references/api.md` when request or response details are needed

Once that project is open in VS Code or attached in Copilot Chat, Copilot can use the cloned repo directly from the workspace.

### 4. Cursor and Similar Repo-Scoped Editors

Cursor is also repo-scoped. It uses `.cursor/rules/*.md` or `.mdc` files, or a root `AGENTS.md`, rather than a global skill directory.

Clone this repository into the project where you want Cursor to use it:

```bash
cd /path/to/your-project
git submodule add https://github.com/omneity-labs/ziryab-lyrics-skill .ai/ziryab-lyrics-api
```

Then add either:

- a root `AGENTS.md` that points Cursor to `.ai/ziryab-lyrics-api/SKILL.md` and `.ai/ziryab-lyrics-api/scripts/ziryab_client.py`
- or a `.cursor/rules/ziryab-lyrics-api.mdc` rule that describes when to use the cloned skill repo

The important part is the same: clone the full repository into the active workspace so the editor can see both the instructions and the Python client.

### 5. MCP or Custom Wrappers

If you want tool-calling outside these editors, wrap `scripts/ziryab_client.py` in an MCP server or another thin adapter. The cloned repository already contains the logic you need; the wrapper only needs to expose it.
---
*Powered by Sawtone & Omneity Labs.*

Visit [Omneity Labs](https://omneitylabs.com)
