import nltk
from nltk.corpus.reader import WordListCorpusReader
from nltk.corpus.reader import PlaintextCorpusReader
from os import listdir
from os.path import isfile, join
from tag import tag_data, save_tagged_data
from evaluation import  eval_all
from Ontology import get_topic, print_tree, getRelevant
from pickle import load

read = open('data/bestTagger.pkl', 'rb')
tagger = load(read)
read.close()
current = 301
self = []
for c in range(301, 485): #485
    reader = PlaintextCorpusReader('data/test_untagged/', [str(c) + '.txt'])
    file = open('data/untagged/' + str(c) + '.txt', 'r')
    text = file.read()
    file.close()
    get_topic(text, c)
    entities = tag_data(text)
    self.append(entities)
    save_tagged_data(text, entities, c)
print_tree()
eval = eval_all(self)
for key, value in eval.items():
    print('***-'+key.upper()+'-***')
    for k, v in value.items():
        print(k + ': ' + str(v*100) + '%')
print(getRelevant('robotics'))
print(getRelevant('students'))
