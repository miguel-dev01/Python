from tkinter import *
from tkinter import messagebox

class Calculadora:

    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas


    def CFloat(self, numero):
        try:
            result = int(numero)
        except:
            result = 0
            messagebox.showerror("Error", "No se pueden introducir letras o caracteres raros, soplagaitas.")

        return result


    def Sumar(self):
        self.resultado.set(self.CFloat(self.numero1.get()) + self.CFloat(self.numero2.get()))
        self.mostrarResultadoSumar()

    def mostrarResultadoSumar(self):
        messagebox.showinfo("Resultado", f"El Resultado de la operación de la suma es: {self.resultado.get()}")


    def Restar(self):
        self.resultado.set(self.CFloat(self.numero1.get()) - self.CFloat(self.numero2.get()))
        self.mostrarResultadoResta()

    def mostrarResultadoResta(self):
        messagebox.showinfo("Resultado", f"El resultado de la operación de resta es: {self.resultado.get()}")


    def Multiplicar(self):
        self.resultado.set(self.CFloat(self.numero1.get()) * self.CFloat(self.numero2.get()))
        self.mostrarResultadoMultiplicacion()

    def mostrarResultadoMultiplicacion(self):
        messagebox.showinfo("Resultado", f"El resultado de la operación de multiplicación es: {self.resultado.get()}")


    def Dividir(self):
        self.resultado.set(self.CFloat(self.numero1.get()) / self.CFloat(self.numero2.get()))
        self.mostrarResultadoDivision()

    def mostrarResultadoDivision(self):
        messagebox.showinfo("Resultado", f"El resultado de la operación de división es: {self.resultado.get()}")


ventana = Tk()
ventana.config(bd=25)
ventana.geometry("490x335")
ventana.iconbitmap("./21-tkinter/imagenes/calculadora.ico")
ventana.title("Calculadora. Ejercicio de Python y Tkinter. Por Miguel Sánchez")

# Llamo a la clase Calculadora, donde se encuentra toda las funciones con la lógica del programa.
calculadora = Calculadora(messagebox)


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




# Campo 1. Formulario + Número a Calcular

texto_campo1 = Label(marco, text="Introduce el primer número a calcular:")
texto_campo1.config(font=("Book Antiqua", 15))
texto_campo1.pack()


campo1 = Entry(marco, textvariable=calculadora.numero1)
campo1.config(font=("Consolas", 15), justify="center")
campo1.pack()


# Campo 2. Formulario + Número a Calcular

texto_campo2 = Label(marco, text="Introduce el segundo número a calcular:")
texto_campo2.config(font=("Book Antiqua", 15))
texto_campo2.pack()


campo2 = Entry(marco, textvariable=calculadora.numero2)
campo2.config(font=("Consolas", 15), justify="center")
campo2.pack()

Button(marco, text="Sumar", activebackground="#F50743", command=calculadora.Sumar).pack(side="left", anchor=CENTER, fill=X, expand=YES)
Button(marco, text="Restar", activebackground="#F50743", command=calculadora.Restar).pack(side="left", anchor=CENTER, fill=X, expand=YES)
Button(marco, text="Multiplicar", activebackground="#F50743", command=calculadora.Multiplicar).pack(side="left", anchor=CENTER, fill=X, expand=YES)
Button(marco, text="Dividir", activebackground="#F50743", command=calculadora.Dividir).pack(side="left", anchor=CENTER, fill=X, expand=YES)





ventana.mainloop()