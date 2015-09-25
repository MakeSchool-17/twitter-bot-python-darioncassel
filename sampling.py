import sys
import random
from frequency import histogram


def main(hist):
    num = random.randint(0, len(hist.keys())-1)
    print(len(hist.keys()))
    return list(hist.keys())[num]


if __name__ == "__main__":
    args = sys.argv[1:]
    text = ' '.join(args)
    hist = histogram(text)
    print(main(hist))
