import nltk
from nltk.corpus.reader import WordListCorpusReader
from os import listdir
from os.path import isfile, join
import re
from pickle import load

# path = '/Users/Matthew/AppData/Roaming/nltk_data/corpora/untagged/'
# path = '/home/students/mmj744/nltk_data/corpora/untagged/'
# onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
# myCorpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(path, onlyfiles)

read = open('data/bestTagger.pkl', 'rb')
tagger = load(read)
read.close()

current = 301
for c in range(301, 486):
    reader = WordListCorpusReader('data/untagged/', [str(c) + '.txt'])
    tokens = [nltk.word_tokenize(i) for i in reader.words()]
    for sentence in tokens:
        taggedSentence = tagger.tag(sentence)
        tree = nltk.ne_chunk(taggedSentence, binary=False)
        print('----------------')
        print(tree)
    print(reader.words())
# for i in reader.words():
#    m = re.search('at [0-9]+(pm|am)', i)
#    if (m): print(m.group(0))
#    m2 = re.search('[0-9]+:[0-9]+ (PM|AM|pm|am)', i)
#    if (m2): print(m2.group(0))
