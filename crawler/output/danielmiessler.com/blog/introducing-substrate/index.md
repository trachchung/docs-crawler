<!-- Source: https://danielmiessler.com/blog/introducing-substrate -->

# Introducing Substrate — An Open-source Framework for Human Understanding, Meaning, and Progress
Substrate is a crowdsourced project designed to enhance understanding, communication, and action in order to move humanity forward
July 16, 2024
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #business](https://danielmiessler.com/archives/?tag=business)[ #culture](https://danielmiessler.com/archives/?tag=culture)[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #ethics](https://danielmiessler.com/archives/?tag=ethics)[ #future](https://danielmiessler.com/archives/?tag=future)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #meaning](https://danielmiessler.com/archives/?tag=meaning)[ #politics](https://danielmiessler.com/archives/?tag=politics)[ #productivity](https://danielmiessler.com/archives/?tag=productivity)[ #science](https://danielmiessler.com/archives/?tag=science)[ #society](https://danielmiessler.com/archives/?tag=society)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #recommended](https://danielmiessler.com/archives/?tag=recommended)[ #top](https://danielmiessler.com/archives/?tag=top)
 Journaling-like-Marcus…
## Introduction [​](https://danielmiessler.com/blog/introducing-substrate#introduction)
I'm excited to share a project I've been working on for a number of months called _Substrate_. Fair warning: it's quite ambitious.
Ok, what is it exactly?
Substrate is an open-source framework for human understanding, meaning, and progress.
What the hell does that mean?
Yep, fantastic question. The purpose of the project is to **make the things that matter to humans more transparent, discussable** , **and ultimately—fixable.**
Interesting. What kinds of things?
Yes, exactly. Here are some of the main ones we're starting with.
## Substrate Components [​](https://danielmiessler.com/blog/introducing-substrate#substrate-components)
When we say "human understanding, meaning, and progress" in the description, we're talking about these types of conceptual objects:
  * **Ideas** — A list of novel human ideas
  * **Problems** — A list of our most important human problems
  * **Beliefs** — A list of beliefs about the world
  * **Models** — A list of models for conceptualizing reality
  * **Frames** — A list of narratives/lenses for perceiving reality
  * **Solutions** — A list of potential solutions to our problems
  * **Information Sources** — A list of sources of data and information
  * **People** — A list of humans
  * **Organizations** — A list of organizations
  * **Laws** — A list of laws that were proposed and/or passed
  * **Claims** — A list of truth claims
  * **Votes** — A list of votes and results from legislation/elections
  * **Arguments** — A list of arguments that have been made
  * **Funding Sources** — A list of groups that fund various projects
  * **Lobbyists** — A list of lobbyists and their agendas
  * **Missions** — A list of human ideas
  * **Donations** — A list of donations made from X to Y
  * **Goals** — A list of potential human goals
  * **Facts** — A list of verified truth claims


