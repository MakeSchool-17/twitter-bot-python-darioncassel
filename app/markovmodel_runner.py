from markovmodel import MarkovModel
from tokenize import tokenize
import pickle
import sys


def run(c, n, length):
    """Run a Markov model given a corpus version and a look-back

    Params: c - corpus version
            n - lookback
            length - number of words to generate
    int, int -> string
    """
    # set to 100,000 to avoid max recursion depth exceeded error
    sys.setrecursionlimit(100000)
    words = tokenize("corpus/clean_corpus_{}.txt".format(c))
    model = None
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
    sentences = model.random_walk(length)
    paragraph = ""
    for sentence in sentences:
        paragraph += sentence + " "
    return paragraph

if __name__ == "__main__":
    print(run(5, 4, 300))
