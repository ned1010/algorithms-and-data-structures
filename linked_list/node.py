class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    def get_next_node(self):
        return self.link_node
    
    def set_next_node(self, next_node):
        self.link_node = next_node

    def get_value(self):
        return self.value

# a = Node(5)
# b = Node(3)
# c = Node(10)

# b.set_next_node(a)
# c.set_next_node(b)
# a_data = b.get_next_node().get_value()
# print(a_data)
# print(a.get_next_node())