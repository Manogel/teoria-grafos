def getArestas(grafo):
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

