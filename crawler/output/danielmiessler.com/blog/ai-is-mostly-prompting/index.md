<!-- Source: https://danielmiessler.com/blog/ai-is-mostly-prompting -->

# AI is Mostly Prompting
After 18 months of active AI development, 90% of the power is in prompting
May 6, 2024
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #creativity](https://danielmiessler.com/archives/?tag=creativity)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #productivity](https://danielmiessler.com/archives/?tag=productivity)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #writing](https://danielmiessler.com/archives/?tag=writing)[ #top](https://danielmiessler.com/archives/?tag=top)
 Rage-against-machining…
I’ve been actively building in AI since early 2023. I’ve put out the open-source framework called [Fabric](https://github.com/danielmiessler/fabric?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ai-is-mostly-prompting) > that augments humans using AI, and a new SaaS offering called [Threshold](https://threshold.app?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ai-is-mostly-prompting) > that only shows you top-tier content. 
**I could still turn out to be wrong—especially at longer time horizons—but my strong intuition is that prompting is the center mass of AI.**
Not RAG, not fine-tuning, and increasingly—not even the models.
Of course you can’t do anything _without_ the models, so they’re what makes it all possible, but I have always thought—and continue to think—that **large context windows and really good prompting is going to take us a very long way**. 
Here are my initial thoughts on why this is true.
## Prompting is clarity
Our open-source framework, Fabric, is a set of dated crowdsourced [AI use cases](https://github.com/danielmiessler/fabric/tree/main/patterns?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ai-is-mostly-prompting) > that solve regular human problems. Stuff like: 
  * Looking at legal contracts for gotchas
  * Instantly taking detailed notes on a long-form podcast
  * Finding hidden messages in content
  * Extracting ideas from reading
  * Analyzing academic papers
  * Creating TED talks from an idea
  * Analyzing prose using Steven Pinker’s style guide
  * Etc.


The current list of Fabric patterns (prompts)
The project’s secret is clarity in prompting.
We use Markdown for all prompts (which we call Patterns), and we stress the legibility and explicit articulation of instructions. 
The extract_wisdom Pattern
This way of doing things has been extraordinarily successful, and while I continue to follow all the RAG and fine-tuning progress, I am still getting the most benefit from: 
  * Improved Patterns, i.e., better clarity in the instructions
  * More Examples in the Pattern
  * Better Haystack Performance
  * Larger Context Windows


And yes—of course we also benefit from upgraded model intelligence (we support OpenAI, Anthropic, Ollama, and Groq), but those improvements are magnified most by improving the above. 
## Nothing compares to precise articulation of intent
What I keep finding—and I’m curious to hear other builders who disagree—is that nothing compares to being super clear in what you want. That means: 
  * Clear in the role of the model
  * Clear in the goals
  * Clear in the steps
  * Clear (and exhaustive) with the examples
  * Clear about output format


This is why I’m so excited about text right now. Like, plaintext.
I’ve always loved the command line, and text editors. And of course reading, and thinking, and writing. 
❝ 
All those people who focused on thinking clearly are being rewarded now with AI. 
But now with AI these things have turned into the ultimate superpower. Specifically: 
  1. Thinking extremely clearly about what the problem is
  2. Being able to explain that problem
  3. And being able to articulate exactly how to solve it


## Models improve with the quality of your prompting
What I love so much about this is how much good prompts benefit from model upgrades. 
With Fabric it’s so incredibly fun to take something like `find_hidden_message`, ([pattern](https://github.com/danielmiessler/fabric/blob/main/patterns/find_hidden_message/system.md?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ai-is-mostly-prompting) >) which is an extraordinarily difficult cognitive task, and running it on a long-form podcast with someone who’s shilling propaganda. 
❝ 
There’s never been a better time to be good at concise communication. 
The difference between GPT-4’s ability to pull out the covert messaging vs. Opus’s is vast. Opus does so much better! It’s like scary good, and with no changes to the prompt. 
I love the fact that all the work is in the clarity. Clarity of explanation becomes the primary currency. It’s the thing that matters most. 
## Ways I could be wrong
There’s a few ways that the power of prompting can significantly diminish over time. 
  1. If we ever get to a point where I can just point a model at a giant datastore of terabytes of data, and have it instantly consume that data and become smarter about it, that’ll be a massive upgrade 
  2. If the models get so good that they can automatically sense the **intention** of the prompt and write/execute it as it should have been, that would be a massive upgrade 
  3. If context windows don’t materially expand, or haystack performance doesn’t keep pace, that will hurt the power of prompting 
  4. If inference costs don’t continue to fall from GPU and other innovations, slamming more and more into prompts won’t scale with the size of the problems 


That being said, I am hoping (and anticipating) that:
  * Good prompting will still be primary even after we have [massive context outside the prompt](https://danielmiessler.com/blog/spqa-ai-architecture-replace-existing-software?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=ai-is-mostly-prompting&last_resource_guid=Post%3A6174d810-7be4-4e06-9d9b-a2402bf95d1d) >
  * Even if models can anticipate what we should have written, there will still be slack in the rope compared to clear initial articulation 
  * Context windows and haystack performance will likely continue to improve massively given how quickly we’ve gotten to this point 
  * Inference costs are likely to continue to fall for a long time


## Final thoughts
This whole thing I’ve written here is basically a well-informed intuition. 
A battle-informed intuition—but an intuition nonetheless.
Nobody knows for sure how things will change, and whether prompting will lose power because of any of the reasons above. 
But I continue to feel like most of the power of AI is in **the clarity of instructions**. And because of that, we have the opportunity to continue improving how we give those instructions—with lower costs, more examples, and larger context windows. 
I think this might continue to be the best paradigm for using AI for a while. 
Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-is-mostly-prompting&title=AI%20is%20Mostly%20Prompting "Share on Hacker News")
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
aicreativityinnovationproductivitytechnologywritingtop
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
