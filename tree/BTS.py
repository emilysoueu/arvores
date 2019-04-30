#Binary Search Tree in Python

class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

    def insert(self,data):
        if self.value == data
            return False
        elif self.value > data:
            if self.left:
                return self.left = Node(data)
        else:
            self.right = Node(data)
            return True

class Tree:
    def __init__(self):
        self .root = None

    def insert (self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.value == data:
            return True
        elif data > self.Node(data):
            find(self.left(data))
        else:
            find(self.right(data))


     