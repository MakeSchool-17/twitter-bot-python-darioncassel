import sys
import re

small_include = ['a', 'I', 'A']


def parse(file_name):
    """Removes words from file in exclude

    Params: file_name - file to clean up
    Returns: string -  cleaned up file
    str -> str
    """
    cleaned_up = ""
    with open(file_name) as file:
        words = file.read()
        regex = re.compile(r'\b[^\W\d_]+\b', flags=re.I)
        whole_words = regex.findall(words)
        for word in whole_words:
            if len(word) < 2:
                if word in small_include:
                    cleaned_up += word + " "
            else:
                cleaned_up += word + " "
    return cleaned_up

if __name__ == "__main__":
    file_name = sys.argv[1]
    result = parse(file_name)
    print(result)
