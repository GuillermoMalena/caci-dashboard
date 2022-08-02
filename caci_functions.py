#!/usr/bin/env python
# coding: utf-8

# ### Import Packages

# In[1]:


import sys
import time
import os
import tweepy as tw
import pandas as pd
import numpy as np
import itertools
import collections
import demoji
import functools
import operator
import emoji
from collections import Counter
from datetime import datetime
from tqdm import tqdm,trange
from datetime import date
from datetime import timedelta
import nltk
from nltk.corpus import stopwords
from nltk import bigrams
from nltk import trigrams
from airtable import Airtable
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


# ### Setup Twitter API Credentials

# In[2]:


consumer_key= 'sFUarGpGxd2g8ffveZlP12abB'
consumer_secret= 'gPRN4tosQKk52tSZ7MG5A6V9h7ln8sTPAYpWp8L52UizYqbf4K'
access_token= '1169759758070505472-Y4iKdDZia6v1fMyXX3Qcmp1k3E10Iz'
access_token_secret= 'CWrLNVwAFXchbpzNHorvcxlli8NAA0DuprB0YrJUEJxu6'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

print('ready')


# In[34]:


def filter_words():
    emoticons_happy = set([
':-)', ':)', ';)', ':o)', ':]', ':3', ':c)', ':>', '=]', '8)', '=)', ':}',
':^)', ':-D', ':D', '8-D', '8D', 'x-D', 'xD', 'X-D', 'XD', '=-D', '=D',
'=-3', '=3', ':-))', ":'-)", ":')", ':*', ':^*', '>:P', ':-P', ':P', 'X-P',
'x-p', 'xp', 'XP', ':-p', ':p', '=p', ':-b', ':b', '>:)', '>;)', '>:-)',
'<3'
])
# Sad Emoticons
    emoticons_sad = set([
':L', ':-/', '>:/', ':S', '>:[', ':@', ':-(', ':[', ':-||', '=L', ':<',
':-[', ':-<', '=\\', '=/', '>:(', ':(', '>.<', ":'-(", ":'(", ':\\', ':-c',
':c', ':{', '>:\\', ';('
])
#Emoji patterns
    emoji_pattern = re.compile("["
     u"\U0001F600-\U0001F64F"  # emoticons
     u"\U0001F300-\U0001F5FF"  # symbols & pictographs
     u"\U0001F680-\U0001F6FF"  # transport & map symbols
     u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
     u"\U00002702-\U000027B0"
     u"\U000024C2-\U0001F251"
     "]+", flags=re.UNICODE)
    emoticons = emoticons_happy.union(emoticons_sad)

    stop_words = set(stopwords.words('english'))
    stop_words.update(emoticons)
    filter_words = pd.read_csv('filter_words.csv')
    filter_words = filter_words['Filter Words'].tolist()
    new_stop_words = list(stop_words) + filter_words
    return new_stop_words


# In[404]:


def processtweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', tweet)
    tweet = re.sub('@[^\s]+', 'AT_USER', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = re.sub(r':', '', tweet)
    tweet = re.sub(r'‚Ä¶', '', tweet)
    tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)

    return tweet


# In[4]:


