import tweepy
import twitter_key
import re
import random

## 트위터 api와 연결
def connect_api():
    consumer_key = twitter_key.DATABASE_TWITTER_KEY['consumer_key']
    consumer_secret = twitter_key.DATABASE_TWITTER_KEY['consumer_secret']
    access_token = twitter_key.DATABASE_TWITTER_KEY['access_token']
    access_token_secret = twitter_key.DATABASE_TWITTER_KEY['access_token_secret']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api
api = connect_api()

URL=input()
id=re.findall(r'/\d+', URL)[0][1:]
rt_count = 100
rt_list = api.retweets(id)
tmp=[]

for rt in rt_list:
    tmp.append(rt.user.screen_name)
print(len(tmp))

# random.shuffle(tmp)
# selected=tmp[:rt_count]
# print(selected)