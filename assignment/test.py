import nltk
from nltk.corpus.reader import WordListCorpusReader
from os import listdir
from os.path import isfile, join
import re
from pickle import load

read = open('data/bestTagger.pkl', 'rb')
tagger = load(read)
read.close()
current = 301
for c in range(301, 302): #486
    reader = WordListCorpusReader('data/untagged/', [str(c) + '.txt'])
    #tokens = [nltk.word_tokenize(i) for i in reader.words()]
    #for sentence in tokens:
       #taggedSentence = tagger.tag(sentence)
        #tree = nltk.ne_chunk(taggedSentence, binary=False)
        #print('----------------')
        #print(tree)
    #print(reader.words())
    s = " ".join(reader.words())
    print(s)
    print(reader.words())
    #print(tag_data(s, c))
# for i in reader.words():
#    m = re.search('at [0-9]+(pm|am)', i)
#    if (m): print(m.group(0))
#    m2 = re.search('[0-9]+:[0-9]+ (PM|AM|pm|am)', i)
#    if (m2): print(m2.group(0))