def tweet_scrap(userid):
    now = datetime.now()
    run_timestamp = now.strftime("%d-%b-%Y %H:%M:%S.%f")
    raw_tweets = pd.DataFrame()

    results = api.user_timeline(userid, tweet_mode='extended',count=1000)
    
    for t in results:
       
        ## first check if its a quoted tweet
        if t.is_quote_status is True:
            try: ## its a normal quoted tweets
               
                tweettext = processtweet(t.quoted_status.full_text)
             
                raw_tweets= raw_tweets.append({'User':t.user.screen_name,
                                   'Tweet': tweettext,
                                   'Bios':t.user.description,
                                   'Time':t.created_at,
                                   'Retweets':t.retweet_count,
                                   'Likes':t.favorite_count,
                                   'Followers':t.user.followers_count,
                                   'User ID': t.user.id_str,
                                   'Tweet ID':t.id_str,
                                   'Verified': t.user.verified,
                                   'Following':t.user.friends_count,
                                   'Run Timestamp':run_timestamp,
                                   'Is Quoted?':t.is_quote_status,
                                   'Is Retweet?': 'False',
                                   'Original Tweet ID': t.quoted_status_id_str,
                                   'Original User ID': t.quoted_status.user.id_str,
                                   'Original User': t.quoted_status.user.screen_name,
                                   'Original Time': t.quoted_status.created_at,
                                   'Original Likes': t.quoted_status.favorite_count,
                                   'Original Retweets': t.quoted_status.retweet_count},        
                                    ignore_index=True)
                
            except AttributeError: ##its a retweeted quoted tweet
                tweettext = processtweet(t.retweeted_status.full_text)
                raw_tweets= raw_tweets.append({'User':t.user.screen_name,
                                   'Tweet': tweettext,
                                   'Bios':t.user.description,
                                   'Time':t.created_at,
                                   'Retweets':t.retweet_count,
                                   'Likes':t.favorite_count,
                                   'Followers':t.user.followers_count,
                                   'User ID': t.user.id_str,
                                   'Tweet ID':t.id_str,
                                   'Verified': t.user.verified,
                                   'Following':t.user.friends_count,
                                   'Run Timestamp':run_timestamp,
                                   'Is Quoted?':t.is_quote_status,
                                   'Is Retweet?': 'True',
                                   'Original Tweet ID': t.retweeted_status.id_str,
                                   'Original User ID': t.retweeted_status.user.id_str,
                                   'Original User': t.retweeted_status.user.screen_name,
                                   'Original Time': t.retweeted_status.created_at,
                                   'Original Likes': t.retweeted_status.favorite_count,
                                   'Original Retweets': t.retweeted_status.retweet_count},        
                                    ignore_index=True)
                 
        else:
            try: ##check if its a normal retweet
                tweettext = processtweet(t.retweeted_status.full_text)
                raw_tweets= raw_tweets.append({'User':t.user.screen_name,
                                   'Tweet': tweettext,
                                   'Bios':t.user.description,
                                   'Time':t.created_at,
                                   'Retweets':t.retweet_count,
                                   'Likes':t.favorite_count,
                                   'Followers':t.user.followers_count,
                                   'User ID': t.user.id_str,
                                   'Tweet ID':t.id_str,
                                   'Verified': t.user.verified,
                                   'Following':t.user.friends_count,
                                   'Run Timestamp':run_timestamp,
                                   'Is Quoted?':t.is_quote_status,
                                   'Is Retweet?':'True',
                                   'Original Tweet ID': t.retweeted_status.id_str,
                                   'Original User ID': t.retweeted_status.user.id_str,
                                   'Original User': t.retweeted_status.user.screen_name,
                                   'Original Time': t.retweeted_status.created_at,
                                   'Original Likes': t.retweeted_status.favorite_count,
                                   'Original Retweets': t.retweeted_status.retweet_count},        
                                    ignore_index=True)
            except AttributeError:

                tweettext = processtweet(t.full_text)
                raw_tweets= raw_tweets.append({'User':t.user.screen_name,
                                   'Tweet': tweettext,
                                   'Bios':t.user.description,
                                   'Time':t.created_at,
                                   'Retweets':t.retweet_count,
                                   'Likes':t.favorite_count,
                                   'Followers':t.user.followers_count,
                                   'User ID': t.user.id_str,
                                   'Tweet ID':t.id_str,
                                   'Verified': t.user.verified,
                                   'Following':t.user.friends_count,
                                   'Run Timestamp':run_timestamp,
                                   'Is Quoted?':t.is_quote_status,
                                   'Is Retweet?':'N/A',
                                   'Original Tweet ID': 'N/A',
                                   'Original User ID': 'N/A',
                                   'Original User': 'N/A',
                                   'Original Time': 'N/A',
                                   'Original Likes': 0,
                                   'Original Retweets': 0},        
                                    ignore_index=True)
     
    
    return raw_tweets


# In[408]:


def get_user(user):
    user = api.get_user(user)
    user_id = user.id
    
    return user_id


# In[409]:


def add_user(user,user_csv):
    users_df = pd.read_csv(user_csv)
    user = api.get_user(user)
    users_df = users_df.append({'user':user.screen_name,
                             'user_id':user.id_str,
                             'name':user.name,
                             'location':user.location,
                             'profile_location':user.profile_location,
                             'bio':user.description,
                             'followers':user.followers_count,
                             'following':user.listed_count,
                             'created_at':user.created_at,
                             'verified':user.verified},
                            ignore_index=True)
    users_df = users_df.drop_duplicates(subset='user_id')
    users_df.to_csv(user_csv,index=False)
    


