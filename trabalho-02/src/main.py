from grafo import GrafoTAD, Coloracao

if __name__ == '__main__':
    grafoTad = GrafoTAD()
    grafoTad.carrega_arquivo('testes/grafo.txt')

    # grafoTad.salvar_arquivo("resultados.txt")

    # grafoTad.remove_vertice(1)
    coloracao = Coloracao(grafoTad, 3)
    coloracao.executar()
