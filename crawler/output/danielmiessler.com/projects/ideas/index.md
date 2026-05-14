<!-- Source: https://danielmiessler.com/projects/ideas -->

# Projects
The projects I'm actively working on
This is where I keep track of my active endeavors. Nothing fancy, just a list with a quick overview and a link to learn more.
Just like with [/ideas](https://danielmiessler.com/ideas/) and [/predictions](https://danielmiessler.com/predictions/), the main purpose here is to ~~shame/prod~~ encourage others into making a similar page of their own.
## Current Focus [​](https://danielmiessler.com/projects/#current-focus)
I do lots of stuff, but I'm primarily building applications and backend AI infrastructure that helps enable Human 3.0. I also advise companies on how best to become antifragile against this whole AI thing.
Here's a short list of the ones I think are most important right now.  
| Name  | Stars  | Short Description  | Reference  |  
| --- | --- | --- | --- |  
| PAI  |   | An open-source framework for building personalized AI infrastructure  |  
| PAI on Pi  | —  | Model-agnostic PAI scaffold for local models and multi-provider use  |  
| Fabric  |   | An open-source repository of AI prompts for solving everyday work and life problems  |  
| SecLists  |   | The penetration tester's companion—passwords, fuzz strings, and security lists  |  
| Telos  |   | A concept and structure for managing context for things you care about  |  
| Ladder  |   | A system for autonomous creation and optimization  |  
| Substrate  |   | An open-source framework for human understanding, meaning, and progress  |  
| Daemon  |   | The API-ification system for people, objects, and organizations  |  
| Human 3.0  | —  | A framework for helping humans thrive in an AI-disrupted world  | [How My Projects Fit Together](https://danielmiessler.com/blog/how-my-projects-fit-together)  |  
| Unsupervised Learning  | —  | Newsletter + podcast on cybersecurity, AI, and society  |  [Subscribe](https://ul.live/sitenl) | [Podcast](https://ul.live/sitepod) | [YouTube](https://www.youtube.com/@unsupervised-learning)  |  
| Surface  | —  | AI-powered content intelligence — curated stories filtered by quality threshold  | [thesurface.ai](https://thesurface.ai)  |  
## Additional detail on the projects [​](https://danielmiessler.com/projects/#additional-detail-on-the-projects)
Some additional context about the various efforts.
### PAI (Personal AI Infrastructure) [​](https://danielmiessler.com/projects/#pai-personal-ai-infrastructure)
> This is the technical implementation layer for Human 3.0.
PAI is an open-source framework for building personalized AI systems that know your goals, learn from your history, and improve over time. It's fundamentally based on a universal pattern of moving from current state to desired state through verifiable iteration.
The repository provides modular "packs"—self-contained, AI-installable capability bundles—that allow you to augment generic AI agents (like Claude Code) with persistent memory, custom skills, intelligent routing, and context-aware functionality.
Rather than installing everything at once, you can incrementally adopt individual packs that solve specific problems, building a personalized infrastructure tailored to your workflows and goals.
→ [PAI on GitHub](https://github.com/danielmiessler/Personal_AI_Infrastructure)
### Human 3.0 (`H3`) [​](https://danielmiessler.com/projects/#human-3-0-h3)
> This is the umbrella project for many other projects below.
Human 3.0 is a framework for helping humans get ready for a world where AI has disrupted traditional corporate work.
It involves becoming an expressive, _full-spectrum_ human who is constantly learning, creating, and interacting with others.
→ [How All My Projects Fit Together](https://danielmiessler.com/blog/how-my-projects-fit-together)
### Telos [​](https://danielmiessler.com/projects/#telos)
> I was using documents like these in my consulting practice going back to 2009, but AI magnifies the power of the format exponentially.
Telos is a concept and structure for managing contextual information for things we care about, e.g., our personal lives, our family, an organization we're running, a team, a department, a company, or whatever.
The spiritual format for this is a single text document, known as a _Telos File_ , but the format isn't as important as the concept of clear, deliberate capture of the various components.
> The exact sections and how they're captured aren't as important as the exercise itself.
Key among those components are mission, goals, metrics, challenges, risks, ideas, team members, a journal, and many other sections.
→ [How All My Projects Fit Together](https://danielmiessler.com/blog/how-my-projects-fit-together)
### Surface [​](https://danielmiessler.com/projects/#surface)
> The evolution of Threshold — AI-powered content intelligence at scale.
Surface is an AI-powered content intelligence platform that curates and filters stories from thousands of high-quality sources. It rates content on quality, relevance, and novelty, allowing you to set a quality threshold so you only see what's actually worth your time.
Surface replaced Threshold with a more powerful architecture — broader source coverage, better AI filtering, and a cleaner interface for discovering what matters.
→ [thesurface.ai](https://thesurface.ai)
### Ladder [​](https://danielmiessler.com/projects/#ladder)
> This is the autonomous optimization layer for everything else.
Ladder is a system for autonomous creation and optimization — collecting ideas, forming hypotheses, running experiments, and applying results in a continuous loop. It structures the same process that has driven every major period of human innovation, from Renaissance salons to Bell Labs, and makes it executable by humans, AI agents, or both.
The pipeline flows: Sources → Ideas → Hypotheses → Experiments → Results, with results feeding back as new sources. This closed loop is what transforms a static collection of notes into an autonomous optimization engine.
→ [Ladder on GitHub](https://github.com/danielmiessler/Ladder)
→ [A Possible Path to ASI](https://danielmiessler.com/blog/path-to-asi)
### Substrate [​](https://danielmiessler.com/projects/#substrate)
Substrate is an open-source framework for human understanding, meaning, and progress.
What does that mean? The purpose of the project is to make the things that matter to humans _more transparent, discussable, and ultimately—fixable_.
→ [Introducting Substrate](https://danielmiessler.com/blog/introducing-substrate)
### Daemon [​](https://danielmiessler.com/projects/#daemon)
> This is the broadcast component of Human 3.0
Daemon is the API-ification system for people, objects, and organizations. It's the technology component that actually presents what an entity is about to the outside world.
Imagine a given Daemon having `/preferences`, `/ideas`, `/resume`, `/books`, etc., if it's for a person, and `/menu`, `/capacity`, and `/staff`, if it's for a restaurant.
→ [How All My Projects Fit Together](https://danielmiessler.com/blog/how-my-projects-fit-together)
### Beacon [​](https://danielmiessler.com/projects/#beacon)
> I could use help from some uber engineers on this one because it's crucial that the architecture is designed well.
This one I'm just starting, and am actively thinking through implementation options.
Beacon is essentially an application / interface for processing activity being broadcasted by someone. So imagine all the books they're reading, the movies they're enjoying, mentions about their new favorite coffee shop, or favorite coffee recipe, etc.
> All of this needs auth, of course.
It's essentially an activity feed for someone, which is automatically created as part of their _Daemon_ , that allows me to **subscribe** to them as a source of connection, inspiration, etc.
→ [How All My Projects Fit Together](https://danielmiessler.com/blog/how-my-projects-fit-together)
### Unsupervised Learning [​](https://danielmiessler.com/projects/#unsupervised-learning)
Since 2015 I've been running a newsletter about security, tech, and society. Today it's still focused on the same things, but with a major orientation towards Human 3.0 that we just talked about. Basically, _how to upgrade ourselves to be ready for whatever comes next._
→ [The YouTube Channel](https://www.youtube.com/@unsupervised-learning)
→ [The Newsletter](https://newsletter.danielmiessler.com/)
→ [The Podcast](https://podcasts.apple.com/us/podcast/unsupervised-learning/id1099711235)
The podcast gets thousands of downloads per week, the newsletter's at around 99,000 subscribers, and the YouTube channel is at over 600,000 subscribers.
### Fabric [​](https://danielmiessler.com/projects/#fabric)
Fabric was my answer to the AI situation in 2023, where there were a million different tools and million different prompts, with no easy way to manage them.
What we created is a crowd-sourced repository of prompts that help with everyday use cases for both work and personal.
Currently at stars with hundreds of prompts and contributors worldwide.
→ [Fabric](https://github.com/danielmiessler/fabric)
### SecLists [​](https://danielmiessler.com/projects/#seclists)
SecLists is a project I started with Jason Haddix back in 2012 as a Pentester's Toolkit. Today it's the most-used repository of passwords, fuzz strings, and other security-related lists in the world—currently at stars.
We were honored to have it included in the Kali Linux distribution, and it's been used by millions of security professionals worldwide.
→ [SecLists](https://github.com/danielmiessler/SecLists)
### Book: The Real Internet of Things [​](https://danielmiessler.com/projects/#book-the-real-internet-of-things)
> Here's an [updated, graphical version](https://danielmiessler.com/p/ai-predictable-path-7-components-2024) of the book.
I wrote a book in 2016 called [The Real Internet of Things](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler/dp/1545327122), where I laid out Digital Assistants powered by AI, how everything would get an API, how our DAs would become our proxies for interacting with the world, how our DAs would be our constant advocates, and many other concepts that are now starting to happen.
> The ideas are powerful, but I'm not really a fan of the book. Luckily it's a very short and fast read. More like a blog post really.
I deliberately wrote this book because I felt in my bones that these things were inevitable, and I wanted to capture them in time. I'm quite happy I did.
→ [The Real Internet of Things](https://www.amazon.com/Real-Internet-Things-Daniel-Miessler/dp/1545327122)
