from representacoes.Grafo import *
import numpy as np


class MatrizAdjacencia(Grafo):
    def __init__(self, txtVertice, txtArestas, dirigido=0):
        super().__init__(txtVertice, txtArestas, dirigido)
        self.grafo = self.matrizAdjacencia()

    def matrizAdjacencia(self):
        # Retorna a representação do grafo por matriz de adjacencia
        qntVertices = len(self.vertices)
        grafo = np.zeros((qntVertices, qntVertices), dtype=np.int)
        for v1, v2 in self.arestas:
            grafo[v1][v2] = 1
        return grafo

    def addVertice(self):
        # Adiciona um vertice ao meu conjunto de vertices
        print('FOI ADICIONADO UM VERTICE')
        nVertices = len(self.vertices)
        vertice = np.zeros((nVertices), dtype=np.int)
        self.grafo = list(self.grafo)
        self.grafo.append(vertice)
        self.vertices.append(max(self.vertices)+1)
        auxGrafo = list()
        for coluna in self.grafo:
            auxColuna = list(coluna)
            auxColuna.append(0)
            auxGrafo.append(np.array(auxColuna))
        auxGrafo = np.array(auxGrafo)
        self.grafo = auxGrafo
        return True

    def dropVertice(self, vertice):
        '''Remove um vertice ao meu conjunto de vertices, após a remocao, é atualizada
        a variavel "GRAFO" que é a representação do grafo, alem disso, é removido todas as arestas que
        que estavam incidindo neste vertice'''
        print('REMOVE VERTICE')
        """ vertice = int(
            input(f'Dado V(G): {conjunto_vertices}, deseja remover qual?\n')) """
        if vertice not in self.vertices:
            return False
        auxArestas = self.arestas[:]
        for aresta in self.arestas:
            if vertice in aresta:
                auxArestas.remove(aresta)
        indexRemocao = self.vertices.index(vertice)
        self.grafo = np.delete(self.grafo, indexRemocao, 0)
        self.grafo = np.delete(self.grafo, indexRemocao, 1)
        self.vertices.remove(vertice)
        self.arestas = auxArestas
        return True

    def addAresta(self, v1, v2):
        '''Adiciona uma aresta ao meu conjunto de arestas, após a adição, é atualizada
        a variavel "GRAFO" que é a representação do grafo'''
        print('ADICIONA ARESTA')
        """ v1 = int(input("Informe o vertice1 de incidencia: "))
        v2 = int(input("Informe o vertice2 de incidencia: ")) """
        if self.dirigido == True and (v1, v2) in self.arestas:
            print(f'ERRO, aresta informada ja exite em seu conjunto de arestas!')
            return False

        if self.dirigido == False and (v1, v2) in self.arestas or (v2, v1) in self.arestas:
            print(f'ERRO, aresta informada ja exite em seu conjunto de arestas!')
            return False

        indexVertice1 = self.vertices.index(v1)
        indexVertice2 = self.vertices.index(v2)
        # print(grafo)
        if (v1, v2) not in self.arestas:
            self.arestas.append((v1, v2))
            self.grafo[indexVertice1][indexVertice2] = 1
        if (v2, v1) not in self.arestas and self.dirigido == False:
            self.arestas.append((v2, v1))
            self.grafo[indexVertice2][indexVertice1] = 1
        return True

    def dropAresta(self, v1, v2):
        '''
            Remove uma aresta do conjunto de arestas, após a remoção, é atualizada
        a variavel "GRAFO" que é a representação do grafo
        '''
        print('REMOVE ARESTA')
        """ v1 = int(input("Informe o vertice1 de incidencia: "))
        v2 = int(input("Informe o vertice2 de incidencia: ")) """

        if v1 not in self.vertices or v2 not in self.vertices:
            print(
                f'ERRO, {v1} e/ou {v2} não pertence ao seu conjunto V(G): {self.vertices}')
            return False

        if (v1, v2) not in self.arestas and self.dirigido == True:
            print(f'ERRO, aresta informada não exite em seu conjunto de arestas!')
            return False

        if (v1, v2) not in self.arestas and (v2, v1) not in self.arestas:
            print(f'ERRO, aresta informada não exite em seu conjunto de arestas!')
            return False

        indexVertice1 = self.vertices.index(v1)
        indexVertice2 = self.vertices.index(v2)

        if (v1, v2) in self.arestas:
            self.arestas.remove((v1, v2))
            self.grafo[indexVertice1][indexVertice2] = 0

        if (v2, v1) in self.arestas and self.dirigido == False:
            self.arestas.remove((v2, v1))
            self.grafo[indexVertice2][indexVertice1] = 0
        return True

    def visitarVertice(self, vertice):
        # Dado um vertice, é feita a consulta imprimindo todos os dados referentes àquele vertice
        print('CONSULTA VERTICE')
        """ vertice = int(
            input(f"Dado V(G): {conjunto_vertices}, deseja visitar qual?\n")) """
        if vertice not in self.vertices:
            return f'ERRO, vetice {vertice} não pertence ao seu conjunto V(G)'
        indexVertice = self.vertices.index(vertice)
        dadoTxt = f'E({vertice}) = ' + '{'
        for incide, value in enumerate(self.grafo[indexVertice]):
            if value == 1:
                dadoTxt = dadoTxt + f'({vertice},{self.vertices[incide]}), '
                if self.dirigido == False:
                    dadoTxt = dadoTxt + \
                        f'({self.vertices[incide]}, {vertice}), '
        if self.dirigido == True:
            return dadoTxt[:-2] + '} ' + f'\n\nSomente arestas que sai do vertice {vertice}!!'
        else:
            return dadoTxt[:-2] + '} '
