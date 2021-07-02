
import numpy as np
import pandas as pd


class Grafo:
    def __init__(self):

        self.max_arestas = 0
        self.max_vertices = 0
        # self.arestas = dict()
        # self.vertices = list()
        self.matriz_adjacencia = None
        # current working directory
        # self.caminho = os.path.join(os.getcwd(), "src/graph/")

    def GGcriaGrafo(self,  v, a):
        """Cria um grafo

           Args:
               a (int): número máximo de arestas previstos.
               v (int): número máximo de vértices previstos.
           """
        self.max_arestas = a
        self.max_vertices = v
        self.matriz_adjacencia = np.zeros((v, v), dtype=int)

    def carregarArquivo(self):
        file = open("graph/grafo.txt", "r")
        lines = file.read().splitlines()

        for (index, line) in enumerate(lines):
            # Primeira linha cont;em as informaçÕes do grafo
            if(index == 0):
                conteudo = line.split()
                cont_vertices = int(conteudo[0])
                cont_arestas = int(conteudo[1])

                self.GGcriaGrafo(cont_vertices, cont_arestas)

            [vertice_origem, vertice_destino] = line.split()
            """
            Como a matriz inicia no index 1 é necessário subtrair 1 no valor do
            vertice para acessar a posição da matriz corretamente.
            """
            self.GAcriaAresta(int(vertice_origem) - 1,
                              int(vertice_destino) - 1)

            print(line.strip())
        df = pd.DataFrame(self.matriz_adjacencia)
        print(df)

    def GAcriaVertice(self):
        """Cria uma aresta"""
        pass

    def GAcriaAresta(self, v1, v2):
        """Cria uma aresta"""
        if v1 >= 0 and v2 >= 0:
            self.matriz_adjacencia[v1, v2] = 1

    def GGdestroiGrafo(self):
        """Inicialzia a matriz de adjacência novamente"""
        self.matriz_adjacencia = np.zeros(
            (self.max_vertices, self.max_vertices))
