def conversionCF():
    print("")
    print("==== Conversión Celsius - Farenheit ====")
    print("")
    grados = int(input("Introduce grados Celsius: "))
    totalFarenheit = int(grados*(9/5) + 32)
    print("Has introducido: " + str(grados) + " grados Celsius. ")
    print(str(grados) + " grados Celsius son " + str(totalFarenheit) + " grados Farenheit.")