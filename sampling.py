import sys
import random
from frequency import histogram


def main(args):
    text = ' '.join(args)
    hist = histogram(text)
    num = random.randint(0, len(hist.keys())-1)
    return list(hist.keys())[num]


if __name__ == "__main__":
    args = sys.argv[1:]
    print(main(args))
