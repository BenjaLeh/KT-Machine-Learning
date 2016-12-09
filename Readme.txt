##################################################################################################################################
--------------------------------------------------------------Readme--------------------------------------------------------------
##################################################################################################################################
 |NBM-170_feature_generator
 |----|unitoken_generator.py------------: Generate top 500 TFIDF mono-tokens from train-tweets.txt for each loc.
 |----|bigram_token_generator.py--------: Generate top 50 TFIDF bi-tokens from train-tweets.txt for each loc.
 |----|tweet2tokenlist------------------: Convert "train/dev/test-tweets.txt" to tokenlist.
 |----|feature_inclusion.py-------------: Include mono-gram features.
 |----|feature_inclusion_bigrams.py-----: Include bi-gram features.
 |----|features2arff.py-----------------: Generate features to arff file("merge" cmd needed to merge the new features with best35).
 |
 |NBM-1000_feature_generator
 |----|sort_tweets_by_tweetID
 |---------|sort_tweets_by_tweetID.py---: Sort train/dev-set by tweetID into folders (B|H|W|SD|Se)(for TextDictionaryLoader in Weka).
 |----|test_by_tweetID
 |---------|test_by_tweetID.py----------: Sort test-set by tweetID into folders (B|H|W|SD|Se)(for TextDictionaryLoader in Weka).
 |
 |NBMT_feature_generator
 |----|sort_tweets_by_userID
 |---------|sort_tweets_by_userID.py----: Sort train/dev-set by userID into folders (B|H|W|SD|Se)(for TextDictionaryLoader in Weka).
 |----|test_by_userID
 |---------|test_userID.py--------------: Sort test-set by userID into folders (B|H|W|SD|Se)(for TextDictionaryLoader in Weka).
 |
 |output_result
 |----|output.py------------------------: convert predicition into Kaggle format.
 |----|testpredict_NBMT.txt-------------: arff file with heads removed.
 |----|output.txt-----------------------: Kaggle-readable test-predicition.("id,Category" was added manually.) 
 |
 |result_buffer
 |----|170_NBM_bytweet------------------: Model result from 170_NBM
 |----|1000_NBM_bytweet-----------------: Model result from 1000_NBM
 |----|NBMT_byuser----------------------: Model result from NBMT
 |Readme.txt
 |output.txt----------------------------: A copy of the file in /output_result/.
 
 