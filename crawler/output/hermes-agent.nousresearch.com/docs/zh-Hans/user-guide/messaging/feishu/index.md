<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu -->

本页总览
Hermes Agent integrates with Feishu and Lark as a full-featured bot. Once connected, you can chat with the agent in direct messages or group chats, receive cron job results in a home chat, and send text, images, audio, and file attachments through the normal gateway flow.
The integration supports both connection modes:
  * `websocket` — recommended; Hermes opens the outbound connection and you do not need a public webhook endpoint
  * `webhook` — useful when you want Feishu/Lark to push events into your gateway over HTTP


## How Hermes Behaves[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#how-hermes-behaves "How Hermes Behaves的直接链接")  
| Context  | Behavior  |  
| --- | --- |  
| Direct messages  | Hermes responds to every message.  |  
| Group chats  | Hermes responds only when the bot is @mentioned in the chat.  |  
| Shared group chats  | By default, session history is isolated per user inside a shared chat.  |  
This shared-chat behavior is controlled by `config.yaml`:

```
group_sessions_per_user:true
```

Set it to `false` only if you explicitly want one shared conversation per chat.
## Step 1: Create a Feishu / Lark App[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#step-1-create-a-feishu--lark-app "Step 1: Create a Feishu / Lark App的直接链接")
### Recommended: Scan-to-Create (one command)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#recommended-scan-to-create-one-command "Recommended: Scan-to-Create \(one command\)的直接链接")

```
hermes gateway setup
```

Select **Feishu / Lark** and scan the QR code with your Feishu or Lark mobile app. Hermes will automatically create a bot application with the correct permissions and save the credentials.
### Alternative: Manual Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#alternative-manual-setup "Alternative: Manual Setup的直接链接")
If scan-to-create is not available, the wizard falls back to manual input:
  1. Open the Feishu or Lark developer console: 
     * Feishu: <https://open.feishu.cn/>
     * Lark: <https://open.larksuite.com/>
  2. Create a new app.
  3. In **Credentials & Basic Info**, copy the **App ID** and **App Secret**.
  4. Enable the **Bot** capability for the app.
  5. Run `hermes gateway setup`, select **Feishu / Lark** , and enter the credentials when prompted.


Keep the App Secret private. Anyone with it can impersonate your app.
## Step 2: Choose a Connection Mode[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#step-2-choose-a-connection-mode "Step 2: Choose a Connection Mode的直接链接")
### Recommended: WebSocket mode[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#recommended-websocket-mode "Recommended: WebSocket mode的直接链接")
Use WebSocket mode when Hermes runs on your laptop, workstation, or a private server. No public URL is required. The official Lark SDK opens and maintains a persistent outbound WebSocket connection with automatic reconnection.

```
FEISHU_CONNECTION_MODE=websocket
```

**Requirements:** The `websockets` Python package must be installed. The SDK handles connection lifecycle, heartbeats, and auto-reconnection internally.
**How it works:** The adapter runs the Lark SDK's WebSocket client in a background executor thread. Inbound events (messages, reactions, card actions) are dispatched to the main asyncio loop. On disconnect, the SDK will attempt to reconnect automatically.
### Optional: Webhook mode[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#optional-webhook-mode "Optional: Webhook mode的直接链接")
Use webhook mode only when you already run Hermes behind a reachable HTTP endpoint.

```
FEISHU_CONNECTION_MODE=webhook
```

In webhook mode, Hermes starts an HTTP server (via `aiohttp`) and serves a Feishu endpoint at:

```
/feishu/webhook
```

**Requirements:** The `aiohttp` Python package must be installed.
You can customize the webhook server bind address and path:

```
FEISHU_WEBHOOK_HOST=127.0.0.1   # default: 127.0.0.1FEISHU_WEBHOOK_PORT=8765# default: 8765FEISHU_WEBHOOK_PATH=/feishu/webhook  # default: /feishu/webhook
```

When Feishu sends a URL verification challenge (`type: url_verification`), the webhook responds automatically so you can complete the subscription setup in the Feishu developer console.
## Step 3: Configure Hermes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#step-3-configure-hermes "Step 3: Configure Hermes的直接链接")
### Option A: Interactive Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#option-a-interactive-setup "Option A: Interactive Setup的直接链接")

```
hermes gateway setup
```

