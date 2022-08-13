from email.mime import image
from tkinter import *
from turtle import bgcolor



root = Tk()
root.title("Bienvenido a tu Calculadora de IMC \n")
root.geometry("700x400")
root.config(bg="#434F71")



frame1 = LabelFrame(root,text="Calculador de Indice de Masa Corporal", font=("calibri", 14))
frame2 = LabelFrame(root,text="Resultado", font=("calibri", 14))

frame1.pack(fill="both", expand="yes", padx=20, pady=15)
frame2.pack(fill="both", expand="yes", padx=20, pady=15)

peso = IntVar()
altura = DoubleVar()
imc = StringVar()


#==============================================================
def mostrar():
    imc.set(str((peso.get())/(altura.get()* altura.get())))

def reiniciar():
    peso.set("")  
    altura.set("") 
    imc.set("")

#==============================================================

lbl1 = Label(frame1, text="Ingrese su peso en Kgs: ", width=20)
lbl1.grid(row=0, column=0, padx=5, pady=3)
entMat = Entry(frame1,textvariable=peso)   
entMat.grid(row=0, column=1, padx=5, pady=3) 


lbl1 = Label(frame1, text="Ingrese su altura en Mts:", width=20)
lbl1.grid(row=1, column=0, padx=5, pady=3)
entMat2 = Entry(frame1,textvariable=altura)   
entMat2.grid(row=1, column=1, padx=5, pady=3) 




lbl1 = Label(frame2, text="IMC", width=20)
lbl1.grid(row=0, column=0, padx=5, pady=3)
entpromedio = Entry(frame2,textvariable=imc)   
entpromedio.grid(row=0, column=1, padx=5, pady=3) 

btn1 = Button(frame2, text="Calcular IMC", width=10, height=2,command=mostrar)
btn1.grid(row=3, column=1, padx=10, pady=10)

btn2 = Button(frame2, text="Reiniciar", width=10, height=2,command=reiniciar)
btn2.grid(row=3, column=3, padx=10, pady=10)







root.mainloop()