import nltk
from nltk.corpus import brown
from nltk.corpus.reader import WordListCorpusReader
reader = WordListCorpusReader('', ['computerscience.txt'])
words = [nltk.word_tokenize(i) for i in reader.words()]
words2 = []
for s in reader.words():
    for i in s:
        words2.append(i)
tokens = [nltk.word_tokenize(i) for i in words2]
from nltk.stem.porter import *
stemmer = PorterStemmer()
from nltk.stem import WordNetLemmatizer
lemmer = WordNetLemmatizer()

stemmed = [[stemmer.stem(y) for y in i] for i in words]
lemmed = [[lemmer.lemmatize(y) for y in i] for i in words]


stemmed2 = [stemmer.stem(i) for i in tokens]
lemmed2 = [lemmer.lemmatize(i) for i in tokens]

print(stemmed2)
