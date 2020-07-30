from farenheit_celsius import conversionFC
from celsius_farenheit import conversionCF


def principal():
    print("")
    print("Conversor de grados.")
    print("Introduce la letra F para convertir los grados Farenheit a Celsius.")
    print("Introduce la letra C para convertir los grados Celsius a Farenheit.")

    detector = input(str())

    if (detector == "f") or (detector == "F"):
        conversionFC()
    elif (detector == "c") or (detector == "C"):
        conversionCF()
    else:
        print("Esa no es una letra válida.")
        principal()