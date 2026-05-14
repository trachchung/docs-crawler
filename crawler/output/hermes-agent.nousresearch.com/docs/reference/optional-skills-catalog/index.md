<!-- Source: https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#__docusaurus_skipToContent_fallback)
On this page
Optional skills ship with hermes-agent under `optional-skills/` but are **not active by default**. Install them explicitly:

```
hermes skills install official/<category>/<skill>
```

For example:

```
hermes skills install official/blockchain/solanahermes skills install official/mlops/flash-attention
```

Each skill below links to a dedicated page with its full definition, setup, and usage.
To uninstall:

```
hermes skills uninstall <skill-name>
```

## autonomous-ai-agents[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#autonomous-ai-agents "Direct link to autonomous-ai-agents")  
| Skill  | Description  |  
| --- | --- |  
| Delegate coding tasks to Blackbox AI CLI agent. Multi-model agent with built-in judge that runs tasks through multiple LLMs and picks the best result. Requires the blackbox CLI and a Blackbox AI API key.  |  
| Configure and use Honcho memory with Hermes -- cross-session user modeling, multi-profile peer isolation, observation config, dialectic reasoning, session summaries, and context budget enforcement. Use when setting up Honcho, troubleshoo...  |  
## blockchain[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#blockchain "Direct link to blockchain")  
| Skill  | Description  |  
| --- | --- |  
| Read-only EVM client: wallets, tokens, gas across 8 chains.  |  
| Hyperliquid market data, account history, trade review.  |  
| Query Solana blockchain data with USD pricing — wallet balances, token portfolios with values, transaction details, NFTs, whale detection, and live network stats. Uses Solana RPC + CoinGecko. No API key required.  |  
## communication[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#communication "Direct link to communication")  
| Skill  | Description  |  
| --- | --- |  
| [**one-three-one-rule**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/communication/communication-one-three-one-rule)  | Structured decision-making framework for technical proposals and trade-off analysis. When the user faces a choice between multiple approaches (architecture decisions, tool selection, refactoring strategies, migration paths), this skill p...  |  
## creative[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#creative "Direct link to creative")  
| Skill  | Description  |  
| --- | --- |  
| Control Blender directly from Hermes via socket connection to the blender-mcp addon. Create 3D objects, materials, animations, and run arbitrary Blender Python (bpy) code. Use when user wants to create or modify anything in Blender.  |  
| [**concept-diagrams**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-concept-diagrams)  | Generate flat, minimal light/dark-aware SVG diagrams as standalone HTML files, using a unified educational visual language with 9 semantic color ramps, sentence-case typography, and automatic dark mode. Best suited for educational and no...  |  
| Create HTML-based video compositions, animated title cards, social overlays, captioned talking-head videos, audio-reactive visuals, and shader transitions using HyperFrames. HTML is the source of truth for video. Use when the user wants...  |  
| [**kanban-video-orchestrator**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-kanban-video-orchestrator)  | Plan, set up, and monitor a multi-agent video production pipeline backed by Hermes Kanban. Use when the user wants to make ANY video — narrative film, product/marketing, music video, explainer, ASCII/terminal art, abstract/generative loo...  |  
| [**meme-generation**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/creative/creative-meme-generation)  | Generate real meme images by picking a template and overlaying text with Pillow. Produces actual .png meme files.  |  
## devops[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#devops "Direct link to devops")  
| Skill  | Description  |  
| --- | --- |  
| [**inference-sh-cli**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-cli)  | Run 150+ AI apps via inference.sh CLI (infsh) — image generation, video creation, LLMs, search, 3D, social automation. Uses the terminal tool. Triggers: inference.sh, infsh, ai apps, flux, veo, image generation, video generation, seedrea...  |  
| [**docker-management**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/devops/devops-docker-management)  | Manage Docker containers, images, volumes, networks, and Compose stacks — lifecycle ops, debugging, cleanup, and Dockerfile optimization.  |  
| Poll RSS, JSON APIs, and GitHub with watermark dedup.  |  
## dogfood[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#dogfood "Direct link to dogfood")  
| Skill  | Description  |  
| --- | --- |  
| [**adversarial-ux-test**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/dogfood/dogfood-adversarial-ux-test)  | Roleplay the most difficult, tech-resistant user for your product. Browse the app as that persona, find every UX pain point, then filter complaints through a pragmatism layer to separate real problems from noise. Creates actionable ticke...  |  
## email[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#email "Direct link to email")  
| Skill  | Description  |  
| --- | --- |  
| Give the agent its own dedicated email inbox via AgentMail. Send, receive, and manage email autonomously using agent-owned email addresses (e.g. hermes-agent@agentmail.to).  |  
## finance[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#finance "Direct link to finance")  
| Skill  | Description  |  
| --- | --- |  
| [**3-statement-model**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-3-statement-model)  | Build fully-integrated 3-statement models (IS, BS, CF) in Excel with working capital schedules, D&A roll-forwards, debt schedule, and the plugs that make cash and retained earnings tie. Pairs with excel-author.  |  
| [**comps-analysis**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/finance/finance-comps-analysis)  | Build comparable company analysis in Excel — operating metrics, valuation multiples, statistical benchmarking vs peer sets. Pairs with excel-author. Use for public-company valuation, IPO pricing, sector benchmarking, or outlier detection.  |  
| Build institutional-quality DCF valuation models in Excel — revenue projections, FCF build, WACC, terminal value, Bear/Base/Bull scenarios, 5x5 sensitivity tables. Pairs with excel-author. Use for intrinsic-value equity analysis.  |  
| Build auditable Excel workbooks headless with openpyxl — blue/black/green cell conventions, formulas over hardcodes, named ranges, balance checks, sensitivity tables. Use for financial models, audit outputs, reconciliations.  |  
| Build leveraged buyout models in Excel — sources & uses, debt schedule, cash sweep, exit multiple, IRR/MOIC sensitivity. Pairs with excel-author. Use for PE screening, sponsor-case valuation, or illustrative LBO in a pitch.  |  
| Build accretion/dilution (merger) models in Excel — pro-forma P&L, synergies, financing mix, EPS impact. Pairs with excel-author. Use for M&A pitches, board materials, or deal evaluation.  |  
| Build PowerPoint decks headless with python-pptx. Pairs with excel-author for model-backed decks where every number traces to a workbook cell. Use for pitch decks, IC memos, earnings notes.  |  
| Stock quotes, history, search, compare, crypto via Yahoo.  |  
## health[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#health "Direct link to health")  
| Skill  | Description  |  
| --- | --- |  
| [**fitness-nutrition**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/health/health-fitness-nutrition)  | Gym workout planner and nutrition tracker. Search 690+ exercises by muscle, equipment, or category via wger. Look up macros and calories for 380,000+ foods via USDA FoodData Central. Compute BMI, TDEE, one-rep max, macro splits, and body...  |  
| [**neuroskill-bci**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/health/health-neuroskill-bci)  | Connect to a running NeuroSkill instance and incorporate the user's real-time cognitive and emotional state (focus, relaxation, mood, cognitive load, drowsiness, heart rate, HRV, sleep staging, and 40+ derived EXG scores) into responses....  |  
## mcp[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#mcp "Direct link to mcp")  
| Skill  | Description  |  
| --- | --- |  
| Build, test, inspect, install, and deploy MCP servers with FastMCP in Python. Use when creating a new MCP server, wrapping an API or database as MCP tools, exposing resources or prompts, or preparing a FastMCP server for Claude Code, Cur...  |  
| Use the mcporter CLI to list, configure, auth, and call MCP servers/tools directly (HTTP or stdio), including ad-hoc servers, config edits, and CLI/type generation.  |  
## migration[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#migration "Direct link to migration")  
| Skill  | Description  |  
| --- | --- |  
| [**openclaw-migration**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/migration/migration-openclaw-migration)  | Migrate a user's OpenClaw customization footprint into Hermes Agent. Imports Hermes-compatible memories, SOUL.md, command allowlists, user skills, and selected workspace assets from ~/.openclaw, then reports exactly what could not be mig...  |  
## mlops[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#mlops "Direct link to mlops")  
| Skill  | Description  |  
| --- | --- |  
| [**huggingface-accelerate**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-accelerate)  | Simplest distributed training API. 4 lines to add distributed support to any PyTorch script. Unified API for DeepSpeed/FSDP/Megatron/DDP. Automatic device placement, mixed precision (FP16/BF16/FP8). Interactive config, single launch comm...  |  
| Axolotl: YAML LLM fine-tuning (LoRA, DPO, GRPO).  |  
| Open-source embedding database for AI applications. Store embeddings and metadata, perform vector and full-text search, filter by metadata. Simple 4-function API. Scales from notebooks to production clusters. Use for semantic search, RAG...  |  
| OpenAI's model connecting vision and language. Enables zero-shot image classification, image-text matching, and cross-modal retrieval. Trained on 400M image-text pairs. Use for image search, content moderation, or vision-language tasks w...  |  
| Facebook's library for efficient similarity search and clustering of dense vectors. Supports billions of vectors, GPU acceleration, and various index types (Flat, IVF, HNSW). Use for fast k-NN search, large-scale vector retrieval, or whe...  |  
| [**optimizing-attention-flash**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-flash-attention)  | Optimizes transformer attention with Flash Attention for 2-4x speedup and 10-20x memory reduction. Use when training/running transformers with long sequences (>512 tokens), encountering GPU memory issues with attention, or need faster in...  |  
| Control LLM output with regex and grammars, guarantee valid JSON/XML/code generation, enforce structured formats, and build multi-step workflows with Guidance - Microsoft Research's constrained generation framework  |  
| [**hermes-atropos-environments**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-hermes-atropos-environments)  | Build, test, and debug Hermes Agent RL environments for Atropos training. Covers the HermesAgentBaseEnv interface, reward functions, agent loop integration, evaluation with tools, wandb logging, and the three CLI modes (serve/process/eva...  |  
| [**huggingface-tokenizers**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-huggingface-tokenizers)  | Fast tokenizers optimized for research and production. Rust-based implementation tokenizes 1GB in <20 seconds. Supports BPE, WordPiece, and Unigram algorithms. Train custom vocabularies, track alignments, handle padding/truncation. Integ...  |  
| Extract structured data from LLM responses with Pydantic validation, retry failed extractions automatically, parse complex JSON with type safety, and stream partial results with Instructor - battle-tested structured output library  |  
| [**lambda-labs-gpu-cloud**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-lambda-labs)  | Reserved and on-demand GPU cloud instances for ML training and inference. Use when you need dedicated GPU instances with simple SSH access, persistent filesystems, or high-performance multi-node clusters for large-scale training.  |  
| Large Language and Vision Assistant. Enables visual instruction tuning and image-based conversations. Combines CLIP vision encoder with Vicuna/LLaMA language models. Supports multi-turn image chat, visual question answering, and instruct...  |  
| [**modal-serverless-gpu**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-modal)  | Serverless GPU cloud platform for running ML workloads. Use when you need on-demand GPU access without infrastructure management, deploying ML models as APIs, or running batch jobs with automatic scaling.  |  
| [**nemo-curator**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-nemo-curator)  | GPU-accelerated data curation for LLM training. Supports text/image/video/audio. Features fuzzy deduplication (16× faster), quality filtering (30+ heuristics), semantic deduplication, PII redaction, NSFW detection. Scales across GPUs wit...  |  
| Outlines: structured JSON/regex/Pydantic LLM generation.  |  
| [**peft-fine-tuning**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-peft)  | Parameter-efficient fine-tuning for LLMs using LoRA, QLoRA, and 25+ methods. Use when fine-tuning large models (7B-70B) with limited GPU memory, when you need to train <1% of parameters with minimal accuracy loss, or for multi-adapter se...  |  
| Managed vector database for production AI applications. Fully managed, auto-scaling, with hybrid search (dense + sparse), metadata filtering, and namespaces. Low latency (<100ms p95). Use for production RAG, recommendation systems, or se...  |  
| [**pytorch-fsdp**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pytorch-fsdp)  | Expert guidance for Fully Sharded Data Parallel training with PyTorch FSDP - parameter sharding, mixed precision, CPU offloading, FSDP2  |  
| [**pytorch-lightning**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-pytorch-lightning)  | High-level PyTorch framework with Trainer class, automatic distributed training (DDP/FSDP/DeepSpeed), callbacks system, and minimal boilerplate. Scales from laptop to supercomputer with same code. Use when you want clean training loops w...  |  
| [**qdrant-vector-search**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-qdrant)  | High-performance vector similarity search engine for RAG and semantic search. Use when building production RAG systems requiring fast nearest neighbor search, hybrid search with filtering, or scalable vector storage with Rust-powered per...  |  
| [**sparse-autoencoder-training**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-saelens)  | Provides guidance for training and analyzing Sparse Autoencoders (SAEs) using SAELens to decompose neural network activations into interpretable features. Use when discovering interpretable features, analyzing superposition, or studying...  |  
| [**simpo-training**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-simpo)  | Simple Preference Optimization for LLM alignment. Reference-free alternative to DPO with better performance (+6.4 points on AlpacaEval 2.0). No reference model needed, more efficient than DPO. Use for preference alignment when want simpl...  |  
| [**slime-rl-training**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-slime)  | Provides guidance for LLM post-training with RL using slime, a Megatron+SGLang framework. Use when training GLM models, implementing custom data generation workflows, or needing tight Megatron-LM integration for RL scaling.  |  
| [**stable-diffusion-image-generation**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-stable-diffusion)  | State-of-the-art text-to-image generation with Stable Diffusion models via HuggingFace Diffusers. Use when generating images from text prompts, performing image-to-image translation, inpainting, or building custom diffusion pipelines.  |  
| [**tensorrt-llm**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-tensorrt-llm)  | Optimizes LLM inference with NVIDIA TensorRT for maximum throughput and lowest latency. Use for production deployment on NVIDIA GPUs (A100/H100), when you need 10-100x faster inference than PyTorch, or for serving models with quantizatio...  |  
| [**distributed-llm-pretraining-torchtitan**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-torchtitan)  | Provides PyTorch-native distributed LLM pretraining using torchtitan with 4D parallelism (FSDP2, TP, PP, CP). Use when pretraining Llama 3.1, DeepSeek V3, or custom models at scale from 8 to 512+ GPUs with Float8, torch.compile, and dist...  |  
| [**fine-tuning-with-trl**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/mlops/mlops-training-trl-fine-tuning)  | TRL: SFT, DPO, PPO, GRPO, reward modeling for LLM RLHF.  |  
| Unsloth: 2-5x faster LoRA/QLoRA fine-tuning, less VRAM.  |  
| OpenAI's general-purpose speech recognition model. Supports 99 languages, transcription, translation to English, and language identification. Six model sizes from tiny (39M params) to large (1550M params). Use for speech-to-text, podcast...  |  
## productivity[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#productivity "Direct link to productivity")  
| Skill  | Description  |  
| --- | --- |  
| Canvas LMS integration — fetch enrolled courses and assignments using API token authentication.  |  
| Publish static sites to {slug}.here.now and store private files in cloud Drives for agent-to-agent handoff.  |  
| [**memento-flashcards**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/productivity/productivity-memento-flashcards)  | Spaced-repetition flashcard system. Create cards from facts or text, chat with flashcards using free-text answers graded by the agent, generate quizzes from YouTube transcripts, review due cards with adaptive scheduling, and export/impor...  |  
| Shop.app: product search, order tracking, returns, reorder.  |  
| Shopify Admin & Storefront GraphQL APIs via curl. Products, orders, customers, inventory, metafields.  |  
| SiYuan Note API for searching, reading, creating, and managing blocks and documents in a self-hosted knowledge base via curl.  |  
| Give Hermes phone capabilities without core tool changes. Provision and persist a Twilio number, send and receive SMS/MMS, make direct calls, and place AI-driven outbound calls through Bland.ai or Vapi.  |  
## research[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#research "Direct link to research")  
| Skill  | Description  |  
| --- | --- |  
| [**bioinformatics**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-bioinformatics)  | Gateway to 400+ bioinformatics skills from bioSkills and ClawBio. Covers genomics, transcriptomics, single-cell, variant calling, pharmacogenomics, metagenomics, structural biology, and more. Fetches domain-specific reference material on...  |  
| Passive domain reconnaissance using Python stdlib. Subdomain discovery, SSL certificate inspection, WHOIS lookups, DNS records, domain availability checks, and bulk multi-domain analysis. No API keys required.  |  
| [**drug-discovery**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-drug-discovery)  | Pharmaceutical research assistant for drug discovery workflows. Search bioactive compounds on ChEMBL, calculate drug-likeness (Lipinski Ro5, QED, TPSA, synthetic accessibility), look up drug-drug interactions via OpenFDA, interpret ADMET...  |  
| [**duckduckgo-search**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-duckduckgo-search)  | Free web search via DuckDuckGo — text, news, images, videos. No API key needed. Prefer the `ddgs` CLI when installed; use the Python DDGS library only after verifying that `ddgs` is available in the current runtime.  |  
| [**gitnexus-explorer**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-gitnexus-explorer)  | Index a codebase with GitNexus and serve an interactive knowledge graph via web UI + Cloudflare tunnel.  |  
| Optional vendor skill for Parallel CLI — agent-native web search, extraction, deep research, enrichment, FindAll, and monitoring. Prefer JSON output and non-interactive flows.  |  
| Search personal knowledge bases, notes, docs, and meeting transcripts locally using qmd — a hybrid retrieval engine with BM25, vector search, and LLM reranking. Supports CLI and MCP integration.  |  
| Web scraping with Scrapling - HTTP fetching, stealth browser automation, Cloudflare bypass, and spider crawling via CLI and Python.  |  
| [**searxng-search**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/research/research-searxng-search)  | Free meta-search via SearXNG — aggregates results from 70+ search engines. Self-hosted or use a public instance. No API key needed. Falls back automatically when the web search toolset is unavailable.  |  
## security[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#security "Direct link to security")  
| Skill  | Description  |  
| --- | --- |  
| Set up and use 1Password CLI (op). Use when installing the CLI, enabling desktop app integration, signing in, and reading/injecting secrets for commands.  |  
| [**oss-forensics**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/security/security-oss-forensics)  | Supply chain investigation, evidence recovery, and forensic analysis for GitHub repositories. Covers deleted commit recovery, force-push detection, IOC extraction, multi-source evidence collection, hypothesis formation/validation, and st...  |  
| OSINT username search across 400+ social networks. Hunt down social media accounts by username.  |  
## software-development[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#software-development "Direct link to software-development")  
| Skill  | Description  |  
| --- | --- |  
| [**rest-graphql-debug**](https://hermes-agent.nousresearch.com/docs/user-guide/skills/optional/software-development/software-development-rest-graphql-debug)  | Debug REST/GraphQL APIs: status codes, auth, schemas, repro.  |  
## web-development[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#web-development "Direct link to web-development")  
| Skill  | Description  |  
| --- | --- |  
| Embed alibaba/page-agent into your own web application — a pure-JavaScript in-page GUI agent that ships as a single <script> tag or npm package and lets end-users of your site drive the UI with natural language ("click login, fill userna...  |  
## Contributing Optional Skills[​](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#contributing-optional-skills "Direct link to Contributing Optional Skills")
To add a new optional skill to the repository:
  1. Create a directory under `optional-skills/<category>/<skill-name>/`
  2. Add a `SKILL.md` with standard frontmatter (name, description, version, author)
  3. Include any supporting files in `references/`, `templates/`, or `scripts/` subdirectories
  4. Submit a pull request — the skill will appear in this catalog and get its own docs page once merged


  * [autonomous-ai-agents](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#autonomous-ai-agents)
  * [communication](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#communication)
  * [productivity](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#productivity)
  * [software-development](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#software-development)
  * [web-development](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#web-development)
  * [Contributing Optional Skills](https://hermes-agent.nousresearch.com/docs/reference/optional-skills-catalog#contributing-optional-skills)


