import sys
import re


def tokenize(file_name):
    """Converts text file to list of tokens

    Params: file_name - file to tokenized
    str -> list
    """
    tokens = []
    with open(file_name) as file:
        words = file.split(" ")
        for word in words:
            tokens.append[word]
    return tokens

if __name__ == "__main__":
    file_name = sys.argv[1]
    print(tokenize(file_name))
