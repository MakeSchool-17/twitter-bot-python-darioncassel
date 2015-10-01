class BinaryHeap:

    def __init__(self):
        self.root = Node()

    def peek(self):
        """Returns the root node as a tuple

        () -> (str, int)
        """
        return (self.root.key, self.root.val)

    def insert(self, data):
        """Wrapper method for insert to start
        at the root

        Params: data - (key, val) to insert
        () -> ()
        """
        self.__insert(self.root, data)

    def delete_max(self):
        """Wrapper method for delete_max to start
        at the root

        () -> ()
        """
        self.__delete_max(self.root)

    def __delete_max(self, node):
        """Delete the given node in-place

        Params: node - node to delete
        Node -> ()
        """
        data = (None, None)
        self.__set(node, data)
        data_left = (node.left.key, node.left.val)
        data_right = (node.right.key, node.right.val)
        if node.left.val and node.right.val:
            if node.left.val > node.right.val:
                self.insert(data_left)
                self.__delete_max(node.left)
            else:
                self.insert(data_right)
                self.__delete_max(node.right)

    def __insert(self, current_node, data):
        """Inserts node at balanced position

        Params: data - (key, val) tuple

        (str, int) -> ()
        """
        if not current_node.key or data[1] > current_node.val:
            self.__replace(current_node, data)
        else:
            if current_node.dir:
                self.__insert(current_node.left, data)
                current_node.dir = False
            else:
                self.__insert(current_node.right, data)
                current_node.dir = True

    def __replace(self, node, data):
        """Replaces node with data and inserts
        node1's data into the tree

        Params: node - node to replace
                data - (key, val) to replace with
        * node should have a smaller val than data[1]
        Node, (str, int) -> ()
        """
        data1 = (node.key, node.val)
        self.__set(node, data)
        if data1[0] and data1[1]:
            self.__insert(node, data1)

    def __set(self, node, data):
        """Sets node to key, val

        Node, str, int -> ()
        """
        node.key = data[0]
        node.val = data[1]
        if not node.left:
            node.left = Node()
        if not node.right:
            node.right = Node()

    def __str__(self):
        """Wrapper for to_str

        () -> () -> str
        """
        return self.to_str(self.root)

    def to_str(self, node, depth=0):
        ret = ""
        # Print right branch
        if node.right:
            ret += self.to_str(node.right, depth + 1)
        # Print own value
        ret += "\n" + ("         "*depth) + str(node)
        # Print left branch
        if node.left:
            ret += self.to_str(node.left, depth + 1)
        return ret


class Node:

    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.dir = False

    def __str__(self):
        return "({}, {})".format(self.key, self.val)
