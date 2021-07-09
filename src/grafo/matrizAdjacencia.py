import numpy as np
import pandas as pd
from . import codigoArestas as CodigoArestas


class MatrizAdjacencia:
    def __init__(self, max_vertices: int, max_arestas: int):

        self.max_vertices = max_vertices
        self.max_arestas = max_arestas
        self.cont_arestas = 0
        self.arestas = dict()

        self.__matriz = np.zeros(
            (self.max_vertices, self.max_vertices), dtype=int)

    def novaAresta(self, v1: int, v2: int, peso=1):
        if self.cont_arestas == self.max_arestas:
            return None

        v1 = int(v1)
        v2 = int(v2)

        if v1 >= 0 and v2 >= 0:
            self.__matriz[v1 - 1, v2 - 1] = peso
            return self.__salvaIdentificador(v1, v2)

    def pegaAresta(self, v1: int, v2: int):
        return self.__matriz[v1, v2]

    # def pegaAresta(self, a: int):
    #     aresta = self.arestas.get(a)
    #     if not aresta:
    #         return None

    #     [vertice_origem, vertice_destino] = aresta
    #     return self.pegaAresta(vertice_origem, vertice_destino)

    def pegaLigacaoDaAresta(self, a: int):
        """
        Recebe como parâmetro o identificador e retorna uma tupla com os vertices
        da aresta

        Args:
            a (int): Identificador

        Returns:
            tuple: Tupla com a aresta
        """
        aresta = self.arestas.get(a)
        if not aresta:
            return None

        [vertice_origem, vertice_destino] = aresta
        return (vertice_origem - 1, vertice_destino - 1)

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

    def pegaGrau(self, v: int):
        v = v - 1

        linha = self.__matriz[v]
        coluna = self.__matriz[:, v]

        contador = 0
        for elemento in linha:
            if elemento != CodigoArestas.SEM_LIGACAO:
                contador += 1

        for elemento in coluna:
            if elemento != CodigoArestas.SEM_LIGACAO:
                contador += 1

        return contador
        # for line in self.__matriz

    def __str__(self):
        df = pd.DataFrame(self.__matriz)
        print(self.arestas)
        return df.to_string()
