# RECUERDA QUE ESTA MAL, HAY MUCHAS COSAS QUE CORREGIR EN ESTAS CLASES DE BASES DE DATOS Y SQL
import mysql.connector

# Ahora realizamos la conexión
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
)

# ¿Como sé que la conexión ha sido realizada correctamente?
# Pues ejecutanto, print(database)

cursor = database.cursor()

# Crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAIT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

# cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")

# Con executemany podemos insertar registros de forma simultanea en la base de datos.
coches = [
    ('Opel','Corsa GS Line', 20000)
    ('Renault','Clio', 50040)
    ('Citroen','Saxo', 57000)
    ('Mercedes-Benz','Clase A', 40000)
]
cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

database.commit()

cursor.execute("SELECT * FROM vehiculos WHERE <= 5000 AND marca = 'Seat' ")
result = cursor.fethall()

print("----- TODOS MIS COCHES -----")
for coche in result:
    print(coche[2])