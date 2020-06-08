#
# CADENAS DE CARACTERES
#
# Acceder a posiciones de cadenas:
# Empezando por la izquierda
#   H O L A   M U N D O
#   0 1 2 3 4 5 6 7 8 9

cadena = "HOLA MUNDO"
cadena[3] #sería la letra A

cadena[0:3] #Extrae de la H a la A

cadena[-1] #Sería la letra O, empezando por el final


# Contar caracteres: función len() -> len(nombredelacadena)
cadena = "Hola mundo"
len(cadena) #El resultado será 10

# Poner en mayúscula la cadena
cadena.upper() #El resultado será "HOLA MUNDO"

# Poner en minúsculas la cadena
cadena.lower() #el resultado será "hola mundo"

# Ver todas las funciones
cadena.TAB #PULSAR TABULADOR

# Dividir cadenas por palabras
cadena.split() #El resultado sería "hola", "mundo"

cadena2 = "uva,pera,manzana,naranja"

cadena2.split(',') #Usa la coma como divisor
#El resultado será: uva, pera, manzana, naranja.


# IMPRIMIR VARIABLES EN CADENAS

nombre = "Antonio"
print("Buenos días " + nombre) #Resultado: Buenos días Antonio.


# .format

nombre = "Antonio"
edad = 18
print("Buenos días {}, feliz {} cumpleaños".format(nombre,edad))
# Se sustituyen las llaves por los parámetros pasados en el .format

resultado = 10/3
3.333333333
#Acortarlo
print("El resultado es {r}".format(r=resultado))
print("El resultado es {r:1.3f}".format(r=resultado)) #coge 1 entero y 3 decimales


# f-strings
nombre = "Antonio"
edad = 18

print(f"Buenos días {nombre}, feliz {edad} cumpleaños")


# ENTRADA POR TECLADO
#
# Función input()
# Se meten valores a través del teclado

print("Introduce un nombre")
entrada = input() #Lo que entre por teclado se guarda en la variable
print("Hola" + entrada)


