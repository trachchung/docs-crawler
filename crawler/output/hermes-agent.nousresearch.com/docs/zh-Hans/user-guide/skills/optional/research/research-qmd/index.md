<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd -->

本页总览
Search personal knowledge bases, notes, docs, and meeting transcripts locally using qmd — a hybrid retrieval engine with BM25, vector search, and LLM reranking. Supports CLI and MCP integration.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#skill-metadata "Skill metadata的直接链接")  
| Source  | Optional — install with `hermes skills install official/research/qmd`  |  
| --- | --- |  
| Path  | `optional-skills/research/qmd`  |  
| Version  | `1.0.0`  |  
| Author  | Hermes Agent + Teknium  |  
| License  | MIT  |  
| Platforms  | macos, linux  |  
| Tags  |  `Search`, `Knowledge-Base`, `RAG`, `Notes`, `MCP`, `Local-AI`  |  
| Related skills  |  [`obsidian`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/note-taking/note-taking-obsidian), [`native-mcp`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/mcp/mcp-native-mcp), [`arxiv`](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/skills/bundled/research/research-arxiv)  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# QMD — Query Markup Documents
Local, on-device search engine for personal knowledge bases. Indexes markdown notes, meeting transcripts, documentation, and any text-based files, then provides hybrid search combining keyword matching, semantic understanding, and LLM-powered reranking — all running locally with no cloud dependencies.
Created by [Tobi Lütke](https://github.com/tobi/qmd). MIT licensed.
## When to Use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#when-to-use "When to Use的直接链接")
  * User asks to search their notes, docs, knowledge base, or meeting transcripts
  * User wants to find something across a large collection of markdown/text files
  * User wants semantic search ("find notes about X concept") not just keyword grep
  * User has already set up qmd collections and wants to query them
  * User asks to set up a local knowledge base or document search system
  * Keywords: "search my notes", "find in my docs", "knowledge base", "qmd"


## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#prerequisites "Prerequisites的直接链接")
### Node.js >= 22 (required)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#nodejs--22-required "Node.js >= 22 \(required\)的直接链接")

```
# Check versionnode--version# must be >= 22# macOS — install or upgrade via Homebrewbrew install node@22# Linux — use NodeSource or nvmcurl-fsSL https://deb.nodesource.com/setup_22.x |sudo-Ebash -sudoapt-getinstall-y nodejs# or with nvm:nvm install22&& nvm use 22
```

### SQLite with Extension Support (macOS only)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#sqlite-with-extension-support-macos-only "SQLite with Extension Support \(macOS only\)的直接链接")
macOS system SQLite lacks extension loading. Install via Homebrew:

```
brew install sqlite
```

### Install qmd[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#install-qmd "Install qmd的直接链接")

```
npminstall-g @tobilu/qmd# or with Bun:bun install-g @tobilu/qmd
```

First run auto-downloads 3 local GGUF models (~2GB total):  
| Model  | Purpose  | Size  |  
| --- | --- | --- |  
| embeddinggemma-300M-Q8_0  | Vector embeddings  | ~300MB  |  
| qwen3-reranker-0.6b-q8_0  | Result reranking  | ~640MB  |  
| qmd-query-expansion-1.7B  | Query expansion  | ~1.1GB  |  
### Verify Installation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#verify-installation "Verify Installation的直接链接")

```
qmd --versionqmd status
```

## Quick Reference[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#quick-reference "Quick Reference的直接链接")  
| Command  | What It Does  | Speed  |  
| --- | --- | --- |  
| `qmd search "query"`  | BM25 keyword search (no models)  | ~0.2s  |  
| `qmd vsearch "query"`  | Semantic vector search (1 model)  | ~3s  |  
| `qmd query "query"`  | Hybrid + reranking (all 3 models)  | ~2-3s warm, ~19s cold  |  
| `qmd get <docid>`  | Retrieve full document content  | instant  |  
| `qmd multi-get "glob"`  | Retrieve multiple files  | instant  |  
| `qmd collection add <path> --name <n>`  | Add a directory as a collection  | instant  |  
| `qmd context add <path> "description"`  | Add context metadata to improve retrieval  | instant  |  
| `qmd embed`  | Generate/update vector embeddings  | varies  |  
| `qmd status`  | Show index health and collection info  | instant  |  
| `qmd mcp`  | Start MCP server (stdio)  | persistent  |  
| `qmd mcp --http --daemon`  | Start MCP server (HTTP, warm models)  | persistent  |  
## Setup Workflow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#setup-workflow "Setup Workflow的直接链接")
### 1. Add Collections[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#1-add-collections "1. Add Collections的直接链接")
Point qmd at directories containing your documents:

```
# Add a notes directoryqmd collection add ~/notes --name notes# Add project docsqmd collection add ~/projects/myproject/docs --name project-docs# Add meeting transcriptsqmd collection add ~/meetings --name meetings# List all collectionsqmd collection list
```

### 2. Add Context Descriptions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#2-add-context-descriptions "2. Add Context Descriptions的直接链接")
Context metadata helps the search engine understand what each collection contains. This significantly improves retrieval quality:

```
qmd context add qmd://notes "Personal notes, ideas, and journal entries"qmd context add qmd://project-docs "Technical documentation for the main project"qmd context add qmd://meetings "Meeting transcripts and action items from team syncs"
```

### 3. Generate Embeddings[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#3-generate-embeddings "3. Generate Embeddings的直接链接")

```
qmd embed
```

This processes all documents in all collections and generates vector embeddings. Re-run after adding new documents or collections.
### 4. Verify[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#4-verify "4. Verify的直接链接")

```
qmd status   # shows index health, collection stats, model info
```

## Search Patterns[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#search-patterns "Search Patterns的直接链接")
### Fast Keyword Search (BM25)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#fast-keyword-search-bm25 "Fast Keyword Search \(BM25\)的直接链接")
Best for: exact terms, code identifiers, names, known phrases. No models loaded — near-instant results.

```
qmd search "authentication middleware"qmd search "handleError async"
```

### Semantic Vector Search[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#semantic-vector-search "Semantic Vector Search的直接链接")
Best for: natural language questions, conceptual queries. Loads embedding model (~3s first query).

```
qmd vsearch "how does the rate limiter handle burst traffic"qmd vsearch "ideas for improving onboarding flow"
```

### Hybrid Search with Reranking (Best Quality)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#hybrid-search-with-reranking-best-quality "Hybrid Search with Reranking \(Best Quality\)的直接链接")
Best for: important queries where quality matters most. Uses all 3 models — query expansion, parallel BM25+vector, reranking.

```
qmd query "what decisions were made about the database migration"
```

### Structured Multi-Mode Queries[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#structured-multi-mode-queries "Structured Multi-Mode Queries的直接链接")
Combine different search types in a single query for precision:

```
# BM25 for exact term + vector for conceptqmd query $'lex: rate limiter\nvec: how does throttling work under load'# With query expansionqmd query $'expand: database migration plan\nlex: "schema change"'
```

### Query Syntax (lex/BM25 mode)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#query-syntax-lexbm25-mode "Query Syntax \(lex/BM25 mode\)的直接链接")  
| Syntax  | Effect  | Example  |  
| --- | --- | --- |  
| `term`  | Prefix match  |  `perf` matches "performance"  |  
| `"phrase"`  | Exact phrase  | `"rate limiter"`  |  
| `-term`  | Exclude term  | `performance -sports`  |  
### HyDE (Hypothetical Document Embeddings)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#hyde-hypothetical-document-embeddings "HyDE \(Hypothetical Document Embeddings\)的直接链接")
For complex topics, write what you expect the answer to look like:

```
qmd query $'hyde: The migration plan involves three phases. First, we add the new columns without dropping the old ones. Then we backfill data. Finally we cut over and remove legacy columns.'
```

### Scoping to Collections[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#scoping-to-collections "Scoping to Collections的直接链接")

```
qmd search "query"--collection notesqmd query "query"--collection project-docs
```

### Output Formats[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#output-formats "Output Formats的直接链接")

```
qmd search "query"--json# JSON output (best for parsing)qmd search "query"--limit5# Limit resultsqmd get "#abc123"# Get by document IDqmd get "path/to/file.md"# Get by file pathqmd get "file.md:50"-l100# Get specific line rangeqmd multi-get "journals/*.md"--json# Batch retrieve by glob
```

## MCP Integration (Recommended)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#mcp-integration-recommended "MCP Integration \(Recommended\)的直接链接")
qmd exposes an MCP server that provides search tools directly to Hermes Agent via the native MCP client. This is the preferred integration — once configured, the agent gets qmd tools automatically without needing to load this skill.
### Option A: Stdio Mode (Simple)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#option-a-stdio-mode-simple "Option A: Stdio Mode \(Simple\)的直接链接")
Add to `~/.hermes/config.yaml`:

```
mcp_servers:qmd:command:"qmd"args:["mcp"]timeout:30connect_timeout:45
```

This registers tools: `mcp_qmd_search`, `mcp_qmd_vsearch`, `mcp_qmd_deep_search`, `mcp_qmd_get`, `mcp_qmd_status`.
**Tradeoff:** Models load on first search call (~19s cold start), then stay warm for the session. Acceptable for occasional use.
### Option B: HTTP Daemon Mode (Fast, Recommended for Heavy Use)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#option-b-http-daemon-mode-fast-recommended-for-heavy-use "Option B: HTTP Daemon Mode \(Fast, Recommended for Heavy Use\)的直接链接")
Start the qmd daemon separately — it keeps models warm in memory:

```
# Start daemon (persists across agent restarts)qmd mcp --http--daemon# Runs on http://localhost:8181 by default
```

Then configure Hermes Agent to connect via HTTP:

```
mcp_servers:qmd:url:"http://localhost:8181/mcp"timeout:30
```

**Tradeoff:** Uses ~2GB RAM while running, but every query is fast (~2-3s). Best for users who search frequently.
### Keeping the Daemon Running[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#keeping-the-daemon-running "Keeping the Daemon Running的直接链接")
#### macOS (launchd)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#macos-launchd "macOS \(launchd\)的直接链接")

```
cat> ~/Library/LaunchAgents/com.qmd.daemon.plist <<'EOF'<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"  "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>  <key>Label</key>  <string>com.qmd.daemon</string>  <key>ProgramArguments</key>  <array>    <string>qmd</string>    <string>mcp</string>    <string>--http</string>    <string>--daemon</string>  </array>  <key>RunAtLoad</key>  <true/>  <key>KeepAlive</key>  <true/>  <key>StandardOutPath</key>  <string>/tmp/qmd-daemon.log</string>  <key>StandardErrorPath</key>  <string>/tmp/qmd-daemon.log</string></dict></plist>EOFlaunchctl load ~/Library/LaunchAgents/com.qmd.daemon.plist
```

#### Linux (systemd user service)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#linux-systemd-user-service "Linux \(systemd user service\)的直接链接")

```
mkdir-p ~/.config/systemd/usercat> ~/.config/systemd/user/qmd-daemon.service <<'EOF'[Unit]Description=QMD MCP DaemonAfter=network.target[Service]ExecStart=qmd mcp --http --daemonRestart=on-failureRestartSec=10Environment=PATH=/usr/local/bin:/usr/bin:/bin[Install]WantedBy=default.targetEOFsystemctl --user daemon-reloadsystemctl --userenable--now qmd-daemonsystemctl --user status qmd-daemon
```

### MCP Tools Reference[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#mcp-tools-reference "MCP Tools Reference的直接链接")
Once connected, these tools are available as `mcp_qmd_*`:  
| MCP Tool  | Maps To  | Description  |  
| --- | --- | --- |  
| `mcp_qmd_search`  | `qmd search`  | BM25 keyword search  |  
| `mcp_qmd_vsearch`  | `qmd vsearch`  | Semantic vector search  |  
| `mcp_qmd_deep_search`  | `qmd query`  | Hybrid search + reranking  |  
| `mcp_qmd_get`  | `qmd get`  | Retrieve document by ID or path  |  
| `mcp_qmd_status`  | `qmd status`  | Index health and stats  |  
The MCP tools accept structured JSON queries for multi-mode search:

```
"searches":[{"type":"lex","query":"authentication middleware"},{"type":"vec","query":"how user login is verified"}"collections":["project-docs"],"limit":10
```

## CLI Usage (Without MCP)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#cli-usage-without-mcp "CLI Usage \(Without MCP\)的直接链接")
When MCP is not configured, use qmd directly via terminal:

```
terminal(command="qmd query 'what was decided about the API redesign' --json", timeout=30)
```

For setup and management tasks, always use terminal:

```
terminal(command="qmd collection add ~/Documents/notes --name notes")terminal(command="qmd context add qmd://notes 'Personal research notes and ideas'")terminal(command="qmd embed")terminal(command="qmd status")
```

## How the Search Pipeline Works[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#how-the-search-pipeline-works "How the Search Pipeline Works的直接链接")
Understanding the internals helps choose the right search mode:
  1. **Query Expansion** — A fine-tuned 1.7B model generates 2 alternative queries. The original gets 2x weight in fusion.
  2. **Parallel Retrieval** — BM25 (SQLite FTS5) and vector search run simultaneously across all query variants.
  3. **RRF Fusion** — Reciprocal Rank Fusion (k=60) merges results. Top-rank bonus: #1 gets +0.05, #2-3 get +0.02.
  4. **LLM Reranking** — qwen3-reranker scores top 30 candidates (0.0-1.0).
  5. **Position-Aware Blending** — Ranks 1-3: 75% retrieval / 25% reranker. Ranks 4-10: 60/40. Ranks 11+: 40/60 (trusts reranker more for long tail).


**Smart Chunking:** Documents are split at natural break points (headings, code blocks, blank lines) targeting ~900 tokens with 15% overlap. Code blocks are never split mid-block.
## Best Practices[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#best-practices "Best Practices的直接链接")
  1. **Always add context descriptions** — `qmd context add` dramatically improves retrieval accuracy. Describe what each collection contains.
  2. **Re-embed after adding documents** — `qmd embed` must be re-run when new files are added to collections.
  3. **Use`qmd search` for speed** — when you need fast keyword lookup (code identifiers, exact names), BM25 is instant and needs no models.
  4. **Use`qmd query` for quality** — when the question is conceptual or the user needs the best possible results, use hybrid search.
  5. **Prefer MCP integration** — once configured, the agent gets native tools without needing to load this skill each time.
  6. **Daemon mode for frequent users** — if the user searches their knowledge base regularly, recommend the HTTP daemon setup.
  7. **First query in structured search gets 2x weight** — put the most important/certain query first when combining lex and vec.


## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#troubleshooting "Troubleshooting的直接链接")
### "Models downloading on first run"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#models-downloading-on-first-run ""Models downloading on first run"的直接链接")
Normal — qmd auto-downloads ~2GB of GGUF models on first use. This is a one-time operation.
### Cold start latency (~19s)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#cold-start-latency-19s "Cold start latency \(~19s\)的直接链接")
This happens when models aren't loaded in memory. Solutions:
  * Use HTTP daemon mode (`qmd mcp --http --daemon`) to keep warm
  * Use `qmd search` (BM25 only) when models aren't needed
  * MCP stdio mode loads models on first search, stays warm for session


### macOS: "unable to load extension"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#macos-unable-to-load-extension "macOS: "unable to load extension"的直接链接")
Install Homebrew SQLite: `brew install sqlite` Then ensure it's on PATH before system SQLite.
### "No collections found"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#no-collections-found ""No collections found"的直接链接")
Run `qmd collection add <path> --name <name>` to add directories, then `qmd embed` to index them.
### Embedding model override (CJK/multilingual)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#embedding-model-override-cjkmultilingual "Embedding model override \(CJK/multilingual\)的直接链接")
Set `QMD_EMBED_MODEL` environment variable for non-English content:

```
exportQMD_EMBED_MODEL="your-multilingual-model"
```

## Data Storage[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#data-storage "Data Storage的直接链接")
  * **Index & vectors:** `~/.cache/qmd/index.sqlite`
  * **Models:** Auto-downloaded to local cache on first run
  * **No cloud dependencies** — everything runs locally


## References[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#references "References的直接链接")
  * [GitHub: tobi/qmd](https://github.com/tobi/qmd)
  * [QMD Changelog](https://github.com/tobi/qmd/blob/main/CHANGELOG.md)


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#reference-full-skillmd)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#when-to-use)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#prerequisites)
    * [Node.js >= 22 (required)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#nodejs--22-required)
    * [SQLite with Extension Support (macOS only)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#sqlite-with-extension-support-macos-only)
    * [Install qmd](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#install-qmd)
    * [Verify Installation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#verify-installation)
  * [Quick Reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#quick-reference)
  * [Setup Workflow](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#setup-workflow)
    * [1. Add Collections](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#1-add-collections)
    * [2. Add Context Descriptions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#2-add-context-descriptions)
    * [3. Generate Embeddings](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#3-generate-embeddings)
  * [Search Patterns](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#search-patterns)
    * [Fast Keyword Search (BM25)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#fast-keyword-search-bm25)
    * [Semantic Vector Search](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#semantic-vector-search)
    * [Hybrid Search with Reranking (Best Quality)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#hybrid-search-with-reranking-best-quality)
    * [Structured Multi-Mode Queries](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#structured-multi-mode-queries)
    * [Query Syntax (lex/BM25 mode)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#query-syntax-lexbm25-mode)
    * [HyDE (Hypothetical Document Embeddings)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#hyde-hypothetical-document-embeddings)
    * [Scoping to Collections](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#scoping-to-collections)
    * [Output Formats](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#output-formats)
  * [MCP Integration (Recommended)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#mcp-integration-recommended)
    * [Option A: Stdio Mode (Simple)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#option-a-stdio-mode-simple)
    * [Option B: HTTP Daemon Mode (Fast, Recommended for Heavy Use)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#option-b-http-daemon-mode-fast-recommended-for-heavy-use)
    * [Keeping the Daemon Running](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#keeping-the-daemon-running)
    * [MCP Tools Reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#mcp-tools-reference)
  * [CLI Usage (Without MCP)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#cli-usage-without-mcp)
  * [How the Search Pipeline Works](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#how-the-search-pipeline-works)
  * [Best Practices](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#best-practices)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#troubleshooting)
    * ["Models downloading on first run"](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#models-downloading-on-first-run)
    * [Cold start latency (~19s)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#cold-start-latency-19s)
    * [macOS: "unable to load extension"](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#macos-unable-to-load-extension)
    * ["No collections found"](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#no-collections-found)
    * [Embedding model override (CJK/multilingual)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#embedding-model-override-cjkmultilingual)
  * [Data Storage](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/optional/research/research-qmd#data-storage)


