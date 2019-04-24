from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
from representacoes.listaAdj import *
from representacoes.setGrafo import *

class Tela_grafo:
    def __init__(self, master, grafo):
        self.master = master
        self.master.geometry('550x240')
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
        self.createMenu()
        self.createVisualizacao()

    def createVisualizacao(self):
        self.txt = scrolledtext.ScrolledText(
            self.container2, width=55, height=10, wrap=WORD)
        self.txt['state'] = DISABLED
        self.txt.pack(side=RIGHT)
        self.attRepresentacao()

    def createMenu(self):
        self.container11 = Frame(self.container1)
        self.container11.pack(side=LEFT)
        self.btnAddVertice = Button(
            self.container11, text='Adicionar vertice', width=17, padding=2, command = self.addVertice)
        self.btnAddVertice.pack()
        self.btnAddAresta = Button(
            self.container11, text='Adicionar aresta', width=17, padding=2)
        self.btnAddAresta.pack()
        self.btnDropVertice = Button(
            self.container11, text='Remove vertice', width=17, padding=2)
        self.btnDropVertice.pack()
        self.btnDropAresta = Button(
            self.container11, text='Remove aresta', width=17, padding=2)
        self.btnDropAresta.pack()

    def addVertice(self):
        self.Grafo.addVertice()
        self.attRepresentacao()
    
    def attRepresentacao(self):
        self.txt['state'] = NORMAL
        self.txt.delete('1.0', END)
        self.txt.insert(INSERT, self.Grafo.listarGrafo())
        self.txt['state'] = DISABLED
        

