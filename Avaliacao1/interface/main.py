from tkinter import *

class Tela:
    def __init__(self, master = None):
        self.master = master
        lblTitle = Label(self.master, text = ' Representação de Grafos ', pady = 6)
        lblTitle.pack()
        self.menuPrincipal()

    def menuPrincipal(self):
        self.container1 = Frame(self.master)
        self.container1.pack()

        self.btnListAdj = Button(self.container1, text = 'Lista de adjacencia', width = 24)
        self.btnListAdj.pack()

        self.btnMatInc = Button(self.container1, text = 'Matriz de Incidencia', width = 24)
        self.btnMatInc.pack()

        self.btnMatAdj = Button(self.container1, text = 'Matriz de Adjacencia', width = 24)
        self.btnMatAdj.pack()

        pass

    def createComponents(self):
        self.containerLeft = Frame(self.master)
        self.containerLeft.pack(side=LEFT)
        self.containerRight = Frame(self.master)
        self.containerRight.pack(side=RIGHT)
        label1 = Label(self.containerLeft, text = 'Text example 1')
        label1.pack()
        label2 = Label(self.containerRight, text = 'Text example 2')
        label2.pack()

        pass

telaPrincipal = Tk()
Tela(telaPrincipal)
telaPrincipal.mainloop()