<!-- Source: https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing -->

# Nobody is Talking About Generalized Hill-Climbing (at Runtime)
Pursuing the unbelievably exciting goal of making everything verifiable
February 14, 2026
[ #ai](https://danielmiessler.com/archives/?tag=AI)[ #algorithm](https://danielmiessler.com/archives/?tag=Algorithm)[ #hill-climbing](https://danielmiessler.com/archives/?tag=Hill-Climbing)[ #pai](https://danielmiessler.com/archives/?tag=PAI)
 Prime-directing…
All the labs are using a combination of pre-training and [RL](https://en.wikipedia.org/wiki/Reinforcement_learning) to create better "general" models. Which means they're not just good at one thing but good at many things, and ideally also good at learning new ones.
I barely know RL fundamentals, and the latest implementation details are way beyond me. Plus, to pursue this _model/RL_ approach to generality you need tons of GPUs and money, which means it's mostly the big labs making progress.
**So I've been pursuing a different path to generalized hill-climbing.**
I've been thinking about this loosely since 2023 or 2024, but [Andrej Karpathy](https://karpathy.ai/) really crystallized it for me with this on Twitter:
Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify.Andrej Karpathy
This must have started a fire in me because it's all I've been thinking about since then. To me it prompts the most interesting question in the world:
**How can we make _everything_ verifiable?**
## Ideal State as a path to general verifiability [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#ideal-state-as-a-path-to-general-verifiability)
I've been thinking about [Ideal State](https://danielmiessler.com/blog/ai-state-management) for a long time, but Karpathy's focus on verifiability made it super tangible in my mind. It connected the two ideas for me.
Basically, in order to have ladder rungs or footholds—whatever analogy you want to use for climbing— _there has to be a thing that you're climbing towards_. So, no matter what, the first question is always,
> What is that thing?
To me this is **the whole game**.
Since everything blew up in early 2023, I've been talking about how important prompting is. I wrote [AI is Mostly Prompting](https://danielmiessler.com/blog/ai-is-mostly-prompting) in May of 2024, where I said nothing compares to precise articulation of intent. I wrote [Coding is Thinking](https://danielmiessler.com/blog/thinking-coding) in March of 2025, which was about how writing = thinking, creating = imagining, and coding = building. And most recently I wrote [How to Talk to AI](https://danielmiessler.com/blog/how-to-talk-to-ai) in June of 2025, where my main point was that if you can't articulate what you want, prompting and context won't help you much.
This Ideal State concept is the ultimate example of that.
What I figured out is that the difficult part is _articulating_ the Ideal State for a thing. Especially generally, for lots of different task types.
So that's my core focus: **Reverse engineering requests and combining that with context to create discrete, boolean, testable Ideal State Criteria**.
And what's super cool about that is the Ideal State Criteria carry through to become the VERIFICATION criteria as well! In fact that's their entire point!
When we reverse engineer any request (and then add research and what else we know about the user and task), we're simultaneously building Ideal State _and_ our testing criteria that we'll use to hill-climb.
## Two nested loops [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#two-nested-loops)
So that's IDEAL STATE, and the algorithm is running two nested loops basically to facilitate climbing.
  1. CURRENT STATE ➡︎ IDEAL STATE
  2. IDEA ➡︎ TEST ➡︎ ITERATE


The first is the one we've been talking about: going from whatever your current state is to your _ideal_ state.
That second one has many names, but it's mostly known as the Scientific Method, or—in Cybersecurity—the [OODA loop](https://en.wikipedia.org/wiki/OODA_loop). Basically, take a look at things, try to figure something out, test against reality using an experiment or some other method, and then adjust and try again until you have your answer.
So basically the main game is going from current to ideal, and we do that via the scientific method. And that inner loop can only run when it's chasing something tangible, which is the ideal destination of the outer loop.
## Using the Algorithm [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#using-the-algorithm)
I've built The Algorithm (my cute handle-name I've given it) into our [PAI](https://github.com/danielmiessler/PAI) project (Personal AI Infrastructure) that runs on top of Claude Code. Here's what it looks like in practice.
### Step 1: Reverse Engineering the Request [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#step-1-reverse-engineering-the-request)
Going back to prompting again, I'm reminded of the concept of _writer's blindness_ , where someone has an idea in their mind but are unable to convey it because of all the assumptions it rests on.
So this starting step is super key.
> What does the user actually want? And what do they _not_ want?
Every input gets reverse engineered.
  * What did they explicitly ask for?
  * What did they _imply_?
  * What do they NOT want?
  * What gotchas should we watch for?
  * What are common failure modes for people trying to do this?
  * Etc.


Here I asked Kai (my [DA](https://danielmiessler.com/blog/personal-ai-infrastructure)) to build a content curation website from a voice transcript:
The OBSERVE phase breaking down a complex request into explicit wants, implied wants, and anti-criteria.  
So here it is going through those exact types of steps. It's pulling out not just what I said, but what I _implied_ and what I specifically _don't_ want.
Requests are often full of these unsaid things, and if you want to build verification criteria you have to deconstruct this and get them into your ideal state.
### Step 2: Selecting the Effort Level [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#step-2-selecting-the-effort-level)
"Fix this typo" shouldn't trigger the same machinery as "design my authentication system." The Algorithm assigns an effort level during OBSERVE that controls how deep everything goes:

```
| Tier          | Budget  | When                                    |
|---------------|---------|---------------------------------------- |
| Instant       | <10s    | Trivial lookup, greeting                |
| Fast          | <1min   | Simple fix, skill invocation            |
| Standard      | <2min   | Normal request, no time pressure        |
| Extended      | <8min   | Quality must be extraordinary           |
| Advanced      | <16min  | Full phases, multi-file changes         |
| Deep          | <32min  | Complex design, thorough exploration    |
| Comprehensive | <120min | Don't feel rushed by time               |
```

123456789
The effort level controls the depth of _everything_ —how many criteria to generate, whether to enter Plan Mode, which capabilities to engage, how thorough verification needs to be. A typo fix at Instant might not even run full phases. A system redesign at Deep gets 40+ criteria, enters Plan Mode for structured codebase exploration, and spawns parallel agents.
### Step 3: Creating Ideal State Criteria [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#step-3-creating-ideal-state-criteria)
With the request understood and the effort level set, it creates IDEAL STATE in the form of Ideal State Criteria.
These are 8-12 word, discrete, testable, boolean statements that describe what "done" looks like. These same criteria become the VERIFICATION criteria later.
Creating ISC for a friend's RPG game—each criterion is a testable yes/no condition that defines IDEAL STATE.  
  * Each encounter has unique primary dynamic.
  * No turn-one lethality possible.
  * Difficulty spread across range 1-25.
  * Every one is binary testable.


You look at the output and say YES or NO.
The number of ISC scales with effort level. Simple task: 4-8 criteria. Medium feature: 12-40. Large project: 40-150+, organized into domains with child PRDs.
Same rule everywhere: 8-12 words, state not action, binary testable.
### Step 4: Selecting Capabilities [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#step-4-selecting-capabilities)
The other big thing is giving the algorithm capabilities. It obviously already has tons because Claude Code is brilliant, but I'm specifically steering it towards native and custom stuff I've built to help the algorithm.
There are (currently) ~25 specific capabilities in the Capabilities Matrix, roughly in these categories.
The THINK phase evaluating all 25 built-in capabilities and selecting the right combination for this task.  
  * **Foundation** — Task tracking, user clarification, isolated execution, the 70+ skill library
  * **Thinking & Analysis** — Iterative depth, first principles decomposition, extended creative thinking, plan mode for structured ISC development
  * **Agents** — Specialized workers: Algorithm agents for ISC, Engineers for building, Architects for design, Researchers for investigation
  * **Collaboration & Challenge** — Multi-agent debate (Council), adversarial analysis with 32 agents (RedTeam), coordinated agent swarms
  * **Execution** — Parallelization across background agents, creative branching, git worktree experiments, browser-based visual verification
  * **Testing** — Test runners, static analysis, deterministic CLI probes


This is what makes the system so dynamic. From a 30-second run to hours (and even longer in Loop mode).
A Fast task might only use the Task tool and a single Skill. An Extended task might spin up Council for multi-agent debate, spawn parallel Engineer agents to build, then use our Browser Skill to visually verify. The effort level and capabilities work together—fast for 90% of tasks, heavy when the problem calls for it.
### Step 5: Verification Against Ideal State [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#step-5-verification-against-ideal-state)
Then, kind of the whole point of all of this, we verify.
After building, the Algorithm verifies each ISC criterion one by one against the actual output:
Ideal State Criteria tracked as tasks—each one verified with evidence before it gets checked off.  
Each criterion is a checkbox. Pass or fail. If you fail, you iterate. If everything passes, you've achieved Ideal State for that request.
### The Dashboard: Running in Parallel [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#the-dashboard-running-in-parallel)
I built a dashboard (probably coming to PAI 3.1 or 3.2) that shows multiple Algorithm sessions running simultaneously, each tracking their own ISC criteria through the seven phases:
Multiple Algorithm sessions running in parallel, each with their own Ideal State Criteria and phase progression.  
And PAI also harvests sentiment signal from every response and overlays that on what was done. This way our _PAIUpdate_ skill can use its _UpgradeAlgorithm_ workflow to suggest specific ways to improve the algorithm going forward.
Hill-climbing on its own hill-climbing capability.
### It Works for Everything [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#it-works-for-everything)
The idea is that this isn't limited to software. You can throw anything at it:
  * "Build me a website" → ISC for design, functionality, performance, content
  * "Create 16 RPG encounters" → ISC for balance, variety, dynamics, fun factor
  * "Design a content pipeline" → ISC for architecture, data flow, reliability, extensibility
  * "Help me lose 20kg" → ISC for nutrition plan, exercise routine, tracking, sustainability


The criteria look completely different for each domain, but the _process_ of creating them, verifying against them, and iterating is always the same. That's what makes it generalized.
## I think this is where things are going [​](https://danielmiessler.com/blog/nobody-is-talking-about-generalized-hill-climbing#i-think-this-is-where-things-are-going)
I anticipate labs and other projects catching on to this in the next few months of 2026.
Like I said at the top, the labs are obviously trying to do this already in the models themselves, but I anticipate that their Agentic frameworks will soon have capabilities like The Algorithm as well.
I feel like this concept of _properly reverse engineering and articulating ideal state_ is extremely fertile ground for chasing AGI, and it's about to blow up as a concept.
#### Notes
  1. AIL Level 1: Daniel wrote this entire post from his own ideas and voice recordings. I (Kai, his DA) helped with formatting, screenshots, and generating the header image. [Learn more about AIL](https://danielmiessler.com/blog/ai-influence-level-ail)
  2. Additional reading: 
     * [Pursuing the Algorithm](https://danielmiessler.com/blog/the-last-algorithm) — My original post on the Algorithm concept from January 2026.
     * [AI's Ultimate Use Case: State Management](https://danielmiessler.com/blog/ai-state-management) — My early thoughts on current to ideal state transition from February '25.
     * [Personal AI Infrastructure](https://danielmiessler.com/blog/personal-ai-infrastructure) — The full PAI system that The Algorithm runs inside of.
     * [Claude Code is Proto-AGI](https://danielmiessler.com/blog/claude-code-proto-agi) — Why I think Claude Code is proto-AGI, and why I build on top of it.
     * [AI is Mostly Prompting](https://danielmiessler.com/blog/ai-is-mostly-prompting) — My 2024 post on why precise articulation of intent matters more than anything.
     * [Coding is Thinking](https://danielmiessler.com/blog/thinking-coding) — Writing is thinking, coding is building, and you can't skip the thinking part.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fnobody-is-talking-about-generalized-hill-climbing&title=Nobody%20is%20Talking%20About%20Generalized%20Hill-Climbing%20\(at%20Runtime\) "Share on Hacker News")
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
aialgorithmhillclimbingpai
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
