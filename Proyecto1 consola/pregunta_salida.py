from funcion_principal import principal


def preguntasalida():
    print("")
    print("¿Quieres hacer otra conversión?")
    print("Introduce la letra S para hacer otra conversión.")
    print("Introduce la letra N para salir.")

    again = input(str())

    if (again == "s") or (again == "S"):
        principal()
    elif (again == "n") or (again == "N"):
        print("Cerrando aplicación. Gracias por usar el conversor.")
        exit()
    else:
        print("Esa no es una letra válida.")
        preguntasalida()

