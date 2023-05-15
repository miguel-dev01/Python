# ¿Que es Tkinter?
# Es un módulo para crear interfaces graficas para el usuario (ventanas)
from tkinter import *
import os.path

# Con esta clase podemos indicar al programa unos valores/propiedades por defecto de Tkinter.
class Programa:
    def __init__(self):
        self.title = "Máster en Python con el profesor Víctor Robles"
        self.icon = "./imagenes/python_18894.ico"
        self.icon_alternative = "./21-tkinter/imagenes/python_18894.ico"
        self.size = "770x470"
        self.resizable = False
        self.dato = "Escrito desde un self, dentro del constructor"

    def Cargar(self):
        # Crear la ventana raíz
        ventana = Tk()
        self.ventana = ventana

        # Titulo de la ventana.
        ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        # Lo siguiente seria una ruta alternativa por si la primera ruta no cargase
        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alternative)

        # Iconos de la ventana (Favicon)
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa. La ruta absoluta de un fichero o archivo.
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Cambio en el tamaño de la ventana.
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

    def addTexto(self, dato):
        texto = Label(self.ventana, text=self.dato)
        texto.pack()

    def CargarPrograma(self):
        self.ventana.mainloop()

# Instanciar(ejecutar) el programa mediante la clase
programa = Programa()
programa.Cargar()

programa.addTexto("Hola soy el texto número 2")
programa.addTexto("Hola soy el texto número 2")
programa.addTexto("Hola soy el texto número 3, viva Python")

programa.CargarPrograma()