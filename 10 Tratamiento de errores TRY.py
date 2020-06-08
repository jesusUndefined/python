
# TRATAMIENTO DE ERRORES

# TRY EXCEPT ELSE FINALLY

# TRY Permite verificar si un bloque de código tiene errores

numero1 = 5
numero2 = 0
division = numero1 / numero2

# Dará fallo ZeroDivisionError

try: #Prueba esto
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
except: #si hay un error, ejecuta esta línea
    print(Ha habido un error)

# Para el error ZeroDivisionError

try: #Prueba esto
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
except ZeroDivisionError: #Si hay error ZeroDivisionError, imprime esto:
    print("Error, división entre cero")
except: #si hay otro error, ejecuta esta línea
    print("Ha habido un error")
else: #en caso que no haya error
    print("La división funcionó correctamente")


# FINALLY
# Se ejecutará siempre

try: #Prueba esto
    numero1 = 5
    numero2 = 0
    division = numero1 / numero2
except ZeroDivisionError: #Si hay error ZeroDivisionError, imprime esto:
    print("Error, división entre cero")
except: #si hay otro error, ejecuta esta línea
    print("Ha habido un error")
else: #en caso que no haya error
    print("La división funcionó correctamente")
finally: #Se ejecutará SIEMPRE
    print("Esta prueba del try se ha acabado")