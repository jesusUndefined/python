# Crear clase "Coche" que tenga estos atributos:
# marca, color, combustible y cilindrada.

# Crear la función __init__ que asigna los parámetros de la clase a los atributos

# Crear otra función mostrar_características que mediante print muestre por pantalla
# los atributos que tiene el coche

# Crear objeto "Coche1" de la clase coche con los atributos opel, rojo, gasolina, 1.6



class Coche:
    def __init__ (self,marca,color,combustible,cilindrada):
        self.marca = marca
        self.color = color
        self.combustible = combustible
        self.cilindrada = cilindrada

    def mostrar_caracteristicas(self):
        print("La marca del coche es {}".format(self.marca)) 
        print("El color del coche es {}".format(self.color)) 
        print("El combustible del coche es {}".format(self.combustible)) 
        print("La cilindrada del coche es {}".format(self.cilindrada)) 

coche1 = Coche("Opel","rojo","gasolina",1.6)

coche1.mostrar_caracteristicas()

# Crear función lambda que calcule la media de 3 notas
nota_media = lambda nota1, nota2, nota3 : (nota1 + nota2 + nota3) / 3
print(nota_media(10,8,5))

