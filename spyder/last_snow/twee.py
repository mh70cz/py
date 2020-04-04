"""
https://apps.twitter.com
Owner	mh70cz
Owner ID	18578903
"""

from pathlib import Path
import json
import tweepy
import pandas as pd
import re



class MyStreamListener(tweepy.StreamListener):
    '''Tweet listener that creates a file called 'tweets.txt', collects
    streaming tweets as .jsons and writes them to the file 'tweets.txt';
    once tweet_limit tweets have been streamed,
    the listener closes the file and stops listening.
    hugobowne/tweet_listener.py
    '''
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.tweet_limit = 20
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write(json.dumps(tweet) + '\n')
        self.num_tweets += 1
        if self.num_tweets < self.tweet_limit:
            return True
        else:
            self.file.close()
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

def get_secrets():
    home = str(Path.home())
    secrets_file = home + '/Documents/pymh70.txt'
    access_token_secret = ""
    consumer_secret = ""
    try:
        with open(secrets_file, "r", encoding="utf8") as f:
            for line in f:
                #print(line)
                if line[0] == "#":
                    continue
                if "access_token_secret" in line:
                    first_qm_pos = line.find('"')
                    tmp_str = line[first_qm_pos + 1 : ]
                    second_qm_pos = tmp_str.find('"')
                    access_token_secret = tmp_str[:second_qm_pos]
                if "consumer_secret" in line:
                    first_qm_pos = line.find('"')
                    tmp_str = line[first_qm_pos + 1 : ]
                    second_qm_pos = tmp_str.find('"')
                    consumer_secret = tmp_str[:second_qm_pos]

    except Exception as e:
        print("Poblem getting secrets")
        raise e
    return (access_token_secret, consumer_secret)

def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False

# Store OAuth authentication credentials in relevant variables
access_token = "18578903-jqIt6bjBzhD46p8GDkYSuE5KChvRwSOWtolWNQjHL"
consumer_key = "dLbcVhiqDUOi9ZYmcYqa2UcqI"
access_token_secret, consumer_secret = get_secrets()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:

#stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])
stream.filter(track=["babiš", "bureš", "zeman", "okamura",
                     "kalousek", "top09", "ods"])
    
    
# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=["text", "lang"])

# Print head of DataFrame
print(df.head())  

# Initialize list to store tweet counts
[babis, zeman, okamura, kalousek] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    babis += word_in_text('babiš', row['text'])
    zeman += word_in_text('zeman', row['text'])
    okamura += word_in_text('okamura', row['text'])
    kalousek += word_in_text('kalousek', row['text'])
  
