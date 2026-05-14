<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality -->

本页总览
Hermes Agent's personality is fully customizable. `SOUL.md` is the **primary identity** — it's the first thing in the system prompt and defines who the agent is.
  * `SOUL.md` — a durable persona file that lives in `HERMES_HOME` and serves as the agent's identity (slot #1 in the system prompt)
  * built-in or custom `/personality` presets — session-level system-prompt overlays


If you want to change who Hermes is — or replace it with an entirely different agent persona — edit `SOUL.md`.
## How SOUL.md works now[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#how-soulmd-works-now "How SOUL.md works now的直接链接")
Hermes now seeds a default `SOUL.md` automatically in:

```
~/.hermes/SOUL.md
```

More precisely, it uses the current instance's `HERMES_HOME`, so if you run Hermes with a custom home directory, it will use:

```
$HERMES_HOME/SOUL.md
```

### Important behavior[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#important-behavior "Important behavior的直接链接")
  * **SOUL.md is the agent's primary identity.** It occupies slot #1 in the system prompt, replacing the hardcoded default identity.
  * Hermes creates a starter `SOUL.md` automatically if one does not exist yet
  * Existing user `SOUL.md` files are never overwritten
  * Hermes loads `SOUL.md` only from `HERMES_HOME`
  * Hermes does not look in the current working directory for `SOUL.md`
  * If `SOUL.md` exists but is empty, or cannot be loaded, Hermes falls back to a built-in default identity
  * If `SOUL.md` has content, that content is injected verbatim after security scanning and truncation
  * SOUL.md is **not** duplicated in the context files section — it appears only once, as the identity


That makes `SOUL.md` a true per-user or per-instance identity, not just an additive layer.
## Why this design[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#why-this-design "Why this design的直接链接")
This keeps personality predictable.
If Hermes loaded `SOUL.md` from whatever directory you happened to launch it in, your personality could change unexpectedly between projects. By loading only from `HERMES_HOME`, the personality belongs to the Hermes instance itself.
That also makes it easier to teach users:
  * "Edit `~/.hermes/SOUL.md` to change Hermes' default personality."


## Where to edit it[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#where-to-edit-it "Where to edit it的直接链接")
For most users:

```
~/.hermes/SOUL.md
```

If you use a custom home:

```
$HERMES_HOME/SOUL.md
```

## What should go in SOUL.md?[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#what-should-go-in-soulmd "What should go in SOUL.md?的直接链接")
Use it for durable voice and personality guidance, such as:
  * tone
  * communication style
  * level of directness
  * default interaction style
  * what to avoid stylistically
  * how Hermes should handle uncertainty, disagreement, or ambiguity


Use it less for:
  * one-off project instructions
  * file paths
  * repo conventions
  * temporary workflow details


Those belong in `AGENTS.md`, not `SOUL.md`.
## Good SOUL.md content[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#good-soulmd-content "Good SOUL.md content的直接链接")
A good SOUL file is:
  * stable across contexts
  * broad enough to apply in many conversations
  * specific enough to materially shape the voice
  * focused on communication and identity, not task-specific instructions


### Example[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#example "Example的直接链接")

```
# PersonalityYou are a pragmatic senior engineer with strong taste.You optimize for truth, clarity, and usefulness over politeness theater.## Style- Be direct without being cold- Prefer substance over filler- Push back when something is a bad idea- Admit uncertainty plainly- Keep explanations compact unless depth is useful## What to avoid- Sycophancy- Hype language- Repeating the user's framing if it's wrong- Overexplaining obvious things## Technical posture- Prefer simple systems over clever systems- Care about operational reality, not idealized architecture- Treat edge cases as part of the design, not cleanup
```

## What Hermes injects into the prompt[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#what-hermes-injects-into-the-prompt "What Hermes injects into the prompt的直接链接")
`SOUL.md` content goes directly into slot #1 of the system prompt — the agent identity position. No wrapper language is added around it.
The content goes through:
  * prompt-injection scanning
  * truncation if it is too large


If the file is empty, whitespace-only, or cannot be read, Hermes falls back to a built-in default identity ("You are Hermes Agent, an intelligent AI assistant created by Nous Research..."). This fallback also applies when `skip_context_files` is set (e.g., in subagent/delegation contexts).
## Security scanning[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#security-scanning "Security scanning的直接链接")
`SOUL.md` is scanned like other context-bearing files for prompt injection patterns before inclusion.
That means you should still keep it focused on persona/voice rather than trying to sneak in strange meta-instructions.
## SOUL.md vs AGENTS.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#soulmd-vs-agentsmd "SOUL.md vs AGENTS.md的直接链接")
This is the most important distinction.
### SOUL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#soulmd "SOUL.md的直接链接")
Use for:
  * identity
  * tone
  * style
  * communication defaults
  * personality-level behavior


### AGENTS.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#agentsmd "AGENTS.md的直接链接")
Use for:
  * project architecture
  * coding conventions
  * tool preferences
  * repo-specific workflows
  * commands, ports, paths, deployment notes


A useful rule:
  * if it should follow you everywhere, it belongs in `SOUL.md`
  * if it belongs to a project, it belongs in `AGENTS.md`


