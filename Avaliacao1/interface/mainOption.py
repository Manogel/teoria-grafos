from tkinter import *
from tkinter.ttk import *
from interface.manipulaGrafo import *
from interface.startGrafo import *


class Tela:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Teoria dos Grafos")
        self.master.geometry('220x170')
        self.master.resizable(False, False)
        self.master.deiconify()
        lblTitle = Label(
            self.master, text=' Representação de Grafos', font="Times 12 bold", padding=5)
        lblTitle.pack()
        self.menuPrincipal()

    def menuPrincipal(self):
        self.container1 = Frame(self.master, padding=10)
        self.container1.pack()

        self.btnListAdj = Button(
            self.container1, text='Lista de adjacencia', width=24, padding=5)
        self.btnListAdj['command'] = self.telaGrafo1
        self.btnListAdj.pack()

        self.btnMatInc = Button(
            self.container1, text='Matriz de Incidencia', width=24, padding=5, command=self.telaGrafo2)
        self.btnMatInc.pack()

        self.btnMatAdj = Button(
            self.container1, text='Matriz de Adjacencia', width=24, padding=5, command=self.telaGrafo3)
        self.btnMatAdj.pack()

        pass

    def createComponents(self):
        self.containerLeft = Frame(self.master)
        self.containerLeft.pack(side=LEFT)
        self.containerRight = Frame(self.master)
        self.containerRight.pack(side=RIGHT)
        label1 = Label(self.containerLeft, text='Text example 1')
        label1.pack()
        label2 = Label(self.containerRight, text='Text example 2')
        label2.pack()
        pass

    def telaGrafo1(self):
        self.limpaTela()
        Start_grafo(self.master, 1)
        pass

    def telaGrafo2(self):
        self.limpaTela()
        Start_grafo(self.master, 2)
        pass

    def telaGrafo3(self):
        self.limpaTela()
        Start_grafo(self.master, 3)
        pass

    def limpaTela(self):
        for widget in self.master.winfo_children():
            widget.destroy()
