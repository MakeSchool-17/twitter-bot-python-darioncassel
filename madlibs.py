import random
import nltk
from nltk.tag import map_tag


def main():
    """Selects a random paragraph from paragraphs.txt,
    and uses NLTK position tagging (excluding adp, conj
    det, and prt) to generate an interative madlibs
    dialog
    """
    exclude = ['ADP', 'CONJ', 'DET', 'PRT']
    text = open("paragraphs.txt").read()
    paragraphs = text.split("\n")
    num = random.randint(0, len(paragraphs)-1)
    paragraph = text.split("\n")[num]
    words = paragraph.split(' ')
    for x in range(5):
        num = random.randint(0, len(words)-1)
        word = [words[num]]
        part = nltk.pos_tag(word)
        simplePart = [(wor, map_tag('en-ptb', 'universal', tag))
                      for wor, tag in part][0][1]
        if simplePart not in exclude:
            print(simplePart)
            word = input()
            words[num] = "__%s__" % word
    print(' '.join(words))


if __name__ == "__main__":
    main()
