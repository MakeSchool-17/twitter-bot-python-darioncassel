import sys
import random


def main(num):
    with open('/usr/share/dict/words') as file:
        words = file.readlines()
        for x in range(int(num)):
            rand = random.randint(0, len(words)-1)
            print(words[rand].split('\n')[0], end=" ")
        print()

if __name__ == "__main__":
    arg = sys.argv[1]
    main(arg)
