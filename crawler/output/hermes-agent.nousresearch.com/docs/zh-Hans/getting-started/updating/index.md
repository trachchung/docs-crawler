<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating -->

本页总览
## Updating[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#updating "Updating的直接链接")
Update to the latest version with a single command:

```
hermes update
```

This pulls the latest code, updates dependencies, and prompts you to configure any new options that were added since your last update.
`hermes update` automatically detects new configuration options and prompts you to add them. If you skipped that prompt, you can manually run `hermes config check` to see missing options, then `hermes config migrate` to interactively add them.
### What happens during an update[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#what-happens-during-an-update "What happens during an update的直接链接")
When you run `hermes update`, the following steps occur:
  1. **Pairing-data snapshot** — a lightweight pre-update state snapshot is saved (covers `~/.hermes/pairing/`, Feishu comment rules, and other state files that get modified at runtime). Recoverable via the snapshot restore flow described under [Snapshots and rollback](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/checkpoints-and-rollback), or by extracting the most recent quick-snapshot zip Hermes wrote next to your `~/.hermes/` directory.
  2. **Git pull** — pulls the latest code from the `main` branch and updates submodules
  3. **Dependency install** — runs `uv pip install -e ".[all]"` to pick up new or changed dependencies
  4. **Config migration** — detects new config options added since your version and prompts you to set them
  5. **Gateway auto-restart** — running gateways are refreshed after the update completes so the new code takes effect immediately. Service-managed gateways (systemd on Linux, launchd on macOS) are restarted through the service manager. Manual gateways are relaunched automatically when Hermes can map the running PID back to a profile.


### Preview-only: `hermes update --check`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#preview-only-hermes-update---check "preview-only-hermes-update---check的直接链接")
Want to know if you're behind `origin/main` before actually pulling? Run `hermes update --check` — it fetches, prints your local commit and the latest remote commit side-by-side, and exits `0` if in sync or `1` if behind. No files are modified, no gateway is restarted. Useful in scripts and cron jobs that gate on "is there an update".
### Full pre-update backup: `--backup`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#full-pre-update-backup---backup "full-pre-update-backup---backup的直接链接")
For high-value profiles (production gateways, shared team installs) you can opt into a full pre-pull backup of `HERMES_HOME` (config, auth, sessions, skills, pairing):

```
hermes update --backup
```

Or make it the default for every run:

```
# ~/.hermes/config.yamlupdates:pre_update_backup:true
```

`--backup` was the always-on behavior in earlier builds, but it was adding minutes to every update on large homes, so it's now opt-in. The lightweight pairing-data snapshot above still runs unconditionally.
Expected output looks like:

```
$ hermes updateUpdating Hermes Agent...📥 Pulling latest code...Already up to date.  (or: Updating abc1234..def5678)📦 Updating dependencies...✅ Dependencies updated🔍 Checking for new config options...✅ Config is up to date  (or: Found 2 new options — running migration...)🔄 Restarting gateways...✅ Gateway restarted✅ Hermes Agent updated successfully!
```

### Recommended Post-Update Validation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#recommended-post-update-validation "Recommended Post-Update Validation的直接链接")
`hermes update` handles the main update path, but a quick validation confirms everything landed cleanly:
  1. `git status --short` — if the tree is unexpectedly dirty, inspect before continuing
  2. `hermes doctor` — checks config, dependencies, and service health
  3. `hermes --version` — confirm the version bumped as expected
  4. If you use the gateway: `hermes gateway status`
  5. If `doctor` reports npm audit issues: run `npm audit fix` in the flagged directory


If `git status --short` shows unexpected changes after `hermes update`, stop and inspect them before continuing. This usually means local modifications were reapplied on top of the updated code, or a dependency step refreshed lockfiles.
### If your terminal disconnects mid-update[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#if-your-terminal-disconnects-mid-update "If your terminal disconnects mid-update的直接链接")
`hermes update` protects itself against accidental terminal loss:
  * The update ignores `SIGHUP`, so closing your SSH session or terminal window no longer kills it mid-install. `pip` and `git` child processes inherit this protection, so the Python environment cannot be left half-installed by a dropped connection.
  * All output is mirrored to `~/.hermes/logs/update.log` while the update runs. If your terminal disappears, reconnect and inspect the log to see whether the update finished and whether the gateway restart succeeded:



