from markovmodel import MarkovModel
from tokenize import tokenize
import pickle
import sys


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    # c = Corpus version number
    c = 3
    words = tokenize("clean_corpus_{}.txt".format(c))
    model = None
    # n = lookback
    n = 3
    with open("trained_model{}_{}.p".format(c, n), "rb") as file:
        if len(list(file.peek())) > 0:
            model = pickle.load(file)
    if not model:
        with open("trained_model{}_{}.p".format(c, n), "wb") as file:
            model = MarkovModel()
            model.train(words, n)
            pickle.dump(model, file)
    inp = input("Len: ")
    while input != 0:
        print(model.random_walk(int(inp)))
        inp = input("Len: ")
