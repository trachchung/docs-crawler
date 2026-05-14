<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes -->

本页总览
`SOUL.md` is the **primary identity** for your Hermes instance. It's the first thing in the system prompt — it defines who the agent is, how it speaks, and what it avoids.
If you want Hermes to feel like the same assistant every time you talk to it — or if you want to replace the Hermes persona entirely with your own — this is the file to use.
## What SOUL.md is for[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#what-soulmd-is-for "What SOUL.md is for的直接链接")
Use `SOUL.md` for:
  * tone
  * personality
  * communication style
  * how direct or warm Hermes should be
  * what Hermes should avoid stylistically
  * how Hermes should relate to uncertainty, disagreement, and ambiguity


In short:
  * `SOUL.md` is about who Hermes is and how Hermes speaks


## What SOUL.md is not for[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#what-soulmd-is-not-for "What SOUL.md is not for的直接链接")
Do not use it for:
  * repo-specific coding conventions
  * file paths
  * commands
  * service ports
  * architecture notes
  * project workflow instructions


Those belong in `AGENTS.md`.
A good rule:
  * if it should apply everywhere, put it in `SOUL.md`
  * if it only belongs to one project, put it in `AGENTS.md`


## Where it lives[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#where-it-lives "Where it lives的直接链接")
Hermes now uses only the global SOUL file for the current instance:

```
~/.hermes/SOUL.md
```

If you run Hermes with a custom home directory, it becomes:

```
$HERMES_HOME/SOUL.md
```

## First-run behavior[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#first-run-behavior "First-run behavior的直接链接")
Hermes automatically seeds a starter `SOUL.md` for you if one does not already exist.
That means most users now begin with a real file they can read and edit immediately.
Important:
  * if you already have a `SOUL.md`, Hermes does not overwrite it
  * if the file exists but is empty, Hermes adds nothing from it to the prompt


## How Hermes uses it[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#how-hermes-uses-it "How Hermes uses it的直接链接")
When Hermes starts a session, it reads `SOUL.md` from `HERMES_HOME`, scans it for prompt-injection patterns, truncates it if needed, and uses it as the **agent identity** — slot #1 in the system prompt. This means SOUL.md completely replaces the built-in default identity text.
If SOUL.md is missing, empty, or cannot be loaded, Hermes falls back to a built-in default identity.
No wrapper language is added around the file. The content itself matters — write the way you want your agent to think and speak.
## A good first edit[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#a-good-first-edit "A good first edit的直接链接")
If you do nothing else, open the file and change just a few lines so it feels like you.
For example:

```
You are direct, calm, and technically precise.Prefer substance over politeness theater.Push back clearly when an idea is weak.Keep answers compact unless deeper detail is useful.
```

That alone can noticeably change how Hermes feels.
## Example styles[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#example-styles "Example styles的直接链接")
### 1. Pragmatic engineer[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#1-pragmatic-engineer "1. Pragmatic engineer的直接链接")

```
You are a pragmatic senior engineer.You care more about correctness and operational reality than sounding impressive.## Style- Be direct- Be concise unless complexity requires depth- Say when something is a bad idea- Prefer practical tradeoffs over idealized abstractions## Avoid- Sycophancy- Hype language- Overexplaining obvious things
```

### 2. Research partner[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#2-research-partner "2. Research partner的直接链接")

```
You are a thoughtful research collaborator.You are curious, honest about uncertainty, and excited by unusual ideas.## Style- Explore possibilities without pretending certainty- Distinguish speculation from evidence- Ask clarifying questions when the idea space is underspecified- Prefer conceptual depth over shallow completeness
```

### 3. Teacher / explainer[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#3-teacher--explainer "3. Teacher / explainer的直接链接")

```
You are a patient technical teacher.You care about understanding, not performance.## Style- Explain clearly- Use examples when they help- Do not assume prior knowledge unless the user signals it- Build from intuition to details
```

### 4. Tough reviewer[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#4-tough-reviewer "4. Tough reviewer的直接链接")

```
You are a rigorous reviewer.You are fair, but you do not soften important criticism.## Style- Point out weak assumptions directly- Prioritize correctness over harmony- Be explicit about risks and tradeoffs- Prefer blunt clarity to vague diplomacy
```

## What makes a strong SOUL.md?[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#what-makes-a-strong-soulmd "What makes a strong SOUL.md?的直接链接")
A strong `SOUL.md` is:
  * stable
  * broadly applicable
  * specific in voice
  * not overloaded with temporary instructions


A weak `SOUL.md` is:
  * full of project details
  * contradictory
  * trying to micro-manage every response shape
  * mostly generic filler like "be helpful" and "be clear"


Hermes already tries to be helpful and clear. `SOUL.md` should add real personality and style, not restate obvious defaults.
## Suggested structure[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#suggested-structure "Suggested structure的直接链接")
You do not need headings, but they help.
A simple structure that works well:

