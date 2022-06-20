#dijstra's algorith finds the shortest distance from start to all the other vertices
#you pop the minimum element from the heap
from dis import dis
from math import inf
from heapq import heappop, heappush


def dijkstra(graph, start):
    #storing distances as dictionary for all the vertices
    distances = {}

    for vertex in graph:
        #making all the other vertices inf 
        distances[vertex]  = inf
    distances[start] = 0
    unvisited = [(0, start)]
    while unvisited:
        #pops from the value from the heap
        current_distance, current_vertex = heappop(unvisited)

        for neighbour, edge_weight in graph[current_vertex]:
            new_distance = current_distance + edge_weight
            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                heappush(unvisited, (new_distance, neighbour))
    return distances
            
