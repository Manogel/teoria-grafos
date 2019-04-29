from representacoes.Grafo import *
import numpy as np


class MatrizIncidencia(Grafo):
    def __init__(self, txtVertice, txtArestas, dirigido=0):
        super().__init__(txtVertice, txtArestas, dirigido)
        self.grafo = self.matrizIncidencia()

    def matrizIncidencia(self):
        # Retorna a representação do grafo por matriz de incidencia
        auxArestas = list()
        for aresta in self.arestas:
            if aresta not in auxArestas and (aresta[1], aresta[0]) not in auxArestas:
                auxArestas.append(aresta)
        grafo = np.zeros((len(self.vertices), len(auxArestas)), dtype=np.int)
        for index, aresta in enumerate(auxArestas):
            indexV1 = self.vertices.index(aresta[0])
            indexV2 = self.vertices.index(aresta[1])
            grafo[indexV1][index] = 1
            if self.dirigido == True:
                grafo[indexV2][index] = -1
            else:
                grafo[indexV2][index] = 1
        self.arestas = auxArestas
        return grafo

    def addVertice(self):
        # Adiona um vertice
        print('UM VERTICE FOI ADICIONADO')
        new_vertice = np.zeros((len(self.arestas)), dtype=np.int)
        auxGrafo = list(self.grafo)
        auxGrafo.append(new_vertice)
        auxGrafo = np.array(auxGrafo)
        self.vertices.append(max(self.vertices)+1)
        self.grafo = auxGrafo
        return True

    def addAresta(self, v1, v2):
        # Adiciona uma aresta
        print('ADICIONAR ARESTA')
        '''v1 = int(input('Insira o vertice1 de incidencia: '))
        v2 = int(input('Insira o vertice2 de incidencia: '))'''

        if v1 not in self.vertices or v2 not in self.vertices:
            print(
                f'ERRO, {v1} e/ou {v2} não pertence ao seu conjunto V(G): {self.vertices}')
            return False
        if (v1, v2) in self.arestas or (v2, v1) in self.arestas:
            print(f'ERRO, aresta informada ja exite em seu conjunto de arestas!')
            return False
        indexV1 = self.vertices.index(v1)
        indexV2 = self.vertices.index(v2)
        auxGrafo = list()
        grafo = list(self.grafo)
        for index, coluna in enumerate(self.grafo):
            auxColuna = list(coluna)
            if indexV1 == index:
                auxColuna.append(1)
            elif indexV2 == index:
                auxColuna.append(1)
            else:
                auxColuna.append(0)
            auxGrafo.append(np.array(auxColuna))
        self.arestas.append((v1, v2))
        self.grafo = np.array(auxGrafo)
        return True

    def dropVertice(self, conjunto_vertices, conjunto_arestas, grafo):
        '''Remove um vertice do meu grafo e atualiza a representação do grafo,
        o conjunto de arestas e vertices'''
        print('REMOVE VERTICE')
        vertice = int(
            input(f'Dado V(G): {conjunto_vertices}, informe o vertice: '))
        if vertice not in conjunto_vertices:
            print(
                f'ERRO, {vertice} não pertence ao seu conjunto de vertices!!')
            return conjunto_vertices, conjunto_arestas, grafo
        indexVertice = conjunto_vertices.index(vertice)
        grafo = np.delete(grafo, indexVertice, 0)
        auxConjArestas = conjunto_arestas[::-1]
        for value in auxConjArestas:
            if vertice in value:
                indexRemocao = conjunto_arestas.index(value)
                grafo = np.delete(grafo, indexRemocao, 1)
                conjunto_arestas.remove(value)
        return conjunto_vertices, conjunto_arestas, grafo

    def dropAresta(self, conjunto_vertices, conjunto_arestas, grafo):
        ''' Remove uma aresta e atualiza a representação do grafo, tambem, o conjunto de arestas'''
        print('REMOVE ARESTA')
        v1 = int(input('Insira o vertice1 de incidencia: '))
        v2 = int(input('Insira o vertice2 de incidencia: '))

        if v1 not in conjunto_vertices or v2 not in conjunto_vertices:
            print(
                f'ERRO, {v1} e/ou {v2} não pertence ao seu conjunto V(G): {conjunto_vertices}')
            return conjunto_arestas, grafo
        if (v1, v2) not in conjunto_arestas and (v2, v1) not in conjunto_arestas:
            print(f'ERRO, aresta informada não exite em seu conjunto de arestas!')
            return conjunto_arestas, grafo
        try:
            indexAresta = conjunto_arestas.index((v1, v2))
        except:
            indexAresta = conjunto_arestas.index((v2, v1))
            (v1, v2) = (v2, v1)
        grafo = np.delete(grafo, indexAresta, 1)
        conjunto_arestas.remove((v1, v2))
        return conjunto_arestas, grafo

    def visitarVertice(self, conjunto_vertices, conjunto_arestas, grafo):
        ''' Faz uma visita no vertice desejado e retorna todos os seus dados'''
        print('VISITAR VERTICE')
        vertice = int(
            input(f'Dado V(G): {conjunto_vertices}, informe o vertice a ser visitado:'))
        if vertice not in conjunto_vertices:
            print(
                f'ERRO, {vertice} não faz parte do seu conjunto de vertices!!')
        indexVertice = conjunto_vertices.index(vertice)
        visita = list(grafo[indexVertice])
        dadoTxt = f'E({vertice}) = ' + '{'
        for incide, value in enumerate(visita):
            if value == 1:
                dadoTxt = dadoTxt + f'{conjunto_arestas[incide]}, '
        print(dadoTxt[:-2] + '}')