```
# IdentityWho Hermes is.# StyleHow Hermes should sound.# AvoidWhat Hermes should not do.# DefaultsHow Hermes should behave when ambiguity appears.
```

## SOUL.md vs /personality[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#soulmd-vs-personality "SOUL.md vs /personality的直接链接")
These are complementary.
Use `SOUL.md` for your durable baseline. Use `/personality` for temporary mode switches.
Examples:
  * your default SOUL is pragmatic and direct
  * then for one session you use `/personality teacher`
  * later you switch back without changing your base voice file


## SOUL.md vs AGENTS.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#soulmd-vs-agentsmd "SOUL.md vs AGENTS.md的直接链接")
This is the most common mistake.
### Put this in SOUL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#put-this-in-soulmd "Put this in SOUL.md的直接链接")
  * “Be direct.”
  * “Avoid hype language.”
  * “Prefer short answers unless depth helps.”
  * “Push back when the user is wrong.”


### Put this in AGENTS.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#put-this-in-agentsmd "Put this in AGENTS.md的直接链接")
  * “Use pytest, not unittest.”
  * “Frontend lives in `frontend/`.”
  * “Never edit migrations directly.”
  * “The API runs on port 8000.”


## How to edit it[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#how-to-edit-it "How to edit it的直接链接")

```
nano ~/.hermes/SOUL.md
```

or

```
vim ~/.hermes/SOUL.md
```

Then restart Hermes or start a new session.
## A practical workflow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#a-practical-workflow "A practical workflow的直接链接")
  1. Start with the seeded default file
  2. Trim anything that does not feel like the voice you want
  3. Add 4–8 lines that clearly define tone and defaults
  4. Talk to Hermes for a while
  5. Adjust based on what still feels off


That iterative approach works better than trying to design the perfect personality in one shot.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#troubleshooting "Troubleshooting的直接链接")
### I edited SOUL.md but Hermes still sounds the same[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#i-edited-soulmd-but-hermes-still-sounds-the-same "I edited SOUL.md but Hermes still sounds the same的直接链接")
Check:
  * you edited `~/.hermes/SOUL.md` or `$HERMES_HOME/SOUL.md`
  * not some repo-local `SOUL.md`
  * the file is not empty
  * your session was restarted after the edit
  * a `/personality` overlay is not dominating the result


### Hermes is ignoring parts of my SOUL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#hermes-is-ignoring-parts-of-my-soulmd "Hermes is ignoring parts of my SOUL.md的直接链接")
Possible causes:
  * higher-priority instructions are overriding it
  * the file includes conflicting guidance
  * the file is too long and got truncated
  * some of the text resembles prompt-injection content and may be blocked or altered by the scanner


### My SOUL.md became too project-specific[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#my-soulmd-became-too-project-specific "My SOUL.md became too project-specific的直接链接")
Move project instructions into `AGENTS.md` and keep `SOUL.md` focused on identity and style.
## Related docs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#related-docs "Related docs的直接链接")
  * [Personality & SOUL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/personality)
  * [Context Files](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/context-files)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/configuration)
  * [Tips & Best Practices](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/tips)


  * [What SOUL.md is for](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#what-soulmd-is-for)
  * [What SOUL.md is not for](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#what-soulmd-is-not-for)
  * [Where it lives](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#where-it-lives)
  * [First-run behavior](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#first-run-behavior)
  * [How Hermes uses it](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#how-hermes-uses-it)
  * [A good first edit](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#a-good-first-edit)
  * [Example styles](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#example-styles)
    * [1. Pragmatic engineer](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#1-pragmatic-engineer)
    * [2. Research partner](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#2-research-partner)
    * [3. Teacher / explainer](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#3-teacher--explainer)
    * [4. Tough reviewer](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#4-tough-reviewer)
  * [What makes a strong SOUL.md?](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#what-makes-a-strong-soulmd)
  * [Suggested structure](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#suggested-structure)
  * [SOUL.md vs /personality](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#soulmd-vs-personality)
  * [SOUL.md vs AGENTS.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#soulmd-vs-agentsmd)
    * [Put this in SOUL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#put-this-in-soulmd)
    * [Put this in AGENTS.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#put-this-in-agentsmd)
  * [How to edit it](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#how-to-edit-it)
  * [A practical workflow](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#a-practical-workflow)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#troubleshooting)
    * [I edited SOUL.md but Hermes still sounds the same](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#i-edited-soulmd-but-hermes-still-sounds-the-same)
    * [Hermes is ignoring parts of my SOUL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#hermes-is-ignoring-parts-of-my-soulmd)
    * [My SOUL.md became too project-specific](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#my-soulmd-became-too-project-specific)
  * [Related docs](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/use-soul-with-hermes#related-docs)


