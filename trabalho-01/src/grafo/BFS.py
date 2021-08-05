from grafo import Grafo


class BFS:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    def buscar(self, v1: int, v2: int):
        v1 = v1 - 1
        v2 = v2 - 1

        fila = [v1]
        vertices_adjacentes = self.grafo.GAAdjacencias(v1)
        vistados = set([v1])
        caminho = []

        while fila:
            atual = fila.pop(0)
            if (atual == v2):
                break

            caminho.append(atual)

            vertices_adjacentes = self.grafo.GAAdjacencias(atual)
            for vertice in vertices_adjacentes:
                if vertice not in vistados:
                    vistados.add(vertice)
                    fila.append(vertice)

        print(caminho)
