<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#__docusaurus_skipToContent_fallback)
On this page
Control Philips Hue lights, scenes, rooms via OpenHue CLI.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#skill-metadata "Direct link to Skill metadata")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/smart-home/openhue`  |  
| Version  | `1.0.0`  |  
| Author  | community  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `Smart-Home`, `Hue`, `Lights`, `IoT`, `Automation`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# OpenHue CLI
Control Philips Hue lights and scenes via a Hue Bridge from the terminal.
## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#prerequisites "Direct link to Prerequisites")

```
# Linux (pre-built binary)curl-sL https://github.com/openhue/openhue-cli/releases/latest/download/openhue-linux-amd64 -o ~/.local/bin/openhue &&chmod +x ~/.local/bin/openhue# macOSbrew install openhue/cli/openhue-cli
```

First run requires pressing the button on your Hue Bridge to pair. The bridge must be on the same local network.
## When to Use[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#when-to-use "Direct link to When to Use")
  * "Turn on/off the lights"
  * "Dim the living room lights"
  * "Set a scene" or "movie mode"
  * Controlling specific Hue rooms, zones, or individual bulbs
  * Adjusting brightness, color, or color temperature


## Common Commands[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#common-commands "Direct link to Common Commands")
### List Resources[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#list-resources "Direct link to List Resources")

```
openhue get light       # List all lightsopenhue get room        # List all roomsopenhue get scene       # List all scenes
```

### Control Lights[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#control-lights "Direct link to Control Lights")

```
# Turn on/offopenhue set light "Bedroom Lamp"--onopenhue set light "Bedroom Lamp"--off# Brightness (0-100)openhue set light "Bedroom Lamp"--on--brightness50# Color temperature (warm to cool: 153-500 mirek)openhue set light "Bedroom Lamp"--on--temperature300# Color (by name or hex)openhue set light "Bedroom Lamp"--on--color redopenhue set light "Bedroom Lamp"--on--rgb"#FF5500"
```

### Control Rooms[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#control-rooms "Direct link to Control Rooms")

```
# Turn off entire roomopenhue set room "Bedroom"--off# Set room brightnessopenhue set room "Bedroom"--on--brightness30
```

### Scenes[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#scenes "Direct link to Scenes")

```
openhue set scene "Relax"--room"Bedroom"openhue set scene "Concentrate"--room"Office"
```

## Quick Presets[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#quick-presets "Direct link to Quick Presets")

```
# Bedtime (dim warm)openhue set room "Bedroom"--on--brightness20--temperature450# Work mode (bright cool)openhue set room "Office"--on--brightness100--temperature250# Movie mode (dim)openhue set room "Living Room"--on--brightness10# Everything offopenhue set room "Bedroom"--offopenhue set room "Office"--offopenhue set room "Living Room"--off
```

## Notes[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#notes "Direct link to Notes")
  * Bridge must be on the same local network as the machine running Hermes
  * First run requires physically pressing the button on the Hue Bridge to authorize
  * Colors only work on color-capable bulbs (not white-only models)
  * Light and room names are case-sensitive — use `openhue get light` to check exact names
  * Works great with cron jobs for scheduled lighting (e.g. dim at bedtime, bright at wake)


  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#reference-full-skillmd)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#prerequisites)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#when-to-use)
  * [Common Commands](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#common-commands)
    * [List Resources](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#list-resources)
    * [Control Lights](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#control-lights)
    * [Control Rooms](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#control-rooms)
  * [Quick Presets](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/smart-home/smart-home-openhue#quick-presets)


