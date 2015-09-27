import sys
import random


# arr is an array of strings
def main(arr):
    shuffle(arr)
    return ' '.join(str(x) for x in arr)


def shuffle(array):
    for i in range(len(array)):
        j = random.randint(0, len(array)-1)
        array[i] = array[j]

if __name__ == "__main__":
    result = main(sys.argv[1:])
    print(result)
