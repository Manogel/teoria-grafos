import numpy as np


class Grafo(object):
    def __init__(self, txtVertice, txtArestas, dirigido):
        self.dirigido = dirigido
        self.vertices = self.getVertices(txtVertice)
        self.arestas = self.getArestas(txtArestas, self.vertices, dirigido)
        pass

    def getVertices(self, txtVertices):
        '''Recebo uma string contendo a lista de vertices do meu grafo, após isso, formato essa string para
        uma lista contendo valores inteiros'''
        """ vertices = str(input(
            'Informe seu conjunto de vertices denotado por {x1, x2, x3, ..., xn} :\n')).strip() """
        vertices = txtVertices
        aux = vertices[1:-1]
        vertices = aux.split(',')
        vertices = [int(e) for e in vertices]
        return vertices

    def getArestas(self, txtArestas, conjunto_vertices, dirigido=False):
        '''Recebo uma string contendo a lista de arestas do meu grafo, após isso, formato essa string para
        uma lista contendo uma tupla com valores inteiros, simbolisando a aresta, para cada aresta'''

        '''É recebido o meu conjunto de vertices pois, no momento que estamos formatando a minha lista de aresta,
        é feita a verificação se a existencia de uma conexão(aresta) coincide com meu conjunto de vertices!!
                EX: dado o conjunto_vertices = [0, 1], é impossivel a existencia da aresta (0, 2), pois, o 2 não existe
                    no meu conjunto de vertices'''

        """ arestas = str(input(
            'Informe seu conjunto de arestas denotado por {(x1, x2) - (x2, x3) - (..., ...) - (xn, xm)}:\n')).strip() """
        arestas = txtArestas
        arestas = arestas[1:-1]
        aux = arestas.split('-')
        lista_arestas = []
        for aresta in aux:
            aux = []
            aresta = aresta.strip()
            aresta = aresta[1:-1].split(',')
            for vertice in aresta:
                if int(vertice) not in conjunto_vertices:
                    print(
                        f'ERRO: O vertice {vertice} não se encontra em seu conjunto de vertices!')
                    return False
                aux.append(int(vertice))
            if tuple(aux) not in lista_arestas:
                lista_arestas.append(tuple(aux))
                if tuple([aux[-1], aux[0]]) not in lista_arestas and dirigido == False:
                    lista_arestas.append(tuple([aux[-1], aux[0]]))
        return lista_arestas

    def listarGrafo(self):
        # Imprime os dados de um grafo
        print(f'V(G): \n{self.vertices}')
        text = ''
        text = text + f'Grafo: \n{self.grafo}'
        text = text + f'\n\nV(G): \n{self.vertices}'
        text = text + f'\n\nE(G): \n{self.arestas}'
        return text
