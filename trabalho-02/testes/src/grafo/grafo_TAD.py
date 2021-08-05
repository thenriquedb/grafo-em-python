class GrafoTAD:
    def __init__(self):
        self.cont_vertices = 0
        self.cont_arestas = 0

        # Os últimos identificadores que foram utilizados para criar os vértices
        # e arestas,
        self.semente = (None, None)
        self.arestas = dict()
        self.vertices = set()

    def novo_vertice(self, id_vertice: int):
        if id_vertice not in self.vertices:
            self.vertices.add(int(id_vertice))

            self.__incrmenta_cont_vertices()
            self.__atualiza_semente(novo_id_vertice=id_vertice)

    def nova_aresta(self, id_aresta: int, v_origem: int, v_destino: int):
        if not self.__aresta_existe(id_aresta):
            self.arestas[id_aresta] = (v_origem, v_destino)

            self.__incrmenta_cont_arestas()
            self.__atualiza_semente(novo_id_aresta=id_aresta)

    def remove_vertice(self, id_vertice: int):
        if id_vertice not in self.vertices:
            return

        self.vertices.remove(id_vertice)
        self.__decrementa_cont_vertices()

        # Se você fizer apenas arestas_clone = self.arestas o valor será copiado
        # por refêrencia, fazendo assim que toda modificação feita em arestas_clone
        # reflita no objeto original.
        arestas_clone = self.arestas.copy()

        for id_aresta, ligacao in self.arestas.items():
            [v_origem, v_destino] = ligacao

            if v_origem == id_vertice or v_destino == id_vertice:
                arestas_clone.pop(id_aresta, None)
                self.__decrementa_cont_arestas()

        self.arestas = arestas_clone

    def remove_aresta(self, id_aresta: int):
        if id_aresta in self.arestas.keys():
            self.arestas.pop(id_aresta, None)

            self.__decrementa_cont_arestas()
            self.atualizase_semente

    def carrega_arquivo(self, caminho_arquivo: str):
        with open(caminho_arquivo, "r") as file:
            lines = file.read().splitlines()

            PRIMEIRA_LINHA = True
            for line in lines:
                conteudo = line.split()

                if PRIMEIRA_LINHA:
                    cont_vertices = int(conteudo[0])
                    cont_arestas = int(conteudo[1])

                    self.__set_cont_vertices(cont_vertices)
                    self.__set_cont_arestas(cont_arestas)

                    PRIMEIRA_LINHA = False
                    continue

                # Identificador do vertíce
                if len(conteudo) == 1:
                    [id_vertice] = conteudo
                    self.novo_vertice(int(id_vertice))
                    continue

                # Aresta
                if len(conteudo) == 3:
                    [id_aresta, v_origem, v_destino] = conteudo
                    self.nova_aresta(int(id_aresta), int(
                        v_origem), int(v_destino))

    def salvar_arquivo(self, nome_arquivo: str = "resultado.txt"):
        """Salva o grafo gerado em um arquivo txt

        Args:
            filename (str): nome do arquivo
        """
        pass

    def __aresta_existe(self, id_aresta: int):
        return id_aresta in self.arestas.keys()

    def __incrmenta_cont_vertices(self):
        self.cont_vertices += 1

    def __incrmenta_cont_arestas(self):
        self.cont_arestas += 1

    def __decrementa_cont_vertices(self):
        self.cont_vertices -= 1

    def __decrementa_cont_arestas(self):
        self.cont_arestas -= 1

    def __set_cont_vertices(self, cont_vertices: int):
        self.cont_vertices = cont_vertices

    def __set_cont_arestas(self, cont_arestas: int):
        self.cont_arestas = cont_arestas

    def __atualiza_semente_vertice(self, novo_id_vertice: int):
        [_, id_aresta] = list(self.semente)

        nova_semente = [novo_id_vertice, id_aresta]
        self.semente = tuple(nova_semente)

        return self.semente

    def __atualiza_semente_aresta(self, novo_id_aresta: int):
        [id_vertice, _] = list(self.semente)

        nova_semente = [id_vertice, novo_id_aresta]
        self.semente = tuple(nova_semente)

        return self.semente

    def __atualiza_semente(self, novo_id_vertice=None, novo_id_aresta=None):
        if novo_id_vertice:
            self.__atualiza_semente_vertice(novo_id_vertice)

        if novo_id_aresta:
            self.__atualiza_semente_aresta(novo_id_aresta)

        if novo_id_vertice and novo_id_aresta:
            self.__atualiza_semente_vertice(novo_id_vertice)
            self.__atualiza_semente_vertice(novo_id_aresta)

        return self.semente
