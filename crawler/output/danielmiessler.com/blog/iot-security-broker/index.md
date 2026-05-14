<!-- Source: https://danielmiessler.com/blog/iot-security-broker -->

# The IoT Security Broker
May 4, 2015
[ #ai](https://danielmiessler.com/archives/?tag=ai)[ #apple](https://danielmiessler.com/archives/?tag=apple)[ #business](https://danielmiessler.com/archives/?tag=business)[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #future](https://danielmiessler.com/archives/?tag=future)[ #innovation](https://danielmiessler.com/archives/?tag=innovation)[ #technology](https://danielmiessler.com/archives/?tag=technology)
 SIEM-correlating…
I’ve written and spoken extensively about [Universal Daemonization](https://danielmiessler.com/blog/universal-daemonization-future-internet-iot/?utm_source=danielmiessler.com&utm_medium=newsletter&utm_campaign=the-iot-security-broker&last_resource_guid=Post%3A127a56cf-51a9-4644-a3a9-ffc73ce9dab7) >, which I believe to be the form that the IoT should/will eventually take. 
The idea is that humans and objects will have bi-directional daemons that broadcast their attributes and interactive capabilities, all built on TCP/IP, HTTP, and RESTFUL web services. Everything will have a daemon. People. Businesses. Restaurants. City park benches. Cars. Furniture in your home. Etc. And each will have associated web services that you can read from (GET) and interact with (POST). 
So when you walk into your home, or into a business, or near any object in the world, your DPA (digital personal assistant), probably Siri, or Cortana, or Google Now, will interact with that object according to your preferences. If it’s your home, it’ll set up the house the way you like it. If it’s a sports bar it might change the TVs to your favorite sport, and if it’s a restaurant it might order you a drink as soon as you sit down. 
That’s where the Security Broker concept comes in.
## The role of the IoT Security Broker
IoT isn’t going to be about how machines can talk to machines. That’s part of it, of course, but it’s not the big story. The real story is about changing how humans interact with their environment. The real story is about ecosystems. 
When someone walks into their home, each and every device in the house will not only be daemon-enabled (web services), but it’ll be enrolled into an ecosystem. 
You’re not going to manually configure every single item you buy and install at the house. You’re going to have your front door, your garage door, your lighting system, your visual display (formerly known as TV), your music collection, your furniture, your security and camera system, etc. 
All these will have services associated with them like in the diagram above. They’ll all be available for interaction from within the house. _But only from certain people_. 
So when you buy a new device from Best Buy or Fry’s, you’ll enroll it into an ecosystem. You’ll say, 
Integrate with my existing home security profile, as a furniture item. 
Or maybe,
Enroll this camera as a security device on the network. 
So what does that do exactly?
It tells the device to trust the house, and the people it trusts, and it tells the house to trust it—to the degree described in the policy. 
## The role of identity
One of the most powerful pieces of this entire concept is how identity will integrate within the ecosystems. 
When I enroll a device at the house, and I tell the house that the camera is integrated at level X, that will indicate who can do what with it. 
The entire house lets me do what I want with it. I have the following things that are IoT enabled in the house: 
  * cameras
  * video display
  * speaker system
  * music library
  * coffee maker
  * scales
  * thermostats
  * all door locks
  * etc.


So when I get home after being out for the day, I move my Apple Watch near my August door lock, and it lets me in. Why? Because the security broker on the door lock knows that Daniel Miessler is allowed to open the door, and it knows that it requires two-factor auth to do so, and it knows that two-factor was required to enable the Apple Watch’s authentication features. 
So it lets me in.
But what ID did I use? Was that a local account tied to the watch and paired with the door? No. Definitely not. 
It was a Federated ID. It was my Google ID, or my LinkedIn ID. Or my Facebook ID. Or, maybe in the future, my USCitizenID. 
_It’s one account._
So if it gets disabled, or you disable it yourself, nobody can use that account to do anything—anywhere. 
So your device you walk around with, and the daemon you emanate from yourself (which is really your device) will be broadcasting under the authority of that account. It’s the center of your identity. 
So when you walk into a VIP event at a club, where you’ve been granted access via a private invite, you can Jedi Wave the door and it’ll open. It’ll open because your hand wave was YOU, as proxied by your Apple Watch, and the auth attempt matched the federated ID that was granted access to the VIP event. 
And when you’re at home, about to go on vacation, you can say things like this to Siri (who just lives in your walls, like in Star Trek): 
Grant Chris Michaels access to the house at level 3. 
This means Chris can get inside the door with a Jedi Wave of his Apple Watch, but once he gets inside he can only use the toilet, watch some TV, and that’s it. 
When I know my buddy Jason is in town, I can say:
Grant Jason Haddix access to the house, at level 1.
This means he can open every door in the house, go anywhere he wants, play music from my collection, and even get access to my safe if he wants. 
It’s granular access, given to specific people, based on who they are. And it’s done through an existing ecosystem, like a house, or a car, or even $LIFE. I could potentially grant Jason $LIFE access Level 1, which will have X access for car, Y access for home, etc. 
The other function of the Security Broker system, within (IoT) objects, will be to protect against malicious usage. These include things like: 
  * User impersonation (Chris tries to be Jason while in my home so he can get into my safe) 
  * Replay attacks (capture someone opening a door
  * Multiple login attempts that don’t make sense (you can’t be using my coffee maker in San Francisco while opening a door lock in Paris, for example) 
  * Malicious requests (request tampering similar to existing web service/API attacks) 
  * Security and threat intelligence (your broker will be able to deny all requests from users known to be malicious, stop certain types of activity that are being seen as malicious around the world, etc.) 


## Summary
A Security Broker will soon be part of every object. Not every IoT object—that name won’t mean anything soon. Everything is an object. Everything is an IoT object. They’re redundant. 
Objects will be enrolled, through their Security Broker, into one or more ecosystems and domains. So the ecosystem may be a Google Home ecosystem that includes all home appliances and control systems, which uses Google IDs. Or maybe the ecosystem is the Apple Life Ecosystem, which includes access to everything. Car, music, images, online backups, etc.—all of which uses Apple IDs. 
And objects will be able to handle and integrate multiple ID federations as well. You’ll be able to tell your home ecosystem to honor Facebook, Google, Apple, and LinkedIn IDs, for example—if you trust those ecosystems to properly filter and protect their users. 
The Security Broker will ensure that the right people are doing the right things with each and every object. 
And finally, the Security Broker will ensure that the object is not being used in a malicious way by performing inspection of all requests as well as checking requests (and the users that make them) against a continuously updated database of suspicious and malicious activity. 
So:
  1. All objects will have services, e.g., home door locks, cars, coffee makers, etc. 
  2. All services will be protected by a broker.
  3. Brokers will allow named, federated users to perform certain actions on the object according to policy, as long as said actions or users are not malicious (locally inspected) or flagged in the global threat intelligence database. 


### Notes
  1. There will be more than just GET and POST, just as with existing REST interfaces. 
  2. Another use case for this delegation to ID concept is access to online resources if you are unavailable. Let’s say you’re in a temporary coma, or you are away in the Icelandic mountains for 9 months, and someone needs to get something. They can submit an unlock request using their ID, which you gave access, and they can get all your stuff. This also solves the issue of people getting access to your stuff if you die. 
  3. There will obviously be local backup options for federated ID on sensitive things like door locks to prevent accidental and intentional DoS of your home access, but those failure scenarios won’t stop it from being primary. 
  4. Payment will also be done via these daemons and gestures. Much like Apple Pay, except more tied to an identity than a device. 
  5. This centralized ID concept is going to considerably magnify the attack vector of deliberately locking peoples’ accounts. And it’s going to make it far more serious if someone’s account gets hacked. 
  6. The security/threat intelligence piece is going to be fascinating with this stuff. It’s not going to be a nice to have; it’s going to be essential infrastructure. We’ll need to know if/when a given user, group of users, or even an entire country needs to be denied access to certain objects or object types within a given location, based on what’s being seen live in the wild. 


Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fiot-security-broker&title=The%20IoT%20Security%20Broker "Share on Hacker News")
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
aiapplebusinesscybersecurityfutureinnovationtechnology
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
