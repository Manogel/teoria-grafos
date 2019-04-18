from checkCicle import verificaCiclo


def verificaDescoberta(peso, visitando, incide, descobertas, arvore):
    if ([peso, (visitando, incide)] not in descobertas) and ([peso, (incide, visitando)] not in descobertas) and ([peso, (visitando, incide)] not in arvore) and ([peso, (incide, visitando)] not in arvore):
        '''Esta é uma condição pra garantir que não ocorra uma redundancia do tipo,
        achei a aresta que liga o vertice 0 ao vertice 1, logo, é incoerente achar uma aresta "diferente"
        que liga o vertice 1 ao vertice 0 '''
        return True
    else:
        return False


grafo1 = [
    [[1, 1], [2, 5]],
    [[2, 2], [4, 2], [3, 5]],
    [[1, 2], [4, 2]],
    [[5, 2], [4, 1]],
    [[3, 1], [5, 4]],
    [[3, 2], [4, 4]]
]

grafo2 = [
    [[3, 5], [1, 7]],
    [[0, 7], [2, 8], [3, 9], [4, 7]],
    [[1, 8], [4, 5]],
    [[0, 5], [4, 15], [1, 9], [5, 6]],
    [[3, 15], [2, 5], [1, 7], [5, 8], [6, 9]],
    [[3, 6], [4, 8], [6, 11]],
    [[5, 11], [4, 9]]
]

grafo3 = [
    [[1, 9], [9, 9], [7, 8], [5, 18]],
    [[0, 9], [9, 3], [2, 6]],
    [[1, 6], [9, 4], [8, 2], [3, 9]],
    [[2, 9], [8, 9], [7, 7], [6, 5], [4, 4]],
    [[3, 4], [6, 1], [5, 4]],
    [[4, 4], [6, 3], [7, 10], [0, 18]],
    [[4, 1], [5, 3], [7, 9], [3, 5]],
    [[3, 7], [6, 9], [5, 10], [0, 8], [9, 9], [8, 8]],
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

grafo = grafo2

n_vertices = len(grafo)  # Numero de vertices
visitas = [0]*n_vertices  # Lista de visitas
visitando = 0  # Qual vertice iremos iniciar
descobertas = list()  # Aqui vai ser armazenado as arestas que foram descobertas
minha_arvore = list()  # Arvore minima a ser encontrada

while visitas != [1]*n_vertices:
    # Garantir que todos os vétices serão visitados
    if visitas[visitando] == 0:
        # Se não foi visitado, iniciar a busca
        visitas[visitando] = 1
        # Identificar que foi visitado
        for incide, peso in grafo[visitando]:
            #print(f'Sai do vertice {visitando} para o {incide} com peso {peso}')
            if verificaDescoberta(peso, visitando, incide, descobertas, minha_arvore):
                descobertas.append([peso, (visitando, incide)])
        descobertas.sort()  # Ordenamos as arestas mapeada por peso
        if verificaCiclo(minha_arvore, descobertas[0][1]) and verificaCiclo(minha_arvore, [descobertas[0][1][1], descobertas[0][1][0]]):
            # Garantir que não haverá a formação de ciclo e adiciono a aresta com menor peso
            minha_arvore.append(descobertas[0])
        # Agora, vou visitar o vertice cuja a areste de incidencia a ele tem peso minimo
        visitando = descobertas[0][1][1]
        descobertas.pop(0)  # Removo a aresta que eu ja analisei
    else:
        ''' Caso o vertice ja foi visitado, removemos a aresta que faz referencia a ele, e passamos a fazer uma nova visita
        em um outro vertice cuja a areste de incidencia a ele tem peso minimo'''
        if verificaCiclo(minha_arvore, descobertas[0][1]) and verificaCiclo(minha_arvore, [descobertas[0][1][1], descobertas[0][1][0]]):
            # Garantir que não haverá a formação de ciclo e adiciono a aresta com menor peso
            minha_arvore.append(descobertas[0])
        descobertas.pop(0)
        visitando = descobertas[0][1][1]
        if verificaCiclo(minha_arvore, descobertas[0][1]) and verificaCiclo(minha_arvore, [descobertas[0][1][1], descobertas[0][1][0]]):
            # Garantir que não haverá a formação de ciclo e adiciono a aresta com menor peso
            minha_arvore.append(descobertas[0])
    # print(descobertas)

print(visitas)
print(minha_arvore)
