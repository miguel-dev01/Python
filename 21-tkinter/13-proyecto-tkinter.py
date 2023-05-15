"""
Crear un programa que tenga:
- Ventana (No redimensionable)
- Tamaño fijo
- Un menú (Inicio, Añadir, Info, Salir)
- Opción de salir
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla "home"
"""
from tkinter import *
from tkinter import ttk

# Definir ventana
ventana = Tk()
# ventana.geometry("700x600")
ventana.minsize(500, 500)
ventana.resizable(0, 0)
ventana.iconbitmap("./21-tkinter/imagenes/python3.ico")
ventana.title("Proyecto Tkinter - Máster en Python. Por Miguel Sánchez")

# Pantallas
def Home():
    # Montar pantalla
    home_label.config(fg="white", bg="black", font=("Arial", 30), padx=200, pady=20)
    home_label.grid(row=0, column=0, columnspan=5)

    # Mostrar caja de los productos
    products_box.grid(row=1)

    """
    # Listar todos los productos sin tabla TTK
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="-------------------------").grid()
    """
    # Listar todos los productos con tabla TTK
    for product in products:
        if len(product) == 3:
            product.append("added")
            products_box.insert('', 0, text=product[0], values = (product[1]))


    # Ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()


def Add():
    # Encabezado principal de la pantalla
    add_label.config(fg="white", bg="black", font=("Arial", 30), padx=150, pady=20)
    add_label.grid(row=0, column=0, columnspan=10)

    # Creamos un frame para no tener que poner el .grid_remove() funcion por funcion, uno por uno
    add_frame.grid(row=1)

    # Etiqueta del nombre del producto
    add_name_label.config(font=("Microsoft YaHei Light", 10))
    add_name_label.grid(row=1, column=0, sticky=N)

    # Campo de formulario del nombre del producto
    add_name_entry.config(font=("Consolas", 15), justify=CENTER)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    # Etiqueta del precio del producto
    add_price_label.config(font=("Microsoft YaHei Light", 10))
    add_price_label.grid(row=2, column=0, sticky=N)

    # Campo de formulario del precio del producto
    add_price_entry.config(font=("Consolas", 15), justify=CENTER)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    # Etiqueta de la descripción
    add_description_label.config(font=("Microsoft YaHei Light", 10))
    add_description_label.grid(row=3, column=0, sticky=N)

    # Campo de formulario de la descripción
    add_description_entry.config(height=5, widt=35, font=("Consolas", 10))
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    # Botón de guardar formulario
    boton.config(fg="#3673A5", bg="#FFD342", activebackground="#980F0F", font=("Helvetica", 13, "bold"), padx=10, pady=10)
    boton.grid(row=4, column=1, padx=10, pady=10)

    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()

    return TRUE

def Info():
    info_label.config(fg="white", bg="black", font=("Arial", 30), padx=150, pady=20)
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    home_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()


def addProducts():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    Home()


# Variables importantes definidas para los Entry de los formularios
products = []
name_data = StringVar()
price_data = StringVar()


# Definir campos de pantallas / (INICIO), LAS DEFINO ¡¡FUERA!! PARA QUE NO SE SOLAPEN CON LAS DEMAS PANTALLAS.
home_label = Label(ventana, text="Inicio")
# products_box = Frame(ventana, width=250)


products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text='Producto', anchor=W)
products_box.heading("#1", text='Precio', anchor=W)

# Definir campos de pantallas / (añadir)
add_label = Label(ventana, text="Añadir producto")



# Definir campos de formularios
add_frame = Frame(ventana)

add_name_label = Label(add_frame, text="Nombre del producto: ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio del producto: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción del producto: ")
add_description_entry = Text(add_frame)

boton = Button(add_frame, text="Guardar datos", command=addProducts)


# Definir campos de pantallas / (info) e (info2)
info_label = Label(ventana, text="Mostrar información")
data_label = Label(ventana, text="Creado por Miguel Sánchez, un domingo del verano del 2022")

# Cargar pantalla de inicio del programa
Home()

# Creando los menús
mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

mi_menu.add_command(label="Inicio", command=Home)
mi_menu.add_command(label="Añadir", command=Add)
mi_menu.add_command(label="Información", command=Info)
mi_menu.add_command(label="Salir", command=ventana.quit)



# Cargar ventana, hasta que la cerremos nosotros
ventana.mainloop()