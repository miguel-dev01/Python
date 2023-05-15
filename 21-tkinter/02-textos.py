"""
fg --> Color de letra
bg --> Color de fondo en las letras
padx --> 20px (márgenes dentro del texto)
pady --> Meterá pixeles por encima y debajo de mi texto
anchor --> Para mover de posición(Mirar detenidamente la imagen facilitada por el profesor)
side --> Mediante SIDE puedes cambiar de una forma más directa la posición de un elemento.
"""
from tkinter import *

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa.")
texto.config(cursor="circle", height=3, bg="red", font=("Consolas", 15), padx=10, pady=20)
texto.pack(anchor=SE)

def Pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}, veo que eres de {pais}"

# Le hemos puesto el nombre del parámetro para que dé igual el orden en que esté en el Label.
texto = Label(ventana, text=Pruebas(nombre="Miguel", pais="España", apellidos="Sanchez"))
texto.config(
    fg="White",
    bg="black",
    padx=30,
    pady=40, 
    font=("Book Antiqua", 20)
)
texto.pack()

ventana.mainloop()