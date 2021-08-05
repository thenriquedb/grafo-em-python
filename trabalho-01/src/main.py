from grafo import DFS, Grafo, BFS
import grafo
from testGrafo import TestGrafo

if __name__ == '__main__':
    # testGrafo = TestGrafo(path_grafo_1="testes/grafo1.txt",
    #                       path_grafo_2="testes/grafo2.txt",
    #                       path_grafo_3="testes/grafo3.txt")

    # testGrafo.testar_grafo_01()
    # testGrafo.testar_grafo_02()
    # testGrafo.testar_grafo_03()

    grafo = Grafo()

    # grafo.GAcriaAresta(7, 7)
    # grafo.GAcriaAresta(1, 2)
    # grafo.GAcriaAresta(1, 5)
    # grafo.GAcriaAresta(2, 3)
    # grafo.GAcriaAresta(2, 5)
    # grafo.GAcriaAresta(3, 4)
    # grafo.GAcriaAresta(4, 5)
    # grafo.GAcriaAresta(4, 6)

    grafo.carregarArquivo("testes/grafo3.txt")

    buscaProfundidade = DFS(grafo)
    buscaLargura = BFS(grafo)

    print("Busca em largura")
    buscaLargura.buscar(1, 9)

    print("\nBusca em profundidae")
    buscaProfundidade.buscar(1, 9)
