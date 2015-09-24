import sys
import random


# arr is an array of string literals
def main(arr):
    random.shuffle(arr)
    return ' '.join(str(x) for x in arr)


if __name__ == "__main__":
    result = main(sys.argv[1:])
    print(result)
