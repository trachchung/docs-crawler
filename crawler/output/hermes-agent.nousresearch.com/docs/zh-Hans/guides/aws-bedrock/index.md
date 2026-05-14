<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock -->

本页总览
Hermes Agent supports Amazon Bedrock as a native provider using the **Converse API** — not the OpenAI-compatible endpoint. This gives you full access to the Bedrock ecosystem: IAM authentication, Guardrails, cross-region inference profiles, and all foundation models.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#prerequisites "Prerequisites的直接链接")
  * **AWS credentials** — any source supported by the [boto3 credential chain](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html): 
    * IAM instance role (EC2, ECS, Lambda — zero config)
    * `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY` environment variables
    * `AWS_PROFILE` for SSO or named profiles
    * `aws configure` for local development
  * **boto3** — install with `pip install hermes-agent[bedrock]`
  * **IAM permissions** — at minimum: 
    * `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream` (for inference)
    * `bedrock:ListFoundationModels` and `bedrock:ListInferenceProfiles` (for model discovery)


On AWS compute, attach an IAM role with `AmazonBedrockFullAccess` and you're done. No API keys, no `.env` configuration — Hermes detects the instance role automatically.
## Quick Start[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#quick-start "Quick Start的直接链接")

```
# Install with Bedrock supportpip install hermes-agent[bedrock]# Select Bedrock as your providerhermes model# → Choose "More providers..." → "AWS Bedrock"# → Select your region and model# Start chattinghermes chat
```

## Configuration[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#configuration "Configuration的直接链接")
After running `hermes model`, your `~/.hermes/config.yaml` will contain:

```
model:default: us.anthropic.claude-sonnet-4-6provider: bedrockbase_url: https://bedrock-runtime.us-east-2.amazonaws.combedrock:region: us-east-2
```

### Region[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#region "Region的直接链接")
Set the AWS region in any of these ways (highest priority first):
  1. `bedrock.region` in `config.yaml`
  2. `AWS_REGION` environment variable
  3. `AWS_DEFAULT_REGION` environment variable
  4. Default: `us-east-1`


### Guardrails[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#guardrails "Guardrails的直接链接")
To apply [Amazon Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) to all model invocations:

```
bedrock:region: us-east-2guardrail:guardrail_identifier:"abc123def456"# From the Bedrock consoleguardrail_version:"1"# Version number or "DRAFT"stream_processing_mode:"async"# "sync" or "async"trace:"disabled"# "enabled", "disabled", or "enabled_full"
```

### Model Discovery[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#model-discovery "Model Discovery的直接链接")
Hermes auto-discovers available models via the Bedrock control plane. You can customize discovery:

```
bedrock:discovery:enabled:trueprovider_filter:["anthropic","amazon"]# Only show these providersrefresh_interval:3600# Cache for 1 hour
```

## Available Models[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#available-models "Available Models的直接链接")
Bedrock models use **inference profile IDs** for on-demand invocation. The `hermes model` picker shows these automatically, with recommended models at the top:  
| Model  | ID  | Notes  |  
| --- | --- | --- |  
| Claude Sonnet 4.6  | `us.anthropic.claude-sonnet-4-6`  | Recommended — best balance of speed and capability  |  
| Claude Opus 4.6  | `us.anthropic.claude-opus-4-6-v1`  | Most capable  |  
| Claude Haiku 4.5  | `us.anthropic.claude-haiku-4-5-20251001-v1:0`  | Fastest Claude  |  
| Amazon Nova Pro  | `us.amazon.nova-pro-v1:0`  | Amazon's flagship  |  
| Amazon Nova Micro  | `us.amazon.nova-micro-v1:0`  | Fastest, cheapest  |  
| DeepSeek V3.2  | `deepseek.v3.2`  | Strong open model  |  
| Llama 4 Scout 17B  | `us.meta.llama4-scout-17b-instruct-v1:0`  | Meta's latest  |  
Models prefixed with `us.` use cross-region inference profiles, which provide better capacity and automatic failover across AWS regions. Models prefixed with `global.` route across all available regions worldwide.
## Switching Models Mid-Session[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#switching-models-mid-session "Switching Models Mid-Session的直接链接")
Use the `/model` command during a conversation:

