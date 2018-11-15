import nltk
from nltk.corpus import treebank
from nltk.tag import DefaultTagger
from nltk.tag import UnigramTagger
from nltk.tag import BigramTagger, TrigramTagger
from os import listdir
from os.path import isfile, join
path = '/Users/Matthew/AppData/Roaming/nltk_data/corpora/untagged/'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
myCorpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(path, onlyfiles)

def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes :
        backoff = cls(train_sents, backoff=backoff)
    return backoff

train_set = treebank.tagged_sents()[:4000]
test_set = treebank.tagged_sents()[2000:]
unigramTagger = UnigramTagger(train_set)
bigramTagger = BigramTagger(train_set, cutoff=2)
trigramTagger = TrigramTagger(train_set, cutoff=3)
tagger = backoff_tagger(train_set, [UnigramTagger, BigramTagger, TrigramTagger], backoff=DefaultTagger('NN'))
words = [nltk.word_tokenize(i) for i in myCorpus.words()]
for sentence in words:
    taggedSentence = tagger.tag(sentence)
    print(taggedSentence)
    tree = nltk.ne_chunk(taggedSentence, binary=False)
    print(tree)

