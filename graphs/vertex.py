#vertex keeps tracks of the value and edges

class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
    
    def add_edge(self, vertex, weight=0):
        self.edges[weight] = vertex

    def get_edges(self):
        return list(self.edges.keys())

# a = Vertex("a")
# b = Vertex("b")
# a.add_edge(b)
# print(a.get_edges())