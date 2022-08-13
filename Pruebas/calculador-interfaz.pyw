from tkinter import *

raiz = Tk()
#root= Tk()


miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroPeso=Entry(miFrame)
cuadroPeso.grid(row=0, column=1)

cuadroAltura=Entry(miFrame)
cuadroAltura.grid(row=1, column=1)

cuadroResultado=Entry(miFrame)
cuadroResultado.grid(row=2, column=1)

pesoLabel=Label(miFrame, text="Ingrese su Peso:")
pesoLabel.grid(row=0, column=0, sticky=W)

alturaLabel=Label(miFrame, text="Ingrese su Altura:")
alturaLabel.grid(row=1, column=0, sticky=W)

resultadoLabel=Label(miFrame, text="Su Indice de Masa Corporal es :")
resultadoLabel.grid(row=2, column=0, sticky=W)



#miImagen=PhotoImage(file="imagen.png")

#Label(miFrame, text="Calculadora IMC", fg="#34495E", font=("Comic Sans MS", 18)).place(x=10, y=10)


raiz.mainloop()