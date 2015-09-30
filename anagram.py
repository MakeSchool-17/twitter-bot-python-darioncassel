import sys
import random
from collections import Counter


# This is word in progress code;
# it works but not efficiently


def load_dictionary():
    """Loads the dictionary but strips all single letter
    entries except 'a' and 'i'

    () -> array
    """
    with open('/usr/share/dict/words') as file:
        arr = file.readlines()
        dict = {}
        for word in arr:
            word = word.split('\n')[0].lower()
            if len(word) == 1:
                if word == "a" or word == "i":
                    chars = Counter(word)
                    dict[word] = chars
            if len(word) > 1:
                chars = Counter(word)
                dict[word] = chars
        return dict


def main(args, dic):
    """Preforms subset matching for each word in dictionary
    to user supplied words

    Params: args - sys argsv[1:]
            dic - dictionary from load_dictionary()
    (array, array) -> str
    """
    char_array = prepare_char_array(args)
    failure = True
    while failure:
        arr = Counter(char_array)
        words = []
        while len(arr) > 0:
            saved_arr = arr.copy()
            keys = list(dic.keys())
            random.shuffle(keys)
            for x in keys:
                if sum(dic[x].values()) <= sum(arr.values())\
                        and is_subset(dic[x], arr):
                    words.append(x)
                    arr -= dic[x]
            if len(arr) == 0:
                failure = False
                print(' '.join(words))
            if arr == saved_arr:
                arr.clear()


def is_subset(this, other):
        """Checks that one array is a proper subset of the other

        params: This - being checked against
                Other -
        (array, array) -> bool
        """
        for char, count in this.items():
            if other[char] < count:
                return False
        return True


def prepare_char_array(args):
    """Given system arguments, convert to and return array of characters

    Params: args - sys argsv[1:]
    array -> array
    """
    str = ' '.join(args)
    char_array = list(str)
    for x in char_array:
        if x == ' ':
            char_array.remove(x)
    return char_array

if __name__ == "__main__":
    args = sys.argv[1:]
    dict = load_dictionary()
    main(args, dict)
