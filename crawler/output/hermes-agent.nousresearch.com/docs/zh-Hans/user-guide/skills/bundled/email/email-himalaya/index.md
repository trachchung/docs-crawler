<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya -->

本页总览
Himalaya CLI: IMAP/SMTP email from terminal.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/email/himalaya`  |  
| Version  | `1.1.0`  |  
| Author  | community  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Email`, `IMAP`, `SMTP`, `CLI`, `Communication`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Himalaya Email CLI
Himalaya is a CLI email client that lets you manage emails from the terminal using IMAP, SMTP, Notmuch, or Sendmail backends.
## References[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#references "References的直接链接")
  * `references/configuration.md` (config file setup + IMAP/SMTP authentication)
  * `references/message-composition.md` (MML syntax for composing emails)


## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#prerequisites "Prerequisites的直接链接")
  1. Himalaya CLI installed (`himalaya --version` to verify)
  2. A configuration file at `~/.config/himalaya/config.toml`
  3. IMAP/SMTP credentials configured (password stored securely)


### Installation[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#installation "Installation的直接链接")

```
# Pre-built binary (Linux/macOS — recommended)curl-sSL https://raw.githubusercontent.com/pimalaya/himalaya/master/install.sh |PREFIX=~/.local sh# macOS via Homebrewbrew install himalaya# Or via cargo (any platform with Rust)cargoinstall himalaya --locked
```

## Configuration Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#configuration-setup "Configuration Setup的直接链接")
Run the interactive wizard to set up an account:

```
himalaya account configure
```

Or create `~/.config/himalaya/config.toml` manually:

```
[accounts.personal]email="you@example.com"display-name="Your Name"default=truebackend.type="imap"backend.host="imap.example.com"backend.port=993backend.encryption.type="tls"backend.login="you@example.com"backend.auth.type="password"backend.auth.cmd="pass show email/imap"# or use keyringmessage.send.backend.type="smtp"message.send.backend.host="smtp.example.com"message.send.backend.port=587message.send.backend.encryption.type="start-tls"message.send.backend.login="you@example.com"message.send.backend.auth.type="password"message.send.backend.auth.cmd="pass show email/smtp"# Folder aliases (himalaya v1.2.0+ syntax). Required whenever the# server's folder names don't match himalaya's canonical names# (inbox/sent/drafts/trash). Gmail is the common case — see# `references/configuration.md` for the `[Gmail]/Sent Mail` mapping.folder.aliases.inbox="INBOX"folder.aliases.sent="Sent"folder.aliases.drafts="Drafts"folder.aliases.trash="Trash"
```

> **Heads up on the alias syntax.** Pre-v1.2.0 docs used a `[accounts.NAME.folder.alias]` sub-section (singular `alias`). v1.2.0 silently ignores that form — TOML parses fine, but the alias resolver never reads it, so every lookup falls through to the canonical name. On Gmail this means save-to-Sent fails _after_ SMTP delivery succeeds, and `himalaya message send` exits non-zero. Any caller (agent, script, user) that retries on that exit code will re-run the entire send — including SMTP — producing duplicate emails to recipients. Always use `folder.aliases.X` (plural, dotted keys, directly under `[accounts.NAME]`).
## Hermes Integration Notes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#hermes-integration-notes "Hermes Integration Notes的直接链接")
  * **Reading, listing, searching, moving, deleting** all work directly through the terminal tool
  * **Composing/replying/forwarding** — piped input (`cat << EOF | himalaya template send`) is recommended for reliability. Interactive `$EDITOR` mode works with `pty=true` + background + process tool, but requires knowing the editor and its commands
  * Use `--output json` for structured output that's easier to parse programmatically
  * The `himalaya account configure` wizard requires interactive input — use PTY mode: `terminal(command="himalaya account configure", pty=true)`


## Common Operations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#common-operations "Common Operations的直接链接")
### List Folders[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#list-folders "List Folders的直接链接")

```
himalaya folder list
```

### List Emails[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#list-emails "List Emails的直接链接")
List emails in INBOX (default):

```
himalaya envelope list
```

List emails in a specific folder:

```
himalaya envelope list --folder"Sent"
```

List with pagination:

```
himalaya envelope list --page1 --page-size 20
```

### Search Emails[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#search-emails "Search Emails的直接链接")

