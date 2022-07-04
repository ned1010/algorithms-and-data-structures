#A star is a modification of the dijkstra'a algorithm
#A star finds the shortest distance between the start and target
#Use heuristic value, estimated distance between the current vertex to target
#heuristic value is calculated either using manhattan or euclidean (pythogorean) method

from heapq import heappop, heappush
from math import inf, sqrt
from manhattan import manhattan_graph, penn_station, grand_central_station, thirty_third_and_madison, library
#Manhattan distance
def heuristic(start, target):
  x_distance = abs(start.position[0] - target.position[0])
  y_distance = abs(start.position[1] - target.position[1])
  return x_distance + y_distance

#Euclidean Distance
# def heuristic(start, target):
#     x = abs(start[0]) - abs(target[0])
#     y = abs(start[1]) - abs(target[1])
#     return sqrt(x**2 + y**2)


def a_star(graph, start, target):
    print("A start algorithm")

    #using dictionary to keep track of all the paths
    path_and_distances = {}
    count = 0

    for vertex in graph:
        #setting all the vertex as inf from start to each
        path_and_distances[vertex] = [inf, [start.name]]
    
    #start vertex is 0
    path_and_distances[start][0] = 0
    #0 is the distance and path is the start in following vertices_to_explore
    vertices_to_explore = [(0, start)]
    #as long as there are vertices to explore and target is inf
    while vertices_to_explore and path_and_distances[target][0] == inf:
        current_distance, current_vertex = heappop(vertices_to_explore)

        for neighbour, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight + heuristic(neighbour, target)
            new_path = path_and_distances[current_vertex][1] + [neighbour.name]

            if new_distance < path_and_distances[neighbour][0]:
                path_and_distances[neighbour][0] = new_distance
                path_and_distances[neighbour][1] = new_path
                heappush(vertices_to_explore, (new_distance, neighbour))      
                count += 1
                print("\nAt " + vertices_to_explore[0][1].name)
    
    print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), path_and_distances[target][1])


    #return all the paths from start to target
    return path_and_distances[target][1]
print(a_star(manhattan_graph,thirty_third_and_madison, library ))


