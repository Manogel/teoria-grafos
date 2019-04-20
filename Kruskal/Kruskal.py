from checkCicle import verificaCiclo as Vc
from grafo import getArestas
grafo1 = [[[3, 5], [1, 7]],
          [[0, 7], [2, 8], [3, 9], [4, 7]],
          [[1, 8], [4, 5]],
          [[0, 5], [4, 15], [1, 9], [5, 6]],
          [[3, 15], [2, 5], [1, 7], [5, 8], [6, 9]],
          [[3, 6], [4, 8], [6, 11]],
          [[5, 11], [4, 9]]]

#[incidencia, peso]

grafo2 = [[[1, 4], [5, 4], [2, 3], [3, 7], [4, 1]],
          [[0, 4], [2, 9]],
          [[0, 3], [3, 3], [1, 9]],
          [[4, 2], [0, 7], [2, 3]],
          [[0, 1], [5, 5], [3, 2]],
          [[4, 5], [0, 4]]
          ]
grafo3 = [[[1, 9], [9, 9], [7, 8], [5, 18]],
          [[0, 9], [9, 3], [2, 6]],
          [[1, 6], [9, 4], [8, 2], [3, 9]],
          [[2, 9], [8, 9], [7, 7], [6, 5], [4, 4]],
          [[3, 4], [6, 1], [5, 4]],
          [[4, 4], [6, 3], [7, 10], [0, 18]],
          [[4, 1], [5, 3], [7, 10], [3, 5]],
          [[3, 7], [6, 9], [5, 10], [0, 8], [2, 9], [8, 8]],
          [[2, 2], [3, 9], [7, 8], [9, 2]],
          [[2, 4], [8, 2], [7, 9], [0, 9], [1, 3]]
          ]

grafo4 = [
    [[5, 80], [6, 47], [1, 54]],
    [[0, 54], [6, 75], [2, 74]],
    [[1, 74], [6, 88], [7, 31], [3, 29]],
    [[2, 29], [7, 79], [4, 68]],
    [[3, 68], [7, 74], [6, 66], [5, 93]],
    [[0, 80], [6, 23], [7, 32], [4, 93]],
    [[0, 47], [1, 75], [2, 88], [7, 55], [4, 66], [5, 23]],
    [[6, 55], [2, 31], [3, 79], [4, 74], [5, 32]]
]

grafo = grafo4
arestas = getArestas(grafo)
print(arestas)
minha_arvore = list()
contador = len(grafo)
vertices_arvore = list()
for peso, aresta in arestas:
    print(f'mandando analisar a aresta {aresta}')
    if Vc(minha_arvore, aresta) and Vc(minha_arvore, [aresta[-1], aresta[0]]):
        minha_arvore.append([peso, aresta])
        for vertice in aresta:
            if vertice not in vertices_arvore:
                vertices_arvore.append(vertice)
    if len(vertices_arvore) == contador and (len(vertices_arvore) - len(minha_arvore)) == 1:
        break


print('Arvore encontrada: ')
print(minha_arvore)
# 0a 1b 2c 3d 4e 5f 6g 7h
