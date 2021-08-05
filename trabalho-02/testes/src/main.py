from grafo import GrafoTAD

if __name__ == '__main__':
    grafoTad = GrafoTAD()
    grafoTad.carrega_arquivo('testes/grafo.txt')

    grafoTad.remove_vertice(1)
