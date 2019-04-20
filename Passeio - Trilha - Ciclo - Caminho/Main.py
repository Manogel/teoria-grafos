
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from checkGraphs import analisaGrafo

class Tela:
    def __init__(self, master):
        self.tela = master
        self.tela.title("T. Grafos")
        self.tela2 = None
        self.createWidget()
        
    def createWidget(self):
        container1 = Frame(self.tela, pady = 10, padx=10)
        container1.pack()
        lblInfo = Label(container1, text = "Considere entrada perfeita!\nV(G) :{0, 1, 2, 3, 4}")
        lblInfo.pack()
        self.inpGrafo = Entry(container1)
        self.inpGrafo.bind("<Return>", self.analisaGrafo)
        self.inpGrafo.pack(side=LEFT)
        self.btnVerificar = Button(container1, text="Verificar")
        self.btnVerificar.bind("<Button-1>", self.analisaGrafo)
        self.btnVerificar.pack(side=LEFT)
    
    def analisaGrafo(self, event):
        if self.tela2 is None:
            self.tela2 = Tk()
            self.tela2.title("T. Grafos")
            self.tela2.bind("<Return>", self.__fechaResultado)
            self.monty = ttk.LabelFrame(self.tela2, text='Resposta')
            self.monty.pack()
            self.scr = scrolledtext.ScrolledText(self.monty, width=25, height=8, wrap=WORD)
            self.scr.pack()
            self.close = ttk.Button(self.tela2, text="Ok/Fechar")
            self.close.pack()
            self.scr['state'] = NORMAL
            self.scr.delete('1.0', END)
            self.scr.insert(INSERT, analisaGrafo(self.inpGrafo.get()))
            self.scr['state'] = DISABLED
            self.tela2.protocol("WM_DELETE_WINDOW", self.__fechaResultado)
            self.close['command'] = self.__fechaResultado
        else:
            self.tela2.lift()

    def __fechaResultado(self, event= None):
        self.tela2.destroy()
        self.tela2 = None
        
tela = Tk()
Tela(tela)
tela.mainloop()
