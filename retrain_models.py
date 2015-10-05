from markovmodel import MarkovModel
from tokenize import tokenize
import pickle
import sys


if __name__ == "__main__":
    # set to 100,000 to avoid max recursion depth exceeded error
    sys.setrecursionlimit(100000)
    mapping = {
        1: [1, 2, 3, 4, 5, 6, 7],
        2: [2, 3, 4, 5],
        3: [2, 3],
        4: [1, 2, 3, 4, 5, 6],
        5: [1, 2, 3, 4]
    }
    # c = Corpus version number
    # n = lookback
    for c in list(mapping.keys()):
        for n in mapping[c]:
            words = tokenize("corpus/clean_corpus_{}.txt".format(c))
            # clear file, train model and pickle it
            open("models/trained_model{}_{}.p".format(c, n), 'wb').close()
            with open("models/trained_model{}_{}.p".format(c, n), "wb") \
                    as file:
                model = MarkovModel()
                model.train(words, n)
                pickle.dump(model, file)
