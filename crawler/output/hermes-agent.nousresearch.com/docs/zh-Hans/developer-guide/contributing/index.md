<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing -->

本页总览
Thank you for contributing to Hermes Agent! This guide covers setting up your dev environment, understanding the codebase, and getting your PR merged.
## Contribution Priorities[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#contribution-priorities "Contribution Priorities的直接链接")
We value contributions in this order:
  1. **Bug fixes** — crashes, incorrect behavior, data loss
  2. **Cross-platform compatibility** — macOS, different Linux distros, WSL2
  3. **Security hardening** — shell injection, prompt injection, path traversal
  4. **Performance and robustness** — retry logic, error handling, graceful degradation
  5. **New skills** — broadly useful ones (see [Creating Skills](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/creating-skills))
  6. **New tools** — rarely needed; most capabilities should be skills
  7. **Documentation** — fixes, clarifications, new examples


## Common contribution paths[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#common-contribution-paths "Common contribution paths的直接链接")
  * Building a custom/local tool without modifying Hermes core? Start with [Build a Hermes Plugin](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/build-a-hermes-plugin)
  * Building a new built-in core tool for Hermes itself? Start with [Adding Tools](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-tools)
  * Building a new skill? Start with [Creating Skills](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/creating-skills)
  * Building a new inference provider? Start with [Adding Providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/adding-providers)


