import sys
import random


def load_dictionary():
    arr = open('/usr/share/dict/words').readlines()
    dict = {}
    for word in arr:
        word = word.split('\n')[0].lower()
        if len(word) == 1:
            if word == "a" or word == "i":
                chars = set(word)
                dict[word] = chars
        if len(word) > 1:
            chars = set(word)
            dict[word] = chars
    return dict


def main(args, dict):
    str = ' '.join(args)
    char_array = list(str)
    for x in char_array:
        if x == ' ':
            char_array.remove(x)
    failure = True
    while failure:
        arr = set(char_array)
        words = []
        while len(arr) > 0:
            keys = list(dict.keys())
            random.shuffle(keys)
            for x in keys:
                if len(x) < len(arr) and dict[x].issubset(arr):
                    words.append(x)
                    for char in dict[x]:
                        arr.remove(char)
            if len(arr) == 0:
                failure = False
                print(' '.join(words))
            if len(arr) == 1:
                arr.clear()
                print(' '.join(words))

if __name__ == "__main__":
    args = sys.argv[1:]
    dict = load_dictionary()
    main(args, dict)
