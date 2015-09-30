import sys
from collections import Counter


def fast_histogram(array):
    """Returns a collections.Counter given an array"""
    return Counter(array)


def small_histogram(array):
    """Returns a list of lists"""
    hist = []
    for word in array:
        if not contains(word, hist):
            hist.append([word, 1])
        else:
            hist[getIndex(word, hist)][1] += 1
    return hist


def contains(item, list):
    """Checks if item is in list"""
    contains = False
    for x in list:
        if item == x[0]:
            contains = True
    return contains


def getIndex(item, list):
    """Returns index of item given list"""
    index = None
    for i in range(len(list)):
        if item == list[i][0]:
            index = i
    return index

if __name__ == "__main__":
    args = sys.argv[1:]
    lists = list(x.split(' ') for x in args)
    array = list(y for x in lists for y in x)
    print(fast_histogram(array))
    print(small_histogram(array))
