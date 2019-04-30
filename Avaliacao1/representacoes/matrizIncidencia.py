from representacoes.Grafo import *
import numpy as np


class MatrizIncidencia(Grafo):
    def __init__(self, txtVertice, txtArestas, dirigido):
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

        if self.dirigido == True and (v1, v2) in self.arestas:
            print(f'ERRO, aresta informada ja exite em seu conjunto de arestas!')
            return False

        if self.dirigido == False and (v1, v2) in self.arestas or (v2, v1) in self.arestas:
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
                if self.dirigido == False:
                    auxColuna.append(1)
                else:
                    auxColuna.append(-1)
            else:
                auxColuna.append(0)
            auxGrafo.append(np.array(auxColuna))
        self.arestas.append((v1, v2))
        self.grafo = np.array(auxGrafo)
        return True

    def dropVertice(self, vertice):
        '''Remove um vertice do meu grafo e atualiza a representação do grafo,
        o conjunto de arestas e vertices'''
        print('REMOVE VERTICE')
        """ vertice = int(
            input(f'Dado V(G): {conjunto_vertices}, informe o vertice: ')) """
        if vertice not in self.vertices:
            print(
                f'ERRO, {vertice} não pertence ao seu conjunto de vertices!!')
            return False
        indexVertice = self.vertices.index(vertice)
        self.vertices.remove(vertice)
        self.grafo = np.delete(self.grafo, indexVertice, 0)
        auxConjArestas = self.arestas[::-1]
        for value in auxConjArestas:
            if vertice in value:
                indexRemocao = self.arestas.index(value)
                self.grafo = np.delete(self.grafo, indexRemocao, 1)
                self.arestas.remove(value)
        return True

    def dropAresta(self, v1, v2):
        ''' Remove uma aresta e atualiza a representação do grafo, tambem, o conjunto de arestas'''
        print('REMOVE ARESTA')
        """ v1 = int(input('Insira o vertice1 de incidencia: '))
        v2 = int(input('Insira o vertice2 de incidencia: ')) """

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
        try:
            indexAresta = self.arestas.index((v1, v2))
        except:
            indexAresta = self.arestas.index((v2, v1))
            (v1, v2) = (v2, v1)
        self.grafo = np.delete(self.grafo, indexAresta, 1)
        self.arestas.remove((v1, v2))
        return True

    def visitarVertice(self, vertice):
        ''' Faz uma visita no vertice desejado e retorna todos os seus dados'''
        print('VISITAR VERTICE')
        """ vertice = int(
            input(f'Dado V(G): {conjunto_vertices}, informe o vertice a ser visitado:')) """
        if vertice not in self.vertices:
            print(
                f'ERRO, {vertice} não faz parte do seu conjunto de vertices!!')
            return "Vertice não existente"
        indexVertice = self.vertices.index(vertice)
        visita = list(self.grafo[indexVertice])
        dadoTxt = f'E({vertice}) = ' + '{'
        for incide, value in enumerate(visita):
            if value == 1:
                dadoTxt = dadoTxt + f'{self.arestas[incide]}, '
        if self.dirigido == True:
            return dadoTxt[:-2] + '} ' + f'\n\nSomente arestas que sai do vertice {vertice}!!'
        else:
            return dadoTxt[:-2] + '} '
