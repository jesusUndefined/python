
# Crear función BUSCAR que me diante expresión regular indique si una palabra está en una frase

# Probar la función con la frase:
    # texto = "Esto es una frase de pruebas para hacer búsquedas"
    # palabra_a_buscar = 'frase'
# En caso de encontrarla palabra en la frase, indicar en qué posición empieza y en cuál acaba

import re

texto = "Esto es una frase de pruebas para hacer búsquedas"
palabra = "frase"

def buscar(palabra,texto):
    resultado = re.search(palabra, texto) # Se vuelca en una variable el resultado del re.search
    return resultado

resultado_ext = buscar(palabra, texto) # Se invoca a la función pasándole 2 parámetros (variables, pero pueden ser texto)

if(resultado_ext): # Si hay resultado, entonces:
    print("Palabra {} encontrada".format(palabra))
    inicial = resultado_ext.start() # Variable que almacena la posición donde empieza el resultado de resultado_ext
    final = resultado_ext.end() # Variable que almacena la posición donde acaba el resultado de resultado_ext
    print("Empieza en la posición {} y termina en la posición {}".format(inicial,final))
else: # Si no hay resultado, entonces:
    print("Palabra {} NO encontrada".format(palabra))

