<!-- Source: https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong -->

# Business AI Is the Automation of Intelligence Tasks
AI is just a way to execute Intelligence Tasks that only humans can (could) do
July 30, 2024
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #business](https://danielmiessler.com/archives/?tag=business)[ #ethics](https://danielmiessler.com/archives/?tag=ethics)[ #future](https://danielmiessler.com/archives/?tag=future)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #productivity](https://danielmiessler.com/archives/?tag=productivity)[ #society](https://danielmiessler.com/archives/?tag=society)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #recommended](https://danielmiessler.com/archives/?tag=recommended)[ #top](https://danielmiessler.com/archives/?tag=top)
 Creator-economying…
2 reading now 
When I tell people that AI going to [separate people into have's and have-nots](https://danielmiessler.com/blog/ai-becoming-reading), or [multiply our global productivity](https://danielmiessler.com/blog/ai-becoming-reading) by trillions of dollars, most don't believe me.
I realize now why that is. It's because most people don't have the right **mental model** for thinking about AI.
Most chatbots are AI, but not all AI is chatbots.
When most people think AI they think image generation or chatbots. And understandably so—since those were the first applications of what's now called GenAI.
But it's much better to think of AI as an _Intelligence Pipeline_.
What the hell does that mean?
Great question. An _Intelligence Pipeline_ is a series of _Intelligence Tasks_ that result in a useful output. And _Intelligence Tasks_ are functions that can only be done using human intelligence.
Here are some real-world examples.
## Intelligence Pipeline Examples [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#intelligence-pipeline-examples)
Before we get into these, let's highlight the point by doing something crazy. **Let's completely abandon the word "AI"**. It's a silly word, and it means 100 different things depending on who you ask.
Instead I want you to think about _people_. Humans. And specifically, human workers.
So imagine a person—let's call them Chris—who works in a cube with a computer. Chris has a coffee next to him, and a small plant. And a picture of his girlfriend and his dog on the cube wall.
### Chris's job [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#chris-s-job)
Chris works at a company called _CutePup. CutePup finds pictures of cute dogs and puts them on the CutePup website._
Chis is a member of a Process Team that does one part of the company workflow. Here's the whole process.
  1. Take an uploaded picture and `determine if it's a dog`
  2. `Determine if the dog is cute`
  3. `Determine what kind of dog it is`
  4. Post all cute dogs on the website in the section for its breed


So the workflow looks like this:
The CutePup Workflow  
That's it. That's what CutePup does.
Chris is not alone in his building. He's in a cube farm with 48,912 other people.
Chris is part of the Process 1 team, so his job is to `determine whether a picture is a dog or not`. Here's what he sees on his screen all day:
That Chris lyfe  
This one is a cat, so Chris clicks on the No button.
### Chris's teammates [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#chris-s-teammates)
Carol sits next to Chris. She works in Process 2. She only gets photos that Process 1 has determined are dogs, and she has a screen that asks her if the dog is cute or not.
Carol has a better job  
Next to Carol is Amir who works in Process 3. Amir is an expert on dog breeds.
When a dog pops up, Amir looks at it and types in the breed into a text box.
You've got to know a lot of dogs  
## Why use humans and not just computer code? [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#why-use-humans-and-not-just-computer-code)
You might be wondering why we don't have computers do this.
Well, because they can't. You can't ask Python or C++ if something is a dog or not. Or if that dog is cute.
You need a human for that. You need Intelligence.
So, the CutePup workflow looks like this:
  1. Is it a dog?
  2. Is it cute?
  3. What kind is it?


That's three different tasks that require human intelligence. That's an _Intelligence Pipeline_ , and each node in the Pipeline is an _Intelligence Task_.
Let's look at more complex example.
## ClaimRight Insurance [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#claimright-insurance)
_ClaimRight_ is an insurance company that pays people out if their products wear out before they're supposed to. It's for all sorts of products, like scooters, tents, baby strollers, etc.
But they don't pay out if it's fraud or abuse of the product. Here's the workflow:
Checking for fraud and abuse of the product  
  1. Look at the 50 pictures of the item that are submitted as part of a claim
  2. Determine if the item is covered by ClaimRight
  3. Review the video of the submitter talking through the photos they took
  4. Determine if it's the same person who took out the policy based on their face and their voice
  5. Determine whether the item in the video is the same as the item in the photos
  6. Determine whether the damage in the photos is from normal wear-and-tear or from abuse
  7. If everything adds up, mark it as wear-and-tear and pay out the policy.


Kira works at ClaimRight, along with 349,219 other people in the Boise office. She has a plaque on her cube for 25 years of service. She's really good at determining the difference between wear-and-tear and abuse.
The big metrics for Intelligence Pipelines are accuracy and speed.
And she's not just good at it—she's fast. In her 8 hour day, not counting lunch and breaks and stuff, **she can get through an average of 29 cases per day!**
29!
That's 11 more than the median, and with an 89% accuracy rating, which is top 2% in the company.
Now let's look at something even more cognitively difficult.
## Overseer [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#overseer)
Kevin works at _Overseer_. They're a military intelligence service company that sells intelligence reports to the US government. They specialize in watching all the military bases in a foreign country using satellite images, and then determining what that country is doing militarily.
Here's the Pipeline.
Lots of analysis and expertise needed in multiple places  
  1. Look at the 28,452 satellite images that come in every day
  2. Compare the images to the previous day's images
  3. Identify everything in the new image
  4. Determine what changed since the last image
  5. Determine the military significance of those changes
  6. Construct a narrative around that significance, framed for a particular customer within the government
  7. Write the report
  8. Submit the report


Kevin is an employee at Overseer, and he's kind of a genius. Among the 712,309 people who work at his company (there are hundreds of satellites and hundreds of places of interest to monitor), he's one of the few who can work in Process 2, Process 3, and Process 5. Plus he's pretty good at 6 and 7. Most people can only do one or two.
Kevin is a star employee because he's super accurate at 86% and he can do 9 reports per week.
And like Carol at ClamRight, Kevin is super fast. He can actually do 9 reports per week! End-to-end if necessary. And his accuracy is off the charts at 86%.
Let's look at another example—this time in Medicine.
## Badspot checks for moles [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#badspot-checks-for-moles)
_BadSpot_ is a company that checks for dangerous moles on people. You send in the picture and it determines if it's something you need to worry about.
Here's the BadSpot Intelligence Pipeline.
Decades of schooling and experience required  
With _CutePup_ and _ClaimRight_ the stakes were pretty low. Maybe you get an occasional cat in your dog pics, or maybe the insurance policy pays out when it shouldn't have. No biggie.
But with _Overseer_ and _BadSpot_ , we're talking about military intelligence and health. So we're potentially dealing with people's lives.
The higher the stakes of the analysis outcome, the more the people doing that Intelligence Task must be intelligent, trained, and experienced.
And as you might expect, the level of expertise required is much higher. Think about the intelligence, knowledge, and experience needed to execute the Intelligence Tasks in these Pipelines:
### Overseer [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#overseer-1)
  * Know thousands of different military vehicles
  * Know the military history of the target country
  * Know all their recent military moves
  * Correlate that data with what's happening in the news
  * Correlate that with what's happening in other intel reports
  * Experience with analyzing satellite photos
  * Experience with detecting techniques that attempt to hide vehicles and military activity
  * Expertise in writing intel reports for different audiences


### BadSpot [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#badspot)
  * Anyone doing the job must be a Doctor (M.D.)
  * So that's medical school, a residency, and then however long they've been practicing
  * The better they are intelligence and creativity wise (think the TV Show, _House_), and the more experienced, the better they are at finding the Bad Spots.


One thing both of these Intelligence Pipelines have in common is that there aren't many people who can do the Intelligence Tasks involved. Like, there aren't many people who can do these things _on the planet_. We're talking a few a few thousand at most.
More on that later. First let's look at how common these types of Tasks and Pipelines are throughout society.
### More Intelligence Task and Pipeline Examples [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#more-intelligence-task-and-pipeline-examples)
As it turns out, [business is nothing but collections of these types of intelligence tasks and pipelines](https://danielmiessler.com/blog/companies-graph-of-algorithms).
Here are a bunch more _Intelligence Tasks_ we all recognize from the corporate world.
#### Office work [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#office-work)
  * `summarize_meeting`
  * `send_summary_to_stakeholders`
  * `read_report`
  * `proofread_document`
  * `create_meeting`
  * `organize_event`


#### Programming work [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#programming-work)
  * `solve_problem`
  * `write_code`
  * `research_better_way`
  * `check_for_security_issues`
  * `check_peers_code`
  * `approve_pr`


#### Customer Service work [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#customer-service-work)
  * `read_complaint`
  * `check_customer_history`
  * `check_for_fraud`
  * `check_current_policy`
  * `respond_to_customer`
  * `make_customer_happy`


#### Medical work [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#medical-work)
  * `analyze_mole`
  * `diagnose_disease`
  * `write_prescription`
  * `analyze_xray`
  * `assess_patient`
  * `analyze_mri`
  * `talk_with_family`


#### Researcher work [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#researcher-work)
  * `find_sources`
  * `rate_sources`
  * `summarize_article`
  * `rate_article`
  * `extract_key_ideas`
  * `synthesize_ideas`
  * `perform_analysis`
  * `write_report`
  * `submit_report`
  * `find_funding`


#### Manager work [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#manager-work)
  * `interview_candidate`
  * `give_performance_review`
  * `manage_budget`
  * `document_program_progress`
  * `write_progress_update`
  * `create_progress_update_presentation`
  * `deliver_presentation`


#### Creative Work [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#creative-work)
  * `brainstorm`
  * `riff_on_idea`
  * `expand_idea`
  * `write_first_draft`
  * `create_art`
  * `write_prose`


And the list goes on…
The thing that unifies all these tasks is that you can't give them to a computer program to execute.
These are things that only humans can do. These aren't just _work_ tasks, they're _Intelligence_ tasks.
## Similarities across tasks and pipelines [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#similarities-across-tasks-and-pipelines)
Now let's look at some similarities across all these tasks and pipelines.
Above we looked at four different companies: _CutePup_ , _ClaimRight_ , _Overseer, and BadSpot_ —all doing various thinking-based activities that require human intelligence. And then we looked above at a whole bunch more examples of intelligence-based tasks.
Now that we've talked about them, let's look at what makes someone good or bad at these things.
### Traits that make people good at intelligence-based tasks [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#traits-that-make-people-good-at-intelligence-based-tasks)
Here are some attributes that make great employees in knowledge work.
  * **Smarts** — how sharp are they at finding patterns and adjusting?
  * **Knowledge** — how much do they know about the field?
  * **Experience** — how many examples have they seen?
  * **Consistency** — do they deliver high-quality after 8 hours of doing it?
  * **Attention-to-detail** — do they catch the details?
  * **Speed** — How many of these tasks can they do in a period?
  * **Dependability** — do they call in sick or take lots of vacation?
  * **Autonomy** — How independent are they at doing the task?
  * **Trustworthiness** — are we sure they haven't been paid off?
  * **Caution** — do they cause problems we have to clean up?
  * **Learning** — do they learn new stuff quickly?


I think these are solid attributes. Now let's collapse them into a few metrics.
### ITEM — Intelligence Task Execution Metrics [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#item-%E2%80%94-intelligence-task-execution-metrics)
So the metrics concept we'll remember as **ITEM** (EYE-tehm), and the metrics themselves we'll remember as **KISAC** (KAI-sack).
  * 📘 **Knowledge** — The depth of their knowledge about the entire field, it's history, all the main thinkers in the field, all the seminal works, all the academic theory, all the reading, all the papers, etc.
  * 🧠 **Intelligence** — The ability to hold all that knowledge in their mind at once, find the patterns in the input being evaluated, and come up with insightful analysis.
  * 🕰️ **Speed** — The number of those tasks they can do—per minute, day, week, etc.—at a given quality level.
  * 🔎 **Accuracy** — Their accuracy, lack of mistakes, etc.
  * 💶 **Cost** — The amount of money it costs to hire them, keep them employed, and keep them trained.


These are decent because they capture not only someone's ability to do a task (knowledge and intelligence), but also the performance of their outputs (speed and accuracy), as well as the cost of execution.
## Coming back to AI [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#coming-back-to-ai)
Right, so that was a lot of setup, and now we're able to make the main point.
The best way to think about AI—especially as it relates to business, the economy, and productivity—is to realize that **AI is simply a way to execute all these various _Intelligence Tasks_ better, more consistently, and cheaper.**
Companies are just Intelligence Tasks organized into Pipelines  
That's it. Forget all the other crap about AI.
  * Forget the chatbots
  * Forget the image generation
  * Forget the crazy videos


**Those are distractions.**
What matters is how AI will help humans do actual work that otherwise humans would have had to do ourselves. And keep in mind—a lot of intelligence-heavy work isn't being done at all!
There are thousands of intelligence-based tasks that desperately need doing, but there simply aren't enough people to do them.
  * Watching all the meteors in the sky (Astronomy)
  * Tutoring (Education)
  * Medical Evals (Medicine)
  * Looking things up (Library Science)
  * Tracking transactions (Fraud & Corruption)
  * Investigations (Journalism)
  * Researching a Topic (Research)
  * Empathic and Active Listening (Mental Health)
  * Watching computer logs (Cybersecurity)
  * Watching security cameras (Physical Security)
  * Tracking down criminals and corruption (Journalism)
  * Etc.


There are literally billions of people who don't have access to teachers, tutors, therapists, nurses, researchers, journalists, etc., and all the wonderful _Intelligence Tasks_ that they are able to do.
Most Intelligence Tasks aren't even being done because there's nobody to do them.
The planet needs hundreds of billions of these _Intelligence Tasks_ done every day, and there are very, very few people with the education, training, certification, or availability to carry them out.
And that's just for the stuff that _nobody_ is doing. Now let's look at the work that's actually being done using the **KISAC** metrics above.
## Comparing humans vs. AI on Intelligence Tasks [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#comparing-humans-vs-ai-on-intelligence-tasks)
Here are the KISAC metrics again.
  * 📘 **Knowledge** — The depth of their knowledge about the entire field, it's history, all the main thinkers in the field, all the seminal works, all the academic theory, all the reading, all the papers, etc.
  * 🧠 **Intelligence** — The ability to hold all that knowledge in their mind at once, find the patterns in the input being evaluated, and come up with insightful analysis.
  * 🕰️ **Speed** — The number of those tasks they can do—per minute, day, week, etc.—at a given quality level.
  * 🔎 **Accuracy** — Their accuracy, lack of mistakes, etc.
  * 💶 **Cost** — The amount of money it costs to hire them, keep them employed, and keep them trained.


### 📘Knowledge [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#%F0%9F%93%98knowledge)
**👥Humans:**
  * 📚**Reading** : A couple thousand reading maximum
  * 💼**Experience** : Let's say 50 years
  * 🔬**Examples** : Let's say hundreds, thousands, or a tens of thousands max


**🤖AI:**
  * 📚**Reading** : All the reading in the entire field, with perfect recall, and millions of related reading
  * 💼**Experience** : The combined experience of every person who's ever done that task
  * 🔬**Examples** : Tens or hundreds of millions, or maybe billions depending on the task


### 🧠 Intelligence [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#%F0%9F%A7%A0-intelligence)
**👥Humans:**
  * Very few Einsteins or Von Neumann's in the world
  * Max I.Q. around 180 or so
  * Most people at around 100
  * Not rising very fast at all


**🤖AI:**
  * In 2022 it was less smart than a child
  * In 2024 it's currently around 100 I.Q., depending on the task
  * Many experts agree that top models will be genius-level within a few years
  * In narrow applications, current models are already super-human
  * It's improving _very_ quickly


### 🕰️ Speed [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#%F0%9F%95%B0%EF%B8%8F-speed)
**👥Humans:**
  * Checking Moles — A few hundred a day
  * Report Writing — 1 to 15 a month
  * Article Summarization — 5 to 20 a day
  * Cyber Investigations — 1 to 5 a week
  * Rating Cute Dog Pics — 200 - 2000 a day
  * Assessing X-Rays — 100 - 500 a day


**🤖AI:**
  * Checking Moles — Millions per day
  * Report Writing — Hundreds per day
  * Article Summarization — Thousands per day
  * Cyber Investigations — Dozens per day
  * Rating Cute Dog Pics — Hundreds of thousands per day
  * Assessing X-Rays — Hundreds of thousands per day


Keep in mind—this is just for a single AI instance, and most systems will have a fleet of them performing what a single human or a small human team was doing. So multiply those numbers by 10, 100, or 1000x.
### 🔬Accuracy [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#%F0%9F%94%ACaccuracy)
**👥Humans:**
  * Very high accuracy if the human goes extremely slow, depending on the person and the task
  * Medical errors are the third largest cause of death in the US. [SOURCE](https://www.ncbi.nlm.nih.gov/reading/NBK499956/)


**🤖AI:**
  * Some studies are already showing AI as equal to, or better than, doctors at identifying diseases, assessing moles, reading X-Rays, etc. [SOURCE](https://www.bbc.com/news/articles/ckdpg5p820xo)
  * Automation allows for faster use of multiple checks and validations to ensure acceptable results
  * AI's accuracy within a given pipeline is likely to increase over time due to the Knowledge and Intelligence advantage, whereas humans have a constant cycle of `get_smart —> retire —> retrain`


### 💶 Cost [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#%F0%9F%92%B6-cost)
**👥Humans:**
  * Expensive to train
  * Expensive to retrain
  * Expensive and time consuming to re-integrate into a team
  * Expensive to replace
  * Even more expensive for those with the best results


**🤖AI:**
  * Will cost a tiny fraction for most Intelligence Tasks
  * Will cost a tiny fraction for re-training and re-deployment
  * Upgrades to general models will often upgrade the entire fleet
  * The difference in cost between execution at mid-human level vs. high-human-level will likely be negligible


### Comparing vs. our examples [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#comparing-vs-our-examples)
Earlier we were talking about how fast and accurate Carol was at her job.
> And she's not just good at it—she's fast! In her 8 hour day, not counting lunch and breaks and stuff, **she can get through an average of 29 cases per day!**
> 29!
> That's 11 more than the median, and with an 89% accuracy rating, which is top 2% in the company.
Now imagine an AI doing this same job but with the following metrics:
_NOTE: These are just estimated numbers, but I think they're fairly realistic._
  * **29,000** a day instead of **29** (which will increase rapidly)
  * **93%** accuracy instead of **89%** (which will increase rapidly)
  * **$3,500** a year in AI costs instead of **$137,200** in salary & benefits (which will decrease rapidly)


In short, _humans will beat out AI in a few things for a long time to come_ —but for most _Intelligence Tasks_ , **AI is going to do 10-1000x the amount of work that humans can do—with as-good-or-better quality—for a fraction of the cost**.
And again, this is not some theoretical or ambiguous work. This is the work we're all familiar with. It's the regular work we get hired at companies to do.
Regular work that humans get hired to do every day  
**That** is what AI is. And **that** is why it matters.
## Summary [​](https://danielmiessler.com/blog/weve-been-thinking-about-ai-all-wrong#summary)
  1. People are confused about AI becasue they equate it with either chatbots or image generation.
  2. The best way to clarify your thinking on it is to remove the word "AI" from the conversation entirely.
  3. Replace the word "AI" with a unit of work that only humans can do, called an _Intelligence Task_.
  4. AI is getting extremely competent at executing such tasks, and it's doing so _faster, better, and cheaper_ every day.
  5. Companies are just sequences of those _Intelligence Tasks_ organized into _Intelligence Pipelines_ that accomplish a given goal.
  6. Which means companies and individuals that intelligently leverage AI will become dominant, while those that don't will get left behind.
  7. Meanwhile, the _Intelligence Pipelines_ that used to get executed by human workers will soon be mostly be executed by AI.
  8. **This** is why AI matters, and why it will have such an extraordinary impact on the economy and society.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fweve-been-thinking-about-ai-all-wrong&title=Business%20AI%20Is%20the%20Automation%20of%20Intelligence%20Tasks "Share on Hacker News")
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
aibusinessethicsfutureinnovationproductivitysocietytechnologyrecommendedtop
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
