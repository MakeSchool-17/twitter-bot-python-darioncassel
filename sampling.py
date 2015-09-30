import sys
import random
from frequency import histogram


def unweighted_select(hist):
    """Selects a random element from a dictionary's keys

    dictionary -> string
    """
    num = random.randint(0, len(hist.keys())-1)
    print(len(hist.keys()))
    return list(hist.keys())[num]


def weighted_select(hist):
    """Selects a element from the histogram taking frequency
    into account

    dictionary -> string
    """
    length = sum(hist[word] for word in hist.keys())
    num = random.randint(0, length)
    for word in hist:
        num -= hist[word]
        if num <= 0:
            return word


def test_probability(hist):
    """Checks to see if the weighted_select has a
    non-uniform selection probability; returns a dictionary
    mapping keys to probabilities

    dictionary -> dictionary
    """
    keys = {}
    for key in hist.keys():
        keys[key] = 0
    for i in range(10000):
        key = weighted_select(hist)
        keys[key] += 1
    for key in keys:
        keys[key] = keys[key]/10000
    return keys

if __name__ == "__main__":
    args = sys.argv[1:]
    text = ' '.join(args)
    hist = histogram(text)
    print(test_probability(hist))
