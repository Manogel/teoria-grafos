from representacoes.setGrafo import *
import numpy as np

class ListaAdjacencia:
    def __init__(self, txtVertice, txtArestas, dirigido):
        self.dirigido = dirigido
        self.vertices = getVertices(txtVertice)
        self.arestas = getArestas(txtArestas, self.vertices, dirigido)
        self.grafo = self.listaAjacencia()
    
    def listaAjacencia(self):
        # Retorna a representação do grafo por lista de adjacencia
        grafo = list()
        for c in self.vertices:
            aux = []
            grafo.append(aux)

        for v1, v2 in self.arestas:
            if v2 not in grafo[v1]:
                grafo[v1].append(v2)
        return grafo

    def addVertice(self):
        # Adiciona um vertice ao meu conjunto de vertices
        print('UM VERTICE FOI ADICIONADO')
        self.vertices.append(max(self.vertices)+1)
        self.grafo.append([])

    def addAresta(self, v1, v2):
        '''Adiciona uma aresta ao meu conjunto de arestas, após a adição, é atualizada
        a variavel "GRAFO" que é a representação do grafo'''
        print('ADICIONAR UMA ARESTA')
        """print(f'Dado V(G) = {self.vertices}')
        v1 = int(input("- Vertice de incidencia 1: "))
        v2 = int(input("- Vertice de incidencia 2: ")) """
        if v1 not in self.vertices or v2 not in self.vertices:
            print(
                f'ERRO: {v1} e/ou {v2} não correspondem ao conjunto de vertices {self.vertices}!!')
            return False
        if (v1, v2) not in self.arestas:
            self.arestas.append((v1, v2))
        if (v2, v1) not in self.arestas and self.dirigido == False:
            self.arestas.append((v2, v1))
        indexAdicao1 = self.vertices.index(v1)
        indexAdicao2 = self.vertices.index(v2)
        if v2 not in self.grafo[indexAdicao1]:
            self.grafo[v1].append(v2)
        if v1 not in self.grafo[indexAdicao2] and self.dirigido == False:
            self.grafo[v2].append(v1)
        return True

    def dropVertice(self, vertice):
        '''Remove um vertice ao meu conjunto de vertices, após a remocao, é atualizada
        a variavel "GRAFO" que é a representação do grafo, alem disso, é removido todas as arestas que
        que estavam incidindo neste vertice'''
        print('REMOVE VERTICE')
        #vertice = int(input(f"Dado V(G): {self.vertices}, qual remover: "))
        if vertice not in self.vertices:
            print(f'ERRO: {vertice} não correspondem ao conjunto de vertices!!')
            return False
        else:
            indice_remocao = self.vertices.index(vertice)
            self.vertices.remove(vertice)
            del self.grafo[indice_remocao]
        auxArestas = self.arestas[:]
        for aresta in self.arestas:
            if vertice in aresta:
                auxArestas.remove(aresta)

        auxGrafo = self.grafo[:]
        for index, adjacencia in enumerate(self.grafo):
            if vertice in adjacencia:
                auxGrafo[index].remove(vertice)
        
        self.arestas = auxArestas
        self.grafo = auxGrafo
        return True


    def dropAresta(self, v1, v2):
        '''
            Remove uma aresta do conjunto de arestas, após a remoção, é atualizada
        a variavel "GRAFO" que é a representação do grafo
        '''
        print('REMOVER UMA ARESTA')
        """ v1 = int(input("- Vertice de incidencia 1: "))
        v2 = int(input("- Vertice de incidencia 2: ")) """
        if (v1, v2) in self.arestas:
            indexRemocao = self.vertices.index(v1)
            self.arestas.remove((v1, v2))
            self.grafo[indexRemocao].remove(v2)

        if (v2, v1) in self.arestas:
            indexRemocao = self.vertices.index(v2)
            self.arestas.remove((v2, v1))
            self.grafo[indexRemocao].remove(v1)

        return True


    def consultarVertice(vertice):
        # Dado um vertice, é feita a consulta imprimindo todos os dados referentes àquele vertice
        print('CONSULTAR VERTICE')
        """ vertice = int(
            input(f'Informe o vertice dado V(G) = {self.vertices}: \n')) """
        indexVertice = self.vertices.index(vertice)
        print(f'Consultando o vertice {vertice}: ')
        dadoTxt = f'E({vertice}) = ' + '{'
        for incide in self.grafo[indexVertice]:
            dadoTxt = dadoTxt + f'({vertice},{incide}), '
        print(dadoTxt[:-2] + '}')
    
    
        