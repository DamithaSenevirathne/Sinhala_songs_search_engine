import pandas as pd
import numpy as np
from gensim import models
from gensim.models import Word2Vec
from gensim.models import FastText

sent= pd.read_excel('vocab.csv')

def saveModel(model,name):
    model.save(name)

def giveMostSimilar(query):

    # model shows us better results
    model = FastText(min_count=1,
                        window=2,
                        size=80,
                        sample=6e-5, 
                        alpha=0.03, 
                        min_alpha=0.0007,
                        workers=5)  # instantiate
    model.build_vocab(sent)
    model.train(sent, total_examples=len(sent), epochs=10000)

    most_similar = model.wv.most_similar(query)

    return query

