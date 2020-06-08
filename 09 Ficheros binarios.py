
# FICHEROS BINARIOS

# Grabar ficheros binarios

import pickle
lista_colores = ["azul", "verde","rojo","amarillo"] #Se quiere grabar esta lista en un archivo binario

fichero = open("fichero_colores.pckl","wb") # Abrir fichero con extensión .pckl (pickle) "w de write y b de binario"
pickle.dump(lista_colores,fichero) # Módulo pickle con método dump, graba la lista_colores en variable fichero con formato binario
fichero.close()

# Leer ficheros binarios

import pickle
fichero = open("fichero_colores.pckl","rb") # Nombre con el que se haya guardado el fichero binario
lista_leida_fichero = pickle.load(fichero) # Carga los datos que hay en el fichero binario y lo devuelve legible.
print(lista_leida_fichero) # Imprimir por pantalla la lista de los colores