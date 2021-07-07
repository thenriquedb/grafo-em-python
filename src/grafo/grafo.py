
from .matrizAdjacencia import MatrizAdjacencia
from . import codigoArestas as CodigoArestas


class Grafo:
    def __init__(self, max_vertices: int, max_arestas: int):
        self.max_vertices = max_vertices
        self.max_arestas = max_arestas

        self.vertices = list(range(1, self.max_vertices))
        self.arestas = dict()

        self.matriz_adjacencia = MatrizAdjacencia(max_vertices, max_arestas)

    @property
    def cont_arestas(self):
        return self.matriz_adjacencia.cont_arestas

    def carregarArquivo(self):
        file = open("graph/grafo.txt", "r")
        lines = file.read().splitlines()

        for (index, line) in enumerate(lines):
            # Primeira linha cont;em as informaçÕes do grafo
            if(index == 0):
                conteudo = line.split()
                max_vertices = int(conteudo[0])
                max_arestas = int(conteudo[1])

                self.max_vertices = max_vertices
                self.max_arestas = max_arestas

            [vertice_origem, vertice_destino] = line.split()

            # Como a matriz inicia no index 1 é necessário subtrair 1 no valor do
            # vertice para acessar a posição da matriz corretamente.
            self.matriz_adjacencia.novaAresta(vertice_origem, vertice_destino)

    def salvarEmArquivo(self):
        pass

    def GAcriaAresta(self, v1: int, v2: int):
        """Cria uma nova ligação no grafo

        Args:
            v1 (int): Vértice de origem
            v2 (int): Vértice de destino

        Returns:
            int: Identificador do vértice criado
        """
        self.matriz_adjacencia.novaAresta(v1, v2)

    def GApegaAresta(self, v1: int, v2: int):
        """Retorna a aresta caso exista

        Args:
           v1 (int): Vértice de origem
           v2 (int): Vértice de destino

        Returns:
           tuple: Caso o identificador seja valído retorna uma tupla com o
                    vértice de origem e destino. Se não retorna None
        """
        return self.matriz_adjacencia.pegaAresta(v1, v2)

    def GApegaAresta(self, a: int):
        """Retorna a aresta caso exista

        Args:
            a (int): Identificador da aresta

        Returns:
            tuple: Caso o identificador seja valído retorna uma tupla com o 
                     vértice de origem e destino. Se não retorna None
        """
        return self.matriz_adjacencia.pegaAresta(a)

    def GBexisteAresta(self, v1: int, v2: int):
        """Verifica se a aresta não dirigida existe no grafo

          Args:
              v1 (int): Vértice de origem
              v2 (int): Vértice de destino

          Returns:
              bool: True caso exista e False se não
        """
        v1_para_v2 = self.matriz_adjacencia.pegaAresta(v1, v2)
        v2_para_v1 = self.matriz_adjacencia.pegaAresta(v2, v1)

        return v1_para_v2 != CodigoArestas.SEM_LIGACAO and v2_para_v1 != CodigoArestas.SEM_LIGACAO

    def GBexisteArestaDir(self, v1: int, v2: int):
        """Verifica se a aresta dirigida existe no grafo

        Args:
            v1 (int): Vértice de origem
            v2 (int): Vértice de destino

        Returns:
            bool: True caso exista e False se não
        """
        return self.matriz_adjacencia.pegaAresta(v1, v2) != CodigoArestas.SEM_LIGACAO

    def GBexisteIdVertice(self, v: int):
        """Verifica se o vértice existe no grafo

        Args:
            v (int): Identificador do vértice

        Returns:
            bool: True caso exista e False se não
        """
        return v in self.vertices

    def GInumeroArestas(self):
        """Retorna o número de arestas no grafo

        Returns:
            int: Quantidade de arestas adicionadas  
        """
        return self.matriz_adjacencia.cont_arestas

    def GInumeroArestasMax(self):
        """Retorna o número maxímo de arestas no grafo

        Returns:
            int: Quantidade de maxíma de arestas   
        """
        return self.max_arestas

    def GIpegaGrau(self, v: int):
        return self.matriz_adjacencia.pegaGrau(v)

    def GGdestroiGrafo(self):
        """Inicialzia a matriz de adjacência novamente"""
        self.matriz_adjacencia = MatrizAdjacencia(
            self.max_vertices, self.max_arestas)

    def __str__(self):
        return self.matriz_adjacencia.__str__()
