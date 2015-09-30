import sys

exclude = ['&#164;', '&#166;', '&#172;', '&#175;', '&#91;', '&#93;', '\n']


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
            if word not in exclude:
                cleaned_up += " " + word
    return cleaned_up

if __name__ == "__main__":
    file_name = sys.argv[1]
    print(parse(file_name))
