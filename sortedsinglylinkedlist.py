class SortedSinglyLinkedList:

    def __init__(self, array):
        self.head = None
        self.last_node = None
        self.length = 0
        for data in array:
            index = self.index_of(data)
            if index is None:
                node = Node(data)
                self.insert(node)
            else:
                self.update(index)
        self.length = len(self)

    def insert(self, node):
        """Inserts node at correct (sorted) position

        Params: node - node to be inserted
        Node -> ()
        """
        if not self.head:
            node.next_node = self.last_node
            self.head = node
        elif self.head and not self.last_node:
            if self.head.data < node.data:
                self.head.next_node = node
                self.last_node = node
            else:
                self.last_node = self.head
                node.next_node = self.last_node
                self.head = node
        else:
            index = 0
            current_node = self.head
            added = False
            while current_node:
                if node.data < current_node.data:
                    self.insert_before(index, node)
                    added = True
                    break
                current_node = current_node.next_node
                index += 1
            if not added:
                self.append(node)

    def insert_after(self, index, node):
        """Inserts node after current node at Index

        Params: index - index to insert after
                node - node to insert

        int, Node -> ()
        """
        current_node = self[index]
        next_node = current_node.next_node
        current_node.next_node = node
        node.next_node = next_node

    def insert_before(self, index, node):
        """Inserts node before current node at Index

        Params: index - index to insert before
                node - node to insert

        int, Node -> ()
        """
        current_node = self[index]
        if current_node == self.head:
            self.head = node
            node.next_node = current_node
        else:
            previous_node = self[index-1]
            previous_node.next_node = node
            node.next_node = current_node

    def append(self, node):
        """Appends node to end of self

        Params: node - Node to append
        Node -> ()
        """
        # head and last node
        if self.head and self.last_node:
            self.last_node.next_node = node
            self.last_node = node
        # head but no last node
        elif self.head:
            self.head.next_node = node
            self.last_node = node
        # no head
        else:
            node.next_node = self.last_node
            self.head = node

    def getNode(self, data):
        """returns node given data

        Params: data - key of node
        str -> Node
        """
        index = 0
        node = self.head
        while index < self.length:
            if node.data == data:
                return node
            if node.next_node:
                node = node.next_node
                index += 1

    def index_of(self, data):
        """Returns index of node

        Params: data - key of node
        str -> (str -> int)
        """
        return self.binary_search(data)

    def binary_search(self, data):
        """Binary search through tree

        Params: data - key of Node
        str -> int
        """
        found = False
        low = 0
        high = self.length-1
        if self.length == 0:
            found = True
        while not found:
            midpoint = int((low+high)/2)
            if data == self[midpoint].data:
                found = True
                return midpoint
            elif data > self[midpoint].data:
                low = midpoint + 1
            else:
                high = midpoint

    def update(self, index):
        """Increases counter of node at index"""
        self[index].count += 1

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
            nodes += "[{}, {}]".format(node.data, node.count)
        return nodes + "]"


class Node:

    def __init__(self, data=None):
        self.data = data
        self.count = 1
        self.next_node = None
