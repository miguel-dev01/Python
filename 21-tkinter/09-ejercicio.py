"""
CALCULADORA:
- Dos campos de texto
- 4 botones para las operaciones
- Mostrar el resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.config(bd=25)
ventana.geometry("490x335")
ventana.iconbitmap("./21-tkinter/imagenes/calculadora.ico")
ventana.title("Calculadora. Ejercicio de Python y Tkinter. Por Miguel Sánchez")

# Marco
marco = Frame(ventana, width=430, height=250)
marco.config(
    padx=15,
    pady=15,
    bd=10,
    relief=SOLID
)
marco.pack_propagate(False)
marco.pack(side=TOP, anchor=CENTER)

# Parte lógica del programa.

def CFloat(numero):
    try:
        result = int(numero)
    except:
        result = 0
        messagebox.showerror("Error", "No se pueden introducir letras o caracteres raros, soplagaitas.")

    return result


def Sumar():
    resultado.set(CFloat(numero1.get()) + CFloat(numero2.get()))
    mostrarResultadoSumar()

def mostrarResultadoSumar():
    messagebox.showinfo("Resultado", f"El Resultado de la operación de la suma es: {resultado.get()}")


def Restar():
    resultado.set(CFloat(numero1.get()) - CFloat(numero2.get()))
    mostrarResultadoResta()

def mostrarResultadoResta():
    messagebox.showinfo("Resultado", f"El resultado de la operación de resta es: {resultado.get()}")


def Multiplicar():
    resultado.set(CFloat(numero1.get()) * CFloat(numero2.get()))
    mostrarResultadoMultiplicacion()

def mostrarResultadoMultiplicacion():
    messagebox.showinfo("Resultado", f"El resultado de la operación de multiplicación es: {resultado.get()}")


def Dividir():
    resultado.set(CFloat(numero1.get()) / CFloat(numero2.get()))
    mostrarResultadoDivision()

def mostrarResultadoDivision():
    messagebox.showinfo("Resultado", f"El resultado de la operación de división es: {resultado.get()}")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()


# Campo 1. Formulario + Texto

texto_campo1 = Label(marco, text="Introduce el primer número a calcular:")
texto_campo1.config(font=("Book Antiqua", 15))
texto_campo1.pack()


campo1 = Entry(marco, textvariable=numero1)
campo1.config(font=("Consolas", 15), justify="center")
campo1.pack()


# Campo 2. Formulario + Texto

texto_campo2 = Label(marco, text="Introduce el segundo número a calcular:")
texto_campo2.config(font=("Book Antiqua", 15))
texto_campo2.pack()


campo2 = Entry(marco, textvariable=numero2)
campo2.config(font=("Consolas", 15), justify="center")
campo2.pack()

Button(marco, text="Sumar", activebackground="#F50743", command=Sumar).pack(side="left", anchor=CENTER, fill=X, expand=YES)
Button(marco, text="Restar", activebackground="#F50743", command=Restar).pack(side="left", anchor=CENTER, fill=X, expand=YES)
Button(marco, text="Multiplicar", activebackground="#F50743", command=Multiplicar).pack(side="left", anchor=CENTER, fill=X, expand=YES)
Button(marco, text="Dividir", activebackground="#F50743", command=Dividir).pack(side="left", anchor=CENTER, fill=X, expand=YES)





ventana.mainloop()