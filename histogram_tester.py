import timeit
import random
from flatassociativearray import FlatAssociativeArray
from sortedsinglylinkedlist import SortedSinglyLinkedList
from doublylinkedlist import DoublyLinkedList
from binarysearchtree import BinarySearchTree
from hashtable import HashTable


# analysis: O(n), benchmark: O(n)
def test_tuple_list(word, words):
    frequency = words.getValue(words)
    return frequency


# analysis: O(n), benchmark: O(n)
def test_ssll(word, words):
    frequency = words.getNode(word).count
    return frequency


# analysis: O(n), benchmark: O(n)
def test_dll(word, words):
    frequency = words[words.index_of(word)].count
    return frequency


# analysis: O(log(n)), benchmark: O(log(n))
def test_bst(word, words):
    frequency = words.binary_search(words.root_node, word)
    return frequency


# analysis: O(1), benchmark: O(n)
def test_hashtable(word, words):
    frequency = words.get(word)
    return frequency


def dict_list(length):
    """Generates a list of length dictionary words

    int -> array
    """
    dict_words = '/usr/share/dict/words'
    words_str = open(dict_words, 'r').read()
    all_words = words_str.split("\n")
    words = all_words[0:length]
    random.shuffle(words)
    return words


def hgram_generate(struct, size):
    """Generates a histogram

    Params: struct - data structure
            size - size of dictionary words to generate
    ___, int -> :histogram
    """
    hgram = struct(dict_list(size))
    return hgram


def benchmark(struct, function, size):
    """Runs a benchmark

    Params: struct - data structure
            function - function (lookup) to test
            size - size of dictionary words to generate
    ___, (str, array -> int), int -> float
    """
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
    return timer.timeit(number=1)

if __name__ == "__main__":

    # FAA 100: 0.027061045599912178
    print("FAA 100: " +
          str(benchmark(FlatAssociativeArray, test_tuple_list, 100)))
    # FAA 1000: 0.12729319000209216
    print("FAA 1000: " +
          str(benchmark(FlatAssociativeArray, test_tuple_list, 1000)))
    # FAA 10000: 8.47697632299969
    print("FAA 10000: " +
          str(benchmark(FlatAssociativeArray, test_tuple_list, 10000)))
    # SSLL 100: 0.02705211373995553
    print("SSLL 100: " +
          str(benchmark(SortedSinglyLinkedList, test_ssll, 100)))
    # SSLL 1000: 0.1555812309961766
    print("SSLL 1000: " +
          str(benchmark(SortedSinglyLinkedList, test_ssll, 1000)))
    # SSLL 10000: 14.267478120993474
    print("SSLL 10000: " +
          str(benchmark(SortedSinglyLinkedList, test_ssll, 10000)))
    # DLL 100: 0.0305517836299623
    print("DLL 100: " +
          str(benchmark(DoublyLinkedList, test_dll, 100)))
    # DLL 1000: 0.11440823299926706
    print("DLL 1000: " +
          str(benchmark(DoublyLinkedList, test_dll, 1000)))
    # DLL 10000: 3.3517625449894695
    print("DLL 10000: " +
          str(benchmark(DoublyLinkedList, test_dll, 10000)))
    # BST 100: 0.027463051750310115
    print("BST 100: " +
          str(benchmark(BinarySearchTree, test_bst, 100)))
    # BST 1000: 0.03592572700290475
    print("BST 1000: " +
          str(benchmark(BinarySearchTree, test_bst, 1000)))
    # BST 10000: 0.11101376298756804
    print("BST 10000: " +
          str(benchmark(BinarySearchTree, test_bst, 10000)))
    # HT 100: 0.026284409992513247
    print("HT 100: " +
          str(benchmark(HashTable, test_hashtable, 100)))
    # HT 1000: 0.050136938007199205
    print("HT 1000: " +
          str(benchmark(HashTable, test_hashtable, 1000)))
    # HT 10000: 1.7139951350109186
    print("HT 10000: " +
          str(benchmark(HashTable, test_hashtable, 10000)))
