
#Se crea el diccionario
frutas = {"manzana":"apple","naranja":"orange","platano":"banana","limon":"lemon"}

frutas.values() #Se comprueban todos los valores

#Se importa pickle
import pickle

#Se asocia a una variable la apertura del fichero binario que se grabará en modo binario WB
fichero = open("fichero1.pckl","wb")

#Se mete la el diccionario en el fichero binario
pickle.dump(frutas,fichero)

#Se cierra el fichero
fichero.close()

#Se crea otra variable nueva y se abre el fichero deseado en modo RB
#Si se abre así, se leería en binario todavía
fichero2 = open("fichero1.pckl","rb")

#Se traduce del binario y se muestra en otra variable que ya se podría imprimir por pantalla de manera legible
datos = pickle.load("fichero2")

print(datos)