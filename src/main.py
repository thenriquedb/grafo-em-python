from grafo import Grafo

if __name__ == '__main__':
    NUM_VERTICES = 7
    NUM_ARESTAS = 32

    grafo = Grafo(NUM_VERTICES, NUM_ARESTAS)

    grafo.GAcriaArestaNaoDirecionada(1, 2, peso=5)
    grafo.GAcriaArestaNaoDirecionada(1, 3, peso=6)
    grafo.GAcriaArestaNaoDirecionada(1, 4, peso=10)
    grafo.GAcriaArestaNaoDirecionada(2, 5, peso=13)
    grafo.GAcriaArestaNaoDirecionada(3, 4, peso=3)
    grafo.GAcriaArestaNaoDirecionada(3, 5, peso=11)
    grafo.GAcriaArestaNaoDirecionada(3, 6, peso=6)
    grafo.GAcriaArestaNaoDirecionada(4, 5, peso=6)
    grafo.GAcriaArestaNaoDirecionada(4, 6, peso=4)
    grafo.GAcriaArestaNaoDirecionada(5, 7, peso=3)
    grafo.GAcriaArestaNaoDirecionada(6, 7, peso=8)

    print(grafo)
    custo = grafo.dijkstra(1)
    print('Lista de custos', custo)
    # bfs = BFS(grafo)
    # bfs.buscar(1, 5)
    # print('cont_arestas: ', grafo.cont_arestas)
    # print('laço ', grafo .GBarestaLaco(6))
    # grafo.carregarArquivo()
