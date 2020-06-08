print("Hola mundo!")

# VARIABLES
#
# Python es case sensitive en variables.
# Python permite empezar variables por letras o guión bajo.

variable1 = 1
Variable2 = 2
VariableCadena = "olakease?"
_VariableCadena = "aprende Python o ke ase?"

#Python no permite comenzar variables por números
2VariableCadena = "No permitida"

# Para identificar el tipo de la variable está la función " type() "
type(variable1)

type(nombredevariable)

# Para concatenar variables string se usa " + "
texto = VariableCadena + _VariableCadena

# Para sumar variables de tipo numéricas se usa " + " también
total = variable1 + Variable2


# Variables decimales
# Al sumar entero y decimal, saldrá tipo float
numeroDecimal = 3.7
type(numeroDecimal) #resultando: float

# Convertir tipos de variables

numero = 5
cadena = str(numero) #La variable después de esto es string

# Los strings que son decimales hay que convertirlos a float 
cadena = '3.2'
numerodecimal = float(cadena)