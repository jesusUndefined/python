
# BUCLES Y CONDICIONES

# IF, ELIF, ELSE
# Elif -> más condiciones
# Else -> en caso contrario
a = 2
b = 3
c = 4
d = 8

if (a > b):
    print("A es mayor que B")

if (a < c) and (b > c):
    print("Imprime esta línea")
elif (c == d):
    print("Imprime aquí")
else:
    print("Imprime la segunda línea")


# FOR

colores = ["rojo", "verde", "azul"]

for color in colores:
    print(color) 

# El resultado será vertical
#rojo
#verde
#azul

cadena = "Hola"

for caracter in cadena:
    print(caracter)

# El resultado será vertical
#h
#o
#l
#a

# Iterar en rango de valores:

range(8) # El resultado sería range(0,8) pero el 8 no estaría incluido

for num in range(8):
    print num
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7

# Para hacerlo de dos en dos
for num in range(3,8,2): #El rango es del 3 al 7
    print(num)

# 3
# 5
# 7

# Break para el bucle

for numero in range(10):
    if(numero == 5):
        break
    print(numero)

# Imprimiría 0 1 2 3 45

# continue para sólo la iteración actual

for num in range(10):
    if (num == 6):
        continue
    print(num)

    # si el numero es 6 no continua, va al sig num
    # El resultado sería 0 1 2 3 4 5 7 8 9 

# doble FOR

for num1 in range(4):
    for num2 in range(3):
        print(num1,num2)

# El resultado sería
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2
# 3 0
# 3 1
# 3 2


# WHILE
# Se ejecuta mientras sea cierta la condición

valor = 1
fin = 10

while (valor < fin):
    print(valor)
    valor = valor + 1

# El resultado sería del 1 al 9 en vertical

valor = 1
fin = 10
while (valor < fin):
    print(valor)
    valor = valor + 1
    if (valor == 5):
        break
# Se pararía en el 5, siendo el último valor que imprime el 4: 1 2 3 4

valor = 1
fin = 10
while (valor < fin):
    print(valor)
    valor = valor + 1
    if (valor == 5):
        continue
# Se saltaría el valor 5 y empezaría en el 6 de nuevo






