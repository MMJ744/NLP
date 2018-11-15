import nltk
from nltk.corpus import treebank
from nltk.tag import DefaultTagger
from nltk.tag import UnigramTagger
from nltk.tag import BigramTagger, TrigramTagger
from nltk.corpus.reader import WordListCorpusReader
from os import listdir
from os.path import isfile, join
import re
#path = '/Users/Matthew/AppData/Roaming/nltk_data/corpora/untagged/'
#path = '/home/students/mmj744/nltk_data/corpora/untagged/'
#onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
#myCorpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(path, onlyfiles)

def backoff_tagger(train_sents, tagger_classes, backoff=None):
    for cls in tagger_classes :
        backoff = cls(train_sents, backoff=backoff)
    return backoff

train_set = treebank.tagged_sents()[:4000]
test_set = treebank.tagged_sents()[2000:]

#tagger = backoff_tagger(train_set, [UnigramTagger, BigramTagger, TrigramTagger], backoff=DefaultTagger('NN'))
#words = 
#print(words)
#for sentence in words:
    #taggedSentence = tagger.tag(sentence)
    #print(taggedSentence)
   # tree = nltk.ne_chunk(taggedSentence, binary=False)
    #print(tree)
current = 301

reader = WordListCorpusReader('data/untagged/', [str(current) + '.txt'])
#tokens = [nltk.word_tokenize(i) for i in reader.words()]
#for sentence in tokens:
#    taggedSentence = tagger.tag(sentence)
#    #print(taggedSentence)
#    tree = nltk.ne_chunk(taggedSentence, binary=False)
#    print(tree)
print(reader.words())
for i in reader.words():
    m = re.search('at [0-9]+(pm|am)', i)
    if(m) : print(m.group(0))
    m2 = re.search('[0-9]+:[0-9]+ (PM|AM|pm|am)', i)
    if(m2) : print(m2.group(0))
