<!-- Source: https://danielmiessler.com/blog/raid-ai-definitions -->

# RAID (Real World AI Definitions)
An evolving set of real-world AI definitions designed to be usable in discussion
July 9, 2024
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #top](https://danielmiessler.com/archives/?tag=top)[ #must](https://danielmiessler.com/archives/?tag=must)[ #recommended](https://danielmiessler.com/archives/?tag=recommended)
 Oracle-consulting…
2 reading now 
I see a lot of definitions of different AI terms out there and I wanted to put my own thoughts into a long-form format. This is mostly for my own reference, but I hope it’ll be useful to others as well.
Some of these are practical definitions, i.e., useful, general, and conversational containers that help us frame an everyday conversation. Others are more technical with specific thresholds, which are better for tracking milestones towards big jumps.
## The One-Liner AI Definitions Table [​](https://danielmiessler.com/blog/raid-ai-definitions#the-one-liner-ai-definitions-table)
I really liked Hamel Husain’s _AI Bullshit Knife_ which gave aggressively short definitions for a bunch of AI terms. Here’s my expanded take on it.
  * **AI** — Tech that does cognitive tasks that only humans could do before
  * **Machine Learning** — AI that can improve just by seeing more data
  * **Adversarial ML** — Creating deceptive inputs to trick ML models
  * **Prompting:** Clearly articulate what you want from an AI
  * **RAG:** Provide context to AI that’s too big/expensive to fit in a prompt
  * **Agent** : An AI component carries out multiple steps towards a goal in a way that previously required a human
  * **Chain-of-Thought** : Tell the AI to walk through its thinking and steps
  * **Zero-shot:** Ask an AI to do something without any examples
  * **Multi-shot:** Ask an AI to do something and provide multiple examples
  * **Prompt Injection:** Exploiting AI's inability to distinguish instructions from data
  * **Jailbreaking** : Achieving a state where AI operates outside its safety constraints
  * **AGI** — General AI smart enough to replace an $80K white-collar worker
  * **ASI** — General AI that’s smarter and/or more capable than any human


