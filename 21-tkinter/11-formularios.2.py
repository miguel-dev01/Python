from tkinter import *

ventana = Tk()
ventana.geometry("500x350")
ventana.iconbitmap("./21-tkinter/imagenes/python_18894.ico")
ventana.title("Formularios 2. Más avanzados")

encabezado = Label(ventana, text="FORMULARIOS 2")
encabezado.config(
    padx=15,
    pady=15,
    bg="blue",
    font=("Consolas", 20)
)
encabezado.grid(row=0, column=0, columnspan=6, sticky=W)

# Botones Check
def mostrarProfesion():
    texto = ""

    if python.get():
        texto += "Te dedicas al desarrollo y creación de programas con Python "

    if patatas.get():
        if python.get():
            texto += "y te dedicas a plantar patatas en la huerta"
        else:
            texto += "Te dedicas a plantar patatas en la huerta"

    mostrar.config(
        text=texto,
        bg="green",
        fg="white",
        
    )


python = IntVar()
patatas = IntVar()

Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0, sticky=W)

# Check 1
Checkbutton(
    ventana, 
    text="A desarrollar y programar con Python",
    variable=python,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion,
).grid(row=2, column=0, sticky=W)


# Check 2
Checkbutton(
    ventana, 
    text="A plantar patatas",
    variable=patatas,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion,
).grid(row=3, column=0, sticky=W)

mostrar = Label(ventana, bg="green")
mostrar.grid(row=4, column=0, sticky=W)


# Radio Buttons
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cuál es tu genero?").grid(row=5, column=0)

Radiobutton(
    ventana, 
    text="Masculino",
    value="Masceulino",
    variable=opcion,
    command=marcar
).grid(row=6, column=0)

Radiobutton(
    ventana, 
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7, column=0)

marcado = Label(ventana)
marcado.grid(row=8, column=0)

# Option Menu
def seleccionar():
    seleccionado.config(text=opcionn.get())


opcionn = StringVar()
opcionn.set("Opción 1")

Label(ventana, text="Selecciona una opción").grid(row=5, column=1)

select = OptionMenu(ventana, opcionn, "Opción 1", "Opción 2", "Opción 3")
select.grid(row=6, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)




ventana.mainloop()