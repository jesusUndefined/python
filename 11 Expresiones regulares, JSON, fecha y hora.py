
# EXPRESIONES REGULARES
 
# search, findall, split, sub

# Es una secuencia de caracteres que sirve para una búsqueda por patrón

texto = "Hola, mi nombre es Antonio"

import re # carga el módulo de regular expresions 
re.search("nombre",texto) # buscará el patrón "nombre" dentro de la variable texto
# Si lo encuentra, devuelve un objeto de tipo match, si no, no devuelve nada

resultado = re.search("nombre",texto)
if (resultado):
    print("Cadena encontrada")
else:
    print("cadena no encontrada")


resultado = re.search("Antonio$",texto) # Añadir el símbolo $ es para buscar si alguna cadena acaba en la palabra Antonio
resultado = re.search("^Hola",texto) # Añadir el símbolo ^ es para buscar si alguna cadena empieza por la palabra Hola
resultado = re.search("mi.*es",texto)   # Añadir el símbolo . entre las dos palabras que pueden tener caracteres en medio ("mi" y "es")
                                        # y * para decir que es puede aparece 0 o más veces caracteres en el medio


# FINDALL
# Busca todas las ocurrencias en una cadena

# Triple comilla doble para escribir el texto en varias líneas y que no dé error
texto = """
El coche de Luis es rojo,
el coche de Antonio es blanco
y el coche de María es rojo 
"""

re.findall("coche.*rojo",texto) # Devuelve 2 elementos en una lista


# SPLIT
# 
# Divide una cadena a partir de un patrón

texto = "La silla es blanca y  vale 80" 

re.split("\s")  # \s significa espacio en blanco, por lo que dividirá las palabras usando el espacio en blanco como patrón
                # El resultado será una lista con las palabras divididas por espacios 

# SUB

# Sustituye todas las ocurrencias en una cadena

texto = "La silla es blanca y vale 80"

re.sub("blanca","roja",texto) # Sustituye el argumento 1 por el argumento 2 en el lugar indicado como argumento 3. Sustituirá los "blanca" por "roja" en el objeto "texto"
# El resultado será "La silla es roja y vale 80"


# JSON

# Forma de almacenar e intercambiar datos en texto
# Convertir datos de un diccionario en Python a JSON

producto = {"nombre":"silla","color":"blanco","precio":80}

# Importar módulo JSON

import JSON

# El módulo json tiene un método .dumps()
# Se le pasa por parámetro la estructura en python (el diccionario creado) y devuelve una estructura json
estructura_json1 = json.dumps(producto)

# Daría como resultado {"nombre":"silla","color":"blanco","precio":80} en formato JSON, texto. No se puede acceder a los elementos
# estructura_json[0] accedería al caracter número 0 
print(estructura_json1) 

# Convertir JSON a Python (diccionario)

import json
producto2 = json.loads(estructura_json1) # Se carga en la variable el elemento JSON que ya puede volverse a acceder como diccionario



# FECHA Y HORA

# Se importa del módulo, la clase datetime solamente
from datetime import datetime

fechayhora = datetime.now()
print("fechayhora") # Mostrará fecha y hora actual

# Para acceder a cada uno de los elementos por separado:

año = fechayhora.year
mes = fechayhora.month
día = fechayhora.day
hora = fechayhora.hour
minutos = fechayhora.minute
segundos = fechayhora.second
microsegundos = fechayhora.microsecond

# Imprimirá "La hora es 22:22:22"
print("La hora es {}:{}:{}".format(hora,minutos,segundos))