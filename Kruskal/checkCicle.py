def verificaCiclo(arestas, aresta):
    # Funcão que vai verificar se vai existir um ciclo no meu conjunto de aresta
    # se for adicionada uma nova aresta
    aux = arestas[:]
    aresta = list(aresta)
    while True:
        tamanho_anterior = len(aux)
        for i, arst in enumerate(aux):
            lista_aux = []
            if aresta[0] == aresta[-1]:
                # Condição de parada para dizer que foi encontrado um ciclo
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
            # Condição de parada se não foi encontrado nenhum ciclo
            return True
