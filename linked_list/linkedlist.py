from node import Node

class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node
    
    def get_head_node(self):
        return self.head_node 

    def add_node_heading(self, value_add):
        new_node = Node(value_add)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node


    def remove_node(self, remove_value):
        current_node = self.head_node

        if current_node.get_value() == remove_value:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == remove_value:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None  
                else:
                    current_node = next_node
    
    def print_list(self):
        result = ""
        current_node = self.head_node

        while current_node:
            if current_node.get_value() != None:
                result += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
        return result

# a = LinkedList()

# for i in range(10):
#     a.add_node_heading(i)

# print(a.print_list())

# a.remove_node(5)

# print(a.print_list())