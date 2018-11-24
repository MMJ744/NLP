import nltk

def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes :
        backoff = cls(train_sents, backoff=backoff)
    return backoff

from nltk.corpus import treebank
from nltk.tag import DefaultTagger
train_set = treebank.tagged_sents()[:4000]
test_set = treebank.tagged_sents()[2000:]
from nltk.tag import UnigramTagger
unigramTagger = UnigramTagger(train_set)
from nltk.tag import BigramTagger, TrigramTagger
bigramTagger = BigramTagger(train_set, cutoff=2)
trigramTagger = TrigramTagger(train_set, cutoff=3)
tagger = backoff_tagger(train_set, [UnigramTagger, BigramTagger, TrigramTagger], backoff=DefaultTagger('NN'))
print(tagger.evaluate(test_set))
          
sentence = "John Smith went to the beach in Blackpool with his dog and Brett. James eats dragons with Gimly."
tokens = nltk.word_tokenize(sentence)
print(tokens)
taggedTokens = tagger.tag(tokens)
print(taggedTokens)
tree = nltk.ne_chunk(taggedTokens, binary=False)
print(tree)
