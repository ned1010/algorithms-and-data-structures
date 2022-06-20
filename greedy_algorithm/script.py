from dijkstra_algorithm import dijkstra

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [('A', 7)],
        'B': [('C', 3), ('D', 2)]
    }


distances_from_a = dijkstra(graph, "A")
print(distances_from_a)