## Development Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#development-setup "Development Setup的直接链接")
### Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#prerequisites "Prerequisites的直接链接")  
| Requirement  | Notes  |  
| --- | --- |  
| **Git**  | With `--recurse-submodules` support, and the `git-lfs` extension installed  |  
| **Python 3.11+**  | uv will install it if missing  |  
| **uv**  | Fast Python package manager ([install](https://docs.astral.sh/uv/))  |  
| **Node.js 20+**  | Optional — needed for browser tools and WhatsApp bridge (matches root `package.json` engines)  |  
### Clone and Install[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#clone-and-install "Clone and Install的直接链接")

```
git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.gitcd hermes-agent# Create venv with Python 3.11uv venv venv --python3.11exportVIRTUAL_ENV="$(pwd)/venv"# Install with all extras (messaging, cron, CLI menus, dev tools)uv pip install-e".[all,dev]"# tinker-atropos is a git submodule — needs `git submodule update --init` first# if you didn't clone with `--recurse-submodules`uv pip install-e"./tinker-atropos"# Optional: browser toolsnpminstall
```

### Configure for Development[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#configure-for-development "Configure for Development的直接链接")

```
mkdir-p ~/.hermes/{cron,sessions,logs,memories,skills}cp cli-config.yaml.example ~/.hermes/config.yamltouch ~/.hermes/.env# Add at minimum an LLM provider key:echo'OPENROUTER_API_KEY=sk-or-v1-your-key'>> ~/.hermes/.env
```

### Run[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#run "Run的直接链接")

```
# Symlink for global accessmkdir-p ~/.local/binln-sf"$(pwd)/venv/bin/hermes" ~/.local/bin/hermes# Verifyhermes doctorhermes chat -q"Hello"
```

### Run Tests[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#run-tests "Run Tests的直接链接")

```
pytest tests/ -v
```

## Code Style[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#code-style "Code Style的直接链接")
  * **PEP 8** with practical exceptions (no strict line length enforcement)
  * **Comments** : Only when explaining non-obvious intent, trade-offs, or API quirks
  * **Error handling** : Catch specific exceptions. Use `logger.warning()`/`logger.error()` with `exc_info=True` for unexpected errors
  * **Cross-platform** : Never assume Unix (see below)
  * **Profile-safe paths** : Never hardcode `~/.hermes` — use `get_hermes_home()` from `hermes_constants` for code paths and `display_hermes_home()` for user-facing messages. See [AGENTS.md](https://github.com/NousResearch/hermes-agent/blob/main/AGENTS.md#profiles-multi-instance-support) for full rules.


## Cross-Platform Compatibility[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#cross-platform-compatibility "Cross-Platform Compatibility的直接链接")
Hermes officially supports **Linux, macOS, WSL2, and native Windows (early beta — via PowerShell install)**. Native Windows uses Git Bash (from [Git for Windows](https://git-scm.com/download/win)) for shell commands. A few features require POSIX kernel primitives and are gated: the dashboard's embedded PTY terminal pane (`/chat` tab) is WSL2-only. The native-Windows path is new and moves fast — if you're doing Windows-heavy dev, expect to hit and fix rough edges.
When contributing code, keep these rules in mind:
  * **Don't add unguarded`signal.SIGKILL` references.** It's not defined on Windows. Either route through `gateway.status.terminate_pid(pid, force=True)` (the centralized primitive that does `taskkill /T /F` on Windows and SIGKILL on POSIX), or fall back with `getattr(signal, "SIGKILL", signal.SIGTERM)`.
  * **Catch`OSError` alongside `ProcessLookupError` on `os.kill(pid, 0)` probes.** Windows raises `OSError` (WinError 87, "parameter is incorrect") for an already-gone PID instead of `ProcessLookupError`.
  * **Don't force the terminal to POSIX semantics.** `os.setsid`, `os.killpg`, `os.getpgid`, `os.fork` all raise on Windows — gate them with `if sys.platform != "win32":` or `if os.name != "nt":`.
  * **Open files with an explicit`encoding="utf-8"`.** The Python default on Windows is the system locale (often cp1252), which mojibakes or crashes on non-Latin text.
  * **Use`pathlib.Path` / `os.path.join` — never manually concat with `/`.** This matters less for strings the OS gives us back and more for strings we construct to hand to subprocesses.


Key patterns:
### 1. `termios` and `fcntl` are Unix-only[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#1-termios-and-fcntl-are-unix-only "1-termios-and-fcntl-are-unix-only的直接链接")
Always catch both `ImportError` and `NotImplementedError`:

```
try:from simple_term_menu import TerminalMenu    menu = TerminalMenu(options)    idx = menu.show()except(ImportError, NotImplementedError):# Fallback: numbered menufor i, opt inenumerate(options):print(f"  {i+1}. {opt}")    idx =int(input("Choice: "))-1
```

### 2. File encoding[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#2-file-encoding "2. File encoding的直接链接")
Some environments may save `.env` files in non-UTF-8 encodings:

```
try:    load_dotenv(env_path)except UnicodeDecodeError:    load_dotenv(env_path, encoding="latin-1")
```

### 3. Process management[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#3-process-management "3. Process management的直接链接")
`os.setsid()`, `os.killpg()`, and signal handling differ across platforms:

```
import platformif platform.system()!="Windows":    kwargs["preexec_fn"]= os.setsid
```

### 4. Path separators[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#4-path-separators "4. Path separators的直接链接")
Use `pathlib.Path` instead of string concatenation with `/`.
## Security Considerations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#security-considerations "Security Considerations的直接链接")
Hermes has terminal access. Security matters.
### Existing Protections[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#existing-protections "Existing Protections的直接链接")  
| Layer  | Implementation  |  
| --- | --- |  
| **Sudo password piping**  | Uses `shlex.quote()` to prevent shell injection  |  
| **Dangerous command detection**  | Regex patterns in `tools/approval.py` with user approval flow  |  
| **Cron prompt injection**  | Scanner blocks instruction-override patterns  |  
| **Write deny list**  | Protected paths resolved via `os.path.realpath()` to prevent symlink bypass  |  
| **Skills guard**  | Security scanner for hub-installed skills  |  
| **Code execution sandbox**  | Child process runs with API keys stripped  |  
| **Container hardening**  | Docker: all capabilities dropped, no privilege escalation, PID limits  |  
### Contributing Security-Sensitive Code[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#contributing-security-sensitive-code "Contributing Security-Sensitive Code的直接链接")
  * Always use `shlex.quote()` when interpolating user input into shell commands
  * Resolve symlinks with `os.path.realpath()` before access control checks
  * Don't log secrets
  * Catch broad exceptions around tool execution
  * Test on all platforms if your change touches file paths or processes


## Pull Request Process[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#pull-request-process "Pull Request Process的直接链接")
### Branch Naming[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#branch-naming "Branch Naming的直接链接")

```
fix/description        # Bug fixesfeat/description       # New featuresdocs/description       # Documentationtest/description       # Testsrefactor/description   # Code restructuring
```

### Before Submitting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#before-submitting "Before Submitting的直接链接")
  1. **Run tests** : `pytest tests/ -v`
  2. **Test manually** : Run `hermes` and exercise the code path you changed
  3. **Check cross-platform impact** : Consider macOS and different Linux distros
  4. **Keep PRs focused** : One logical change per PR


### PR Description[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#pr-description "PR Description的直接链接")
Include:
  * **What** changed and **why**
  * **How to test** it
  * **What platforms** you tested on
  * Reference any related issues


### Commit Messages[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#commit-messages "Commit Messages的直接链接")
We use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>
```
  
| Type  | Use for  |  
| --- | --- |  
| `fix`  | Bug fixes  |  
| `feat`  | New features  |  
| `docs`  | Documentation  |  
| `test`  | Tests  |  
| `refactor`  | Code restructuring  |  
| `chore`  | Build, CI, dependency updates  |  
Scopes: `cli`, `gateway`, `tools`, `skills`, `agent`, `install`, `whatsapp`, `security`
Examples:

```
fix(cli): prevent crash in save_config_value when model is a stringfeat(gateway): add WhatsApp multi-user session isolationfix(security): prevent shell injection in sudo password piping
```

## Reporting Issues[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#reporting-issues "Reporting Issues的直接链接")
  * Use [GitHub Issues](https://github.com/NousResearch/hermes-agent/issues)
  * Include: OS, Python version, Hermes version (`hermes version`), full error traceback
  * Include steps to reproduce
  * Check existing issues before creating duplicates
  * For security vulnerabilities, please report privately


## Community[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#community "Community的直接链接")
  * **Discord** : [discord.gg/NousResearch](https://discord.gg/NousResearch)
  * **GitHub Discussions** : For design proposals and architecture discussions
  * **Skills Hub** : Upload specialized skills and share with the community


## License[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#license "License的直接链接")
By contributing, you agree that your contributions will be licensed under the [MIT License](https://github.com/NousResearch/hermes-agent/blob/main/LICENSE).
  * [Contribution Priorities](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#contribution-priorities)
  * [Common contribution paths](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#common-contribution-paths)
  * [Development Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#development-setup)
    * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#prerequisites)
    * [Clone and Install](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#clone-and-install)
    * [Configure for Development](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#configure-for-development)
  * [Cross-Platform Compatibility](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#cross-platform-compatibility)
    * [1. `termios` and `fcntl` are Unix-only](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#1-termios-and-fcntl-are-unix-only)
    * [2. File encoding](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#2-file-encoding)
    * [3. Process management](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#3-process-management)
    * [4. Path separators](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#4-path-separators)
  * [Security Considerations](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#security-considerations)
    * [Existing Protections](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#existing-protections)
    * [Contributing Security-Sensitive Code](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#contributing-security-sensitive-code)
  * [Pull Request Process](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#pull-request-process)
    * [Branch Naming](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#branch-naming)
    * [Before Submitting](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#before-submitting)
    * [PR Description](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#pr-description)
    * [Commit Messages](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#commit-messages)
  * [Reporting Issues](https://hermes-agent.nousresearch.com/docs/zh-Hans/developer-guide/contributing#reporting-issues)


