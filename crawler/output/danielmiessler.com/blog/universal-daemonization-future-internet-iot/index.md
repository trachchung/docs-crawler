<!-- Source: https://danielmiessler.com/blog/universal-daemonization-future-internet-iot -->

# Universal Deamonization is the Future of the Internet and the Internet of Things
February 19, 2015
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #business](https://danielmiessler.com/archives/?tag=business)[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #ethics](https://danielmiessler.com/archives/?tag=ethics)[ #future](https://danielmiessler.com/archives/?tag=future)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #society](https://danielmiessler.com/archives/?tag=society)[ #technology](https://danielmiessler.com/archives/?tag=technology)
 RLHF-aligning…
1 reading now 
This piece is going to describe the future of the Internet and the Internet of Things. This isn't just a potential future—it's a virtual inevitability. Not many have heard it. You'll be one of the first.
The concept is called Universal Daemonization, and I've been writing and presenting on the topic for about a year now.
## Concepts [​](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#concepts)
Universal Daemonization, at its core, is a new way in which humans and other types of objects will interact with the world. Here are the primary concepts and components:
  * Both humans and objects will broadcast daemons around themselves, complete with hundreds of pieces of information about them. Imagine an aggregate of every profile ever completed, only being dynamically updated by interaction with the world
  * These daemons will sit on top of a modified version of a standard tech stack, i.e., TCP/IP, HTTP, REST-based web services
  * Both humans and objects will have Intention Brokers (IBs) that parse the daemons around them and take actions on their behalf
  * For humans this will come in the form of Personal Assistants like Siri, Google Now, and Cortana, which will parse the daemons around them and do things like update their preferences, submit food orders, send social pokes to people nearby with similar interests, and requesting more information about products of interest


  * For objects and machines the Intention Brokers will interact with the world in prescribed ways that pertain to its function. Parking meters will photograph cars parked in its spot, submit license plates, report tampering, etc., and bar surfaces will monitor how many drinks are on it, how many people are sitting in front of it, and ask lonely patrons how they're doing if they're alone (and their daemon says they're willing to chat)
  * People will be tied into the world through the connection between their daemons and a universal authentication framework. This will allow your Personal Assistant, or you directly, to make requests of the environment using the appropriate level of authorization that you have to do so
  * So, a regular citizen could be inside a club and say, "Take a picture of the dance floor from overhead.", and his personal assistant would do that by finding the API for the camera listed as above the dancefloor and submitting a POST request to it
  * Similarly, a police officer could approach a crime scene and tell her personal assistant, "Retrieve all video of this location for the last 2 hours.", and that video would be sent to her viewer and the police department from the surrounding 27 city cameras on light poles, parking meters, trees, and even authorized citizen cameras
  * This will mean continuous customization of your environment based on where you are. When you enter a restaurant your PA will read the restaurant's daemon, tell you all the specials, tell you who your waiter is (if you still have one), and then order for you if you want your go-to meal. It'll arrive with extra ketchup, because that's how you liked it
  * All this was possible because the restaurant had a REST API that your PA submitted to on your behalf. It crawled the API, found the food you want, and customized it according to your preferences. This was on the drive over, or as you walked up to the building, and when you are done you just walk away because you paid beforehand without doing anything
  * Machines will interact with each other in this way as well, GETTING and POSTING to APIs on a continuous basis, learning about the world around them, and sending updates, providing value, and doing what it was they were built for
  * This will enable a whole new type of [live dashboard](https://www.youtube.com/watch?v=TioYIJhdaKo) for any level of a household or business. Analytics engines will pull information and make requests to required services at various intervals in order to provide real-time views of every aspect of life
  * The living room wall in a family will be transformable into a real-time display of the entire family's fitness, diet, blood work, grades in school, heartrate, daily purchase history, summary of voice and text messages used, social interaction tree, college fund savings goals, current home value based on who moved in on the block today, and current retirement fund performance—all updated to the minute
  * And the same will be possible for businesses. Employee health stats, attendance, safety incidents, delays in shipments, air quality in the main worker areas, current company trading price, employee morale based on social media analysis, money lost in health insurance based on the physical health of employees, etc.—all updated to the second and displayed for any executive who asks


Everything will be broadcasting data and providing services to certain people, and the data pulled will be displayed in powerful ways to better enable decision makers (which will increasingly be machines/daemons themselves).
People and objects will be in a constant state of interaction with the world. Personal Assistants / Identity Brokers will be continuously sending GET and POST requests to surrounding human/object APIs, using their identity's token as authorization. And basic, nearly imperceptible actions by a human, such as a shiver, will be responded to by our PAs by a POST request to the nearest climate API for a temperature increase.
Desires—even those you didn't know you had or don't remember conveying—will become silent commands to the environment to conform to your preferences. And everyone and everything will be doing this… _all the time_.
That's Universal Daemonization.
## Technologies closer than they may appear [​](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#technologies-closer-than-they-may-appear)
What's fascinating about this is how tangible it is given existing technology. We have the protocols and tech stacks. All we need is someone to realize how close we are and how much money can be made from it.
And while the technology is remarkably within reach, it's application in this way will be highly emergent in nature. The social implications will be particularly significant, as who you are—and the privileges you enjoy—will exponentially magnify what you have access to.
Doors will literally open in front of some people as they walk, while for others they will remain forever closed. And your PA will whisper ratings of peoples' quality/usefulness as they approach you from afar.
Of course, big changes require big money, but to find sponsors we need look no further than governments and advertisers.
Governments will _invent_ budgets once they realize the monitoring and tracking power of centralized and continuous identity broadcast, and it'll all happen quickly under the Jedi-hand-gesture of "security".
To accelerate things even further, the advertising industry will dump untold billions the moment they realize the staggering potential to hyperfocus their spend on those most likely to purchase.
It's simply too logical, too obvious, and has too much potential to be stopped.
## Summary [​](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#summary)
  1. Humans and objects will broadcast daemons around them, advertising their attributes and interaction capabilities
  2. The daemons will sit on a TCP/IP, HTTP, and REST Web Services stack
  3. Intention Brokers will interact with surrounding daemons on the behalf of their human/object owners
  4. All interactions, whether automated or manual, will leverage a federated identity infrastructure that determines who can do what to various objects
  5. This interaction will enable ubiquitous and continuous customization of environments, perfectly targeted advertising, and hyper-magnification of socio-economic capabilities between individuals and groups


Universal Daemonization will change how humans interact with the world, and how the world interacts with itself. It's impossible to foresee all the various forms it will take.
The only thing we know for sure is that it's coming, and that we should get ready.
  * [Technical Components](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#components)
  * [Use Cases](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#usecases)
  * [Abuse Cases](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#abusecases)
  * [The Real Internet of Things](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#summary)


People are colossally underestimating the Internet of Things.
The IoT is not about alarm clocks that start your coffee maker, or about making more regular "things" accessible over the internet. The IoT will fundamentally alter how humans interact with the physical world, and will ultimately register as more significant than the internet itself.
## The primary technical components [​](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#the-primary-technical-components)
Here are the major pieces that will make up the real IoT:
  1. **Universal Daemonization** will give every object (humans, businesses, cars, furniture) a bi-directional digital interface that serves as a representation of itself. These interfaces will broadcast information about the object, as well as provide interaction points for others. Human objects will display their favorite reading, where they grew up, etc. for read-only information, and they'll have /connect interfaces for people to link up professionally, to request a date, or to digitally flirt if within 50 meters, etc. Businesses will have APIs for displaying menus, allergy information if it's a restaurant, an /entertainment interface so TV channels will change when people walk into a sports bar, and a /climate interface for people to request a temperature increase if they're cold.
  2. **Personal Assistants** will consume these services for you, letting you know what you should know about your surroundings based on your preferences, which you've either given it explicitly or it's learned over time. They'll also interact with the environment on your behalf, based on your preferences, to make the world more to your liking. So they'll order a water when you sit down to eat at a restaurant, send a coffee request (and payment) to the barista as you walk into your favorite coffee shop, and raise the temperature in any build you walk into because it knows you have a cold.
  3. **Digital Reputation** will be conveyed for humans through their daemons and federated ID. Through a particular identity tied to our real self, our professional skills, our job history, our buying power, our credit worthiness—will all be continuously updated and validated through a tech layer that works off of karma exchanges with other entities. If you think someone is trustworthy, or you like the work they do, or you found them hilarious during a dinner party, you'll be able to say this about them in a way that sticks to them (and their daemon) for others to see. It'll be possible to hide these comments, but most will be discouraged from doing so by social pressure.
  4. **Augmented Reality** will enable us to see the world with various filters for quality. So if I want to see only funny people around me, I can tell Siri, "Show me the funniest people in the room.", and 4 people will light up with a green outline. You can do the same for the richest, or the tallest, or the people who grew up in the same city as you. You'll be able to do the same when looking for the best restaurants or coffee shops as you walk down an unfamiliar street.


## What these advances mean for humanity [​](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#what-these-advances-mean-for-humanity)
  * The combination of daemons and digital reputation will **completely disrupt how work is done** on Earth. Instead of antiquated (and ineffective) interviews, a technical layer powered by matching algorithms will take information about jobs that need to be done and match them to people who are available (and qualified) to do them. Transportation, household jobs, creative work, mainstream corporate requisitions—these will all be staffed based on the best possible fit, and it'll happen in seconds rather than weeks or months.
  * Because so many of the objects we interact with will be daemonized, we'll be receiving an extraordinary amount of information from the world around us. This information will be used to create **full-scope life dashboards** that will illuminate and guide our behavior with regard to finances, health, social interaction, education, etc. Personal dashboards will be displayed on our living room walls, showing how the family did that day in food intake, calories burned, steps walked, and Karma gained and lost. Heads of household will see how college saving is going, how the family's investments are doing, and what if any tweaks should be made to existing strategies. The same will exist for businesses, with unified dashboards showing employee morale, cyber risk, public sentiment, logistical efficiency, employee health, and any anomalies worth noting, along with a list of recommendations for improvement.
  * Your daemon will be a representation of you, so **you'll be able to pay for things, open doors, get into clubs, gain access to your car, enter your hotel room, open your home's front door, send people money or Karma** for doing things you approve of, etc., all with a word or motion or gesture. You'll also be able to praise or dislike people or things with these gestures, which will stick to their daemons and profiles as part of their identity. The key is that your presence and gestures will represent something to the world, as your singular identity.
  * **The world will adjust to you as you move through it**. Car seats will adjust even though you've never been in it before. Lights will dim or change color based on your mood, and entertainment will adjust based on your preferences when you walk into buildings. Your personal assistant will be making these things happen on your behalf, using your identity to get access to perks and specials and privileged locations based on your reputation and Karma. The world (public infrastructure, your home and office, and businesses you frequent will be constantly customizing themselves based on your preferences.


## Use cases [​](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#use-cases)
Universal Daemonization will open entirely new categories of possibility, but here are a few examples. Consider that these aren't necessarily universally desired, and some of them are downright frightening in their power and scope.
But what I'm describing here is what I believe is _going to happen_ , not what I necessarily believe _should_ happen. These are two separate things, but if they are useful to the right subset of people or markets they will happen regardless of who approves.
  * Your environment will customize to you as you move through it, not only in your own home and office, but in public and in other businesses as well. The environment will read your daemon and adjust accordingly
  * Your Personal Assistant will be continually sending and receiving information on your behalf as you come in proximity with other people and objects. Submitting job qualifications, relationship interest, requests for more information about a product or service, requests to gain access to restricted areas or events, etc.
  * For those who empower their Personal Assistant to help manage their lives, there will be little need to manually check the location of someone you'll be meeting soon, or when their flight lands, or what they might want to eat. This will all be as easily available
  * Logistics becomes infinitely easier when every object has its own daemon that can report contents, location, speed, previous checkpoints, and any other metadata regarding the route, payload, etc. Many of these things are available now in various forms, but Universal Daemonization allows this data to live within the object itself and be updated far more dynamically
  * Work become a matter of reputation and discrete tasks that will be distributed to the most qualified person within seconds. The decision will be based on physical location, work reputation, skills, qualifications, credentials, reviews, and up-to-the-second availability. Imagine the Uber driver's app, but everyone has one at all times, and for every skill that they're good at. Siri will simply ask you quietly in your ear, "Web security assessment job from a 94 rated individual–do we accept?" And the same for dog grooming, massages, house-sitting, and personal finance–but with billions of people participating and competing for the same work.
  * Human sensory experience of the world will be augmented by the various layers of information provided by the objects around us, including other humans. We'll see, hear, and maybe even smell when people or things are of benefit, or are dangerous, to us in various contexts. Examples could include highlighting notable people in groups, warning you against rough neighborhoods or individuals while you drive or walk, etc.
  * When you look at a crowd you might see clusters of color (blue, red, green, purple) where various cliques are assembling, or see where the most dangerous people are, or the most wealthy, or the most beautiful
  * The same may be true when you're looking at neighborhoods, maps, buildings, or even individuals. You will see layers of information rendered as altered color, colored halos, or numbers on or around their person. Examples could include their Universal Reputation score, a subset of it such as credit worthiness, reliability, agreeableness, net worth, percentage of similar interests to yours. Your display of others will be completely configurable, showing people what matters to them about humans and objects that they're perceiving
  * Bouncers will be able to allow people into exclusive clubs based on a visual cue on their person, such as a green halo, or a green checkbox floating on their chest. The validation that produces the visual effect will come from them having received a valid invite, or from them having a popularity or beauty score that reaches a given standard.
  * You will be able to request photos and video from multiple angles in many locations. You'll tell your personal assistant, "Get a picture of me from above, or from the side, or from across the river, or from the other side of the street. This will issue requests to surrounding cameras along with your ID that authorizes you (or not) to access that camera, at which point the photo will be taken or not.
  * Exclusive offers can be sent to people of all manner of characteristics. People with the highest incomes, people who own houses over a certain size, people with certain bloodlines, people who have gone to certain schools, people who are over a certain height and also drive BMWs, etc. This concept of exclusivity will be one that is highlighted significantly by the combination of these technologies, and there will be many cases where they are used to increase the distance between those that have and those that do not.


## Abuse cases [​](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#abuse-cases)
This interactive capability between objects will not come without downsides. Universal Daemonization, and the services that emerge from it, will introduce an extraordinary new surface area for attack.
Here are some example abuse cases:
  * **Daemon spoofing** that allows one user to become another. Essentially the identity theft of the future
  * Users **overshare information** in their daemons that is sucked up by Passive Parsing Modules (PPMs) that sit in crowded locations
  * **Input validation** failures, due to insufficient [Security Broker](https://danielmiessler.com/blog/iot-security-broker/) protection, leads to dangerous/harmful manipulation of the object
  * **Insufficient authentication or authorization** on daemons allows for harvesting of personal information not meant for public
  * **Attacks against the validation services** allow people to post false validators in their own daemons, granting them illegitimate access and perks, e.g., showing themselves as making more than 100K/year, having a credit score above 800, or having VIP access to a given club, etc.
  * **Replay attacks** against resources, whereby an attack captures a successful, authorized interaction with a service and then replays that request to gain the same access


This is just a small subset of the security issues that we'll need to address. But don't convince yourself that these are so serious that it'll stop Universal Daemonization from happening. They're not. The functionality offered by this model will be so compelling that it will be rolled out regardless. It'll be our responsibility to secure it as it happens, just like many times in the past.
## The real Internet of Things [​](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot#the-real-internet-of-things)
IoT isn't about smart gadgets or connecting more things to the Internet. It's about continuous two-way interaction between everything in the world. It's about changing how humans and other objects interact with the world around them.
It will turn people and objects from static to dynamic, and make them machine-readable and fully interactive entities. Algorithms will continuously optimize the interactions between everyone and everything in the world, and make it so that the environment around humans constantly adjusts based on presence, preference, and desire.
The Internet of Things is not an Internet use case. Quite the opposite, the IoT represents the ultimate platform for human interaction with the physical world, and it will turn the Internet into a mere medium.
Let's get ready.
#### Notes
  1. There will be strong controls in place for dealing with malicious and accidental reputation tampering, as one's reputation will become an increasingly important part of peoples' lives and livelihood.
  2. A "daemon" is a service that listens for requests and responds to them in various ways when they arrive.
  3. As someone working in information security, the potential for abuse here is just staggering. Not just by attackers, but by governments. But we cannot afford to ignore what's coming because we don't like what it'll bring.
  4. Think about dating, seamless payments, customized experiences, humans adjusting their behavior based on being communicated your preferences by their PAs, etc. It touches everything.
  5. This is just a summary, and doesn't cover things like the implications to the concept of "private conversation" when everything is listening and recording.
  6. If the tone of this piece seems overconfident or presumptuous, I both agree and apologize. I am attempting something new by presenting some of my ideas in a way that will encourage one to read them, and that unfortunately seems to require posturing like an ass. Apologies.
  7. For a glimpse of the types of analytics and dashboarding that will soon be commonplace, have a look at [http://dashboard.sidlee.com](https://www.youtube.com/watch?v=TioYIJhdaKo).
  8. Here is [a more thorough discussion](https://danielmiessler.com/projects/ideas/#universaldaemonization) of the topic here on the site.
  9. [Here is the deck](https://danielmiessler.com/projects/ideas/#universaldaemonization) I used to present UD at HouSecCon in 2014.
  10. I lead a project called [The OWASP Internet of Things Top 10](https://owasp.org/www-project-internet-of-things-top-10/) that highlights the primary areas of security concern for IoT.
  11. The icons in the images are samples from Paul Sahner at iconizeme.com.


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Funiversal-daemonization-future-internet-iot&title=Universal%20Deamonization%20is%20the%20Future%20of%20the%20Internet%20and%20the%20Internet%20of%20Things "Share on Hacker News")
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
aibusinesscybersecurityethicsfutureinnovationsocietytechnology
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
