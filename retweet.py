#!/bin/python
import os
from twitter import *

CONSUMER_KEY = "YOUR_CONSUMER_KEY"
CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"

FILTER = "ohm2013"

MY_TWITTER_CREDS = os.path.expanduser('./.twitter_credentials')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("Retweet Bot", CONSUMER_KEY, CONSUMER_SECRET,
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)

twitter_stream = TwitterStream(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))
iterator = twitter_stream.statuses.filter(track=FILTER)

twitter = Twitter(auth=OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET))

for tweet in iterator:
	#print tweet
	if (tweet.get('user') and tweet.get('text')):
		if ((not tweet['text'].startswith("RT @")) and (not tweet['text'].startswith("@"))):
			print "(" + str(tweet["id"]) + ") " + tweet['user']['screen_name'] + ": " + tweet['text']
			try:
				twitter.statuses.retweet._(tweet["id"])()
			except :
				print "Something went wrong. API limit?"
				pass
