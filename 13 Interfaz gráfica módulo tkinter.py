
# ------------- INTERFAZ GRÁFICA: MÓDULO TKINTER

# Las interfaces gráficas son medios visuales que permiten a los usuarios interactuar
# con nuestro programa de forma gráfica
# El módulo tkinter tiene una serie de componentes llamados widgets, que son componentes gráficos


# ------------- TK es el componente que contiene al resto de los componentes (el elemento raíz)

# Se importa módulo tkinter
import tkinter 

# Se usa el método Tk que devuelve el elemento raíz
raiz = tkinter.Tk()

# Se la nombre a la ventana con title()
raiz.title("Mi programa")

# Se usa mainloop() para que siempre se ejecute
raiz.mainloop()




# ------------- FRAME es un marco que puede contener otros componentes y que tienen un tamaño propio.

# Parte común en todos los programas
import tkinter

raiz = tkinter.Tk()
raiz.title("Programa Frame")

# Parte específica en los programas

# Se le pasa por parámetro sobre qué raíz tiene que crear el Frame
# Devuelve un objeto tipo frame
frame = tkinter.Frame(raiz)

# Se puede configurar
frame.config(bg="blue", width=400, height=300)

# Se muestra por pantalla mediante:
frame.pack()

# Parte común en todos los programas
raiz.mainloop()




# ------------- LABEL es una etiqueta donde podemos insertar un texto. 

import tkinter

raiz = tkinter.Tk()
raiz.title("Programa LABEL")

# Variable con el texto
texto = "Hola mundo"

# Método .Label con 2 parámetros: Componente sobre el que se va a crear (raíz) y el texto que mostrará (variable texto)
# Devuelve una etiqueta
etiqueta = tkinter.Label(raiz, text=texto)

# Se configura la etiqueta
# fg=letras, bg=fondo font=tipo de fuente y tamaño
etiqueta.config(fg="green",bg="lightgrey",font=("Cortana",30))

# Se muestra por pantalla mediante:
etiqueta.pack()

raiz.mainloop()



# ------------- Entry es un campo de texto sencillo para escribir un texto corto (nombre de un formulario)

import tkinter

raiz = tkinter.Tk()
raiz.title("Programa ENTRY")

# Se crea varaible y usa el módulo tkinter con su método .Entry pasándole por parámetro la raíz
entrada = tkinter.Entry(raiz)

# Se configura la entrada de datos
# Si es un campo para password, se usará en la configuración show="*" (o el carácter que se quiera) para que no se vean los caracteres
entrada.config(justify="center",show=("*"))

# Se imprime por pantalla
entrada.pack()

raiz.mainloop()




# ------------- Text es un campo de texto más grande para escribir varias líneas (comentario) 

import tkinter

raiz = tkinter.Tk()
raiz.title("Programa TEXT")

# Se crea varaible y usa el módulo tkinter con su método .Entry pasándole por parámetro la raíz
entrada = tkinter.Text(raiz)

# Se puede configurar
# padx = padding eje X, pady = padding eje y, selectedbackground = fondo de texto seleccionado
entrada.config(width=20, height=10, font=("Verdana",15), padx=10, pady=10, fg="green", selectbackground="lightgrey")

# Se muestra mediante
entrada.pack()

raiz.mainloop()




# ------------- Button  es un botón sobre el que se puede realizar un clic

import tkinter

raiz = tkinter.Tk()
raiz.title("Programa BUTTON")

# Se crea una función que se ejecutará al pulsar el botón
def accion():
    print("Hola mundo")

# Se crea la variable y se usa el módulo tkinter + método .Button al que se le pasan 3 parámetros: componente raíz, texto a mostrar y comando a ejecutar
# El comando a ejecutar será una función, por lo que habrá que crearla ANTES que el botón
boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.config(fg="green")
boton.pack()

raiz.mainloop()



# ------------- RadioButton, es un botón para elegir una opción entre varias posibilidades

import tkinter

raiz = tkinter.Tk()
raiz.title("Programa Radio Button")

