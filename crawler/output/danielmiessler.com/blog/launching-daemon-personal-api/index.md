<!-- Source: https://danielmiessler.com/blog/launching-daemon-personal-api -->

# Building a Personal API
The first version of a public API endpoint for describing who you are and what you're up to
August 1, 2025
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #projects](https://danielmiessler.com/archives/?tag=projects)[ #api](https://danielmiessler.com/archives/?tag=api)
 Persistence-establishing…
Super hyped to be launching the (very early) first version of _Daemon_ today!
Since 2014 I've been obsessed with this idea of everything having an API. I first talked about it in 2016 in my (kind of crappy but with great ideas) book [The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things).
> So this is the first building block: every object has a daemon—An API to the world that all other objects understand. Any computer, system, or even a human with appropriate access, can look at any other object's daemon and know precisely how to interact with it, what its status is, and what it's capable of. [The Real Internet of Things, 2016](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler/dp/1545327122)
The idea was that it wouldn't just be objects—like cars or restaurants—that got daemons/APIs, but also people.
> Most importantly, humans themselves will also have daemons, and we'll be moving through a world full of other daemons. Human daemons will hold all information about a person, compartmentalized based on type, sensitivity, access restrictions, etc., and that data will be used to send hyper-personalized requests to the daemons around us. [The Real Internet of Things, 2016](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler/dp/1545327122)
## Combining with Digital Assistants [​](https://danielmiessler.com/blog/launching-daemon-personal-api#combining-with-digital-assistants)
And that then clicked with the other main concept, which was that we'd have AI-powered Digital Assistants (DAs) that would constantly process these thousands of APIs that were constantly "around" us, since there's no way we could do that as humans.
> The most visible and significant role that Synthetic Intelligence will play in the near future will be serving as the interface between humans and the world. To clarify, I don't mean the ever-promised, conscious, and self-improving brand of SI that so much science fiction is based on. The SI I'm referring to I define as: A computer system that can monitor human context, intentions, and commands, interpret them, and then take action as well as or better than a (human) professional personal assistant. [The Real Internet of Things, 2016](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler/dp/1545327122)
So the idea was that DAs would fundamentally change how we interact with the things around us using tech. Instead of us using our devices to do it, which doesn't scale, our DAs would be doing it for us.
> Instead of interacting with technology directly, we will interact with our DA, and our DA will work out the details with the necessary daemon. We speak, things happen. We gesture, things happen. We text, things happen. No need to find, understand, or master new tech—that's for the service and the DA to work out amongst themselves. [The Real Internet of Things, 2016](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler/dp/1545327122)
## How I think it'll work in practice [​](https://danielmiessler.com/blog/launching-daemon-personal-api#how-i-think-it-ll-work-in-practice)
So for people specifically, the use case I always think of is the coffee shop, where you're single, and your DA knows you're looking for a relationship, and you walk in and it reads all the daemons in the shop.
You're waiting in line at Starbucks, and Kai (your DA) is continuously reading all the public Daemons (things) and Auras (people) around you. Kai lights up a girl in front of you because she matches on so many things.
  * 7/9 favorite reading match
  * Shy but loving in a relationship
  * Dogs > Cats
  * 😍 She believes it should be legal to kill people who chew loudly


So Kai starts talking to _her_ DA, Tara, and now he and Tara are about to tell you two where to look so you see each other from across the room.
Even everyday objects will have their own auras  
So, Daemon is my early version of this—a public endpoint that serves up-to-date information about me in a format that both humans and AIs can use.
## Architecture [​](https://danielmiessler.com/blog/launching-daemon-personal-api#architecture)
Update Pipeline
Cloudflare Edge
Client Side
HTTPS
Read/Write
Sync
Response
User/AI Agent
JSON-RPC Request
Worker(Daemon MCP)
KV StoragePersonal Data
daemon.md
Update Script
Website Data
f2laom
The Daemon architecture on the Cloudflare MCP  
And here's a rough breakdown of how interactions work.
Daemon MCP architecture on Cloudflare Workers (click for full size)  
## How to Use It [​](https://danielmiessler.com/blog/launching-daemon-personal-api#how-to-use-it)
Daemon runs as an [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) server at `https://daemon.danielmiessler.com`. Here's how to interact with it:
### Get Available Tools [​](https://danielmiessler.com/blog/launching-daemon-personal-api#get-available-tools)
First, see what endpoints are available:
bash
```
curl -X POST https://daemon.danielmiessler.com \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/list",
    "id": 1
  }'
```

1234567
This returns a list of all available tools:
json
```

  "jsonrpc": "2.0",
  "result": {
    "tools": [

        "name": "get_about",
        "description": "Get basic information about Daniel Miessler"
      },

        "name": "get_telos",
        "description": "Get Daniel's TELOS framework - problems, missions, goals"

      // ... more tools

  },
  "id": 1

```

