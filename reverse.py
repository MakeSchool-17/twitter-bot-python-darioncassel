import sys


def reverse(str):
    """Reverses a string

    string -> string
    """
    arr = list(str)
    arr.reverse()
    return ''.join(arr)


if __name__ == "__main__":
    args = ' '.join(sys.argv[1:])
    print(reverse(args))
