from inicializacao import *

grafo = [[1, 3], [0, 3], [2, 3], [0, 1, 2]]


def addVertice(conjunto_vertices, grafo):
    #Adiciona um vertice ao meu conjunto de vertices
    print('ADICIONA VERTICE')
    conjunto_vertices.append(max(conjunto_vertices)+1)
    grafo.append([])
    return conjunto_vertices, grafo

def addAresta(conjunto_vertices, conjunto_arestas, grafo, dirigido = False):
    '''Adiciona uma aresta ao meu conjunto de arestas, após a adição, é atualizada
    a variavel "GRAFO" que é a representação do grafo'''
    print('ADICIONAR UMA ARESTA')
    print(f'Dado V(G) = {conjunto_vertices}')
    v1 = int(input("- Vertice de incidencia 1: "))
    v2 = int(input("- Vertice de incidencia 2: "))
    if v1 not in conjunto_vertices or v2 not in conjunto_vertices:
        print(f'ERRO: {v1} e/ou {v2} não correspondem ao conjunto de vertices {conjunto_vertices}!!')
        return conjunto_arestas, grafo
    if (v1, v2) not in conjunto_arestas:
        conjunto_arestas.append((v1, v2))
    if (v2, v1) not in conjunto_arestas and dirigido == False:
        conjunto_arestas.append((v2, v1))
    indexAdicao1 = conjunto_vertices.index(v1)
    indexAdicao2 = conjunto_vertices.index(v2)
    if v2 not in grafo[indexAdicao1]:
        grafo[v1].append(v2)
    if v1 not in grafo[indexAdicao2] and dirigido == False:
        grafo[v2].append(v1)
    return conjunto_arestas, grafo

def dropVertice(conjunto_vertices, conjunto_arestas, grafo):
    '''Remove um vertice ao meu conjunto de vertices, após a remocao, é atualizada
    a variavel "GRAFO" que é a representação do grafo, alem disso, é removido todas as arestas que
    que estavam incidindo neste vertice'''
    print('REMOVE VERTICE')
    vertice = int(input(f"Dado V(G): {conjunto_vertices}, qual remover: "))
    if vertice not in conjunto_vertices:
        print(f'ERRO: {vertice} não correspondem ao conjunto de vertices!!')
        return conjunto_vertices, conjunto_arestas, grafo
    else:
        indice_remocao = conjunto_vertices.index(vertice)
        conjunto_vertices.remove(vertice)
        del grafo[indice_remocao]
    auxArestas = conjunto_arestas[:]
    for aresta in conjunto_arestas:
        if vertice in aresta:
            auxArestas.remove(aresta)

    auxGrafo = grafo[:]
    for index, adjacencia in enumerate(grafo):
        if vertice in adjacencia:
            auxGrafo[index].remove(vertice)
    
    return conjunto_vertices, auxArestas, auxGrafo

def dropAresta(conjunto_vertices, conjunto_arestas, grafo):
    '''
        Remove uma aresta do conjunto de arestas, após a remoção, é atualizada
    a variavel "GRAFO" que é a representação do grafo
    '''
    print('REMOVER UMA ARESTA')
    v1 = int(input("- Vertice de incidencia 1: "))
    v2 = int(input("- Vertice de incidencia 2: "))
    if (v1, v2) in conjunto_arestas:
        indexRemocao = conjunto_vertices.index(v1)
        conjunto_arestas.remove((v1, v2))
        grafo[indexRemocao].remove(v2)
        
    if (v2, v1) in conjunto_arestas:
        indexRemocao = conjunto_vertices.index(v2)
        conjunto_arestas.remove((v2, v1))
        grafo[indexRemocao].remove(v1)
    
    return conjunto_arestas, grafo

def consultarVertice(grafo, conjunto_vertices):
    #Dado um vertice, é feita a consulta imprimindo todos os dados referentes àquele vertice
    print('CONSULTAR VERTICE')
    vertice = int(input(f'Informe o vertice dado V(G) = {conjunto_vertices}: \n'))
    indexVertice = conjunto_vertices.index(vertice)
    print(f'Consultando o vertice {vertice}: ')
    dadoTxt = f'E({vertice}) = ' + '{'
    for incide in grafo[indexVertice]:
        dadoTxt = dadoTxt + f'({vertice},{incide}), '
    print(dadoTxt[:-2] + '}')

vertices, arestas, grafo = dropVertice(vertices, arestas, grafo)
vertices, grafo = addVertice(vertices, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
arestas, grafo = addAresta(vertices, arestas, grafo)
arestas, grafo = dropAresta(vertices, arestas, grafo)

print('==============')
listarGrafo(grafo, vertices, arestas)
consultarVertice(grafo, vertices)
