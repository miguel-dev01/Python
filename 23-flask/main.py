from flask import Flask, redirect, url_for, render_template, request, flash
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'clave_secreta_flask'

# Conexión a la base de datos con el driver que hemos instalado (pip install flask-mysqldb)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectoflask'

# Ejecutamos ahora la conexión con la base de datos
variable_mysql = MySQL(app)


# Context processors
# Este context processor es el de mostrar la fecha gracias al modulo de Python "datetime"
@app.context_processor
def Date_Now():
    return {
        'now': datetime.utcnow()
    }

# Endpoints (Rutas)



# Ruta de Inicio de la página
@app.route('/')
def Index():

    edad = 20
    personas = ["Miguel", "Maria", "Tony Stark", "Pepper Pots"]

    return render_template('index.html',
                            edad=edad,
                            dato1="Valor",
                            dato2="Valor2",    
                            lista=["uno", "dos", "tres"],
                            personas=personas
                        )

# Ruta de Información
@app.route('/informacion')
@app.route('/informacion/<nombre>')
@app.route('/informacion/<nombre>/<apellidos>')
def Informacion(nombre = None, apellidos = None):

    texto = ""
    if nombre != None and apellidos != None:
        texto = f"<h3>Bienvenido, {nombre} {apellidos}</h3>"

    return render_template('informacion.html', text=texto)

# Ruta de Contacto
@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def Contacto(redireccion = None):

    if redireccion is not None:
        return redirect(url_for('lenguajes-de-programacion'))

    return render_template('contactos.html')


@app.route('/lenguajes-de-programacion')
def Lenguajes():

    return render_template('lenguajes.html')

# En la siguiente vista estamos trabajando con la base de datos:
@app.route('/insertar-coche', methods=['GET', 'POST'])
def Insertar_Coche():
    if request.method == 'POST':

        marca = request.form['marca']
        modelo = request.form['modelo']
        precio  = request.form['precio']
        ciudad = request.form['ciudad']

        cursor = variable_mysql.connection.cursor()
        cursor.execute("INSERT INTO coches VALUES(NULL, %s, %s, %s, %s)", (marca, modelo, precio, ciudad))
        cursor.connection.commit()

        flash('Has creado tu coche correctamente!!')

        return redirect(url_for('Index'))

    return render_template('crear-coche.html')

@app.route('/coches')
def Coches():
    cursor = variable_mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches")
    coches = cursor.fetchall()
    cursor.close()

    return render_template('coches.html', listar_coches=coches)

@app.route('/coche/<coche_id>')
def Coche(coche_id):
    cursor = variable_mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coche = cursor.fetchall()
    cursor.close()

    return render_template('coche.html', coche=coche)


@app.route('/borrar-coche/<coche_id>')
def Borrar_Coche(coche_id):
    cursor = variable_mysql.connection.cursor()
    cursor.execute(f"DELETE FROM coches WHERE id = {coche_id}")
    variable_mysql.connection.commit()

    flash('El coche ha sido eliminado!!')

    return redirect(url_for('Coches'))


if __name__ == '__main__':
    app.run(debug=True)