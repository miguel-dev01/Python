from tkinter import *
ventana = Tk()

ventana.geometry("700x600")
ventana.iconbitmap("./21-tkinter/imagenes/python_18894.ico")
ventana.title("Trabajando con los menús de Tkinter en Python")

# Creando el menú
mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

# Creamos el segundo menú
archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)


# Creamos el menú principal
mi_menu.add_cascade(label="Archivo", menu=archivo)
mi_menu.add_command(label="Editar")
mi_menu.add_command(label="Selección")


ventana.mainloop()