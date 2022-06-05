#based on queue data structure
#queue is store the nodes

from collections import deque 

def bfs(root_node, goal_value):

    #using this queue to store the node
    frontier_queue = deque()

    initial_path = [root_node]
    frontier_queue.appendleft(initial_path)

    while len(frontier_queue) > 0:
        #this removes/pops node from the last of the list
        current_path = frontier_queue.pop()
        for node in current_path:
            print(node.value)
        #current_node is the last element of current_path
        current_node = current_path[-1]

        if current_node.value == goal_value:
            return current_path
        
        #if current_node is not the goal value, check if it's children

        for child in current_node.children:
            #create a new_path so that it doesn't mess up original path
            new_path = current_path[:]
            new_path.append(child)
            frontier_queue.appendleft(new_path)

    return None