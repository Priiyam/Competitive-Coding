class Vertex:
    def __init__(self, n):
        self.name = n


class Graph:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False

    def add_edge(self, u, v, weight=1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False

    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(' ')
            for j in range(len(self.edges)):
                print(self.edges[i][j]),
                print(' '),




n, m = map(int, raw_input().split())
g = Graph()
for i in xrange(1, n+1):
    g.add_vertex(Vertex(str(i)))
edges = []
for i in xrange(m):
    edges.append(raw_input().replace(' ',''))
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.print_graph()