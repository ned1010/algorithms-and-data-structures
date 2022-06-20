#depth first search uses stack
#using recursion


def dfs(graph, current_vertex, target_vertex, visited=None):
    #base case
    if visited is None:
        visited = []

    visited.append(current_vertex)
    
    if current_vertex is target_vertex:
        return visited
    
    for neighbour in graph[current_vertex]:
        if neighbour not in visited:
            path = dfs(graph, neighbour, target_vertex, visited)
            if path:
                return path





