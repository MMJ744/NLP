from pickle import dump, load

import nltk
from nltk import RegexpTagger
from nltk.corpus import treebank, brown
from nltk.tag import DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger

import brill_tagger_wrapper

taggerTrained = True  # Load or save tagger


def make_train_set(corpora):
    list = []
    for corpus in corpora:
        x = int(len(corpus.tagged_sents()) * 0.95)
        list = list + corpus.tagged_sents()[:x]
    return list


def make_test_set(corpora):
    list = []
    for corpus in corpora:
        x = int(len(corpus.tagged_sents()) * 0.05)
        list = list + corpus.tagged_sents()[x:]
    return list


test_set = make_test_set([brown, treebank])


def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes:
        backoff = cls(train_sents, backoff=backoff)
    return backoff


if taggerTrained:
    input = open('data/bestTagger.pkl', 'rb')
    tagger = load(input)
    input.close()
else:
    output = open('data/bestTagger.pkl', 'wb')
    train_set = make_train_set([brown, treebank])
    backoffTagger = backoff_tagger(train_set, [UnigramTagger, BigramTagger, TrigramTagger], backoff=DefaultTagger('NN'))
    brillTagger = brill_tagger_wrapper.train_brill_tagger(backoffTagger, train_set)
    dump(brillTagger, output, -1)
    output.close()
    tagger = brillTagger
print(tagger.evaluate(test_set))
print(tagger.evaluate(brown.tagged_sents()))
print(tagger.evaluate(treebank.tagged_sents()))
# cpos = ClassifierBasedPOSTagger(train=train_set)
# print(cpos.evaluate(test_set))
##################
#  Regex tagger  #
##################
patterns = [
    (r'[0-9]+:[0-9]+|[0-9]+-[0-9]+', 'T'),
    (r'.*road', 'L')
]
regexTagger = RegexpTagger(patterns)

# try out the regex tagger
x = nltk.word_tokenize("its at 9:00 till 5-00 on bigroad")
print(regexTagger.tag(x))
