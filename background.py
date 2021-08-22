import tweepy
import twitter_key
import re
import time
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

URL = input()
api = connect_api()
id= re.findall(r'/\d+', URL)[0][1:]
rt_list = api.retweets(id, 200)
tmp=[]

for rt in rt_list:
    tmp.append([rt.user.name, rt.user.screen_name])
print(len(tmp))


from time import time
t = int(time())
with open('retweeters-ids-%s-%s.txt' % (id, t), 'w', encoding='UTF-8') as f_out:
     for r in tmp:
         f_out.write(','.join(r))
         f_out.write('\n')
print('done')