# In[410]:


def remove_user(user,user_csv):
    users_df = pd.read_csv(user_csv)
    users_df = users_df[users_df['user_id'] != user]
    print(users_df['user_id'].to_list())
    users_df.to_csv(user_csv,index=False)


# In[30]:


def get_tweets(tweet_csv,user_csv):
    if os.path.isfile(tweet_csv) is True:
        all_ztweets = pd.read_csv(tweet_csv,dtype={'User ID':'string','Tweet ID':'string','Original Tweet ID': 'string','Original User ID':'string'})
        users_df = pd.read_csv(user_csv)
        users_list = users_df['user_id'].to_list()
        for u in users_list:
            try:
                o = tweet_scrap(u)
                all_ztweets = all_ztweets.append(o)
            except:
                pass
        
     
    else:
        all_ztweets = pd.DataFrame()
        users_df = pd.read_csv(user_csv)
        users_list = users_df['user_id'].to_list()
        for u in users_list:
            try:
                o = tweet_scrap(u)
                all_ztweets = all_ztweets.append(o)
            except:
                pass
        
        
    all_ztweets = all_ztweets.drop_duplicates(subset='Tweet ID')

    all_ztweets['date'] = pd.to_datetime(all_ztweets['Time'])
    all_ztweets['date'] = all_ztweets['date'].dt.date
    all_ztweets['date']= all_ztweets['date'].astype(str)
    all_ztweets.to_csv(tweet_csv,index=False)
    return all_ztweets


# In[31]:


def tweet_topic_scrape(search_words, topic, resulttype, count):
    now = datetime.now()
    timestamp = now.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    csv_file_name = search_words + '_tweets.csv'
    file_path = r'/Users/GuillermoMalena_1/Desktop/Cacicazgo/Code/twitter_scraper'
    tweet_path = os.path.join(file_path, csv_file_name)
    tweets = tw.Cursor(api.search, q=search_words, result_type=resulttype,
                       lang="en", tweet_mode='extended').items(count)
    raw_tweets = pd.DataFrame()
    if os.path.isfile(tweet_path) is True:
        old_tweets = pd.read_csv(tweet_path)
        for t in tweets:
            if (not t.retweeted) and ('RT @' not in t.full_text):
                tweettext = processtweet(t.full_text)
                score = analyser.polarity_scores(tweettext)
                sentiment = score['compound']
                raw_tweets = raw_tweets.append({'User': t.user.screen_name,
                                                'Tweet': tweettext,
                                                'Bios': t.user.description,
                                                'Sentiment': sentiment,
                                                'Time': t.created_at,
                                                'Retweets': t.retweet_count,
                                                'Likes': t.favorite_count,
                                                'Followers': t.user.followers_count,
                                                'User ID': t.user.id_str,
                                                'Tweet ID': t.id_str,
                                                'Verified': t.user.verified,
                                                'Following': t.user.friends_count,
                                                'Is Retweet': t.is_quote_status,
                                                'Topic': topic,
                                                'Timestamp': timestamp},
                                               ignore_index=True)
    else:
        old_tweets = pd.DataFrame()
        for t in tweets:
            if (not t.retweeted) and ('RT @' not in t.full_text):
                tweettext = processtweet(t.full_text)
                score = analyser.polarity_scores(tweettext)
                sentiment = score['compound']
                raw_tweets = raw_tweets.append({'User': t.user.screen_name,
                                                'Tweet': tweettext,
                                                'Bios': t.user.description,
                                                'Sentiment': sentiment,
                                                'Time': t.created_at,
                                                'Retweets': t.retweet_count,
                                                'Likes': t.favorite_count,
                                                'Followers': t.user.followers_count,
                                                'User ID': t.user.id_str,
                                                'Tweet ID': t.id_str,
                                                'Verified': t.user.verified,
                                                'Following': t.user.friends_count,
                                                'Is Retweet': t.is_quote_status,
                                                'Topic': topic,
                                                'Timestamp': timestamp},
                                               ignore_index=True)

    raw_tweets = raw_tweets.drop_duplicates(subset=['User ID'])
    all_tweets = old_tweets.append(raw_tweets).reset_index(drop=True)
    all_tweets.to_csv(tweet_path, index=False)
    tweet_len = len(raw_tweets.index)

    return all_tweets

