import linecache
import os
import re
a=['train','dev','test']
file="train-tweets.txt"

def writein(tweetline):
    path=tweetline[3].strip()
    if not os.path.isdir(path):
        os.makedirs(path)
    f = open(path+"\\"+tweetline[1]+'.txt', 'a', encoding='utf-8')
    f.write(tweetline[2]+'\t')
    f.close()

tweets = linecache.getlines(file)
tweets = [x.split("\t") for x in tweets]
for tweet in tweets:
    tweet[2]=re.sub(r'[^a-zA-Z\s]','',tweet[2])
    writein(tweet)