```
tail-f ~/.hermes/logs/update.log
```

  * `Ctrl-C` (SIGINT) and system shutdown (SIGTERM) are still honored — those are deliberate cancellations, not accidents.


You no longer need to wrap `hermes update` in `screen` or `tmux` to survive a terminal drop.
### Checking your current version[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#checking-your-current-version "Checking your current version的直接链接")

```
hermes version
```

Compare against the latest release at the [GitHub releases page](https://github.com/NousResearch/hermes-agent/releases).
### Updating from Messaging Platforms[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#updating-from-messaging-platforms "Updating from Messaging Platforms的直接链接")
You can also update directly from Telegram, Discord, Slack, WhatsApp, or Teams by sending:

```
/update
```

This pulls the latest code, updates dependencies, and restarts running gateways. The bot will briefly go offline during the restart (typically 5–15 seconds) and then resume.
### Manual Update[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#manual-update "Manual Update的直接链接")
If you installed manually (not via the quick installer):

```
cd /path/to/hermes-agentexportVIRTUAL_ENV="$(pwd)/venv"# Pull latest code and submodulesgit pull origin maingit submodule update --init--recursive# Reinstall (picks up new dependencies)uv pip install-e".[all]"uv pip install-e"./tinker-atropos"# Check for new config optionshermes config checkhermes config migrate   # Interactively add any missing options
```

### Rollback instructions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#rollback-instructions "Rollback instructions的直接链接")
If an update introduces a problem, you can roll back to a previous version:

```
cd /path/to/hermes-agent# List recent versionsgit log --oneline-10# Roll back to a specific commitgit checkout <commit-hash>git submodule update --init--recursiveuv pip install-e".[all]"# Restart the gateway if runninghermes gateway restart
```

To roll back to a specific release tag:

```
git checkout v0.6.0git submodule update --init--recursiveuv pip install-e".[all]"
```

Rolling back may cause config incompatibilities if new options were added. Run `hermes config check` after rolling back and remove any unrecognized options from `config.yaml` if you encounter errors.
### Note for Nix users[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#note-for-nix-users "Note for Nix users的直接链接")
If you installed via Nix flake, updates are managed through the Nix package manager:

```
# Update the flake inputnix flake update hermes-agent# Or rebuild with the latestnix profile upgrade hermes-agent
```

Nix installations are immutable — rollback is handled by Nix's generation system:

```
nix profile rollback
```

See [Nix Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/nix-setup) for more details.
## Uninstalling[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#uninstalling "Uninstalling的直接链接")

```
hermes uninstall
```

The uninstaller gives you the option to keep your configuration files (`~/.hermes/`) for a future reinstall.
### Manual Uninstall[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#manual-uninstall "Manual Uninstall的直接链接")

```
rm-f ~/.local/bin/hermesrm-rf /path/to/hermes-agentrm-rf ~/.hermes            # Optional — keep if you plan to reinstall
```

If you installed the gateway as a system service, stop and disable it first:

```
hermes gateway stop# Linux: systemctl --user disable hermes-gateway# macOS: launchctl remove ai.hermes.gateway
```

  * [Updating](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#updating)
    * [What happens during an update](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#what-happens-during-an-update)
    * [Preview-only: `hermes update --check`](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#preview-only-hermes-update---check)
    * [Full pre-update backup: `--backup`](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#full-pre-update-backup---backup)
    * [Recommended Post-Update Validation](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#recommended-post-update-validation)
    * [If your terminal disconnects mid-update](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#if-your-terminal-disconnects-mid-update)
    * [Checking your current version](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#checking-your-current-version)
    * [Updating from Messaging Platforms](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#updating-from-messaging-platforms)
    * [Manual Update](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#manual-update)
    * [Rollback instructions](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#rollback-instructions)
    * [Note for Nix users](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#note-for-nix-users)
  * [Uninstalling](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#uninstalling)
    * [Manual Uninstall](https://hermes-agent.nousresearch.com/docs/zh-Hans/getting-started/updating#manual-uninstall)


