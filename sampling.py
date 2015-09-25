import sys
import random
from frequency import histogram


def unweighted_select(hist):
    num = random.randint(0, len(hist.keys())-1)
    print(len(hist.keys()))
    return list(hist.keys())[num]


def weighted_select(hist):
    length = sum(hist[x] for x in hist.keys())
    num = random.randint(0, length)
    for x in hist:
        num = num - hist[x]
        if num <= 0:
            return x

if __name__ == "__main__":
    args = sys.argv[1:]
    text = ' '.join(args)
    hist = histogram(text)
    print(weighted_select(hist))
