from math import log, pow


class HashTable:

    def __init__(self, array=None):
        self.key_list = set()
        self.vals = []
        if array:
            size = int(100*pow(log(len(array)), 2))
        else:
            size = 0
        self.buckets = max(1, size)
        self.vals = [None] * self.buckets
        self.length = 0
        if array:
            for key in array:
                if key in self.key_list:
                    self.update(key, self.get(key)+1)
                else:
                    self.set(key, 1)

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        """Returns value of a key

        str -> int
        """
        index = self.index(key)
        if self.vals[index]:
            return self.vals[index].find(key).val

    def set(self, key, val):
        """Sets key to val (linkedlist.appends to linkedlist at bucket)

        * Should be called iff key not in key_list
        str, int -> ()
        """
        index = self.index(key)
        if not self.vals[index]:
            self.vals[index] = LinkedList()
        self.vals[index].append(key)
        if key not in self.key_list:
            self.key_list.add(key)
        self.length += 1

    def update(self, key, val):
        """Finds index(bucket) of key and calls linkedlist.update

        * Should be called iff key is in key_list
        str, int -> (str, int) -> ()
        """
        index = self.index(key)
        self.vals[index].update(key, val)
        self.length += 1

    def keys(self):
        return self.key_list

    def __iter__(self):
        """Required for iterable"""
        for linkedlist in self.vals:
            if linkedlist:
                for node in linkedlist:
                    if node:
                        yield node.key

    def values(self):
        """Returns all the values in the hashtable

        () -> array
        """
        array = []
        for linkedlist in self.vals:
            if linkedlist:
                for node in linkedlist:
                    if node:
                        array.append(node.val)
        return array

    def index(self, key):
        """Generates vals index from key

        params: key - string
                self.buckets - number of nodes
        int, str -> int
        """
        return hash(key) % self.buckets

    def __len__(self):
        """Returns number of nodes

        () -> int
        """
        return self.length


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, key):
        """Appends node to end of self

        Params: key - key to append
        str -> ()
        """
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
        self.length += 1

    def find(self, key):
        """returns node given key

        str -> Node
        """
        index = 0
        node = self.head
        while index < len(self):
            if node.key == key:
                return node
            if node.next_node:
                node = node.next_node
                index += 1

    def update(self, key, val):
        """Sets val of existing key

        int -> ()
        """
        self.find(key).val = val

    def remove(self, index):
        """Remove node at index

        int -> ()
        """
        current_node = self[index]
        if current_node == self.head:
            self.head = current_node.next_node
            current_node = None
        else:
            previous_node = self[index-1]
            previous_node.next_node = current_node.next_node
            del current_node
        self.length -= 1

    def __iter__(self):
        """Required for iterable"""
        node = self.head
        while node:
            yield node
            node = node.next_node

    def __getitem__(self, index):
        """Required for iterable; returns Node at index

        int -> Node
        """
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

    def __len__(self):
        """Define for len() to work

        () -> int
        """
        return self.length

    def __str__(self):
        """Returns self as formatted string

        () -> str
        """
        nodes = "["
        for node in self:
            nodes += "[{}, {}]".format(node.key, node.val)
        return nodes + "]"


class Node:

    def __init__(self, key=None):
        self.key = key
        self.val = 1
        self.next_node = None
