import nltk
from nltk import RegexpTagger
import pickle
from pickle import dump, load
from nltk.corpus import treebank, brown
train_set = treebank.tagged_sents()[:4000] + brown.tagged_sents()[:4000]
test_set = treebank.tagged_sents()[2000:]
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger
from nltk import ClassifierBasedPOSTagger
import brill_tagger_wrapper
from brill_tagger_wrapper import train_brill_tagger
taggerTrained = False #Load or save tagger

def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes :
        backoff = cls(train_sents, backoff=backoff)
    return backoff
if taggerTrained:
    input = open('data/bestTagger.pkl', 'rb')
    tagger = load(input)
    input.close()
else:
    output = open('data/bestTagger.pkl', 'wb')
    backoffTagger = backoff_tagger(train_set, [UnigramTagger, BigramTagger, TrigramTagger], backoff=DefaultTagger('NN'))
    brillTagger   = train_brill_tagger(backoffTagger, train_set)
    dump(brillTagger, output, -1)
    output.close()
    tagger = brillTagger
print(tagger.evaluate(test_set))
print(tagger.evaluate(brown.tagged_sents()))
#cpos = ClassifierBasedPOSTagger(train=train_set)
#print(cpos.evaluate(test_set))
##################
#  Regex tagger  #
##################
patterns = [
    (r'[0-9]+:[0-9]+|[0-9]+-[0-9]+', 'T'),
    (r'.*road', 'L')
]
regexTagger = RegexpTagger(patterns)



#try out the regex tagger
x = nltk.word_tokenize("its at 9:00 till 5-00 on bigroad")
print(regexTagger.tag(x))




