from representacoes.setGrafo import *
import numpy as np

""" vertices = [0, 1, 2, 3]
arestas = [(0, 1), (1, 0), (0, 3), (3, 0), (1, 3),
           (3, 1), (2, 2), (3, 2), (2, 3)] """

vertices = [0]
arestas = []

arestas, grafo = matrizIncidencia(vertices, arestas)


def addVertice(conjunto_vertices, conjunto_arestas, grafo):
    # Adiona um vertice
    print('UM VERTICE FOI ADICIONADO')
    new_vertice = np.zeros((len(conjunto_arestas)), dtype=np.int)
    auxGrafo = list(grafo)
    auxGrafo.append(new_vertice)
    auxGrafo = np.array(auxGrafo)
    conjunto_vertices.append(max(conjunto_vertices)+1)
    return conjunto_vertices, auxGrafo


def addAresta(conjunto_vertices, conjunto_arestas, grafo):
    # Adiciona uma aresta
    print('ADICIONAR ARESTA')
    v1 = int(input('Insira o vertice1 de incidencia: '))
    v2 = int(input('Insira o vertice2 de incidencia: '))

    if v1 not in conjunto_vertices or v2 not in conjunto_vertices:
        print(
            f'ERRO, {v1} e/ou {v2} não pertence ao seu conjunto V(G): {conjunto_vertices}')
        return conjunto_arestas, grafo
    if (v1, v2) in conjunto_arestas or (v2, v1) in conjunto_arestas:
        print(f'ERRO, aresta informada ja exite em seu conjunto de arestas!')
        return conjunto_arestas, grafo
    indexV1 = conjunto_vertices.index(v1)
    indexV2 = conjunto_vertices.index(v2)
    auxGrafo = list()
    grafo = list(grafo)
    for index, coluna in enumerate(grafo):
        auxColuna = list(coluna)
        if indexV1 == index:
            auxColuna.append(1)
        elif indexV2 == index:
            auxColuna.append(1)
        else:
            auxColuna.append(0)
        auxGrafo.append(np.array(auxColuna))
    conjunto_arestas.append((v1, v2))
    return conjunto_arestas, np.array(auxGrafo)


def dropVertice(conjunto_vertices, conjunto_arestas, grafo):
    '''Remove um vertice do meu grafo e atualiza a representação do grafo,
    o conjunto de arestas e vertices'''
    print('REMOVE VERTICE')
    vertice = int(
        input(f'Dado V(G): {conjunto_vertices}, informe o vertice: '))
    if vertice not in conjunto_vertices:
        print(f'ERRO, {vertice} não pertence ao seu conjunto de vertices!!')
        return conjunto_vertices, conjunto_arestas, grafo
    indexVertice = conjunto_vertices.index(vertice)
    grafo = np.delete(grafo, indexVertice, 0)
    auxConjArestas = conjunto_arestas[::-1]
    for value in auxConjArestas:
        if vertice in value:
            indexRemocao = conjunto_arestas.index(value)
            grafo = np.delete(grafo, indexRemocao, 1)
            conjunto_arestas.remove(value)
    return conjunto_vertices, conjunto_arestas, grafo


def dropAresta(conjunto_vertices, conjunto_arestas, grafo):
    ''' Remove uma aresta e atualiza a representação do grafo, tambem, o conjunto de arestas'''
    print('REMOVE ARESTA')
    v1 = int(input('Insira o vertice1 de incidencia: '))
    v2 = int(input('Insira o vertice2 de incidencia: '))

    if v1 not in conjunto_vertices or v2 not in conjunto_vertices:
        print(
            f'ERRO, {v1} e/ou {v2} não pertence ao seu conjunto V(G): {conjunto_vertices}')
        return conjunto_arestas, grafo
    if (v1, v2) not in conjunto_arestas and (v2, v1) not in conjunto_arestas:
        print(f'ERRO, aresta informada não exite em seu conjunto de arestas!')
        return conjunto_arestas, grafo
    try:
        indexAresta = conjunto_arestas.index((v1, v2))
    except:
        indexAresta = conjunto_arestas.index((v2, v1))
        (v1, v2) = (v2, v1)
    grafo = np.delete(grafo, indexAresta, 1)
    conjunto_arestas.remove((v1, v2))
    return conjunto_arestas, grafo


def visitarVertice(conjunto_vertices, conjunto_arestas, grafo):
    ''' Faz uma visita no vertice desejado e retorna todos os seus dados'''
    print('VISITAR VERTICE')
    vertice = int(
        input(f'Dado V(G): {conjunto_vertices}, informe o vertice a ser visitado:'))
    if vertice not in conjunto_vertices:
        print(f'ERRO, {vertice} não faz parte do seu conjunto de vertices!!')
    indexVertice = conjunto_vertices.index(vertice)
    visita = list(grafo[indexVertice])
    dadoTxt = f'E({vertice}) = ' + '{'
    for incide, value in enumerate(visita):
        if value == 1:
            dadoTxt = dadoTxt + f'{conjunto_arestas[incide]}, '
    print(dadoTxt[:-2] + '}')


#vertices, arestas, grafo = dropVertice(vertices, arestas, grafo)
""" vertices, grafo = addVertice(vertices, arestas, grafo)
vertices, grafo = addVertice(vertices, arestas, grafo)
vertices, grafo = addVertice(vertices, arestas, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
print(vertices)
print(arestas)
print(grafo)
visitarVertice(vertices, arestas, grafo)
 """