# In[33]:


def trending_topics(tweet_output, head):
    print("Calculating final trending topics")
    tweet_output = tweet_output.reset_index(drop=True)
    tweets_test = tweet_output[['User', 'Tweet']]
    tweets_test['Tweet'] = tweets_test['Tweet'].str.split()
    tweets_test['words'] = pd.Series(dtype='object')
    tweets_test['clean_words'] = pd.Series(dtype='object')
    for index, row in tweets_test.iterrows():
        body = row['Tweet']

        
        sw = filter_words()
        sw_new = [i for i in sw if type(i) is not float]
        clean_words = ' '.join((filter(lambda s: s not in sw_new, body))).split()

        tweets_test.at[index, "words"] = list(nltk.bigrams(tweets_test['Tweet'][index]))
        tweets_test.at[index, "clean_words"] = list(nltk.bigrams(clean_words))
    bigrams_df2 = pd.DataFrame(tweets_test['clean_words'].tolist(), tweets_test.index).add_prefix('bigram_')
    final = bigrams_df2.merge(tweets_test, how='inner', left_index=True, right_index=True)
    final_2 = final.drop('Tweet', 1)
    final_2 = final.drop(['words', 'clean_words', 'Tweet'], 1)
    final_melted = final_2.melt(id_vars='User')
    grouped = final_melted.groupby('value')['User'].value_counts().reset_index(name='count')
    final_trending = grouped['value'].value_counts().reset_index(name='count').head(head)
    
    return final_trending


# In[29]:


def get_trending_topics(date):
    
    path = r'/Users/GuillermoMalena_1/Desktop/Cacicazgo/Code/twitter_scraper'
    t_topics_csv = fr'test_topics_{date}.csv'
    topics_df = pd.read_csv(os.path.join(path, t_topics_csv))
    topics_list = list()
    for i in range(3):
        topic = topics_df['index'][i]
        topic_clean = re.sub('[(,.)]', '', topic)
        topic_clean = topic_clean.replace("'", "")
        topics_list.append(topic_clean)

    return topics_list


# In[412]:


def cities_dict():
        cities ={'Brooklyn':'40.6958,-73.9171',
         'Uptown':'40.84703397932981,-73.938452788558',
         'Atlanta': '33.7537,-84.3863',
         'Chicago':'41.71848203916271,-87.64219828351402',
         'Los Angeles': '34.05,-118.25',
         'Houston':'29.762778,-95.383056',
         'Detroit': '42.331389,-83.045833',
         'Memphis': '35.1175,-89.971111',
         'Baltimore' : '39.289444,-76.615278',
         'Miami' : '25.775278,-80.208889'    
    
        }
        return cities


def emoji_cleanup(tweets_df):
    tweets_df = tweets_df.drop_duplicates(subset='User ID').reset_index()
    tweets_df['New Bios'] = tweets_df['Bios'].str.split()
    # tweets_df['New Bios'] = tweets_df['New Bios'].astype(str)

    for index, row in tweets_df.iterrows():
        em_list = []
        if pd.isnull(row['New Bios']) is True:
            pass

        else:
            # print(row['New Bios'])
            for word in range(len(row['New Bios'])):

                if bool(emoji.get_emoji_regexp().search(row['New Bios'][word])) is True:

                    strings = emoji.get_emoji_regexp().split(row['New Bios'][word])

                    em_split_emoji = [x for x in strings if x]
                    split_emoji_len = len(em_split_emoji)

                    if split_emoji_len >= 1:

                        em_split_whitespace = [substr.split() for substr in em_split_emoji]
                        em_split = functools.reduce(operator.concat, em_split_whitespace)

                        for i in range(len(em_split)):

                            if bool(emoji.get_emoji_regexp().search(em_split[i])) is True:

                                text_em = demoji.findall(em_split[i]).get(em_split[i])
                                if text_em is not None:

                                    if text_em[:5] == 'flag:':
                                        em_list.append(text_em[6:])
                                    else:
                                        em_list.append(text_em)
                            tweets_df.at[index, 'New Bios'] = row['New Bios'] + em_list
                        # print(tweets_df[index,'New Bios'])
                        # tweets_df[index,'New Bios'].remove(row['New Bios'][word])

    return tweets_df['New Bios']


