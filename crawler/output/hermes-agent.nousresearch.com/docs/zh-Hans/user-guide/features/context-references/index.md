<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references -->

本页总览
Type `@` followed by a reference to inject content directly into your message. Hermes expands the reference inline and appends the content under an `--- Attached Context ---` section.
## Supported References[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#supported-references "Supported References的直接链接")  
| Syntax  | Description  |  
| --- | --- |  
| `@file:path/to/file.py`  | Inject file contents  |  
| `@file:path/to/file.py:10-25`  | Inject specific line range (1-indexed, inclusive)  |  
| `@folder:path/to/dir`  | Inject directory tree listing with file metadata  |  
| `@diff`  | Inject `git diff` (unstaged working tree changes)  |  
| `@staged`  | Inject `git diff --staged` (staged changes)  |  
| `@git:5`  | Inject last N commits with patches (max 10)  |  
| `@url:https://example.com`  | Fetch and inject web page content  |  
## Usage Examples[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#usage-examples "Usage Examples的直接链接")

```
Review @file:src/main.py and suggest improvementsWhat changed? @diffCompare @file:old_config.yaml and @file:new_config.yamlWhat's in @folder:src/components?Summarize this article @url:https://arxiv.org/abs/2301.00001
```

Multiple references work in a single message:

```
Check @file:main.py, and also @file:test.py.
```

Trailing punctuation (`,`, `.`, `;`, `!`, `?`) is automatically stripped from reference values.
## CLI Tab Completion[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#cli-tab-completion "CLI Tab Completion的直接链接")
In the interactive CLI, typing `@` triggers autocomplete:
  * `@` shows all reference types (`@diff`, `@staged`, `@file:`, `@folder:`, `@git:`, `@url:`)
  * `@file:` and `@folder:` trigger filesystem path completion with file size metadata
  * Bare `@` followed by partial text shows matching files and folders from the current directory


## Line Ranges[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#line-ranges "Line Ranges的直接链接")
The `@file:` reference supports line ranges for precise content injection:

```
@file:src/main.py:42        # Single line 42@file:src/main.py:10-25     # Lines 10 through 25 (inclusive)
```

Lines are 1-indexed. Invalid ranges are silently ignored (full file is returned).
## Size Limits[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#size-limits "Size Limits的直接链接")
Context references are bounded to prevent overwhelming the model's context window:  
| Threshold  | Value  | Behavior  |  
| --- | --- | --- |  
| Soft limit  | 25% of context length  | Warning appended, expansion proceeds  |  
| Hard limit  | 50% of context length  | Expansion refused, original message returned unchanged  |  
| Folder entries  | 200 files max  | Excess entries replaced with `- ...`  |  
| Git commits  | 10 max  |  `@git:N` clamped to range [1, 10]  |  
## Security[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#security "Security的直接链接")
### Sensitive Path Blocking[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#sensitive-path-blocking "Sensitive Path Blocking的直接链接")
These paths are always blocked from `@file:` references to prevent credential exposure:
  * SSH keys and config: `~/.ssh/id_rsa`, `~/.ssh/id_ed25519`, `~/.ssh/authorized_keys`, `~/.ssh/config`
  * Shell profiles: `~/.bashrc`, `~/.zshrc`, `~/.profile`, `~/.bash_profile`, `~/.zprofile`
  * Credential files: `~/.netrc`, `~/.pgpass`, `~/.npmrc`, `~/.pypirc`
  * Hermes env: `$HERMES_HOME/.env`


These directories are fully blocked (any file inside):
  * `~/.ssh/`, `~/.aws/`, `~/.gnupg/`, `~/.kube/`, `$HERMES_HOME/skills/.hub/`


### Path Traversal Protection[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#path-traversal-protection "Path Traversal Protection的直接链接")
All paths are resolved relative to the working directory. References that resolve outside the allowed workspace root are rejected.
### Binary File Detection[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#binary-file-detection "Binary File Detection的直接链接")
Binary files are detected via MIME type and null-byte scanning. Known text extensions (`.py`, `.md`, `.json`, `.yaml`, `.toml`, `.js`, `.ts`, etc.) bypass MIME-based detection. Binary files are rejected with a warning.
## Platform Availability[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#platform-availability "Platform Availability的直接链接")
Context references are primarily a **CLI feature**. They work in the interactive CLI where `@` triggers tab completion and references are expanded before the message is sent to the agent.
In **messaging platforms** (Telegram, Discord, etc.), the `@` syntax is not expanded by the gateway — messages are passed through as-is. The agent itself can still reference files via the `read_file`, `search_files`, and `web_extract` tools.
## Interaction with Context Compression[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#interaction-with-context-compression "Interaction with Context Compression的直接链接")
When conversation context is compressed, the expanded reference content is included in the compression summary. This means:
  * Large file contents injected via `@file:` contribute to context usage
  * If the conversation is later compressed, the file content is summarized (not preserved verbatim)
  * For very large files, consider using line ranges (`@file:main.py:100-200`) to inject only relevant sections


## Common Patterns[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#common-patterns "Common Patterns的直接链接")

```
# Code review workflowReview @diff and check for security issues# Debug with contextThis test is failing. Here's the test @file:tests/test_auth.pyand the implementation @file:src/auth.py:50-80# Project explorationWhat does this project do? @folder:src @file:README.md# ResearchCompare the approaches in @url:https://arxiv.org/abs/2301.00001and @url:https://arxiv.org/abs/2301.00002
```

## Error Handling[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#error-handling "Error Handling的直接链接")
Invalid references produce inline warnings rather than failures:  
| Condition  | Behavior  |  
| --- | --- |  
| File not found  | Warning: "file not found"  |  
| Binary file  | Warning: "binary files are not supported"  |  
| Folder not found  | Warning: "folder not found"  |  
| Git command fails  | Warning with git stderr  |  
| URL returns no content  | Warning: "no content extracted"  |  
| Sensitive path  | Warning: "path is a sensitive credential file"  |  
| Path outside workspace  | Warning: "path is outside the allowed workspace"  |  
  * [Supported References](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#supported-references)
  * [Usage Examples](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#usage-examples)
  * [CLI Tab Completion](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#cli-tab-completion)
  * [Line Ranges](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#line-ranges)
  * [Size Limits](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#size-limits)
  * [Security](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#security)
    * [Sensitive Path Blocking](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#sensitive-path-blocking)
    * [Path Traversal Protection](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#path-traversal-protection)
    * [Binary File Detection](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#binary-file-detection)
  * [Platform Availability](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#platform-availability)
  * [Interaction with Context Compression](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#interaction-with-context-compression)
  * [Common Patterns](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#common-patterns)
  * [Error Handling](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/context-references#error-handling)


