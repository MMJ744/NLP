import nltk
from nltk.corpus import brown
from nltk.corpus import treebank

train_set = treebank.tagged_sents()[:4000]
test_set = treebank.tagged_sents()[2000:]

from nltk.tag import DefaultTagger
#tagger = DefaultTagger('NN')

#print(tagger.evaluate(test_set))

from nltk.tag import UnigramTagger
unigramTagger = UnigramTagger(train_set)
#print(unigramTagger.evaluate(test_set))
#print(unigramTagger.evaluate(train_set))
#unigramTagger2 = UnigramTagger(train_set, cutoff=3)
#print(unigramTagger2.evaluate(test_set))
#print(unigramTagger2.evaluate(train_set))

from nltk.tag import BigramTagger, TrigramTagger
bigramTagger = BigramTagger(train_set, cutoff=2)
trigramTagger = TrigramTagger(train_set, cutoff=3)
#print(bigramTagger.evaluate(test_set))
#print(trigramTagger.evaluate(test_set))

#import brill_tagger_wrapper
#from brill_tagger_wrapper import train_brill_tagger
#brillTagger = train_brill_tagger(unigramTagger, train_set)
#print(brillTagger.evaluate(test_set))

def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes :
        backoff = cls(train_sents, backoff=backoff)
    return backoff
tagger = backoff_tagger(train_set, [UnigramTagger, BigramTagger, TrigramTagger], backoff=DefaultTagger('NN'))
print(tagger.evaluate(test_set))#0.99 found

