import linecache
from collections import Counter
from nltk.corpus import stopwords
from nltk import bigrams
from nltk import pos_tag
import string
import re
from nltk.tokenize import TweetTokenizer

tknz= TweetTokenizer(strip_handles=True, reduce_len=True)
stop = stopwords.words('english')+list(string.punctuation)+ ['rt', 'via','u','im','...','..',':)']

tweets = linecache.getlines("dev-tweets.txt")
tweets=[x.split("\t") for x in tweets]
f=open('dev-parsed.txt','w',encoding='utf-8')

for line in tweets:
        line[2]=line[2].replace("'"," ")
        terms_all = [term for term in tknz.tokenize(line[2].lower())if term not in stop and (len(term)>1 and not term.isdigit())]
        bgs = bigrams(terms_all)
        f.write(str([list(set(terms_all)),list(set(bgs))]) + '\n')
f.close()
print("#######################")
print("done")
