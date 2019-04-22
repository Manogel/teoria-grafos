vertice_visitando = int(input('Digite um vertice de 0 a 4: '))

def getGrafo():
    grafo = [0]*5
    grafo[0] = [1]
    grafo[1] = [3, 2]
    grafo[2] = [4]
    grafo[3] = [0, 4]
    grafo[4] = [1]
    return grafo

def getBuscaLargura(grafo):
    #Inicializa o grafo
    fila = list()
    #Declara a fila
    n_vertices = len(grafo)
    #Armazena a quantidade de vertices do grafo
    visita = [0]*n_vertices
    #Declara a lista de visita

    print(f'Lista de visita{visita}')
    print(f'Lista de adjacencia {grafo}')
    print(f'fila {fila}')

    fila.append(vertice_visitando)
    #Adiciona o vertice passado, na fila de visita
    while len(fila) != 0:
        #olho os vertices adjacentes àquele vertice
        print(f'Visitando o vertice {fila[0]}')
        adjacencia = grafo[fila[0]]
        for vertice in adjacencia:
            if visita[fila[0]] == 0 and vertice not in fila:
                #Se o vertice lido não foi visitado e não se encontra em minha fila, adiciona a fila
                fila.append(vertice)
        print(f'fila: {fila}')
        #Marca-se visita
        visita[fila[0]] = 1
        #Remove o vertice que ja foi visitado
        print(f'Removendo o vertice {fila[0]} da fila')
        fila.pop(0)
    else:
        print('Fila vazia, FINALIZANDO')
        

grafo = getGrafo()
getBuscaLargura(grafo)