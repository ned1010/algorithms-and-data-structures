#Graph is network data structure
from vertex import Vertex


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.graph_dict = {}
    
    def add_vertex(self, vertex):
        self.graph_dict[vertex.value] = vertex 
    
    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(self.graph_dict[to_vertex.value])

        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(self.graph_dict[from_vertex.value])

    def find_path(self, start_vertex, target_vertex):
        start = [start_vertex]
        seen = {}

        while len(start) > 0:
            current_vertex = start.pop()
            seen[current_vertex] = True
            print("Current vertex", current_vertex)

            if current_vertex == target_vertex:
                return True
            else:
                #all the edges connected to the current vertex
                vertices = self.graph_dict[current_vertex]
                next_vertices = vertices.get_edges()

                next_vertices = [vertex for vertex in next_vertices if vertex not in seen]

                start += next_vertices
        return False

#let's build a graph
# def build_graph(directed):
#     graph = Graph(directed)
#     vertices = ["a", "b", "c", "d"]

#     for value in vertices:
#         vertex = Vertex(value)
#         graph.add_vertex(vertex)
        
#     print(graph.find_path("a", "b"))
# build_graph(True)
