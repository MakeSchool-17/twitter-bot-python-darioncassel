from sortedsinglylinkedlist import SortedSinglyLinkedList
from random import randint
import re


class MarkovModel:

    def __init__(self):
        self.pointers = {}

    def train(self, words, n):
        """Train the corpus on a list with n look-back

        Params: words - list of strings to train on
                n - look-back length
        [string], int -> ()
        """
        words_length = len(words)-1-n
        for index in range(words_length):
            current_words = ""
            next_words = ""
            for i in range(n):
                # if at last index don't append a space
                if i == n-1:
                    current_words += words[index+i]
                    next_words += words[index+i+1]
                else:
                    current_words += words[index+i] + " "
                    next_words += words[index+i+1] + " "
            if not next_words.split(" ")[-1] == current_words.split(" ")[-1]:
                # if current_words doesn't have a SSLL indexed to it
                if not self.pointers.get(current_words, None):
                    self.pointers[current_words] = None
                    heap = SortedSinglyLinkedList()
                    heap.insert(next_words)
                    self.pointers[current_words] = heap
                else:
                    heap = self.pointers[current_words]
                    heap.insert(next_words)

    def random_walk(self, length):
        """Walk the Markov model with weighted random selection

        Params: length - number of words to select
        int -> [string]
        """
        num = randint(0, len(self.pointers)-1)
        keys = list(self.pointers.keys())
        current_words = keys[num]
        result = ""
        while length > 0:
            # append the last word
            result += current_words.split(" ")[-1] + " "
            current_words = self.pointers.get(current_words, None)
            if current_words:
                current_words = self.weighted_select(current_words).data
                length -= 1
            else:
                length = -1
        # Extract full sentences from text
        # (begins with a capital letter, ends with punctuation)
        regex = re.compile(r'[A-Z][^\.!\?]*[\.!\?]+')
        sentences = regex.findall(result)
        return sentences

    def weighted_select(self, hist):
        """Selects a element from a histogram taking frequency
        into account

        dictionary -> string
        """
        length = len(hist)
        num = randint(0, length)
        for word in hist:
            num -= word.count
            if num <= 0:
                return word
