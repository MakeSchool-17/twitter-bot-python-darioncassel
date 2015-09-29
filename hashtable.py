class HashTable:

    def __init__(self, array):
        self.keys = []
        self.vals = []
        self.length = 0
        self.length = len(array)
        self.vals = [None] * self.length
        for key in array:
            if key in self.getKeys():
                self.update(key, self.get(key)+1)
            else:
                self.set(key, 1)

    # returns val of key
    def get(self, key):
        index = self.index(key)
        return self.vals[index].find(key).val

    def set(self, key, val):
        index = self.index(key)
        if not self.vals[index]:
            self.vals[index] = LinkedList()
        self.vals[index].append(key)
        if key not in self.keys:
            self.keys.append(key)

    def update(self, key, val):
        index = self.index(key)
        self.vals[index].update(key, val)

    def getKeys(self):
        return self.keys

    def getVals(self):
        array = []
        for linkedlist in self.vals:
            if linkedlist:
                for node in linkedlist:
                    if node:
                        array.append(node.val)
        return array

    # Generates vals index from key
    # params: length of key array, key string
    # (int, str) -> int
    def index(self, key):
        return hash(key) % self.length


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    # appends node to end of list
    def append(self, key):
        node = Node(key)
        # head and last node
        if self.head and self.tail:
            self.tail.next_node = node
            self.tail = node
        # head but no last node
        elif self.head:
            self.head.next_node = node
            self.tail = node
        # no head
        else:
            node.next_node = self.tail
            self.head = node

    # returns node given data
    def find(self, data):
        index = 0
        node = self.head
        while index < len(self):
            if node.data == data:
                return node
            if node.next_node:
                node = node.next_node
                index += 1

    # sets val of existing key
    def update(self, key, val):
        self.find(key).val = val

    # remove node at index
    def remove(self, index):
        current_node = self[index]
        if current_node == self.head:
            self.head = current_node.next_node
            current_node = None
        else:
            previous_node = self[index-1]
            previous_node.next_node = current_node.next_node
            del current_node

    # required for iterable
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_node

    # required for iterable
    def __getitem__(self, index):
        counter = 0
        node = self.head
        while counter < index:
            if node.next_node:
                node = node.next_node
                counter += 1
            else:
                print("Error: Index out of bounds")
                return None
        return node

    # define for len() to work
    def __len__(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next_node
        return counter

    # print the list
    def __str__(self):
        nodes = "["
        for node in self:
            nodes += "[{}, {}]".format(node.data, node.val)
        return nodes + "]"


class Node:

    def __init__(self, data=None):
        self.data = data
        self.val = 1
        self.next_node = None