def get_sent(tweet_df):
    pos_sent = tweet_df[tweet_df['Sentiment'] > .2]
    neg_sent = tweet_df[tweet_df['Sentiment'] < .2]

    return pos_sent, neg_sent

def profile_count(tweet_df,profile_map,sent):
    pos_sent,neg_sent = get_sent(tweet_df)
    if sent == 'pos':
        total_counter = {}
        new_bios = emoji_cleanup(pos_sent)

        for i in range(len(new_bios)):

            bio = new_bios[i]
            if pd.isnull(bio) is True:
                pass
            else:
                a = [profile_map.get(key, 'not in dict') for key in bio if type(key) is not float]
                count = Counter(a)

                total_counter = dict(Counter(count)+Counter(total_counter))
    else:
        total_counter = {}
        new_bios = emoji_cleanup(neg_sent)

        for i in range(len(new_bios)):

            bio = new_bios[i]
            if pd.isnull(bio) is True:
                pass
            else:
                a = [profile_map.get(key, 'not in dict') for key in bio if type(key) is not float]
                count = Counter(a)

                total_counter = dict(Counter(count)+Counter(total_counter))
    final_counter = pd.DataFrame(sorted(total_counter.items(), key=lambda x: x[1],reverse=True),columns = ['Profile','Count'])
    return final_counter


def sentiment_table(tweet_df):
    pos_percentage = (len(tweet_df.loc[tweet_df['Sentiment'] > 0.05]) / len(tweet_df)) * 100
    neg_percentage = (len(tweet_df.loc[tweet_df['Sentiment'] < - 0.05]) / len(tweet_df)) * 100
    neu_percentage = (len(tweet_df[tweet_df['Sentiment'].between(-.05, .05)]) / len(tweet_df)) * 100
    data = [['Positive', pos_percentage], ['Negative', neg_percentage], ['Neutral', neu_percentage]]

    pos_len = len(tweet_df.loc[tweet_df['Sentiment'] > 0.05])
    neg_len = len(tweet_df.loc[tweet_df['Sentiment'] < 0.05])
    neu_len = len(tweet_df[tweet_df['Sentiment'].between(-.05, .05)])

    sent_table = pd.DataFrame(data, columns=['Sentiment', 'Value'])
    sent_table['User Count'] = pd.Series([pos_len, neg_len, neu_len])
    return sent_table



def topic_timeseries(csv_name,topic,frequency):
    path = r'/Users/GuillermoMalena_1/Desktop/Cacicazgo/Code/twitter_scraper'
    csv = csv_name
    full_path = os.path.join(path,csv)
    scraped_tweets = pd.read_csv(full_path)
    search_tweets = scraped_tweets.loc[scraped_tweets['Tweet'].str.contains(topic,case=False)]
    search_tweets['New Time'] = pd.to_datetime(search_tweets['Time'])
    tweet_freq = search_tweets.groupby(pd.Grouper(key='New Time',freq= frequency))['Tweet'].count()
    return tweet_freq


