import sys
from tokenize import tokenize
from hashtable import HashTable
from sampling import weighted_select


def main(file_name):
    """Returns seven words by weighted random selection
    from a histogram generated with the tokenized corpus

    Params: file_name - name of cleaned corpus file
    str -> list
    """
    words = []
    hgram = generate_hgram(file_name)
    for i in range(7):
        word = weighted_select(hgram)
        words.append(word)
    return words


def generate_hgram(file_name):
    """Returns a hashtable intialized with the tokenized
    corpus

    Params: file_name - name of cleaned corpus file
    str -> hashtable:Histogram
    """
    return HashTable(tokenize(file_name))

if __name__ == "__main__":
    file_name = sys.argv[1]
    print(main(file_name))
