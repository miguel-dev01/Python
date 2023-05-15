"""
Definicion de lista: 
LISTAS (arrays)
Son colecciones de datos bajo un unico nombres y para acceder a esos valores debemos usar un indice
númerico. Es decir, contiene un conjunto de variables.
"""

pelicula = "batman"
print(pelicula)

# Forma 1 para definir una lista
peliculas = ["Iron Man","Spiderman","Capitan America"]
print(peliculas)

# Forma 2 para definir una lista
cantantes = list(('Drake','Jennifer','Nate Gentile'))
print(cantantes)

# Lista para introducir rangos de numeros
years = list(range(2020, 2050))
print(years)

# Lista variada
variada = ["Miguel", 30, 4.4, True, "Texto"]
print(variada)

# Acceder a Indices
print(peliculas[0])
print(peliculas[-2])
# Indices con un rango, de tal a tal
print(cantantes[0:3])

# Desde un indice en concreto
print(peliculas[1:])

# Añadir elementos a una lista ya existente
cantantes.append("Heroes del Silencio")

print(cantantes)


# Recorrer lista
print("\n**** LISTADO DE PELICULAS ****")

nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce una pelicula: ")
    peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)} {pelicula}")

# Listas multidimensionales. Son listas dentro de otras listas.

print("\n Listado de contactos")
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'Salvador',
        'salvador@salvador.com'
    ]
]

# Para acceder a una lista en concreto se empieza a contar desde el 0.
print(contactos[1])

# Recorrer lista en multidimensional, con bucle FOR
for contacto in contactos:
    print(contacto[0])

# Recorrer listas. Mas pro...

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("E-mail: " + elemento)
