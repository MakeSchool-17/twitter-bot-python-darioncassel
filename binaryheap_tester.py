from binaryheap import BinaryHeap

if __name__ == "__main__":
    heap = BinaryHeap()
    data = [("dog", 1), ("cat", 2), ("bat", 3), ("slug", 1),
            ("rat", 4), ("mule", 3), ("fish", 2), ("goat", 5),
            ("fly", 3), ("snail", 4), ("bird", 6), ("fox", 2)]
    for x in data:
        heap.insert(x)
        print(heap)
        print("-"*50)
    print("-"*50)
    print(heap)
    print("-"*50)
    heap.delete_max()
    print(heap)
    print("-"*50)
    heap.delete_max()
    print(heap)
    print("-"*50)
