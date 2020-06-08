
# COLECCIONES DE DATOS

# LISTAS
# Colección de elementos ordenados que se pueden modificar

colores = ["rojo","amarillo","verde"] # Lista de 3 elementos
colores[0] # Será el color rojo
colores[1] = "azul" # Cambia el color rojo que había en la lista por el azul

len(colores) # Mide la longitud de la lista
colores.append("blanco") # Agrega el valor a la lista
colores.remove("rojo") # Borra el valor seleccionado
colores.clear # Borra todo el contenido de la lista
colores.TAB # Presionando TAB aparecen las opciones que se pueden aplicar

# Recorrer una lista con un for
for color in colores:
    print(color)


# TUPLAS
# Colección de elementos ordenadas que no se pueden modificar

tupla_colores = ("rojo","verde","amarillo")
tupla_colores[2] # Muestra el índice 2, que sería amarillo
len(tupla_colores) # Mide la longitud de la tupla

# Recorrer la tupla
for color in tupla_colores:
    print(color)


# CONJUNTOS
# Colección de elementos desordenados. Sin índice para acceder a sus elementos.

conjunto_colores = {"rojo","verde","azul"} 
conjunto_colores[0] # No permitido porque no soporta índices, siempre desordenados
len(conjunto_colores) # Mide la longitud del conjunto
conjunto_colores.add("negro") # Añadir un elemento
conjunto_colores.remove("negro") # Borra el elemento seleccionado

# Recorrer el conjunto con un bucle for
for color in conjunto_colores:
    print(color)



# DICCIONARIOS
# Conjunto de elementos desordenados que se pueden modificar. 
# Formado por clave:valor

diccionario_colores = {"red":"rojo","blue":"azul","yellow":"amarillo"}

diccionario_colores["red"] # Accede al elemento por su clave, el resultado será rojo
valor = diccionario_colores["yellow"] # Guarda en la variable valor el valor de la clave yellow, el resultado es amarillo
diccionario_colores["black":"negro"] # Añadir clave:valor al diccionario
diccionario_colores.pop("yellow") # Borrar elemento con clave yellow
del(diccionario_colores["yellow"]) # Borrar elemento con clave yellow

# Recorrer diccionario con bucle for
for color in diccionario_colores:
    print(color)

# Imprimir por pantalla clave y valor
for clave,valor in diccionario_colores.items():
    print(clave,valor)