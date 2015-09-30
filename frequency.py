
def histogram(source_text):
    """Given a string, creates a histogram with
    Python's dictionary

    str -> dictionary
    """
    words = source_text.split(' ')
    result = {}
    for word in words:
        if word in result.keys():
            result[word] = result[word] + 1
        else:
            result[word] = 1
    return result


def histogram_tuple(source_text):
    """Given a string, creates a histogram with
    a basic flat associative array

    str -> [tuple]
    """
    words = source_text.split(' ')
    result = []
    for word in words:
        contains = False
        index = 0
        for x in range(len(result)-1):
            if word == result[x][0]:
                contains = True
                index = x
        if not contains:
            entry = (word, 1)
            result.append(entry)
        else:
            result[index] = (word, result[index][1] + 1)
    return result


def unique_words(source_text):
    """Returns the number of unique words
    given a source string

    str -> int
    """
    words = source_text.split(' ')
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    return len(result)


def frequency(word, histogram):
    """Returns frequency of word given an interable histogram

    str, :histogram -> int
    """
    return histogram[word]

if __name__ == "__main__":
    text = open('paragraphs.txt').read()
    print(histogram_tuple(text))
    print(unique_words(text))
    print(frequency("of", histogram(text)))
