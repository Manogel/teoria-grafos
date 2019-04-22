import numpy as np
# np.delete(array, index, 0) linha
# np.delete(array, index, 1) coluna


def getVertices():
    '''Recebo uma string contendo a lista de vertices do meu grafo, após isso, formato essa string para
    uma lista contendo valores inteiros'''
    vertices = str(input(
        'Informe seu conjunto de vertices denotado por {x1, x2, x3, ..., xn} :\n')).strip()
    aux = vertices[1:-1]
    vertices = aux.split(',')
    vertices = [int(e) for e in vertices]
    return vertices


def getArestas(conjunto_vertices, dirigido=False):
    '''Recebo uma string contendo a lista de arestas do meu grafo, após isso, formato essa string para
       uma lista contendo uma tupla com valores inteiros, simbolisando a aresta, para cada aresta'''

    '''É recebido o meu conjunto de vertices pois, no momento que estamos formatando a minha lista de aresta,
       é feita a verificação se a existencia de uma conexão(aresta) coincide com meu conjunto de vertices!!
            EX: dado o conjunto_vertices = [0, 1], é impossivel a existencia da aresta (0, 2), pois, o 2 não existe
                no meu conjunto de vertices'''

    arestas = str(input(
        'Informe seu conjunto de arestas denotado por {(x1, x2) - (x2, x3) - (..., ...) - (xn, xm)}:\n')).strip()
    arestas = arestas[1:-1]
    aux = arestas.split('-')
    lista_arestas = []
    for aresta in aux:
        aux = []
        aresta = aresta.strip()
        aresta = aresta[1:-1].split(',')
        for vertice in aresta:
            if int(vertice) not in conjunto_vertices:
                print(
                    f'ERRO: O vertice {vertice} não se encontra em seu conjunto de vertices!')
                return False
            aux.append(int(vertice))
        if tuple(aux) not in lista_arestas and dirigido == False:
            lista_arestas.append(tuple(aux))
            if tuple([aux[-1], aux[0]]) not in lista_arestas:
                lista_arestas.append(tuple([aux[-1], aux[0]]))
    return lista_arestas


def listaAjacencia(conjunto_vertices, conjunto_arestas):
    # Retorna a representação do grafo por lista de adjacencia
    grafo = list()
    for c in conjunto_vertices:
        aux = []
        grafo.append(aux)

    for v1, v2 in conjunto_arestas:
        if v2 not in grafo[v1]:
            grafo[v1].append(v2)
    return grafo


def matrizAdjacencia(conjunto_vertices, conjunto_arestas):
    # Retorna a representação do grafo por matriz de adjacencia
    import numpy as np
    qntVertices = len(conjunto_vertices)
    grafo = np.zeros((qntVertices, qntVertices), dtype=np.int)
    for v1, v2 in conjunto_arestas:
        grafo[v1][v2] = 1
    return grafo


def listarGrafo(grafo, conjunto_vertices, conjunto_arestas):
    # Imprime os dados de um grafo
    print(f'Grafo: \n{grafo}')
    print(f'V(G): \n{conjunto_vertices}')
    print(f'E(G): \n{conjunto_arestas}')


def matrizIncidencia(conjunto_vertices, conjunto_arestas, dirigido=False):
    # Retorna a representação do grafo por matriz de incidencia
    auxArestas = list()
    for aresta in conjunto_arestas:
        if aresta not in auxArestas and (aresta[1], aresta[0]) not in auxArestas:
            auxArestas.append(aresta)
    grafo = np.zeros((len(conjunto_vertices), len(auxArestas)), dtype=np.int)
    for index, aresta in enumerate(auxArestas):
        indexV1 = conjunto_vertices.index(aresta[0])
        indexV2 = conjunto_vertices.index(aresta[1])
        grafo[indexV1][index] = 1
        if dirigido == True:
            grafo[indexV2][index] = -1
        else:
            grafo[indexV2][index] = 1
    return auxArestas, grafo
