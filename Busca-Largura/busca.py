vertice_inicial = int(input('Digite um vertice de 0 a 4: '))

def getGrafo():
    grafo[0] = [1]
    grafo[1] = [3, 2]
    grafo[2] = [4]
    grafo[3] = [0, 4]
    grafo[4] = [1]
    return grafo

grafo = getGrafo()
fila = list()
n_vertices = len(grafo)
visita = [0]*n_vertices

print(f'Lista de visita{visita}')
print(f'Lista de adjacencia {grafo}')
print(f'fila {fila}')

fila.append(vertice_inicial)
visita[vertice_inicial] = 1
cont = 1
print(fila, cont)
while (len(fila) != 0):
    for vertice in grafo[fila[0]]:
        if visita[vertice] == 0:
            cont += 1
            # print(vertice)
            fila.pop(0)
            fila.append(vertice)
            visita[vertice] = cont
            print(fila, cont)
        elif (cont == 5):
            fila.pop(0)
            print(fila, cont)
            break
