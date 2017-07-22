class Node(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


class BinaryTree(object):
    def __init__(self, value=None):
        self.root = Node(value)


    def insert_node(self, value):
        if self.root:

        else:
            self.root = value
