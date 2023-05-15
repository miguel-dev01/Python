from tkinter import *
ventana = Tk()

ventana.geometry("700x500")
ventana.iconbitmap("./21-tkinter/imagenes/python_18894.ico")
ventana.title("Recoger datos de los formularios de Tkinter")
ventana.config(
    bd=50,
)

def getDato():
    resultado.set(dato.get())
    if len(resultado.get()) >= 1:
        texto_resultado.config(bg="green")

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Mete un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_resultado = Label(ventana, textvariable=resultado)
texto_resultado.pack(anchor=NW)


Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)


ventana.mainloop()