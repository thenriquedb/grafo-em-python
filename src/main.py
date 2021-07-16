from grafo import Grafo

if __name__ == '__main__':
    NUM_VERTICES = 6
    NUM_ARESTAS = 6

    grafo = Grafo(NUM_VERTICES, NUM_ARESTAS)

    grafo.GAcriaAresta(1, 6, peso=9)
    grafo.GAcriaAresta(6, 1, peso=8)
    grafo.GAcriaAresta(1, 3, peso=7)
    grafo.GAcriaAresta(6, 2, peso=6)
    grafo.GAcriaAresta(5, 4)
    grafo.GAcriaAresta(2, 2)

    grafo.GIpegaGrau(1)
    print('adjancencias de 1 ', grafo.GAAdjacencias(2))

    # print('cont_arestas: ', grafo.cont_arestas)
    # print('laço ', grafo .GBarestaLaco(6))
    print(grafo)
    # grafo.carregarArquivo()