# Se crea la función seleccionar 
# opcion.get() sirve para recoger el valor de la variable opcion
def seleccionar():
    print("La opción seleccionada es {}".format(opcion.get()))

# Se crea la variable opcion (Se declara de tipo INT)
opcion = tkinter.IntVar()

# Se crea la variable, se usa el módulo tkinter con el método .Radiobutton al que se le pasa el componente raiz, el texto que va a mostrar 
# asignará el valor 1 a la variable opcion y ejecutará la función seleccionar
radiobutton1 = tkinter.Radiobutton(raiz, text="Opción 1", variable=opcion, value=1, command=seleccionar)
radiobutton1.pack()

radiobutton2 = tkinter.Radiobutton(raiz, text="Opción 2", variable=opcion, value=2, command=seleccionar)
radiobutton2.pack()

radiobutton3 = tkinter.Radiobutton(raiz, text="Opción 3", variable=opcion, value=3, command=seleccionar)
radiobutton3.pack()

raiz.mainloop()




# ------------- CheckButton, es un botón para marcar una acción de tipo activado desactivado

import tkinter

raiz = tkinter.Tk()
raiz.title("Programa CheckButton")

# Se crea la función verificar que recogerá el valor de la variable check1 y con un if imprimirá por consola si el check está activado o desactivado
def verificar():
    valor = check1.get()
    if (valor == 1):
        print("El check está activado")
    else:
        print("El check está desactivado")

# Se crea la variable de tipo INT
check1 = tkinter.IntVar()

# Se usa el módulo tkinter con el método Checkbutton al que se le pasa por parámetro el componente raíz, el texto que tendrá el check, la variable a la que irá asociada
# el valor que tendrá cuando esté en on y off y la función que ejecutará cuando se marque
boton1 = tkinter.Checkbutton(raiz, text="Opción 1", variable=check1, onvalue=1, offvalue=0, command=verificar)
boton1.pack()

raiz.mainloop()




# ------------- messagebox es un componente para crear ventanas emergentes, pop up


import tkinter

# Hay que importar específicamente el método messagebox del módulo tkinter
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Programa messagebox POPUP")

# Se crea la función que invoca el método messagebox.showinfo a los que se le pasará por parámetro el título del pop up y su mensaje.
def avisar():
    tkinter.messagebox.showinfo("Título ventana", "Mensaje con la información")

# Se crea un botón para que cuando se pulse, se abra el popup
boton = tkinter.Button(raiz, text="Pulsar para aviso", command=avisar)
boton.pack()

raiz.mainloop()




# ------------- messagebox para realizar preguntas

import tkinter

#Se importa messagebox
from tkinter import messagebox

raiz = tkinter.Tk()
raiz.title("Programa messagebox preguntas")

# Se crea la función que crea el messagebox para preguntar
# La respuesta del askquestion se guarda en la variable resultado que se mete en un if para que
# si la respuesta es sí o no, saque por consola un texto
def preguntar():
    resultado = tkinter.messagebox.askquestion("Título de pregunta", "Pregunta: ¿Quieres borrar el fichero?")
    if (resultado == "yes"):
        print("Sí quiero borrar el fichero")
    else:
        print("No quiero borrar el fichero")   

# Se crea un botón para que cuando se pulse, se abra el popup
boton = tkinter.Button(raiz, text="Pulsar para preguntar", command=preguntar)
boton.pack()


raiz.mainloop()





# ------------- FILEDIALOG para abrir un fichero

import tkinter

# Se importa específicamente filedialog
from tkinter import filedialog

raiz = tkinter.Tk()
raiz.title("Programa FILEDIALOG")

# Se crea la función que guardará en una variable la ruta del fichero que se haya escogido mediante filedialog.askopenfilename 
# y luego imprimirá por consola la ruta
def abrirfichero():
    rutafichero = filedialog.askopenfilename(title="Abrir un fichero")
    print(rutafichero)

# Se crea un botón para abrir el filedialog
boton = tkinter.Button(raiz, text="Pulsar para abrir", command=abrirfichero)
boton.pack()


raiz.mainloop()
