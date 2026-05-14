<!-- Source: https://danielmiessler.com/blog/personal-ai-maturity-model -->

# A Personal AI Maturity Model (PAIMM)
9 tiers of personal AI progress, from chatbots to a full AI companion
December 15, 2025
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #future](https://danielmiessler.com/archives/?tag=future)[ #personal](https://danielmiessler.com/archives/?tag=personal)
 Glanding-charge…
5 reading now 
As we think about what's happening with Agents, Agent frameworks like [Claude Code](https://claude.com/claude-code), voice interfaces, etc, I invite you to ask a simple question:
**Where is this all going?**
  1. What are we actually building towards?
  2. How far along are we?
  3. How many more steps are there?
  4. What is the current next step?


My overall approach to answering these is to imagine the ideal capabilities of an AI companion system—through the lens of what humans eternally strive for—**and work backwards**.
So that's what this maturity model does, in 9 ascending levels.
# A simple 9-level framework [​](https://danielmiessler.com/blog/personal-ai-maturity-model#a-simple-9-level-framework)
**The idea is to have handles for talking about—and working on—progression towards the destination.**
So here are the tiers: from past, through current, to future states.
## TIER 1 - CHATBOTS [​](https://danielmiessler.com/blog/personal-ai-maturity-model#tier-1-chatbots)
The first interface to modern AI. You ask a question and you get back an extraordinarily useful answer. And you take it from there.
This was ChatGPT when it first came out. Brilliant. Limited.
  * Just a chat interface
  * No tools
  * No knowledge of you whatsoever
  * Mindblowing compared to not having anything, but definitely early days


The beginning of some tools and some rudimentary memory features.
  * Still just chat
  * Tools are still basic
  * Limited knowledge of you and your goals


Chatbots' final form before moving into Agents.
  * Tooling far more advanced now
  * Additional context and memory features
  * Agents are still mostly experimental


## Breaking these across 6 dimensions [​](https://danielmiessler.com/blog/personal-ai-maturity-model#breaking-these-across-6-dimensions)
Another way to break down the transitions is as a set of spectrums across 6 dimensions.
  * **Context** [ None -> Basic Knowledge -> Deep Knowledge -> Understanding of Purpose/Goals ]
  * **Personality** [ None -> Basic Personality -> Persistent Personality/Preferences -> Human-like ]
  * **Tool Use** [ None -> Basic Tools -> Advanced Computer Use -> Platform Fluency ]
  * **Awareness** [ None -> Voice Receive -> Computer Visibility -> Persistent Personal Voice/Sight ]
  * **Proactivity** [ None -> Scheduled Tasks/Triggers -> State Monitoring and Execution -> Continuous Advocacy ]
  * **Multitask Scale** [ Self -> Dozens of Tool Calls/Second -> Dozens of Agents Simultaneously -> Hundreds/Thousands Simultaneously ]


## TIER 2 - AGENTS [​](https://danielmiessler.com/blog/personal-ai-maturity-model#tier-2-agents)
Instead of us asking questions and getting answers from Chatbots, we assign work to Agents that can autonomously do work on our behalf.
The initial transition from Chatbots to Agents as the main way of thinking about and using AI.
  * Standalone agents via LangGraph, other frameworks
  * Early 2025 acceleration
  * Claude Code and n8n makes them mainstream
  * Claude Code best/most-used example, but CLI-based
  * Agents are mostly ephemeral (n8n/similar being the exception)
  * Early voice interaction stuff
  * Experimental computer usage


Agents start to become the main mental model for AI work.
  * Agents become a lot more controllable and deterministic due to scaffolding of Agentic Systems like Claude Code
  * Background and scheduled agents starting to materialize
  * Voice accelerates as a usage pattern
  * Early signs of universal accessibility, e.g., you can interact with your agents via a mobile app or OS assistant
  * Computer usage gets more serious but still isn't mainstream


> Predictions are hard, especially about the future.Niels Bohr
The final form of Agents vs. Assistants, with the main distinction being personality and trust.
  * Agents are now both interactive but also running continuously in the background, both locally and in the cloud
  * Agents easily manageable from mobile / device when not on main system / traveling / etc.
  * Extensive use of voice as the interface
  * Computer usage becomes viable and adoption begins
  * Very advanced and steerable, but still mostly reactive vs. proactive


