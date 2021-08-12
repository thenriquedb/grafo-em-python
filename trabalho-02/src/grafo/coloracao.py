# from grafo_TAD import GrafoTAD


class Coloracao:
    def __init__(self, grafo, quant_max_cores: int):
        self.grafo = grafo
        self.quant_max_cores = quant_max_cores

    def executar(self):
        # vertices_coloridos = self.grafo.cont_vertices * None

        resultado = {}

        # Inicia todos os vertices com sem cor
        for vertice in list(self.grafo.vertices):
            resultado[vertice] = None

        # print(self.grafo.arestas)
        # cont_vertices = self.grafo.cont_vertices
        adjacentes = self.grafo.pega_vertices_adjacentes()
        for vertice_atual in list(self.grafo.vertices):
            if vertice_atual not in adjacentes:
                continue

            # vertices_adjacentes = self.grafo.arestas[vertice_atual]
            # cores_adjcantes = set()

            # atribuidos = set(
            # [resultado.get(i) for i in self.grafo.arestas[vertice_atual] if i in resultado])

            atribuidos = set()
            for vertice, ids in adjacentes.items():
                if vertice in resultado:
                    atribuidos.add(resultado.get(vertice))

            # check for the first free color
            color = 1
            for c in atribuidos:
                if color != c:
                    break
                if color >= self.quant_max_cores:
                    return

                color = color + 1

            resultado[vertice_atual] = color

        print("> resultado", resultado)
