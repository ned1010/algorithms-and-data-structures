from linkedlist import LinkedList
from node import Node

#naive method
def naive_find_nth_element(array, n):
    result = []
    current_node = array.head_node
    while current_node:
        result.append(current_node.get_value())
        current_node = current_node.get_next_node()
    return result[len(result) - n]
#two pointer method
#tail pointer and current_pointer
#tail pointer is points to head of the list and nth_pointer is None
#When the count is equal or greater than n+1, then check if nth_pointer is none
#nth pointer is none, then set it to head

def two_pointer_method(array, n):
    tail_pointer = array.head_node
    count = 0
    nth_pointer = None
    
    while tail_pointer:
        tail_pointer = tail_pointer.get_next_node()
        count += 1
        if count >= n + 1:
            if nth_pointer is None:
                nth_pointer = array.head_node
            else:
                nth_pointer = nth_pointer.get_next_node()
    return nth_pointer.get_value()
a = LinkedList()


for i in range(10, 0, -1):
    a.add_node_heading(i)
print(a.print_list())
print(two_pointer_method(a, 5))
