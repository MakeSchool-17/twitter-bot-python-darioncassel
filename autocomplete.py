import sys
import re


def main(str):
    """Given an 'incomplete' string, prints a
        list of possible completions

    params: str - sys argv[1]
    str -> ()
    """
    with open('/usr/share/dict/words') as file:
        words = file.readlines()
        regex = '%s[a-z]*' % str
        search = re.compile(regex)
        for word in words:
            if search.match(word):
                print(word)

if __name__ == "__main__":
    arg = sys.argv[1]
    main(arg)
