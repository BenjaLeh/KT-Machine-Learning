import linecache
import time
from ast import literal_eval
filelist=["best_35","feature_Bigram_40","feature_test97"]

best35 = linecache.getlines("best_35.txt")
Bigram_40 = linecache.getlines("feature_Bigram_40.txt")
test97= linecache.getlines("feature_test97.txt")
addition=linecache.getlines("georelated.txt")

k97=[]
for line in test97:
    k97.append(line.strip())

k_addition=[]
for line in addition:
    k_addition.append(line.strip())

k97=k97+k_addition

k35=[]
for line in best35:
    k35.append(line.strip())

unigrams=[x for x in k97 if x not in k35]

bigrams=[]
for line in Bigram_40:
    (t1,t2)=(line.split()[0],line.split()[1])
    bigrams.append((t1,t2))

linecache.clearcache()

tweets = linecache.getlines("dev-parsed.txt")
f = open('dev-extra133.arff','w', encoding='utf-8')

f.write("@relation "+"extra133" +'\n')
for uni in unigrams:
    f.write("@attribute "+str(uni)+" numeric "+'\n')
for bi in bigrams:
    f.write("@attribute " + str(bi[0]+'_'+bi[1]) + " numeric " + '\n')
f.write('@data'+'\n')
i=0
for rtweet in tweets:
    i+=1
    print(i)
    tweet=literal_eval(rtweet.strip())
    terms=tweet[0]

    bi_terms=tweet[1]

    d1 = [1 if x in terms else 0 for x in unigrams]
    d2 = [1 if x in bi_terms else 0 for x in bigrams]


    d = d1+d2

    f.write(str(d).replace(", ",",").replace("[","").replace("]","")+'\n')