## TIER 3 - ASSISTANTS [​](https://danielmiessler.com/blog/personal-ai-maturity-model#tier-3-assistants)
Instead of random Agents performing work, we have a named, trusted Assistant that works with us to further our goals.
The transition begins from focus on Agents to the concept of an Assistant that _uses Agents in the background_ to proactively pursue your goals.
  * The first transition to _Proactive vs. Reactive_
  * Assistants start to have initial personalities, both through the providers and also through custom scaffolding (persistent personality context)
  * Assistants start to become our primary interface to AI
  * Agents start to become less important, background elements that are working to do the bidding of your Assistant


  * Your Assistant's context about you starts including things like your Goals, Challenges, Metrics, Projects, and other aspects of your life
  * Voice overtakes typing as primary interface
  * Your Assistant can now (significantly) see and hear what's happening on your computer
  * Early signs of personal cameras and microphones that you can wear on your body (not just while on your computer) to give your Assistant awareness of your environment, i.e., seeing and hearing what you're seeing and hearing, watching behind you and around you, etc.


Assistant personalities start to crystallize and they begin performing as _Proactive Advocates_ of us and our goals, vs. reactive helpers.
  * Initial unification of all inputs into a cohesive picture that your Assistant can see and understand


  * Full Agent orchestration, including spin up and spin down, custom task assignment, etc., all happening transparently in the background without your knowledge

