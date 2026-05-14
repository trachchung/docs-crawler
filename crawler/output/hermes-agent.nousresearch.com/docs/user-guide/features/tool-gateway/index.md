<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#__docusaurus_skipToContent_fallback)
On this page
**One subscription. Every tool built in.**
The Tool Gateway is included with every paid [Nous Portal](https://portal.nousresearch.com) subscription. It routes Hermes' tool calls — web search, image generation, text-to-speech, and cloud browser automation — through infrastructure Nous already runs, so you don't have to sign up with Firecrawl, FAL, OpenAI, Browser Use, or anyone else just to make your agent useful.
[Start or manage subscription →](https://portal.nousresearch.com/manage-subscription)
## What's included[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#whats-included "Direct link to What's included")  
| Tool  | What you get  |  
| --- | --- |  
| 🔍  | **Web search & extract**  | Agent-grade web search and full-page extraction via Firecrawl. No rate limits to worry about — the gateway handles scaling.  |  
| 🎨  | **Image generation**  | Nine models under one endpoint: **FLUX 2 Klein 9B** , **FLUX 2 Pro** , **Z-Image Turbo** , **Nano Banana Pro** (Gemini 3 Pro Image), **GPT Image 1.5** , **GPT Image 2** , **Ideogram V3** , **Recraft V4 Pro** , **Qwen Image**. Pick per-generation with a flag, or let Hermes default to FLUX 2 Klein.  |  
| 🔊  | **Text-to-speech**  | OpenAI TTS voices wired into the `text_to_speech` tool. Drop voice notes into Telegram, generate audio for pipelines, narrate anything.  |  
| 🌐  | **Cloud browser automation**  | Headless Chromium sessions via Browser Use. `browser_navigate`, `browser_click`, `browser_type`, `browser_vision` — all the agent-driving primitives, no Browserbase account required.  |  
All four are pay-as-you-use billed against your Nous subscription. Use any combination — run the gateway for web and images while keeping your own ElevenLabs key for TTS, or route everything through Nous.
## Why it's here[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#why-its-here "Direct link to Why it's here")
Building an agent that can actually _do things_ means stitching together 5+ API subscriptions — each with their own signup, rate limits, billing, and quirks. The gateway collapses that into one account:
  * **One bill.** Pay Nous; we handle the rest.
  * **One signup.** No Firecrawl, FAL, Browser Use, or OpenAI audio accounts to manage.
  * **One key.** Your Nous Portal OAuth covers every tool.
  * **Same quality.** Same backends the direct-key route uses — just fronted by us.


Bring your own keys anytime — per-tool, whenever you want to. The gateway isn't a lock-in, it's a shortcut.
## Get started[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#get-started "Direct link to Get started")

```
hermes model          # Pick Nous Portal as your provider
```

When you select Nous Portal, Hermes offers to turn on the Tool Gateway. Accept, and you're done — every supported tool is live on the next run.
Check what's active at any time:

```
hermes status
```

You'll see a section like:

```
◆ Nous Tool Gateway  Nous Portal     ✓ managed tools available  Web tools       ✓ active via Nous subscription  Image gen       ✓ active via Nous subscription  TTS             ✓ active via Nous subscription  Browser         ○ active via Browser Use key
```

Tools marked "active via Nous subscription" are going through the gateway. Anything else is using your own keys.
## Eligibility[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#eligibility "Direct link to Eligibility")
The Tool Gateway is a **paid-subscription** feature. Free-tier Nous accounts can use Portal for inference but don't include managed tools — [upgrade your plan](https://portal.nousresearch.com/manage-subscription) to unlock the gateway.
## Mix and match[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#mix-and-match "Direct link to Mix and match")
The gateway is per-tool. Turn it on for just what you want:
  * **All tools through Nous** — easiest; one subscription, done.
  * **Gateway for web + images, bring your own TTS** — keep your ElevenLabs voice, let Nous handle the rest.
  * **Gateway only for things you don't have keys for** — "I already pay for Browserbase, but I don't want a Firecrawl account" works fine.


Switch any tool at any time via:

```
hermes tools          # Interactive picker for each tool category
```

Select the tool, pick **Nous Subscription** as the provider (or any direct provider you prefer). No config editing required.
## Using individual image models[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#using-individual-image-models "Direct link to Using individual image models")
Image generation defaults to FLUX 2 Klein 9B for speed. Override per-call by passing the model ID to the `image_generate` tool:  
| Model  | ID  | Best for  |  
| --- | --- | --- |  
| FLUX 2 Klein 9B  | `fal-ai/flux-2/klein/9b`  | Fast, good default  |  
| FLUX 2 Pro  | `fal-ai/flux-2/pro`  | Higher fidelity FLUX  |  
| Z-Image Turbo  | `fal-ai/z-image/turbo`  | Stylized, fast  |  
| Nano Banana Pro  | `fal-ai/gemini-3-pro-image`  | Google Gemini 3 Pro Image  |  
| GPT Image 1.5  | `fal-ai/gpt-image-1/5`  | OpenAI image gen, text+image  |  
| GPT Image 2  | `fal-ai/gpt-image-2`  | OpenAI latest  |  
| Ideogram V3  | `fal-ai/ideogram/v3`  | Strong prompt adherence + typography  |  
| Recraft V4 Pro  | `fal-ai/recraft/v4/pro`  | Vector-style, graphic design  |  
| Qwen Image  | `fal-ai/qwen-image`  | Alibaba multimodal  |  
The set evolves — `hermes tools` → Image Generation shows the current live list.
## Configuration reference[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#configuration-reference "Direct link to Configuration reference")
Most users never need to touch this — `hermes model` and `hermes tools` cover every workflow interactively. This section is for writing config.yaml directly or scripting setups.
### Per-tool `use_gateway` flag[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#per-tool-use_gateway-flag "Direct link to per-tool-use_gateway-flag")
Each tool's config block takes a `use_gateway` boolean:

```
web:backend: firecrawluse_gateway:trueimage_gen:use_gateway:truetts:provider: openaiuse_gateway:truebrowser:cloud_provider: browser-useuse_gateway:true
```

Precedence: `use_gateway: true` routes through Nous regardless of any direct keys in `.env`. `use_gateway: false` (or absent) uses direct keys if available and only falls back to the gateway when none exist.
### Disabling the gateway[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#disabling-the-gateway "Direct link to Disabling the gateway")

```
web:use_gateway:false# Hermes now uses FIRECRAWL_API_KEY from .env
```

`hermes tools` automatically clears the flag when you pick a non-gateway provider, so this usually happens for you.
### Self-hosted gateway (advanced)[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#self-hosted-gateway-advanced "Direct link to Self-hosted gateway \(advanced\)")
Running your own Nous-compatible gateway? Override endpoints in `~/.hermes/.env`:

```
TOOL_GATEWAY_DOMAIN=your-domain.example.comTOOL_GATEWAY_SCHEME=httpsTOOL_GATEWAY_USER_TOKEN=your-token        # normally auto-populated from Portal loginFIRECRAWL_GATEWAY_URL=https://..# override one endpoint specifically
```

These knobs exist for custom infrastructure setups (enterprise deployments, dev environments). Regular subscribers never set them.
## FAQ[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#faq "Direct link to FAQ")
### Does it work with Telegram / Discord / the other messaging gateways?[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#does-it-work-with-telegram--discord--the-other-messaging-gateways "Direct link to Does it work with Telegram / Discord / the other messaging gateways?")
Yes. Tool Gateway operates at the tool-execution layer, not the CLI. Every interface that can call a tool — CLI, Telegram, Discord, Slack, IRC, Teams, the API server, anything — benefits from it transparently.
### What happens if my subscription expires?[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#what-happens-if-my-subscription-expires "Direct link to What happens if my subscription expires?")
Tools routed through the gateway stop working until you renew or swap in direct API keys via `hermes tools`. Hermes shows a clear error pointing at the portal.
### Can I see usage or costs per tool?[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#can-i-see-usage-or-costs-per-tool "Direct link to Can I see usage or costs per tool?")
Yes — the [Nous Portal dashboard](https://portal.nousresearch.com) breaks usage down by tool so you can see what's driving your bill.
### Is Modal (serverless terminal) included?[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#is-modal-serverless-terminal-included "Direct link to Is Modal \(serverless terminal\) included?")
Modal is available as an **optional add-on** through the Nous subscription, not part of the default Tool Gateway bundle. Configure it via `hermes setup terminal` or directly in `config.yaml` when you want a remote sandbox for shell execution.
### Do I need to delete my existing API keys when I enable the gateway?[​](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#do-i-need-to-delete-my-existing-api-keys-when-i-enable-the-gateway "Direct link to Do I need to delete my existing API keys when I enable the gateway?")
No — keep them in `.env`. When `use_gateway: true`, Hermes skips direct keys and uses the gateway. Flip the flag back to `false` and your keys become the source again. The gateway isn't a lock-in.
  * [What's included](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#whats-included)
  * [Why it's here](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#why-its-here)
  * [Get started](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#get-started)
  * [Eligibility](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#eligibility)
  * [Mix and match](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#mix-and-match)
  * [Using individual image models](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#using-individual-image-models)
  * [Configuration reference](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#configuration-reference)
    * [Per-tool `use_gateway` flag](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#per-tool-use_gateway-flag)
    * [Disabling the gateway](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#disabling-the-gateway)
    * [Self-hosted gateway (advanced)](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#self-hosted-gateway-advanced)
  * [FAQ](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#faq)
    * [Does it work with Telegram / Discord / the other messaging gateways?](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#does-it-work-with-telegram--discord--the-other-messaging-gateways)
    * [What happens if my subscription expires?](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#what-happens-if-my-subscription-expires)
    * [Can I see usage or costs per tool?](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#can-i-see-usage-or-costs-per-tool)
    * [Is Modal (serverless terminal) included?](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#is-modal-serverless-terminal-included)
    * [Do I need to delete my existing API keys when I enable the gateway?](https://hermes-agent.nousresearch.com/docs/user-guide/features/tool-gateway#do-i-need-to-delete-my-existing-api-keys-when-i-enable-the-gateway)


