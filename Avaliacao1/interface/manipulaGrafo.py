from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
from representacoes.listaAdjacecia import *
#from representacoes.setGrafo import *
from representacoes.matrizIncidencia import *


class Tela_grafo:
    def __init__(self, master, grafo, representacao):
        self.representacao = representacao
        self.master = master
        self.master.geometry('750x440')
        lblTitle = Label(
            self.master, text='Listar Grafo', font="Times 12 bold", padding=5)
        lblTitle.pack(side=TOP)
        self.Grafo = grafo
        self.createWidget()
        pass

    def createWidget(self):
        framePrincipal = Frame(self.master, padding=15)
        framePrincipal.pack()
        self.container1 = Frame(framePrincipal, padding=1)
        self.container1.pack(side=LEFT)
        auxTxt = Label(framePrincipal, text='             ')
        auxTxt.pack(side=LEFT)
        self.container2 = Frame(framePrincipal, padding=1)
        self.container2.pack(side=RIGHT)
        self.container11 = Frame(self.container1)
        self.container11.pack(side=LEFT)
        self.createVisualizacao()
        self.createMenu()

    def createVisualizacao(self):
        self.txt = scrolledtext.ScrolledText(
            self.container2, width=57, height=22, wrap=WORD)
        self.txt['state'] = DISABLED
        self.txt.pack(side=RIGHT)

    def createMenu(self):
        self.attRepresentacao()
        self.limpaFrame(self.container11)
        self.btnAddVertice = Button(
            self.container11, text='Adicionar vertice', width=17, padding=8, command=self.addVertice)
        self.btnAddVertice.pack()
        self.lblSeparator = Label(
            self.container11, text='', padding=0)
        self.lblSeparator.pack()
        self.btnAddAresta = Button(
            self.container11, text='Adicionar aresta', width=17, padding=8, command=self.adicionaAresta)
        self.btnAddAresta.pack()
        self.lblSeparator = Label(
            self.container11, text='', padding=0)
        self.lblSeparator.pack()
        self.btnDropVertice = Button(
            self.container11, text='Remove vertice', width=17, padding=8, command=self.removeVertice)
        self.btnDropVertice.pack()
        self.lblSeparator = Label(
            self.container11, text='', padding=0)
        self.lblSeparator.pack()
        self.btnDropAresta = Button(
            self.container11, text='Remove aresta', width=17, padding=8, command=self.removeAresta)
        self.btnDropAresta.pack()
        self.lblSeparator = Label(
            self.container11, text='', padding=0)
        self.lblSeparator.pack()
        self.btnVisitaVertice = Button(
            self.container11, text='Visitar Vertice', width=17, padding=8, command=self.visitaVertice)
        self.btnVisitaVertice.pack()

    def addVertice(self):
        self.Grafo.addVertice()
        self.attRepresentacao()

    def attRepresentacao(self, text=None):
        if text == None:
            text = self.Grafo.listarGrafo()

        text = f'{self.representacao}'.center(60) + '\n' + text
        self.txt['state'] = NORMAL
        self.txt.delete('1.0', END)
        self.txt.insert(INSERT, text)
        self.txt['state'] = DISABLED

    def removeAresta(self):
        self.limpaFrame(self.container11)
        self.lblVertice1 = Label(
            self.container11, text='Vertice incidente:', padding=2)
        self.lblVertice1.pack()
        self.inpVertice1 = Entry(
            self.container11, width=17)
        self.inpVertice1.pack()

        self.lblVertice2 = Label(
            self.container11, text='Vertice incidente:', padding=2)
        self.lblVertice2.pack()
        self.inpVertice2 = Entry(
            self.container11, width=17)
        self.inpVertice2.pack()

        self.lblSeparator = Label(
            self.container11, text='', padding=0)
        self.lblSeparator.pack()

        self.btnAttArestas = Button(
            self.container11, text='Remover', width=17, padding=8, command=self.dropAresta)
        self.btnAttArestas.pack()
        self.lblSeparator = Label(
            self.container11, text='', padding=0)
        self.lblSeparator.pack()
        self.btnVoltar = Button(
            self.container11, text='Voltar', width=17, padding=8, command=self.createMenu)
        self.btnVoltar.pack()
        pass

    def adicionaAresta(self):
        self.limpaFrame(self.container11)
        self.lblVertice1 = Label(
            self.container11, text='Vertice incidente:', padding=2)
        self.lblVertice1.pack()
        self.inpVertice1 = Entry(
            self.container11, width=17)
        self.inpVertice1.pack()

        self.lblVertice2 = Label(
            self.container11, text='Vertice incidente:', padding=2)
        self.lblVertice2.pack()
        self.inpVertice2 = Entry(
            self.container11, width=17)
        self.inpVertice2.pack()

        self.lblSeparator = Label(
            self.container11, text='', padding=0)
        self.lblSeparator.pack()

        self.btnAttArestas = Button(
            self.container11, text='Adicionar', width=17, padding=8, command=self.addAresta)
        self.btnAttArestas.pack()

        self.lblSeparator = Label(
            self.container11, text='', padding=0)
        self.lblSeparator.pack()

        self.btnVoltar = Button(
            self.container11, text='Voltar', width=17, padding=8, command=self.createMenu)
        self.btnVoltar.pack()
        pass

    def removeVertice(self):
        self.limpaFrame(self.container11)
        self.lblVertice1 = Label(
            self.container11, text='Vertice:', padding=2)
        self.lblVertice1.pack()
        self.inpVertice = Entry(
            self.container11, width=17)
        self.inpVertice.pack()

        self.lblVertice2 = Label(
            self.container11, text='', padding=0)
        self.lblVertice2.pack()

        self.btnAttArestas = Button(
            self.container11, text='Remover', width=17, padding=8, command=self.dropVertice)
        self.btnAttArestas.pack()

        self.lblSeparator = Label(
            self.container11, text='', padding=0)
        self.lblSeparator.pack()

        self.btnVoltar = Button(
            self.container11, text='Voltar', width=17, padding=8, command=self.createMenu)
        self.btnVoltar.pack()
        pass

    def dropAresta(self):
        vertice1 = int(self.inpVertice1.get())
        vertice2 = int(self.inpVertice2.get())
        self.Grafo.dropAresta(vertice1, vertice2)
        self.attRepresentacao()

    def addAresta(self):
        vertice1 = int(self.inpVertice1.get())
        vertice2 = int(self.inpVertice2.get())
        self.Grafo.addAresta(vertice1, vertice2)
        self.attRepresentacao()

    def visitaVertice(self):
        self.limpaFrame(self.container11)
        self.lblVertice1 = Label(
            self.container11, text='Vertice:', padding=2)
        self.lblVertice1.pack()
        self.inpVertice = Entry(
            self.container11, width=17)
        self.inpVertice.pack()

        self.lblVertice2 = Label(
            self.container11, text='', padding=0)
        self.lblVertice2.pack()

        self.btnAttArestas = Button(
            self.container11, text='Visitar', width=17, padding=8, command=self.visVertice)
        self.btnAttArestas.pack()

        self.lblSeparator = Label(
            self.container11, text='', padding=0)
        self.lblSeparator.pack()

        self.btnVoltar = Button(
            self.container11, text='Voltar', width=17, padding=8, command=self.createMenu)
        self.btnVoltar.pack()

    def visVertice(self):
        vertice = int(self.inpVertice.get())
        text = self.Grafo.visitarVertice(vertice)
        self.attRepresentacao(text)

    def dropVertice(self):
        vertice = int(self.inpVertice.get())
        self.Grafo.dropVertice(vertice)
        self.attRepresentacao()

    def limpaFrame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
