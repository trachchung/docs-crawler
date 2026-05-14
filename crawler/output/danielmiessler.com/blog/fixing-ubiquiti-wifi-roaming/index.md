<!-- Source: https://danielmiessler.com/blog/fixing-ubiquiti-wifi-roaming -->

# Fixing Ubiquiti WiFi Roaming
The settings I used to fix my multi-AP roaming issues with Ubiquiti WiFi
November 3, 2024
[ #cybersecurity](https://danielmiessler.com/archives/?tag=cybersecurity)[ #technology](https://danielmiessler.com/archives/?tag=technology)[ #tutorial](https://danielmiessler.com/archives/?tag=tutorial)[ #top](https://danielmiessler.com/archives/?tag=top)
 Glanding-warp…
1 reading now 
The three settings I had to enable to get proper WiFi roaming
## The problem
I’m a massive fan of Ubiquiti stuff, but even after upgrading to U7 Pro APs (and having a lot of them for enough coverage) I still had the following problem. 
**When I would move from one room to another, I’d keep my full WiFi signal, but I would lose connection to the network/internet.**
In order to fix it, I’d have to disconnect from wireless and reconnect—which means connecting to the closer AP. 
In other words, it wasn’t properly switching AP by itself, and when I moved to another room where another one was primary, I lost connection—even though I still showed full WiFi bars. 
## The solution
So the solution was first—a whole lot of searching—including using the new SearchGPT feature. Here’s a screenshot of the question and answer. 
SearchGPT’s answer to which settings to enable to fix the issue
To enable those you need to switch from Auto to Manual for your Wireless Network settings. 
Then enable these three:
  1. Fast Roaming
  2. BSS Transition
  3. Brand Steering


Within Wireless Manual Settings
After doing this, I can now move throughout the house without losing internet connectivity. 
Hope this helps!
Share
[HN Hacker News ](https://ul.live/share-hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Ffixing-ubiquiti-wifi-roaming&title=Fixing%20Ubiquiti%20WiFi%20Roaming "Share on Hacker News")
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
cybersecuritytechnologytutorialtop
[HOME](https://danielmiessler.com/)·[BLOG](https://danielmiessler.com/blog)·[ARCHIVES](https://danielmiessler.com/archives)·[ABOUT](https://danielmiessler.com/about)
