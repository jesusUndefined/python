def conversionFC():
    print("")
    print("==== Conversión Farenheit - Celsius ====")
    print("")
    grados = int(input("Introduce grados Farenheit: "))
    totalCelsius = int((grados-32)*(5/9))
    print("Has introducido: " + str(grados) + " grados Farenheit. ")
    print(str(grados) + " grados Farenheit son " + str(totalCelsius) + " grados Celsius.")