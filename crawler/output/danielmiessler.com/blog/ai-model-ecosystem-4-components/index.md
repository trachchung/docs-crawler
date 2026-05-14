<!-- Source: https://danielmiessler.com/blog/ai-model-ecosystem-4-components -->

# The 4 Components of Top AI Model Ecosystems
The four things I think will determine who wins the AI Model Wars
August 20, 2024
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #future](https://danielmiessler.com/archives/?tag=future)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #top](https://danielmiessler.com/archives/?tag=top)
 Context-engineering…
## Table of Contents
  * [The Model](https://danielmiessler.com/blog/ai-model-ecosystem-4-components#the-model) >
  * [Post-training](https://danielmiessler.com/blog/ai-model-ecosystem-4-components#posttraining) >
  * [Internal tooling](https://danielmiessler.com/blog/ai-model-ecosystem-4-components#internal-tooling) >
  * [Agents](https://danielmiessler.com/blog/ai-model-ecosystem-4-components#agents) >
  * [Analysis](https://danielmiessler.com/blog/ai-model-ecosystem-4-components#analysis) >
  * [Summary](https://danielmiessler.com/blog/ai-model-ecosystem-4-components#summary) >


I have been thinking a lot about the competition between OpenAI, Anthropic, Meta, and Google for who has the best pinnacle AI model. 
I think it comes down to 4 key areas.
  * The Model Itself
  * Post-training
  * Internal Tooling
  * Agent Functionality


Let’s look at each of these.
## The Model
The model is obviously one of the most important components because it it’s the base of everything. 
So here we’re talking about how big and powerful the base model is, e.g., the size of the neural net. This is a competition around training clusters, energy requirements, time requirements, etc. And each generation (e.g., GPT 3→4→5) it gets drastically more difficult to scale. 
So it’s largely a resources competition there, plus some smart engineering to use those resources as efficiently as possible. 
But a lot of people are figuring out now that it’s not just the model that matters. The post-training of the model is also super key. 
## Post-training
Post-training refines and shapes model knowledge to enhance its accuracy, relevance, and performance in real-world applications. 
**I think of it as a set of highly proprietary tricks that magnify the overall quality of the raw model. Another way to think of this is to say that it’s a way to connect model weights to human problems.**
I’ve come to believe that post-training is pivotal to the overall performance of a model, and that a company can potentially still dominate if they have a somewhat worse base model but do this better than others. 
I’ve been shouting from the rooftops for nearly two years that there is likely _massive slack in the rope_ , and that the stagnation we saw in 2023 and 2024 around model size will get massively leaped over by these tricks. 
**Post-training is perhaps the most powerful category of those tricks. It’s like teaching a giant alien brain** _**how to be smart**_**, when it had tremendous potential before but no direction.**
So the model itself might be powerful, but it’s unguided. So post-training teaches the model about the types of real-world things it will have to work on, and makes it better at solving them. 
So that’s the model and post-training, which are definitely the two most important pieces. But tooling matters as well. 
## Internal tooling
What we’re seeing in 2024 is that **the connective tissue around an AI model really matters**. It makes the models more _usable_. Here are some examples: 
  * High-quality APIs
  * Larger context sizes
  * Simple Fine Tuning
  * Haystack performance
  * Strict output control
  * External tooling functionality (functions, etc)
  * Trust/Safety features
  * Mobile apps
  * Prompt testing/evaluation frameworks
  * Voice mode on apps
  * OS integration
  * Integrations with things like Make, Zapier, n2n
  * Anthropic’s Caching mode


Just like with pre-training, these things aren’t as important as the model itself, but they matter because things are only useful to the extent that they can be used. 
So, Tooling is about the _integration_ of AI functionality into customer workflows. 
Next lets talk about Agents.
## Agents
Right now AI Agent functionality is mostly externally developed and integrated. There are projects like CrewAI, Autogen, Langchain, Langraph, etc., that do this with varying levels of success. 
But first—real quick—what is an agent?
❝ 
An AI agent is an AI component that interprets instructions and takes on more of the work in a total AI workflow than just LLM response, e.g., executing functions, performing data lookups, etc., before passing on results. 
Real-world AI Definitions 
So basically, an AI Agent is _something that emulates giving work to a human_ who can think, adjust to the input given, and intelligently do things for you as part of a workflow. 
**I think the future of Agent functionality is to have it deeply integrated into the models themselves. Not in the weights, but in the ecosystem overall.**
In other words, we soon won’t be writing code that creates an Agent in Langchain or something, which then calls a particular model and returns the results to the agent. 
**Instead, we’ll just send our actual goal to the model itself** , and the model will figure out what part needs agents to be spun up, using which tools (like search, planning, writing, etc.) and **it’ll just go do it and give you back the result when it’s done**. 
This is part of this entire ecosystem story. It’s taking pieces that are external right now (Agent Frameworks), and brings that internal to the native model ecosystem. 
## Analysis
Here’s how I see this playing out.
Models continue to get bigger and bigger, but you can only multiply by 10 so many times before we run out of GPUs and energy. After a number of years, gains in model power will have to come from efficiency gains, algorithm improvements, and other tricks. 
At some point, most of the gains will start coming from post-training, because that’s where we **harness and direct** the power of the models. It’s how effectively we’re explaining our problems to the model, and giving it ways of unlocking its intelligence to help us solve them. So gains there are multiplicative or exponential on top of the gains of model intelligence. 
Tooling will continue to make it easier and easier to use these AI ecosystems in daily life. From command-line to voice, and integrated into all of our various tools and workflows we use every day, e.g., email, calendar, reading, writing, etc. In short—it’ll just get easier to use these models wherever you are and whatever you’re doing. And it won’t require you to contort yourself in order to do so. 
And finally—and most significantly—**we’re going to move from using AI ourselves to giving tasks to AI Agents** —which will ultimately become integrated into [Digital Assistants](https://danielmiessler.com/blog/ai-predictable-path-7-components-2024?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=the-4-components-of-top-ai-model-ecosystems&_bhlid=1c85a10501c659154b58b488cb01622bd4e97796&last_resource_guid=Post%3Af6ebca7a-f24c-4738-b5a2-a00bc629ef4f) >. This is the big one, because individuals and [companies](https://danielmiessler.com/blog/companies-graph-of-algorithms?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=the-4-components-of-top-ai-model-ecosystems&_bhlid=b157c377be1952ca50b8b075e6d91d94ad9609ae&last_resource_guid=Post%3Af6ebca7a-f24c-4738-b5a2-a00bc629ef4f) > will then be able to spin up massive teams of agents [to do work for them](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=the-4-components-of-top-ai-model-ecosystems&_bhlid=417a44802cdd937208aa96fb36e46e846e3e8afb&last_resource_guid=Post%3Af6ebca7a-f24c-4738-b5a2-a00bc629ef4f) >—effectively multiplying their effectiveness many times over. 
## Summary
  1. We should start thinking about top AI models as **Model Ecosystems** rather than just models because it’s not just the neural nets doing the work. 
  2. There are four (4) main components to a Model Ecosystem—the Model itself, Post-training, Internal Tooling, and Agent functionality. 
  3. #1 (The model) is the most well-known piece, and it’s largely judged by its size (billions of parameters). 
  4. #2 (Post-training) is all about teaching that big model how to solve real-world problems. 
  5. #3 (Internal Tooling) is about making it easier to use a given model. 
  6. #4 (Agent functionality) emulates human intelligence, decision-making, and action as part of workflows—ultimately multiplying the capabilities of companies and individuals. 
  7. **The company that wins the AI Model Wars will need to excel at all four of these—not just building neural nets with the most parameters**. 


#### NOTES
  1. Thanks to Jai Patel for informing many thoughts on this, especially around pre-training. 
  2. Some additional, related reading:

> > > > > > >
We've Been Thinking About AI All Wrong
AI is just a way to execute Intelligence Tasks that only humans can (could) do 
danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong
> > > > > > >
Companies Are Just a Graph of Algorithms
AI is about to see your company as a series of components to be optimized 
danielmiessler.com/blog/companies-graph-of-algorithms
Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fai-model-ecosystem-4-components&title=The%204%20Components%20of%20Top%20AI%20Model%20Ecosystems "Share on Hacker News")
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
aifutureinnovationtechnologytop
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
