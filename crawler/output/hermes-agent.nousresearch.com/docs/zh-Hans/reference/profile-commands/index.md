<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands -->

本页总览
This page covers all commands related to [Hermes profiles](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/profiles). For general CLI commands, see [CLI Commands Reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/cli-commands).
##  `hermes profile`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile "hermes-profile的直接链接")

```
hermes profile <subcommand>
```

Top-level command for managing profiles. Running `hermes profile` without a subcommand shows help.  
| Subcommand  | Description  |  
| --- | --- |  
| `list`  | List all profiles.  |  
| `use`  | Set the active (default) profile.  |  
| `create`  | Create a new profile.  |  
| `delete`  | Delete a profile.  |  
| `show`  | Show details about a profile.  |  
| `alias`  | Regenerate the shell alias for a profile.  |  
| `rename`  | Rename a profile.  |  
| `export`  | Export a profile to a tar.gz archive.  |  
| `import`  | Import a profile from a tar.gz archive.  |  
| `install`  | Install a profile distribution from a git URL or local directory. See [Profile Distributions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/profile-distributions).  |  
| `update`  | Re-pull a distribution-managed profile and re-apply its bundle.  |  
| `info`  | Show distribution metadata for a profile (origin URL, commit, last update).  |  
##  `hermes profile list`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-list "hermes-profile-list的直接链接")

```
hermes profile list
```

Lists all profiles. The currently active profile is marked with `*`.
**Example:**

```
$ hermes profile list  default* work  dev  personal
```

No options.
##  `hermes profile use`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-use "hermes-profile-use的直接链接")

```
hermes profile use <name>
```

Sets `<name>` as the active profile. All subsequent `hermes` commands (without `-p`) will use this profile.  
| Argument  | Description  |  
| --- | --- |  
| `<name>`  | Profile name to activate. Use `default` to return to the base profile.  |  
**Example:**

```
hermes profile use workhermes profile use default
```

##  `hermes profile create`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-create "hermes-profile-create的直接链接")

```
hermes profile create <name>[options]
```

Creates a new profile.  
| Argument / Option  | Description  |  
| --- | --- |  
| `<name>`  | Name for the new profile. Must be a valid directory name (alphanumeric, hyphens, underscores).  |  
| `--clone`  | Copy `config.yaml`, `.env`, and `SOUL.md` from the current profile.  |  
| `--clone-all`  | Copy everything (config, memories, skills, sessions, state) from the current profile.  |  
| `--clone-from <profile>`  | Clone from a specific profile instead of the current one. Used with `--clone` or `--clone-all`.  |  
| `--no-alias`  | Skip wrapper script creation.  |  
Creating a profile does **not** make that profile directory the default project/workspace directory for terminal commands. If you want a profile to start in a specific project, set `terminal.cwd` in that profile's `config.yaml`.
**Examples:**

```
# Blank profile — needs full setuphermes profile create mybot# Clone config only from current profilehermes profile create work --clone# Clone everything from current profilehermes profile create backup --clone-all# Clone config from a specific profilehermes profile create work2 --clone --clone-from work
```

##  `hermes profile delete`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-delete "hermes-profile-delete的直接链接")

```
hermes profile delete <name>[options]
```

Deletes a profile and removes its shell alias.  
| Argument / Option  | Description  |  
| --- | --- |  
| `<name>`  | Profile to delete.  |  
|  `--yes`, `-y`  | Skip confirmation prompt.  |  
**Example:**

```
hermes profile delete mybothermes profile delete mybot --yes
```

This permanently deletes the profile's entire directory including all config, memories, sessions, and skills. Cannot delete the currently active profile.
##  `hermes profile show`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-show "hermes-profile-show的直接链接")

```
hermes profile show <name>
```

Displays details about a profile including its home directory, configured model, gateway status, skills count, and configuration file status.
This shows the profile's Hermes home directory, not the terminal working directory. Terminal commands start from `terminal.cwd` (or the launch directory on the local backend when `cwd: "."`).  
| Argument  | Description  |  
| --- | --- |  
| `<name>`  | Profile to inspect.  |  
**Example:**

```
$ hermes profile show workProfile: workPath:    ~/.hermes/profiles/workModel:   anthropic/claude-sonnet-4 (anthropic)Gateway: stoppedSkills:  12.env:    existsSOUL.md: existsAlias:   ~/.local/bin/work
```

##  `hermes profile alias`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-alias "hermes-profile-alias的直接链接")

```
hermes profile alias<name>[options]
```

Regenerates the shell alias script at `~/.local/bin/<name>`. Useful if the alias was accidentally deleted or if you need to update it after moving your Hermes installation.  
| Argument / Option  | Description  |  
| --- | --- |  
| `<name>`  | Profile to create/update the alias for.  |  
| `--remove`  | Remove the wrapper script instead of creating it.  |  
| `--name <alias>`  | Custom alias name (default: profile name).  |  
**Example:**

