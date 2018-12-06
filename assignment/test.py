import nltk
from nltk.corpus.reader import WordListCorpusReader
from nltk.corpus.reader import PlaintextCorpusReader
from os import listdir
from os.path import isfile, join
from tag import tag_regex_data
from pickle import load

read = open('data/bestTagger.pkl', 'rb')
tagger = load(read)
read.close()
current = 301
for c in range(480, 481): #486
    reader = PlaintextCorpusReader('data/untagged/', [str(c) + '.txt'])
    file = open('data/untagged/' + str(c) + '.txt', 'r')
    print(tag_regex_data(file.read()))
    #print(reader.words())


# for i in reader.words():
#    m = re.search('at [0-9]+(pm|am)', i)
#    if (m): print(m.group(0))
#    m2 = re.search('[0-9]+:[0-9]+ (PM|AM|pm|am)', i)
#    if (m2): print(m2.group(0))
