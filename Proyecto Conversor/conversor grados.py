import tkinter
from tkinter import * 

raiz = tkinter.Tk()
raiz.title("Conversor de grados")

# ----- Configuración del aspecto general
#frame = tkinter.Frame(raiz)
#frame.config(bg="grey", width=600, height=600)
#frame.pack()

# e = Entry(raiz)
# e.grid(row=10, column=1 0, padx=10, pady=10)
# e.pack()
 
# etiqueta = tkinter.Label(raiz, text="Conversión de grados Celsius a Farenheit")
# etiqueta.pack()

def open():
    top = Toplevel()
    top.title("Conversor de grados")
    lbl = Label()
    btn2 = Button(top, text="Cerrar conversor", command=top.destroy).pack()

btn = Button(raiz, text="Conversor de grados", command=open).pack()




raiz.mainloop()