
# Crear base de datos
# Crear tabla productos con 3 campos:
#   -id : tipo numérico
#   -nombre : tipo texto
#   -precio : tipo numérico

# Insertar 3 productos:
#   1, "impresora", 300
#   2, "ratón", 20
#   3, "ordenador", 600

# Consultar productos de la tabla y cerrar la BBDD.


import sqlite3
conexion = sqlite3.connect("ejerciciobbdd.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE PRODUCTOS (id INTEGER, nombre TEXT, precio INTEGER)")
conexion.commit()

lista_productos = [(1,'Impresora', 300), (2,'Ratón',20), (3,'Ordenador', 600)]
cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", lista_productos)
conexion.commit()

cursor.execute("Select * from PRODUCTOS")
consulta_productos = cursor.fetchall()
for producto in consulta_productos:
    print(producto)

conexion.close()