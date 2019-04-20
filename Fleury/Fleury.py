import numpy as np 

def escolheGrafo (escolha):
    if escolha == 1:
        #lista de incidencia
        cj_arestas = [(0,3), (0,4), (4,1), (1,5), (5,2), (2,6), (3,4), (4,5), (5,6)]
        grafo = np.zeros((7,len(cj_arestas)), dtype=np.int)
        #a, b, c, d, e, f, g, h, i respectivamente em um grafo não direcional
    elif escolha == 2:
        cj_arestas = [(0,1), (1,2), (4,5), (5,0),(3,2), (3,4), (0,6), (6,5), (5,7), (7,4), (4,8), (8,3), (3,9), (9,2), (2,10), (10,1), (1,11), (11,0)]
        grafo = np.zeros((12,len(cj_arestas)), dtype=np.int)
    elif escolha == 3:
        cj_arestas = [(0,1), (1,2), (2,3), (3,4),(4,0), (0,3), (3,1)]
        grafo = np.zeros((5,len(cj_arestas)), dtype=np.int)
    
    for indice, arst in enumerate(cj_arestas):
        grafo[arst[0]][indice] = 1
        grafo[arst[1]][indice] = 1
    return grafo
    
def verificaGrau(grafo):
    #verifica se o grau de cada vertice é par
    contador = 0
    for x in range(len(grafo)):
        if (list(grafo[x]).count(1)) % 2 != 0:
            contador += 1
    if contador == 2:
        print('Grafo semi-euleriano')
        return True
    elif contador == 0:
        print('Grafo euleriano')
        return True
    else:
        print('Não é um grafo euleriano')
        
        return False

def algFleury(grafo):
    print("****Para grafos semi-eulerianos, é preciso escolher vertices de grau impar****")
    inicio = int(input(f'Este grafo tem vertices enumerados de 0 a {len(grafo)-1}!\nInforme o vertice inicial:'))
    if verificaGrau(grafo):
        contador = 0
        trilha = [inicio]
        print(len(grafo))

        while contador != 2*len(grafo[0]):
            #print(grafo)
            #trilha.append(inicio)
            for i, aresta in enumerate(grafo[inicio]):
                #print(inicio)
                #print(aresta)
                if aresta == 1:
                    grafo[inicio][i] = -1
                    contador += 1
                    for x in range(len(grafo)):
                        if grafo[x][i] == 1:
                            #print(f'achei na linha {x} e coluna {aresta}')
                            grafo[x][i] = -1
                            contador += 1
                            inicio = x
                            break
                    #print(contador)
                    trilha.append(inicio)
                    break
            if (list(grafo[inicio]).count(1)) == 0:
                break
        print(grafo)
        print(f'\n\nTrilha encontrada: {trilha}')

x = int(input('Informe a questao: '))
if x == 1: 
    grafo = escolheGrafo(1)
    algFleury(grafo)
elif x == 2:
    grafo = escolheGrafo(2)
    algFleury(grafo)
elif x == 3:
    grafo = escolheGrafo(3)
    algFleury(grafo)
    
###### LEIA O ARQUIVO README.MD ########


