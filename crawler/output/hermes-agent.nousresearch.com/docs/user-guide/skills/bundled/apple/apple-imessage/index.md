<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#__docusaurus_skipToContent_fallback)
On this page
Send and receive iMessages/SMS via the imsg CLI on macOS.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#skill-metadata "Direct link to Skill metadata")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/apple/imessage`  |  
| Version  | `1.0.0`  |  
| Author  | Hermes Agent  |  
| License  | MIT  |  
| Platforms  | macos  |  
| Tags  |  `iMessage`, `SMS`, `messaging`, `macOS`, `Apple`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# iMessage
Use `imsg` to read and send iMessage/SMS via macOS Messages.app.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#prerequisites "Direct link to Prerequisites")
  * **macOS** with Messages.app signed in
  * Install: `brew install steipete/tap/imsg`
  * Grant Full Disk Access for terminal (System Settings → Privacy → Full Disk Access)
  * Grant Automation permission for Messages.app when prompted


## When to Use[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#when-to-use "Direct link to When to Use")
  * User asks to send an iMessage or text message
  * Reading iMessage conversation history
  * Checking recent Messages.app chats
  * Sending to phone numbers or Apple IDs


## When NOT to Use[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#when-not-to-use "Direct link to When NOT to Use")
  * Telegram/Discord/Slack/WhatsApp messages → use the appropriate gateway channel
  * Group chat management (adding/removing members) → not supported
  * Bulk/mass messaging → always confirm with user first


## Quick Reference[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#quick-reference "Direct link to Quick Reference")
### List Chats[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#list-chats "Direct link to List Chats")

```
imsg chats --limit10--json
```

### View History[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#view-history "Direct link to View History")

```
# By chat IDimsg history --chat-id 1--limit20--json# With attachments infoimsg history --chat-id 1--limit20--attachments--json
```

### Send Messages[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#send-messages "Direct link to Send Messages")

```
# Text onlyimsg send --to"+14155551212"--text"Hello!"# With attachmentimsg send --to"+14155551212"--text"Check this out"--file /path/to/image.jpg# Force iMessage or SMSimsg send --to"+14155551212"--text"Hi"--service imessageimsg send --to"+14155551212"--text"Hi"--service sms
```

### Watch for New Messages[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#watch-for-new-messages "Direct link to Watch for New Messages")

```
imsg watch --chat-id 1--attachments
```

## Service Options[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#service-options "Direct link to Service Options")
  * `--service imessage` — Force iMessage (requires recipient has iMessage)
  * `--service sms` — Force SMS (green bubble)
  * `--service auto` — Let Messages.app decide (default)


## Rules[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#rules "Direct link to Rules")
  1. **Always confirm recipient and message content** before sending
  2. **Never send to unknown numbers** without explicit user approval
  3. **Verify file paths** exist before attaching
  4. **Don't spam** — rate-limit yourself


## Example Workflow[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#example-workflow "Direct link to Example Workflow")
User: "Text mom that I'll be late"

```
# 1. Find mom's chatimsg chats --limit20--json| jq '.[] | select(.displayName | contains("Mom"))'# 2. Confirm with user: "Found Mom at +1555123456. Send 'I'll be late' via iMessage?"# 3. Send after confirmationimsg send --to"+1555123456"--text"I'll be late"
```

  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#reference-full-skillmd)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#prerequisites)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#when-to-use)
  * [When NOT to Use](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#when-not-to-use)
  * [Quick Reference](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#quick-reference)
    * [View History](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#view-history)
    * [Send Messages](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#send-messages)
    * [Watch for New Messages](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#watch-for-new-messages)
  * [Service Options](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#service-options)
  * [Example Workflow](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/apple/apple-imessage#example-workflow)