Select **Feishu / Lark** and fill in the prompts.
### Option B: Manual Configuration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#option-b-manual-configuration "Option B: Manual Configuration的直接链接")
Add the following to `~/.hermes/.env`:

```
FEISHU_APP_ID=cli_xxxFEISHU_APP_SECRET=secret_xxxFEISHU_DOMAIN=feishuFEISHU_CONNECTION_MODE=websocket# Optional but strongly recommendedFEISHU_ALLOWED_USERS=ou_xxx,ou_yyyFEISHU_HOME_CHANNEL=oc_xxx
```

`FEISHU_DOMAIN` accepts:
  * `feishu` for Feishu China
  * `lark` for Lark international


## Step 4: Start the Gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#step-4-start-the-gateway "Step 4: Start the Gateway的直接链接")

```
hermes gateway
```

Then message the bot from Feishu/Lark to confirm that the connection is live.
## Home Chat[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#home-chat "Home Chat的直接链接")
Use `/set-home` in a Feishu/Lark chat to mark it as the home channel for cron job results and cross-platform notifications.
You can also preconfigure it:

```
FEISHU_HOME_CHANNEL=oc_xxx
```

## Security[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#security "Security的直接链接")
### User Allowlist[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#user-allowlist "User Allowlist的直接链接")
For production use, set an allowlist of Feishu Open IDs:

```
FEISHU_ALLOWED_USERS=ou_xxx,ou_yyy
```

If you leave the allowlist empty, anyone who can reach the bot may be able to use it. In group chats, the allowlist is checked against the sender's open_id before the message is processed.
### Webhook Encryption Key[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#webhook-encryption-key "Webhook Encryption Key的直接链接")
When running in webhook mode, set an encryption key to enable signature verification of inbound webhook payloads:

```
FEISHU_ENCRYPT_KEY=your-encrypt-key
```

This key is found in the **Event Subscriptions** section of your Feishu app configuration. When set, the adapter verifies every webhook request using the signature algorithm:

```
SHA256(timestamp + nonce + encrypt_key + body)
```

The computed hash is compared against the `x-lark-signature` header using timing-safe comparison. Requests with invalid or missing signatures are rejected with HTTP 401.
In WebSocket mode, signature verification is handled by the SDK itself, so `FEISHU_ENCRYPT_KEY` is optional. In webhook mode, it is strongly recommended for production.
### Verification Token[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#verification-token "Verification Token的直接链接")
An additional layer of authentication that checks the `token` field inside webhook payloads:

```
FEISHU_VERIFICATION_TOKEN=your-verification-token
```

This token is also found in the **Event Subscriptions** section of your Feishu app. When set, every inbound webhook payload must contain a matching `token` in its `header` object. Mismatched tokens are rejected with HTTP 401.
Both `FEISHU_ENCRYPT_KEY` and `FEISHU_VERIFICATION_TOKEN` can be used together for defense in depth.
## Group Message Policy[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#group-message-policy "Group Message Policy的直接链接")
The `FEISHU_GROUP_POLICY` environment variable controls whether and how Hermes responds in group chats:

```
FEISHU_GROUP_POLICY=allowlist   # default
```
  
| Value  | Behavior  |  
| --- | --- |  
| `open`  | Hermes responds to @mentions from any user in any group.  |  
| `allowlist`  | Hermes only responds to @mentions from users listed in `FEISHU_ALLOWED_USERS`.  |  
| `disabled`  | Hermes ignores all group messages entirely.  |  
In all modes, the bot must be explicitly @mentioned (or @all) in the group before the message is processed. Direct messages always bypass this gate.
Set `FEISHU_REQUIRE_MENTION=false` to let Hermes read all group traffic without requiring an @mention:

```
FEISHU_REQUIRE_MENTION=false
```

