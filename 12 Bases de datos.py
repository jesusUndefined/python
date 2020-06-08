
# BASES DE DATOS

# ------------- CREAR BASES DE DATOS
# SQLite

# Importar módulo 
import sqlite3 

# Usar método connect para crear bbdd nueva o conectarse a una existente y devuelve el enlace a la bbdd en la variable conexion
conexion = sqlite3.connect("db1.db")

# Cerrar la conexión
conexion.close()

# ------------- CREAR UNA TABLA 

import sqlite3

conexion = sqlite3.connect("db1.db")

cursor = conexion.cursor() # El método CURSOR se usa para ejecutar sentencias SQL dentro de la BBDD

# Se usa el método execute para ejecutar la sentencia
cursor.execute("CREATE TABLE PERSONAS (nombre TEXT, apellido1 TEXT, apellido2 TEXT, edad INTEGER)")

# Hacer commit de la sentencia

conexion.commit()

conexion.close()



# ------------- INSERTAR UNA FILA

import sqlite3

conexion = sqlite3.connect("db1.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS values ('Antonio','Perez','Gomez',35)") # Todo lo que vaya dentro de comillas dobles irá en comillas simples en la sentencia SQL

conexion.commit()
conexion.close()



# ------------- INSERTAR VARIAS FILAS

import sqlite3

conexion = sqlite3.connect("db1.db")

cursor = conexion.cursor()

lista_personas = [ ('Pablo','Clavó','Unclavito',33), ('Ramón','Rodríguez','Verdejo',51), ] 
cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", lista_personas)

conexion.commit()
conexion.close()



# ------------- CONSULTAR DATOS

import sqlite3
conexion = sqlite3.connect("db1.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS")
personas = cursor.fetchall() # fetchall recoge los resultados del SELECT y los vuelca en la variable personas
for persona in personas: # Recorrer la lista
    print(persona)

conexion.close()



# ------------- CONSULTAR DATOS CON WHERE (CONDICIÓN)

import sqlite3
conexion = sqlite3.connect("db1.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS WHERE edad < 50")
personas = cursor.fetchall()
for persona in personas:
    print(persona)
conexion.close()



# ------------- CONSULTAR DATOS Y ORDENARLOS

import sqlite3
conexion = sqlite3.connect("db1.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS ORDER BY edad desc")
personas = cursor.fetchall()
for persona in personas:
    print(persona)
conexion.close()



# ------------- BORRAR DATOS

import sqlite3
conexion = sqlite3.connect("db1.db")
cursor = conexion.cursor()
cursor.execute("DELETE FROM PERSONAS WHERE edad = 35")
conexion.commit()
conexion.close()



# ------------- ACTUALIZAR DATOS

import sqlite3
conexion = sqlite3.connect("db1.db")
cursor = conexion.cursor()
cursor.execute("UPDATE PERSONAS SET edad = 55 WHERE nombre = 'Ramón'")
conexion.commit()
conexion.close()

