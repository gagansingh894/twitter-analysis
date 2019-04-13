import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt

#function to find percentage
def percentage(part, whole):
    return 100 * float(part)/float(whole)

#Establish Connection
consumer_key = 'CRQK2f7uXIa3fbRs1GnjaHrhI'
consumer_secret = '3f7QKkdGZ1dHCLlfZ3ZkwJM2MAA0GvMaNr6ACalO3WoYudmRaG'
access_token = '1657300350-mVG4Ywlee4LJz02gCk8zZ7IakJJvVbKLNnSUYGH'
access_token_secret = '5bBSyTsyBBMX5C9tOriaIYxiY5G67lRIdWwKQJydIND34'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

inputVal = int(input("""Select Option:
1. Keyword
2. Hashtag
Your Selection: """))

if inputVal == 1 :
    searchTerm = input("Enter search item: ")
elif inputVal == 2:
    Term = input("Enter search item: ")
    searchTerm = "#" + Term 

noOfSearchTerms = int(input("Enter number of items: "))


public_tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

neutral = 0
polarity = 0
positive = 0
negative = 0

for tweet in public_tweets:
    #print()
    #print(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity 

    if (analysis.sentiment.polarity == 0 ):
        neutral += 1
    
    elif (analysis.sentiment.polarity < 0.00 ):
        negative += 1
    
    elif (analysis.sentiment.polarity > 0.00 ):
        positive += 1

positive = format(percentage(positive, noOfSearchTerms), '.2f')
negative = format(percentage(negative, noOfSearchTerms),'.2f')
neutral = format(percentage(neutral, noOfSearchTerms), '.2f')

print("Following are the results after analyzing " + str(noOfSearchTerms) + " items containing " + searchTerm)
print("Positive Sentiment % : " + positive)
print("Negative Sentiment % : " + negative)
print("Neutral Sentiment % : " + neutral)

#Plot on graph
labels = ['Positive [' + str(positive) + '%]', 'Neutral [' + str(neutral) + '%]', 'Negative [' + str(negative) + '%']
sizes = [positive,negative,neutral]
colors = ['green','red','blue']
patches, texts = plt.pie(sizes,colors=colors, startangle=90)
plt.legend(patches,labels, loc='best')
plt.title("Following are the results after analyzing " + str(noOfSearchTerms) + " items containing " + searchTerm)
plt.axis('equal')
plt.tight_layout
plt.show()
