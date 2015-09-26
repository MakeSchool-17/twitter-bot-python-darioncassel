import sys
from collections import Counter


def fast_histogram(array):
    hist = Counter()
    for word in array:
        hist[word] += 1
    return hist


def small_histogram(array):
    hist = []
    for word in array:
        if not contains(word, hist):
            hist.append([word, 1])
        else:
            hist[getIndex(word, hist)][1] += 1
    return hist


def contains(item, list):
    contains = False
    for x in list:
        if item == x[0]:
            contains = True
    return contains


def getIndex(item, list):
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
