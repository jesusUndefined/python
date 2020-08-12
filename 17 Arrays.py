# ------------- ARRAYS
# Se importa el módulo numpy que es el que se usa para hacer arrays.

import numpy as np

# Se puede crear un array de elementos vacíos con la función .zeros()
np.zeros(4)
# El output sería:
# array([0.,0.,0.,0.])

# También puede hacerse de unos.
np.ones(4)
# El output sería:
# array([1.,1.,1.,1.])

# Se puede hacer un array de elementos.
np.arange(5)
# Crea un array de 5 elementos, del 0 al 4
# El output sería:
# array([0, 1, 2, 3, 4])

# También se puede crear un array con principio y final
np.arange(2,20,3)
# En este caso, empieza en el 2, termina en el 20 y salta de 3 en 3.
# El output sería:
# array([2, 5, 8, 11, 14, 17])


# Se puede usar un array a partir de una lista
lista = [1,2,3,4]
array1 = np.array(lista1)

# El output de array1 sería:
# array([1, 2, 3, 4])

# También se puede usar un array de 2 dimensiones
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

lista_doble = (lista1,lista2)

arraydoble = np.array(lista_doble)

# El output sería:
# array([[1,2,3,4],[5,6,7,8]])

# Con  arraydoble.shape se muestra las filas y las columnas que tiene el array.
# El output sería:
# (2, 4)
# 2 filas, 4 columnas

# Para ver el tipo de dato que tiene el array:
arraydoble.dtype

# El output sería:
# dtype('int64')