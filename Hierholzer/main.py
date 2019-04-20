import numpy as np
def verificaGrau(grafo):
    #verifica se o grau de cada vertice é par
    for x in range(len(grafo)):
        if (list(grafo[x]).count(1)) % 2 != 0:
            return False
    return True    

def achaCiclo(indInicio, prox, grafo, ciclo):  
    #procura ciclos dentro de um grafo
    for indice, arst in enumerate(list(grafo[prox])):
        #print(indice, arst, indInicio)
        try:
            if arst == 1 and arst == grafo[prox+1][indice]:
                ciclo.append(prox+1)
                grafo[prox][indice] = -1
                grafo[prox+1][indice] = -1
                #print(grafo)
                print(f'achei outro caminho no indice: {indice}')
                if grafo[0][indice] == 1:
                    return True 
                else:
                    return achaCiclo(indInicio, prox+1, grafo, ciclo)
            elif arst == 1 and grafo[indInicio][indice] == 1:
                ciclo.append(indInicio)
                grafo[prox][indice] = -1
                grafo[indInicio][indice] = -1
                return ciclo
            elif arst == 1 and (0 == grafo[prox+1][indice]) and grafo[indInicio][indice] == 1:
                ciclo.append(indInicio)
                grafo[prox][indice] = -1
                grafo[indInicio][indice] = -1
                return ciclo
        except:
            if arst == 1 and grafo[indInicio][indice] == 1:
                ciclo.append(indInicio)
                grafo[prox][indice] = -1
                grafo[indInicio][indice] = -1
                return ciclo

def criaGrafo(arestas, vertices):
    grafo = np.zeros((vertices ,arestas), dtype = np.int)
    grafo[0][0] = 1
    grafo[0][2] = 1
    grafo[1][0:2] = 1
    grafo[2][1:5] = 1
    grafo[3][3] =1 
    grafo[3][5] = 1
    grafo[4][4:6] = 1
    return grafo

grafo = criaGrafo(6,5)

if verificaGrau(grafo) :
    ciclos = []
    for j, aresta in enumerate(list(grafo)):
        for indice, arst in enumerate(list(aresta)):
            if arst ==  1 and arst == grafo[j+1][indice]:
                print(f'Achei no indice um caminho: {indice}')
                grafo[j][indice] = -1
                grafo[j+1][indice] = -1
                ciclos.append(achaCiclo(j, j+1, grafo, [j, j+1]))
        
    principal = ciclos[0]
    for ciclo in ciclos[1:]:
        print(ciclo) 
        for indice, vertice in enumerate(principal):
            if vertice in ciclo:
                for value in ciclo[1:-1]:
                    principal.insert(indice, value)
                break

    print(principal)
else:
    print('Existe algum vertice cujo o grau é impar')