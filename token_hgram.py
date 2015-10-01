import sys
from tokenize import tokenize
from hashtable import HashTable
from sampling import weighted_select


def main(file_name):
    words = []
    hgram = generate_hgram(file_name)
    for i in range(7):
        word = weighted_select(hgram)
        words.append(word)
    return words


def generate_hgram(file_name):
    return HashTable(tokenize(file_name))

if __name__ == "__main__":
    file_name = sys.argv[1]
    print(main(file_name))
