
# MÓDULOS 

# Es un fichero que contiene un conjunto de funciones que se puede incluir y usar en una aplicación
# Se crean distintos ficheros y luego se llaman desde uno

# Fichero 1: módulo1.py
# Contiene una función que toma por parámetros la variable nombre e imprime la frase
def saludar(nombre):
    print("Hola, soy " + nombre)

# Fichero 2: programa1.py
# El programa llamará al módulo del fichero 1
# Se importa el módulo1 y ya se podría usar la función saluda()

import modulo1
modulo1.saludar("Ezú") # El resultado sería: "Hola, soy Ezú"

# También se puede usar metiendo el nombre en la variable

import modulo1
nombre = "Ezú"
modulo1.saludar(nombre)

# Se puede importar sólo una parte del fichero del módulo
# Se importará sólo la función saludar() del fichero módulo1.py
from modulo1 import saludar

# Se puede importar sólo una parte del fichero y renombrar la función que se importa
# Se importará sólo la función saludar() del fichero módulo1.py pero se renombra a saludito()
# Se tendrá que usar saludito() en vez de saludar()
from modulo1 import saludar as saludito


# INSTALAR UN MÓDULO NUEVO CON PIP

# PIP es un gestor de paquetes y módulos para Python. 
# Un módulo es una librería de código python que se puede incluir en el proyecto

# Para usar un módulo que no está instalado hay que instalarlo con PIP
# Para instalarlo, hay que trabajar en la consola
# Con pip --version verifica si está instalado pip y qué versión tiene en caso de estar instalado
# Con pip list se ven los paquetes/módulos que están instalados
# Con pip install nombremódulo se instala el paquete/módulo que se pide
# Ejemplo: pip install camelcase
# Una vez instalado ya se puede usar

# Se importa el módulo
import camelcase

# Se crea un objeto camel que usará la clase CamelCase() del módulo camelcase
camel = camelcase.CamelCase() 

# Se crea una variable tipo texto
texto = "mi nombre es ezú"

# Imprimirá por pantalla el contenido de la variable texto con mayúscula en cada una de las palabras 
# usando el método .hump() de la clase camelcase que está dentro del objeto camel.
print(camel.hump(texto)) # El resultado será " Mi Nombre Es Ezú "

# Con pip uninstall camelcase se desinstala el paquete