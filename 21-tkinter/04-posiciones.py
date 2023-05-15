"""
Con (fill), relleno en el eje X, es decir, en horizontal.
Y con (expand) le confirmamos que lo haga, por así decirlo, por tanto expand=YES.

"""
from tkinter import *

ventana = Tk()
# ventana.geometry("700x500")
ventana.iconbitmap("./21-tkinter/imagenes/python_18894.ico")

texto = Label(ventana, text="Bienvenido a mi programa. Aquí veremos posiciones")
texto.config(cursor="circle", height=3, bg="red", font=("Consolas", 15), padx=10, pady=20)
texto.pack(side=TOP, fill=X, expand=YES)


texto = Label(ventana, text="Bienvenido a Python, con Tkinter")
texto.config(
    fg="White",
    bg="black",
    padx=30,
    pady=40, 
    font=("Book Antiqua", 20)
)
texto.pack(side=TOP)


texto = Label(ventana, text="Basico 1")
texto.config(
    fg="White",
    bg="Cyan",
    padx=30,
    pady=40,
    font=("Consolas", 20)
)
texto.pack(side=LEFT, fill=X, expand=YES)


texto = Label(ventana, text="Basico 2")
texto.config(
    fg="Orange",
    bg="Blue",
    padx=30,
    pady=40,
    font=("Consolas", 20)
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico 3")
texto.config(
    fg="light cyan",
    bg="maroon",
    padx=30,
    pady=40,
    font=("Consolas", 20)
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()