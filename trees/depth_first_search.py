#based on the stack data structure (Last In First Out)

def dfs(root_node, goal, path=[]):
    path = path + [root_node]

    if root_node.value == goal:
        return path
    
    for child in root_node.children:
        path_found = dfs(child, goal, path)

        if path is not None:
            return path_found