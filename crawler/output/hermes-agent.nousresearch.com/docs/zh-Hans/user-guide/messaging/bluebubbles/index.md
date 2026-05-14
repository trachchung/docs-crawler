<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles -->

本页总览
Connect Hermes to Apple iMessage via [BlueBubbles](https://bluebubbles.app/) — a free, open-source macOS server that bridges iMessage to any device.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#prerequisites "Prerequisites的直接链接")
  * A **Mac** (always on) running [BlueBubbles Server](https://bluebubbles.app/)
  * Apple ID signed into Messages.app on that Mac
  * BlueBubbles Server v1.0.0+ (webhooks require this version)
  * Network connectivity between Hermes and the BlueBubbles server


## Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#setup "Setup的直接链接")
### 1. Install BlueBubbles Server[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#1-install-bluebubbles-server "1. Install BlueBubbles Server的直接链接")
Download and install from [bluebubbles.app](https://bluebubbles.app/). Complete the setup wizard — sign in with your Apple ID and configure a connection method (local network, Ngrok, Cloudflare, or Dynamic DNS).
### 2. Get your Server URL and Password[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#2-get-your-server-url-and-password "2. Get your Server URL and Password的直接链接")
In BlueBubbles Server → **Settings → API** , note:
  * **Server URL** (e.g., `http://192.168.1.10:1234`)
  * **Server Password**


### 3. Configure Hermes[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#3-configure-hermes "3. Configure Hermes的直接链接")
Run the setup wizard:

```
hermes gateway setup
```

Select **BlueBubbles (iMessage)** and enter your server URL and password.
Or set environment variables directly in `~/.hermes/.env`:

```
BLUEBUBBLES_SERVER_URL=http://192.168.1.10:1234BLUEBUBBLES_PASSWORD=your-server-password
```

### 4. Authorize Users[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#4-authorize-users "4. Authorize Users的直接链接")
Choose one approach:
**DM Pairing (recommended):** When someone messages your iMessage, Hermes automatically sends them a pairing code. Approve it with:

```
hermes pairing approve bluebubbles <CODE>
```

Use `hermes pairing list` to see pending codes and approved users.
**Pre-authorize specific users** (in `~/.hermes/.env`):

```
BLUEBUBBLES_ALLOWED_USERS=user@icloud.com,+15551234567
```

**Open access** (in `~/.hermes/.env`):

```
BLUEBUBBLES_ALLOW_ALL_USERS=true
```

### 5. Start the Gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#5-start-the-gateway "5. Start the Gateway的直接链接")

```
hermes gateway run
```

Hermes will connect to your BlueBubbles server, register a webhook, and start listening for iMessage messages.
## How It Works[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#how-it-works "How It Works的直接链接")

```
iMessage → Messages.app → BlueBubbles Server → Webhook → HermesHermes → BlueBubbles REST API → Messages.app → iMessage
```

  * **Inbound:** BlueBubbles sends webhook events to a local listener when new messages arrive. No polling — instant delivery.
  * **Outbound:** Hermes sends messages via the BlueBubbles REST API.
  * **Media:** Images, voice messages, videos, and documents are supported in both directions. Inbound attachments are downloaded and cached locally for the agent to process.


## Environment Variables[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#environment-variables "Environment Variables的直接链接")  
| Variable  | Required  | Default  | Description  |  
| --- | --- | --- | --- |  
| `BLUEBUBBLES_SERVER_URL`  | Yes  | —  | BlueBubbles server URL  |  
| `BLUEBUBBLES_PASSWORD`  | Yes  | —  | Server password  |  
| `BLUEBUBBLES_WEBHOOK_HOST`  | No  | `127.0.0.1`  | Webhook listener bind address  |  
| `BLUEBUBBLES_WEBHOOK_PORT`  | No  | `8645`  | Webhook listener port  |  
| `BLUEBUBBLES_WEBHOOK_PATH`  | No  | `/bluebubbles-webhook`  | Webhook URL path  |  
| `BLUEBUBBLES_HOME_CHANNEL`  | No  | —  | Phone/email for cron delivery  |  
| `BLUEBUBBLES_ALLOWED_USERS`  | No  | —  | Comma-separated authorized users  |  
| `BLUEBUBBLES_ALLOW_ALL_USERS`  | No  | `false`  | Allow all users  |  
Auto-marking messages as read is controlled by the `send_read_receipts` key under `platforms.bluebubbles.extra` in `~/.hermes/config.yaml` (default: `true`). There is no corresponding environment variable.
## Features[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#features "Features的直接链接")
### Text Messaging[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#text-messaging "Text Messaging的直接链接")
Send and receive iMessages. Markdown is automatically stripped for clean plain-text delivery.
### Rich Media[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#rich-media "Rich Media的直接链接")
  * **Images:** Photos appear natively in the iMessage conversation
  * **Voice messages:** Audio files sent as iMessage voice messages
  * **Videos:** Video attachments
  * **Documents:** Files sent as iMessage attachments


### Tapback Reactions[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#tapback-reactions "Tapback Reactions的直接链接")
Love, like, dislike, laugh, emphasize, and question reactions. Requires the BlueBubbles [Private API helper](https://docs.bluebubbles.app/helper-bundle/installation).
### Typing Indicators[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#typing-indicators "Typing Indicators的直接链接")
Shows "typing..." in the iMessage conversation while the agent is processing. Requires Private API.
### Read Receipts[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#read-receipts "Read Receipts的直接链接")
Automatically marks messages as read after processing. Requires Private API.
### Chat Addressing[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#chat-addressing "Chat Addressing的直接链接")
You can address chats by email or phone number — Hermes resolves them to BlueBubbles chat GUIDs automatically. No need to use raw GUID format.
## Private API[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#private-api "Private API的直接链接")
Some features require the BlueBubbles [Private API helper](https://docs.bluebubbles.app/helper-bundle/installation):
  * Tapback reactions
  * Typing indicators
  * Read receipts
  * Creating new chats by address


Without the Private API, basic text messaging and media still work.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#troubleshooting "Troubleshooting的直接链接")
### "Cannot reach server"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#cannot-reach-server ""Cannot reach server"的直接链接")
  * Verify the server URL is correct and the Mac is on
  * Check that BlueBubbles Server is running
  * Ensure network connectivity (firewall, port forwarding)


### Messages not arriving[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#messages-not-arriving "Messages not arriving的直接链接")
  * Check that the webhook is registered in BlueBubbles Server → Settings → API → Webhooks
  * Verify the webhook URL is reachable from the Mac
  * Check `hermes logs gateway` for webhook errors (or `hermes logs -f` to follow in real-time)


### "Private API helper not connected"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#private-api-helper-not-connected ""Private API helper not connected"的直接链接")
  * Install the Private API helper: [docs.bluebubbles.app](https://docs.bluebubbles.app/helper-bundle/installation)
  * Basic messaging works without it — only reactions, typing, and read receipts require it


  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#prerequisites)
  * [Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#setup)
    * [1. Install BlueBubbles Server](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#1-install-bluebubbles-server)
    * [2. Get your Server URL and Password](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#2-get-your-server-url-and-password)
    * [3. Configure Hermes](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#3-configure-hermes)
    * [4. Authorize Users](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#4-authorize-users)
    * [5. Start the Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#5-start-the-gateway)
  * [How It Works](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#how-it-works)
  * [Environment Variables](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#environment-variables)
  * [Features](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#features)
    * [Text Messaging](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#text-messaging)
    * [Tapback Reactions](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#tapback-reactions)
    * [Typing Indicators](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#typing-indicators)
    * [Read Receipts](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#read-receipts)
    * [Chat Addressing](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#chat-addressing)
  * [Private API](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#private-api)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#troubleshooting)
    * ["Cannot reach server"](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#cannot-reach-server)
    * [Messages not arriving](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#messages-not-arriving)
    * ["Private API helper not connected"](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/bluebubbles#private-api-helper-not-connected)


