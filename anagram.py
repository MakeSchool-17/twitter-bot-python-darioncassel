import sys
import random
from collections import Counter


# This is word in progress code;
# it works but not efficiently


def load_dictionary():
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
        for char, count in this.items():
            if other[char] < count:
                return False
        return True


def prepare_char_array(args):
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
