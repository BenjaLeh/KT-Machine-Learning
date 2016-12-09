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

tweets = linecache.getlines("E:\\Text and Reference\\Knowledge Technology\\assignment2\\project2\\tweets\\train-tweets.txt")
tweets=[x.split("\t") for x in tweets]

def tweet_bigramtoken_generator(b):
    # count_hash = Counter()
    count_all = Counter()
    count_id=[]

    tweets_X = [x for x in tweets if x[3].strip() == b]
    i=0
    for line in tweets_X:
            i=i+1
            count_id.append(line[0])
            line[2]=line[2].replace("'"," ")
            terms_all = [term for term in tknz.tokenize(line[2].lower())if term not in stop and (len(term)>1 and not term.isdigit())]
            bgs = bigrams(terms_all)
            count_all.update(bgs)
    print(len(set(count_id)))
    tokenlist=[p for (p,s) in count_all.most_common(50)]
    print(tokenlist)
    newlist=[]
    for token in tokenlist:
        countpop=[]
        for tweet in tweets_X:
            tweet[2] = tweet[2].replace("'", " ")
            terms_all = [term for term in tknz.tokenize(tweet[2].lower()) if
                         term not in stop and (len(term) > 1 and not term.isdigit())]
            bgs = bigrams(terms_all)
            if token in bgs:
                countpop.append(tweet[0])
        # print(token,len(set(countpop)))
        if len(set(countpop))>(len(set(count_id))*0.02):
        # if len(set(countpop)) / len(countpop) > 0.:
            newlist.append(token)
        print(newlist)
    candidate=[(p,c) for (p,c) in count_all.most_common(50) if p in newlist]
    print("#######################")
    print(candidate)
    print("found candidate "+str(len(candidate))+" potential uni-tokens")
    f=open('E:\\Text and Reference\\Knowledge Technology\\assignment2\\project2\\tweets\\tweet_Bigram_'+b+'.txt','w',encoding='utf-8')
    for i in candidate:
        f.write (str(i[0])+'\t'+str(i[1])+'\n')
    f.close()
    print("done")
#
Locations=['B','Se','H','SD','W']
for city in Locations:
    tweet_bigramtoken_generator(city)

