
# CLASES, OBJETOS Y FUNCIONES. Programación orientada a objetos (POO).

# CLASES:
# Creador de la clase, llamado CONSTRUCTOR
# Se inicializan los atributos de la clase creada dentro
class ClaseSilla: 
    color = "blanco"
    precio = 100

# Creación del objeto
# Tal y como se ha declarado, será blanco y tendrá un precio de 100
objetoSilla1 = Clasesilla() 

# Uso del objeto
# Así se sabrían sus atributos
objetoSilla1.color
objetoSilla1.precio

# Se crea y se inicializa, que por defecto sería blanco y de precio 100
objetoSilla2 = ClaseSilla()
# Se modificaría de esta forma y pasaría a ser verde con precio 399
objetoSilla2.color = "verde"
objetoSilla2.precio = 399

# __init__ -> automáticamente al crear nuevo objeto, se ejecuta el método (constructor)
# self -> no es palabra reservada, pero se usa habitualmente
#
# class Ejemplo:
#   def _init(self):
#       self.otro = otro

class Persona:
    def __init__(self,nombre,edad): # método constructor
        self.nombre = nombre        # atributo
        self.edad = edad            # atributo

    def saludar(self):              #método
        print("Hola me llamo {} y tengo {} años".format(self.nombre,self.edad))

# Se crea el objeto persona y se le pasan los dos parámetros: nombre y edad
persona1 = Persona("Juan",37) 

# Para consultar los atributos del objeto:-
persona1.edad       # El resultado sería 37
persona1.nombre     # El resultado sería Juan

# Para consultar el método saludar()
persona1.saludar()  # El resultado seria: Hola me llamo Juan y tengo 37 años.



# FUNCIONES
#
# Bloque de código que se ejecuta cuando es llamado

# Se consrtuye de la siguiente forma:
def saludar():
    print("Hola, buenos días")

# Se llama de la siguiente forma:
saludar()

# Con paso de parámetros:
def saludar(nombre):
    print("Hola, buenos días" + nombre)

#Se mete en una variable el nombre
nombre = "Antonio"

# Para invocarla:
saludar(nombre) # El resultado sería "Hola, buenos días Antonio"


# Paso de valor por referencia

# Se crea lista de valores
colores = ["rojo","verde","azul"] 

# Se crea una función que le va a pasar a la lista "colores" el valor que haya en la variable "color"
# A través de la opción .append()
def incluir_color(colores, color):
    colores.append(color)

# Se inicializa la variable con el color deseado y se ejecuta la función 
# pasándole por parámetro la lista y la variable
color = "negro"
incluir_color(colores,color)

# La lista de valores estará ahora así:
# colores = ["rojo","verde","azul","negro"]  


# FUNCIONES LAMBDA
#
# Las función lambda recibirá un parámetro (numero) y el resultado será numero + 30
# Se le pasa a la variable resultado por parámetro ese número y en el resultado aparecerá la suma
resultado = lambda numero : numero + 30
resultado(10) # El resultado sería 40
