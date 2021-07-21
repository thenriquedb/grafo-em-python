from grafo import Grafo


class TestGrafo:
    def __init__(self, path_grafo_1: str, path_grafo_2: str, path_grafo_3: str):
        self.grafo = Grafo()

        self.__path_grafo_1 = path_grafo_1
        self.__path_grafo_2 = path_grafo_2
        self.__path_grafo_3 = path_grafo_3

    def __carregar_grafo(self, path: str):
        self.grafo.carregarArquivo(path)

    def __informacoes_basicas(self):
        print(self.grafo)

        print("\nLista de arestas: ")
        for [id, aresta] in self.grafo.arestas.items():
            print("\t{} - {}".format(id, aresta))

        print("\nLista de vertices: {}".format(self.grafo.vertices))
        print("Qtde máxima de vertices {}".format(self.grafo.max_vertices))
        print("Qtde máxima de arestas {}".format(self.grafo.max_arestas))
        print("----------------------------------------------\n")
    def __existe_vertice(self, v: int):
        print("Existe o vértice {}: {}".format(
            v, self.grafo. GBexisteIdVertice(v)))

    def __existe_aresta(self, a: int):
        [vertice_origem, vertice_destino] = self.grafo.GApegaAresta(a)
        print("Existe aresta {}: {}".format(
            a, self.grafo.GBexisteAresta(vertice_origem, vertice_destino)))

    def __existe_aresta_direcionada(self, v1: int, v2: int):
        existe = self.grafo.GBexisteArestaDir(v1, v2)
        print("Existe aresta direcionada ({},{}) {}".format(v1, v2, existe))

    def __e_laco(self, a: int):
        print("Aresta {} é um laço {}".format(a,
                                              self.grafo.GBarestaLaco(a)))

    def __vizinhos(self, v: int):
        pass
        # self.grafo.matriz_adjacencia.pegarVerticesAdjacentes()

    def __grau_vertice(self, v: int):
        print("Grau do vertíce {}: {}".format(self.grafo.GIpegaGrau(v), v))

    def __existe_id_vertice(self, id: int):
        print("Existe vértice com o id {}: {}".format(id,
                                                      self.grafo.GBexisteIdVertice(id)))

    def __pega_aresta(self, v1: int, v2: int):
        aresta = self.grafo.matriz_adjacencia.pegaAresta(v1, v2)
        print("Pega aresta ({},{}): {}".format(v1, v2, aresta))

    def __prima_entrada(self, v: int):
        print("Primeira aresta na estrela de entrada do vértice {}: {}".format(
            v, self.grafo.GAprimaEntrada(v)))

    def __prima_saida(self, v: int):
        print("Primeira aresta na estrela de saída do vértice {}: {}".format(
            v, self.grafo.GAprimaSaida(v)))

    def testar_grafo_01(self):
        self.__carregar_grafo(self.__path_grafo_1)

        print("GRAFO 01")
        self.__informacoes_basicas()
        self.__existe_vertice(10)
        self.__existe_aresta(6)
        self.__existe_aresta_direcionada(3, 6)
        self.__e_laco(4)
        self.__grau_vertice(2)

        # print(grafo.)

    def testar_grafo_02(self):
        self.__carregar_grafo(self.__path_grafo_2)

        print("GRAFO 02")
        self.__informacoes_basicas()
        self.__existe_id_vertice(0)
        self.__existe_aresta_direcionada(3, 4)
        self.__existe_aresta(6)
        self.__e_laco(11)
        self.__grau_vertice(11)

    def testar_grafo_03(self):
        self.__carregar_grafo(self.__path_grafo_3)

        print("GRAFO 03")
        self.__informacoes_basicas()
        self.__existe_id_vertice(10)
        self.__existe_aresta_direcionada(3, 4)
        self.__existe_aresta(6)
        self.__pega_aresta(5, 6)
        self.__e_laco(11)
        self.__grau_vertice(11)
        self.__prima_entrada(10)
        self.__prima_saida(10)
