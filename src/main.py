from grafo import Grafo
import grafo
from testGrafo import TestGrafo

if __name__ == '__main__':
    testGrafo = TestGrafo(path_grafo_1="testes/grafo1.txt",
                          path_grafo_2="testes/grafo2.txt",
                          path_grafo_3="testes/grafo3.txt")

    # testGrafo.testar_grafo_01()
    # testGrafo.testar_grafo_02()
    testGrafo.testar_grafo_03()
