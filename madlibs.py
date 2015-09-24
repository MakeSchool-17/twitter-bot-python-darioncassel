import sys
import random
import nltk


def main():
    text = open("paragraphs.txt").read()
    paragraphs = text.split("\n")
    num = random.randint(0, len(paragraphs)-1)
    paragraph = text.split("\n")[num]
    words = paragraph.split(' ')
    for x in range(10):
        num = random.randint(0, len(words)-1)
        word = [words[num]]
        part = nltk.pos_tag(word)[0][1]
        #added comment
        words[num] = "__%w__" % part
    return ' '.join(words)


if __name__ == "__main__":
    print(main())
