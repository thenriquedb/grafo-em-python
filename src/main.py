from grafo import Grafo

if __name__ == '__main__':
    NUM_VERTICES = 6
    NUM_ARESTAS = 6

    grafo = Grafo(NUM_VERTICES, NUM_ARESTAS)

    grafo.GAcriaAresta(1, 6)
    grafo.GAcriaAresta(6, 1)
    grafo.GAcriaAresta(1, 3)
    grafo.GAcriaAresta(6, 2)
    grafo.GAcriaAresta(5, 4)
    grafo.GAcriaAresta(1, 2)

    print('cont_arestas: ', grafo.cont_arestas)
    print(grafo)
    # grafo.carregarArquivo()
