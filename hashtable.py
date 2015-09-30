class HashTable:

    def __init__(self, array):
        self.keys = []
        self.vals = []
        self.length = 0
        self.length = len(array)
        self.vals = [None] * self.length
        for key in array:
            if key in self.keys:
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
        return self.vals[index].find(key).val

    def set(self, key, val):
        """Sets key to val (linkedlist.appends to linkedlist at bucket)

        * Should be called iff key not in keys
        str, int -> ()
        """
        index = self.index(key)
        if not self.vals[index]:
            self.vals[index] = LinkedList()
        self.vals[index].append(key)
        if key not in self.keys:
            self.keys.append(key)

    def update(self, key, val):
        """Finds index(bucket) of key and calls linkedlist.update

        * Should be called iff key is in keys
        str, int -> (str, int) -> ()
        """
        index = self.index(key)
        self.vals[index].update(key, val)

    def keys(self):
        return self.keys

    def __iter__(self):
        """Required for iterable"""
        for linkedlist in self.vals:
            if linkedlist:
                for node in linkedlist:
                    if node:
                        yield node

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
                self.length - number of nodes
        int, str -> int
        """
        return hash(key) % self.length

    def __len__(self):
        """Returns number of nodes

        () -> int
        """
        counter = 0
        for linkedlist in self.vals:
            if linkedlist:
                for node in linkedlist:
                    if node:
                        counter += 1
        return counter


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

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
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next_node
        return counter

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
