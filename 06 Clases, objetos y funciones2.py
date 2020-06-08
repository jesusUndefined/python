
# CLASES, OBJETOS Y FUNCIONES. Programación orientada a objetos.

# CLASES:

# Se llama constructor, en este caso, estás inicializando los atributos de la
# clase dentro del método constructor,
class ClaseSilla: #Creador de la clase
    color = "blanco"
    precio = 100

objetoSilla1 = Clasesilla() #Creación del objeto
# El objetoSilla1, tal como lo has declarado arriba en su clase, será blanco y tendrá un precio de 100

# uso del objeto
# Para consultar los atributos, lo harás así
objetoSilla1.color
objetoSilla1.precio

# De nuevo, objetoSilla2 se te crea con las propiedades del color blanco y precio 100
objetoSilla2 = ClaseSilla()
# Pero puedes modificarlo así
objetoSilla2.color = "verde"
objetoSilla2.precio = 399

# Si quieres poder crear objetos de forma dinánima, no los inicializas dentro
# de la clase sino que creas un MÉTODO CONSTRUCTOR con parámetros.
# No son incompatibles ambas formas, puedes tener atributos con valores por defecto
# y puedes tener dos constructores, uno sin parámetros y otro con parámetros
class Persona:
    # Self es el propio objeto, por lo que se ve en el ejemplo de abajo, se pasa de serie
    def __init__(self,nombre,edad): #método constructor
        self.nombre = nombre
        self.edad = edad

    # Según el ejemplo de abajo, self se pasa solo y es lo que usas dentro la
    # función para asignar los parámetros "self.nombre"
    def saludar(self):              #método
        print("Hola me llamo {} y tengo {} años".format(self.nombre,self.edad))

persona1 = Persona("Juan",37) #Se crea el objeto persona, con los atributos pasados por parámetro

persona1.edad # El resultado sería 37
persona1.nombre # El resultado sería Juan
persona1.saludar() # El resultado seria: Hola me llamo Juan y tengo 37 años.