```
/model us.amazon.nova-pro-v1:0/model deepseek.v3.2/model us.anthropic.claude-opus-4-6-v1
```

## Diagnostics[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#diagnostics "Diagnostics的直接链接")

```
hermes doctor
```

The doctor checks:
  * Whether AWS credentials are available (env vars, IAM role, SSO)
  * Whether `boto3` is installed
  * Whether the Bedrock API is reachable (ListFoundationModels)
  * Number of available models in your region


## Gateway (Messaging Platforms)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#gateway-messaging-platforms "Gateway \(Messaging Platforms\)的直接链接")
Bedrock works with all Hermes gateway platforms (Telegram, Discord, Slack, Feishu, etc.). Configure Bedrock as your provider, then start the gateway normally:

```
hermes gateway setuphermes gateway start
```

The gateway reads `config.yaml` and uses the same Bedrock provider configuration.
## Troubleshooting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#troubleshooting "Troubleshooting的直接链接")
### "No API key found" / "No AWS credentials"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#no-api-key-found--no-aws-credentials ""No API key found" / "No AWS credentials"的直接链接")
Hermes checks for credentials in this order:
  1. `AWS_BEARER_TOKEN_BEDROCK`
  2. `AWS_ACCESS_KEY_ID` + `AWS_SECRET_ACCESS_KEY`
  3. `AWS_PROFILE`
  4. EC2 instance metadata (IMDS)
  5. ECS container credentials
  6. Lambda execution role


If none are found, run `aws configure` or attach an IAM role to your compute instance.
### "Invocation of model ID ... with on-demand throughput isn't supported"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#invocation-of-model-id--with-on-demand-throughput-isnt-supported ""Invocation of model ID ... with on-demand throughput isn't supported"的直接链接")
Use an **inference profile ID** (prefixed with `us.` or `global.`) instead of the bare foundation model ID. For example:
  * ❌ `anthropic.claude-sonnet-4-6`
  * ✅ `us.anthropic.claude-sonnet-4-6`


### "ThrottlingException"[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#throttlingexception ""ThrottlingException"的直接链接")
You've hit the Bedrock per-model rate limit. Hermes automatically retries with backoff. To increase limits, request a quota increase in the [AWS Service Quotas console](https://console.aws.amazon.com/servicequotas/).
## One-Click AWS Deployment[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#one-click-aws-deployment "One-Click AWS Deployment的直接链接")
For a fully automated deployment on EC2 with CloudFormation:
**[sample-hermes-agent-on-aws-with-bedrock](https://github.com/JiaDe-Wu/sample-hermes-agent-on-aws-with-bedrock)** — creates VPC, IAM role, EC2 instance, and configures Bedrock automatically. Deploy in any region with one click.
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#prerequisites)
  * [Quick Start](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#quick-start)
  * [Configuration](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#configuration)
    * [Model Discovery](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#model-discovery)
  * [Available Models](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#available-models)
  * [Switching Models Mid-Session](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#switching-models-mid-session)
  * [Diagnostics](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#diagnostics)
  * [Gateway (Messaging Platforms)](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#gateway-messaging-platforms)
  * [Troubleshooting](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#troubleshooting)
    * ["No API key found" / "No AWS credentials"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#no-api-key-found--no-aws-credentials)
    * ["Invocation of model ID ... with on-demand throughput isn't supported"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#invocation-of-model-id--with-on-demand-throughput-isnt-supported)
    * ["ThrottlingException"](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#throttlingexception)
  * [One-Click AWS Deployment](https://hermes-agent.nousresearch.com/docs/zh-Hans/guides/aws-bedrock#one-click-aws-deployment)


