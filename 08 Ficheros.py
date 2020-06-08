
# FICHEROS
# Es una secuencia de bits que se almacenan con algún nombre en el disco duro


# LEER FICHEROS

# Teniendo el fichero "ficheroEjemplo.txt" con el siguiente texto:
    línea 1
    línea 2  
# Se usará el método open() al que se le pasará por parámetro el fichero y el modo de lectura
# "r" de "read" y "t" de "text" en este caso 
fichero = open("ficheroEjemplo.txt","rt")

# Se usará el método read() para leerlo
datos_fichero = fichero.read()

# Se sacará por pantalla
print(datos_fichero)

# El resultado será:
# línea 1
# línea 2


# GRABAR FICHEROS

# Creación de un fichero de texto que no existe desde python
# Se usará el método open, pasándole por parámetro el nombre del archivo y el modo de escritura
# que será "w" de "write" y "t" de "text"
fichero = open("fichero_para_grabar.txt","wt")

texto_fichero = "La línea de texto que se va a grabar"

# Se usará el método write() para escribirlo y se le pasa por parámetro la variable que contiene el texto que queremos grabar
fichero.write(texto_fichero)

# Se cierra el fichero con close()
fichero.close()


# INCLUIR DATOS EN UN FICHERO DE TEXTO EXISTENTE

# Se usará el método open() pasándole por parámetro el nombre del archivo al que se le van a meter datos
# y el modo de añadir texto "a" de "append" y "t" de "text"
fichero = open("fichero_para_grabar.txt","at")

# Con \n se usa el retorno de carro para bajar una línea en la escritura
texto_fichero = "\nOtra línea más"

# Se usará el método write() para escribirlo y se le pasa por parámetro la variable que contiene el texto que queremos grabar
fichero.write(texto_fichero)
fichero.close()


# BORRAR UN FICHERO DE TEXTO

# Se importa el módulo "os" y se usa el método remove
import os
os.remove("fichero_para_grabar.txt")
