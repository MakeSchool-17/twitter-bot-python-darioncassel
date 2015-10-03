from markovmodel import MarkovModel
from tokenize import tokenize
import pickle
import sys


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    words = tokenize("clean_corpus.txt")
    model = None
    with open("trained_model_2.p", "rb") as file:
        if len(list(file.peek())) > 0:
            model = pickle.load(file)
    if not model:
        with open("trained_model_2.p", "wb") as file:
            model = MarkovModel()
            model.train(words, 1)
            pickle.dump(model, file)
    inp = input("Len: ")
    while input != 0:
        print(model.random_walk(int(inp)))
        inp = input("Len: ")
