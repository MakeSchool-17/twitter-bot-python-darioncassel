from markovmodel import MarkovModel
from tokenize import tokenize
import pickle
import sys


if __name__ == "__main__":
    # set to 100,000 to avoid max recursion depth exceeded error
    sys.setrecursionlimit(100000)
    # c = Corpus version number
    c = 5
    words = tokenize("corpus/clean_corpus_{}.txt".format(c))
    model = None
    # n = lookback
    n = 3
    # if a model already exists load it
    with open("models/trained_model{}_{}.p".format(c, n), "rb") as file:
        if len(list(file.peek())) > 0:
            model = pickle.load(file)
    # if not, train one and pickle it
    if not model:
        with open("models/trained_model{}_{}.p".format(c, n), "wb") as file:
            model = MarkovModel()
            model.train(words, n)
            pickle.dump(model, file)
    inp = input("Len: ")
    # keep asking for length
    while input != 0:
        sentences = model.random_walk(int(inp))
        print(sentences)
        inp = input("Len: ")
