<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing -->

本页总览
When using [OpenRouter](https://openrouter.ai) as your LLM provider, Hermes Agent supports **provider routing** — fine-grained control over which underlying AI providers handle your requests and how they're prioritized.
OpenRouter routes requests to many providers (e.g., Anthropic, Google, AWS Bedrock, Together AI). Provider routing lets you optimize for cost, speed, quality, or enforce specific provider requirements.
## Configuration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#configuration "Configuration的直接链接")
Add a `provider_routing` section to your `~/.hermes/config.yaml`:

```
provider_routing:sort:"price"# How to rank providersonly:[]# Whitelist: only use these providersignore:[]# Blacklist: never use these providersorder:[]# Explicit provider priority orderrequire_parameters:false# Only use providers that support all parametersdata_collection:null# Control data collection ("allow" or "deny")
```

Provider routing only applies when using OpenRouter. It has no effect with direct provider connections (e.g., connecting directly to the Anthropic API).
## Options[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#options "Options的直接链接")
###  `sort`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#sort "sort的直接链接")
Controls how OpenRouter ranks available providers for your request.  
| Value  | Description  |  
| --- | --- |  
| `"price"`  | Cheapest provider first  |  
| `"throughput"`  | Fastest tokens-per-second first  |  
| `"latency"`  | Lowest time-to-first-token first  |  

```
provider_routing:sort:"price"
```

###  `only`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#only "only的直接链接")
Whitelist of provider names. When set, **only** these providers will be used. All others are excluded.

```
provider_routing:only:-"Anthropic"-"Google"
```

###  `ignore`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#ignore "ignore的直接链接")
Blacklist of provider names. These providers will **never** be used, even if they offer the cheapest or fastest option.

```
provider_routing:ignore:-"Together"-"DeepInfra"
```

###  `order`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#order "order的直接链接")
Explicit priority order. Providers listed first are preferred. Unlisted providers are used as fallbacks.

```
provider_routing:order:-"Anthropic"-"Google"-"AWS Bedrock"
```

###  `require_parameters`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#require_parameters "require_parameters的直接链接")
When `true`, OpenRouter will only route to providers that support **all** parameters in your request (like `temperature`, `top_p`, `tools`, etc.). This avoids silent parameter drops.

```
provider_routing:require_parameters:true
```

###  `data_collection`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#data_collection "data_collection的直接链接")
Controls whether providers can use your prompts for training. Options are `"allow"` or `"deny"`.

```
provider_routing:data_collection:"deny"
```

## Practical Examples[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#practical-examples "Practical Examples的直接链接")
### Optimize for Cost[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#optimize-for-cost "Optimize for Cost的直接链接")
Route to the cheapest available provider. Good for high-volume usage and development:

```
provider_routing:sort:"price"
```

### Optimize for Speed[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#optimize-for-speed "Optimize for Speed的直接链接")
Prioritize low-latency providers for interactive use:

```
provider_routing:sort:"latency"
```

### Optimize for Throughput[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#optimize-for-throughput "Optimize for Throughput的直接链接")
Best for long-form generation where tokens-per-second matters:

```
provider_routing:sort:"throughput"
```

### Lock to Specific Providers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#lock-to-specific-providers "Lock to Specific Providers的直接链接")
Ensure all requests go through a specific provider for consistency:

```
provider_routing:only:-"Anthropic"
```

### Avoid Specific Providers[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#avoid-specific-providers "Avoid Specific Providers的直接链接")
Exclude providers you don't want to use (e.g., for data privacy):

```
provider_routing:ignore:-"Together"-"Lepton"data_collection:"deny"
```

### Preferred Order with Fallbacks[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#preferred-order-with-fallbacks "Preferred Order with Fallbacks的直接链接")
Try your preferred providers first, fall back to others if unavailable:

```
provider_routing:order:-"Anthropic"-"Google"require_parameters:true
```

## How It Works[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#how-it-works "How It Works的直接链接")
Provider routing preferences are passed to the OpenRouter API via the `extra_body.provider` field on every API call. This applies to both:
  * **CLI mode** — configured in `~/.hermes/config.yaml`, loaded at startup
  * **Gateway mode** — same config file, loaded when the gateway starts


The routing config is read from `config.yaml` and passed as parameters when creating the `AIAgent`:

```
providers_allowed  ← from provider_routing.onlyproviders_ignored  ← from provider_routing.ignoreproviders_order    ← from provider_routing.orderprovider_sort      ← from provider_routing.sortprovider_require_parameters ← from provider_routing.require_parametersprovider_data_collection    ← from provider_routing.data_collection
```

You can combine multiple options. For example, sort by price but exclude certain providers and require parameter support:

```
provider_routing:sort:"price"ignore:["Together"]require_parameters:truedata_collection:"deny"
```

## Default Behavior[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#default-behavior "Default Behavior的直接链接")
When no `provider_routing` section is configured (the default), OpenRouter uses its own default routing logic, which generally balances cost and availability automatically.
Provider routing controls which **sub-providers within OpenRouter** handle your requests. For automatic failover to an entirely different provider when your primary model fails, see [Fallback Providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/docs/user-guide/features/fallback-providers).
  * [Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#configuration)
  * [Options](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#options)
    * [`require_parameters`](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#require_parameters)
    * [`data_collection`](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#data_collection)
  * [Practical Examples](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#practical-examples)
    * [Optimize for Cost](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#optimize-for-cost)
    * [Optimize for Speed](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#optimize-for-speed)
    * [Optimize for Throughput](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#optimize-for-throughput)
    * [Lock to Specific Providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#lock-to-specific-providers)
    * [Avoid Specific Providers](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#avoid-specific-providers)
    * [Preferred Order with Fallbacks](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#preferred-order-with-fallbacks)
  * [How It Works](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#how-it-works)
  * [Default Behavior](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/features/provider-routing#default-behavior)


