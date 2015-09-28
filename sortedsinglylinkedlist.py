class SortedSinglyLinkedList:

    head = None
    last_node = None
    length = 0

    def __init__(self, array):
        self.head = None
        self.last_node = None
        for data in array:
            index = self.index_of(data)
            if index is None:
                node = Node(data)
                self.insert(node)
            else:
                self.update(index)
        self.length = len(self)

    # insert at correct (sorted) position
    def insert(self, node):
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

    # insert node at index after current node there
    def insert_after(self, index, node):
        current_node = self[index]
        next_node = current_node.next_node
        current_node.next_node = node
        node.next_node = next_node

    # insert node at index before current node there
    def insert_before(self, index, node):
        current_node = self[index]
        if current_node == self.head:
            self.head = node
            node.next_node = current_node
        else:
            previous_node = self[index-1]
            previous_node.next_node = node
            node.next_node = current_node

    # appends node to end of list
    def append(self, node):
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

    # returns index of node given data
    def index_of(self, data):
        return self.binary_search(data)

    def binary_search(self, data):
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

    # increases counter of node at index
    def update(self, index):
        self[index].count += 1

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
            nodes += "[{}, {}]".format(node.data, node.count)
        return nodes + "]"


class Node:

    data = None
    count = 1
    next_node = None

    def __init__(self, data):
        self.data = data
