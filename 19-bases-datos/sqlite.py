"""
SQLITE es un gestor de bases de datos que viene preinstalado en Python.
"""

# Importar módulo
import sqlite3

# Realizamos la conexión con la siguiente línea y le pasamos el parametro, que será el nombre de la base de datos
conexion = sqlite3.connect("pruebas.db")

# Para realizar consultar a nuestra BD, debemos crear "cursor" me va a permitir ejecutar consultas.
cursor = conexion.cursor()
 
# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(225),
    descripcion text,
    precio int(255)
);
""")

# Guardar los cambios
conexion.commit()

# Insertar datos
""" # DESCOMENTAR CUANDO HAYA FINALIZADO LA CLASE
cursor.execute("INSERT INTO productos VALUES (null, 'Primer productor', 'Descripción de mi producto', 550)")
conexion.commit()
"""

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Insertar muchos registros simultaneamente
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Disco duro 1TB", "Buen Disco", 100),
    ("PC sobremesa", "Buen PC", 500),
    ("Licencias de software", "Buena licencia", 50),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

#    RECUERDA QUE QUEDABAN ALGUNAS MIGAJAS TIPO: HACER UNA CONSULTA SI SE DA UNA CONDICIÓN, ETC...
# Listar datos para leerlos.
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
print(productos)
        
for producto in productos:
    print("ID: ", producto[0])
    print("Descripción: ", producto[1])
    print("Descripción: ", producto[2])
    print("Descripción: ", producto[3])
    print("\n")

producto = cursor.fetchone()
print(producto)

# Y hay que cerrar la conexion ya que si no el fichero se quedará abierto.
conexion.close