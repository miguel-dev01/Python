"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento que el usuario pida por teclado
"""

# Crear la lista
lista = [13,64,82,33,44,55,58,96]

# Recorrer la lista y mostrarla
for numero in lista:
    print(numero)

# Ordenarla y mostrarla
lista.sort()
print(lista)

# Mostrar su longitud
print(len(lista))


# Buscar algun elemento que el usuario pida por teclado
i = int(input("Introduce el número del 1 al 100 que quieras buscar: "))

if i > 100:
    print("No se puede introducir un numero mayor que 100, debe ser entre el 1 y el 100")
else:
    if i in lista:
        print(f"El {i} esta en la lista")
    else:
        print(f"El {i} no esta en la lista")



"""
Ejercicio 1.1 Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer una funcion que recorra listas de numeros y devuelva un string
- Ordenarla y mostralarla
- Mostrar su longitud
- Buscar algun elemento que el usuario pida por teclado
"""
print("###### Búsqueda en la lista ######")

busqueda = int(input("Introduce el número: "))

comprobar = isinstance(busqueda, int)
while not comprobar or busqueda <= 0:
    busqueda = int(input("Introduce el número: "))
else:
    print(f"Has introducido el {busqueda}")

print(f"##### Buscar en la lista el número {busqueda} #####")

try:
    search = numeros.index(busqueda)
    print(f"El número buscado existe en la lista, es el índice: {search}")
except:
    print("El número no está en la lista, lo siento")