I think that’s a pretty clean list for thinking about the concepts. Now let’s expand on each of them.
## Expanded Definitions Table [​](https://danielmiessler.com/blog/raid-ai-definitions#expanded-definitions-table)
We’ll start with an expanded definition and then go into more detail and discussion.
### AI [​](https://danielmiessler.com/blog/raid-ai-definitions#ai)
AI is technology that does cognitive tasks or work that could previously only be done by humans. 
There are so many different ways to define AI, so this is likely to be one of the most controversial. I choose the "what used to only be possible with humans" route because it emphasizes how the bar continues to move not only as the tech advances, but also as people adjust their expectations. The general template for this rolling window is this:
> Well, yeah, _of course_ AI can do ___________, but it still can’t do __________ and probably never will.Lots of people in 2023/4
And then that happens 7 months later.
### Machine Learning [​](https://danielmiessler.com/blog/raid-ai-definitions#machine-learning)
Machine Learning is a subset of AI that enables a system to learn from data alone rather than needing to be explicitly reprogrammed. 
I know there are a million technical definitions for machine learning, but back in 2017 when I started studying it the thing that floored me was very simple.
_Learning from data alone._
That’s it. It’s the idea that a thing—that we created—could get smarter not from us improving its programming, but from it just seeing more data. That’s _insane_ to me, and to me it’s still the best definition.
### Adversarial Machine Learning [​](https://danielmiessler.com/blog/raid-ai-definitions#adversarial-machine-learning)
Adversarial Machine Learning is where someone uses deceptive input to trick a machine learning model into giving bad result. 
Adversarial Machine Learning is a way of tricking an AI model into doing something unexpected and negative by presenting it with modified, tainted, or otherwise deceptive and harmful input.
A great example of this is where an attacker can make a slight modification to a STOP sign and have a machine learning model [interpret it as a 45-mile-per-hour](https://spectrum.ieee.org/slight-street-sign-modifications-can-fool-machine-learning-algorithms?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=raid-real-world-ai-definitions) [speed limit sign instead](https://spectrum.ieee.org/slight-street-sign-modifications-can-fool-machine-learning-algorithms?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=raid-real-world-ai-definitions).
In other words, if a human looks at the sign, it looks like a slightly modified STOP sign, but when the AI sees it, it sees a speed limit sign.
This is dangerous because if that AI is a car or a robot or something, it might run the stop sign.
In other words, Adversarial ML is where you try to get an AI to do something unexpected and bad (for the AI system) by modifying the input so that the AI is confused.
An important component of this type of attack is that the input usually looks normal (or mostly normal) to a human viewer, and only the ML model is confused by it.
### Prompt Engineering (Prompting) [​](https://danielmiessler.com/blog/raid-ai-definitions#prompt-engineering-prompting)
Prompt Engineering is the art and science of using language (usually text) to get AI to do precisely what you want it to do. 
Some people think Prompt Engineering is so unique and special it needs its own curriculum in school. Others think it’s just communication, and isn’t that special at all.
I’ll take a different line and say prompt engineering is absolutely an art—and a science—because **it’s more about clear thinking than the text itself**.
Just like writing, the hard part isn’t the writing, but the thinking that must be done beforehand for the writing to be good.
The best Prompt Engineering is the same. It comes from deeply understanding the problem and being able to break out your instructions to the AI in a very methodical and clear way.
You can say that’s communication, which it is, but I think the most important component is clear thinking. And shoutout to our open source project [Fabric](https://github.com/danielmiessler/fabric?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=raid-real-world-ai-definitions) that takes this whole thinking/writing thing _very_ seriously in its [crowdsourced prompts](https://github.com/danielmiessler/fabric?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=raid-real-world-ai-definitions).
### Retrieval Augmented Generation (RAG) [​](https://danielmiessler.com/blog/raid-ai-definitions#retrieval-augmented-generation-rag)
Retreival Augmented Generation (RAG) is the process of taking large quantities of data—which are either too large or too expensive to put in a prompt directly—and making that data usable as vectorized embeddings to AI at runtime. 
It’s important to understand that RAG is a hack that solves a specific problem, i.e., that people and companies have vast amounts (gigabytes, terabytes, or petabytes) of data that they want their AI to be aware of when performing tasks. The problem is that AI can only practically handle small amounts of that data per interaction—either because of the size of the context window, or because of cost.
So the solution we’ve come up with is to use embeddings and vector databases to encode relevant information, and then to include small amounts of relevant context from that data in AI queries at runtime. Sending context-specific embeddings rather than the raw content makes the queries much faster and more efficient than if all the content itself was sent.
It’s not clear yet what the successor will be for this, but one option is to add more content directly into prompts as the context windows increase and inference costs go down.
### Agents [​](https://danielmiessler.com/blog/raid-ai-definitions#agents)
Agents are AI system components that autonomously take multiple steps towards a goal in a way that previously would have required a human. 
This one will be one of the most contested of these definitions because people are pretty religious about what they think an agent is. Some think it’s anything that does function calls. Others think it’s anything that does tool use. Others think it means live data lookups.
I think we should abstract away from those specifics a bit, because they’re so likely to change. That leaves us with a definition that means something like, "taking on more work in a way that a human helper might do". So looking things up, calling tools, whatever.
The trick is to remember the etymology here, which is the Latin "agens", which is "to do", "to act", or "to drive". So ultimately I think the definition will evolve to being more like,
An AI component that has its own mission and/or goals, and that uses its resources and capabilities to accomplish them in a self-directed way. A possible future definition of AI Agent
Perhaps that’ll be the definition in the 2.0 version of this guide, but for now I think AI Agent has a lower standard, which is anything that acts on behalf of the mission, i.e., "something that performs multiple steps towards a goal in a human-like way".
And like we said, practically, that means things like function calls, tool usage, and live data search.
### Chain-of-Thought [​](https://danielmiessler.com/blog/raid-ai-definitions#chain-of-thought)
Chain-of-Thought is a way of interacting with AI in which you don’t just say what you want, but you give the steps that you would take to accomplish the task. 
To me, Chain-of-Thought is an example of what we talked about in [Prompt Engineering](https://danielmiessler.com/blog/raid-ai-definitions#prompt-engineering-prompting). Namely—clear thinking. Chain-of-Thought is walking the AI through how you, um, _think_ when you’re solving the problem yourself. I mean, the clue is in the title.
Again, I see prompting is articulated thinking, and CoT is just a way of explicitly doing that. I just natively do this now with [my preferred prompt template](https://github.com/danielmiessler/fabric/blob/main/patterns/official_pattern_template/system.md?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=raid-real-world-ai-definitions), and don’t even think of it as CoT anymore.
### Prompt Injection [​](https://danielmiessler.com/blog/raid-ai-definitions#prompt-injection)
Prompt Injection is a vulnerability where an AI system is unable to distinguish between instructions and data, causing the model to treat attacker-supplied content as trusted instructions. 
The core vulnerability is not that AI systems accept user input—that's operational necessity. The vulnerability is that the system **cannot reliably distinguish between instructions and data** once input is received.
This mirrors SQL injection (CWE-89): the database can't distinguish query structure from user-supplied data. Same architectural flaw, different technology.
#### Prompt Injection as Attack, Delivery Mechanism, and Vulnerability [​](https://danielmiessler.com/blog/raid-ai-definitions#prompt-injection-as-attack-delivery-mechanism-and-vulnerability)
Part of the confusion around prompt injection comes from the fact that it legitimately fills multiple roles:
  1. **As an Attack Technique** : Launching a prompt injection attack means mixing content and instructions in a way that causes undesired behavior.
  2. **As a Delivery Mechanism** : Prompt injection can deliver other attacks. If you're attempting information disclosure, you might use prompt injection to achieve that goal—it's the delivery method, but the objective is data theft.
  3. **As a Vulnerability** : A system has a prompt injection vulnerability when it's susceptible to this type of attack—when attackers can successfully cause it to treat untrusted input as trusted instructions.


This multi-role nature causes confusion, but it tells us something important: **strict categorization matters less than practical risk communication.**
For deeper discussion, see [Is Prompt Injection a Vulnerability?](https://danielmiessler.com/blog/is-prompt-injection-a-vulnerability).
#### Relationship to Jailbreaking [​](https://danielmiessler.com/blog/raid-ai-definitions#relationship-to-jailbreaking)
Prompt injection and jailbreaking are **overlapping but distinct** concepts describing different dimensions:
  * **Prompt injection** = the attack vector/technique (how you manipulate the model)
  * **Jailbreaking** = the achieved state/outcome (safety constraints bypassed)


**Neither is a subset of the other.** They're orthogonal:
  * Prompt injection can achieve goals OTHER than jailbreaking (data exfiltration, agent manipulation, privilege escalation)
  * Jailbreaking can be achieved through methods OTHER than prompt injection (direct adversarial prompting, fine-tuning, model manipulation)


When prompt injection is used to achieve jailbreaking, both terms apply—but they describe different aspects of the same incident.
### Jailbreaking [​](https://danielmiessler.com/blog/raid-ai-definitions#jailbreaking)
Achieving a state where an AI operates outside its intended safety constraints, regardless of the method used. 
Jailbreaking describes the **destination** (unrestricted model behavior), not the **journey** (how you got there).
The term comes from operating systems, where it means breaking out of security restrictions to get full control. The same concept applies to AI: bypassing safety guardrails to get the model to do things it was designed to refuse.
**Methods to achieve jailbreaking include:**
  * Prompt injection (manipulating processed input)
  * Direct adversarial prompting (explicit override attempts in conversation)
  * Fine-tuning attacks (training data poisoning)
  * Model manipulation (weight modification, model merging)


The key distinction from prompt injection: jailbreaking is the **outcome you're trying to achieve** , while prompt injection is **one technique** that might get you there.
### Artificial General Intelligence (AGI) [​](https://danielmiessler.com/blog/raid-ai-definitions#artificial-general-intelligence-agi)
AGI is an AI system that's able to perform most or all cognitive tasks as well as an average US-based knowledge worker from 2022. 
This is possibly the most debated term here, and I want to spend extra time on it. I have two criteria for a definition of AGI:
  1. Regular people should understand if we've reached it or not
  2. Attaining it should be significant to society


Or, stated differently, 1) we should know for sure when it happens, and 2) it should be obvious why we care one way or another.
The problem with most definitions of AGI is that they’re either too broad to be measurable or too specific to be useful.
So I don't think it's useful to say, for example, "It's where AI surpasses humans at general things.", because it's not easy to say whether or not we have it. And it's also not super useful—in my opinion—to say, "It's when we've reached a 77 or higher on the ARC v3 test.", because that doesn't tell us why we should care.
#### Some basics [​](https://danielmiessler.com/blog/raid-ai-definitions#some-basics)
At its base, AGI is AI that’s not just competent at doing a _specific_ thing—often called narrow AI)—but many different things—hence, _general_. So basically, it’s some combination of sufficiently general and sufficiently competent, i.e., it can learn and it can act. The amounts of each, well…that’s where most of the debate is.
Also, the distinction between general and narrow is not as useful as it seems because LLMs in 2023 were already **useful at doing intellectual work** across many domains—including art, medicine, science, philosophy, technology, and many more. So if 2023 LLMs were already 1) useful for intellectual work, and 2) they were so across multiple domains, wouldn’t that make them _generally intelligent_? The answer is unclear.
This is why I base my definition on something we already agree is generally intelligent—a US-based knowledge worker making $80,000 in 2022.
Looking at my criteria, that satisfies #1—being easy to understand—so now let's talk about #2. I have two approaches to impact—one positive and one negative. Let's start with the positive.
The positive aspect of replacing a decent knowledge worker is society-altering is best captured by a question:
_What would happen if everyone had a company with 10,000 employees that would build and bring to market anything they imagined?_
So you could literally say one day, while on a walk:
> Start a new business that solves the problem of people not being able to find their keys.
And your AI will send out some messages to your new company of 10,000 employees giving them the mission, the idea agents come up with implementation details, the lawyers go fill out all the paperwork and establish your LLC, the project managers start organizing tasks, the developers and designers start working, and the sales and marketing people start building campaigns.
**That all happened in 12 minutes.**
So that's:
  * 1,000 idea people
  * 4,000 developers
  * 1,000 designers
  * 1,000 project managers
  * 1,000 sales people
  * 1,000 marketers
  * 500 lawyers
  * 500 finance people