💡 Somewhere around AS2 or AS3 is when we'll likely start to see deeper integration with [AR interfaces](https://danielmiessler.com/blog/the-real-internet-of-things#augmented-reality), as they become available. AR is largely a hardware miniaturization issue, and it's difficult to predict when the hardware will get small/good enough.
  * The introduction of your Assistant understanding what you're trying to do in life, your goals, the metrics that matter to you, etc., which will allow him/her/it to start thinking proactively on how to help you accomplish them
  * We start to see the concept of [Managing State](https://danielmiessler.com/blog/ai-state-management), i.e., your Assistant takes periodic inventory of all inputs and assesses _Current State_ relative to _Desired State_ , in order to plan actions to move towards Desired State
  * Nearly full usage of any of your computing environments / interfaces


AS3 is the final level of this maturity model. This is the Digital Assistant I described in 2016, and that has been partially depicted in various ways in sci-fi books and films for decades.
There are many more features that can be added as you go further in time and tech, but I'm thinking really only up to 5-10 years from now. Even beyond 5 years is nutty given how fast things are changing.
Here are the main characteristics of AS3.
💡 You might scoff at the idea of people including sensitive stuff like traumas and one's journal, but I think people's DAs will be the closest thing/person to many people. And just as with humans, relationships are closer when people know the why's behind the what's.Plus, as DA's, they can also assist you better if they know the internal challenges you're grappling with.
  * **Trusted Companion** —AS3-level Assistants feel more like trusted companions, partners, protectors, friends, and confidants than technology, managing both life and work while becoming (for both better and worse) many people's closest relationships
  * **Loved Ones Monitoring** —Continuous monitoring of everyone you care about who can't monitor themselves (children, elderly parents, those with special needs), watching all cameras, security systems, and logs 24/7 for signs of danger or distress
  * **Continuous Advocate** —Works continuously, without rest, as an Advocate. Constantly scanning the world for opportunities, threats, better deals, useful information, and ways to optimize your life according to your goals
  * **Building Partner** —When you sit down at a computer, your Assistant has full access to everything the computer can do, can see all your screens, can hear everything. You can speak, type, and gesture, and have your DA do most of the work using all the power of the connected systems


  * **Environmental Customization** —Automatically adjusts environments you enter into such as lighting, temperature, music, displays, and ambient settings in any space you enter based on preferences, current mood, time of day, and what you're trying to accomplish
  * **Enhanced Perception** —Will grant superhuman-like senses through available feeds: seeing through walls via building cameras, hearing specific conversations across rooms by filtering audio, accessing available mics, zooming into distant objects, accessing thermal vision and other sensory augmentation


  * **Active Protection** —Rewrites abusive messages before you see them, summarizes manipulative communications to extract what's really being asked, removes extremist propaganda from feeds, fact-checks claims in real-time during conversations, performs live character analysis on people you're interacting with
  * **Universal Authentication** —Handles all authentication continuously through multi-factor streams (voice, gait, location, behavior patterns), automatically enrolling new devices into your ecosystem with proper security settings and managing permissions across all connected systems
  * **Deep Understanding** —Deep understanding of your full context and history as a person: your upbringing, your relationship with your parents and family, your education, your traumas (optional, of course), your journal, your goals, your aspirations, etc. All in service of better helping you become who you are trying to become


# Some vignettes [​](https://danielmiessler.com/blog/personal-ai-maturity-model#some-vignettes)
Sometimes the best way to tell is to show, so here are some examples of what it'll be like to use an AS3 level Assistant.
## Protecting You and Your Loved Ones [​](https://danielmiessler.com/blog/personal-ai-maturity-model#protecting-you-and-your-loved-ones)
  * **Your mom hasn't moved from her bedroom in three hours past wake time** —Your DA calls her, alerts the neighbor and emergency services with her location and medical history
  * **Walking at night, your DA monitors 47 nearby cameras and notices concerning behavior ahead** —"Take the next right, safer route, you'll still make it on time"


## Outsourcing Research [​](https://danielmiessler.com/blog/personal-ai-maturity-model#outsourcing-research)
  * **You mention wanting a new couch** —Six minutes later your DA interrupts: "Found the perfect one, your roommate loves it, on sale tomorrow at 4am for $1,100 less." You: "Order it." Your DA: "Done. Delivery Thursday between 2-4pm, I've already cleared your calendar."


## Detecting and Filtering Influence Campaigns [​](https://danielmiessler.com/blog/personal-ai-maturity-model#detecting-and-filtering-influence-campaigns)
  * **Propaganda campaign targeting your 16-year-old son, and marketing campaign trying to get you to dislike a certain product** —Your DA: "Heads up, there's a coordinated propaganda campaign targeting teens in your area. I've been filtering it from your son's feeds. Also detected astroturfing trying to tank Brand X's reputation. Want the analysis or just the cleaned feed?" You: "Just keep it clean." Your DA: "Done."


## Freelance Work [​](https://danielmiessler.com/blog/personal-ai-maturity-model#freelance-work)
  * **You do bug bounties on the side, and a new program just opened** —While you're eating dinner, Kai messages you: "New program just launched. I'm doing recon right now and already found something juicy. Just submitted the report. Team's response time is fast, so you might hear back before dessert."


## Monitoring Mental State and Energy [​](https://danielmiessler.com/blog/personal-ai-maturity-model#monitoring-mental-state-and-energy)
  * **You've been doing negative self-talk for the past hour, energy levels dropping** —Your DA notices the pattern and adjusts your lighting to warmer tones, starts playing your "getting unstuck" playlist. Then: "Hey, I've noticed you're being pretty hard on yourself today. You've actually shipped three major features this week. Want to take a walk? I can reschedule your 3pm."


## Routine Management and Optimization [​](https://danielmiessler.com/blog/personal-ai-maturity-model#routine-management-and-optimization)
  * **Your entire morning needs coordinating** —Optimal wake time, coffee started, news queued, 9am meeting moved to 10am, vitamins ordered, bills paid, 127 spam emails dismissed. Fifteen minutes in, zero decisions made


## Business Context [​](https://danielmiessler.com/blog/personal-ai-maturity-model#business-context)
### Career Growth (Employee) [​](https://danielmiessler.com/blog/personal-ai-maturity-model#career-growth-employee)
  * **You're heads-down on a project that isn't connected to your promotion goals** —Your DA: "Hey, you've spent 23 hours this week on the legacy migration, but it's not on your promo doc and your manager doesn't know about it. Meanwhile, the API redesign—your Q1 key result—hasn't moved in two weeks. Want me to draft a quick status update for Sarah showing the migration work, or should we carve out time tomorrow for the API project?"
  * **Quarterly business review coming up** —Your DA has been monitoring company OKRs, your team's goals, and your personal deliverables. "Your presentation is 80% done, but I noticed you're missing the cost-savings analysis leadership cares about. I pulled the numbers from last quarter and drafted a slide. Also, the CEO mentioned supply chain resilience three times in last week's all-hands—I added a section connecting your project to that theme. Review when you're ready."


### Team Leadership (Manager) [​](https://danielmiessler.com/blog/personal-ai-maturity-model#team-leadership-manager)
  * **You manage a team of eight and need to stay on top of everything** —Your DA monitors each team member's projects, blockers, and career goals. "Quick heads up: Marcus has been blocked on the vendor API for four days and hasn't escalated. Jenny's utilization is at 120% while Tom's at 60%—might want to rebalance. Also, your 1:1 with Priya is in an hour and she's been researching internal transfer policies. Might be worth asking how she's feeling about growth opportunities."
  * **Budget planning season** —Your DA: "I've mapped all current projects against your Q2 budget allocation. You're 15% over on contractor spend but 20% under on tooling. Three projects have no clear tie to the department's OKRs—want me to flag those for the prioritization meeting? Also, here's a one-pager showing how your team's work ladders up to the VP's top three priorities. Useful ammunition."


### Executive (Company Leadership) [​](https://danielmiessler.com/blog/personal-ai-maturity-model#executive-company-leadership)
  * **You're a VP responsible for a business unit** —Your DA maintains continuous awareness of company goals, team performance, project status, budget utilization, and competitive threats. "Board meeting prep: Revenue is tracking 8% ahead, but two key hires fell through and the roadmap is slipping. Your biggest risk right now is the enterprise deal with Acme—their CISO raised concerns about our SOC 2 timeline. I've drafted talking points and a mitigation plan. Also, competitor X just announced a feature that undercuts our Q3 launch. Want the analysis now or after your 10am?"
  * **Strategic planning and threat modeling** —Your DA: "Based on current spend patterns, market signals, and the threat model we built last quarter, here's what I'm seeing: 60% of security budget is on perimeter defense but our actual incidents are coming from supply chain and insider threats. I've drafted a reallocation proposal. Also, three of your five strategic initiatives are competing for the same engineering resources—someone's going to lose. Want me to model the trade-offs before Thursday's leadership sync?"


## Tactical vs. Strategic Goal Monitoring [​](https://danielmiessler.com/blog/personal-ai-maturity-model#tactical-vs-strategic-goal-monitoring)
  * **Quarterly review time** —Your DA: "We shipped 47 features and closed $280K in consulting this quarter, but we're off track on your 2026 goals. Your Q1 target was launching the AI Security Fundamentals course and signing three enterprise partnerships. We're at 12% course completion and zero partnerships. Here's the fix: transition Acme Corp and TechStart to Ryan as referrals, block Tuesdays/Thursdays for course recording starting next week, and I'll schedule intro calls with the four target companies from your January strategy doc—Microsoft, Google, Anthropic, and OpenAI."


The power of AS3-level Assistants comes from their combination of continuous awareness, proactive action, and deep understanding of your goals and context.
This shifts the relationship from tool to partner—one that actively works to make you safer, healthier, more focused on what matters, and more effective at becoming who you want to be.
# Summary [​](https://danielmiessler.com/blog/personal-ai-maturity-model#summary)
  1. There's nothing wrong with the various companies and builders stumbling randomly towards something that ends up looking like Digital Assistants. That's fun too. I just prefer knowing—at least roughly—where it's heading and where we are along the path.
  2. The idea that such a thing _is predictable at all_ is based on my belief/conjecture that tech (and the future more generally) are _not_ predictable, but _human desires are_. And that they're mostly stable over time. So if we know people consistently want more safety, more connection, more capability, etc...you can stochastically anticipate this is what will get built and selected for. From there I start with what an ultimate form of that might look like, and work backwards.
  3. Combining that with how modern AI has progressed since late 2022, I see the rough evolution of personal AI as: _Chatbots - > Agents -> Assistants_. Chatbots are basic call-and-response, leaving all the work to the user. [Agents](https://danielmiessler.com/blog/raid-ai-definitions#agents) are autonomous workers who can do tasks on their own. And Assistants are what we're actually building towards, i.e., competent companions that make us safer, healthier, happier, etc., and generally more effective at whatever we're trying to do in life and work.
  4. This model basically argues that 1) it is actually _possible_ to know (roughly) where we are going, and that 2) it's actually _useful_ to know this because it serves the purpose of [Sensemaking](https://en.wikipedia.org/wiki/Sensemaking). It gives order to the seemingly random, noisy tech developments along the way. And most importantly, for builders like us, it provides focus and direction on what to create next, and why.


