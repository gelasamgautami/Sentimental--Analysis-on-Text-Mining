import pandas as pd
import matplotlib.pyplot as polt
from textblob import TextBlob
# Reading tweets from csv file
df = pd.read_csv("C:\\Users\\noopur\\Downloads\\gold.csv", encoding="ISO-8859-1")
# df = pd.read_csv("C:\\Users\\nikhila\\Desktop\\Sentiment\\keralaflood.csv",encoding = "ISO-8859-1")
raw_tweets = df.text
tweets = []
for tweet in raw_tweets:
 # empty dictionary to store required params of a tweet
 structured_tweet = {}
 # saving text of tweet
 structured_tweet['text'] = tweet
 # saving sentiment of tweet
 analysis = TextBlob(tweet)
 if analysis.sentiment.polarity > 0:
 structured_tweet['sentiment'] = 'positive'
 structured_tweet['polarity'] = analysis.sentiment.polarity
 elif analysis.sentiment.polarity == 0:
 structured_tweet['sentiment'] = 'neutral'
 structured_tweet['polarity'] = analysis.sentiment.polarity
 else:
 structured_tweet['sentiment'] = 'negative'
 structured_tweet['polarity'] = analysis.sentiment.polarity
 tweets.append(structured_tweet)
# Separating positive tweets from tweets
pos_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
# % of positive tweets
print("Positive tweet {} %".format(100 * len(pos_tweets) / len(tweets)))
# Separating negative tweets from tweets
neg_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
# % of negative tweets
print("Negative tweets {} %".format(100 * len(neg_tweets) / len(tweets)))
# % of neutral tweets
print("Neutral tweets {} % ".format(100 * (len(tweets) - len(neg_tweets) - len(pos_tweets)) / len(tweets)))
ptext = []
ntext = []
for tweet in tweets:
 if tweet['polarity'] > 0.8:
 ptext.append(tweet['text'])
for tweet in tweets:
6
 if tweet['polarity'] < -0.7:
 ntext.append(tweet['text'])
# printing tweets
print("\n Positive tweets:")
print(ptext[:5])
print("\n Negative tweets:")
print(ntext[:5])
def print_worldcloud(words):
 from wordcloud import WordCloud
 word_cloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(words)
 polt.figure(figsize=(10, 7))
 polt.imshow(word_cloud, interpolation="bilinear")
 polt.axis('off')
 polt.show()
all_words = ' '.join([text for text in ptext])
print_worldcloud(all_words)
all_words = ' '.join([text for text in ntext])
print_worldcloud(all_words)