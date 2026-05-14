<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage -->

本页总览
Send and receive iMessages/SMS via the imsg CLI on macOS.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#skill-metadata "Skill metadata的直接链接")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/apple/imessage`  |  
| Version  | `1.0.0`  |  
| Author  | Hermes Agent  |  
| License  | MIT  |  
| Platforms  | macos  |  
| Tags  |  `iMessage`, `SMS`, `messaging`, `macOS`, `Apple`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#reference-full-skillmd "Reference: full SKILL.md的直接链接")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# iMessage
Use `imsg` to read and send iMessage/SMS via macOS Messages.app.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#prerequisites "Prerequisites的直接链接")
  * **macOS** with Messages.app signed in
  * Install: `brew install steipete/tap/imsg`
  * Grant Full Disk Access for terminal (System Settings → Privacy → Full Disk Access)
  * Grant Automation permission for Messages.app when prompted


## When to Use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#when-to-use "When to Use的直接链接")
  * User asks to send an iMessage or text message
  * Reading iMessage conversation history
  * Checking recent Messages.app chats
  * Sending to phone numbers or Apple IDs


## When NOT to Use[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#when-not-to-use "When NOT to Use的直接链接")
  * Telegram/Discord/Slack/WhatsApp messages → use the appropriate gateway channel
  * Group chat management (adding/removing members) → not supported
  * Bulk/mass messaging → always confirm with user first


## Quick Reference[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#quick-reference "Quick Reference的直接链接")
### List Chats[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#list-chats "List Chats的直接链接")

```
imsg chats --limit10--json
```

### View History[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#view-history "View History的直接链接")

```
# By chat IDimsg history --chat-id 1--limit20--json# With attachments infoimsg history --chat-id 1--limit20--attachments--json
```

### Send Messages[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#send-messages "Send Messages的直接链接")

```
# Text onlyimsg send --to"+14155551212"--text"Hello!"# With attachmentimsg send --to"+14155551212"--text"Check this out"--file /path/to/image.jpg# Force iMessage or SMSimsg send --to"+14155551212"--text"Hi"--service imessageimsg send --to"+14155551212"--text"Hi"--service sms
```

### Watch for New Messages[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#watch-for-new-messages "Watch for New Messages的直接链接")

```
imsg watch --chat-id 1--attachments
```

## Service Options[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#service-options "Service Options的直接链接")
  * `--service imessage` — Force iMessage (requires recipient has iMessage)
  * `--service sms` — Force SMS (green bubble)
  * `--service auto` — Let Messages.app decide (default)


## Rules[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#rules "Rules的直接链接")
  1. **Always confirm recipient and message content** before sending
  2. **Never send to unknown numbers** without explicit user approval
  3. **Verify file paths** exist before attaching
  4. **Don't spam** — rate-limit yourself


## Example Workflow[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#example-workflow "Example Workflow的直接链接")
User: "Text mom that I'll be late"

```
# 1. Find mom's chatimsg chats --limit20--json| jq '.[] | select(.displayName | contains("Mom"))'# 2. Confirm with user: "Found Mom at +1555123456. Send 'I'll be late' via iMessage?"# 3. Send after confirmationimsg send --to"+1555123456"--text"I'll be late"
```

  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#reference-full-skillmd)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#prerequisites)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#when-to-use)
  * [When NOT to Use](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#when-not-to-use)
  * [Quick Reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#quick-reference)
    * [View History](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#view-history)
    * [Send Messages](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#send-messages)
    * [Watch for New Messages](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#watch-for-new-messages)
  * [Service Options](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#service-options)
  * [Example Workflow](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/skills/bundled/apple/apple-imessage#example-workflow)


