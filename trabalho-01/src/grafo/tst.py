class DijkstraGraph(Graph):
    def init(self, graph={}):
        Graph.init(self, graph)

    def min_distance(self, dist, sptSet):
        min = float('inf')

        for v in range(len(self.vertices())):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):

        dist = [float('inf')] * len(self.vertices())
        dist[src] = 0
        visited = [False] * len(self.vertices())

        for cout in range(len(self.vertices())):
            u = self.min_distance(dist, visited)  # Busca o minimo
            visited[u] = True
            for v in range(len(self.vertices())):
                cost = self.get_cost(u, v)
                # Relazamento
                if cost > 0 and visited[v] == False and dist[v] > dist[u] + cost:
                    dist[v] = dist[u] + cost
        return dist


def dijkstra(graph, root):
    return DijkstraGraph(graph).dijkstra(root)


if name == 'main':

    g = Graph()
    edges = [
        (0, 1, 17),
        (0, 2, 14),
        (0, 3, 5),
        (1, 4, 18),
        (1, 3, 13),
        (5, 2, 20),
        (5, 6, 2),
        (7, 2, 19),
        (7, 4, 8),
        (2, 4, 12),
        (6, 4, 1),
        (6, 3, 13)
    ]

    for e in edges:
        g.add_edge(*e)

    dijkstra_weight = dijkstra(g, 0)

    print(dijkstra_weight)

    print(f'Grafo Original:\n{g}')
    print('--------------------------------------------------\n')
    print(
        f'Minimal Spanning Tree - Dijkstra (Peso Final = {sum(dijkstra_weight)}):')
