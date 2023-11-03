def process_text(text, punct = '.,;:"?!.'): 
    tweet = text.replace('#',' #')
    tweet_1 = tweet.replace('@',' @')
    tweet_1 = tweet_1.translate(tweet.maketrans('-',' ', punct)).split()
    return tweet_1
   
def get_features(text_list, feature): 
    return [item for item in text_list if item.startswith(feature)]
    

def feature_extract(filename, feature = '#'): 
    with open(filename, 'r', encoding = 'UTF8') as test:
        dict = {}
        text = test.read()
        w = process_text(text)
        v = get_features(w, feature)
        for i in v:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict
