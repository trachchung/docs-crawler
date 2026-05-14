<!-- Source: https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant -->

本页总览
Hermes Agent integrates with [Home Assistant](https://www.home-assistant.io/) in two ways:
  1. **Gateway platform** — subscribes to real-time state changes via WebSocket and responds to events
  2. **Smart home tools** — four LLM-callable tools for querying and controlling devices via the REST API


## Setup[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#setup "Setup的直接链接")
### 1. Create a Long-Lived Access Token[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#1-create-a-long-lived-access-token "1. Create a Long-Lived Access Token的直接链接")
  1. Open your Home Assistant instance
  2. Go to your **Profile** (click your name in the sidebar)
  3. Scroll to **Long-Lived Access Tokens**
  4. Click **Create Token** , give it a name like "Hermes Agent"
  5. Copy the token


### 2. Configure Environment Variables[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#2-configure-environment-variables "2. Configure Environment Variables的直接链接")

```
# Add to ~/.hermes/.env# Required: your Long-Lived Access TokenHASS_TOKEN=your-long-lived-access-token# Optional: HA URL (default: http://homeassistant.local:8123)HASS_URL=http://192.168.1.100:8123
```

The `homeassistant` toolset is automatically enabled when `HASS_TOKEN` is set. Both the gateway platform and the device control tools activate from this single token.
### 3. Start the Gateway[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#3-start-the-gateway "3. Start the Gateway的直接链接")

```
hermes gateway
```

Home Assistant will appear as a connected platform alongside any other messaging platforms (Telegram, Discord, etc.).
## Available Tools[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#available-tools "Available Tools的直接链接")
Hermes Agent registers four tools for smart home control:
###  `ha_list_entities`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#ha_list_entities "ha_list_entities的直接链接")
List Home Assistant entities, optionally filtered by domain or area.
**Parameters:**
  * `domain` _(optional)_ — Filter by entity domain: `light`, `switch`, `climate`, `sensor`, `binary_sensor`, `cover`, `fan`, `media_player`, etc.
  * `area` _(optional)_ — Filter by area/room name (matches against friendly names): `living room`, `kitchen`, `bedroom`, etc.


**Example:**

```
List all lights in the living room
```

Returns entity IDs, states, and friendly names.
###  `ha_get_state`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#ha_get_state "ha_get_state的直接链接")
Get detailed state of a single entity, including all attributes (brightness, color, temperature setpoint, sensor readings, etc.).
**Parameters:**
  * `entity_id` _(required)_ — The entity to query, e.g., `light.living_room`, `climate.thermostat`, `sensor.temperature`


**Example:**

```
What's the current state of climate.thermostat?
```

Returns: state, all attributes, last changed/updated timestamps.
###  `ha_list_services`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#ha_list_services "ha_list_services的直接链接")
List available services (actions) for device control. Shows what actions can be performed on each device type and what parameters they accept.
**Parameters:**
  * `domain` _(optional)_ — Filter by domain, e.g., `light`, `climate`, `switch`


**Example:**

```
What services are available for climate devices?
```

###  `ha_call_service`[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#ha_call_service "ha_call_service的直接链接")
Call a Home Assistant service to control a device.
**Parameters:**
  * `domain` _(required)_ — Service domain: `light`, `switch`, `climate`, `cover`, `media_player`, `fan`, `scene`, `script`
  * `service` _(required)_ — Service name: `turn_on`, `turn_off`, `toggle`, `set_temperature`, `set_hvac_mode`, `open_cover`, `close_cover`, `set_volume_level`
  * `entity_id` _(optional)_ — Target entity, e.g., `light.living_room`
  * `data` _(optional)_ — Additional parameters as a JSON object


**Examples:**

```
Turn on the living room lights→ ha_call_service(domain="light", service="turn_on", entity_id="light.living_room")
```


```
Set the thermostat to 22 degrees in heat mode→ ha_call_service(domain="climate", service="set_temperature",    entity_id="climate.thermostat", data={"temperature": 22, "hvac_mode": "heat"})
```


```
Set living room lights to blue at 50% brightness→ ha_call_service(domain="light", service="turn_on",    entity_id="light.living_room", data={"brightness": 128, "color_name": "blue"})
```

## Gateway Platform: Real-Time Events[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#gateway-platform-real-time-events "Gateway Platform: Real-Time Events的直接链接")
The Home Assistant gateway adapter connects via WebSocket and subscribes to `state_changed` events. When a device state changes and matches your filters, it's forwarded to the agent as a message.
### Event Filtering[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#event-filtering "Event Filtering的直接链接")
By default, **no events are forwarded**. You must configure at least one of `watch_domains`, `watch_entities`, or `watch_all` to receive events. Without filters, a warning is logged at startup and all state changes are silently dropped.
Configure which events the agent sees in `~/.hermes/config.yaml` under the Home Assistant platform's `extra` section:

```
platforms:homeassistant:enabled:trueextra:watch_domains:- climate- binary_sensor- alarm_control_panel- lightwatch_entities:- sensor.front_door_batteryignore_entities:- sensor.uptime- sensor.cpu_usage- sensor.memory_usagecooldown_seconds:30
```
  
| Setting  | Default  | Description  |  
| --- | --- | --- |  
| `watch_domains`  | _(none)_  | Only watch these entity domains (e.g., `climate`, `light`, `binary_sensor`)  |  
| `watch_entities`  | _(none)_  | Only watch these specific entity IDs  |  
| `watch_all`  | `false`  | Set to `true` to receive **all** state changes (not recommended for most setups)  |  
| `ignore_entities`  | _(none)_  | Always ignore these entities (applied before domain/entity filters)  |  
| `cooldown_seconds`  | `30`  | Minimum seconds between events for the same entity  |  
Start with a focused set of domains — `climate`, `binary_sensor`, and `alarm_control_panel` cover the most useful automations. Add more as needed. Use `ignore_entities` to suppress noisy sensors like CPU temperature or uptime counters.
### Event Formatting[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#event-formatting "Event Formatting的直接链接")
State changes are formatted as human-readable messages based on domain:  
| Domain  | Format  |  
| --- | --- |  
| `climate`  | "HVAC mode changed from 'off' to 'heat' (current: 21, target: 23)"  |  
| `sensor`  | "changed from 21°C to 22°C"  |  
| `binary_sensor`  | "triggered" / "cleared"  |  
|  `light`, `switch`, `fan`  | "turned on" / "turned off"  |  
| `alarm_control_panel`  | "alarm state changed from 'armed_away' to 'triggered'"  |  
| _(other)_  | "changed from 'old' to 'new'"  |  
### Agent Responses[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#agent-responses "Agent Responses的直接链接")
Outbound messages from the agent are delivered as **Home Assistant persistent notifications** (via `persistent_notification.create`). These appear in the HA notification panel with the title "Hermes Agent".
### Connection Management[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#connection-management "Connection Management的直接链接")
  * **WebSocket** with 30-second heartbeat for real-time events
  * **Automatic reconnection** with backoff: 5s → 10s → 30s → 60s
  * **REST API** for outbound notifications (separate session to avoid WebSocket conflicts)
  * **Authorization** — HA events are always authorized (no user allowlist needed, since the `HASS_TOKEN` authenticates the connection)


## Security[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#security "Security的直接链接")
The Home Assistant tools enforce security restrictions:
The following service domains are **blocked** to prevent arbitrary code execution on the HA host:
  * `shell_command` — arbitrary shell commands
  * `command_line` — sensors/switches that execute commands
  * `python_script` — scripted Python execution
  * `pyscript` — broader scripting integration
  * `hassio` — addon control, host shutdown/reboot
  * `rest_command` — HTTP requests from HA server (SSRF vector)


Attempting to call services in these domains returns an error.
Entity IDs are validated against the pattern `^[a-z_][a-z0-9_]*\.[a-z0-9_]+$` to prevent injection attacks.
## Example Automations[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#example-automations "Example Automations的直接链接")
### Morning Routine[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#morning-routine "Morning Routine的直接链接")

```
User: Start my morning routineAgent:1. ha_call_service(domain="light", service="turn_on",     entity_id="light.bedroom", data={"brightness": 128})2. ha_call_service(domain="climate", service="set_temperature",     entity_id="climate.thermostat", data={"temperature": 22})3. ha_call_service(domain="media_player", service="turn_on",     entity_id="media_player.kitchen_speaker")
```

### Security Check[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#security-check "Security Check的直接链接")

```
User: Is the house secure?Agent:1. ha_list_entities(domain="binary_sensor")     → checks door/window sensors2. ha_get_state(entity_id="alarm_control_panel.home")     → checks alarm status3. ha_list_entities(domain="lock")     → checks lock states4. Reports: "All doors closed, alarm is armed_away, all locks engaged."
```

### Reactive Automation (via Gateway Events)[​](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#reactive-automation-via-gateway-events "Reactive Automation \(via Gateway Events\)的直接链接")
When connected as a gateway platform, the agent can react to events:

```
[Home Assistant] Front Door: triggered (was cleared)Agent automatically:1. ha_get_state(entity_id="binary_sensor.front_door")2. ha_call_service(domain="light", service="turn_on",     entity_id="light.hallway")3. Sends notification: "Front door opened. Hallway lights turned on."
```

  * [Setup](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#setup)
    * [1. Create a Long-Lived Access Token](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#1-create-a-long-lived-access-token)
    * [2. Configure Environment Variables](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#2-configure-environment-variables)
    * [3. Start the Gateway](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#3-start-the-gateway)
  * [Available Tools](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#available-tools)
    * [`ha_list_entities`](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#ha_list_entities)
    * [`ha_get_state`](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#ha_get_state)
    * [`ha_list_services`](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#ha_list_services)
    * [`ha_call_service`](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#ha_call_service)
  * [Gateway Platform: Real-Time Events](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#gateway-platform-real-time-events)
    * [Event Filtering](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#event-filtering)
    * [Event Formatting](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#event-formatting)
    * [Agent Responses](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#agent-responses)
    * [Connection Management](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#connection-management)
  * [Example Automations](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#example-automations)
    * [Morning Routine](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#morning-routine)
    * [Security Check](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#security-check)
    * [Reactive Automation (via Gateway Events)](https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/homeassistant#reactive-automation-via-gateway-events)


