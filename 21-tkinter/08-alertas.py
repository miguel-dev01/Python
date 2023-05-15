from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("700x600")
ventana.iconbitmap("./21-tkinter/imagenes/python_18894.ico")
ventana.title("Alertas en Tkinter, junto con Python")
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Soy Miguel Sánchez")
    MessageBox.showwarning("Alerta de Peligro", "Soy Miguel Sánchez")
    MessageBox.showerror("Alerta de Error", "De Python al cielo")


Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()

# También podemos sacar alertas como ¿Quieres seguir usando la aplicación?

def salir(nombre):
    resultado = MessageBox.askquestion("Salir","¿Quieres continuar ejecutando la aplicación?")
    if resultado != "yes":
        MessageBox.showinfo("Chao Pescao", f"Adiós {nombre}")
        ventana.destroy()


Button(ventana, text="Mostrar segunda alerta", command=lambda: salir("Miguelico")).pack()



ventana.mainloop()