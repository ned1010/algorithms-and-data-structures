from node import Node
from linkedlist import LinkedList

def reverse(array):
    prev_node = None
    current_node = array.head_node
    next_node = array.get_next_node()
    while current_node:
        current_node.next_node = prev_node
        #moving the previous and current forward the list
        prev_node = current_node
        current_node = next_node 
    array.head_node = prev_node
    return array

b = LinkedList()
for i in range(10):
    b.add_node_heading(i)
print(b.print_list())
print(reverse(b))

