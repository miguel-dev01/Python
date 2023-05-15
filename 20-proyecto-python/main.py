"""
Proyecto de Python y MySQL, hará lo siguiente:
- Abrir un asistente.
-   Que nos dé a elegir si nos registramos en el programa, o nos logueamos.
-       Si elegimos REGISTRARNOS, creará un usuario en la base de datos.
-       Si elegimos LOGIN, se identificará al usuario y nos preguntará la password.
- Crear notas, mostrar notas, y borrarlas.
"""
from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login
""")
hazEl = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion == "registro":
    # Aqui tenemos la lógica del "registro", sin embargo, para no tenerlo todo concentrado en un único fichero, lo dividiremos en varios de estos.
    hazEl.registro()

elif accion == "login":
    hazEl.login()