For per-chat control, set `require_mention` on a `group_rules` entry — see [Per-Group Access Control](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#per-group-access-control) below.
### Bot Identity[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#bot-identity "Bot Identity的直接链接")
Hermes auto-detects the bot's `open_id` and display name on startup. You only need to set these manually when auto-detection cannot reach the Feishu API, or when your app uses tenant-scoped user IDs:

```
FEISHU_BOT_OPEN_ID=ou_xxx     # only when auto-detection failsFEISHU_BOT_USER_ID=xxx        # required if your app uses sender_id_type=user_idFEISHU_BOT_NAME=MyBot         # only when auto-detection fails
```

## Bot-to-Bot Messaging[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#bot-to-bot-messaging "Bot-to-Bot Messaging的直接链接")
By default Hermes ignores messages sent by other bots. Enable bot-to-bot messaging when you want Hermes to participate in A2A orchestration or receive notifications from other bots in the same group.

```
FEISHU_ALLOW_BOTS=mentions   # default: none
```
  
| Value  | Behavior  |  
| --- | --- |  
| `none`  | Ignore all messages from other bots (default).  |  
| `mentions`  | Accept only when the peer bot @mentions Hermes.  |  
| `all`  | Accept every peer bot message.  |  
Also configurable as `feishu.allow_bots` in `config.yaml` (env wins when both are set).
Peer bots do not need to be added to `FEISHU_ALLOWED_USERS` — that allowlist applies to human senders only.
Grant the `application:bot.basic_info:read` scope to display peer bot names; without it, peer bots still route correctly but appear as their `open_id`.
## Interactive Card Actions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#interactive-card-actions "Interactive Card Actions的直接链接")
When users click buttons or interact with interactive cards sent by the bot, the adapter routes these as synthetic `/card` command events:
  * Button clicks become: `/card button {"key": "value", ...}`
  * The action's `value` payload from the card definition is included as JSON.
  * Card actions are deduplicated with a 15-minute window to prevent double processing.


Gateway-driven update prompts use a native Feishu `Yes` / `No` card instead of falling back to plain text replies. When `hermes update --gateway` needs confirmation, the adapter records the selected answer in Hermes's `.update_response` file and replaces the card inline with a resolved state.
Card action events are dispatched with `MessageType.COMMAND`, so they flow through the normal command processing pipeline.
This is also how **command approval** works — when the agent needs to run a dangerous command, it sends an interactive card with Allow Once / Session / Always / Deny buttons. The user clicks a button, and the card action callback delivers the approval decision back to the agent.
### Required Feishu App Configuration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#required-feishu-app-configuration "Required Feishu App Configuration的直接链接")
Interactive cards require **three** configuration steps in the Feishu Developer Console. Missing any of them causes error **200340** when users click card buttons.
  1. **Subscribe to the card action event:** In **Event Subscriptions** , add `card.action.trigger` to your subscribed events.
  2. **Enable the Interactive Card capability:** In **App Features > Bot**, ensure the **Interactive Card** toggle is enabled. This tells Feishu that your app can receive card action callbacks.
  3. **Configure the Card Request URL (webhook mode only):** In **App Features > Bot > Message Card Request URL**, set the URL to the same endpoint as your event webhook (e.g. `https://your-server:8765/feishu/webhook`). In WebSocket mode this is handled automatically by the SDK.


Without all three steps, Feishu will successfully _send_ interactive cards (sending only requires `im:message:send` permission), but clicking any button will return error 200340. The card appears to work — the error only surfaces when a user interacts with it.
## Document Comment Intelligent Reply[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#document-comment-intelligent-reply "Document Comment Intelligent Reply的直接链接")
Beyond chat, the adapter can also answer `@`-mentions left on **Feishu/Lark documents**. When a user comments on a document (local text selection or whole-doc comment) and @-mentions the bot, Hermes reads the document plus the surrounding comment thread and posts an LLM reply inline on the thread.
Powered by the `drive.notice.comment_add_v1` event, the handler:
  * Fetches the document content and comment timeline in parallel (20 messages for whole-doc threads, 12 for local-selection threads).
  * Runs the agent with the `feishu_doc` + `feishu_drive` toolsets scoped to that single comment session.
  * Chunks replies at 4000 chars and posts them back as threaded replies.
  * Caches per-document sessions for 1 hour with a 50-message cap so follow-up comments on the same doc keep context.


### 3-Tier Access Control[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#3-tier-access-control "3-Tier Access Control的直接链接")
Document-comment replies are **explicit-grant only** — there is no implicit allow-all mode. Permissions resolve in this order (first match wins, per field):
  1. **Exact doc** — rule scoped to a specific document token.
  2. **Wildcard** — rule that matches a pattern of docs.
  3. **Top-level** — default rule for the workspace.


Two policies are available per rule:
  * **`allowlist`**— a static list of users / tenants.
  * **`pairing`**— static list ∪ runtime-approved store. Useful for rollouts where moderators can grant access live.


Rules live in `~/.hermes/feishu_comment_rules.json` (pairing grants in `~/.hermes/feishu_comment_pairing.json`) with mtime-cached hot-reload — edits take effect on the next comment event without restarting the gateway.
CLI:

```
# Inspect current rules and pairing statepython -m gateway.platforms.feishu_comment_rules status# Simulate an access check for a specific doc + userpython -m gateway.platforms.feishu_comment_rules check <fileType:fileToken><user_open_id># Manage pairing grants at runtimepython -m gateway.platforms.feishu_comment_rules pairing listpython -m gateway.platforms.feishu_comment_rules pairing add<user_open_id>python -m gateway.platforms.feishu_comment_rules pairing remove <user_open_id>
```

### Required Feishu App Configuration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#required-feishu-app-configuration-1 "Required Feishu App Configuration的直接链接")
On top of the chat/card permissions already granted, add the drive comment event:
  * Subscribe to `drive.notice.comment_add_v1` in **Event Subscriptions**.
  * Grant the `docs:doc:readonly` and `drive:drive:readonly` scopes so the handler can read document content.


## Media Support[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#media-support "Media Support的直接链接")
### Inbound (receiving)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#inbound-receiving "Inbound \(receiving\)的直接链接")
The adapter receives and caches the following media types from users:  
| Type  | Extensions  | How it's processed  |  
| --- | --- | --- |  
| **Images**  | .jpg, .jpeg, .png, .gif, .webp, .bmp  | Downloaded via Feishu API and cached locally  |  
| **Audio**  | .ogg, .mp3, .wav, .m4a, .aac, .flac, .opus, .webm  | Downloaded and cached; small text files are auto-extracted  |  
| **Video**  | .mp4, .mov, .avi, .mkv, .webm, .m4v, .3gp  | Downloaded and cached as documents  |  
| **Files**  | .pdf, .doc, .docx, .xls, .xlsx, .ppt, .pptx, and more  | Downloaded and cached as documents  |  
Media from rich-text (post) messages, including inline images and file attachments, is also extracted and cached.
For small text-based documents (.txt, .md), the file content is automatically injected into the message text so the agent can read it directly without needing tools.
### Outbound (sending)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#outbound-sending "Outbound \(sending\)的直接链接")  
| Method  | What it sends  |  
| --- | --- |  
| `send`  | Text or rich post messages (auto-detected based on markdown content)  |  
|  `send_image` / `send_image_file`  | Uploads image to Feishu, then sends as native image bubble (with optional caption)  |  
| `send_document`  | Uploads file to Feishu API, then sends as file attachment  |  
| `send_voice`  | Uploads audio file as a Feishu file attachment  |  
| `send_video`  | Uploads video and sends as native media message  |  
| `send_animation`  | GIFs are downgraded to file attachments (Feishu has no native GIF bubble)  |  
File upload routing is automatic based on extension:
  * `.ogg`, `.opus` → uploaded as `opus` audio
  * `.mp4`, `.mov`, `.avi`, `.m4v` → uploaded as `mp4` media
  * `.pdf`, `.doc(x)`, `.xls(x)`, `.ppt(x)` → uploaded with their document type
  * Everything else → uploaded as a generic stream file


## Markdown Rendering and Post Fallback[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#markdown-rendering-and-post-fallback "Markdown Rendering and Post Fallback的直接链接")
When outbound text contains markdown formatting (headings, bold, lists, code blocks, links, etc.), the adapter automatically sends it as a Feishu **post** message with an embedded `md` tag rather than as plain text. This enables rich rendering in the Feishu client.
If the Feishu API rejects the post payload (e.g., due to unsupported markdown constructs), the adapter automatically falls back to sending as plain text with markdown stripped. This two-stage fallback ensures messages are always delivered.
Plain text messages (no markdown detected) are sent as the simple `text` message type.
## Processing Status Reactions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#processing-status-reactions "Processing Status Reactions的直接链接")
While the agent is working, the bot shows a `Typing` reaction on your message. It's cleared when the reply arrives, or replaced with `CrossMark` if processing failed.
Set `FEISHU_REACTIONS=false` to turn it off.
## Burst Protection and Batching[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#burst-protection-and-batching "Burst Protection and Batching的直接链接")
The adapter includes debouncing for rapid message bursts to avoid overwhelming the agent:
### Text Batching[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#text-batching "Text Batching的直接链接")
When a user sends multiple text messages in quick succession, they are merged into a single event before being dispatched:  
| Setting  | Env Var  | Default  |  
| --- | --- | --- |  
| Quiet period  | `HERMES_FEISHU_TEXT_BATCH_DELAY_SECONDS`  | 0.6s  |  
| Max messages per batch  | `HERMES_FEISHU_TEXT_BATCH_MAX_MESSAGES`  | 8  |  
| Max characters per batch  | `HERMES_FEISHU_TEXT_BATCH_MAX_CHARS`  | 4000  |  
### Media Batching[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#media-batching "Media Batching的直接链接")
Multiple media attachments sent in quick succession (e.g., dragging several images) are merged into a single event:  
| Setting  | Env Var  | Default  |  
| --- | --- | --- |  
| Quiet period  | `HERMES_FEISHU_MEDIA_BATCH_DELAY_SECONDS`  | 0.8s  |  
### Per-Chat Serialization[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#per-chat-serialization "Per-Chat Serialization的直接链接")
Messages within the same chat are processed serially (one at a time) to maintain conversation coherence. Each chat has its own lock, so messages in different chats are processed concurrently.
## Rate Limiting (Webhook Mode)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#rate-limiting-webhook-mode "Rate Limiting \(Webhook Mode\)的直接链接")
In webhook mode, the adapter enforces per-IP rate limiting to protect against abuse:
  * **Window:** 60-second sliding window
  * **Limit:** 120 requests per window per (app_id, path, IP) triple
  * **Tracking cap:** Up to 4096 unique keys tracked (prevents unbounded memory growth)


Requests that exceed the limit receive HTTP 429 (Too Many Requests).
### Webhook Anomaly Tracking[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#webhook-anomaly-tracking "Webhook Anomaly Tracking的直接链接")
The adapter tracks consecutive error responses per IP address. After 25 consecutive errors from the same IP within a 6-hour window, a warning is logged. This helps detect misconfigured clients or probing attempts.
Additional webhook protections:
  * **Body size limit:** 1 MB maximum
  * **Body read timeout:** 30 seconds
  * **Content-Type enforcement:** Only `application/json` is accepted


## WebSocket Tuning[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#websocket-tuning "WebSocket Tuning的直接链接")
When using `websocket` mode, you can customize reconnect and ping behavior:

```
platforms:feishu:extra:ws_reconnect_interval:120# Seconds between reconnect attempts (default: 120)ws_ping_interval:30# Seconds between WebSocket pings (optional; SDK default if unset)
```
  
| Setting  | Config key  | Default  | Description  |  
| --- | --- | --- | --- |  
| Reconnect interval  | `ws_reconnect_interval`  | 120s  | How long to wait between reconnection attempts  |  
| Ping interval  | `ws_ping_interval`  | _(SDK default)_  | Frequency of WebSocket keepalive pings  |  
## Per-Group Access Control[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#per-group-access-control "Per-Group Access Control的直接链接")
Beyond the global `FEISHU_GROUP_POLICY`, you can set fine-grained rules per group chat using `group_rules` in config.yaml:

```
platforms:feishu:extra:default_group_policy:"open"# Default for groups not in group_rulesadmins:# Users who can manage bot settings-"ou_admin_open_id"group_rules:"oc_group_chat_id_1":policy:"allowlist"# open | allowlist | blacklist | admin_only | disabledallowlist:-"ou_user_open_id_1"-"ou_user_open_id_2""oc_group_chat_id_2":policy:"admin_only""oc_group_chat_id_3":policy:"blacklist"blacklist:-"ou_blocked_user""oc_free_chat":policy:"open"require_mention:false# overrides FEISHU_REQUIRE_MENTION for this chat
```
  
| Policy  | Description  |  
| --- | --- |  
| `open`  | Anyone in the group can use the bot  |  
| `allowlist`  | Only users in the group's `allowlist` can use the bot  |  
| `blacklist`  | Everyone except users in the group's `blacklist` can use the bot  |  
| `admin_only`  | Only users in the global `admins` list can use the bot in this group  |  
| `disabled`  | Bot ignores all messages in this group  |  
Set `require_mention: false` on a `group_rules` entry to skip the @-mention requirement for that specific chat. When omitted, the chat inherits the global `FEISHU_REQUIRE_MENTION` value.
Groups not listed in `group_rules` fall back to `default_group_policy` (defaults to the value of `FEISHU_GROUP_POLICY`).
## Deduplication[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#deduplication "Deduplication的直接链接")
Inbound messages are deduplicated using message IDs with a 24-hour TTL. The dedup state is persisted across restarts to `~/.hermes/feishu_seen_message_ids.json`.  
| Setting  | Env Var  | Default  |  
| --- | --- | --- |  
| Cache size  | `HERMES_FEISHU_DEDUP_CACHE_SIZE`  | 2048 entries  |  
## All Environment Variables[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#all-environment-variables "All Environment Variables的直接链接")  
| Variable  | Required  | Default  | Description  |  
| --- | --- | --- | --- |  
| `FEISHU_APP_ID`  | ✅  | —  | Feishu/Lark App ID  |  
| `FEISHU_APP_SECRET`  | ✅  | —  | Feishu/Lark App Secret  |  
| `FEISHU_DOMAIN`  | —  | `feishu`  |  `feishu` (China) or `lark` (international)  |  
| `FEISHU_CONNECTION_MODE`  | —  | `websocket`  |  `websocket` or `webhook`  |  
| `FEISHU_ALLOWED_USERS`  | —  | _(empty)_  | Comma-separated open_id list for user allowlist  |  
| `FEISHU_ALLOW_BOTS`  | —  | `none`  | Accept messages from other bots: `none`, `mentions`, or `all`  |  
| `FEISHU_REQUIRE_MENTION`  | —  | `true`  | Whether group messages must @mention the bot  |  
| `FEISHU_HOME_CHANNEL`  | —  | —  | Chat ID for cron/notification output  |  
| `FEISHU_ENCRYPT_KEY`  | —  | _(empty)_  | Encrypt key for webhook signature verification  |  
| `FEISHU_VERIFICATION_TOKEN`  | —  | _(empty)_  | Verification token for webhook payload auth  |  
| `FEISHU_GROUP_POLICY`  | —  | `allowlist`  | Group message policy: `open`, `allowlist`, `disabled`  |  
| `FEISHU_BOT_OPEN_ID`  | —  | _(empty)_  | Bot's open_id (for @mention detection)  |  
| `FEISHU_BOT_USER_ID`  | —  | _(empty)_  | Bot's user_id (for @mention detection)  |  
| `FEISHU_BOT_NAME`  | —  | _(empty)_  | Bot's display name (for @mention detection)  |  
| `FEISHU_WEBHOOK_HOST`  | —  | `127.0.0.1`  | Webhook server bind address  |  
| `FEISHU_WEBHOOK_PORT`  | —  | `8765`  | Webhook server port  |  
| `FEISHU_WEBHOOK_PATH`  | —  | `/feishu/webhook`  | Webhook endpoint path  |  
| `HERMES_FEISHU_DEDUP_CACHE_SIZE`  | —  | `2048`  | Max deduplicated message IDs to track  |  
| `HERMES_FEISHU_TEXT_BATCH_DELAY_SECONDS`  | —  | `0.6`  | Text burst debounce quiet period  |  
| `HERMES_FEISHU_TEXT_BATCH_MAX_MESSAGES`  | —  | Max messages merged per text batch  |  
| `HERMES_FEISHU_TEXT_BATCH_MAX_CHARS`  | —  | `4000`  | Max characters merged per text batch  |  
| `HERMES_FEISHU_MEDIA_BATCH_DELAY_SECONDS`  | —  | `0.8`  | Media burst debounce quiet period  |  
WebSocket and per-group ACL settings are configured via `config.yaml` under `platforms.feishu.extra` (see [WebSocket Tuning](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#websocket-tuning) and [Per-Group Access Control](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#per-group-access-control) above).
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#troubleshooting "Troubleshooting的直接链接")  
| Problem  | Fix  |  
| --- | --- |  
| `lark-oapi not installed`  | Install the SDK: `pip install lark-oapi`  |  
| `websockets not installed; websocket mode unavailable`  | Install websockets: `pip install websockets`  |  
| `aiohttp not installed; webhook mode unavailable`  | Install aiohttp: `pip install aiohttp`  |  
| `FEISHU_APP_ID or FEISHU_APP_SECRET not set`  | Set both env vars or configure via `hermes gateway setup`  |  
| `Another local Hermes gateway is already using this Feishu app_id`  | Only one Hermes instance can use the same app_id at a time. Stop the other gateway first.  |  
| Bot doesn't respond in groups  | Ensure the bot is @mentioned, check `FEISHU_GROUP_POLICY`, and verify the sender is in `FEISHU_ALLOWED_USERS` if policy is `allowlist`  |  
| `Webhook rejected: invalid verification token`  | Ensure `FEISHU_VERIFICATION_TOKEN` matches the token in your Feishu app's Event Subscriptions config  |  
| `Webhook rejected: invalid signature`  | Ensure `FEISHU_ENCRYPT_KEY` matches the encrypt key in your Feishu app config  |  
| Post messages show as plain text  | The Feishu API rejected the post payload; this is normal fallback behavior. Check logs for details.  |  
| Images/files not received by bot  | Grant `im:message` and `im:resource` permission scopes to your Feishu app  |  
| Bot identity not auto-detected  | Usually a transient network issue reaching Feishu's bot info endpoint. Set `FEISHU_BOT_OPEN_ID` and `FEISHU_BOT_NAME` manually as a workaround.  |  
| Peer bot messages still ignored after enabling `FEISHU_ALLOW_BOTS`  | Hermes can't identify itself yet — set `FEISHU_BOT_OPEN_ID` (and `FEISHU_BOT_USER_ID` if your app uses `sender_id_type=user_id`).  |  
| Peer bots show as `ou_xxxxxx` instead of by name  | Grant the `application:bot.basic_info:read` scope.  |  
| Error 200340 when clicking approval buttons  | Enable **Interactive Card** capability and configure **Card Request URL** in the Feishu Developer Console. See [Required Feishu App Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#required-feishu-app-configuration) above.  |  
| `Webhook rate limit exceeded`  | More than 120 requests/minute from the same IP. This is usually a misconfiguration or loop.  |  
## Toolset[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#toolset "Toolset的直接链接")
Feishu / Lark uses the `hermes-feishu` platform preset, which includes the same core tools as Telegram and other gateway-based messaging platforms.
  * [How Hermes Behaves](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#how-hermes-behaves)
  * [Step 1: Create a Feishu / Lark App](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#step-1-create-a-feishu--lark-app)
    * [Recommended: Scan-to-Create (one command)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#recommended-scan-to-create-one-command)
    * [Alternative: Manual Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#alternative-manual-setup)
  * [Step 2: Choose a Connection Mode](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#step-2-choose-a-connection-mode)
    * [Recommended: WebSocket mode](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#recommended-websocket-mode)
    * [Optional: Webhook mode](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#optional-webhook-mode)
  * [Step 3: Configure Hermes](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#step-3-configure-hermes)
    * [Option A: Interactive Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#option-a-interactive-setup)
    * [Option B: Manual Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#option-b-manual-configuration)
  * [Step 4: Start the Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#step-4-start-the-gateway)
  * [Security](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#security)
    * [User Allowlist](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#user-allowlist)
    * [Webhook Encryption Key](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#webhook-encryption-key)
    * [Verification Token](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#verification-token)
  * [Group Message Policy](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#group-message-policy)
    * [Bot Identity](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#bot-identity)
  * [Bot-to-Bot Messaging](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#bot-to-bot-messaging)
  * [Interactive Card Actions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#interactive-card-actions)
    * [Required Feishu App Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#required-feishu-app-configuration)
  * [Document Comment Intelligent Reply](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#document-comment-intelligent-reply)
    * [3-Tier Access Control](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#3-tier-access-control)
    * [Required Feishu App Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#required-feishu-app-configuration-1)
  * [Media Support](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#media-support)
    * [Inbound (receiving)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#inbound-receiving)
    * [Outbound (sending)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#outbound-sending)
  * [Markdown Rendering and Post Fallback](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#markdown-rendering-and-post-fallback)
  * [Processing Status Reactions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#processing-status-reactions)
  * [Burst Protection and Batching](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#burst-protection-and-batching)
    * [Text Batching](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#text-batching)
    * [Media Batching](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#media-batching)
    * [Per-Chat Serialization](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#per-chat-serialization)
  * [Rate Limiting (Webhook Mode)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#rate-limiting-webhook-mode)
    * [Webhook Anomaly Tracking](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#webhook-anomaly-tracking)
  * [WebSocket Tuning](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#websocket-tuning)
  * [Per-Group Access Control](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#per-group-access-control)
  * [Deduplication](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#deduplication)
  * [All Environment Variables](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#all-environment-variables)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/feishu#troubleshooting)


