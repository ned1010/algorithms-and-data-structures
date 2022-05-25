from node import Node
from linkedlist import LinkedList

def find_middle(array):
    fast_pointer = array.head_node
    slow_pointer = array.head_node

    while fast_pointer:
        fast_pointer = fast_pointer.get_next_node()
        if fast_pointer:
            fast_pointer = fast_pointer.get_next_node()
            slow_pointer = slow_pointer.get_next_node()
    return slow_pointer.get_value()

b = LinkedList()

for i in range(11):
    b.add_node_heading(i)
print(b.print_list())
print(find_middle(b))