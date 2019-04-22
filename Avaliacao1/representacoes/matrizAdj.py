from representacoes.setGrafo import *
import numpy as np


def addVertice(conjunto_vertices, grafo):
    # Adiciona um vertice ao meu conjunto de vertices
    print('FOI ADICIONADO UM VERTICE')
    nVertices = len(conjunto_vertices)
    vertice = np.zeros((nVertices), dtype=np.int)
    grafo = list(grafo)
    grafo.append(vertice)
    conjunto_vertices.append(max(conjunto_vertices)+1)
    auxGrafo = list()
    for coluna in grafo:
        auxColuna = list(coluna)
        auxColuna.append(0)
        auxGrafo.append(np.array(auxColuna))
    auxGrafo = np.array(auxGrafo)
    return conjunto_vertices, auxGrafo


def dropVertice(conjunto_vertices, conjunto_arestas, grafo):
    '''Remove um vertice ao meu conjunto de vertices, após a remocao, é atualizada
    a variavel "GRAFO" que é a representação do grafo, alem disso, é removido todas as arestas que
    que estavam incidindo neste vertice'''
    print('REMOVE VERTICE')
    vertice = int(
        input(f'Dado V(G): {conjunto_vertices}, deseja remover qual?\n'))
    auxArestas = conjunto_arestas[:]
    for aresta in conjunto_arestas:
        if vertice in aresta:
            auxArestas.remove(aresta)
    indexRemocao = conjunto_vertices.index(vertice)
    grafo = np.delete(grafo, indexRemocao, 0)
    grafo = np.delete(grafo, indexRemocao, 1)

    conjunto_vertices.remove(vertice)
    return conjunto_vertices, auxArestas, grafo


def addAresta(conjunto_vertices, conjunto_arestas, grafo, dirigido=False):
    '''Adiciona uma aresta ao meu conjunto de arestas, após a adição, é atualizada
    a variavel "GRAFO" que é a representação do grafo'''
    print('ADICIONA ARESTA')
    v1 = int(input("Informe o vertice1 de incidencia: "))
    v2 = int(input("Informe o vertice2 de incidencia: "))
    indexVertice1 = conjunto_vertices.index(v1)
    indexVertice2 = conjunto_vertices.index(v2)
    # print(grafo)
    if (v1, v2) not in conjunto_arestas:
        conjunto_arestas.append((v1, v2))
        grafo[indexVertice1][indexVertice2] = 1
    if (v2, v1) not in conjunto_arestas and dirigido == False:
        conjunto_arestas.append((v2, v1))
        grafo[indexVertice2][indexVertice1] = 1
    return conjunto_arestas, grafo


def dropAresta(conjunto_vertices, conjunto_arestas, grafo):
    '''
        Remove uma aresta do conjunto de arestas, após a remoção, é atualizada
    a variavel "GRAFO" que é a representação do grafo
    '''
    print('REMOVE ARESTA')
    v1 = int(input("Informe o vertice1 de incidencia: "))
    v2 = int(input("Informe o vertice2 de incidencia: "))
    if (v1, v2) in conjunto_arestas:
        conjunto_arestas.remove((v1, v2))
        grafo[v1][v2] = 0
    else:
        print(f'ERRO, aresta ({v1}, {v2}) não existe!')
    if (v2, v1) in conjunto_arestas:
        conjunto_arestas.remove((v2, v1))
        grafo[v2][v1] = 0
    return conjunto_arestas, grafo


def consultarVertice(grafo, conjunto_vertices):
    # Dado um vertice, é feita a consulta imprimindo todos os dados referentes àquele vertice
    print('CONSULTA VERTICE')
    vertice = int(
        input(f"Dado V(G): {conjunto_vertices}, deseja visitar qual?\n"))
    if vertice not in conjunto_vertices:
        print(f'ERRO, vetice {vertice} não pertence ao seu conjunto V(G)')
        return False
    indexVertice = conjunto_vertices.index(vertice)
    dadoTxt = f'E({vertice}) = ' + '{'
    for incide, value in enumerate(grafo[indexVertice]):
        if value == 1:
            dadoTxt = dadoTxt + f'({vertice},{incide}), '
    print(dadoTxt[:-2] + '}')


""" vertices = [0, 1, 2, 3]
arestas = [(0, 1), (1, 0), (0, 3), (3, 0), (1, 3),
           (3, 1), (2, 2), (3, 2), (2, 3)]

grafo = matrizAdjacencia(vertices, arestas)
vertices, arestas, grafo = dropVertice(vertices, arestas, grafo)
vertices, grafo = addVertice(vertices, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
arestas, grafo = dropAresta(vertices, arestas, grafo)

print('==============')
listarGrafo(grafo, vertices, arestas)
consultarVertice(grafo, vertices)
 """