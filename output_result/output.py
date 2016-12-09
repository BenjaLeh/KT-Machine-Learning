import linecache
import re

resultfile="testpredict.txt"
file="test-tweets.txt"

def output(tweetline):
    f = open('outout.txt', 'a', encoding='utf-8')
    for x in results:
        if tweetline[0]==x[0]:
            tweetline[3]=x[1].strip()
    f.write(tweetline[1]+','+tweetline[3]+'\n')
    f.close()

results = linecache.getlines(resultfile)
results = [x.split() for x in results]
print(results)
tweets = linecache.getlines(file)
tweets = [x.split("\t") for x in tweets]

for tweet in tweets:
    output(tweet)