I hope it's useful to you.
#### Notes
  1. I am 85% happy with Version 1.0 of this model, but there will most definitely be features/dimensions I will want to fix/add in the near future. I expect a v2.0 before July 2026, and maybe smaller releases before that. Please reach out with any comments of what you think I missed or can improve on. If I include them, I'll credit you here in the notes.
  2. Another thing to mention which I talked about in my [Predictable Path AI post](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024) is that all this capability is guaranteed to come with a wide range of downsides. There are too many to cover here, and I talk about them in the other post, but anything that's this powerful will be abused. First of all, a compromise of the system that controls this for someone will be catastrophic. They can be manipulated through it. Their friend/partner/DA can be deleted, altered, or erased in the way that Alzheimer's or death does. Then there are the possibilities of paying poorer people to install shims into their DAs that allow or push certain narratives and not others. And then there's the prospect of the government mandating access to the primary DA providers to monitor, inject, and otherwise control what's being seen by its principal. All this stuff is very possible and could happen. I focus on the positive because that's what I'm trying to build. But you can't be in security for nearly 30 years and not know that it can also go down this path.
  3. One aspect I've talked about elsewhere is that you may need [multiple DA roles](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024#_7-we-ll-have-additional-role-based-das-performing-specific-tasks-it-ll-be-a-collective-of-ais-managed-by-your-primary-da) because it will be weird to have your "best buddy" be your coach and your therapist and your doctor and your flirty partner at the same time, so those will likely be different DA personas, possibly/likely with your main DA as primary.
  4. I have a whole sister model to this for Corporate vs. Personal AI, which I've talked a bunch about in some of the posts linked below.
  5. Additional Reading: "[The Real Internet of Things](https://danielmiessler.com/blog/the-real-internet-of-things)." 2016. The original conception of Digital Assistants as the endpoint of personal AI.
  6. Additional Reading: "[AI's Predictable Path: 7 Components](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024)." 2023. The architectural framework underlying modern AI systems and how TELOS and Kai fit into the complete trajectory of AI development.
  7. Additional Reading: "[AI's Next Big Thing is Digital Assistants](https://danielmiessler.com/blog/ais-next-big-thing-is-digital-assistants)." 2023. More on the endpoint of this progression.
  8. Additional Reading: "[AI Agents, API Calling, and Prompt Injection](https://danielmiessler.com/blog/ai-agents-api-calling-prompt-injection)." 2023. Security considerations as we build these systems.
  9. Additional Reading: "[SPQA: AI Architecture Replacing Software](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software)." 2023. The underlying architecture pattern enabling this evolution.
  10. Additional Reading: "[RAID (Real World AI Definitions)](https://danielmiessler.com/blog/raid-ai-definitions)." 2024. Practical definitions of AI terms including Agents, AGI, ASI, and other key concepts.
  11. Additional Reading: "[Personal AIs Will Mediate Everything](https://danielmiessler.com/blog/personal-ais-will-mediate-everything)." 2024. Why personal AI assistants will become our primary interfaces to the digital world.
  12. Additional Reading: "[AI's Ultimate Use Case: Current to Desired State](https://danielmiessler.com/blog/ai-state-management)." 2025. More on the state management concept referenced in AS2.
  13. Credits: Thanks to [Jason Haddix](https://x.com/Jhaddix) and [Saša Zdjelar](https://linkedin.com/in/sasazdjelar) most of all for their constant support and feedback when I was writing the book in 2016, and for being an endless stream of ideas, discussion, and help up through today on these topics. And also to [Clint Gibler](https://www.linkedin.com/in/clintgibler/) for always being up for frequent phone calls and long walk discussions about this stuff. And to [Matt Johansen](https://x.com/mattjay) for a constant source of mutual ideas and encouragement.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fpersonal-ai-maturity-model&title=A%20Personal%20AI%20Maturity%20Model%20\(PAIMM\) "Share on Hacker News")
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
aifuturepersonal
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
