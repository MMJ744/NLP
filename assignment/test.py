import nltk
from nltk.corpus.reader import WordListCorpusReader
from nltk.corpus.reader import PlaintextCorpusReader
from os import listdir
from os.path import isfile, join
from tag import tag_regex_data, save_tagged_data
from evaluation import  eval_all
from pickle import load

read = open('data/bestTagger.pkl', 'rb')
tagger = load(read)
read.close()
current = 301
for c in range(301, 485): #485
    reader = PlaintextCorpusReader('data/test_untagged/', [str(c) + '.txt'])
    file = open('data/untagged/' + str(c) + '.txt', 'r')
    text = file.read()
    file.close()
    entities = tag_regex_data(text)
    save_tagged_data(text, entities, c)
eval = eval_all()
for key, value in eval.items():
    print('***-'+key.upper()+'-***')
    for k, v in value.items():
        print(k + ': ' + str(round(v*100)) + '%')