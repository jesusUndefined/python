# ------------- EJERCICIO
# Crear función generadora de números primos entre 0 y 100
# Lista de números primos entre 0 y 100:
numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Usar función generadora para mostrar por pantalla números primos menores de 50.

def primos(maximo):

    for num in range(maximo):
        if (num in numeros_primos):
            yield num
        if (num > 100):
            break


maximo = 100
for num in primos(maximo):
    print(num)
