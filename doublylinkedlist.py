class DoublyLinkedList:

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
                self.append(node)
            else:
                self.update(index)
        self.length = len(self)

    # appends node to end of list
    def append(self, node):
        # head and last node
        if self.head and self.last_node:
            self.last_node.next_node = node
            node.previous_node = self.last_node
            self.last_node = node
        # head but no last node
        elif self.head:
            self.head.next_node = node
            node.previous_node = self.head
            self.last_node = node
        # no head
        else:
            node.next_node = self.last_node
            self.head = node

    # returns index of node given data
    def index_of(self, data):
        for index in range(self.length):
            if self[index].data == data:
                return index

    # increases counter of node at index
    def update(self, index):
        self[index].count += 1

    # remove node at index
    def remove(self, index):
        current_node = self[index]
        next_node = current_node.next_node
        previous_node = current_node.previous_node
        if current_node == self.head:
            self.head = next_node
            next_node.previous_node = None
            current_node = None
        else:
            previous_node.next_node = next_node
            next_node.previous_node = previous_node
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
    previous_node = None
    next_node = None

    def __init__(self, data):
        self.data = data
