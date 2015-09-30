import sys
import re

def parse(file_name):
    """Removes words from file in exclude

    Params: file_name - file to clean up
    Returns: string -  cleaned up file
    str -> str
    """
    cleaned_up = ""
    with open(file_name) as file:
        words = file.read().split(" ")
        for word in words:
            for item in exclude:
                word = re.sub(item, '', word)
                word = re.sub('([a-z])|([A-Z])\w+', '', word)
            cleaned_up += " " + word
    return cleaned_up

if __name__ == "__main__":
    file_name = sys.argv[1]
    print(parse(file_name))
