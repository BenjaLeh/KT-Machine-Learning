import linecache
import numpy
featurelist=[]
Locations=['B','Se','H','SD','W']
termsets={}
allkeys=set()
tweets_sum={}
totol_tweets_sum=214880
for city in Locations:
    termsets[city]={}
    lines = linecache.getlines("tweet_1"+city+".txt")
    tweets_sum[city]=lines[0].split()[1]
    lines=lines[2:]
    for line in lines:
        (term, frequency) = line.split()
        termsets[city][term]=frequency
    print(len(termsets[city].keys()))
    print(tweets_sum[city])
    allkeys=allkeys.union(set(termsets[city].keys()))
for key in allkeys:
    evaluator=[0 for i in range(len(Locations))]
    keyoccur=0
    for i in range(len(Locations)):
        city=Locations[i]
        if key in termsets[city]:
            evaluator[i]=100*int(termsets[city][key])/int(tweets_sum[city])
            keyoccur+=int(termsets[city][key])
        else:
            evaluator[i]=0
    Ex = 100*keyoccur/totol_tweets_sum
    Evalu=0
    for each in evaluator:
        Evalu+=(each-Ex)*(each-Ex)/(Ex*Ex)
    if Evalu>15:
        print(key, Evalu,Ex,evaluator)
        featurelist.append(key)
print(str(len(featurelist))+"features included")
print(featurelist)
f=open('feature1_'+str(len(featurelist))+'.txt','w',encoding='utf-8')
for feature in featurelist:
    f.write(str(feature) + '\n')
f.close()










