import re
import json
import pandas as pd
import matplotlib.pyplot as plt


tweets_data_path = 'i_have_the_flu2.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r", 16777216)
tweets_locations = []
tweets_timezone = []
tweets_createdat = []
tweets_place = []
tweets_text = []
tweets_full = []


for line in tweets_file:
    try:
        tweet = json.loads(line)

        # print tweet['text']
        # tweets_locations.append(tweet['user']['location'])
        # tweets_createdat.append(tweet['user']['created_at'])
        # tweets_place.append(tweet['place']['name'])
        # tweets_timezone.append(tweet['user']['time_zone'])
        tweets_data.append(tweet)
        # print "User: \n"
        # print "\nTime Zone: " + tweet['user']['time_zone']
        # print "\nLocation: " + tweet['user']['location']
        # print "\nCreated At: " + tweet['user']['created_at']
        # print "\nPlace: " + tweet['place']['name']
        # print "\n\n\n\n"
        # tweets_locations.append(tweet['user']['location'])
        # tweets_createdat.append(tweet['user']['created_at'])
        # tweets_place.append(tweet['place']['name'])
        # tweets_timezone.append(tweet['user']['time_zone'])


        if "i have the flu" in tweet['text']:
            tweets_locations.append(tweet['user']['location'])
            tweets_createdat.append(tweet['user']['created_at'])
            tweets_place.append(tweet['place']['name'])
            tweets_timezone.append(tweet['user']['time_zone'])

        if "I have the flu" in tweet['text']:
            tweets_locations.append(tweet['user']['location'])
            tweets_createdat.append(tweet['user']['created_at'])
            tweets_place.append(tweet['place']['name'])
            tweets_timezone.append(tweet['user']['time_zone'])

        if "fever and chills" in tweet['text']:
            tweets_locations.append(tweet['user']['location'])
            tweets_createdat.append(tweet['user']['created_at'])
            tweets_place.append(tweet['place']['name'])
            tweets_timezone.append(tweet['user']['time_zone'])

        if "HAVE THE FLU" in tweet['text']:
            tweets_locations.append(tweet['user']['location'])
            tweets_createdat.append(tweet['user']['created_at'])
            tweets_place.append(tweet['place']['name'])
            tweets_timezone.append(tweet['user']['time_zone'])

        if "hate the flu" in tweet['text']:
            tweets_locations.append(tweet['user']['location'])
            tweets_createdat.append(tweet['user']['created_at'])
            tweets_place.append(tweet['place']['name'])
            tweets_timezone.append(tweet['user']['time_zone'])

        if "body aches" in tweet['text']:
            tweets_locations.append(tweet['user']['location'])
            tweets_createdat.append(tweet['user']['created_at'])
            tweets_place.append(tweet['place']['name'])
            tweets_timezone.append(tweet['user']['time_zone'])



    except:
        continue

# print tweets_locations
# print tweets_createdat
# print tweets_place
# print tweets_timezone


# print(tweets_text)
# print(tweets_data)

# def word_in_text(word, text):
#     word = word.lower()
#     text = text.lower()
#     match = re.search(word, text)
#     if match:
#         return True
#     return False

print len(tweets_data)

# tweets = json.loads(tweets_file)
#
# if 'place' in tweets and tweets['place'] is not None:
#      print tweets['place']

tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet.get('text', None),tweets_data)
tweets['lang'] = map(lambda tweet: tweet.get('lang', None),tweets_data)
tweets['location'] = map(lambda tweet: tweet.get('location', None),tweets_data)




# tweets['flu'] = tweets['text'].apply(lambda tweet: word_in_text('flu', tweet))
# tweets['fever'] = tweets['text'].apply(lambda tweet: word_in_text('fever', tweet))
# tweets['chills'] = tweets['text'].apply(lambda tweet: word_in_text('chills', tweet))
#
#
# print tweets['flu'].value_counts()[True]
# print tweets['fever'].value_counts()[True]
# print tweets['chills'].value_counts()[True]