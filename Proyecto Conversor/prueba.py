# Recogida por consola de grados a convertir
grados = float(input("Introduzca grados Celsius a convertir en Farenheit: "))

#Función de conversión Celsius - Farenheit
def conversionCF(grados):
    farenheit = float((9/5)) * float(grados) + 32
    print("Conversión: " + str(grados) + " grados Celsius son " + str(farenheit) + " grados Farenheit.")
    
conversionCF(grados)


# Recogida por consola de grados a convertir
grados = float(input("Introduzca grados Farenheit a convertir en Celsius: "))

#Función de conversión Farenheit - Celsius
def conversionFC(grados):
    celsius = float(grados - 32) * float((5/9))
    print("Conversión: " + str(grados) + " grados Farenheit son " + str(celsius) + " grados Celsius.")

conversionFC(grados)