```
himalaya envelope list from john@example.com subject meeting
```

### Read an Email[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#read-an-email "Read an Email的直接链接")
Read email by ID (shows plain text):

```
himalaya message read42
```

Export raw MIME:

```
himalaya message export42--full
```

### Reply to an Email[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#reply-to-an-email "Reply to an Email的直接链接")
To reply non-interactively from Hermes, read the original message, compose a reply, and pipe it:

```
# Get the reply template, edit it, and sendhimalaya template reply 42|sed's/^$/\nYour reply text here\n/'| himalaya template send
```

Or build the reply manually:

```
cat<<'EOF'| himalaya template sendFrom: you@example.comTo: sender@example.comSubject: Re: Original SubjectIn-Reply-To: <original-message-id>Your reply here.EOF
```

Reply-all (interactive — needs $EDITOR, use template approach above instead):

```
himalaya message reply 42--all
```

### Forward an Email[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#forward-an-email "Forward an Email的直接链接")

```
# Get forward template and pipe with modificationshimalaya template forward 42|sed's/^To:.*/To: newrecipient@example.com/'| himalaya template send
```

### Write a New Email[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#write-a-new-email "Write a New Email的直接链接")
**Non-interactive (use this from Hermes)** — pipe the message via stdin:

```
cat<<'EOF'| himalaya template sendFrom: you@example.comTo: recipient@example.comSubject: Test MessageHello from Himalaya!EOF
```

Or with headers flag:

```
himalaya message write-H"To:recipient@example.com"-H"Subject:Test""Message body here"
```

Note: `himalaya message write` without piped input opens `$EDITOR`. This works with `pty=true` + background mode, but piping is simpler and more reliable.
### Move/Copy Emails[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#movecopy-emails "Move/Copy Emails的直接链接")
Move to folder:

```
himalaya message move 42"Archive"
```

Copy to folder:

```
himalaya message copy 42"Important"
```

### Delete an Email[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#delete-an-email "Delete an Email的直接链接")

```
himalaya message delete 42
```

### Manage Flags[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#manage-flags "Manage Flags的直接链接")
Add flag:

```
himalaya flag add42--flag seen
```

Remove flag:

```
himalaya flag remove 42--flag seen
```

## Multiple Accounts[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#multiple-accounts "Multiple Accounts的直接链接")
List accounts:

```
himalaya account list
```

Use a specific account:

```
himalaya --account work envelope list
```

## Attachments[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#attachments "Attachments的直接链接")
Save attachments from a message:

```
himalaya attachment download 42
```

Save to specific directory:

```
himalaya attachment download 42--dir ~/Downloads
```

## Output Formats[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#output-formats "Output Formats的直接链接")
Most commands support `--output` for structured output:

```
himalaya envelope list --output jsonhimalaya envelope list --output plain
```

## Debugging[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#debugging "Debugging的直接链接")
Enable debug logging:

```
RUST_LOG=debug himalaya envelope list
```

Full trace with backtrace:

```
RUST_LOG=trace RUST_BACKTRACE=1 himalaya envelope list
```

## Tips[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#tips "Tips的直接链接")
  * Use `himalaya --help` or `himalaya <command> --help` for detailed usage.
  * Message IDs are relative to the current folder; re-list after folder changes.
  * For composing rich emails with attachments, use MML syntax (see `references/message-composition.md`).
  * Store passwords securely using `pass`, system keyring, or a command that outputs the password.


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#reference-full-skillmd)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#prerequisites)
    * [Installation](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#installation)
  * [Configuration Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#configuration-setup)
  * [Hermes Integration Notes](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#hermes-integration-notes)
  * [Common Operations](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#common-operations)
    * [List Folders](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#list-folders)
    * [List Emails](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#list-emails)
    * [Search Emails](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#search-emails)
    * [Read an Email](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#read-an-email)
    * [Reply to an Email](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#reply-to-an-email)
    * [Forward an Email](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#forward-an-email)
    * [Write a New Email](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#write-a-new-email)
    * [Move/Copy Emails](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#movecopy-emails)
    * [Delete an Email](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#delete-an-email)
    * [Manage Flags](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#manage-flags)
  * [Multiple Accounts](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#multiple-accounts)
  * [Attachments](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#attachments)
  * [Output Formats](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/email/email-himalaya#output-formats)