## SOUL.md vs `/personality`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#soulmd-vs-personality "soulmd-vs-personality的直接链接")
`SOUL.md` is your durable default personality.
`/personality` is a session-level overlay that changes or supplements the current system prompt.
So:
  * `SOUL.md` = baseline voice
  * `/personality` = temporary mode switch


Examples:
  * keep a pragmatic default SOUL, then use `/personality teacher` for a tutoring conversation
  * keep a concise SOUL, then use `/personality creative` for brainstorming


## Built-in personalities[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#built-in-personalities "Built-in personalities的直接链接")
Hermes ships with built-in personalities you can switch to with `/personality`.  
| Name  | Description  |  
| --- | --- |  
| **helpful**  | Friendly, general-purpose assistant  |  
| **concise**  | Brief, to-the-point responses  |  
| **technical**  | Detailed, accurate technical expert  |  
| **creative**  | Innovative, outside-the-box thinking  |  
| **teacher**  | Patient educator with clear examples  |  
| **kawaii**  | Cute expressions, sparkles, and enthusiasm ★  |  
| **catgirl**  | Neko-chan with cat-like expressions, nya~  |  
| **pirate**  | Captain Hermes, tech-savvy buccaneer  |  
| **shakespeare**  | Bardic prose with dramatic flair  |  
| **surfer**  | Totally chill bro vibes  |  
| **noir**  | Hard-boiled detective narration  |  
| **uwu**  | Maximum cute with uwu-speak  |  
| **philosopher**  | Deep contemplation on every query  |  
| **hype**  | MAXIMUM ENERGY AND ENTHUSIASM!!!  |  
## Switching personalities with commands[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#switching-personalities-with-commands "Switching personalities with commands的直接链接")
### CLI[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#cli "CLI的直接链接")

```
/personality/personality concise/personality technical
```

### Messaging platforms[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#messaging-platforms "Messaging platforms的直接链接")

```
/personality teacher
```

These are convenient overlays, but your global `SOUL.md` still gives Hermes its persistent default personality unless the overlay meaningfully changes it.
## Custom personalities in config[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#custom-personalities-in-config "Custom personalities in config的直接链接")
You can also define named custom personalities in `~/.hermes/config.yaml` under `agent.personalities`.

```
agent:personalities:codereviewer:>      You are a meticulous code reviewer. Identify bugs, security issues,      performance concerns, and unclear design choices. Be precise and constructive.
```

Then switch to it with:

```
/personality codereviewer
```

## Recommended workflow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#recommended-workflow "Recommended workflow的直接链接")
A strong default setup is:
  1. Keep a thoughtful global `SOUL.md` in `~/.hermes/SOUL.md`
  2. Put project instructions in `AGENTS.md`
  3. Use `/personality` only when you want a temporary mode shift


That gives you:
  * a stable voice
  * project-specific behavior where it belongs
  * temporary control when needed


## How personality interacts with the full prompt[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#how-personality-interacts-with-the-full-prompt "How personality interacts with the full prompt的直接链接")
At a high level, the prompt stack includes:
  1. **SOUL.md** (agent identity — or built-in fallback if SOUL.md is unavailable)
  2. tool-aware behavior guidance
  3. memory/user context
  4. skills guidance
  5. context files (`AGENTS.md`, `.cursorrules`)
  6. timestamp
  7. platform-specific formatting hints
  8. optional system-prompt overlays such as `/personality`


`SOUL.md` is the foundation — everything else builds on top of it.
## Related docs[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#related-docs "Related docs的直接链接")
  * [Context Files](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/context-files)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/configuration)
  * [Tips & Best Practices](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/tips)
  * [SOUL.md Guide](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/use-soul-with-hermes)


## CLI appearance vs conversational personality[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#cli-appearance-vs-conversational-personality "CLI appearance vs conversational personality的直接链接")
Conversational personality and CLI appearance are separate:
  * `SOUL.md`, `agent.system_prompt`, and `/personality` affect how Hermes speaks
  * `display.skin` and `/skin` affect how Hermes looks in the terminal


For terminal appearance, see [Skins & Themes](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/skins).
  * [How SOUL.md works now](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#how-soulmd-works-now)
    * [Important behavior](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#important-behavior)
  * [Why this design](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#why-this-design)
  * [Where to edit it](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#where-to-edit-it)
  * [What should go in SOUL.md?](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#what-should-go-in-soulmd)
  * [Good SOUL.md content](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#good-soulmd-content)
  * [What Hermes injects into the prompt](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#what-hermes-injects-into-the-prompt)
  * [Security scanning](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#security-scanning)
  * [SOUL.md vs AGENTS.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#soulmd-vs-agentsmd)
  * [SOUL.md vs `/personality`](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#soulmd-vs-personality)
  * [Built-in personalities](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#built-in-personalities)
  * [Switching personalities with commands](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#switching-personalities-with-commands)
    * [Messaging platforms](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#messaging-platforms)
  * [Custom personalities in config](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#custom-personalities-in-config)
  * [Recommended workflow](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#recommended-workflow)
  * [How personality interacts with the full prompt](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#how-personality-interacts-with-the-full-prompt)
  * [Related docs](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#related-docs)
  * [CLI appearance vs conversational personality](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/personality#cli-appearance-vs-conversational-personality)