def tweet_topic_scrape_qc(search_words, topic, resulttype, count):
    now = datetime.now()
    timestamp = now.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    csv_file_name = search_words + '_tweets.csv'
    file_path = r'/Users/GuillermoMalena_1/Desktop/Cacicazgo/Code/twitter_scraper'
    tweet_path = os.path.join(file_path, csv_file_name)
    results = tw.Cursor(api.search, q=search_words, result_type=resulttype,
                       lang="en", tweet_mode='extended').items(count)
    raw_tweets = pd.DataFrame()
    if os.path.isfile(tweet_path) is True:
        old_tweets = pd.read_csv(tweet_path)
        for t in results:

            ## first check if its a quoted tweet
            if t.is_quote_status is True:
                try:  ## its a normal quoted tweets

                    tweettext = processtweet(t.quoted_status.full_text)
                    score = analyser.polarity_scores(tweettext)
                    sentiment = score['compound']
                    raw_tweets = raw_tweets.append({'User': t.user.screen_name,
                                                    'Tweet': tweettext,
                                                    'Bios': t.user.description,
                                                    'Time': t.created_at,
                                                    'Retweets': t.retweet_count,
                                                    'Likes': t.favorite_count,
                                                    'Followers': t.user.followers_count,
                                                    'User ID': t.user.id_str,
                                                    'Tweet ID': t.id_str,
                                                    'Verified': t.user.verified,
                                                    'Following': t.user.friends_count,
                                                    'Run Timestamp': timestamp,
                                                    'Is Quoted?': t.is_quote_status,
                                                    'Is Retweet?': 'False',
                                                    'Sentiment': sentiment,
                                                    'Original Tweet ID': t.quoted_status_id_str,
                                                    'Original User ID': t.quoted_status.user.id_str,
                                                    'Original User': t.quoted_status.user.screen_name,
                                                    'Original Time': t.quoted_status.created_at,
                                                    'Original Likes': t.quoted_status.favorite_count,
                                                    'Original Retweets': t.quoted_status.retweet_count},
                                                   ignore_index=True)

                except AttributeError:  ##its a retweeted quoted tweet
                    tweettext = processtweet(t.retweeted_status.full_text)
                    score = analyser.polarity_scores(tweettext)
                    sentiment = score['compound']
                    raw_tweets = raw_tweets.append({'User': t.user.screen_name,
                                                    'Tweet': tweettext,
                                                    'Bios': t.user.description,
                                                    'Time': t.created_at,
                                                    'Retweets': t.retweet_count,
                                                    'Likes': t.favorite_count,
                                                    'Followers': t.user.followers_count,
                                                    'User ID': t.user.id_str,
                                                    'Tweet ID': t.id_str,
                                                    'Verified': t.user.verified,
                                                    'Following': t.user.friends_count,
                                                    'Run Timestamp': timestamp,
                                                    'Is Quoted?': t.is_quote_status,
                                                    'Is Retweet?': 'True',
                                                    'Sentiment': sentiment,
                                                    'Original Tweet ID': t.retweeted_status.id_str,
                                                    'Original User ID': t.retweeted_status.user.id_str,
                                                    'Original User': t.retweeted_status.user.screen_name,
                                                    'Original Time': t.retweeted_status.created_at,
                                                    'Original Likes': t.retweeted_status.favorite_count,
                                                    'Original Retweets': t.retweeted_status.retweet_count},
                                                   ignore_index=True)

            else:
                try:  ##check if its a normal retweet
                    tweettext = processtweet(t.retweeted_status.full_text)
                    score = analyser.polarity_scores(tweettext)
                    sentiment = score['compound']
                    raw_tweets = raw_tweets.append({'User': t.user.screen_name,
                                                    'Tweet': tweettext,
                                                    'Bios': t.user.description,
                                                    'Time': t.created_at,
                                                    'Retweets': t.retweet_count,
                                                    'Likes': t.favorite_count,
                                                    'Followers': t.user.followers_count,
                                                    'User ID': t.user.id_str,
                                                    'Tweet ID': t.id_str,
                                                    'Verified': t.user.verified,
                                                    'Following': t.user.friends_count,
                                                    'Run Timestamp': timestamp,
                                                    'Is Quoted?': t.is_quote_status,
                                                    'Is Retweet?': 'True',
                                                    'Sentiment': sentiment,
                                                    'Original Tweet ID': t.retweeted_status.id_str,
                                                    'Original User ID': t.retweeted_status.user.id_str,
                                                    'Original User': t.retweeted_status.user.screen_name,
                                                    'Original Time': t.retweeted_status.created_at,
                                                    'Original Likes': t.retweeted_status.favorite_count,
                                                    'Original Retweets': t.retweeted_status.retweet_count},
                                                   ignore_index=True)
                except AttributeError:

                    tweettext = processtweet(t.full_text)
                    score = analyser.polarity_scores(tweettext)
                    sentiment = score['compound']
                    raw_tweets = raw_tweets.append({'User': t.user.screen_name,
                                                    'Tweet': tweettext,
                                                    'Bios': t.user.description,
                                                    'Time': t.created_at,
                                                    'Retweets': t.retweet_count,
                                                    'Likes': t.favorite_count,
                                                    'Followers': t.user.followers_count,
                                                    'User ID': t.user.id_str,
                                                    'Tweet ID': t.id_str,
                                                    'Verified': t.user.verified,
                                                    'Following': t.user.friends_count,
                                                    'Run Timestamp': timestamp,
                                                    'Is Quoted?': t.is_quote_status,
                                                    'Is Retweet?': 'N/A',
                                                    'Sentiment': sentiment,
                                                    'Original Tweet ID': 'N/A',
                                                    'Original User ID': 'N/A',
                                                    'Original User': 'N/A',
                                                    'Original Time': 'N/A',
                                                    'Original Likes': 0,
                                                    'Original Retweets': 0},
                                                   ignore_index=True)

    else:
        old_tweets = pd.DataFrame()
        for t in results:

            ## first check if its a quoted tweet
            if t.is_quote_status is True:
                try:  ## its a normal quoted tweets

                    tweettext = processtweet(t.quoted_status.full_text)
                    score = analyser.polarity_scores(tweettext)
                    sentiment = score['compound']
                    raw_tweets = raw_tweets.append({'User': t.user.screen_name,
                                                    'Tweet': tweettext,
                                                    'Bios': t.user.description,
                                                    'Time': t.created_at,
                                                    'Retweets': t.retweet_count,
                                                    'Likes': t.favorite_count,
                                                    'Followers': t.user.followers_count,
                                                    'User ID': t.user.id_str,
                                                    'Tweet ID': t.id_str,
                                                    'Verified': t.user.verified,
                                                    'Following': t.user.friends_count,
                                                    'Run Timestamp': timestamp,
                                                    'Is Quoted?': t.is_quote_status,
                                                    'Is Retweet?': 'False',
                                                    'Sentiment': sentiment,
                                                    'Original Tweet ID': t.quoted_status_id_str,
                                                    'Original User ID': t.quoted_status.user.id_str,
                                                    'Original User': t.quoted_status.user.screen_name,
                                                    'Original Time': t.quoted_status.created_at,
                                                    'Original Likes': t.quoted_status.favorite_count,
                                                    'Original Retweets': t.quoted_status.retweet_count},
                                                   ignore_index=True)

                except AttributeError:  ##its a retweeted quoted tweet
                    tweettext = processtweet(t.retweeted_status.full_text)
                    score = analyser.polarity_scores(tweettext)
                    sentiment = score['compound']
                    raw_tweets = raw_tweets.append({'User': t.user.screen_name,
                                                    'Tweet': tweettext,
                                                    'Bios': t.user.description,
                                                    'Time': t.created_at,
                                                    'Retweets': t.retweet_count,
                                                    'Likes': t.favorite_count,
                                                    'Followers': t.user.followers_count,
                                                    'User ID': t.user.id_str,
                                                    'Tweet ID': t.id_str,
                                                    'Verified': t.user.verified,
                                                    'Following': t.user.friends_count,
                                                    'Run Timestamp': timestamp,
                                                    'Is Quoted?': t.is_quote_status,
                                                    'Is Retweet?': 'True',
                                                    'Sentiment': sentiment,
                                                    'Original Tweet ID': t.retweeted_status.id_str,
                                                    'Original User ID': t.retweeted_status.user.id_str,
                                                    'Original User': t.retweeted_status.user.screen_name,
                                                    'Original Time': t.retweeted_status.created_at,
                                                    'Original Likes': t.retweeted_status.favorite_count,
                                                    'Original Retweets': t.retweeted_status.retweet_count},
                                                   ignore_index=True)

            else:
                try:  ##check if its a normal retweet
                    tweettext = processtweet(t.retweeted_status.full_text)
                    score = analyser.polarity_scores(tweettext)
                    sentiment = score['compound']
                    raw_tweets = raw_tweets.append({'User': t.user.screen_name,
                                                    'Tweet': tweettext,
                                                    'Bios': t.user.description,
                                                    'Time': t.created_at,
                                                    'Retweets': t.retweet_count,
                                                    'Likes': t.favorite_count,
                                                    'Followers': t.user.followers_count,
                                                    'User ID': t.user.id_str,
                                                    'Tweet ID': t.id_str,
                                                    'Verified': t.user.verified,
                                                    'Following': t.user.friends_count,
                                                    'Run Timestamp': timestamp,
                                                    'Is Quoted?': t.is_quote_status,
                                                    'Is Retweet?': 'True',
                                                    'Sentiment': sentiment,
                                                    'Original Tweet ID': t.retweeted_status.id_str,
                                                    'Original User ID': t.retweeted_status.user.id_str,
                                                    'Original User': t.retweeted_status.user.screen_name,
                                                    'Original Time': t.retweeted_status.created_at,
                                                    'Original Likes': t.retweeted_status.favorite_count,
                                                    'Original Retweets': t.retweeted_status.retweet_count},
                                                   ignore_index=True)
                except AttributeError:

                    tweettext = processtweet(t.full_text)
                    score = analyser.polarity_scores(tweettext)
                    sentiment = score['compound']
                    raw_tweets = raw_tweets.append({'User': t.user.screen_name,
                                                    'Tweet': tweettext,
                                                    'Bios': t.user.description,
                                                    'Time': t.created_at,
                                                    'Retweets': t.retweet_count,
                                                    'Likes': t.favorite_count,
                                                    'Followers': t.user.followers_count,
                                                    'User ID': t.user.id_str,
                                                    'Tweet ID': t.id_str,
                                                    'Verified': t.user.verified,
                                                    'Following': t.user.friends_count,
                                                    'Run Timestamp': timestamp,
                                                    'Is Quoted?': t.is_quote_status,
                                                    'Is Retweet?': 'N/A',
                                                    'Sentiment': sentiment,
                                                    'Original Tweet ID': 'N/A',
                                                    'Original User ID': 'N/A',
                                                    'Original User': 'N/A',
                                                    'Original Time': 'N/A',
                                                    'Original Likes': 0,
                                                    'Original Retweets': 0},
                                                   ignore_index=True)


    raw_tweets = raw_tweets.drop_duplicates(subset=['User ID'])
    all_tweets = old_tweets.append(raw_tweets).reset_index(drop=True)
    all_tweets.to_csv(tweet_path, index=False)
    tweet_len = len(raw_tweets.index)

    return all_tweets


