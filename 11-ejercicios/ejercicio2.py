"""
Ejercicio 2. Escribir un programa que añada valores a una lista mientras que su longitud
sea menor a 120 y luego mostrar la lista.
plus: usar While y For.
"""

# Lo que he hecho yo
lista = list(range(1,51))

i = int(input("Introduce un valor: "))

if i < 120:
    lista.append(i)
    print(lista)
else: 
    print("No se puede introducir este dato a la lista ya que tiene que ser menor que 120")


# Como es según el profesor

coleccion = []

for contador in range(0,120):
    coleccion.append(f"elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])

print(coleccion)

# Resolucion del ejercicio con bucle While

coleccion = []
x = 0

while x < 120:
    coleccion.append(f"elemento-{x}")
    print("Mostrando el " + coleccion[x])
    x += 1

print(coleccion[77])