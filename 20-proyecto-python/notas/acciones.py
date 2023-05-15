import notas.nota as modelo

class Acciones:

    def Crear(self, usuario):
        print(f"\nOk {usuario[1]}, vamos a crear una nueva nota.")

        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Introduce el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.Guardar()

        # Si tengo el rowcount mayor a uno, si me habrá guardado la nota correctamente.
        if guardar[0] >= 1:
            print(f"\nPerfecto, tu nota, {nota.titulo} ha sido guardada correctamente.")
        else:
            print(f"\nNo se ha guardado la nota correctamente, {usuario[1]}")

    def Mostrar(self, usuario):
        print(f"\nVale, {usuario[1]}, aquí tienes todas notas: ")

        nota = modelo.Nota(usuario[0], "", "")
        notas = nota.Listar()

        for nota in notas:
            print("******************************")
            print(nota[2])
            print(nota[3])

    def Eliminar(self, usuario):
        print(f"\nA continuación vamos a eliminar tu nota, {usuario[1]}.")

        titulo = input("Introduce el título de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        suprimir = nota.Suprimir()

        if suprimir[0] >= 1:
            print(f"Hemos borrado {nota.titulo}")
        else:
            print("No se ha borrado la nota. Inténtalo más tarde.")