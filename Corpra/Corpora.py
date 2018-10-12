import nltk
from nltk.corpus.reader import WordListCorpusReader
reader = WordListCorpusReader('', ['computerscience.txt'])
words = [nltk.word_tokenize(i) for i in reader.words()]
from nltk.stem.porter import *
stemmer = PorterStemmer()
from nltk.stem import WordNetLemmatizer
lemmer = WordNetLemmatizer()

stemmed = [[stemmer.stem(y) for y in i] for i in words]
lemmed = [[lemmer.lemmatize(y) for y in i] for i in words]

print(stemmed)
