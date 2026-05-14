<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway -->

本页总览
Tool Gateway 包含在付费 Nous Portal 订阅中。
**Tool Gateway** 让已付费的 [Nous Portal](https://portal.nousresearch.com) 用户通过同一份订阅，直接使用网页搜索、文生图、语音合成（TTS）与浏览器自动化，而**不必** 再分别注册 Firecrawl、FAL、OpenAI、Browser Use 等服务的 API Key。
## 包含能力[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E5%8C%85%E5%90%AB%E8%83%BD%E5%8A%9B "包含能力的直接链接")  
| 工具  | 作用  | 若不用网关，可改用  |  
| --- | --- | --- |  
| **网页搜索与抓取**  | 通过 Firecrawl 搜索并抽取页面内容  |  `FIRECRAWL_API_KEY`、`EXA_API_KEY`、`PARALLEL_API_KEY`、`TAVILY_API_KEY`  |  
| **文生图**  | 通过 FAL 生成图像（8 个模型：FLUX 2 Klein/Pro、GPT-Image、Nano Banana Pro、Ideogram、Recraft V4 Pro、Qwen、Z-Image）  | `FAL_KEY`  |  
| **语音合成**  | 通过 OpenAI TTS 将文字转为语音  |  `VOICE_TOOLS_OPENAI_KEY`、`ELEVENLABS_API_KEY`  |  
| **浏览器自动化**  | 通过 Browser Use 控制云端浏览器  |  `BROWSER_USE_API_KEY`、`BROWSERBASE_API_KEY`  |  
上述四类能力均计入 Nous 订阅计费。你可以按需组合——例如网页与文生图走网关，TTS 仍使用自己的 ElevenLabs Key。
## 资格与账号[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E8%B5%84%E6%A0%BC%E4%B8%8E%E8%B4%A6%E5%8F%B7 "资格与账号的直接链接")
Tool Gateway 仅对 Nous Portal 订阅开放；免费档不可用——请 [升级订阅](https://portal.nousresearch.com/manage-subscription) 后解锁。
检查当前状态：

```
hermes status
```

在输出中找到 **Nous Tool Gateway** 小节：会标明哪些工具经订阅网关启用、哪些使用直连 Key、哪些尚未配置。
## 如何启用 Tool Gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E5%A6%82%E4%BD%95%E5%90%AF%E7%94%A8-tool-gateway "如何启用 Tool Gateway的直接链接")
### 在模型配置流程中[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E5%9C%A8%E6%A8%A1%E5%9E%8B%E9%85%8D%E7%BD%AE%E6%B5%81%E7%A8%8B%E4%B8%AD "在模型配置流程中的直接链接")
运行 `hermes model` 并选择 Nous Portal 作为提供商时，Hermes 会主动询问是否启用 Tool Gateway：

```
Your Nous subscription includes the Tool Gateway.  The Tool Gateway gives you access to web search, image generation,  text-to-speech, and browser automation through your Nous subscription.  No need to sign up for separate API keys — just pick the tools you want.  ○ Web search & extract (Firecrawl) — not configured  ○ Image generation (FAL) — not configured  ○ Text-to-speech (OpenAI TTS) — not configured  ○ Browser automation (Browser Use) — not configured  ● Enable Tool Gateway  ○ Skip
```

选择 **Enable Tool Gateway** 即可。
若 `.env` 中已有部分直连 API Key，提示会相应变化：可为全部工具启用网关（直连 Key 仍保留在 `.env` 但运行时不用）、仅为未配置项启用，或完全跳过。
### 通过 `hermes tools`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E9%80%9A%E8%BF%87-hermes-tools "通过-hermes-tools的直接链接")
也可在交互式工具配置中逐项启用：

```
hermes tools
```

选择工具类别（Web、Browser、Image Generation、TTS），再将提供商选为 **Nous Subscription** 。这会在配置里把对应工具的 `use_gateway` 设为 `true`。
### 手动编辑配置[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E6%89%8B%E5%8A%A8%E7%BC%96%E8%BE%91%E9%85%8D%E7%BD%AE "手动编辑配置的直接链接")
在 `~/.hermes/config.yaml` 中直接设置 `use_gateway`：

```
web:backend: firecrawluse_gateway:trueimage_gen:use_gateway:truetts:provider: openaiuse_gateway:truebrowser:cloud_provider: browser-useuse_gateway:true
```

## 工作原理[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86 "工作原理的直接链接")
当某工具的 `use_gateway: true` 时，运行时会把 API 调用路由到 Nous Tool Gateway，而不是使用直连 Key：
  1. **网页工具** — `web_search` / `web_extract` 走网关的 Firecrawl 端点
  2. **文生图** — `image_generate` 走网关的 FAL 端点
  3. **TTS** — `text_to_speech` 走网关的 OpenAI Audio 端点
  4. **浏览器** — `browser_navigate` 等走网关的 Browser Use 端点


网关使用 Nous Portal 凭据认证（在 `hermes model` 完成后写入 `~/.hermes/auth.json`）。
### 优先级[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E4%BC%98%E5%85%88%E7%BA%A7 "优先级的直接链接")
每个工具都会先看 `use_gateway`：
  * **`use_gateway: true`**→ 强制走网关，即使`.env` 里仍有直连 Key
  * **`use_gateway: false`**（或未设置）→ 若有直连 Key 则优先直连；仅在没有直连凭据时才回退到网关


因此你可以在网关与直连之间切换，而无需删除 `.env` 中的旧 Key。
## 切回直连 Key[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E5%88%87%E5%9B%9E%E7%9B%B4%E8%BF%9E-key "切回直连 Key的直接链接")
对单个工具停用网关：

```
hermes tools    # 选择该工具 → 选直连提供商
```

或在配置中设 `use_gateway: false`：

```
web:backend: firecrawluse_gateway:false# 此时使用 .env 中的 FIRECRAWL_API_KEY
```

在 `hermes tools` 中选择非网关提供商时，`use_gateway` 会自动设为 `false`，避免配置自相矛盾。
## 查看状态[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E6%9F%A5%E7%9C%8B%E7%8A%B6%E6%80%81 "查看状态的直接链接")

```
hermes status
```

**Nous Tool Gateway** 小节示例：

```
◆ Nous Tool Gateway  Nous Portal   ✓ managed tools available  Web tools       ✓ active via Nous subscription  Image gen       ✓ active via Nous subscription  TTS             ✓ active via Nous subscription  Browser         ○ active via Browser Use key  Modal           ○ available via subscription (optional)
```

标记为 “active via Nous subscription” 的即经网关路由；带自有 Key 的会显示当前激活的提供商。
## 进阶：自建网关[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E8%BF%9B%E9%98%B6%E8%87%AA%E5%BB%BA%E7%BD%91%E5%85%B3 "进阶：自建网关的直接链接")
若使用自建或自定义网关，可在 `~/.hermes/.env` 中用环境变量覆盖端点：

```
TOOL_GATEWAY_DOMAIN=nousresearch.com     # 网关路由基础域名TOOL_GATEWAY_SCHEME=https                 # http 或 https（默认 https）TOOL_GATEWAY_USER_TOKEN=your-token        # 鉴权 Token（通常由程序自动填充）FIRECRAWL_GATEWAY_URL=https://..# 单独覆盖 Firecrawl 端点
```

这些变量与订阅状态无关，始终可在配置中看到，便于自建基础设施。
## 常见问题[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98 "常见问题的直接链接")
### 需要删掉已有的 API Key 吗？[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E9%9C%80%E8%A6%81%E5%88%A0%E6%8E%89%E5%B7%B2%E6%9C%89%E7%9A%84-api-key-%E5%90%97 "需要删掉已有的 API Key 吗？的直接链接")
不需要。`use_gateway: true` 时运行时会跳过直连 Key 并走网关；Key 仍保留在 `.env`。之后若关闭网关，会自动恢复使用直连 Key。
### 能否部分工具走网关、部分走直连？[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E8%83%BD%E5%90%A6%E9%83%A8%E5%88%86%E5%B7%A5%E5%85%B7%E8%B5%B0%E7%BD%91%E5%85%B3%E9%83%A8%E5%88%86%E8%B5%B0%E7%9B%B4%E8%BF%9E "能否部分工具走网关、部分走直连？的直接链接")
可以。`use_gateway` 按工具独立配置。例如：网页与文生图走网关，TTS 用 ElevenLabs，浏览器用 Browserbase。
### 订阅到期会怎样？[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E8%AE%A2%E9%98%85%E5%88%B0%E6%9C%9F%E4%BC%9A%E6%80%8E%E6%A0%B7 "订阅到期会怎样？的直接链接")
经网关路由的工具会停止工作，直到你 [续订](https://portal.nousresearch.com/manage-subscription) 或通过 `hermes tools` 改回直连 Key。
### 与「消息网关」（各聊天平台）是否冲突？[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E4%B8%8E%E6%B6%88%E6%81%AF%E7%BD%91%E5%85%B3%E5%90%84%E8%81%8A%E5%A4%A9%E5%B9%B3%E5%8F%B0%E6%98%AF%E5%90%A6%E5%86%B2%E7%AA%81 "与「消息网关」（各聊天平台）是否冲突？的直接链接")
不冲突。Tool Gateway 作用于**工具运行时** 的 API 路由，与 CLI、Telegram、Discord 等入口无关。
### Modal 算在 Tool Gateway 里吗？[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#modal-%E7%AE%97%E5%9C%A8-tool-gateway-%E9%87%8C%E5%90%97 "Modal 算在 Tool Gateway 里吗？的直接链接")
Modal（无服务器终端后端）可作为 Nous 订阅的可选附加能力，但**不会** 由 Tool Gateway 安装向导一并打开——请单独通过 `hermes setup terminal` 或在 `config.yaml` 中配置。
  * [如何启用 Tool Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E5%A6%82%E4%BD%95%E5%90%AF%E7%94%A8-tool-gateway)
    * [通过 `hermes tools`](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E9%80%9A%E8%BF%87-hermes-tools)
  * [工作原理](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86)
  * [常见问题](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98)
    * [需要删掉已有的 API Key 吗？](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E9%9C%80%E8%A6%81%E5%88%A0%E6%8E%89%E5%B7%B2%E6%9C%89%E7%9A%84-api-key-%E5%90%97)
    * [能否部分工具走网关、部分走直连？](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E8%83%BD%E5%90%A6%E9%83%A8%E5%88%86%E5%B7%A5%E5%85%B7%E8%B5%B0%E7%BD%91%E5%85%B3%E9%83%A8%E5%88%86%E8%B5%B0%E7%9B%B4%E8%BF%9E)
    * [与「消息网关」（各聊天平台）是否冲突？](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#%E4%B8%8E%E6%B6%88%E6%81%AF%E7%BD%91%E5%85%B3%E5%90%84%E8%81%8A%E5%A4%A9%E5%B9%B3%E5%8F%B0%E6%98%AF%E5%90%A6%E5%86%B2%E7%AA%81)
    * [Modal 算在 Tool Gateway 里吗？](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/tool-gateway#modal-%E7%AE%97%E5%9C%A8-tool-gateway-%E9%87%8C%E5%90%97)


