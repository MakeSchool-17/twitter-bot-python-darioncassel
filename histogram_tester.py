import timeit
from flatassociativearray import FlatAssociativeArray
from sortedsinglylinkedlist import SortedSinglyLinkedList


# analysis: O(n), benchmark: O(n)
def test_tuple_list(word, words):
    frequency = words.getValue(words)
    return frequency


# analysis: O(n), benchmark: O(n)
def test_ssll(word, words):
    frequency = words[words.index_of(word)].count
    return frequency


def dict_list(length):
    dict_words = '/usr/share/dict/words'
    words_str = open(dict_words, 'r').read()
    all_words = words_str.split("\n")
    return all_words[0:length]


def hgram_generate(struct, size):
    hgram = struct(dict_list(size))
    return hgram


def benchmark(struct, function, size):
    words = dict_list(size)
    hsearch = words[-1]
    setup = "from {} import {}; \
        from __main__ import {}, hgram_generate".format(
            struct.__name__.lower(), struct.__name__, function.__name__)
    test = "{}('{}', hgram_generate({}, {}))".format(function.__name__,
                                                     hsearch,
                                                     struct.__name__,
                                                     size)
    timer = timeit.Timer(test, setup=setup)
    num = 0
    sum = 0
    for x in range(1000):
        sum += timer.timeit(number=1)
        num += 1
    return sum/num

if __name__ == "__main__":

    # FAA 100: 0.027061045599912178
    print(benchmark(FlatAssociativeArray, test_tuple_list, 100))
    # FAA 1000: 0.11650251239971113
    print(benchmark(FlatAssociativeArray, test_tuple_list, 1000))
    # SSLL 100: 0.02705211373995553
    print(benchmark(SortedSinglyLinkedList, test_ssll, 100))
    # SSLL 1000: 0.11500938755001698
    print(benchmark(SortedSinglyLinkedList, test_ssll, 1000))
