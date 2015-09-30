class BinarySearchTree:

    def __init__(self, array):
        self.root_node = Node(None)
        self.counter = 0
        for key in array:
            self.insert(self.root_node, key)

    def insert(self, current_node, key):
        """Recursive insertion with in-place count updating

        Params: current_node - node function is applied to
                key - to be inserted
        (Node, string) -> ()
        """
        if not current_node.key:
            current_node.key = key
            current_node.child_left = Node(None)
            current_node.child_right = Node(None)
        else:
            if key < current_node.key:
                self.insert(current_node.child_left, key)
            elif key == current_node.key:
                current_node.value += 1
            else:
                self.insert(current_node.child_right, key)

    def binary_search(self, node, key):
        """Recursively returns value of node given keys

        Params: node - current node function applied to
                key - key being searched for
        (Node, string) -> int
        """
        if key == node.key:
            return node.value
        elif key < node.key:
            self.binary_search(node.child_left, key)
        else:
            self.binary_search(node.child_right, key)

    def __iter__(self):
        """In-order iteration"""
        for index in range(len(self)):
            yield self[index]

    def __getitem__(self, index):
        """Returns item at index with in-order traversal

        int -> Node
        """
        self.counter = 0
        return self.traverse_to(self.root_node, index+1)

    def traverse_to(self, node, index):
        """In-order iteration to index

        params: node - curent Node
                index - in-order node to be returned
                counter - to track current index pos
        (Node, int) -> Node
        """
        condition = self.counter < index
        if condition:
            if node.child_left.key or node.child_right.key:
                pos1 = None
                pos2 = None
                if node.child_left.key and condition:
                    pos1 = self.traverse_to(node.child_left, index)
                self.counter += 1
                if self.counter == index:
                    return node
                if node.child_right.key and condition:
                    pos2 = self.traverse_to(node.child_right, index)
                return pos1 or pos2
            else:
                self.counter += 1
                if self.counter == index:
                    return node

    def __len__(self):
        """Returns length of self

        () -> int
        """
        return self.length(self.root_node)

    def length(self, node):
        """Returns length of tree

        Params: node - current nodes
        Node -> int
        """
        counter = 1
        if node.child_left.key:
            counter += self.length(node.child_left)
        if node.child_right.key:
            counter += self.length(node.child_right)
        return counter

    def __str__(self):
        nodes = ""
        for index in range(len(self)):
            node = self[index]
            nodes += "({}, {}) ".format(node.key, node.value)
        return nodes


class Node:

    def __init__(self, key=None):
        self.key = key
        self.value = 1
        self.child_left = None
        self.child_right = None
