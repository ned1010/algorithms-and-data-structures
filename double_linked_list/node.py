class Node:
    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node
    
    def get_value(self):
        return self.value
    
    def get_prev_node(self):
        return self.prev_node
    
    def get_next_node(self):
        return self.next_node
    
    def set_prev_node(self, new_prev_node):
        self.prev_node = new_prev_node
    
    def set_next_node(self, new_next_node):
        self.next_node = new_next_node

# a = Node(5)
# b = Node(6)
# c = Node(7)

# a.set_next_node(b)
# b.set_prev_node(a)
# b.set_next_node(c)
# c.set_prev_node(b)
# print(c.get_prev_node().get_value())