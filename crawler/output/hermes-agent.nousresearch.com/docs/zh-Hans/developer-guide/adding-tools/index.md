<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools -->

本页总览
Before writing a tool, ask yourself: **should this be a[skill](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/creating-skills) instead?**
This page is for adding a **built-in Hermes tool** to the repository itself. If you want a personal, project-local, or otherwise custom tool without modifying Hermes core, use the plugin route instead:
  * [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/guides/build-a-hermes-plugin)


Default to plugins for most custom tool creation. Only follow this page when you explicitly want to ship a new built-in tool in `tools/` and `toolsets.py`.
Make it a **Skill** when the capability can be expressed as instructions + shell commands + existing tools (arXiv search, git workflows, Docker management, PDF processing).
Make it a **Tool** when it requires end-to-end integration with API keys, custom processing logic, binary data handling, or streaming (browser automation, TTS, vision analysis).
## Overview[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#overview "Overview的直接链接")
Adding a tool touches **2 files** :
  1. **`tools/your_tool.py`**— handler, schema, check function,`registry.register()` call
  2. **`toolsets.py`**— add tool name to`_HERMES_CORE_TOOLS` (or a specific toolset)


Any `tools/*.py` file with a top-level `registry.register()` call is auto-discovered at startup — no manual import list required.
## Step 1: Create the Built-in Tool File[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#step-1-create-the-built-in-tool-file "Step 1: Create the Built-in Tool File的直接链接")
Every tool file follows the same structure:

```
# tools/weather_tool.py"""Weather Tool -- look up current weather for a location."""import jsonimport osimport logginglogger = logging.getLogger(__name__)# --- Availability check ---defcheck_weather_requirements()->bool:"""Return True if the tool's dependencies are available."""returnbool(os.getenv("WEATHER_API_KEY"))# --- Handler ---defweather_tool(location:str, units:str="metric")->str:"""Fetch weather for a location. Returns JSON string."""    api_key = os.getenv("WEATHER_API_KEY")ifnot api_key:return json.dumps({"error":"WEATHER_API_KEY not configured"})try:# ... call weather API ...return json.dumps({"location": location,"temp":22,"units": units})except Exception as e:return json.dumps({"error":str(e)})# --- Schema ---WEATHER_SCHEMA ={"name":"weather","description":"Get current weather for a location.","parameters":{"type":"object","properties":{"location":{"type":"string","description":"City name or coordinates (e.g. 'London' or '51.5,-0.1')""units":{"type":"string","enum":["metric","imperial"],"description":"Temperature units (default: metric)","default":"metric""required":["location"]# --- Registration ---from tools.registry import registryregistry.register(    name="weather",    toolset="weather",    schema=WEATHER_SCHEMA,    handler=lambda args,**kw: weather_tool(        location=args.get("location",""),        units=args.get("units","metric")),    check_fn=check_weather_requirements,    requires_env=["WEATHER_API_KEY"],
```

### Key Rules[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#key-rules "Key Rules的直接链接")
  * Handlers **MUST** return a JSON string (via `json.dumps()`), never raw dicts
  * Errors **MUST** be returned as `{"error": "message"}`, never raised as exceptions
  * The `check_fn` is called when building tool definitions — if it returns `False`, the tool is silently excluded
  * The `handler` receives `(args: dict, **kwargs)` where `args` is the LLM's tool call arguments


## Step 2: Add the Built-in Tool to a Toolset[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#step-2-add-the-built-in-tool-to-a-toolset "Step 2: Add the Built-in Tool to a Toolset的直接链接")
In `toolsets.py`, add the tool name:

```
# If it should be available on all platforms (CLI + messaging):_HERMES_CORE_TOOLS =[..."weather",# <-- add here# Or create a new standalone toolset:"weather":{"description":"Weather lookup tools","tools":["weather"],"includes":[]
```

##  ~~Step 3: Add Discovery Import~~ (No longer needed)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#step-3-add-discovery-import-no-longer-needed "step-3-add-discovery-import-no-longer-needed的直接链接")
Tool modules with a top-level `registry.register()` call are auto-discovered by `discover_builtin_tools()` in `tools/registry.py`. No manual import list to maintain — just create your file in `tools/` and it's picked up at startup.
## Async Handlers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#async-handlers "Async Handlers的直接链接")
If your handler needs async code, mark it with `is_async=True`:

```
asyncdefweather_tool_async(location:str)->str:asyncwith aiohttp.ClientSession()as session:...return json.dumps(result)registry.register(    name="weather",    toolset="weather",    schema=WEATHER_SCHEMA,    handler=lambda args,**kw: weather_tool_async(args.get("location","")),    check_fn=check_weather_requirements,    is_async=True,# registry calls _run_async() automatically
```

The registry handles async bridging transparently — you never call `asyncio.run()` yourself.
## Handlers That Need task_id[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#handlers-that-need-task_id "Handlers That Need task_id的直接链接")
Tools that manage per-session state receive `task_id` via `**kwargs`:

```
def_handle_weather(args,**kw):    task_id = kw.get("task_id")return weather_tool(args.get("location",""), task_id=task_id)registry.register(    name="weather",...    handler=_handle_weather,
```

## Agent-Loop Intercepted Tools[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#agent-loop-intercepted-tools "Agent-Loop Intercepted Tools的直接链接")
Some tools (`todo`, `memory`, `session_search`, `delegate_task`) need access to per-session agent state. These are intercepted by `run_agent.py` before reaching the registry. The registry still holds their schemas, but `dispatch()` returns a fallback error if the intercept is bypassed.
## Optional: Setup Wizard Integration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#optional-setup-wizard-integration "Optional: Setup Wizard Integration的直接链接")
If your tool requires an API key, add it to `hermes_cli/config.py`:

```
OPTIONAL_ENV_VARS ={..."WEATHER_API_KEY":{"description":"Weather API key for weather lookup","prompt":"Weather API key","url":"https://weatherapi.com/","tools":["weather"],"password":True,
```

## Checklist[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#checklist "Checklist的直接链接")
  * Tool file created with handler, schema, check function, and registration
  * Added to appropriate toolset in `toolsets.py`
  * Confirmed this really should be a built-in/core tool and not a plugin
  * Handler returns JSON strings, errors returned as `{"error": "..."}`
  * Optional: API key added to `OPTIONAL_ENV_VARS` in `hermes_cli/config.py`
  * Optional: Added to `toolset_distributions.py` for batch processing
  * Tested with `hermes chat -q "Use the weather tool for London"`


  * [Step 1: Create the Built-in Tool File](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#step-1-create-the-built-in-tool-file)
  * [Step 2: Add the Built-in Tool to a Toolset](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#step-2-add-the-built-in-tool-to-a-toolset)
  * [~~Step 3: Add Discovery Import~~ (No longer needed)](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#step-3-add-discovery-import-no-longer-needed)
  * [Async Handlers](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#async-handlers)
  * [Handlers That Need task_id](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#handlers-that-need-task_id)
  * [Agent-Loop Intercepted Tools](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#agent-loop-intercepted-tools)
  * [Optional: Setup Wizard Integration](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools#optional-setup-wizard-integration)


