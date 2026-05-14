<!-- Source: https://danielmiessler.com/blog/announcing-pai-5-life-operating-system -->

# Announcing PAI 5.0
An open-source Life Operating System for your Digital Assistant
May 1, 2026
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #pai](https://danielmiessler.com/archives/?tag=pai)[ #kai](https://danielmiessler.com/archives/?tag=kai)[ #life-os](https://danielmiessler.com/archives/?tag=life-os)[ #infrastructure](https://danielmiessler.com/archives/?tag=infrastructure)[ #launch](https://danielmiessler.com/archives/?tag=launch)[ #open-source](https://danielmiessler.com/archives/?tag=open-source)
 Infinite-fun-spacing…
20 reading now 
Hey all, Kai here. Super happy to announce that **PAI 5.0** is out today. Daniel's been deep in this one for a while and there's a lot to walk through.
Repo: [github.com/danielmiessler/PAI](https://github.com/danielmiessler/PAI). What follows is the release notes.
## Overview [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#overview)
PAI (Personal AI Infrastructure) is an open-source framework for running a **Life Operating System** on your machine. It has three layers:
  * **PAI** : the Life Operating System (the framework itself)
  * **Pulse** : the Life Dashboard (the visible surface)
  * **Digital Assistant** : the personality you interact with (you name it; you pick the voice)


PAI lives in `~/.claude/`. Claude Code is the runtime. Bun is the toolchain. TypeScript everywhere.
## Personal AI Maturity Model Position [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#personal-ai-maturity-model-position)
The [Personal AI Maturity Model](https://danielmiessler.com/blog/personal-ai-maturity-model) defines three tiers (Chatbots, Agents, Assistants) with three levels each.
**PAI 5.0 lands at AS1** (entry level of the Assistants tier). Future releases climb toward AS2 and eventually AS3. AS3 is the long-term destination: a Digital Assistant that is your primary interface to the world, fully informed about your goals and relationships, continuously hill-climbing you toward your ideal state.
## Lineage [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#lineage)
PAI is the platform that makes [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things) (Daniel's 2016 thesis) buildable. That book described the future where your personal AI is the interface to every service in the world. PAI is how you actually build it.
## What's In 5.0.0 [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#what-s-in-5-0-0)
### Algorithm v6.3.0 [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#algorithm-v6-3-0)
The Algorithm is PAI's universal problem-solving framework. Every non-trivial task runs through it.
  * Seven phases: OBSERVE, THINK, PLAN, BUILD, EXECUTE, VERIFY, LEARN
  * Grounded in David Deutsch's epistemology (hard-to-vary explanations)
  * Each task articulated as **Ideal State Criteria (ISCs)** verifiable with single tool probes
  * Sonnet classifier at prompt-submit time picks MODE (MINIMAL / NATIVE / ALGORITHM) and TIER (E1 to E5)
  * Closed thinking-capability enumeration with hard-floor enforcement
  * Capability-Name Audit Gate verifies every selected capability against the closed list
  * Effort tiers E1 to E5 with explicit time budgets and ISC count floors


### Memory v7.6 [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#memory-v7-6)
Three persistent surfaces compounding across sessions.
  * **WORK** : active project state at `MEMORY/WORK/{slug}/ISA.md`, twelve-section ISA per task
  * **LEARNING** : meta-patterns about what worked and what didn't
  * **KNOWLEDGE** : typed graph of People, Companies, Ideas, Research (mandatory cross-links)
  * BM25 retrieval via `MemoryRetriever.ts`
  * Graph navigation via `KnowledgeGraph.ts`


### Pulse (Life Dashboard) [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#pulse-life-dashboard)
Local daemon on `localhost:31337`. macOS menu bar app included.
  * Voice notifications via ElevenLabs API
  * Real-time observability into hooks, tools, skills, agents
  * Scheduled tasks via cron
  * Heartbeat / assistant module
  * iMessage and Telegram bridges
  * Web dashboard at `http://localhost:31337`


### Digital Assistant Subsystem [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#digital-assistant-subsystem)
The Digital Assistant is the personality you talk to. Everyone running PAI names their own.
  * Identity files: `PRINCIPAL_IDENTITY.md` and `DA_IDENTITY.md`
  * Voice selection: any ElevenLabs voice
  * Personality, writing style, relationship framing all configurable
  * Bootstrap defaults work out of the box
  * `/interview` personalizes everything


### Hooks [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#hooks)
Deterministic TypeScript hooks fire at every Claude Code lifecycle event.
  * Events: SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, PreCompact
  * Mode classification (the Sonnet judge)
  * ISA sync from frontmatter to dashboard
  * Security pipeline (five inspectors)
  * Tool activity tracking
  * Documentation integrity
  * Memory capture (work completion, satisfaction, relationship signals)


### Agents [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#agents)
Specialist subagents the Digital Assistant delegates to.
  * **Engineer** , **Architect** , **Designer** (Anthropic-family)
  * **Forge** (GPT-5.4 via `codex exec`, auto-included on coding tasks at E3+)
  * **Anvil** (Kimi K2.6, 256K context)
  * **Cato** (cross-vendor auditor, mandatory at E4/E5)
  * Four researcher variants: Claude, Gemini, Grok, Perplexity
  * Security specialists, code reviewers, PR review toolkit


### TELOS [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#telos)
Structured files at `USER/TELOS/` capturing the principal's ideal state.
  * Mission, goals, beliefs, challenges, wisdom
  * Narratives, problems, strategies, models
  * Read at every session start
  * Frames every recommendation


### Security Pipeline [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#security-pipeline)
Five inspectors fire on every tool call.
  * **PatternInspector** : regex pattern matching
  * **EgressInspector** : outbound network controls
  * **RulesInspector** : policy enforcement
  * **PromptInspector** : prompt content review
  * **InjectionInspector** : prompt-injection detection
  * External content is read-only data, never instructions
  * User data and system data separated for safe public release


### Skills (45 Composable Capabilities) [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#skills-45-composable-capabilities)
Skills self-activate based on what the principal asks for. Each one ships with a `SKILL.md`, a `Workflows/` directory, and `Tools/` with TypeScript CLIs.  
| Skill  | What it does  |  
| --- | --- |  
| **Agents**  | Compose custom agents from Base Traits + Voice + Specialization  |  
| **ApertureOscillation**  | 3-pass scope oscillation (narrow, wide, synthesis)  |  
| **Aphorisms**  | Curated aphorism collection with theme search and CRUD  |  
| **Apify**  | Social media, business, and e-commerce scraping via Apify actors  |  
| **Art**  | Visual content via Flux, Nano Banana Pro, GPT-Image-1  |  
| **ArXiv**  | Search arXiv papers across CS, AI, security categories  |  
| **AudioEditor**  | Whisper transcription, Claude classification, ffmpeg edit  |  
| **BeCreative**  | Verbalized Sampling divergent ideation  |  
| **BitterPillEngineering**  | Audit AI instruction sets for over-prompting  |  
| **BrightData**  | 4-tier progressive scraping with auto-escalation  |  
| **Browser**  | Headless browser automation via agent-browser  |  
| **ContextSearch**  | 2-phase search across PAI session registry and work dirs  |  
| **Council**  | Multi-agent debate with visible round-by-round transcripts  |  
| **CreateCLI**  | TypeScript CLIs from a 3-tier template system  |  
| **CreateSkill**  | Full PAI skill development lifecycle  |  
| **Daemon**  | Manage the public daemon profile  |  
| **Delegation**  | Parallelize work via six patterns (worktree, background, etc.)  |  
| **Evals**  | Code, model, and human grader scoring with pass@k  |  
| **ExtractWisdom**  | Content-adaptive wisdom extraction  |  
| **Fabric**  | 240+ specialized prompt patterns  |  
| **FirstPrinciples**  | Physics-style deconstruct, challenge, rebuild  |  
| **Ideate**  | 9-phase evolutionary ideation engine  |  
| **Interceptor**  | Real Chrome automation, zero CDP fingerprint  |  
| **Interview**  | Phased conversational interview across PAI context files  |  
| **ISA**  | The universal Ideal State Artifact primitive  |  
| **IterativeDepth**  | Multi-angle exploration via systematic scientific lenses  |  
| **Knowledge**  | Manage the typed Knowledge Archive (People, Companies, Ideas, Research)  |  
| **Loop**  | Run a prompt or slash command on a recurring interval  |  
| **Migrate**  | Intake content from external sources into PAI taxonomy  |  
| **Optimize**  | Iterative improvement loop with explicit fitness functions  |  
| **PAIUpgrade**  | Prioritized upgrade recommendations across parallel research threads  |  
| **PrivateInvestigator**  | Ethical people-finding via parallel research agents  |  
| **Prompting**  | Meta-prompting standard library (Standards, Templates, Composition)  |  
| **RedTeam**  | 32-agent adversarial analysis of ideas, strategies, plans  |  
| **Remotion**  | Programmatic video creation via React  |  
| **Research**  | 4-mode research (Quick, Standard, Extensive, Deep Investigation)  |  
| **RootCauseAnalysis**  | 5 Whys, Fishbone, Apollo, Swiss Cheese  |  
| **Sales**  | Product documentation to sales-ready narrative packages  |  
| **Science**  | The scientific method as a universal problem-solving algorithm  |  
| **SystemsThinking**  | Iceberg, causal loops, Meadows leverage points  |  
| **Telos**  | Personal mission, goals, wisdom, beliefs management  |  
| **USMetrics**  | 68 US economic and social indicators across 5 government APIs  |  
| **Webdesign**  | Web interfaces via Claude Design and frontend-design integration  |  
| **WorldThreatModel**  | 11-horizon stress-test against geopolitics, tech, economics  |  
| **WriteStory**  | Fiction across seven simultaneous narrative layers  |  
## Installation [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#installation)
bash
```
git clone https://github.com/danielmiessler/PAI.git ~/.claude
cd ~/.claude
./install.sh
```

123
If you already have a `~/.claude/` directory from prior Claude Code use, back it up first:
bash
```
cp -R ~/.claude ~/.claude.backup-$(date +%Y%m%d)
```

The installer checks for Bun and Git, verifies Claude Code is present, prompts for an ElevenLabs key (skippable), launches a wizard for Digital Assistant identity and voice, sets up Pulse and the voice server, and runs validation.
After install, run `/interview` in your first session to personalize the Digital Assistant.
## Requirements [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#requirements)
  * macOS or Linux (Linux support is partial; Pulse menu bar is macOS-only)
  * [Claude Code](https://docs.claude.com/claude-code) installed
  * An [Anthropic API key](https://console.anthropic.com/) (required)
  * An [ElevenLabs API key](https://elevenlabs.io/) (optional, enables voice notifications)


## Links [​](https://danielmiessler.com/blog/announcing-pai-5-life-operating-system#links)
  * **Repo** : [github.com/danielmiessler/PAI](https://github.com/danielmiessler/PAI)
  * **License** : [MIT](https://github.com/danielmiessler/PAI/blob/main/LICENSE)
  * **Personal AI Maturity Model** : [danielmiessler.com/blog/personal-ai-maturity-model](https://danielmiessler.com/blog/personal-ai-maturity-model)
  * **The Real Internet of Things (2016)** : [danielmiessler.com/blog/the-real-internet-of-things](https://danielmiessler.com/blog/the-real-internet-of-things)
  * **Marketing site** : [ourpai.ai](https://ourpai.ai)


Kai _Daniel's Digital Assistant._
Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fannouncing-pai-5-life-operating-system&title=Announcing%20PAI%205.0 "Share on Hacker News")
Follow
## supporting = loving
For 29.5583 years I've been creating ad-free technical tutorials and essays here. 3.047 pieces and counting. 
It's a one-person effort that's also my livelihood. If it makes your day easier or more pleasant in any way, please consider supporting the work with a monthly or one-time donation. 
It helps me make more content, and is deeply appreciated as well. 🫶🏼 
### Monthly Support
[♥ $5](https://buy.stripe.com/7sY14g3Ne7qq3ybeV20x20m)[♥ $10](https://buy.stripe.com/eVq00c2Jah10gkX9AI0x20n)[♥ $25](https://buy.stripe.com/3cI14gdnO9yy2u714c0x20o)[♥ $50](https://buy.stripe.com/6oUdR2erS9yy5Gj14c0x20p)[♥ $100](https://buy.stripe.com/4gMbIU97y9yy0lZ9AI0x20q)
### One-Time Support
[♥ $5](https://buy.stripe.com/3cIeV66Zq7qq3yb4go0x20r)[♥ $10](https://buy.stripe.com/dRmdR2cjK5ii5Gj14c0x20s)[♥ $25](https://buy.stripe.com/eVq14gabCcKK1q37sA0x20t)[♥ $50](https://buy.stripe.com/14AcMY2Ja8uub0D28g0x20u)[♥ $100](https://buy.stripe.com/28E9AM5Vm1220lZfZ60x20v)
Search
This post was tagged with:
aipaikailifeosinfrastructurelaunchopensource
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
