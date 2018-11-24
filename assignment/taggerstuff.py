import nltk
from nltk import RegexpTagger
import pickle
from pickle import dump, load
from nltk.corpus import treebank, brown
train_set = brown.tagged_sents()[:4000] + treebank.tagged_sents()[:4000]
test_set = brown.tagged_sents()[2000:] + treebank.tagged_sents()[2000:]
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger
from nltk import ClassifierBasedPOSTagger
taggerTrained = True #Load or save tagger

def findBestTagger():
    defTagger = DefaultTagger('NN')
    #unigram
    t0 = UnigramTagger(train_set, backoff=defTagger)
    t1 = UnigramTagger(train_set, backoff=defTagger, cutoff=1)
    t2 = UnigramTagger(train_set, backoff=defTagger, cutoff=2)
    t3 = UnigramTagger(train_set, backoff=defTagger, cutoff=3)
    uniTagger = highest([t0,t1,t2,t3])
    #bigram
    t0 = BigramTagger(train_set, backoff=uniTagger)
    t1 = BigramTagger(train_set, backoff=uniTagger, cutoff=1)
    t2 = BigramTagger(train_set, backoff=uniTagger, cutoff=2)
    t3 = BigramTagger(train_set, backoff=uniTagger, cutoff=3)
    biTagger = highest([t0,t1,t2,t3])
    #trigram
    t0 = TrigramTagger(train_set, backoff=biTagger)
    t1 = TrigramTagger(train_set, backoff=biTagger, cutoff=1)
    t2 = TrigramTagger(train_set, backoff=biTagger, cutoff=2)
    t3 = TrigramTagger(train_set, backoff=biTagger, cutoff=3)
    t4 = TrigramTagger(train_set, backoff=biTagger, cutoff=4)
    triTagger = highest([t0,t1,t2,t3,t4])
    return triTagger

def highest(taggers):
    max = 0
    for t in taggers:
        x = t.evaluate(test_set)
        print(x)
        if x > max:
            max = x
            best = t
    return best

if taggerTrained:
    input = open('data/bestTagger.pkl', 'rb')
    bestTagger = load(input)
    input.close()
else:
    output = open('data/bestTagger.pkl', 'wb')
    dump(findBestTagger(), output, -1)
    output.close()

print(bestTagger.evaluate(test_set))
cpos = ClassifierBasedPOSTagger(train=train_set)
print(cpos.evaluate(test_set))
##################
#  Regex tagger  #
##################
patterns = [
    (r'[0-9]+:[0-9]+|[0-9]+-[0-9]+', 'T'),
    (r'.*road', 'L')
]
regexTagger = RegexpTagger(patterns, backoff=bestTagger)



#try out the regex tagger
x = nltk.word_tokenize("its at 9:00 till 5-00 on bigroad")
print(regexTagger.tag(x))
