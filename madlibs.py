import sys
import random

text = open("paragraphs.txt").read()
arr = text.split("\n")


if __name__ == "__main__":
    print(len(arr))
