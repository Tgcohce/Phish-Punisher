# Phish-Punisher

Made with the contributions of [@arin-prashar](https://github.com/arin-prasha) and Nelson (@techbynels on instagram)

Don't you hate scammers? Yeah we too! That is why we created this Python Script
To make real looking POST requests to a phishing website in order to fill up their database with fake credentials:

Costing them Money and Time (as they will have to go through each request and differentiate real victims from our generated ones)

# How?

- We took 300 most common male and female names. Put them into a big list, added numbers after them and added a random domain name from the biggest email service provider companies.
- For passwords we randomly generated some of them meanwhile also taking some from a passwordlist.
- We used threading for no downtime between requests


## The site
The phishing site we targeted was a clone of microsoft sign in, in the future we may write scripts for more and also add them here.

### Want to use this?
Feel free to edit, contribute, fork or use it yourself. Remember to only target phishing websites. We do not take responsibility for damages done on a legitimate website.

# Crypto Phish Punisher

I fine-tuned the original script to make post requests to a phishing website that tries to grab a crypto wallet's secret seed phrase. The site seems legitimate but when I looked at the code running in the background I noticed that your secret phrase gets sent to an email address and the site gives you an error no matter what.
