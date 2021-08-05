from .heapMin import HeapMin
# from .grafo import Grafo
from . import codigoArestas as CodigoArestas


class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def calcular(self, origem: int):
        INFINITY = -1
        max_vertices = self.grafo.max_vertices

        custo_vem = [[INFINITY, 0] for _ in range(max_vertices)]
        custo_vem[origem - 1] = [0, origem]
        h = HeapMin()
        h.adiciona_no(0, origem)

        matriz_adjacencia = self.grafo.matriz_adjacencia

        while h.tamanho() > 0:
            dist, v = h.remove_no()

            for i in range(max_vertices):
                if matriz_adjacencia.pegaAresta(v - 1, i) == CodigoArestas.SEM_LIGACAO:
                    continue

                e_infinito = custo_vem[i][0] == INFINITY
                custo_atual = custo_vem[i][0]
                novo_custo = dist + matriz_adjacencia.pegaAresta(v - 1, i)

                if e_infinito or custo_atual > novo_custo:
                    custo_vem[i] = [novo_custo, v]
                    h.adiciona_no(novo_custo, i + 1)

        return custo_vem
