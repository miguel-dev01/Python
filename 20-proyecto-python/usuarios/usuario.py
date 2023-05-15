import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

# Tenemos que dar una serie de parámetros para realizar la conexión con la base de datos.
""" # En el caso siguiente lo he comentado para realizarlo en el fichero "conexion.py".
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="master_python",
    port=3306
)

cursor = database.cursor(buffered=True)
"""


class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()

        # Debemos cifrar la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

        
    def identificar(self):
        # Consulta para comprobar si existe el usuario con su correspondiente contraseña. Si estos coinciden, se nos dará acceso.
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s "

        # Ciframos la contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # Datos que van a ir a la base de datos en forma de consulta.
        usuario = (self.email, cifrado.hexdigest())

        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result


# Lo que hace (%s) es sustituir cada campo por cada (%s) que haya. Despues executamos las variables -
# con cursor.execute. Y posteriormente con database.commit es lo que va a hacer que se guarden las -
# consultas en la base de datos.

# Lo de cursor.rowcount nos hará saber cuantos registros se han modificado en la base de datos.
