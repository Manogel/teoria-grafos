def getArestas(grafo):
    '''Funcão que vai retornar a lista de arestas de um grafo, representado por lista
    de adjacencia, não direcional, e com pesos. Ao final será retornado a lista ordenada
    por peso'''
    arestas = list()
    for index, value in enumerate(grafo):
        for aresta, peso in value:
            aux = [peso, (index, aresta)]
            aux2 = [peso, (aresta, index)]
            if (aux in arestas) or (aux2 in arestas):
                pass
            else:
                arestas.append(aux)
    arestas.sort()
    return arestas