def bio_ngrams(topic,tweet_output, test_map, profile):
    total_counter = {}
    new_bio = emoji_cleanup(tweet_output)
    # new_bio = new_bio.str.split()
    for i in tqdm(range(len(new_bio))):

        bio = new_bio[i]

        if pd.isnull(bio) is True:
            pass
        else:
            # count_len +=1
            bio = [re.sub('[(.,)]', "", str(bio[t])).replace("'", "") for t in range(len(bio))]
            l = list(nltk.bigrams(bio))

            bigrams = [re.sub('[(.,)]', "", str(l[t])).replace("'", "") for t in range(len(l))]
            a = [test_map.get(key, 'not in dict') for key in bigrams if type(key) is not float]
            b = [test_map.get(key, 'not in dict') for key in bio if type(key) is not float]

            c = set(a + b)

            count = Counter(c)

            total_counter = dict(Counter(count) + Counter(total_counter))

    final_counter = pd.DataFrame(sorted(total_counter.items(), key=lambda x: x[1], reverse=True),
                                 columns=[profile, f'{topic}_count'])
    final_counter[f'{topic}_percent'] = (final_counter[f'{topic}_count'] / final_counter[f'{topic}_count'].sum()) * 100
    pct_counter = final_counter.loc[final_counter[profile] != 'not in dict']
    pct_counter[f'{topic}_percent'] = pct_counter[f'{topic}_percent'] / pct_counter[f'{topic}_percent'].sum() * 100

    count_len = pct_counter[f'{topic}_count'].sum()

    users_len = len(tweet_output['User ID'].drop_duplicates())
    count_pct = (count_len / users_len) * 100
    print(f'Out of the {users_len} users for {topic}, {count_len} had {profile} data for this mapping, so {count_pct} percent')
    return pct_counter

def profile_heatmap(profile_map,tweet_df,column_header):
    bio_list = []
    profile = []
    tweet_df['New Bios'] = emoji_cleanup(tweet_df)
    for i in range(len(tweet_df['New Bios'].to_list())):
        bio = tweet_df['New Bios'][i]
        if pd.isnull(bio) is True:
            profile.append('N/A')
            pass
        else:

            a = [profile_map.get(key, 'not in dict') for key in bio if type(key) is not float]
            val = 'not in dict'
            b = [i for i in a if i != val]
            b = list(set(b))
            loc = ','.join(b)
            if len(b) > 0:
                bio_list.append(loc)
                profile.append(loc)
            else:
                profile.append('N/A')

    tweet_df[column_header] = profile
    print(len(bio_list))
    final_map = tweet_df.groupby(column_header)['Sentiment'].agg(['mean','count'])
    return final_map