Each of these will be an actual list, maintained as a repository within Github. Each list will have a schema, similar to this one for the [Problems](https://github.com/human-substrate/Problems) repository:  
| Problem Name  | Problem ID  | Problem Description  |  
| --- | --- | --- |  
| Toxic Drinking Water in Poor US Towns  | PR-1097  | Many towns with populations with low socioeconomic status have water that's not safe to drink.  |  
| Deforestation of Our Rain Tropical Rain Forests  | PR-33082  | Our rainforests are being destroyed, which will negatively affect humans on Earth.  |  
GitHub - Substrate/Problems: The Problems people consider worth working on.  
And all of these live within an over-arching [Substrate Organization](https://github.com/human-substrate) within Github.
Substrate - An Open-source Framework for Human Understanding, Meaning, and Progress  
This structure will allow the entire open-source community (i.e., the world) to contribute their own _Problems, Claims, Sources, Frames, Goals_ , etc., that others can use.
Ok, I think I'm starting to get it, but I need more.
Fair enough.
One way to think about this is as **a way to put handles on things that are hard to discuss**.
Here are a couple of examples.
## Component Examples [​](https://danielmiessler.com/blog/introducing-substrate#component-examples)
Here are some more examples of Substrate Components in everyday scenarios. Let's look at an **Argument** component.
### An Argument [​](https://danielmiessler.com/blog/introducing-substrate#an-argument)
Think of a common argument we might hear on any given day about whatever topic. This one is about recycling.
> I don't know why you recycle, man. It's a total waste. It costs so much to recycle right now and the programs are poorly run, so it's not actually benefiting the environment. Like, I'd do it it it worked, but it doesn't. Some guy watching you put a can in a recycling bin
We're confronted by this type of thing constantly. About things like recycling, but also about things that matter much more, like politics.
What _Substrate_ will do is take an argument like this recycling example, and turn it into something like this:
A MermaidJS Visualization of this claim (Using Sonnet 3.5) Click for full size.  
Each of those objects in that diagram will be Substrate Components! The _Claims_ , the _Sources_ , etc.
Here's what the Arguments repository might look like:  
| Argument Name  | Argument ID  | Argument Description  |  
| --- | --- | --- |  
| Recycling Plastic Isn't Worth The Effort in the US  | AR-28445  | It'd be good to recycle plastic if it were actually worth the effort, but current systems are so inefficient that they cost more energy than they save.  |  
### A Source [​](https://danielmiessler.com/blog/introducing-substrate#a-source)
Examples of Organizational Sources  
When people make truth claims, it's important that we be able to fact-check or research those claims to see their support. Substrate does this by maintaining a list of Sources that we may or may not trust for new information, such as an _Organization_ , or a _Person_ (both of which are also Substrate Components).
When someone makes an _Argument_ , or a _Claim_ within an _Argument_ , it can be linked to _Sources_ that people can choose to trust or not trust.
**But either way, people can see the full argument and its support in one visual!**
An example of Argument → Claims → Sources  
This is why we're so excited about Substrate. It is going to make things that used to be murky and opaque into transparent objects that can be inspected, analyzed, and discussed.
**OLD** : "You're just not able to counter all my arguments and evidence."
**NEW** : "Here's my argument (throws it up on a shared viewscreen). Show me which claim you disagree with, or which source you disagree with that backs up those claims."
This will enable far more logical and precise discussions!
## Real-world Use Cases [​](https://danielmiessler.com/blog/introducing-substrate#real-world-use-cases)
> Ok, sounds really cool. But what do you actually *do* with it? Intrigued but practical
Yes, so now we're getting to the best part—how to actually use this thing!
First, keep in mind that this is very early. We're just getting started. But we already have many use cases planned that we want to talk about below.
Also, keep in mind that some of these you can do starting immediately, some will take time, and many of them will get magnified significantly by AI.
Let's take a look.
### Describing Yourself [​](https://danielmiessler.com/blog/introducing-substrate#describing-yourself)
Visualizing Your Being Using Substrate  
Many people have trouble describing who they are and what they're about.
With Substrate you'll soon be able to just describe yourself in text, audio, or video, **or even have a conversation with an AI** —and it will be able to both articulate and visualize you.
And if you [share your context or Substrate representation with others](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024), they'll be able to see what you're about as well.
### Learning a Person's Values [​](https://danielmiessler.com/blog/introducing-substrate#learning-a-person-s-values)
Substrate will be a wonderful way to start learning about someone, e.g., what they care about, and how they see the world.
Imagine having something like this available when you look at someone, or research them.
A Visual Conversation Starter  
This will be a wonderful way to learn about what someone really cares about, and how they see the world.
  * They believe the most important _Problems_ are PR-1097, PR-2210, and PR-2231
  * They believe the best _Solutions_ are SL-1128, SL-3110, and SL-1012 to those Problems.
  * They intend to track progress using the following _KPIs_.


Imagine matching up with someone like that across multiple axes:
  * Values
  * Goals
  * Beliefs
  * Preferences
  * Etc.


We're very excited about the potential to spawn more human connection in this way.
### Visualize Any Argument [​](https://danielmiessler.com/blog/introducing-substrate#visualize-any-argument)
Another great use will be when a given narrative, or rumor, or conspiracy theory is going viral. We'll be able to use Substrate to analyze the _Argument_ or _Claim_ and publish the results.
Here's an argument that we never went to the moon.
Click for Full Size  
Using this kind of visualization, you'll be able to see (for example) that:
  * They're making the following _Arguments_ that SL-19992 and SL-44091 are the best _Solutions_ : AR-7781, AR-9812, and AR-9992.
  * Which include the following _Claims_ : CL-1111, CL-2309, and CL-0002.
  * Which we fact-checked using the following _Sources_.
  * Which resulted in the following Results (Claim = False / True).
  * Which—using the following methodology—leads us to this _Conclusion_.


**Think Snopes, but as a graph that everyone can visually explore.**
What's amazing about this is that someone from any political background can now evaluate this with more transparency than has ever been possible. They can SEE the _Arguments_ , the _Claims_ , and the _Sources_ that were used to validate them, etc. _It's all right there_.
And, of course, people will be able to add all their favorite sources of ground truth, so they can make sure the Substrate visualization is trustworthy to them. At that point, the question just becomes which sources you trust, but you can then see how the logic and sources flow to the conclusion.
**I think this has the potential to significantly strengthen our shared understanding of reality, and will allow us to disagree with each other in a far healthier way.**
Here's one for the claim that there's a tiny teapot orbiting the sun.
These aren't using Substrate yet, but they will be soon, making each component of the argument community-sourced and transparent.
## Substrate + AI = Action [​](https://danielmiessler.com/blog/introducing-substrate#substrate-ai-action)
Yeah, yeah, yeah. AI this—AI that.
I hear you, but this is different. This isn't about AI. It's about human meaning and progress. AI is just a tool for helping that along.
Consider this about what you've heard so far about Substrate, and what's simultaneously happening with AI:
  * Context sizes (prompt sizes) are increasing
  * Inference costs (the cost to run AI) are plummeting


**What this means is we can _Chocolate-Peanutbutter_ Substrate with AI's ability to hold multiple things in its mind at once.**
So we can feed AI with our _Goals_ , _KPIs_ , _Risks_ , etc.—and have it help us untangle them and take action.
Here are some examples that we're most excited about.
### SCIENCE: Automated Hypothesis to Results Workflows [​](https://danielmiessler.com/blog/introducing-substrate#science-automated-hypothesis-to-results-workflows)
One big problem with science is that it takes so long. Look at the set of things that have to happen:
  * It's hard to come up with ideas.
  * It's hard to design experiments.
  * It's hard to find funding to do experiments.
  * It's hard to interpret results.
  * It's hard to publish results.
  * It's hard to get the results in front of the right people.


So now imagine we have our list of Problems, a list of Proposed Experiments, a list of Funding Sources, etc. They're all there.
Now AI can help us do most every step in that chain—completely automated!
  * Coming up with—or collecting—ideas and hypotheses
  * Designing experiments
  * Collecting and evaluating the best funding sources
  * Requesting funding by writing a perfect pitch
  * Helping set up the experiments (eventually with robotic help as well)
  * Running and monitoring the experiments
  * Interpreting results
  * Writing the paper
  * Sharing the paper


So in other words:
Hypothesis ➡️ Proposed Experiment ➡️ Look Up Funding Sources ➡️ Acquire Funding ➡️ Run Experiments ➡️ Publish Results ➡️ Make Progress
In the beginning, this will still require a lot of human help—especially at the idea and the running of the experiments phases. But over time AI will only become more useful in those areas, too.
**We're talking about _accelerating science!_**
### ACCOUNTABILITY: Monitoring Crime and Corruption [​](https://danielmiessler.com/blog/introducing-substrate#accountability-monitoring-crime-and-corruption)
It's easy to get away with corruption and crime because not enough people are watching for it.
Gangs, cartels, embezzlers, and dirty politicians leave evidence all over the place all the time. But small pieces. Scattered about. Across thousands of different locations and points in time.
It usually takes a major journalist team—or a massive law enforcement operation—to dump **thousands of hours** of highly skilled work to collect all the evidence. Then you have to do the analysis on it. Then you have to formulate the conclusions. And then you have to document it all.
Most crime and corruption slips by because nobody's watching. There aren't enough law enforcement groups. There aren't enough journalist teams. There aren't enough people with the skills to do this stuff—let alone the resources to support them doing it.
#### Substrate + AI vs. Dirty Politician [​](https://danielmiessler.com/blog/introducing-substrate#substrate-ai-vs-dirty-politician)
But now let's take Substrate with some AI added on, and let's think about a dirty politician who is taking massive gifts from a particular lobbyist, which is clearly affecting their votes.
The problem is—there are so many donations. There are so many lobbyists. There are so many representatives. There are so many bills. And so many votes.
But guess what? It's all public. The legislation is public. The lobbyist groups must register themselves. The donations they make are public. Records of meetings with representatives are public. And so are the votes.
So a non-profit could use AI to collect all these things—continuously—and save them in Substrate for everyone to inspect. And then a separate AI could do the work of the journalists.
  * Here are all the bills written by this representative.
  * Here are the summaries of those bills.
  * Here's who those bills helped and hurt.
  * Here are all the lobbyists that care about those issues.
  * Here are all the donations to that representative's campaigns.
  * Here's how the representative voted on every single bill.


Then you can instruct the AI:
> Ok, perform a comprehensive analysis of all legislation created and voted on from Bill Meyers, senator from Arkansas, cross-referenced with every single donation ever made to him, every dinner he's attended with them, every gift he's received, etc. 
> Finally, give me your assessment of whether he is being unduly influenced by this lobbyist, and give your reasons for your conclusion. You instructing the Substrate AI system
And then it can come back with something like:
Assessment: This is a compromised politician.
Reasoning:
  1. OSINT reveals that he was illegally gifted a small yacht last year, which he tweeted about and later deleted.
  2. He's had 31 dinners in the last 18 months with them, totalling over $14,800.
  3. OSINT reveals that the lobbyist's president used considerable influence to get Bill Meyers' daughter admitted to an exclusive private school she wasn't qualified for.
  4. Every vote he's made about this issue has been in the direction that the lobbyist wanted.
  5. Previous votes about this same topic, before this relationship was formed, went in the opposite direction 7 out of 8 times.


In short, the incredibly important objects of _Legislation_ , _Votes_ , etc. are all things that can monitored using AI and stored within Substrate.
### LEADERSHIP: Describing A Comprehensive Plan [​](https://danielmiessler.com/blog/introducing-substrate#leadership-describing-a-comprehensive-plan)
A visual representation of a political platform (Click for Full Size)  
Many leaders struggle with clarity. It's hard to know what they think the issues are, what they _specifically_ plan on doing, and how they plan to measure progress.
_We see this with both business leaders and politicians._
So with Substrate, we intend to make it so that every leader will need to have a full, detailed plan that has the following components:
  * Here's what I think the _Problems_ are
  * Here's what I think the _Solutions_ are
  * Here are my proposed _Strategies_ for accomplishing that
  * Here are the _KPIs_ we'll use to track progress
  * Fire me if I don't get the _KPIs_ to _________ by ___________ date.


Imagine having that level of **clarity and accountability** for any leader trying to get a job, doing _anything_.
### IMPROVEMENT: Optimizing Any Process [​](https://danielmiessler.com/blog/introducing-substrate#improvement-optimizing-any-process)
Ok, I saved the best one for last. This is the one that I'm personally most excited about.
From Companies Are Just Graphs of Algorithms  
In a recent piece, I talked about how [_Companies Are Just Graphs of Algorithms_](https://danielmiessler.com/blog/companies-graph-of-algorithms). True, but I don't think I went far enough with it.
_Everything can be conceptualized in this way—as a process._
  * State of things
  * Action / Event
  * Result = New State of Things


And if we add human components in there, like peoples' jobs, or making decisions—like we do for like running a business, or a country, or a family, we have additional pieces:
  * People
  * Decisions
  * Strategies
  * Lessons-learned
  * Conclusions
  * Reasons
  * Etc.


And what that results in is a way to tie this all together into much larger graphs. Graphs we can use to describe the operations of a Family, or a Company, or even a Country.
Here's one for a small company:
A Company Process Flow (Click for Full Screen)  
That's pretty cool that we can create that, but that's not the full power of Substrate combined with AI.
**The smarter AI gets, the better it will get at optimizing flows of any kind.**
In other words, this is just the current state. We can now ask AI what it would do to optimize this.
  * Should this company merge departments?
  * Where can we add more people?
  * Which processes here are inefficient?
  * Which can be replaced by AI?
  * Where could we use more human decision-making?
  * If we wanted to grow, where should that happen?


Now imagine this for:
  * A family
  * A corporation
  * A church
  * A city
  * A county
  * Etc.


And keep in mind, the more data you have here the better. You can feed such a system all the various efficiency metrics for the various pieces as well.
#### A security team analysis example [​](https://danielmiessler.com/blog/introducing-substrate#a-security-team-analysis-example)
  * It currently takes 3.5 business days to complete a security assessment
  * "Delays in Security Assessment Turnaround" are the #1 complaint in the Engineering survey
  * If we switch to the new FlexScan model using fewer generalist security testers, we'll be able to complete Type B and C assessments 94% faster.
  * This will give our senior testers 2 extra days to do high-impact assessments
  * This will also likely make Engineering much happier with Security, and make them more likely to cooperate on our goals.


So this is really multiple steps here:
  1. The full articulation and breakdown of how a process is currently running
  2. Visualization of that process to help with human understanding
  3. AI analysis of how to optimize the process to optimize the stated goals of the entity


And remember—the AI will also have access to the mission of the organization as well. And its goals. And its strategies. And its team members. And their projects. Etc.
So it will have the full context on how resources are being spent relative to the desired outcomes, and it will be able to see how the actual KPIs are moving.
From there it will be able to make all sorts of recommendations, such as:
  * Hiring new people
  * Hiring people with certain skills
  * Using more AI in high volume and low creativity areas
  * Adjusting strategies based on goals and market conditions
  * Cancelling projects X and Y to work on Z instead because it's more aligned with the goals
  * Etc.


**Ultimately we're talking about the ability to continuously analyze and optimize any system using full knowledge of its goals and progress.**
And the more data about the system it has, the better it'll perform. And the smarter AI gets, the better it'll perform.
Insane.
## Summary [​](https://danielmiessler.com/blog/introducing-substrate#summary)
Ok, that was a lot.
Here are the main points.
  1. The world is hard to understand, and **things that are hard to understand are hard to discuss and improve**.
  2. The goal of Substrate is to address this problem by making the things humans care about more visible, discussable, and improvable.
  3. The framework is open-source and lives on GitHub.
  4. At its core, it's a collection of crowdsourced lists of the things humans care about, and that make up our discourse and society.
  5. One major problem that people and organizations have is not knowing—and/or being able to communicate—what they are about.
  6. Using the framework, people and organizations will be able to articulate their values and purpose more clearly, which will help not only them but everyone they interact with.
  7. Substrate is magnified by AI because AI can—or will soon be able to—hold all of Substrate in its mind at once.
  8. From there, we'll be able to ask all sorts of meaningful questions, such as, "What is that person or organization about?", "Are we pursuing the best path towards our goals?", or, "What are the most critical mistakes I'm currently making?"
  9. Ultimately _this will allow us to take action on these things_., e.g., "What actions should I take right now to optimize this workflow?", or, "What should I do right now to achieve the best possible outcome that's aligned with my goals?"
  10. In short, **Substrate is a way to better understand and optimize the things we care about as humans**.


## How to Get Involved [​](https://danielmiessler.com/blog/introducing-substrate#how-to-get-involved)
Here are some of my friends and colleagues who have already signed on to help with this project.
  * Jonathan Dunn — MD, Hacker
  * Jason Haddix — Cybersecurity Expert, Hacker, Trainer
  * Clint Gibler — Cybersecurity Expert, Hacker
  * Joseph Thacker — Cybersecurity Expert, Hacker
  * Joel Parish — Cybersecurity Expert, Hacker
  * Robert Hansen — Cybersecurity Expert, Hacker


If you are interested in contributing, you can do so through [the Github projects themselves](https://github.com/human-substrate), or you can connect with us directly.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fintroducing-substrate&title=Introducing%20Substrate%20%E2%80%94%20An%20Open-source%20Framework%20for%20Human%20Understanding%2C%20Meaning%2C%20and%20Progress "Share on Hacker News")
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
aibusinessculturecybersecurityethicsfutureinnovationmeaningpoliticsproductivitysciencesocietytechnologyrecommendedtop
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
