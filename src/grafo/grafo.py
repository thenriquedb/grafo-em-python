
import numpy as np
from .matrizAdjacencia import MatrizAdjacencia
from . import codigoArestas as CodigoArestas
from .dijkstra import Dijkstra


class Grafo:
    def __init__(self, max_vertices: int = 0, max_arestas: int = 0):
        if max_vertices != 0 and max_arestas != 0:
            self.__inicia_grafo(max_vertices, max_arestas)

    def __inicia_grafo(self, max_vertices: int, max_arestas: int):
        self.max_vertices = max_vertices
        self.max_arestas = max_arestas

        self.vertices = list(range(1, self.max_vertices))

        self.matriz_adjacencia = MatrizAdjacencia(
            max_vertices, max_arestas)

    @property
    def cont_arestas(self):
        return self.matriz_adjacencia.cont_arestas

    @property
    def arestas(self):
        return self.matriz_adjacencia.arestas

    def carregarArquivo(self, path):
        file = open(path, "r")
        lines = file.read().splitlines()

        for (index, line) in enumerate(lines):
            # Primeira linha cont;em as informaçÕes do grafo
            if(index == 0):
                conteudo = line.split()
                max_vertices = int(conteudo[0])
                max_arestas = int(conteudo[1])

                self.__inicia_grafo(max_vertices, max_arestas)
                continue

            [vertice_origem, vertice_destino] = line.split()

            # Como a matriz inicia no index 1 é necessário subtrair 1 no valor do
            # vertice para acessar a posição da matriz corretamente.
            self.matriz_adjacencia.novaAresta(vertice_origem, vertice_destino)

    def __grafoEPonderado(self):
        """Verifica se o grafo é ponderado ou não

        Returns:
            bool: True caso seja ponderado
        """
        matriz = self.matriz_adjacencia.getMatriz()
        res = np.where(matriz != CodigoArestas.ARESTA_SIMPLES)
        return res[0].size > 0

    def salvarEmArquivo(self, filename: str = "resultado.txt"):
        """Salva o grafo gerado em um arquivo txt

        Args:
            filename (str): nome do arquivo
        """
        with open(filename, "w") as file:
            grafoPonderado = self.__grafoEPonderado()

            for i in range(self.max_vertices):
                for j in range(self.max_vertices):
                    aresta = self.matriz_adjacencia.pegaAresta(i, j)

                    if(aresta == CodigoArestas.SEM_LIGACAO):
                        continue

                    if(grafoPonderado):
                        file.write("{} {} {}\n".format(i + 1, j + 1, aresta))
                        continue

                    file.write("{} {}\n".format(i + 1, j + 1))

    def __arestaValida(a):
        return a != None

    def GAcriaAresta(self, v1: int, v2: int, peso=1):
        """Cria uma nova ligação no grafo

        Args:
            v1 (int): Vértice de origem
            v2 (int): Vértice de destino

        Returns:
            int: Identificador do vértice criado
        """
        self.matriz_adjacencia.novaAresta(v1, v2, peso)

    def GAcriaArestaNaoDirecionada(self, v1: int, v2: int, peso=1):
        """Cria uma nova ligação não direcionada grafo

        Args:
            v1 (int): Vértice de origem
            v2 (int): Vértice de destino

        Returns:
            int: Identificador do vértice criado
        """
        self.matriz_adjacencia.novaAresta(v1, v2, peso)
        self.matriz_adjacencia.novaAresta(v2, v1, peso)

    def GApegaArestaDir(self, v1: int, v2: int):
        """Retorna a aresta direcionada caso exista

        Args:
           v1 (int): Vértice de origem
           v2 (int): Vértice de destino

        Returns:
           tuple: Caso o identificador seja valído retorna uma tupla com o
                    vértice de origem e destino. Se não retorna None
        """
        matriz_adjacencia = self.matriz_adjacencia
        return matriz_adjacencia.pegaAresta(v1, v2) or matriz_adjacencia.pegaAresta(v2, v1)

    def GApegaArestza(self, v1: int, v2: int):
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
        return self.matriz_adjacencia.arestas.get(a)

    def GVprimeiroVertice(self):
        """
        Retorna o primeiro vértice do grafo

        Returns:
            int: Identificador do vértice
        """
        return self.vertices[0]

    def GVproximoVertice(self, v: int):
        """
        Retorna o próximo vértice do grafo

        Returns:
            int: identificador do vértice 
        """
        return self.vertices[v + 1]

    def GAprimeiraAresta(self):
        """
        Pega a próxima aresta do grafo

        Returns:
            int: identificador da aresta 
        """
        return self.matriz_adjacencia.arestas[0]

    def GVproximaAresta(self, a: int):
        """
        Pega a primeira aresta do grafo

        Returns:
            int: identificador da aresta 
        """
        return self.matriz_adjacencia.arestas[a + 1]

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

    def GBexisteIdAresta(self, a: int):
        return self.matriz_adjacencia.pegaArestaID(a)

    def __pega_arestas_a_partir_do_identificador(self, a: int):
        # Pega o index do identificador a no dicionário de arestas
        arestas = self.matriz_adjacencia.arestas
        keys = list(arestas.keys())
        index = keys.index(a)
        items = list(arestas.items())

        return items[index + 1:]

    def GVvizinho(self, a: int, v: int):
        if not self.GBexisteIdVertice(v) and not self.GBexisteIdAresta(a):
            return None

        [v_origem, v_destino] = self.GApegaAresta(a)

        if v_origem == v:
            return v_destino

        if v_destino == v:
            return v_origem

        return None

    def GAproxAresta(self, v: int, a: int):
        """
        Pega a próxima aresta do grafo

        Args:
            a (int): [description]
            v (int): [description]
        """

        if not self.GBexisteIdVertice(v) and not self.GBexisteIdAresta(a):
            return None

        arestas = self.__pega_arestas_a_partir_do_identificador(a)
        for id, aresta in arestas:
            [v_origem, v_destino] = aresta

            if v == v_origem or v == v_destino:
                return id

        return None

    def GAproxEntrada(self, v: int, a: int):
        """
        Pega a próxima aresta de entrada grafo

        Args:
            a (int): [description]
            v (int): [description]
        """
        if not self.GBexisteIdVertice(v) and not self.GBexisteIdAresta(a):
            return None

        arestas = self.__pega_arestas_a_partir_do_identificador(a)
        for id, aresta in arestas:
            [v_origem, _] = aresta

            if v == v_origem:
                return id

        return None

    def GAproxSaida(self, v: int, a: int):
        """
        Pega a próxima aresta de entrada grafo

        Args:
            a (int): [description]
            v (int): [description]
        """
        if not self.GBexisteIdVertice(v) and not self.GBexisteIdAresta(a):
            return None

        arestas = self.__pega_arestas_a_partir_do_identificador(a)
        for id, aresta in arestas:
            [_, v_destino] = aresta

            if v == v_destino:
                return id

        return None

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

    def GIpegaGrau(self, v: int):
        return self.matriz_adjacencia.pegaGrau(v)

    def GBarestaLaco(self, a: int):
        matriz_adjacencia = self.matriz_adjacencia
        aresta = matriz_adjacencia.pegaLigacaoDaAresta(a)

        if not aresta:
            return None

        [vertice_origem, vertice_destino] = aresta
        aresta = matriz_adjacencia.pegaAresta(vertice_origem, vertice_destino)

        return aresta != CodigoArestas.SEM_LIGACAO

    def GAlfa(self, a: int):
        """Pega o vértice de partida da aresta

        Args:
            a (int): Identificador da arestas
        """
        arestas = self.matriz_adjacencia.pegaLigacaoDaAresta(a)
        if(self.__arestaValida(arestas)):
            [vertice_origem, _] = arestas
            return vertice_origem

        return None

    def GOmega(self, a: int):
        """Pega o vértice de chegada da aresta

        Args:
            a (int): Identificador da arestas
        """
        arestas = self.matriz_adjacencia.pegaLigacaoDaAresta(a)

        if(self.__arestaValid(arestas)):
            [_, vertice_destino] = arestas
            return vertice_destino

        return None

    def GAprimaAresta(self, v: int):
        """
        Pega a primeira aresta na estrela do vértice, em grafos não dirigidos

        Args:
            v (int): Vertice
        """
        arestas = self.matriz_adjacencia.arestas
        for (identificador, aresta) in arestas.items():
            [v1, v2] = aresta
            if v1 == v or v2 == v:
                return identificador

        return None

    def GAprimaEntrada(self, v: int):
        """
        Pega a primeira aresta na estrela de entrada do vértice, em grafos dirigidos

        Args:
            v (int): Vertice buscado
        """
        arestas = self.matriz_adjacencia.arestas
        for (identificador, aresta) in arestas.items():
            [vertice_origem, _] = aresta
            if vertice_origem == v:
                return identificador

        return None

    def GAprimaSaida(self, v: int):
        """
        Pega a primeira aresta na estrela de saída do vértice, em grafos dirigidos

        Args:
            v (int): Vertice
        """
        arestas = self.matriz_adjacencia.arestas
        for (identificador, aresta) in arestas.items():
            [_, vertice_destino] = aresta
            if vertice_destino == v:
                return identificador

        return None

    def GAAdjacencias(self, v):
        return self.matriz_adjacencia.pegarVerticesAdjacentes(v)

    def dijkstra(self, vertice_origem: int):
        dijkstra = Dijkstra(self)
        return dijkstra.calcular(vertice_origem)
