from stack.node import Node

#creating queue class 
#enqueue -> add to the tail
#dequeue -> remove from the head
#peek -> seek the value
#max_size -> the maximum space of queue

class Queue:
    def __init__(self, max_size, head_node=None, tail_node=None):
        self.max_size = max_size
        self.head_node = head_node
        self.tail_node = tail_node
        self.size = 0
    
    def enqueue(self, value):
        if self.has_space():
            new_node = Node(value)
            #check whether the stack is empty, if it's then make it both tail and head
            print("Adding item {0} to the queue".format(new_node.get_value()))
            #if the queue is empty, then make the node both tail and head
            if self.is_empty():
                self.head_node = new_node
                self.tail_node = new_node
            else:
                self.tail_node.set_next_node(new_node)
                self.tail_node = new_node
            self.size += 1
        else:
            print("there is no space in the queue")


    def dequeue(self):
        #remove from the head
        if self.get_size() > 0:
            node_to_dequeue = self.head_node
            print("Removing {0} from the queue".format(node_to_dequeue.get_value()))

            #if there is only one node in the queue
            if self.get_size() == 1:
                self.head_node = None
                self.tail_node = None
            else:
                self.head_node = node_to_dequeue.get_next_node()
            self.size -= 1
        else:
            print("The queue is empty")


    def peek(self):
        current_head = self.head_node
        if current_head.get_value() != None:
            return None
        else:
            return current_head.get_value()

    def is_empty(self):
        return self.size == 0

    def has_space(self):
        if self.max_size == None:
            return True
        return self.size < self.max_size

    def get_size(self):
        return self.size



print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
# ------------------------ #
# Uncomment the line below:
deli_line.enqueue("western omelet with home fries")
# ------------------------ #
print("------------\nOur first order will be " + str(deli_line.peek()))
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
# ------------------------ #
# Uncomment the line below:
deli_line.dequeue()
# ------------------------ #