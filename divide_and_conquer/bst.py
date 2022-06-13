#binary search tree is special tree in which left-subtree always
#have values lesser than root/parent and right has greater than parent
import random
class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if (value < self.value):
            #if the left is empty add
            if (self.left is None):
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth +1}')
            else:
                #this would recursively called left until it founds an empty node
                self.left.insert(value)
        else:
            if (self.right is None):
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f"Tree node {value} added to the right of {self.value} at depth {self.depth +1}")
            else:
                #if calls recursively until leaf node is found to add new node
                self.right.insert(value)

    def search_node_by_value(self, value):
        if (self.value == value):
            return self
        elif (self.left is not None) and (value < self. value):
            self.left.search_node_by_value(value)
        elif (self.right is not None) and (value > self.value):
            self.right.search_node_by_value(value)
        else:
            return None
    def depth_first_traversal(self):
        if (self.left is not None):
            self.left.depth_first_traversal()
        print(f'Depth={self.depth}, value = {self.value}')
        if (self.right is not None):
            self.right.depth_first_traversal()

newBST = BinarySearchTree(10)

for i in range(10):
    newBST.insert(random.randint(0, 20))
print(newBST.depth_first_traversal())

