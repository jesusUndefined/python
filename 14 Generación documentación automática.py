
# ------------- GENERACIÓN DE DOCUMENTACIÓN AUTOMÁTICA
# ------------- DOCSTRINGS

# Son cadenas para generar documentación automáticamente en programas python

def saludar(nombre):
    """
    Comentario de la función saludar.
    Recibe como parámetro una cadena con un nombre.
    Imprimirá por pantalla un saludo con el nombre concatenado.
    """
    print("Buenos días " + nombre)

# Invocamos la función saludar()
saludar("Antonio")

# El resultado será: Buenos días Antonio

# Para usar la generación de documentación automática:
# Se usará help(función), tal que así: help(saludar)
# El resultado será el comentario que se ha puesto en la función entre triple comilla.

help(saludar)

class Saludos:
    """
    Esta clase tendrá dos funciones: buenos_días y adios.
    Ambas recibirán un nombre como parámetro
    """
    def buenos_dias(self,nombre):
        """
        Comentario función buenos días
        """
        print("Buenos días {}".format(nombre))

    def adios(self,nombre):
        """
        Comentario función adiós
        """
        print("Adiós {}".format(nombre))


# ------------- PYDOCS
# Genera documentación automática desde la consola

# Se abre la consola
# Se cambia a la ruta donde esté el archivo python
# ejecutamos lo siguiente:

pydoc /rutaDelArchivoPython.

# Se abrirá la documentación que se ha generado mediante la consola, mostrando lo mismo
# que muestran en docstrings pero por consola.


# Para generar un documento HTML de documentación se hará lo siguiente:

pydoc -w /rutaDelArchivoPython.py

# Esto creará en el directorio un archivo HTML de la documentación.