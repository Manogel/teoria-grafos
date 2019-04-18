def verificaCiclo(arestas, aresta):
    aux = arestas[:]
    aresta = list(aresta)
    while True:
        tamanho_anterior = len(aux)
        for i, arst in enumerate(aux):
            lista_aux = []
            if aresta[0] == aresta[-1]:
                print(aresta)
                return False
            if aresta[-1] in arst[-1]:
                verificando = aresta[-1]
                for vrtc in arst[-1]:
                    lista_aux = aux[:]
                    lista_aux.remove(arst)
                    if verificando != vrtc:
                        aresta.append(vrtc)
                        if verificaCiclo(lista_aux, aresta) == True:
                            continue
                        else:
                            return False
        print(aresta)
        if len(aux) == tamanho_anterior or len(aux) == 0:
            return True