```
hermes profile alias work# Creates/updates ~/.local/bin/workhermes profile alias work --name mywork# Creates ~/.local/bin/myworkhermes profile alias work --remove# Removes the wrapper script
```

##  `hermes profile rename`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-rename "hermes-profile-rename的直接链接")

```
hermes profile rename<old-name><new-name>
```

Renames a profile. Updates the directory and shell alias.  
| Argument  | Description  |  
| --- | --- |  
| `<old-name>`  | Current profile name.  |  
| `<new-name>`  | New profile name.  |  
**Example:**

```
hermes profile rename mybot assistant# ~/.hermes/profiles/mybot → ~/.hermes/profiles/assistant# ~/.local/bin/mybot → ~/.local/bin/assistant
```

##  `hermes profile export`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-export "hermes-profile-export的直接链接")

```
hermes profile export<name>[options]
```

Exports a profile as a compressed tar.gz archive.  
| Argument / Option  | Description  |  
| --- | --- |  
| `<name>`  | Profile to export.  |  
|  `-o`, `--output <path>`  | Output file path (default: `<name>.tar.gz`).  |  
**Example:**

```
hermes profile export work# Creates work.tar.gz in the current directoryhermes profile export work -o ./work-2026-03-29.tar.gz
```

##  `hermes profile import`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-import "hermes-profile-import的直接链接")

```
hermes profile import<archive>[options]
```

Imports a profile from a tar.gz archive.  
| Argument / Option  | Description  |  
| --- | --- |  
| `<archive>`  | Path to the tar.gz archive to import.  |  
| `--name <name>`  | Name for the imported profile (default: inferred from archive).  |  
**Example:**

```
hermes profile import ./work-2026-03-29.tar.gz# Infers profile name from the archivehermes profile import ./work-2026-03-29.tar.gz --name work-restored
```

## Distribution commands[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#distribution-commands "Distribution commands的直接链接")
**New to distributions?** Start with the [Profile Distributions user guide](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/profile-distributions) — it covers the why, when, and how with full examples. The sections below are a dry CLI reference for when you know what you want.
Distributions turn a profile into a shareable, versioned artifact published as a **git repository**. A recipient installs the distribution with a single command and can update it in place later without touching their local memories, sessions, or credentials.
`auth.json` and `.env` are never part of a distribution — they stay on the installing user's machine.
The recipient's user data (memories, sessions, auth, their own edits to `.env`) is always preserved across the initial install and subsequent updates.
`hermes profile export` / `import` are still the right commands for **local backup and restore** of a profile on your own machine. Distribution (`install` / `update` / `info`) is a separate concept: ship a profile via git so someone else can install it.
###  `hermes profile install`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-install "hermes-profile-install的直接链接")

```
hermes profile install<source>[--name <name>][--alias][--force][--yes]
```

Installs a profile distribution from a git URL or a local directory.  
| Option  | Description  |  
| --- | --- |  
| `<source>`  | Git URL (`github.com/user/repo`, `https://...`, `git@...`, `ssh://`, `git://`) or a local directory containing `distribution.yaml` at its root.  |  
| `--name NAME`  | Override the profile name from the manifest.  |  
| `--alias`  | Also create a shell wrapper (e.g. `telemetry` → `hermes -p telemetry`).  |  
| `--force`  | Overwrite an existing profile of the same name. User data is still preserved.  |  
|  `-y`, `--yes`  | Skip the manifest-preview confirmation prompt.  |  
The installer shows the manifest, lists required env vars, and warns about cron jobs before asking for confirmation. Required env vars go into a `.env.EXAMPLE` file you copy to `.env` and fill in.
**Examples:**

```
# Install from a GitHub repo (shorthand)hermes profile install github.com/kyle/telemetry-distribution --alias# Install from a full HTTPS git URLhermes profile install https://github.com/kyle/telemetry-distribution.git# Install from SSHhermes profile install git@github.com:kyle/telemetry-distribution.git# Install from a local directory during developmenthermes profile install ./telemetry/
```

###  `hermes profile update`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-update "hermes-profile-update的直接链接")

```
hermes profile update <name>[--force-config][--yes]
```

Re-clones the distribution from its recorded source and applies updates. Distribution-owned files (SOUL.md, skills/, cron/, mcp.json) are overwritten; user data (memories, sessions, auth, .env) is never touched.
`config.yaml` is preserved by default to keep your local overrides. Pass `--force-config` to reset it to the distribution's shipped config.
###  `hermes profile info`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-info "hermes-profile-info的直接链接")

```
hermes profile info <name>
```

