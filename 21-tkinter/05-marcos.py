"""
La sintaxis para los marcos es bastante similar a la de los textos(Label), solo se cambia -
Frame por Label
relief --> La de un conjunto de relieve al marco. Se puede poner en constante "", o en mayusculas y
sin comillas
"""
from distutils.command.config import config
from tkinter import *

ventana = Tk()
ventana.title("Marcos y Frames en máster en Python")
ventana.geometry("700x600")
ventana.iconbitmap("./21-tkinter/imagenes/python_18894.ico")

# Marco Padre 1
marco_padre = Frame(ventana, height=250, width=250)
marco_padre.config(
            bg="pink",
            bd=10,
            relief=GROOVE
            #relief="solid"
)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)

# Marco 1
marco = Frame(marco_padre, height=250, width=250)
marco.config(
            bg="lightblue",
            bd=10,
            relief=SOLID
            #relief="solid"
)
marco.pack(side=RIGHT)
marco.pack_propagate(FALSE)

texto = Label(marco, text="Primer marco")
texto.config(bg="lightblue", fg="white", font=("Consolas", 15), height=4, width=15, anchor=CENTER, bd=3, relief=SOLID)
texto.pack(anchor=S)


# Marco 2
marco = Frame(marco_padre, height=250, width=250)
marco.config(
            bg="yellow",
            bd=10,
            relief=SOLID
            #relief="solid"
)
marco.pack(side=BOTTOM, anchor=SW)


#---------------------------------------------

# Marco Padre 2
marco_padre = Frame(ventana, height=250, width=250)
marco_padre.config(
            bg="green2",
            bd=10,
            relief=GROOVE
            #relief="solid"
)
marco_padre.pack(side=TOP, anchor=N,fill=X, expand=YES)

# Marco 1
marco = Frame(marco_padre, height=250, width=250)
marco.config(
            bg="orange",
            bd=10,
            relief=SOLID
            #relief="solid"
)
marco.pack(side=LEFT)

# Marco 2
marco = Frame(marco_padre, height=250, width=250)
marco.config(
            bg="azure4",
            bd=10,
            relief=SOLID
            #relief="solid"
)
marco.pack(side=RIGHT, anchor=SE)


ventana.mainloop()