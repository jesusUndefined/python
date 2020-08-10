# ------------- PRUEBAS AUTOMÁTICAS

# ------------- DOCTEST
# Genera pruebas dentro de la propia documentación
# Se crea la documentación automática en una función (por ejemplo).
# A continuación se hace un ejemplo de lo que hace la función y el resultado de la siguente manera:
# >>> sumar(4,3)
# 7

# Para que ejecute esa prueba, hay que escribir al final del documento lo siguiente:
# import doctest
# doctest.testmod()


def sumar(num1, num2):
    """
    Documentación de función sumar:
    Recibe 2 números como parámetros y devuelve su suma.
    >>> sumar(4,3)
    7
    """
    return num1 + num2


resultado = sumar(2, 4)
print(resultado)

import doctest

doctest.testmod()


# Se ejecutará por terminal añadiendo -v después del nombre del archivo.
# Ejemplo: archivo.py -v

# El resultado será:
# (venv) C:\Users\win10\Desktop\python\.01 Curso Python>"15 Pruebas automáticas.py" -v
# 6
# Trying:
#    sumar(4,3)
# Expecting:
#    7
# ok
# 1 items had no tests:
#    __main__
# 1 items passed all tests:
#   1 tests in __main__.sumar
# 1 tests in 2 items.
# 1 passed and 0 failed.
# Test passed.


# ------------- UNITTEST
# Sirve para crear pruebas dentro del propio código

# Se crea una función de ejemplo que multiplique dos números.
# Para implementar pruebas dentro del mismo código hay que importar unittest y crear una clase de pruebas.

def multiplicar(num1, num2):
    return num1 * num2


resultado = multiplicar(2, 4)
print(resultado)

import unittest

class Pruebas(unittest.TestCase):
    def test(self):
        self.assertEqual(multiplicar(2, 4), 8)

if __name__ == '__main__':
    unittest.main()

# Se ejecuta el archivo .py después por consola y saldrá el resultado.
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
#
# OK
