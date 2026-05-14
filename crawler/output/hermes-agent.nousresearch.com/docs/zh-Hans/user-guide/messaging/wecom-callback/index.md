<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback -->

本页总览
Connect Hermes to WeCom (Enterprise WeChat) as a self-built enterprise application using the callback/webhook model.
Hermes supports two WeCom integration modes:
  * — bot-style, connects via WebSocket. Simpler setup, works in group chats.
  * **WeCom Callback** (this page) — self-built app, receives encrypted XML callbacks. Shows as a first-class app in users' WeCom sidebar. Supports multi-corp routing.


## How It Works[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#how-it-works "How It Works的直接链接")
  1. You register a self-built application in the WeCom Admin Console
  2. WeCom pushes encrypted XML to your HTTP callback endpoint
  3. Hermes decrypts the message, queues it for the agent
  4. Immediately acknowledges (silent — nothing displayed to the user)
  5. The agent processes the request (typically 3–30 minutes)
  6. The reply is delivered proactively via the WeCom `message/send` API


## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#prerequisites "Prerequisites的直接链接")
  * A WeCom enterprise account with admin access
  * `aiohttp` and `httpx` Python packages (included in the default install)
  * A publicly reachable server for the callback URL (or a tunnel like ngrok)


## Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#setup "Setup的直接链接")
### 1. Create a Self-Built App in WeCom[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#1-create-a-self-built-app-in-wecom "1. Create a Self-Built App in WeCom的直接链接")
  1. Go to [WeCom Admin Console](https://work.weixin.qq.com/) → **Applications** → **Create App**
  2. Note your **Corp ID** (shown at the top of the admin console)
  3. In the app settings, create a **Corp Secret**
  4. Note the **Agent ID** from the app's overview page
  5. Under **Receive Messages** , configure the callback URL: 
     * URL: `http://YOUR_PUBLIC_IP:8645/wecom/callback`
     * Token: Generate a random token (WeCom provides one)
     * EncodingAESKey: Generate a key (WeCom provides one)


### 2. Configure Environment Variables[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#2-configure-environment-variables "2. Configure Environment Variables的直接链接")
Add to your `.env` file:

```
WECOM_CALLBACK_CORP_ID=your-corp-idWECOM_CALLBACK_CORP_SECRET=your-corp-secretWECOM_CALLBACK_AGENT_ID=1000002WECOM_CALLBACK_TOKEN=your-callback-tokenWECOM_CALLBACK_ENCODING_AES_KEY=your-43-char-aes-key# OptionalWECOM_CALLBACK_HOST=0.0.0.0WECOM_CALLBACK_PORT=8645WECOM_CALLBACK_ALLOWED_USERS=user1,user2
```

### 3. Start the Gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#3-start-the-gateway "3. Start the Gateway的直接链接")

```
hermes gateway
```

(Use `hermes gateway start` only after `hermes gateway install` has registered the systemd/launchd service.)
The callback adapter starts an HTTP server on the configured port. WeCom will verify the callback URL via a GET request, then begin sending messages via POST.
## Configuration Reference[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#configuration-reference "Configuration Reference的直接链接")
Set these in `config.yaml` under `platforms.wecom_callback.extra`, or use environment variables:  
| Setting  | Default  | Description  |  
| --- | --- | --- |  
| `corp_id`  | —  | WeCom enterprise Corp ID (required)  |  
| `corp_secret`  | —  | Corp secret for the self-built app (required)  |  
| `agent_id`  | —  | Agent ID of the self-built app (required)  |  
| `token`  | —  | Callback verification token (required)  |  
| `encoding_aes_key`  | —  | 43-character AES key for callback encryption (required)  |  
| `host`  | `0.0.0.0`  | Bind address for the HTTP callback server  |  
| `port`  | `8645`  | Port for the HTTP callback server  |  
| `path`  | `/wecom/callback`  | URL path for the callback endpoint  |  
## Multi-App Routing[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#multi-app-routing "Multi-App Routing的直接链接")
For enterprises running multiple self-built apps (e.g., across different departments or subsidiaries), configure the `apps` list in `config.yaml`:

```
platforms:wecom_callback:enabled:trueextra:host:"0.0.0.0"port:8645apps:-name:"dept-a"corp_id:"ww_corp_a"corp_secret:"secret-a"agent_id:"1000002"token:"token-a"encoding_aes_key:"key-a-43-chars..."-name:"dept-b"corp_id:"ww_corp_b"corp_secret:"secret-b"agent_id:"1000003"token:"token-b"encoding_aes_key:"key-b-43-chars..."
```

Users are scoped by `corp_id:user_id` to prevent cross-corp collisions. When a user sends a message, the adapter records which app (corp) they belong to and routes replies through the correct app's access token.
## Access Control[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#access-control "Access Control的直接链接")
Restrict which users can interact with the app:

```
# Allowlist specific usersWECOM_CALLBACK_ALLOWED_USERS=zhangsan,lisi,wangwu# Or allow all usersWECOM_CALLBACK_ALLOW_ALL_USERS=true
```

## Endpoints[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#endpoints "Endpoints的直接链接")
The adapter exposes:  
| Method  | Path  | Purpose  |  
| --- | --- | --- |  
| GET  | `/wecom/callback`  | URL verification handshake (WeCom sends this during setup)  |  
| POST  | `/wecom/callback`  | Encrypted message callback (WeCom sends user messages here)  |  
| GET  | `/health`  | Health check — returns `{"status": "ok"}`  |  
## Encryption[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#encryption "Encryption的直接链接")
All callback payloads are encrypted with AES-CBC using the EncodingAESKey. The adapter handles:
  * **Inbound** : Decrypt XML payload, verify SHA1 signature
  * **Outbound** : Replies sent via proactive API (not encrypted callback response)


The crypto implementation is compatible with Tencent's official WXBizMsgCrypt SDK.
## Limitations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#limitations "Limitations的直接链接")
  * **No streaming** — replies arrive as complete messages after the agent finishes
  * **No typing indicators** — the callback model doesn't support typing status
  * **Text only** — currently supports text messages for input; image/file/voice input not yet implemented. The agent is aware of outbound media capabilities via the WeCom platform hint (images, documents, video, voice).
  * **Response latency** — agent sessions take 3–30 minutes; users see the reply when processing completes


  * [How It Works](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#how-it-works)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#prerequisites)
  * [Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#setup)
    * [1. Create a Self-Built App in WeCom](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#1-create-a-self-built-app-in-wecom)
    * [2. Configure Environment Variables](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#2-configure-environment-variables)
    * [3. Start the Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#3-start-the-gateway)
  * [Configuration Reference](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#configuration-reference)
  * [Multi-App Routing](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#multi-app-routing)
  * [Access Control](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#access-control)
  * [Limitations](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/wecom-callback#limitations)


