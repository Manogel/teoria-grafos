from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import *
from interface.grafo import *
from representacoes.listaAdjacecia import *
from representacoes.matrizIncidencia import *

class Start_grafo:
    def __init__(self, master=None, txt='representacao'):
        self.master = master
        self.master.geometry('480x280')
        lblTitle = Label(
            self.master, text=txt, font="Times 12 bold", padding=5)
        lblTitle.pack(side=TOP) 
        self.start()  
     
    def start(self):
        frameIncial = Frame(self.master)
        frameIncial.pack()
        frameVertices = Frame(frameIncial, padding = 5)
        frameVertices.pack()
        frameArestas = Frame(frameIncial, padding = 5)
        frameArestas.pack()
        frameDirecional = Frame(frameIncial, padding = 5)
        frameDirecional.pack()
        frameButton = Frame(frameIncial, padding = 5)
        frameButton.pack()

        self.lblVertices = Label(frameVertices, text='Informe a V(G): ')
        self.lblVertices.pack()
        self.inpVertices = Entry(frameVertices, width = 50)
        self.inpVertices.pack()

        self.lblArestas = Label(frameArestas, text='Informe a E(G): ')
        self.lblArestas.pack()
        self.inpArestas = Entry(frameArestas, width = 50)
        self.inpArestas.pack()

        self.checkBox = IntVar()
        self.boxDirecional = Checkbutton(frameDirecional, text = 'Grafo direcional', variable = self.checkBox)
        self.boxDirecional.pack()

        self.btnGrafo = Button(frameButton, text = 'Incializar Grafo', width = 20, padding = 3, command = self.setGrafo)
        self.btnGrafo.pack(side=BOTTOM)

        self.lblObs = Label(self.master, text = '''
        OBS: Considere entrada perfeita!
        Para entrada de vertices, utilize: { X1, X2, X3, ..., Xn}
        Para entrada de arestas, utilize: { (X1, X2) - (X3, X1) - ... - (Xn, Xm)}
        ''', foreground = 'red')

        self.lblObs.pack(side=BOTTOM)
    
    def setGrafo(self):
        # {0, 1, 2, 3}
        # {(0, 1) - (1, 2) - (3, 0) - (2, 3)}
        direcional = self.checkBox.get()
        vertices = self.inpVertices.get()
        arestas = self.inpArestas.get()
        Grafo = MatrizIncidencia('{0, 1, 2, 3}', '{(0, 1) - (1, 2) - (3, 0) - (2, 3)}', direcional)

        self.limpaTela()
        Tela_grafo(self.master, Grafo)
    
    def limpaTela(self):
        for widget in self.master.winfo_children():
            widget.destroy()