class DoublyLinkedList:

    def __init__(self, array):
        self.head = None
        self.last_node = None
        self.length = 0
        for data in array:
            index = self.index_of(data)
            if index is None:
                node = Node(data)
                self.append(node)
            else:
                self.update(index)
        self.length = len(self)

    def append(self, node):
        """Appends node to end of self

        Params: node - Node to append
        Node -> ()
        """
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

    def index_of(self, data):
        """Returns index of node given data

        Params: data - 'key' of the node
        str -> int
        """
        for index in range(self.length):
            if self[index].data == data:
                return index

    def update(self, index):
        """increases counter of node at index

        int -> ()
        """
        self[index].count += 1

    def remove(self, index):
        """Remove node at index

        int -> ()
        """
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
        self.previous_node = None
        self.next_node = None
