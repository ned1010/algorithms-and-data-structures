#breath first search is visits every node of the graph
#it should also tell the path of the graph

def bfs(graph, start_vertex, target_vertex):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    #since bfs using queue, make it a queue
    queue = [vertex_and_path]
    visited = list()

    while len(queue) > 0:
        current_vertex, current_path = queue.pop()
        visited.append(current_vertex)

        #base case
        if current_vertex == target_vertex:
            return path

        else:
            for neighbour in graph[current_vertex]:
                if neighbour not in visited:
                    return path + [neighbour]
                else:
                    queue.append([neighbour, path+[neighbour]])

