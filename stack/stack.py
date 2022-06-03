
from node import Node 

#create stack class
#push -> add to the head
#pop -> remove from the head
#peek -> reveal the data on top
#max_size -> keeps the track of the size

class Stack:

    def __init__(self, max_size=1000):
        self.max_size = max_size
        self.head_node = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)

        if self.has_space():
            print("Adding {0} to the stack".format(new_node.get_value()))
            self.head_node = new_node
            new_node.set_next_node(self.head_node)
            self.size += 1
        else:
            print("Stack has no space")

    def pop(self):
        #checking if there is an element in the stack
        if not self.is_empty():
            node_to_remove = self.head_node
            #if there is just one element in the stack
            self.head_node = node_to_remove.get_next_node()
            print("Removing {0} from the stack".format(node_to_remove.get_value()))
            self.size -= 1
        else:
            print("Stack is empty")


    def peek(self):
        if self.get_size() == None:
            return None
        else:
            return self.head_node.get_value()

    def has_space(self):
        if self.max_size == None:
            return True
        return self.size < self.max_size
    
    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")

# Uncomment the push() statement below:
pizza_stack.push("pizza #7")

# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()

# Uncomment the pop() statement below:
# pizza_stack.pop()
