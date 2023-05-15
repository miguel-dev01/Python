# Vamos a recordar que toda la lógica mostrada a continuación se puede realizar en un solo fichero -
# pero para que todo no se encuentre en un único archivo lo tendremos todo dividido en varios para -
# tenerlo todo con más y mejor acceso.
import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def registro(self):
        print("\nDe acuerdo. A continuación voy a registrarte en el sistema...")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuarioo = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuarioo.registrar()

        # El siguiente if va ligado al "cursor.rowcount" de "usuario.py". Para que el programa nos diga si nos hemos registrado correctamente.
        if registro[0] >= 1:
            print(f"\nPerfecto, {registro[1].nombre} ,te has registrado correctamente en la base de datos con el email {registro[1].email}.")
        else:
            print("\nLo sentimos, no has sido registrado correctamente en la base de datos")

    def login(self):
        print("\nVale. Identifícate al sistema")

        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido al sistema de Python {login[1]}")
                self.proximasAcciones(login)
                
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto. Inténtalo más tarde.")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear notas (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)
        accion = input("Que acción te gustaría realizar: ")
        hazEl = notas.acciones.Acciones()

        if accion == "crear":
            hazEl.Crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.Mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.Eliminar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Hasta pronto, {usuario[1]}")
            exit()