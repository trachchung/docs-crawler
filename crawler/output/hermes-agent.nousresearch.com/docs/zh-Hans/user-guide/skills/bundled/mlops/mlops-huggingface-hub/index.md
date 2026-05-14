<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub -->

本页总览
HuggingFace hf CLI: search/download/upload models, datasets.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/mlops/huggingface-hub`  |  
| Version  | `1.0.0`  |  
| Author  | Hugging Face  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Hugging Face CLI (`hf`) Reference Guide
The `hf` command is the modern command-line interface for interacting with the Hugging Face Hub, providing tools to manage repositories, models, datasets, and Spaces.
> **IMPORTANT:** The `hf` command replaces the now deprecated `huggingface-cli` command.
## Quick Start[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#quick-start "Quick Start的直接链接")
  * **Installation:** `curl -LsSf https://hf.co/cli/install.sh | bash -s`
  * **Help:** Use `hf --help` to view all available functions and real-world examples.
  * **Authentication:** Recommended via `HF_TOKEN` environment variable or the `--token` flag.


## Core Commands[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#core-commands "Core Commands的直接链接")
### General Operations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#general-operations "General Operations的直接链接")
  * `hf download REPO_ID`: Download files from the Hub.
  * `hf upload REPO_ID`: Upload files/folders (recommended for single-commit).
  * `hf upload-large-folder REPO_ID LOCAL_PATH`: Recommended for resumable uploads of large directories.
  * `hf sync`: Sync files between a local directory and a bucket.
  * `hf env` / `hf version`: View environment and version details.


### Authentication (`hf auth`)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#authentication-hf-auth "authentication-hf-auth的直接链接")
  * `login` / `logout`: Manage sessions using tokens from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
  * `list` / `switch`: Manage and toggle between multiple stored access tokens.
  * `whoami`: Identify the currently logged-in account.


### Repository Management (`hf repos`)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#repository-management-hf-repos "repository-management-hf-repos的直接链接")
  * `create` / `delete`: Create or permanently remove repositories.
  * `duplicate`: Clone a model, dataset, or Space to a new ID.
  * `move`: Transfer a repository between namespaces.
  * `branch` / `tag`: Manage Git-like references.
  * `delete-files`: Remove specific files using patterns.


## Specialized Hub Interactions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#specialized-hub-interactions "Specialized Hub Interactions的直接链接")
### Datasets & Models[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#datasets--models "Datasets & Models的直接链接")
  * **Datasets:** `hf datasets list`, `info`, and `parquet` (list parquet URLs).
  * **SQL Queries:** `hf datasets sql SQL` — Execute raw SQL via DuckDB against dataset parquet URLs.
  * **Models:** `hf models list` and `info`.
  * **Papers:** `hf papers list` — View daily papers.


### Discussions & Pull Requests (`hf discussions`)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#discussions--pull-requests-hf-discussions "discussions--pull-requests-hf-discussions的直接链接")
  * Manage the lifecycle of Hub contributions: `list`, `create`, `info`, `comment`, `close`, `reopen`, and `rename`.
  * `diff`: View changes in a PR.
  * `merge`: Finalize pull requests.


### Infrastructure & Compute[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#infrastructure--compute "Infrastructure & Compute的直接链接")
  * **Endpoints:** Deploy and manage Inference Endpoints (`deploy`, `pause`, `resume`, `scale-to-zero`, `catalog`).
  * **Jobs:** Run compute tasks on HF infrastructure. Includes `hf jobs uv` for running Python scripts with inline dependencies and `stats` for resource monitoring.
  * **Spaces:** Manage interactive apps. Includes `dev-mode` and `hot-reload` for Python files without full restarts.


### Storage & Automation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#storage--automation "Storage & Automation的直接链接")
  * **Buckets:** Full S3-like bucket management (`create`, `cp`, `mv`, `rm`, `sync`).
  * **Cache:** Manage local storage with `list`, `prune` (remove detached revisions), and `verify` (checksum checks).
  * **Webhooks:** Automate workflows by managing Hub webhooks (`create`, `watch`, `enable`/`disable`).
  * **Collections:** Organize Hub items into collections (`add-item`, `update`, `list`).


## Advanced Usage & Tips[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#advanced-usage--tips "Advanced Usage & Tips的直接链接")
### Global Flags[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#global-flags "Global Flags的直接链接")
  * `--format json`: Produces machine-readable output for automation.
  * `-q` / `--quiet`: Limits output to IDs only.


### Extensions & Skills[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#extensions--skills "Extensions & Skills的直接链接")
  * **Extensions:** Extend CLI functionality via GitHub repositories using `hf extensions install REPO_ID`.
  * **Skills:** Manage AI assistant skills with `hf skills add`.


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#reference-full-skillmd)
  * [Quick Start](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#quick-start)
  * [Core Commands](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#core-commands)
    * [General Operations](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#general-operations)
    * [Authentication (`hf auth`)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#authentication-hf-auth)
    * [Repository Management (`hf repos`)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#repository-management-hf-repos)
  * [Specialized Hub Interactions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#specialized-hub-interactions)
    * [Datasets & Models](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#datasets--models)
    * [Discussions & Pull Requests (`hf discussions`)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#discussions--pull-requests-hf-discussions)
    * [Infrastructure & Compute](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#infrastructure--compute)
    * [Storage & Automation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#storage--automation)
  * [Advanced Usage & Tips](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#advanced-usage--tips)
    * [Global Flags](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#global-flags)
    * [Extensions & Skills](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/mlops/mlops-huggingface-hub#extensions--skills)


