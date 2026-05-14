<!-- Source: https://danielmiessler.com/blog/machine-learning-will-revolutionize-content-discovery -->

# Machine Learning Will Revolutionize Content Discovery
January 18, 2017
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #creativity](https://danielmiessler.com/archives/?tag=creativity)[ #culture](https://danielmiessler.com/archives/?tag=culture)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #society](https://danielmiessler.com/archives/?tag=society)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #writing](https://danielmiessler.com/archives/?tag=writing)
 Meaning-searching…
1 reading now 
There are going to be millions of surprising applications of Machine Learning in coming years and decades, but I believe I’ve found one of the biggest ones. 
Content Discovery.
Today there are likely tens of millions of people creating things: short stories, dance, singing, poetry, essays, sculpture, and hundreds of other types of art. But let’s just take writing as an example. 
Tens of millions of people are writing online, but nobody sees 99% of what they create. 
That’s a travesty of a so-called technologically advanced civilization if I’ve ever heard of one, but the problem is simple to grasp. The systems being used to discover and present quality content to potential readers are horribly antiquated. 
  1. **Media** : Big media sites hire and discover good content from various sources, and then present those pieces to their readership. This is a good way to get exposed to the 1% of available content that some random person thought you should read, but a horrible way to see the rest of what wasn’t selected. Would you have picked the same 1% for yourself? Probably not. 
  2. **Content Platforms** : Platforms like WordPress, Blogger, Medium, and Tumblr that were designed to 1) help people create, and 2) help content be discovered by readers, but the problem of millions of creators is simply too hard for platforms like this to solve. Platforms like these simply have too much material in them to be usable for readers. The work of discovery is passed to the consumer, and with millions of options it’s a non-starter. 
  3. **Aggregators** : Services like Reddit and Hacker News are attempts at meritocracies for content. People submit their stuff (or someone else’s) and the community votes on it. After a period of time the best content bubbles to the top. The issue with these systems is that there is often a negative human element involved, either from blackhat SEO or from overzealous moderators with a particular set of biases or perspectives. In addition, only a tiny percentage of the best content is even being submitted. The result is that much good content either never gets seen or promoted, even on platforms designed to do precisely that. 


## Finding magic in the masses
I can think of no more perfect use of Machine Learning, and Supervised Learning in specific. The power of Supervised Learning specifically is that it can—with stunning and eerie accuracy—tell you when something has the magical _je ne sais quoi_. 
So the system we need to build is fairly straight-forward:
  * **Collect and model the highest-rated / best-received writing** for the last 5-100 years (the project can start smaller and then expand). The point is to teach the model what humans consider to be great content. 
  * **Create a crawling system that can index all writing platforms** (blogs, media, aggregators, etc.). The key is to get the long tail content, including what that random person just wrote yesterday on a brand-new blog. 
  * **Run the new content against the model to find the gems** that would otherwise have been ignored. 
  * **Create a series of APIs and frontends that highlight the best content** in particular topics and categories—regardless of source. So you can just read the best content in a broad category, or you could do a training exercise (or share your previous patterns) and receive extremely personalized recommendations. 


Imagine an AI-powered version of Reddit that harvested from 100% of written content instead of 1%. Think of all the wonderful pieces of thought and creativity that we could expose the world to that would have no chance of being seen otherwise. 
And then realize that we will do the same exact thing for audio, video, dance, music, and every other type of art. 
Think about someone in some tiny little town or village—with nothing but a mobile phone—being able to create something spontaneous and beautiful, and be discovered and exposed to the world within minutes. That’s what can happen when human bandwidth, attention, and biases are no longer limiters. 
Not only will this extract and highlight the other 99% of creativity that we haven’t been seeing in the world, but think of how many great artists never create because they’re daunted by the infetesimal chances of being discovered. Once people know that they can be seen if they create something exceptional, they’re far more likely to exercise their passion and talent. 
## Summary
  1. 99% of the best content is never discovered for multiple reasons.
  2. Humans can’t possibly find and review millions (and soon billions) of individual creators’ content. 
  3. Even if we could find and review, we would promote much that was bad, and ignore much that was good, due to our own sets of biases and incentives. 
  4. Machine (Supervised) Learning doesn’t have this problem, and if it could be trained properly and exposed to the world’s content, we could start to approach an actual artistic meritocracy. 


Tech and science are here to advance humanity, and there’s nothing more precious in that humanity than the creation and enjoyment of artistic expression. 
This system can (and will) literally discover and magnify human creativity in a way that was simply impossible before Machine Learning. 
Let’s build it.
### Notes
  1. I’m not actually sure what the true numbers are for people writing online, or how much exposure they’re getting. But I do think the approximation is accurate enough for the point being made. 
  2. We’d still have to worry about gaming with this system, but a combination of supervised and unsupervised learning should be able to tell us better than ever before what’s spam vs. genuine content. 
  3. Reverse Engineering the output of the Supervised Learning will be a fun project in and of itself. The way Deep Learning / Neural Nets work we wouldn’t automatically get an explanation for why any particular story resonated when another didn’t. 
  4. There will also be some variables that it’ll be hard for the algorithms to factor, such as a subject being topical. Riding a zeitgeist is a matter of time and place, which is largely a matter of luck, but even without this element considered at all it’d still be possible. But I can actually already think of a way to factor it, so solutions will certainly emerge for how to integrate it into the rating algorithm. 
  5. One idea is to go to the current aggregators (I’m thinking Reddit) and see if they want to start a project like this. The output would look much like their current product; the only difference is that the top stories would be less (or not at all) determined by human voting. 
  6. There’s a chance that some of the biases could get baked into the models, so we’d have to work around that as well. 


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fmachine-learning-will-revolutionize-content-discovery&title=Machine%20Learning%20Will%20Revolutionize%20Content%20Discovery "Share on Hacker News")
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
aicreativitycultureinnovationsocietytechnologywriting
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
