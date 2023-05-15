from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios de Máster en Python")
ventana.iconbitmap("./21-tkinter/imagenes/python_18894.ico")

# Texto encabezado
encabezado = Label(ventana, text="Formularios con Tkinter, hecho por Miguel Sánchez")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 15),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=12)

# Texto para el campo del formulario. (Nombre)
label = Label(ventana, text="Nombre")
label.config(font=("Consolas", 12))
label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

# Campo de texto de nuestro formulario:
# Side y Anchor se utilizan especialmente para ordenar cajas. Se hace difícil ordenar formularios así.
# Por tanto usamos grid.

# Formulario de (Nombre)
campo_texto = Entry(ventana)
campo_texto.config(justify="left", state="normal")
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)

# Texto para campo (Apellidos)
label = Label(ventana, text="Apellidos")
label.config(font=("Consolas", 12))
label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

# Formulario de (Apellidos)
campo_texto2 = Entry(ventana)
campo_texto2.config(justify="left", state="normal")
campo_texto2.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Texto para campo (Descripción)
label = Label(ventana, text="Descripción")
label.config(font=("Consolas", 12))
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

# Campo de texto grande (Descripción)
campo_grande = Text(ventana)
campo_grande.config(width=30, height=5, font=("Book Antiqua", 12))
campo_grande.grid(row=3, column=1)

# Botón
Label(ventana).grid(row=4, column=1)  # Separador de botón, usando Label

boton = Button(ventana, text="ENVIAR")
boton.config(padx=15, pady=15, bg="green", fg="white")
boton.grid(row=5, column=1, sticky=W)


ventana.mainloop()