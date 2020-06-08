
# Se crea un archivo llamado moduloficheros.py
# Se crea la clase Fichero 
# Se le pasará por parámetro el nombre del archivo de texto
class Fichero:
    def __init__(self,nombre):
        self.nombre = nombre

# Se crea el método para grabar el texto en el fichero
# Se le pasará por parámetro una variable con el texto dentro
    def grabar_fichero(self,texto):
        fichero = open(self.nombre,"wt")
        fichero.write(texto)
        fichero.close()

# Se crea el método para incluir el texto en el fichero
# Se le pasará por parámetro una variable con el texto dentro
    def incluir_fichero(self,texto):
        fichero = open(self,nombre,"at")
        fichero.write(texto)
        fichero.close()

# Se crea el método para leer el fichero de texto
# No se le pasará nada por parámetros
# NOTA: La variable texto no tiene nada que ver con la que escribe texto en el fichero, simplemente coincide en el nombre
    def leer_fichero(self):
        fichero = open(self,nombre,"rt")
        texto = fichero.read()
        return texto


# Se crea un archivo llamado programa.py
# Se importa el módulo que contiene los métodos de grabar, incluir y leer ficheros, hechos anteriormente
import moduloficheros 

# Se crea un objeto que accede al módulo "moduloficheros", usa la clase Fichero y se le pasa por parámetro el nombre del fichero a usar
fichero = moduloficheros.Fichero(nombre_fichero) 

# Variable con el texto que se quiere grabar
texto = "Primera fila.\nSegunda fila."

# Objeto fichero usando el método grabar y pasándole por parámetro la variable que contiene la cadena que se quiere grabar en el fichero
fichero.grabar_fichero(texto)

texto = "\nTercera fila."

# Objeto fichero usando el método incluir y pasándole por parámetro la variable que contiene la cadena que se quiere incluir en el fichero
fichero.incluir_fichero(texto)

# Objeto texto_leido usando el método leer fichero e imprimiendo por pantalla el objeto
texto_leido = fichero.leer_fichero()
print(texto_leido)