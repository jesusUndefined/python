# ------------- FUNCIONES AVANZADAS
# ------------- FUNCIONES GENERADORAS

# Genera valores sobre la marcha, como por ejemplo range()
# Esta función generará números del 0 al 11 menos 1, es decir, 10.

range(0, 11)
for num in range(0, 11):
    print(num)


# También puede usarse de la siguiente manera range(11).
# Así saldría el mismo resultado, del 0 al 10.

# Ahora generaremos una función generadora propia de pares.
# La función para generar números pares en la que se puede configurar el número máximo.

def pares(maximo):
    for num in range(maximo):
        if (num % 2 == 0):
            yield num


# Yield actuará igual que Return.

maximo = 11
for num in pares(maximo):
    print(num)


# El resultado será 0,2,4,6,8,10


# ------------- FUNCIÓN FILTER
# Se usa para filtrar resultados a partir de una lista y una función condicional.
# El resultado será otra lista con resultados que cumplen esa condición.

# Primero se creará una función condicional.
# Se crea una función que devuelve true si el número es positivo y false en caso contrario.

def positivo(nume):
    if (nume > 0):
        return True
    else:
        return False


# Usando la función, dará true o false
positivo(3)

positivo(-3)

# Se genera una lista de números:
numeros = [4, -2, 8, -5, -4, 2, 88]

# Se usa el filtro:
filtro = filter(positivo, numeros)
resultado = list(filtro)
print(resultado)

# El resultado es: [4, 8, 2, 88]

# ------------- MAP
# Aplicar una función a los elementos de una lista

def multiplicar(numerito):
    return numerito * 2


multiplicar(2)

numeros = [1,5,66]

mapeo = map(multiplicar, numeros)
resultado = list(mapeo)
print(resultado)

# En una línea sería de la siguiente forma:
lista_res = list(map(multiplicar, numeros))
print(lista_res)


# Para hacerlo sin crear una función:
# Se usa una función lambda que recibe un parámetro (numero) y devuelve el numero * 2.
# El último parámetro es la lista que se va a multiplicar.

lista_resultado = list(map(lambda numero: numero * 2, numeros))
print(lista_resultado)