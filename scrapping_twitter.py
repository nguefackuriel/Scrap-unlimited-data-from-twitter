#pip install snscrape
#pip install pandas

# Import the librairies
import snscrape.modules.twitter as snstwitter
import pandas as pd

# Enter the key word of your research, the language and also the interval of date if needed
query = "('2023 OR elections,Nigeria, OR PDP, OR APC, OR PMB OR leaves, OR BODO-BONNY OR BRIDGES OR & OR ROAD, OR Nigeria's OR election) lang:en until:2023-04-01 since:2022-10-01"
# Create an empty list tweets that will contain the results of our search
tweets = []
# specify the limit
limit = 5000

for tweet in snstwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content, tweet.sourceLabel, tweet.hashtags, tweet.retweetCount, tweet.likeCount])

# Create a dataframe to save the result
df = pd.DataFrame(tweets, columns = ['Date', 'User', 'Tweet','Source', 'Hashtags', 'RetweetCount', 'likeCount' ])
#save the dataframe into a csv file
df.to_csv('Tweet_result_complete.csv') 

