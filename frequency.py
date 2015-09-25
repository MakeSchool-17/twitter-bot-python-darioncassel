
def histogram(source_text):
    words = source_text.split(' ')
    result = {}
    for word in words:
        if word in result.keys():
            result[word] = result[word] + 1
        else:
            result[word] = 1
    return result


def histogram_tuple(source_text):
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
    words = source_text.split(' ')
    result = []
    for word in words:
        if word not in result:
            result.append(word)
    return len(result)


def frequency(word, histogram):
    return histogram[word]

if __name__ == "__main__":
    text = open('paragraphs.txt').read()
    print(histogram_tuple(text))
    # print(unique_words(text))
    # print(frequency("of", histogram(text)))
