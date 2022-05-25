from node import Node
from linkedlist import LinkedList

def swap_element(array, value1, value2):
    print(("swapping {0} {1}".format(value1, value2)))
    
    if value1 == value2:
        print("Both values are equal, so cannot swap the values")
        return
    #first step is located value1
    node1_prev = None
    node1 = array.head_node
    
    while node1 is not None:
        if node1.get_value() == value1:
            break
        node1_prev = node1
        node1 = node1.get_next_node()
    

    #locate value2 in the list
    node2_prev = None
    #make the node2 head of the list
    node2 = array.head_node
    while node2 is not None:
        if node2.get_value() == value2:
            break
        node2_prev = node2
        node2 = node2.get_next_node()
    
    if node1 is None or node2 is None:
        print("One of the values is not in the list")
        return


    #swapping
    if node1_prev is None:
        array.head_node = node2
    else:
        node1_prev.set_next_node(node2)
    
    if node2_prev is None:
        array.head_node = node1
    else:
        node2_prev.set_next_node(node1)

    #after removing the nodes from their respective positions,
    #place it back in ther swapped place
    #temp is need because without temp you are just copying the address
    #but we need a temporary memory to hold the node1.
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)

linked_list = LinkedList()

for i in range(5):
    linked_list.add_node_heading(i)
print(linked_list.print_list())
swap_element(linked_list, 1, 2)
print(linked_list.print_list())

