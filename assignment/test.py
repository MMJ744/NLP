import nltk
from os import listdir
from os.path import isfile, join
path = '/Users/Matthew/AppData/Roaming/nltk_data/corpora'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
corpus_root = path + '/untagged'
corpus = nltk.corpus.reader.plaintext.PlaintextCorpusReader(corpus_root, onlyfiles)

