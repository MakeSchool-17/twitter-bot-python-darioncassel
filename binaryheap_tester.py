from binaryheap import BinaryHeap

if __name__ == "__main__":
    heap = BinaryHeap()
    data = [("dog", 1), ("cat", 2), ("bat", 3), ("slug", 1),
            ("rat", 4), ("mule", 3), ("fish", 2), ("goat", 5)]
    for x in data:
        heap.insert(x)
    print("-"*50)
    print(heap)
    print("-"*50)
