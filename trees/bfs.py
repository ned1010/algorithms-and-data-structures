from collections import deque
def breathfirtsearch(root_node, goal):

    queue = deque()

    initial_path = [root_node]
    queue.appendleft(initial_path)

    while queue:
        
        current_path = queue.pop()
        current_node = current_path[-1]

        if current_node.value == goal:
            return current_path

        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            queue.appendleft(new_path)
    return None