1234567891011121314151617
### Call a Tool [​](https://danielmiessler.com/blog/launching-daemon-personal-api#call-a-tool)
To get information from a specific endpoint, like my TELOS (purpose framework):
bash
```
curl -X POST https://daemon.danielmiessler.com \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
      "name": "get_telos",
      "arguments": {}
    },
    "id": 2
  }'
```

1234567891011
This returns my TELOS framework data:
json
```

  "jsonrpc": "2.0",
  "result": {
    "content": [

        "type": "text",
        "text": "TELOS is my personal framework for tracking purpose and direction in life...\n\nProblems (P):\n- P1: People lack meaning in their lives...\n- P2: People are stuck in a 1950's style hierarchical mindset...\n\nMissions (M):\n- M1: Increase human Eudaimonia...\n- M2: Build systems—heavily leveraging AI..."


  },
  "id": 2

```

123456789101112
## MCP Configuration [​](https://danielmiessler.com/blog/launching-daemon-personal-api#mcp-configuration)
If you want to add Daemon to your [Claude Code](https://github.com/anthropics/claude-code) or other MCP-compatible tools, add this to your MCP config:
json
```

  "mcpServers": {
    "daemon": {
      "url": "https://daemon.danielmiessler.com"



```

1234567
## Available Endpoints [​](https://danielmiessler.com/blog/launching-daemon-personal-api#available-endpoints)
Here's what you can query through Daemon:
  * `get_about` - Basic information about me and what I do
  * `get_narrative` - My personal narrative and focus areas
  * `get_mission` - What I'm trying to accomplish
  * `get_projects` - My current projects
  * `get_telos` - My TELOS framework (Problems, Missions, Goals, Metrics)
  * `get_favorite_books` - My favorite books
  * `get_favorite_movies` - My favorite movies
  * `get_current_location` - Where I am currently
  * `get_preferences` - Personal preferences and work style
  * `get_all` - Get all available data at once
  * `get_section` - Get a specific section by name


## What's Next [​](https://danielmiessler.com/blog/launching-daemon-personal-api#what-s-next)
This is version 0.1 of Daemon. I plan to expand it with more endpoints, real-time updates, and tons more. So many ideas.
I'm currently working on the ability to update my daemon via little voice notes from my iPhone, so like:
> Just landed in Vegas
...and have that get added to the `timeline` and `location` sections of my daemon.
I'll also be putting out a full guide on how to set this up for yourself—or any other entity that you think needs an API.
More to come.
#### Notes
  1. MCP stands for Model Context Protocol - it's Anthropic's new standard for AI agents to interact with external tools and APIs. Learn more at [modelcontextprotocol.io](https://modelcontextprotocol.io/).
  2. The daemon.md file updates are synced via a simple update script that parses the markdown and uploads to [Cloudflare KV](https://developers.cloudflare.com/kv/). And I can actually just give Kai (my digital assistant) verbal updates and he makes all the changes and pushes them within a couple of seconds!
  3. Kai retrieved the header image from my ["AI's Predictable Path"](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024) post and created all the diagrams you see in this post automatically based on the text. If you want to read more about that, check out my [personal AI infrastructure](https://danielmiessler.com/blog/personal-ai-infrastructure) post.
  4. You can my (very short) _The Real Internet of Things_ without dealing with Amazon by reading the [blog post version](https://danielmiessler.com/blog/the-real-internet-of-things) I recently published here in full on the site.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Flaunching-daemon-personal-api&title=Building%20a%20Personal%20API "Share on Hacker News")
Follow
## supporting = loving
For 29.5583 years I've been creating ad-free technical tutorials and essays here. 3.047 pieces and counting. 
It's a one-person effort that's also my livelihood. If it makes your day easier or more pleasant in any way, please consider supporting the work with a monthly or one-time donation. 
It helps me make more content, and is deeply appreciated as well. 🫶🏼 
### Monthly Support
[♥ $5](https://buy.stripe.com/7sY14g3Ne7qq3ybeV20x20m)[♥ $10](https://buy.stripe.com/eVq00c2Jah10gkX9AI0x20n)[♥ $25](https://buy.stripe.com/3cI14gdnO9yy2u714c0x20o)[♥ $50](https://buy.stripe.com/6oUdR2erS9yy5Gj14c0x20p)[♥ $100](https://buy.stripe.com/4gMbIU97y9yy0lZ9AI0x20q)
### One-Time Support
[♥ $5](https://buy.stripe.com/3cIeV66Zq7qq3yb4go0x20r)[♥ $10](https://buy.stripe.com/dRmdR2cjK5ii5Gj14c0x20s)[♥ $25](https://buy.stripe.com/eVq14gabCcKK1q37sA0x20t)[♥ $50](https://buy.stripe.com/14AcMY2Ja8uub0D28g0x20u)[♥ $100](https://buy.stripe.com/28E9AM5Vm1220lZfZ60x20v)
Search
This post was tagged with:
aitechnologyprojectsapi
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
