
import numpy as np
import pandas as pd


# Constantes
SEM_LIGACAO = 0
ARESTA_SIMPLES = 1
ARESTA_PARALELA = 2


class Grafo:
    def __init__(self, max_vertices: int, max_arestas: int):
        self.max_vertices = max_vertices
        self.max_arestas = max_arestas
        self.cont_arestas = 0

        self.arestas = dict()
        self.vertices = dict()
        self.matriz_adjacencia = None

        self.__iniciaGrafo()

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

            # Como a matriz inicia no index 1 é necessário subtrair 1 no valor do
            # vertice para acessar a posição da matriz corretamente.
            self.GAcriaAresta(int(vertice_origem),
                              int(vertice_destino))

    def salvarEmArquivo(self):
        pass

    def __iniciaGrafo(self):
        self.arestas = dict()
        self.vertices = dict()

        self.matriz_adjacencia = np.zeros(
            (self.max_vertices, self.max_vertices), dtype=int)

    def GGcriaGrafo(self, v):
        """Cria um grafo

           Args:
               a (int): número máximo de arestas previstos.
               v (int): número máximo de vértices previstos.
           """
        self.vertices = list(range(1, v if v else self.max_vertices))
        self.__iniciaGrafo()

    def GBexisteIdVertice(self, v: int):
        """Verifica se o vértice existe no grafo

        Args:
            v (int): Identificador do vértice

        Returns:
            bool: True caso exista e False se não
        """
        return v in self.vertices

    def GBexisteArestaDir(self, v1: int, v2: int):
        """Verifica se a aresta dirigida existe no grafo

        Args:
            v1 (int): Vértice de origem
            v2 (int): Vértice de destino

        Returns:
            bool: True caso exista e False se não
        """
        return self.matriz_adjacencia[v1, v2] != SEM_LIGACAO

    def GBexisteAresta(self, v1: int, v2: int):
        """Verifica se a aresta não dirigida existe no grafo

        Args:
            v1 (int): Vértice de origem
            v2 (int): Vértice de destino

        Returns:
            bool: True caso exista e False se não
        """
        v1_para_v2 = self.matriz_adjacencia[v1, v2]
        v2_para_v1 = self.matriz_adjacencia[v2, v1]
        return v1_para_v2 != SEM_LIGACAO and v2_para_v1 != SEM_LIGACAO

    def GAcriaAresta(self, v1: int, v2: int):
        """Cria uma nova ligação no grafo

        Args:
            v1 (int): Vértice de origem
            v2 (int): Vértice de destino

        Returns:
            int: Identificador do vértice criado
        """
        if self.cont_arestas == self.max_arestas:
            return None

        if v1 >= 0 and v2 >= 0:
            self.matriz_adjacencia[v1-1, v2-1] = 1
            return self.__salvaIdentificador(v1, v2)

    def GInumeroArestas(self):
        """Retorna o número de arestas no grafo

        Returns:
            int: Quantidade de arestas adicionadas  
        """
        return self.cont_arestas

    def GInumeroArestasMax(self):
        """Retorna o número maxímo de arestas no grafo

        Returns:
            int: Quantidade de maxíma de arestas   
        """
        return self.max_arestas

    def GIpegaGrau(self, v: int):
        return

    def GApegaAresta(self, a: int):
        """Retorna a aresta caso exista

        Args:
            a (int): Identificador da aresta

        Returns:
            tuple: Caso o identificador seja valído retorna uma tupla com o 
                     vértice de origem e destino. Se não retorna None
        """
        return self.arestas.get(a)

    def GGdestroiGrafo(self):
        """Inicialzia a matriz de adjacência novamente"""
        self.__iniciaGrafo()

    def __salvaIdentificador(self, v1: int, v2: int):
        """
        Para toda nova aresta do grafo um identificador deve ser criado para ela.
        Estes identificadores são armazenados em uma estrutura de dicionário, que
        funciona como uma tabela hash onde a chave é o identificador e valor é uma
        tupla no formato (vértice origem, vértice destino)

        Args:
            v1 (int): Vértice de origem
            v2 (int): Vértice de destino

        Returns:
            int: Identificador do vértice criado
        """
        self.cont_arestas = self.cont_arestas + 1
        identificador = self.cont_arestas
        self.arestas[identificador] = (v1, v2)

        return identificador

    def __str__(self):
        df = pd.DataFrame(self.matriz_adjacencia)
        return df.to_string()