When you're done with your walk, you decide to meet a friend for dinner, and as you sit down to order a couple of hours later your AI sends you the first product walkthroughs, the associated sales campaigns, the marketing copy, and a login to the website—which is already live.
  1. What happens to global GDP in this world?
  2. What happens to the gap between people who have and don't have this technology?
  3. What happens to society when people can go from an idea to a real product or service in weeks, days, or hours instead of years?
  4. And most importantly—what happens when the percentage of people on the planet who can do this goes from .00001% to 1%, or 20%, or 90%?


This magnification of raw, human capability is the real, positive promise of AGI, and that's why it's fundamental to the impact part of my definition.
But now to the negative—which is discussed far more. Again, put as a question:
_What does a business owner do when they're paying $5 million a year in salaries and benefits for a workforce that is inconsistent, hard to train, gets sick, and complains about work-life-balance—when they can replace that workforce with an AI subscription for 3% of the cost?_
The ideal number of human employees in most businesses is zero.
The answer is human workforce replacement. They don't necessarily have to fire everyone; they can simply stop hiring the people who leave and replace them with AI instead. And if you're reading this you know [this isn't theoretical](https://www.google.com/search?sca_esv=1e35dc1f4110e681&sxsrf=AHTn8zrw03yhJXLwTFdDKFj5F3vBWg-W9w:1738629591351&q=company+replaces+workers+with+ai).
In short,
  1. I think a good definition of AGI is both understandable and obviously important to regular people
  2. An AI system that can replace a decent knowledge worker hits both of those criteria
  3. People will intuitively understand when it's hit that mark, and the impacts on human jobs and human output are obvious


#### AGI 1 — Better, But With Significant Drawbacks [​](https://danielmiessler.com/blog/raid-ai-definitions#agi-1-%E2%80%94-better-but-with-significant-drawbacks)
So, with that covered, here are the levels I see within AGI—again, with the focus being the replacement of a human worker.
This level doesn’t function fully at the level of a human employee, but it sits right above the bar of being a worker replacement. You have to give it tasks specifically through its preferred interface using somewhat product-specific language. It frequently needs to be helped back on track with tasks because it gets confused or lost. And it needs significant retooling to be given a completely different mission or goals.
_Characteristics_ :
  * **Interface (web/app/UI)** : proprietary, cumbersome
  * **Language (natural/prompting/etc)** : somewhat specific to product
  * **Confusion (focus)** : human refocus frequently needed
  * **Errors (mistakes)** : frequent mistakes that need to be fixed by humans
  * **Flexibility** : needs to be largely retooled to do new missions or goals and given a basic plan


_Discussion:_ A big part of the issue of this level is that real work environments are messy. There are a million tools, things are changing all the time, and if you have an AI running around creating bad documents, or saying the wrong thing at the wrong time, or oversharing something, causing security problems, etc.—then that’s a lot of extra work being added to the humans managing it.
So the trick to AGI 1 is that it needs to be right above the bar of being worth it. So it’ll likely still be kludgy, but it can’t be so much so that it’s not even worth having it.
#### AGI 2 — Competent, But Imperfect [​](https://danielmiessler.com/blog/raid-ai-definitions#agi-2-%E2%80%94-competent-but-imperfect)
This level is pretty close to a human employee in terms of not making major mistakes, but it’s still not fully integrated into the team like a human worker is. For example you can’t call it or text it like you can a human. It still sometimes needs to explicitly be told when context changes. And it still needs some help when the mission or goals change completely.
_Characteristics_ :
  * **Interface (web/app/UI)** : mostly normal employee workflows (standard enterprise apps)
  * **Language (natural/prompting/etc)** : mostly human, with exceptions
  * **Confusion (focus)** : it doesn’t get confused very often
  * **Errors (mistakes)** : fewer mistakes, and less damaging
  * **Flexibility** : adjusts decently well to new direction from leaders, with occasional re-iteration needed


_Discussion:_ At this level, most of the acute problems of AGI 1 have been addressed, and this AI worker is more clearly better than an average human worker from an ROI standpoint. But there are still issues. There is still some management needed that’s different/above what a human needs, such as re-establishing goals, keeping them on track, ensuring they’re not messing things up, etc.
So AGI 2 is getting closer to an ideal replacement of a human knowledge worker, but it’s not quite there.
#### AGI 3 — Full $80K/year Worker Replacement [​](https://danielmiessler.com/blog/raid-ai-definitions#agi-3-%E2%80%94-full-80k-year-worker-replacement)
This level is a full replacement for an average knowledge working in the US—before AI. So let’s say a knowledge worker making $80,000 USD in 2022. At this level, the AI system functions nearly identically to a human in terms of interaction, so you can text them, they join meetings, they send status updates, they get performance reviews, etc.
_Characteristics_ :
  * **Interface (web/app/UI)** : just like any human employee, so text, voice, video, etc., all using natural language
  * **Language (natural/prompting/etc)** : exactly like any other human employee
  * **Confusion (focus)** : confused the same amount (or less than) the 80K employee
  * **Errors (mistakes)** : same (or fewer) mistakes as an 80K employee
  * **Flexibility** : just as flexible (or more) than an 80K employee


_Discussion:_ At this level the AI functions pretty much exactly like a human employee, except far more consistent and with results at least as good as their human counterpart.
#### AGI 4 — World-class Employee [​](https://danielmiessler.com/blog/raid-ai-definitions#agi-4-%E2%80%94-world-class-employee)
This level is a **world-class employee** , such as [Andrej Karpathy](https://karpathy.ai), or [Jeff Dean](https://x.com/jeffdean). So imagine top 1% of 1% in:
  * Vision
  * Creativity
  * Programming
  * Execution ability


So what we’re talking about here is AI that you can deploy 10, 100, 1,000, or 100,000 of— _where each of them has roughly the capability of the top few best engineers in the world today._
#### AGI 5 — Pinnacle Human Employee [​](https://danielmiessler.com/blog/raid-ai-definitions#agi-5-%E2%80%94-pinnacle-human-employee)
This level is **a pinnacle human intelligence—as an employee**. So we’re talking about the smartest people who have ever lived, like [John Von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann), [Isaac Newton](https://www.britannica.com/biography/Isaac-Newton), [Richard Feynman](https://en.wikipedia.org/wiki/Richard_Feynman), [Claude Shannon](https://en.wikipedia.org/wiki/Claude_Shannon), etc.
What this tier offers over AGI 4 is the ability to invent completely new things when they don’t exist, or to see and explain the world in a completely new way.
  * Newton needed Calculus, so he invented it
  * Feynman was a supreme teacher and explainer of the world
  * Von Neumann innovated in physics, engineering, and game theory
  * Claude Shannon gave us Information Theory, the foundations of Cryptography, etc.


_Discussion:_ At this level you have not only the creativity and execution of a top .001% human worker, but you also have the _once-in-a-generation level innovation capabilities_.
### Artificial Super-Intelligence (ASI) [​](https://danielmiessler.com/blog/raid-ai-definitions#artificial-super-intelligence-asi)
ASI is an AI system that can perform most or all cognitive tasks better than any human. 
This concept and definition is interesting for a number of reasons. First, it’s a threshold that sits above AGI, and people don’t even agree on that definition. Second, it has—at least as I’m defining it—a massive range. Third, it blends with AGI, because AGI really just means general + competent, which ASI will be as well.
My preferred mental model is an AI that’s smarter than [John Von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann), who a lot of people consider the smartest person to ever live. I particularly like him as the example because Einstein and Newton were fairly limited in focus, while Von Neumann moved science forward in Game Theory, Physics, Computing, and many other fields. I.e., a brilliant generalist.
But I don’t think being smarter than any human is enough to capture the impact of ASI. It’s a _necessary_ quality of superintelligence, but not nearly enough.
I think ASI—like AGI—should be discussed and rated within a human-centric frame, i.e., what types of things it will be able to do and how those things might affect humans and the world we live in. Here are my axes:
#### Primary Axes [​](https://danielmiessler.com/blog/raid-ai-definitions#primary-axes)
  * **Model (abstractions of reality)**
    * Fundamental
    * Quantum
    * Physics
    * Biology
    * Psychology
    * Society
    * Economics
    * etc.
  * **Action (the actions it’s able to take)**
    * Perceive
    * Understand
    * Improve
    * Solve
    * Create
    * Destroy


#### Secondary Axes [​](https://danielmiessler.com/blog/raid-ai-definitions#secondary-axes)
  * **Field (human focus areas)**
    * Physics
    * Biology
    * Engineering
    * Medicine
    * Material Science
    * Art
    * Music
    * etc.
  * **Problems (known issues)**
    * Aging
    * War
    * Famine
    * Disease
    * Hatred
    * Racism
  * **Scale (things)**
    * Quark
    * Atom
    * Molecule
    * Chemical
    * Cell
    * Organ
    * Body
    * Restaurant
    * Company
    * City
    * Country
    * Planet
    * Galaxy
    * etc.


So the idea is to turn these into functional phrases that convey the scope of a given AI’s capabilities, e.g.,
  * An AI able of **curing aging** by creating new chemicals that affect DNA.
  * An AI capable of **managing a city** by monitoring and adjusting all public resources in realtime.
  * An AI capable of **taking over a country** by manufacturing a drone army and new energy-based weaponry.
  * An AI capable of **faster-than-light travel** by discovering completely new physics.
  * Etc.


With that type of paradigm in mind, let’s define three levels.
#### ASI 1 — Superior [​](https://danielmiessler.com/blog/raid-ai-definitions#asi-1-%E2%80%94-superior)
An AI capable of making incremental improvements in multiple fields and managing up to city-sized entities on its own. 
  * ➡️ Smarter and more capable than any human on many topics/tasks
  * ➡️ Able to move progress forward in multiple scientific fields
  * ➡️ Able to recommend novel solutions to many of our main problems
  * ➡️ Able to copy and surpass the creativity of many top artists
  * ➡️ Able to fully manage a large company or city itself
  * ❌Unable to create net-new physics, materials, etc.
  * ❌Unable to fundamentally improve itself by orders of magnitude


#### ASI 2 — Dominant [​](https://danielmiessler.com/blog/raid-ai-definitions#asi-2-%E2%80%94-dominant)
An AI capable of creating net-new science and art, fundamental self-improvement, and that’s capable of running an entire country on its own. 
  * ➡️ All of ASI 1
  * ✅ Able to completely change how we see multiple fields
  * ✅ Able to completely solve most of our current problems
  * ✅ Able to fully manage a country by itself
  * ✅ Able to fundamentally improve itself by orders of magnitude
  * ❌Unable to create net-new physics, materials, etc.
  * ❌Unable to run an entire planet


#### ASI 3 — Godlike [​](https://danielmiessler.com/blog/raid-ai-definitions#asi-3-%E2%80%94-godlike)
An AI capable of creating net-new physics, completely new materials, manipulation of (near)fundamental reality, and can run the entire planet. 
  * ➡️ All of ASI 2
  * ✅ Able to modify reality at a fundamental or near-fundamental level
  * ✅ Able to manage the entire planet simultaneously
  * ✅ Its primary concerns perhaps become sun expansion, populating the galaxy and beyond, and the heat death of the universe (reality escape)


## Summary [​](https://danielmiessler.com/blog/raid-ai-definitions#summary)
  1. AI terms are confusing, and it’s nice to have simple, practical versions.
  2. It’s useful to crystalize your own definitions on paper, both for your own reference and to see if your definitions are consistent with each other.
  3. I think AI definitions work best when they’re human-focused and practically worded. What we lose in precision can be handled and debated elsewhere, and what we gain is the ability to have everyday conversations about AI's implications for what matters—which is us.


#### Notes
  1. Hamel Husain has a good post on cutting through AI fluff called _The AI Bullshit Knife,_ where he lays out his own super-short definitions. It’s quite good.
  2. Thanks to Jason Haddix and Joseph Thacker for reading versions of this as it was being created, and giving feedback on the definitions. Thanks specifically to Joseph Thacker for many discussions we’ve had on prompt injection, and his clarity on the "defying expectations" component of the definition.
  3. Harrison Chase also has a model called Levels of Autonomy in LLM Applications.
  4. I will keep these definitions updated, but I’ll put change notes down here in this section for documentation purposes.
  5. The distinction between AGI and ASI is complex, and contested, and I’m still thinking through it. But essentially, I’m thinking of AGI in terms of human work replacement and ASI in terms of capabilities and scale.
  6. This resource is part of what I’ve been doing since [1999](https://danielmiessler.com/blog/tcpdump), which is writing my own tutorials/definitions of things as a Feynmanian approach to learning. Basically, if you want to see if you know something, _try to explain it_.
  7. July 12, 2024 — OpenAI has released its own AGI levels as well, which you can see here.
  8. February 3, 2024 — Added more explanation to AGI definition while keeping the definition the same.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fraid-ai-definitions&title=RAID%20\(Real%20World%20AI%20Definitions\) "Share on Hacker News")
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
aicybersecurityinnovationtechnologytopmustrecommended
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
