class BinarySearchTree:

    root_node = None

    def __init__(self, array):
        self.root_node = Node(None)
        for key in array:
            self.insert(self.root_node, key)

    # recursive insertion with in-place count updating
    def insert(self, current_node, key):
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

    # in-order traversal
    def traverse_print(self, node):
        left = node.child_left
        right = node.child_right
        if left.key or right.key:
            if left.key:
                self.traverse(left)
            print(node.key)
            if right.key:
                self.traverse(right)
        else:
            print(node.key)

    # in-order traversal
    def traverse_print_root(self):
        self.traverse_print(self.root_node)

    # in-order iteration
    def __iter__(self):
        node = self.traverse(self.root_node)
        while node:
            return node

    # in-order traversal
    def traverse(self, node):
        left = node.child_left
        right = node.child_right
        if left.key or right.key:
            if left.key:
                self.traverse(left)
            yield node
            if right.key:
                self.traverse(right)
        else:
            yield node

    def __getitem__(self, index):
        return self.traverse_to(self.root_node, index)

    # in-order traversal to index
    def traverse_to(self, node, index):
        counter = 1
        while counter <= index:
            left = node.child_left
            right = node.child_right
            if left.key or right.key:
                if left.key:
                    counter += self.traverse_to(left, index)
                if right.key:
                    counter += self.traverse_to(right, index)
            #else:
                #yield node
            yield counter
        return node

    def __len__(self):
        return self.length(self.root_node)

    def length(self, node):
        counter = 1
        if node.child_left.key:
            counter += self.length(node.child_left)
        if node.child_right.key:
            counter += self.length(node.child_right)
        return counter

    def __str__(self):
        pass


class Node:

    key = None
    value = 1
    child_left = None
    child_right = None

    def __init__(self, key):
        self.key = key
