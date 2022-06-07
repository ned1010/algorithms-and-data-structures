#Trees are hierarchical data structures.
class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.children = []

    def add_child(self, child_node):
        print("adding child", child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing" + child_node.value + "from" + self.value)
        self.children = [child for child in self.children if child is not child_node]
    def traverse(self):
        #putting all the values in list/queue structure to travel
        node_to_travel = [self]
        while (len(node_to_travel)) > 0:
            current_node = node_to_travel.pop()
            print(current_node.value)
            node_to_travel += current_node.children