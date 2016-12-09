import linecache
import math
featurelist=[]
featuretry=[]
Locations=['B','Se','H','SD','W']
termsets={}
allkeys=set()
tweets_sum={}
totol_tweets_sum=0

for city in Locations:
    termsets[city]={}
    lines = linecache.getlines("tweet_Bigram_"+city+".txt")
    tweets_sum[city]=lines[0].split()[1]
    totol_tweets_sum +=int(lines[0].split()[1])
    lines=lines[2:]
    for line in lines:
        (term1,term2,frequency) = line.split()
        print(term1,term2,frequency)
        term=(term1,term2)
        termsets[city][term]=frequency
    print(len(termsets[city].keys()))
    print(tweets_sum[city])
    allkeys=allkeys.union(set(termsets[city].keys()))
print(totol_tweets_sum)
for key in allkeys:
    evaluator=[0 for i in range(len(Locations))]
    dif = 0
    keyoccur=0
    Evalu = 0
    for i in range(len(Locations)):
        city=Locations[i]
        if key in termsets[city]:
            evaluator[i]=100*int(termsets[city][key])/int(tweets_sum[city])
            keyoccur+=int(termsets[city][key])
        else:
            evaluator[i]=0
    Ex = 100*keyoccur/totol_tweets_sum
    for each in evaluator:
        # dif=max(dif,abs(each-Ex)/Ex)
        Evalu=Evalu+(each-Ex)*(each-Ex)/(Ex*Ex)
        # print(dif)
    if (Evalu>12):
        print(key,dif,Evalu,Ex,evaluator)
        featurelist.append(key)
print(str(len(featurelist))+"features included")
print(featurelist)
f=open('feature_Bigram_'+str(len(featurelist))+'.txt','w',encoding='utf-8')
for feature in featurelist:
    f.write(str(feature) + '\n')
f.close()










