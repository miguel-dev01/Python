from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")
ventana.iconbitmap("./21-tkinter/imagenes/python_18894.ico")

Label(ventana, text="Hola Soy un progromador pre-junior").pack(anchor=W)

imagen = Image.open('./21-tkinter/imagenes/tesla.jpg')
renderizar = ImageTk.PhotoImage(imagen)

Label(ventana, image=renderizar).pack(anchor=E)

ventana.mainloop()