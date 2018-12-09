from gensim.models import Word2Vec

model = Word2Vec.load_word2vec_format( '/Users/Matthew/GoogleNews-vectors-negative300.bin', binary=True)
print(model.similarity( 'AI', 'neural' ))
ontology = {'arts': {'history': {'words': [], 'ids': set()}},
            'science': {'computer science': {'words': [], 'ids': set(), 'ai': {'words': [], 'ids': set()}}}
            }