import sys
import random


def main():
    text = open("paragraphs.txt").read()
    paragraphs = text.split("\n")
    num = random.randint(0, len(paragraphs))
    paragraph = text.split("\n")[num]
    words = paragraph.split(' ')
    for x in range(10):
        num = random.randint(0, len(words)-1)
        words[num] = "_____"
    return ' '.join(words)


if __name__ == "__main__":
    print(main())
