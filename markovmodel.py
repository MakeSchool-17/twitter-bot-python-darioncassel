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
            next_word = ""
            for i in range(n):
                # if at last index don't append a space
                if i == n-1:
                    current_words += words[index+i]
                else:
                    current_words += words[index+i] + " "
            next_word = words[index+n]
            if not next_word == current_words.split(" ")[-1]:
                # if current_words doesn't have a SSLL indexed to it
                if not self.pointers.get(current_words, None):
                    self.pointers[current_words] = None
                    next_words = []
                    next_words.append(next_word)
                    self.pointers[current_words] = next_words
                else:
                    next_words = self.pointers[current_words]
                    next_words.append(next_word)

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
            current_words_list = current_words.split(" ")
            result += current_words_list[-1] + " "
            # compute n-lookback prefix
            key_prefix = " ".join(current_words_list[1:])
            if not key_prefix == "":
                key_prefix += " "
            current_words = self.pointers.get(current_words, None)
            if current_words:
                words_length = len(current_words)
                current_words = key_prefix + \
                    current_words[randint(0, words_length-1)]
                length -= 1
            else:
                length = -1
        # Extract full sentences from text
        # (begins with a capital letter, ends with punctuation)
        regex = re.compile(r'[A-Z][^\.!\?]*[\.!\?]+')
        sentences = regex.findall(result)
        return sentences
