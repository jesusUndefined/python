
# OPERADORES
#
# OPERADORES ARITMÉTICOS
#
# Suma +
# Resta -
# Multiplicación *
# División /
# Resto % (resto de una división)
numero1 = 5
numero2 = 2
resto = numero1 % numero2
print(resto) # El resultado sería 1

# Cociente // (valor entero de la división)
numero1 = 5
numero2 = 2
cociente = numero1 // numero2
print(cociente) # El resultado sería 2

# Exponente **
exponente = 2 ** 3 # El resultado de 2 al cubo sería 8

# OPERADORES DE ASIGNACIÓN

numero = 5

numero = numero + 4 # El resultado sería 9
numero += 4 #también se puede poner así

numero = numero - 4 # El resultado sería 1
numero -= 4 #también se puede poner así

numero = numero * 2 # El resultado sería 10
numero *= 2 #también se puede poner así

numero = numero / 5 # El resultado sería 1
numero /= 5 #también se puede poner así

numero = numero ** 2 # El resultado sería 25
numero **= 2 #también se puede poner así


# OPARADORES DE COMPARACIÓN
#
# Si coinciden devolverán valor true y si no false
#
# igual ==
# distinto !=
# mayor que >
# menor que <
# mayor o igual >=
# menor o igual <=


# OPERADORES LÓGICOS

# AND -> Para que ambos sean verdaderos

numero1 = 10
numero2 = 5
numero3 = 7
numero4 = 8

# Para comparar hay que meterlo en paréntesis

(numero1 > numero2) and (numero4 > numero3) # El resultado será TRUE porque ambas son TRUE

# OR -> Para que uno de los dos sean verdaderos

(numero1 > numero2) or (numero2 > numero4) # El resultado será TRUE porque una de las dos es TRUE

# NOT -> Será TRUE cuando la operación de su interior sea FALSE

not(numero3 > numero4) #El resultado será TRUE porque su interior es FALSE


# OPERADORES DE IDENTIDAD 
# Intenta identificar si dos objetos son iguales o distintos

# IS
frutas1 = ["manzana","pera"]
frutas2 = ["manzana","pera"]
frutas3 = frutas1

frutas3 is frutas1 # El resultado será TRUE

frutas3.append("naranja") #añade un elemento a la lista

# IS NOT
frutas3 is not frutas1 # El resultado será FALSE


# OPERADORES DE PERTENENCIA
# Verifica si un valor está dentro de una lista de valores 

 # IN
frutas1 = ["manzana","pera","naranja"] #lista de valores
frutas2 = "pera" #variable, cadena de texto

frutas2 in frutas1 # El resultado será TRUE porque está incluido

# NOT IN
frutas2 not in frutas1 # El resultado será false porque sí está dentro. Para que fue TRUE no tendría que estar dentro de la lista