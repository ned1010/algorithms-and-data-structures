#unlike singly linked list, double has two pointers one forward and one backward
from stack.node import Node

class DoubleLinkedList:
    def __init__(self, head_node= None, tail_node= None):
        self.head_node = head_node
        self.tail_node = head_node
    
    #methods for double linked list
    #methods should be able to add value, remove value
    #adding to head of the list
    def add_to_head(self, value):
        new_head = Node(value)
        current_head = self.head_node

        if current_head != None:
            new_head.set_next_node(current_head)
            current_head.set_prev_node(new_head)
        #else if it's empty or head is none
        self.head_node = new_head

        #if list is empty and the tail is also none
        if self.tail_node is None:
            self.tail_node = new_head
            

    def add_to_tail(self, value):
        new_tail  = Node(value)
        current_tail = self.tail_node

        if current_tail is not None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
        self.tail_node = new_tail

        #if list is empty, you make the node both tail and head
        if self.head_node is None:
            self.head_node = new_tail
            
    #remove node from the list
    #remove from  head
    def remove_head(self):
        head_to_remove = self.head_node

        if head_to_remove is None:
            return None
        #create new head of the list 
        self.head_node = head_to_remove.get_next_node()

        if self.head_node != None:
            self.head_node.set_prev_node(None)

        if head_to_remove == self.tail_node:
            self.remove_tail()

        # return head_to_remove.get_value()



    def remove_tail(self):
        tail_to_remove = self.tail_node

        if tail_to_remove is None:
            return None
        #else 
        #making the second last element the new tail
        self.tail_node = tail_to_remove.get_prev_node()

        if self.tail_node != None:
            self.tail_node.set_next_node(None)
        
        if tail_to_remove == self.head_node:
            self.remove_head()

        # return tail_to_remove.get_value()

    #remove a node by value
    def remove_by_value(self, value):
        node_to_remove = None
        current_head = self.head_node
        
        while current_head != None:
            if current_head.get_value() == value:
                node_to_remove = current_head
                break
            current_head = current_head.get_next_node()

        if node_to_remove == None:
            return None
        
        #if node_to_remove is head, then use remove_head method
        #if node_to_remove is tail, then use removed_tail method
        #if node_to_remove is none, return none
        #if node_to_remove is none of above conditions, then set remove it and set
        #pointers
        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            prev_node = node_to_remove.get_prev_node()
            next_node = node_to_remove.get_next_node()
            prev_node.set_next_node(next_node)
            next_node.set_prev_node(prev_node)

        # return node_to_remove
            
    def print_list(self):
        result = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() is not None:
                result += str(current_node.get_value()) + "\n"
                current_node = current_node.get_next_node()
        return result 


x = DoubleLinkedList()

for i in range(10, 0, -1):
    x.add_to_head(i)
print(x.print_list())
x.remove_head()
x.remove_tail()
x.remove_by_value(7)
# x.add_after_nodes(3, 5)
print(x.print_list())