Prints the profile's distribution manifest — name, version, required Hermes version, author, env var requirements, the source URL/path, and the `Installed:` timestamp recorded when the distribution was last `install`-ed or `update`-d. Useful for checking what a shared profile needs before installing it, and for spotting "this profile was installed 6 months ago and hasn't been updated."
`hermes profile list` also shows the distribution name and version in a `Distribution` column, and `hermes profile show <name>` / `delete <name>` surface the source URL so you can tell at a glance which profiles came from a git repo vs. were created locally.
### Private distributions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#private-distributions "Private distributions的直接链接")
A private git repository works as a distribution source with no extra configuration — the install shells out to your normal `git` binary, so whatever authentication your shell is already set up for (SSH key, `git credential` helper, GitHub CLI's stored HTTPS credentials) applies transparently.

```
# Uses your SSH key, the same as any other `git clone`hermes profile install git@github.com:your-org/internal-assistant.git# Uses your git credential helperhermes profile install https://github.com/your-org/internal-assistant.git
```

If a clone prompts for credentials interactively in your terminal during install, that prompt flows through. Set up your auth the way you'd normally use `git clone` against the same repo first, then install.
### Distribution manifest (`distribution.yaml`)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#distribution-manifest-distributionyaml "distribution-manifest-distributionyaml的直接链接")
Every distribution has a `distribution.yaml` at the root of its repository:

```
name: telemetryversion: 0.1.0description:"Compliance monitoring harness"hermes_requires:">=0.12.0"author:"Your Name"license:"MIT"env_requires:-name: OPENAI_API_KEYdescription:"OpenAI API key"required:true-name: GRAPHITI_MCP_URLdescription:"Memory graph URL"required:falsedefault:"http://127.0.0.1:8000/sse"distribution_owned:# optional; defaults to SOUL.md, config.yaml,#   mcp.json, skills/, cron/, distribution.yaml- SOUL.md- skills/compliance/- cron/
```

`hermes_requires` supports `>=`, `<=`, `==`, `!=`, `>`, `<`, or a bare version (treated as `>=`). Install fails with a clear error if the current Hermes version doesn't satisfy the spec.
`distribution_owned` is optional. If set, only those paths are replaced on update; anything else in the profile stays user-owned. If omitted, the defaults above apply.
### Publishing a distribution[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#publishing-a-distribution "Publishing a distribution的直接链接")
Authoring a distribution is just a git push:
  1. In your profile directory, create `distribution.yaml` with at least `name` and `version`.
  2. Initialize a git repo (or use an existing one) and push to GitHub / GitLab / any host Hermes can clone from.
  3. Tell recipients to run `hermes profile install <your-repo-url>`.


Use git tags for versioned releases — recipients who clone `HEAD` get your latest state, and you can always bump `version:` in the manifest.
##  `hermes -p` / `hermes --profile`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes--p--hermes---profile "hermes--p--hermes---profile的直接链接")

```
hermes -p<name><command>[options]hermes --profile<name><command>[options]
```

Global flag to run any Hermes command under a specific profile without changing the sticky default. This overrides the active profile for the duration of the command.  
| Option  | Description  |  
| --- | --- |  
|  `-p <name>`, `--profile <name>`  | Profile to use for this command.  |  
**Examples:**

```
hermes -p work chat -q"Check the server status"hermes --profile dev gateway starthermes -p personal skills listhermes -p work config edit
```

##  `hermes completion`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-completion "hermes-completion的直接链接")

```
hermes completion <shell>
```

Generates shell completion scripts. Includes completions for profile names and profile subcommands.  
| Argument  | Description  |  
| --- | --- |  
| `<shell>`  | Shell to generate completions for: `bash`, `zsh`, or `fish`.  |  
**Examples:**

```
# Install completionshermes completion bash>> ~/.bashrchermes completion zsh>> ~/.zshrchermes completion fish > ~/.config/fish/completions/hermes.fish# Reload shellsource ~/.bashrc
```

After installation, tab completion works for:
  * `hermes profile <TAB>` — subcommands (list, use, create, etc.)
  * `hermes profile use <TAB>` — profile names
  * `hermes -p <TAB>` — profile names


## See also[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#see-also "See also的直接链接")
  * [Profiles User Guide](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/profiles)
  * [CLI Commands Reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/cli-commands)
  * [FAQ — Profiles section](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/faq#profiles)


  * [`hermes profile`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile)
  * [`hermes profile list`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-list)
  * [`hermes profile use`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-use)
  * [`hermes profile create`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-create)
  * [`hermes profile delete`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-delete)
  * [`hermes profile show`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-show)
  * [`hermes profile alias`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-alias)
  * [`hermes profile rename`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-rename)
  * [`hermes profile export`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-export)
  * [`hermes profile import`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-import)
  * [Distribution commands](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#distribution-commands)
    * [`hermes profile install`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-install)
    * [`hermes profile update`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-update)
    * [`hermes profile info`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-profile-info)
    * [Private distributions](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#private-distributions)
    * [Distribution manifest (`distribution.yaml`)](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#distribution-manifest-distributionyaml)
    * [Publishing a distribution](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#publishing-a-distribution)
  * [`hermes -p` / `hermes --profile`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes--p--hermes---profile)
  * [`hermes completion`](https://hermes-agent.nousresearch.com/docs/zh-Hans/reference/profile-commands#hermes-completion)


