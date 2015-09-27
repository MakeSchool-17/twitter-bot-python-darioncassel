import timeit
from flatassociativearray import FlatAssociativeArray


# analysis: O(n), benchmark: O(n)
def test_tuple_list(word, words):
    tuple_list = FlatAssociativeArray(words)
    frequency = tuple_list.getValue(words)
    return frequency


def dict_list(length):
    dict_words = '/usr/share/dict/words'
    words_str = open(dict_words, 'r').read()
    all_words = words_str.split("\n")
    return all_words[0:length]


def hgram_generate(struct, size):
    words = dict_list(size)
    hgram = struct(words)
    return hgram


def benchmark(struct, function, size):
    hgram = hgram_generate(struct, size)
    hsearch = hgram[-1]
    test = "{}('{}', hgram_generate({}, {}))".format(function.__name__,
                                                     hsearch, struct.__name__,
                                                     size)
    setup = "from flatassociativearray import FlatAssociativeArray; \
        from __main__ import {}, hgram_generate".format(function.__name__)
    timer = timeit.Timer(test, setup=setup)
    iterations = 1
    result = timer.timeit(number=iterations)
    return result

if __name__ == "__main__":

    # FAA 100: 0.02784024599532131
    print(benchmark(FlatAssociativeArray, test_tuple_list, 100))
    # FAA 1000: 0.20183217800513376
    print(benchmark(FlatAssociativeArray, test_tuple_list, 1000))
