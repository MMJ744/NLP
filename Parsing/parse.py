import nltk
from nltk import load_parser

from nltk.corpus.reader import WordListCorpusReader
reader = WordListCorpusReader('', ['words.txt'])
words = [nltk.word_tokenize(i) for i in reader.words()]
cp = load_parser('grammar.fcfg', trace=0)


from nltk.corpus import treebank
from nltk.tag import DefaultTagger
train_set = treebank.tagged_sents()[:4000]
test_set = treebank.tagged_sents()[2000:]
from nltk.tag import UnigramTagger
unigramTagger = UnigramTagger(train_set)
from nltk.tag import BigramTagger, TrigramTagger
bigramTagger = BigramTagger(train_set, cutoff=2)
trigramTagger = TrigramTagger(train_set, cutoff=3)
def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes :
        backoff = cls(train_sents, backoff=backoff)
    return backoff
tagger = backoff_tagger(train_set, [UnigramTagger, BigramTagger, TrigramTagger], backoff=DefaultTagger('NN'))
for sentence in words:
    print(tagger.tag(sentence))




for sentence in words:
    print(sentence)
    for tree in cp.parse(sentence):
        print(tree)
    





