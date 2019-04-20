import numpy as np

grafo = np.zeros((5, 5), dtype=np.int)


# Tenho uma matriz que representa um grafo DIRECIONADO de 5 vetices, V(G) :{ 0, 1, 2, 3, 4}
#Considere o software com entrada perfeita!!!

grafo[1, 3] = 1
# Uma aresta que vai de um vertice X para o vertice Y, é representado por  grafo[X, Y] = 1
#   Onde X é minha origem e Y é o destino!!

grafo[3, 2] = 1
grafo[2, 4] = 1
grafo[4, 3] = 1
grafo[3, 2] = 1
grafo[2, 1] = 1

def verificaPasseio(sequencia):
    # print(sequencia)
    if (grafo[sequencia[0], sequencia[1]]) == 1:
        if len(sequencia) == 2:
            return True
        return verificaPasseio(sequencia[1:])
    else:
        return False

def verificaCaminhoSimples(sequencia):
    # Não pode haver a repetição de vertices
    if len(sequencia) != len(set(sequencia)):
        return False
    return verificaPasseio(sequencia)

def analisaAresta(aresta, sequencia):
    # Analisa se há repetição da aresta repassada
    # E se houver, retorna False
    if(aresta != sequencia[:2]):
        if len(sequencia) == 2:
            return True
        return analisaAresta(aresta, sequencia[1:])
    else:
        return False

def verificaTrilha(sequencia):
    # Utilizando funçoes ja existentes, verifica se é uma trilha
    if len(sequencia) == 2:
        return True
    return analisaAresta(sequencia[:2], sequencia[1:]) and verificaPasseio(sequencia) and verificaTrilha(sequencia[1:])

def analisaGrafo(sequencia):
    try:
        import ast
        sequencia = ast.literal_eval(sequencia)
        txt = ''
        if verificaPasseio(sequencia):
            if sequencia[0] == sequencia[-1]:
                print('É um passeio fechado')
                txt += 'É um passeio fechado\n'
            else:
                print('É um passeio aberto')
                txt += 'É um passeio aberto\n'

        if verificaTrilha(sequencia):
            if sequencia[0] == sequencia[-1]:
                print('É uma trilha fechada')
                txt += 'É uma trilha fechada\n'
            else:
                print('É uma trilha aberta')
                txt += 'É uma trilha aberta\n'

        if verificaCaminhoSimples(sequencia):
            print('É um caminho simples')
            txt += 'É um caminho simples\n'
        if verificaTrilha(sequencia) and sequencia[0] == sequencia[-1]:
            if (len(sequencia[1:]) != len(set(sequencia))):
                print('É um ciclo')
                txt += 'É um ciclo\n'
            elif (len(sequencia[1:]) >= 3):
                print('É um ciclo simples')
                txt += 'É um ciclo simples\n'
        if txt == '':
            txt += 'Esse "trajeto" não é possivel'
        return txt
    except:
        return 'Entrada invalida'

""" import sys
param = sys.argv[1:]

sequencia = list()
for valor in param:
    sequencia.append(int(valor))
print(sequencia)
analisaGrafo(sequencia) """
