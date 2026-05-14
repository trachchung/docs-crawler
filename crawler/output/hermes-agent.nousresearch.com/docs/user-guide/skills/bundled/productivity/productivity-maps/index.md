<!-- Source: https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps -->

[Skip to main content](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#__docusaurus_skipToContent_fallback)
On this page
Geocode, POIs, routes, timezones via OpenStreetMap/OSRM.
## Skill metadata[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#skill-metadata "Direct link to Skill metadata")  
| Source  | Bundled (installed by default)  |  
| --- | --- |  
| Path  | `skills/productivity/maps`  |  
| Version  | `1.2.0`  |  
| Author  | Mibayy  |  
| License  | MIT  |  
| Platforms  | linux, macos, windows  |  
| Tags  |  `maps`, `geocoding`, `places`, `routing`, `distance`, `directions`, `nearby`, `location`, `openstreetmap`, `nominatim`, `overpass`, `osrm`  |  
## Reference: full SKILL.md[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#reference-full-skillmd "Direct link to Reference: full SKILL.md")
The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when the skill is active.
# Maps Skill
Location intelligence using free, open data sources. 8 commands, 44 POI categories, zero dependencies (Python stdlib only), no API key required.
Data sources: OpenStreetMap/Nominatim, Overpass API, OSRM, TimeAPI.io.
This skill supersedes the old `find-nearby` skill — all of find-nearby's functionality is covered by the `nearby` command below, with the same `--near "<place>"` shortcut and multi-category support.
## When to Use[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#when-to-use "Direct link to When to Use")
  * User sends a Telegram location pin (latitude/longitude in the message) → `nearby`
  * User wants coordinates for a place name → `search`
  * User has coordinates and wants the address → `reverse`
  * User asks for nearby restaurants, hospitals, pharmacies, hotels, etc. → `nearby`
  * User wants driving/walking/cycling distance or travel time → `distance`
  * User wants turn-by-turn directions between two places → `directions`
  * User wants timezone information for a location → `timezone`
  * User wants to search for POIs within a geographic area → `area` + `bbox`


## Prerequisites[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#prerequisites "Direct link to Prerequisites")
Python 3.8+ (stdlib only — no pip installs needed).
Script path: `~/.hermes/skills/maps/scripts/maps_client.py`
## Commands[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#commands "Direct link to Commands")

```
MAPS=~/.hermes/skills/maps/scripts/maps_client.py
```

### search — Geocode a place name[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#search--geocode-a-place-name "Direct link to search — Geocode a place name")

```
python3 $MAPS search "Eiffel Tower"python3 $MAPS search "1600 Pennsylvania Ave, Washington DC"
```

Returns: lat, lon, display name, type, bounding box, importance score.
### reverse — Coordinates to address[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#reverse--coordinates-to-address "Direct link to reverse — Coordinates to address")

```
python3 $MAPS reverse 48.85842.2945
```

Returns: full address breakdown (street, city, state, country, postcode).
### nearby — Find places by category[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#nearby--find-places-by-category "Direct link to nearby — Find places by category")

```
# By coordinates (from a Telegram location pin, for example)python3 $MAPS nearby 48.85842.2945 restaurant --limit10python3 $MAPS nearby 40.7128-74.0060 hospital --radius2000# By address / city / zip / landmark — --near auto-geocodespython3 $MAPS nearby --near"Times Square, New York"--category cafepython3 $MAPS nearby --near"90210"--category pharmacy# Multiple categories merged into one querypython3 $MAPS nearby --near"downtown austin"--category restaurant --category bar --limit10
```

46 categories: restaurant, cafe, bar, hospital, pharmacy, hotel, guest_house, camp_site, supermarket, atm, gas_station, parking, museum, park, school, university, bank, police, fire_station, library, airport, train_station, bus_stop, church, mosque, synagogue, dentist, doctor, cinema, theatre, gym, swimming_pool, post_office, convenience_store, bakery, bookshop, laundry, car_wash, car_rental, bicycle_rental, taxi, veterinary, zoo, playground, stadium, nightclub.
Each result includes: `name`, `address`, `lat`/`lon`, `distance_m`, `maps_url` (clickable Google Maps link), `directions_url` (Google Maps directions from the search point), and promoted tags when available — `cuisine`, `hours` (opening_hours), `phone`, `website`.
### distance — Travel distance and time[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#distance--travel-distance-and-time "Direct link to distance — Travel distance and time")

```
python3 $MAPS distance "Paris"--to"Lyon"python3 $MAPS distance "New York"--to"Boston"--mode drivingpython3 $MAPS distance "Big Ben"--to"Tower Bridge"--mode walking
```

Modes: driving (default), walking, cycling. Returns road distance, duration, and straight-line distance for comparison.
### directions — Turn-by-turn navigation[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#directions--turn-by-turn-navigation "Direct link to directions — Turn-by-turn navigation")

```
python3 $MAPS directions "Eiffel Tower"--to"Louvre Museum"--mode walkingpython3 $MAPS directions "JFK Airport"--to"Times Square"--mode driving
```

Returns numbered steps with instruction, distance, duration, road name, and maneuver type (turn, depart, arrive, etc.).
### timezone — Timezone for coordinates[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#timezone--timezone-for-coordinates "Direct link to timezone — Timezone for coordinates")

```
python3 $MAPS timezone 48.85842.2945python3 $MAPS timezone 35.6762139.6503
```

Returns timezone name, UTC offset, and current local time.
### area — Bounding box and area for a place[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#area--bounding-box-and-area-for-a-place "Direct link to area — Bounding box and area for a place")

```
python3 $MAPS area "Manhattan, New York"python3 $MAPS area "London"
```

Returns bounding box coordinates, width/height in km, and approximate area. Useful as input for the bbox command.
### bbox — Search within a bounding box[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#bbox--search-within-a-bounding-box "Direct link to bbox — Search within a bounding box")

```
python3 $MAPS bbox 40.75-74.0040.77-73.98 restaurant --limit20
```

Finds POIs within a geographic rectangle. Use `area` first to get the bounding box coordinates for a named place.
## Working With Telegram Location Pins[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#working-with-telegram-location-pins "Direct link to Working With Telegram Location Pins")
When a user sends a location pin, the message contains `latitude:` and `longitude:` fields. Extract those and pass them straight to `nearby`:

```
# User sent a pin at 36.17, -115.14 and asked "find cafes nearby"python3 $MAPS nearby 36.17-115.14 cafe --radius1500
```

Present results as a numbered list with names, distances, and the `maps_url` field so the user gets a tap-to-open link in chat. For "open now?" questions, check the `hours` field; if missing or unclear, verify with `web_search` since OSM hours are community-maintained and not always current.
## Workflow Examples[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#workflow-examples "Direct link to Workflow Examples")
**"Find Italian restaurants near the Colosseum":**
  1. `nearby --near "Colosseum Rome" --category restaurant --radius 500` — one command, auto-geocoded


**"What's near this location pin they sent?":**
  1. Extract lat/lon from the Telegram message
  2. `nearby LAT LON cafe --radius 1500`


**"How do I walk from hotel to conference center?":**
  1. `directions "Hotel Name" --to "Conference Center" --mode walking`


**"What restaurants are in downtown Seattle?":**
  1. `area "Downtown Seattle"` → get bounding box
  2. `bbox S W N E restaurant --limit 30`


## Pitfalls[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#pitfalls "Direct link to Pitfalls")
  * Nominatim ToS: max 1 req/s (handled automatically by the script)
  * `nearby` requires lat/lon OR `--near "<address>"` — one of the two is needed
  * OSRM routing coverage is best for Europe and North America
  * Overpass API can be slow during peak hours; the script automatically falls back between mirrors (overpass-api.de → overpass.kumi.systems)
  * `distance` and `directions` use `--to` flag for the destination (not positional)
  * If a zip code alone gives ambiguous results globally, include country/state


## Verification[​](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#verification "Direct link to Verification")

```
python3 ~/.hermes/skills/maps/scripts/maps_client.py search "Statue of Liberty"# Should return lat ~40.689, lon ~-74.044python3 ~/.hermes/skills/maps/scripts/maps_client.py nearby --near"Times Square"--category restaurant --limit3# Should return a list of restaurants within ~500m of Times Square
```

  * [Skill metadata](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#skill-metadata)
  * [Reference: full SKILL.md](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#reference-full-skillmd)
  * [When to Use](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#when-to-use)
  * [Prerequisites](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#prerequisites)
  * [Commands](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#commands)
    * [search — Geocode a place name](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#search--geocode-a-place-name)
    * [reverse — Coordinates to address](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#reverse--coordinates-to-address)
    * [nearby — Find places by category](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#nearby--find-places-by-category)
    * [distance — Travel distance and time](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#distance--travel-distance-and-time)
    * [directions — Turn-by-turn navigation](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#directions--turn-by-turn-navigation)
    * [timezone — Timezone for coordinates](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#timezone--timezone-for-coordinates)
    * [area — Bounding box and area for a place](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#area--bounding-box-and-area-for-a-place)
    * [bbox — Search within a bounding box](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#bbox--search-within-a-bounding-box)
  * [Working With Telegram Location Pins](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#working-with-telegram-location-pins)
  * [Workflow Examples](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#workflow-examples)
  * [Verification](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/productivity/productivity-maps#verification)


