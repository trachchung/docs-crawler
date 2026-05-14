<!-- Source: https://danielmiessler.com/blog/the-last-algorithm -->

# Pursuing the Algorithm
2026 might be the year continuous algorithm approaches start to generalize into universal problem solvers
January 17, 2026
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #future](https://danielmiessler.com/archives/?tag=future)[ #technology](https://danielmiessler.com/archives/?tag=technology)
 Root-causing…
2 reading now 
I just had a strange premonition that we're about to get ASI-like outcomes from AI in 2026, but not from a new model.
It'll be from loops.
And perhaps one loop in particular, which I sometimes call the Last Algorithm, or the Foundational Algorithm. Something cool. The algorithm deserves a cool word.
I feel like if we run into alien life as we explore the galaxy, and we say, "Well, it was ultimately THIS thing that got us here (TADA!)," they'll be like, "Yep, that's what everyone figured out..."
The [Ralph (Wiggum) loop](https://ghuntley.com/ralph/), created by [Geoffrey Huntley](https://ghuntley.com) is pointing at this.
I talked about it in February of 2025 in a post called [AI's Ultimate Use Case: Transition from Current State to Desired State](https://danielmiessler.com/blog/ai-state-management).
I've written dozens of posts pointing sharp sticks at the general idea, but I've always been extremely cautious about such things because they're serious shit. And there are thousands of people way smarter than me on this stuff, with way more specialized education on it as well, who aren't actively trying. So what am I going to do? Just stumble on it? Not likely.
But I'm not so sure anymore. I think the world might actually be weird enough that things like this slip through the cracks sometimes. And something that seems too easy or obvious could actually work if enough people tried it.
Anyway. I'm trying it. With full pre-acceptance that it could be absolute pseudo-science trash.
## Current loops are too small [​](https://danielmiessler.com/blog/the-last-algorithm#current-loops-are-too-small)
My issue with Ralph and similar loops is that they're—in my opinion—thinking way too small. By a lot. They're grinding on features. They're grinding on code.
My approach, which I have in early alpha in this [PAI](https://github.com/danielmiessler/PAI) skill, is to go much more general than that.
A general problem solver.
Yes, I know. Like I said above. I've read enough books to know that such things are 99% of the time complete ass. I've also read enough books, however, to know that most ideas that moved things forward initially looked like ass. I'm not sure which this is, but I think there's a [CIA Words of Estimative Probability](https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf), 50-75% chance that there's something here. (Chances About Even -> Probable)
And crucially, I think it can likely yield major fruit above current agentic harnesses even if I (or someone else) don't nail it. Here's the basic idea.
  1. Take a request
  2. Understand deeply what's being asked.
  3. Factor in everything you know about the requestor, and everything you know about the current state of the world that could be useful and that fits in working memory/context.
  4. Using this we establish the OUTER loop of The Algorithm, which is the IDEAL STATE of this request that was made. What would produce Euphoric Surprise in the requestor? That's IDEAL STATE.
  5. Then we start the INNER LOOP. The inner loop is basically the scientific method, but this early alpha version in the skill has 7 phases. OBSERVE, THINK, PLAN, BUILD, EXECUTE, VERIFY, LEARN. Then that merges back with OBSERVE basically.
  6. Depending on how much time, and how many resources you have, do extensive research to think about, red team, debate, hallucinate, daydream, genetically combine ideas, etc., to produce extensive granular criteria that make up and update the IDEAL STATE. This will include tons of criteria that are actually anti-criteria. Things to avoid.


So the whole purpose of this OBSERVE phase is to enhance the IDEAL state. To tighten it up. Expand it. Prune it. Blossom it. Manicure it. Nurture it. Etc. It's the most important thing in the world. And the hardest to get right. Especially at a granular level. Especially for GENERAL tasks. Any task.
Then you come up with experiments (THINK and PLAN) on how to build this thing, whatever it is. Or test whether it's true if it's an idea. You're basically making things granular and measurable so you can properly hill-climb.
Then you EXECUTE/RUN THE EXPERIMENTS, depending on the task time.
Then you VERIFY, and this part is kind of the most important part. You VERIFY against the IDEAL STATE.
The IDEAL STATE criteria are the VERIFICATION criteria.
If you don't produce Euphoric Surprise with the final judge, e.g., the USER, or reality, or whoever, that means you either had bad IDEAL STATE criteria or you somehow weren't able to VERIFY them properly. Or both.
So you LEARN and go back into the INNER LOOP.
You exit the INNER LOOP when you hit the happy half of the OUTER loop, which is you have achieved IDEAL STATE.
The Ralph Loop and similar projects are brilliant. But they are extremely tightly scoped to a very specific domain, at least in the current conversation.
The difference here is you can throw anything into The Algorithm.
  * I want to ethically hack a website
  * I want to get married to ______ type of person
  * I want to create AAA role-playing game
  * I want a nice website for my baking business
  * I want a system that helps me lose 20KG (really)


**CURRENT STATE - > IDEAL STATE**
Everything starts with proper capture of the IDEAL STATE. That is the key to generality. And this is what somehow feels tractable. Not perfectly, because there's no such thing. But good enough to exceed current methods of getting to Euphoric Surprise. Especially at scale for the trillions of nano and micro problems humans face daily.
## Karpathy nudged me on this too [​](https://danielmiessler.com/blog/the-last-algorithm#karpathy-nudged-me-on-this-too)
Another orthogonal inspiration for this came from [Andrej Karpathy](https://karpathy.medium.com/software-2-0-a64152b37c35).
He said like a year ago that Software 1.0 was about writing software. And Software 2.0 was about verifying software.
I think that influenced my current version of this idea a lot. It's like verifiability is the universal ladder. Or the universal system for hill-climbing. But why only software? That's my thing. Why only software. There's way more opportunity here.
So the trick is making things verifiable. General things. General goals.
Which requires that you have IDEAL STATE. The criteria for which are simultaneously your GOAL criteria and your VERIFICATION criteria.
## The prediction [​](https://danielmiessler.com/blog/the-last-algorithm#the-prediction)
So, just for fun, based on this intuition / hunch feeling I'm having right now, I am predicting that 2026 could be the year that continuous algorithm approaches start to generalize into universal problem solvers. Like my dumb one in PAI right now, but way better.
Again, they don't have to work perfectly. They only have to work a little bit. I think. And they'll still jump things way ahead of where they are now.
The world feels strange enough in this moment that a basic idea like this, being basement-hacked and iterated on by 100,000 hackers like you and me for a few months, could actually move the state of the art forward.
Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fthe-last-algorithm&title=Pursuing%20the%20Algorithm "Share on Hacker News")
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
aifuturetechnology
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
