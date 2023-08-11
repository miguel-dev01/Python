cantantes = ["Heroes del Silencio","Shinova","Shakira","Julio Iglesias"]
numeros = [1, 2, 5, 8, 3, 4]

# Ordenar una lista
print(numeros)
numeros.sort()
print(numeros)

# Añadir elementos
cantantes.append("Paco Pepe","p")
cantantes.insert(1, "David Bisbal")
print(cantantes)

# Eliminar elementos
cantantes.pop(1)
cantantes.remove("Shakira")
print(cantantes)

# Dar la vuelta
numeros.reverse()
print(numeros)

# Buscar dentro de una lista, tan solo con IN.
print('Shakira' in cantantes)

# Contar elementos
print(len(cantantes))

# Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

# Conseguir indice
print(cantantes.index("Shakira"))

# Unir dos listas
cantantes.extend(numeros)
print(cantantes)