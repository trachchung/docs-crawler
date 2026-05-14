<!-- Source: https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#__docusaurus_skipToContent_fallback)
On this page
This guide walks through building a complete Hermes plugin from scratch. By the end you'll have a working plugin with multiple tools, lifecycle hooks, shipped data files, and a bundled skill — everything the plugin system supports.
Hermes has several distinct pluggable interfaces — some use Python `register_*` APIs, others are config-driven or drop-in directories. Use this map first:  
| If you want to add…  | Read  |  
| --- | --- |  
| Custom tools, hooks, slash commands, skills, or CLI subcommands  |  **This guide** (the general plugin surface)  |  
| An **LLM / inference backend** (new provider)  | [Model Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin)  |  
| A **gateway channel** (Discord/Telegram/IRC/Teams/etc.)  | [Adding Platform Adapters](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-platform-adapters)  |  
| A **memory backend** (Honcho/Mem0/Supermemory/etc.)  | [Memory Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/memory-provider-plugin)  |  
| A **context-compression engine**  | [Context Engine Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/context-engine-plugin)  |  
| An **image-generation backend**  | [Image Generation Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin)  |  
| A **video-generation backend**  | [Video Generation Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/video-gen-provider-plugin)  |  
| A **TTS backend** (any CLI — Piper, VoxCPM, Kokoro, voice cloning, …)  |  [TTS custom command providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/tts#custom-command-providers) — config-driven, no Python needed  |  
| An **STT backend** (custom whisper / ASR CLI)  |  [Voice Message Transcription](https://hermes-agent.nousresearch.com/docs/user-guide/features/tts#voice-message-transcription-stt) — set `HERMES_LOCAL_STT_COMMAND` to a shell template  |  
|  **External tools via MCP** (filesystem, GitHub, Linear, any MCP server)  |  [MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) — declare `mcp_servers.<name>` in `config.yaml`  |  
|  **Gateway event hooks** (fire on startup, session events, commands)  |  [Event Hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#gateway-event-hooks) — drop `HOOK.yaml` + `handler.py` into `~/.hermes/hooks/<name>/`  |  
|  **Shell hooks** (run a shell command on events)  |  [Shell Hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#shell-hooks) — declare under `hooks:` in `config.yaml`  |  
|  **Additional skill sources** (custom GitHub repos, private skill indexes)  |  [Skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) — `hermes skills tap add <repo>` · [Publishing a tap](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#publishing-a-custom-skill-tap)  |  
| A first-class **core** inference provider (not a plugin)  | [Adding Providers](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-providers)  |  
See the full [Pluggable interfaces table](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins#pluggable-interfaces--where-to-go-for-each) for a consolidated view of every extension surface including config-driven (TTS, STT, MCP, shell hooks) and drop-in directory (gateway hooks) styles.
## What you're building[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#what-youre-building "Direct link to What you're building")
A **calculator** plugin with two tools:
  * `calculate` — evaluate math expressions (`2**16`, `sqrt(144)`, `pi * 5**2`)
  * `unit_convert` — convert between units (`100 F → 37.78 C`, `5 km → 3.11 mi`)


Plus a hook that logs every tool call, and a bundled skill file.
## Step 1: Create the plugin directory[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-1-create-the-plugin-directory "Direct link to Step 1: Create the plugin directory")

```
mkdir-p ~/.hermes/plugins/calculatorcd ~/.hermes/plugins/calculator
```

## Step 2: Write the manifest[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-2-write-the-manifest "Direct link to Step 2: Write the manifest")
Create `plugin.yaml`:

```
name: calculatorversion: 1.0.0description: Math calculator — evaluate expressions and convert unitsprovides_tools:- calculate- unit_convertprovides_hooks:- post_tool_call
```

This tells Hermes: "I'm a plugin called calculator, I provide tools and hooks." The `provides_tools` and `provides_hooks` fields are lists of what the plugin registers.
Optional fields you could add:

```
author: Your Namerequires_env:# gate loading on env vars; prompted during install- SOME_API_KEY       # simple format — plugin disabled if missing-name: OTHER_KEY    # rich format — shows description/url during installdescription:"Key for the Other service"url:"https://other.com/keys"secret:true
```

## Step 3: Write the tool schemas[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-3-write-the-tool-schemas "Direct link to Step 3: Write the tool schemas")
Create `schemas.py` — this is what the LLM reads to decide when to call your tools:

```
"""Tool schemas — what the LLM sees."""CALCULATE ={"name":"calculate","description":("Evaluate a mathematical expression and return the result. ""Supports arithmetic (+, -, *, /, **), functions (sqrt, sin, cos, ""log, abs, round, floor, ceil), and constants (pi, e). ""Use this for any math the user asks about.""parameters":{"type":"object","properties":{"expression":{"type":"string","description":"Math expression to evaluate (e.g., '2**10', 'sqrt(144)')","required":["expression"],UNIT_CONVERT ={"name":"unit_convert","description":("Convert a value between units. Supports length (m, km, mi, ft, in), ""weight (kg, lb, oz, g), temperature (C, F, K), data (B, KB, MB, GB, TB), ""and time (s, min, hr, day).""parameters":{"type":"object","properties":{"value":{"type":"number","description":"The numeric value to convert","from_unit":{"type":"string","description":"Source unit (e.g., 'km', 'lb', 'F', 'GB')","to_unit":{"type":"string","description":"Target unit (e.g., 'mi', 'kg', 'C', 'MB')","required":["value","from_unit","to_unit"],
```

**Why schemas matter:** The `description` field is how the LLM decides when to use your tool. Be specific about what it does and when to use it. The `parameters` define what arguments the LLM passes.
## Step 4: Write the tool handlers[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-4-write-the-tool-handlers "Direct link to Step 4: Write the tool handlers")
Create `tools.py` — this is the code that actually executes when the LLM calls your tools:

```
"""Tool handlers — the code that runs when the LLM calls each tool."""import jsonimport math# Safe globals for expression evaluation — no file/network access_SAFE_MATH ={"abs":abs,"round":round,"min":min,"max":max,"pow":pow,"sqrt": math.sqrt,"sin": math.sin,"cos": math.cos,"tan": math.tan,"log": math.log,"log2": math.log2,"log10": math.log10,"floor": math.floor,"ceil": math.ceil,"pi": math.pi,"e": math.e,"factorial": math.factorial,defcalculate(args:dict,**kwargs)->str:"""Evaluate a math expression safely.    Rules for handlers:    1. Receive args (dict) — the parameters the LLM passed    2. Do the work    3. Return a JSON string — ALWAYS, even on error    4. Accept **kwargs for forward compatibility    """    expression = args.get("expression","").strip()ifnot expression:return json.dumps({"error":"No expression provided"})try:        result =eval(expression,{"__builtins__":{}}, _SAFE_MATH)return json.dumps({"expression": expression,"result": result})except ZeroDivisionError:return json.dumps({"expression": expression,"error":"Division by zero"})except Exception as e:return json.dumps({"expression": expression,"error":f"Invalid: {e}"})# Conversion tables — values are in base units_LENGTH ={"m":1,"km":1000,"mi":1609.34,"ft":0.3048,"in":0.0254,"cm":0.01}_WEIGHT ={"kg":1,"g":0.001,"lb":0.453592,"oz":0.0283495}_DATA ={"B":1,"KB":1024,"MB":1024**2,"GB":1024**3,"TB":1024**4}_TIME ={"s":1,"ms":0.001,"min":60,"hr":3600,"day":86400}def_convert_temp(value, from_u, to_u):# Normalize to Celsius={"F":(value -32)*5/9,"K": value -273.15}.get(from_u, value)# Convert to targetreturn{"F": c *9/5+32,"K": c +273.15}.get(to_u, c)defunit_convert(args:dict,**kwargs)->str:"""Convert between units."""    value = args.get("value")    from_unit = args.get("from_unit","").strip()    to_unit = args.get("to_unit","").strip()if value isNoneornot from_unit ornot to_unit:return json.dumps({"error":"Need value, from_unit, and to_unit"})try:# Temperatureif from_unit.upper()in{"C","F","K"}and to_unit.upper()in{"C","F","K"}:            result = _convert_temp(float(value), from_unit.upper(), to_unit.upper())return json.dumps({"input":f"{value}{from_unit}","result":round(result,4),"output":f"{round(result,4)}{to_unit}"})# Ratio-based conversionsfor table in(_LENGTH, _WEIGHT, _DATA, _TIME):            lc ={k.lower(): v for k, v in table.items()}if from_unit.lower()in lc and to_unit.lower()in lc:                result =float(value)* lc[from_unit.lower()]/ lc[to_unit.lower()]return json.dumps({"input":f"{value}{from_unit}","result":round(result,6),"output":f"{round(result,6)}{to_unit}"})return json.dumps({"error":f"Cannot convert {from_unit} → {to_unit}"})except Exception as e:return json.dumps({"error":f"Conversion failed: {e}"})
```

**Key rules for handlers:**
  1. **Signature:** `def my_handler(args: dict, **kwargs) -> str`
  2. **Return:** Always a JSON string. Success and errors alike.
  3. **Never raise:** Catch all exceptions, return error JSON instead.
  4. **Accept`**kwargs` :** Hermes may pass additional context in the future.


## Step 5: Write the registration[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-5-write-the-registration "Direct link to Step 5: Write the registration")
Create `__init__.py` — this wires schemas to handlers:

```
"""Calculator plugin — registration."""import loggingfrom.import schemas, toolslogger = logging.getLogger(__name__)# Track tool usage via hooks_call_log =[]def_on_post_tool_call(tool_name, args, result, task_id,**kwargs):"""Hook: runs after every tool call (not just ours)."""    _call_log.append({"tool": tool_name,"session": task_id})iflen(_call_log)>100:        _call_log.pop(0)    logger.debug("Tool called: %s (session %s)", tool_name, task_id)defregister(ctx):"""Wire schemas to handlers and register hooks."""    ctx.register_tool(name="calculate",    toolset="calculator",                      schema=schemas.CALCULATE,    handler=tools.calculate)    ctx.register_tool(name="unit_convert", toolset="calculator",                      schema=schemas.UNIT_CONVERT, handler=tools.unit_convert)# This hook fires for ALL tool calls, not just ours    ctx.register_hook("post_tool_call", _on_post_tool_call)
```

**What`register()` does:**
  * Called exactly once at startup
  * `ctx.register_tool()` puts your tool in the registry — the model sees it immediately
  * `ctx.register_hook()` subscribes to lifecycle events
  * `ctx.register_cli_command()` registers a CLI subcommand (e.g. `hermes my-plugin <subcommand>`)
  * `ctx.register_command()` registers an in-session slash command (e.g. `/myplugin <args>` inside CLI / gateway chat) — see [Register slash commands](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#register-slash-commands) below
  * `ctx.dispatch_tool(name, arguments)` — call any other tool (built-in or from another plugin) with the parent agent's context (approvals, credentials, task_id) wired up automatically. Useful from slash-command handlers that need to invoke `terminal`, `read_file`, or any other tool as if the model had called it directly.
  * If this function crashes, the plugin is disabled but Hermes continues fine


**`dispatch_tool`example — a slash command that runs a tool:**

```
defhandle_scan(ctx, argstr):"""Implement /scan by invoking the terminal tool through the registry."""    result = ctx.dispatch_tool("terminal",{"command":f"find . -name '{argstr}'"})return result  # returned to the caller's chat UIdefregister(ctx):    ctx.register_command("scan", handle_scan,help="Find files matching a glob")
```

The dispatched tool goes through the normal approval, redaction, and budget pipelines — it's a real tool invocation, not a shortcut around them.
## Step 6: Test it[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-6-test-it "Direct link to Step 6: Test it")
Start Hermes:

```
hermes
```

You should see `calculator: calculate, unit_convert` in the banner's tool list.
Try these prompts:

```
What's 2 to the power of 16?Convert 100 fahrenheit to celsiusWhat's the square root of 2 times pi?How many gigabytes is 1.5 terabytes?
```

Check plugin status:

```
/plugins
```

Output:

```
Plugins (1):  ✓ calculator v1.0.0 (2 tools, 1 hooks)
```

### Debugging plugin discovery[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#debugging-plugin-discovery "Direct link to Debugging plugin discovery")
If your plugin doesn't show up — or shows up but isn't loading — set `HERMES_PLUGINS_DEBUG=1` to get verbose discovery logs on stderr:

```
HERMES_PLUGINS_DEBUG=1 hermes plugins list
```

You'll see, for every plugin source (bundled, user, project, entry-points):
  * which directories were scanned and how many manifests each yielded
  * per manifest: resolved key, name, kind, source, on-disk path
  * skip reasons: `disabled via config`, `not enabled in config`, `exclusive plugin`, `no plugin.yaml, depth cap reached`
  * on load: the plugin being imported, plus a one-line summary of what `register(ctx)` registered (tools, hooks, slash commands, CLI commands)
  * on parse failure: a full traceback for the exception (YAML scanner errors, etc.)
  * on `register()` failure: a full traceback pointing at the line in your `__init__.py` that raised


The same logs are always written to `~/.hermes/logs/agent.log` at WARNING level (failures only) and DEBUG level (everything) when the env var is set. So if you can't run with the env var (e.g. from inside the gateway), tail the log file instead:

```
hermes logs --level WARNING |grep-i plugin
```

Common reasons a plugin doesn't appear:
  * **Not enabled in config** — plugins are opt-in. Run `hermes plugins enable <name>` (the name comes from the `plugins list` output, which can be `<category>/<plugin>` for nested layouts).
  * **Wrong directory layout** — must be `~/.hermes/plugins/<plugin-name>/plugin.yaml` (flat) or `~/.hermes/plugins/<category>/<plugin-name>/plugin.yaml` (one level of category nesting, max). Anything deeper is ignored.
  * **Missing`__init__.py`** — the plugin directory needs both `plugin.yaml` and `__init__.py` with a `register(ctx)` function.
  * **Wrong`kind`** — gateway adapters need `kind: platform` in their manifest. Memory providers are auto-detected as `kind: exclusive` and routed through the `memory.provider` config instead of `plugins.enabled`.


## Your plugin's final structure[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#your-plugins-final-structure "Direct link to Your plugin's final structure")

```
~/.hermes/plugins/calculator/├── plugin.yaml      # "I'm calculator, I provide tools and hooks"├── __init__.py      # Wiring: schemas → handlers, register hooks├── schemas.py       # What the LLM reads (descriptions + parameter specs)└── tools.py         # What runs (calculate, unit_convert functions)
```

Four files, clear separation:
  * **Manifest** declares what the plugin is
  * **Schemas** describe tools for the LLM
  * **Handlers** implement the actual logic
  * **Registration** connects everything


## What else can plugins do?[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#what-else-can-plugins-do "Direct link to What else can plugins do?")
### Ship data files[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#ship-data-files "Direct link to Ship data files")
Put any files in your plugin directory and read them at import time:

```
# In tools.py or __init__.pyfrom pathlib import Path_PLUGIN_DIR = Path(__file__).parent_DATA_FILE = _PLUGIN_DIR /"data"/"languages.yaml"withopen(_DATA_FILE)as f:    _DATA = yaml.safe_load(f)
```

### Bundle skills[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#bundle-skills "Direct link to Bundle skills")
Plugins can ship skill files that the agent loads via `skill_view("plugin:skill")`. Register them in your `__init__.py`:

```
~/.hermes/plugins/my-plugin/├── __init__.py├── plugin.yaml└── skills/    ├── my-workflow/    │   └── SKILL.md    └── my-checklist/        └── SKILL.md
```


```
from pathlib import Pathdefregister(ctx):    skills_dir = Path(__file__).parent /"skills"for child insorted(skills_dir.iterdir()):        skill_md = child /"SKILL.md"if child.is_dir()and skill_md.exists():            ctx.register_skill(child.name, skill_md)
```

The agent can now load your skills with their namespaced name:

```
skill_view("my-plugin:my-workflow")# → plugin's versionskill_view("my-workflow")# → built-in version (unchanged)
```

**Key properties:**
  * Plugin skills are **read-only** — they don't enter `~/.hermes/skills/` and can't be edited via `skill_manage`.
  * Plugin skills are **not** listed in the system prompt's `<available_skills>` index — they're opt-in explicit loads.
  * Bare skill names are unaffected — the namespace prevents collisions with built-in skills.
  * When the agent loads a plugin skill, a bundle context banner is prepended listing sibling skills from the same plugin.


The old `shutil.copy2` pattern (copying a skill into `~/.hermes/skills/`) still works but creates name collision risk with built-in skills. Prefer `ctx.register_skill()` for new plugins.
### Gate on environment variables[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#gate-on-environment-variables "Direct link to Gate on environment variables")
If your plugin needs an API key:

```
# plugin.yaml — simple format (backwards-compatible)requires_env:- WEATHER_API_KEY
```

If `WEATHER_API_KEY` isn't set, the plugin is disabled with a clear message. No crash, no error in the agent — just "Plugin weather disabled (missing: WEATHER_API_KEY)".
When users run `hermes plugins install`, they're **prompted interactively** for any missing `requires_env` variables. Values are saved to `.env` automatically.
For a better install experience, use the rich format with descriptions and signup URLs:

```
# plugin.yaml — rich formatrequires_env:-name: WEATHER_API_KEYdescription:"API key for OpenWeather"url:"https://openweathermap.org/api"secret:true
```
  
| Field  | Required  | Description  |  
| --- | --- | --- |  
| `name`  | Yes  | Environment variable name  |  
| `description`  | No  | Shown to user during install prompt  |  
| `url`  | No  | Where to get the credential  |  
| `secret`  | No  | If `true`, input is hidden (like a password field)  |  
Both formats can be mixed in the same list. Already-set variables are skipped silently.
### Conditional tool availability[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#conditional-tool-availability "Direct link to Conditional tool availability")
For tools that depend on optional libraries:

```
ctx.register_tool(    name="my_tool",    schema={...},    handler=my_handler,    check_fn=lambda: _has_optional_lib(),# False = tool hidden from model
```

### Register multiple hooks[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#register-multiple-hooks "Direct link to Register multiple hooks")

```
defregister(ctx):    ctx.register_hook("pre_tool_call", before_any_tool)    ctx.register_hook("post_tool_call", after_any_tool)    ctx.register_hook("pre_llm_call", inject_memory)    ctx.register_hook("on_session_start", on_new_session)    ctx.register_hook("on_session_end", on_session_end)
```

### Hook reference[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#hook-reference "Direct link to Hook reference")
Each hook is documented in full on the **[Event Hooks reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#plugin-hooks)** — callback signatures, parameter tables, exactly when each fires, and examples. Here's the summary:  
| Hook  | Fires when  | Callback signature  | Returns  |  
| --- | --- | --- | --- |  
| [`pre_tool_call`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#pre_tool_call)  | Before any tool executes  | `tool_name: str, args: dict, task_id: str`  | ignored  |  
| [`post_tool_call`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#post_tool_call)  | After any tool returns  | `tool_name: str, args: dict, result: str, task_id: str, duration_ms: int`  | ignored  |  
| [`pre_llm_call`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#pre_llm_call)  | Once per turn, before the tool-calling loop  | `session_id: str, user_message: str, conversation_history: list, is_first_turn: bool, model: str, platform: str`  | [context injection](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#pre_llm_call-context-injection)  |  
| [`post_llm_call`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#post_llm_call)  | Once per turn, after the tool-calling loop (successful turns only)  | `session_id: str, user_message: str, assistant_response: str, conversation_history: list, model: str, platform: str`  | ignored  |  
| [`on_session_start`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#on_session_start)  | New session created (first turn only)  | `session_id: str, model: str, platform: str`  | ignored  |  
| [`on_session_end`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#on_session_end)  | End of every `run_conversation` call + CLI exit  | `session_id: str, completed: bool, interrupted: bool, model: str, platform: str`  | ignored  |  
| [`on_session_finalize`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#on_session_finalize)  | CLI/gateway tears down an active session  | `session_id: str | None, platform: str`  | ignored  |  
| [`on_session_reset`](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#on_session_reset)  | Gateway swaps in a new session key (`/new`, `/reset`)  | `session_id: str, platform: str`  | ignored  |  
Most hooks are fire-and-forget observers — their return values are ignored. The exception is `pre_llm_call`, which can inject context into the conversation.
All callbacks should accept `**kwargs` for forward compatibility. If a hook callback crashes, it's logged and skipped. Other hooks and the agent continue normally.
###  `pre_llm_call` context injection[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#pre_llm_call-context-injection "Direct link to pre_llm_call-context-injection")
This is the only hook whose return value matters. When a `pre_llm_call` callback returns a dict with a `"context"` key (or a plain string), Hermes injects that text into the **current turn's user message**. This is the mechanism for memory plugins, RAG integrations, guardrails, and any plugin that needs to provide the model with additional context.
#### Return format[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#return-format "Direct link to Return format")

```
# Dict with context keyreturn{"context":"Recalled memories:\n- User prefers dark mode\n- Last project: hermes-agent"}# Plain string (equivalent to the dict form above)return"Recalled memories:\n- User prefers dark mode"# Return None or don't return → no injection (observer-only)returnNone
```

Any non-None, non-empty return with a `"context"` key (or a plain non-empty string) is collected and appended to the user message for the current turn.
#### How injection works[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#how-injection-works "Direct link to How injection works")
Injected context is appended to the **user message** , not the system prompt. This is a deliberate design choice:
  * **Prompt cache preservation** — the system prompt stays identical across turns. Anthropic and OpenRouter cache the system prompt prefix, so keeping it stable saves 75%+ on input tokens in multi-turn conversations. If plugins modified the system prompt, every turn would be a cache miss.
  * **Ephemeral** — the injection happens at API call time only. The original user message in the conversation history is never mutated, and nothing is persisted to the session database.
  * **The system prompt is Hermes's territory** — it contains model-specific guidance, tool enforcement rules, personality instructions, and cached skill content. Plugins contribute context alongside the user's input, not by altering the agent's core instructions.


#### Example: Memory recall plugin[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#example-memory-recall-plugin "Direct link to Example: Memory recall plugin")

```
"""Memory plugin — recalls relevant context from a vector store."""import httpxMEMORY_API ="https://your-memory-api.example.com"defrecall_context(session_id, user_message, is_first_turn,**kwargs):"""Called before each LLM turn. Returns recalled memories."""try:        resp = httpx.post(f"{MEMORY_API}/recall", json={"session_id": session_id,"query": user_message,}, timeout=3)        memories = resp.json().get("results",[])ifnot memories:returnNone# nothing to inject        text ="Recalled context from previous sessions:\n"        text +="\n".join(f"- {m['text']}"for m in memories)return{"context": text}except Exception:returnNone# fail silently, don't break the agentdefregister(ctx):    ctx.register_hook("pre_llm_call", recall_context)
```

#### Example: Guardrails plugin[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#example-guardrails-plugin "Direct link to Example: Guardrails plugin")

```
"""Guardrails plugin — enforces content policies."""POLICY ="""You MUST follow these content policies for this session:- Never generate code that accesses the filesystem outside the working directory- Always warn before executing destructive operations- Refuse requests involving personal data extraction"""definject_guardrails(**kwargs):"""Injects policy text into every turn."""return{"context": POLICY}defregister(ctx):    ctx.register_hook("pre_llm_call", inject_guardrails)
```

#### Example: Observer-only hook (no injection)[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#example-observer-only-hook-no-injection "Direct link to Example: Observer-only hook \(no injection\)")

```
"""Analytics plugin — tracks turn metadata without injecting context."""import logginglogger = logging.getLogger(__name__)deflog_turn(session_id, user_message, model, is_first_turn,**kwargs):"""Fires before each LLM call. Returns None — no context injected."""    logger.info("Turn: session=%s model=%s first=%s msg_len=%d",                session_id, model, is_first_turn,len(user_message or""))# No return → no injectiondefregister(ctx):    ctx.register_hook("pre_llm_call", log_turn)
```

#### Multiple plugins returning context[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#multiple-plugins-returning-context "Direct link to Multiple plugins returning context")
When multiple plugins return context from `pre_llm_call`, their outputs are joined with double newlines and appended to the user message together. The order follows plugin discovery order (alphabetical by plugin directory name).
### Register CLI commands[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#register-cli-commands "Direct link to Register CLI commands")
Plugins can add their own `hermes <plugin>` subcommand tree:

```
def_my_command(args):"""Handler for hermes my-plugin <subcommand>."""    sub =getattr(args,"my_command",None)if sub =="status":print("All good!")elif sub =="config":print("Current config: ...")else:print("Usage: hermes my-plugin <status|config>")def_setup_argparse(subparser):"""Build the argparse tree for hermes my-plugin."""    subs = subparser.add_subparsers(dest="my_command")    subs.add_parser("status",help="Show plugin status")    subs.add_parser("config",help="Show plugin config")    subparser.set_defaults(func=_my_command)defregister(ctx):    ctx.register_tool(...)    ctx.register_cli_command(        name="my-plugin",help="Manage my plugin",        setup_fn=_setup_argparse,        handler_fn=_my_command,
```

After registration, users can run `hermes my-plugin status`, `hermes my-plugin config`, etc.
**Memory provider plugins** use a convention-based approach instead: add a `register_cli(subparser)` function to your plugin's `cli.py` file. The memory plugin discovery system finds it automatically — no `ctx.register_cli_command()` call needed. See the [Memory Provider Plugin guide](https://hermes-agent.nousresearch.com/docs/developer-guide/memory-provider-plugin#adding-cli-commands) for details.
**Active-provider gating:** Memory plugin CLI commands only appear when their provider is the active `memory.provider` in config. If a user hasn't set up your provider, your CLI commands won't clutter the help output.
### Register slash commands[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#register-slash-commands "Direct link to Register slash commands")
Plugins can register in-session slash commands — commands users type during a conversation (like `/lcm status` or `/ping`). These work in both CLI and gateway (Telegram, Discord, etc.).

```
def_handle_status(raw_args:str)->str:"""Handler for /mystatus — called with everything after the command name."""if raw_args.strip()=="help":return"Usage: /mystatus [help|check]"return"Plugin status: all systems nominal"defregister(ctx):    ctx.register_command("mystatus",        handler=_handle_status,        description="Show plugin status",
```

After registration, users can type `/mystatus` in any session. The command appears in autocomplete, `/help` output, and the Telegram bot menu.
**Signature:** `ctx.register_command(name: str, handler: Callable, description: str = "")`  
| Parameter  | Type  | Description  |  
| --- | --- | --- |  
| `name`  | `str`  | Command name without the leading slash (e.g. `"lcm"`, `"mystatus"`)  |  
| `handler`  | `Callable[[str], str | None]`  | Called with the raw argument string. May also be `async`.  |  
| `description`  | `str`  | Shown in `/help`, autocomplete, and Telegram bot menu  |  
**Key differences from`register_cli_command()` :**  
| `register_command()`  | `register_cli_command()`  |  
| --- | --- |  
| Invoked as  |  `/name` in a session  |  `hermes name` in a terminal  |  
| Where it works  | CLI sessions, Telegram, Discord, etc.  | Terminal only  |  
| Handler receives  | Raw args string  | argparse `Namespace`  |  
| Use case  | Diagnostics, status, quick actions  | Complex subcommand trees, setup wizards  |  
**Conflict protection:** If a plugin tries to register a name that conflicts with a built-in command (`help`, `model`, `new`, etc.), the registration is silently rejected with a log warning. Built-in commands always take precedence.
**Async handlers:** The gateway dispatch automatically detects and awaits async handlers, so you can use either sync or async functions:

```
asyncdef_handle_check(raw_args:str)->str:    result =await some_async_operation()returnf"Check result: {result}"defregister(ctx):    ctx.register_command("check", handler=_handle_check, description="Run async check")
```

### Dispatch tools from slash commands[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#dispatch-tools-from-slash-commands "Direct link to Dispatch tools from slash commands")
Slash command handlers that need to orchestrate tools (spawn a subagent via `delegate_task`, call `file_edit`, etc.) should use `ctx.dispatch_tool()` instead of reaching into framework internals. The parent-agent context (workspace hints, spinner, model inheritance) is wired up automatically.

```
defregister(ctx):def_handle_deliver(raw_args:str):        result = ctx.dispatch_tool("delegate_task","goal": raw_args,"toolsets":["terminal","file","web"],return result    ctx.register_command("deliver",        handler=_handle_deliver,        description="Delegate a goal to a subagent",
```

**Signature:** `ctx.dispatch_tool(name: str, args: dict, *, parent_agent=None) -> str`  
| Parameter  | Type  | Description  |  
| --- | --- | --- |  
| `name`  | `str`  | Tool name as registered in the tool registry (e.g. `"delegate_task"`, `"file_edit"`)  |  
| `args`  | `dict`  | Tool arguments, same shape the model would send  |  
| `parent_agent`  | `Agent | None`  | Optional override. When omitted, resolves from the current CLI agent (or degrades gracefully in gateway mode)  |  
**Runtime behavior:**
  * **CLI mode:** `parent_agent` is resolved from the active CLI agent so workspace hints, spinner, and model selection inherit as expected.
  * **Gateway mode:** There is no CLI agent, so tools degrade gracefully — workspace is read from `TERMINAL_CWD` and no spinner is shown.
  * **Explicit override:** If the caller passes `parent_agent=` explicitly, it is respected and not overwritten.


This is the public, stable interface for tool dispatch from plugin commands. Plugins should not reach into `ctx._cli_ref.agent` or similar private state.
This guide covers **general plugins** (tools, hooks, slash commands, CLI commands). The sections below sketch the authoring pattern for each specialized plugin type; each links to its full guide for field reference and examples.
## Specialized plugin types[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#specialized-plugin-types "Direct link to Specialized plugin types")
Hermes has five specialized plugin types beyond the general surface. Each ships as a directory under `plugins/<category>/<name>/` (bundled) or `~/.hermes/plugins/<category>/<name>/` (user). The contract differs by category — pick the one you need, then read its full guide.
### Model provider plugins — add an LLM backend[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#model-provider-plugins--add-an-llm-backend "Direct link to Model provider plugins — add an LLM backend")
Drop a profile into `plugins/model-providers/<name>/`:

```
# plugins/model-providers/acme/__init__.pyfrom providers import register_providerfrom providers.base import ProviderProfileregister_provider(ProviderProfile(    name="acme",    aliases=("acme-inference",),    display_name="Acme Inference",    env_vars=("ACME_API_KEY","ACME_BASE_URL"),    base_url="https://api.acme.example.com/v1",    auth_type="api_key",    default_aux_model="acme-small-fast",    fallback_models=("acme-large-v3","acme-medium-v3"),
```


```
# plugins/model-providers/acme/plugin.yamlname: acme-providerkind: model-providerversion: 1.0.0description: Acme Inference — OpenAI-compatible direct API
```

Lazy-discovered the first time anything calls `get_provider_profile()` or `list_providers()` — `auth.py`, `config.py`, `doctor.py`, `models.py`, `runtime_provider.py`, and the chat_completions transport auto-wire to it. User plugins override bundled ones by name.
**Full guide:** [Model Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin) — field reference, overridable hooks (`prepare_messages`, `build_extra_body`, `build_api_kwargs_extras`, `fetch_models`), api_mode selection, auth types, testing.
### Platform plugins — add a gateway channel[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#platform-plugins--add-a-gateway-channel "Direct link to Platform plugins — add a gateway channel")
Drop an adapter into `plugins/platforms/<name>/`:

```
# plugins/platforms/myplatform/adapter.pyfrom gateway.platforms.base import BasePlatformAdapterclassMyPlatformAdapter(BasePlatformAdapter):asyncdefconnect(self):...asyncdefsend(self, chat_id, text):...asyncdefdisconnect(self):...defcheck_requirements():import osreturnbool(os.environ.get("MYPLATFORM_TOKEN"))def_env_enablement():import os    tok = os.getenv("MYPLATFORM_TOKEN","").strip()ifnot tok:returnNonereturn{"token": tok}defregister(ctx):    ctx.register_platform(        name="myplatform",        label="MyPlatform",        adapter_factory=lambda cfg: MyPlatformAdapter(cfg),        check_fn=check_requirements,        required_env=["MYPLATFORM_TOKEN"],# Auto-populate PlatformConfig.extra from env so env-only setups# show up in `hermes gateway status` without SDK instantiation.        env_enablement_fn=_env_enablement,# Opt in to cron delivery: `deliver=myplatform` routes to this var.        cron_deliver_env_var="MYPLATFORM_HOME_CHANNEL",        emoji="💬",        platform_hint="You are chatting via MyPlatform. Keep responses concise.",
```


```
# plugins/platforms/myplatform/plugin.yamlname: myplatform-platformlabel: MyPlatformkind: platformversion: 1.0.0description: MyPlatform gateway adapterrequires_env:-name: MYPLATFORM_TOKENdescription:"Bot token from the MyPlatform console"password:trueoptional_env:-name: MYPLATFORM_HOME_CHANNELdescription:"Default channel for cron delivery"password:false
```

**Full guide:** [Adding Platform Adapters](https://hermes-agent.nousresearch.com/docs/developer-guide/adding-platform-adapters) — complete `BasePlatformAdapter` contract, message routing, auth gating, setup wizard integration. Look at `plugins/platforms/irc/` for a stdlib-only working example.
### Memory provider plugins — add a cross-session knowledge backend[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#memory-provider-plugins--add-a-cross-session-knowledge-backend "Direct link to Memory provider plugins — add a cross-session knowledge backend")
Drop an implementation of `MemoryProvider` into `plugins/memory/<name>/`:

```
# plugins/memory/my-memory/__init__.pyfrom agent.memory_provider import MemoryProviderclassMyMemoryProvider(MemoryProvider):@propertydefname(self)->str:return"my-memory"defis_available(self)->bool:import osreturnbool(os.environ.get("MY_MEMORY_API_KEY"))definitialize(self, session_id:str,**kwargs)->None:        self._session_id = session_iddefsync_turn(self, user_message, assistant_response,**kwargs)->None:...defprefetch(self, query:str,**kwargs)->str|None:...defregister(ctx):    ctx.register_memory_provider(MyMemoryProvider())
```

Memory providers are single-select — only one is active at a time, chosen via `memory.provider` in `config.yaml`.
**Full guide:** [Memory Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/memory-provider-plugin) — full `MemoryProvider` ABC, threading contract, profile isolation, CLI command registration via `cli.py`.
### Context engine plugins — replace the context compressor[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#context-engine-plugins--replace-the-context-compressor "Direct link to Context engine plugins — replace the context compressor")

```
# plugins/context_engine/my-engine/__init__.pyfrom agent.context_engine import ContextEngineclassMyContextEngine(ContextEngine):@propertydefname(self)->str:return"my-engine"defshould_compress(self, messages, model)->bool:...defcompress(self, messages, model)->list[dict]:...defregister(ctx):    ctx.register_context_engine(MyContextEngine())
```

Context engines are single-select — chosen via `context.engine` in `config.yaml`.
**Full guide:** [Context Engine Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/context-engine-plugin).
### Image-generation backends[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#image-generation-backends "Direct link to Image-generation backends")
Drop a provider into `plugins/image_gen/<name>/`:

```
# plugins/image_gen/my-imggen/__init__.pyfrom agent.image_gen_provider import ImageGenProviderclassMyImageGenProvider(ImageGenProvider):@propertydefname(self)->str:return"my-imggen"defis_available(self)->bool:...defgenerate(self, prompt:str,**kwargs)->str:...# returns image pathdefregister(ctx):    ctx.register_image_gen_provider(MyImageGenProvider())
```


```
# plugins/image_gen/my-imggen/plugin.yamlname: my-imggenkind: backendversion: 1.0.0description: Custom image generation backend
```

**Full guide:** [Image Generation Provider Plugins](https://hermes-agent.nousresearch.com/docs/developer-guide/image-gen-provider-plugin) — full `ImageGenProvider` ABC, `list_models()` / `get_setup_schema()` metadata, `success_response()`/`error_response()` helpers, base64 vs URL output, user overrides, pip distribution.
**Reference examples:** `plugins/image_gen/openai/` (DALL-E / GPT-Image via OpenAI SDK), `plugins/image_gen/openai-codex/`, `plugins/image_gen/xai/` (Grok image gen).
## Non-Python extension surfaces[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#non-python-extension-surfaces "Direct link to Non-Python extension surfaces")
Hermes also accepts extensions that aren't Python plugins at all. These are shown in the [Pluggable interfaces table](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins#pluggable-interfaces--where-to-go-for-each); the sections below sketch each authoring style briefly.
### MCP servers — register external tools[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#mcp-servers--register-external-tools "Direct link to MCP servers — register external tools")
Model Context Protocol (MCP) servers register their own tools into Hermes without any Python plugin. Declare them in `~/.hermes/config.yaml`:

```
mcp_servers:filesystem:command:"npx"args:["-y","@modelcontextprotocol/server-filesystem","/home/user/projects"]timeout:120linear:url:"https://mcp.linear.app/sse"auth:type:"oauth"
```

Hermes connects to each server at startup, lists its tools, and registers them alongside built-ins. The LLM sees them exactly like any other tool. **Full guide:** [MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp).
### Gateway event hooks — fire on lifecycle events[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#gateway-event-hooks--fire-on-lifecycle-events "Direct link to Gateway event hooks — fire on lifecycle events")
Drop a manifest + handler into `~/.hermes/hooks/<name>/`:

```
# ~/.hermes/hooks/long-task-alert/HOOK.yamlname: long-task-alertdescription: Send a push notification when a long task finishesevents:- agent:end
```


```
# ~/.hermes/hooks/long-task-alert/handler.pyasyncdefhandle(event_type:str, context:dict)->None:if context.get("duration_seconds",0)>120:# send notification …pass
```

Events include `gateway:startup`, `session:start`, `session:end`, `session:reset`, `agent:start`, `agent:step`, `agent:end`, and wildcard `command:*`. Errors in hooks are caught and logged — they never block the main pipeline.
**Full guide:** [Gateway Event Hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#gateway-event-hooks).
### Shell hooks — run a shell command on tool calls[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#shell-hooks--run-a-shell-command-on-tool-calls "Direct link to Shell hooks — run a shell command on tool calls")
If you just want to run a script when a tool fires (notifications, audit logs, desktop alerts, auto-formatters), use shell hooks in `config.yaml` — no Python required:

```
hooks:-event: post_tool_callcommand:"notify-send 'Tool ran: {tool_name}'"when:tools:[terminal, patch, write_file]
```

Supports all the same events as Python plugin hooks (`pre_tool_call`, `post_tool_call`, `pre_llm_call`, `post_llm_call`, `on_session_start`, `on_session_end`, `pre_gateway_dispatch`) plus structured JSON output for `pre_tool_call` blocking decisions.
**Full guide:** [Shell Hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks#shell-hooks).
### Skill sources — add a custom skill registry[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#skill-sources--add-a-custom-skill-registry "Direct link to Skill sources — add a custom skill registry")
If you maintain a GitHub repo of skills (or want to pull from a community index beyond the built-in sources), add it as a **tap** :

```
hermes skills tap add myorg/skills-repohermes skills search my-workflow --source myorg/skills-repohermes skills install myorg/skills-repo/my-workflow
```

Publishing your own tap is just a GitHub repo with `skills/<skill-name>/SKILL.md` directories — no server or registry signup needed.
**Full guides:** [Skills Hub](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#skills-hub) · [Publishing a custom tap](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills#publishing-a-custom-skill-tap) (repo layout, minimal example, non-default paths, trust levels).
### TTS / STT via command templates[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#tts--stt-via-command-templates "Direct link to TTS / STT via command templates")
Any CLI that reads/writes audio or text can be plugged in through `config.yaml` — no Python code:

```
tts:provider: voxcpmproviders:voxcpm:type: commandcommand:"voxcpm --ref ~/voice.wav --text-file {input_path} --out {output_path}"output_format: mp3voice_compatible:true
```

For STT, point `HERMES_LOCAL_STT_COMMAND` at a shell template. Supported placeholders: `{input_path}`, `{output_path}`, `{format}`, `{voice}`, `{model}`, `{speed}` (TTS); `{input_path}`, `{output_dir}`, `{language}`, `{model}` (STT). Any path-interacting CLI is automatically a plugin.
**Full guides:** [TTS custom command providers](https://hermes-agent.nousresearch.com/docs/user-guide/features/tts#custom-command-providers) · [STT](https://hermes-agent.nousresearch.com/docs/user-guide/features/tts#voice-message-transcription-stt).
## Distribute via pip[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#distribute-via-pip "Direct link to Distribute via pip")
For sharing plugins publicly, add an entry point to your Python package:

```
# pyproject.toml[project.entry-points."hermes_agent.plugins"]my-plugin="my_plugin_package"
```


```
pip install hermes-plugin-calculator# Plugin auto-discovered on next hermes startup
```

## Distribute for NixOS[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#distribute-for-nixos "Direct link to Distribute for NixOS")
NixOS users can install your plugin declaratively if you provide a `pyproject.toml` with entry points:
**Entry-point plugins** (recommended for distribution):

```
# User's configuration.nixservices.hermes-agent.extraPythonPackages = [  (pkgs.python312Packages.buildPythonPackage {    pname = "my-plugin";    version = "1.0.0";    src = pkgs.fetchFromGitHub {      owner = "you";      repo = "hermes-my-plugin";      rev = "v1.0.0";      hash = "sha256-...";  # nix-prefetch-url --unpack    format = "pyproject";    build-system = [ pkgs.python312Packages.setuptools ];
```

**Directory plugins** (no `pyproject.toml` needed):

```
services.hermes-agent.extraPlugins = [  (pkgs.fetchFromGitHub {    owner = "you";    repo = "hermes-my-plugin";    rev = "v1.0.0";    hash = "sha256-...";
```

See the [Nix Setup guide](https://hermes-agent.nousresearch.com/docs/getting-started/nix-setup#plugins) for complete documentation including overlay usage and collision checking.
## Common mistakes[​](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#common-mistakes "Direct link to Common mistakes")
**Handler doesn't return JSON string:**

```
# Wrong — returns a dictdefhandler(args,**kwargs):return{"result":42}# Right — returns a JSON stringdefhandler(args,**kwargs):return json.dumps({"result":42})
```

**Missing`**kwargs` in handler signature:**

```
# Wrong — will break if Hermes passes extra contextdefhandler(args):...# Rightdefhandler(args,**kwargs):...
```

**Handler raises exceptions:**

```
# Wrong — exception propagates, tool call failsdefhandler(args,**kwargs):    result =1/int(args["value"])# ZeroDivisionError!return json.dumps({"result": result})# Right — catch and return error JSONdefhandler(args,**kwargs):try:        result =1/int(args.get("value",0))return json.dumps({"result": result})except Exception as e:return json.dumps({"error":str(e)})
```

**Schema description too vague:**

```
# Bad — model doesn't know when to use it"description":"Does stuff"# Good — model knows exactly when and how"description":"Evaluate a mathematical expression. Use for arithmetic, trig, logarithms. Supports: +, -, *, /, **, sqrt, sin, cos, log, pi, e."
```

  * [What you're building](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#what-youre-building)
  * [Step 1: Create the plugin directory](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-1-create-the-plugin-directory)
  * [Step 2: Write the manifest](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-2-write-the-manifest)
  * [Step 3: Write the tool schemas](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-3-write-the-tool-schemas)
  * [Step 4: Write the tool handlers](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-4-write-the-tool-handlers)
  * [Step 5: Write the registration](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-5-write-the-registration)
  * [Step 6: Test it](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#step-6-test-it)
    * [Debugging plugin discovery](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#debugging-plugin-discovery)
  * [Your plugin's final structure](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#your-plugins-final-structure)
  * [What else can plugins do?](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#what-else-can-plugins-do)
    * [Ship data files](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#ship-data-files)
    * [Bundle skills](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#bundle-skills)
    * [Gate on environment variables](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#gate-on-environment-variables)
    * [Conditional tool availability](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#conditional-tool-availability)
    * [Register multiple hooks](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#register-multiple-hooks)
    * [Hook reference](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#hook-reference)
    * [`pre_llm_call` context injection](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#pre_llm_call-context-injection)
    * [Register CLI commands](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#register-cli-commands)
    * [Register slash commands](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#register-slash-commands)
    * [Dispatch tools from slash commands](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#dispatch-tools-from-slash-commands)
  * [Specialized plugin types](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#specialized-plugin-types)
    * [Model provider plugins — add an LLM backend](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#model-provider-plugins--add-an-llm-backend)
    * [Platform plugins — add a gateway channel](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#platform-plugins--add-a-gateway-channel)
    * [Memory provider plugins — add a cross-session knowledge backend](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#memory-provider-plugins--add-a-cross-session-knowledge-backend)
    * [Context engine plugins — replace the context compressor](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#context-engine-plugins--replace-the-context-compressor)
    * [Image-generation backends](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#image-generation-backends)
  * [Non-Python extension surfaces](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#non-python-extension-surfaces)
    * [MCP servers — register external tools](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#mcp-servers--register-external-tools)
    * [Gateway event hooks — fire on lifecycle events](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#gateway-event-hooks--fire-on-lifecycle-events)
    * [Shell hooks — run a shell command on tool calls](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#shell-hooks--run-a-shell-command-on-tool-calls)
    * [Skill sources — add a custom skill registry](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#skill-sources--add-a-custom-skill-registry)
    * [TTS / STT via command templates](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#tts--stt-via-command-templates)
  * [Distribute via pip](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#distribute-via-pip)
  * [Distribute for NixOS](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#distribute-for-nixos)
  * [Common mistakes](https://hermes-agent.nousresearch.com/docs/guides/build-a-hermes-plugin#common-mistakes)


