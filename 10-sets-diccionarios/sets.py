"""
SET --> Es una coleccion de datos o valores pero no tienen ningun index ni orden...
"""

personas = {
    "Miguel",
    "Paquico",
    "Maria"
}

personas.add("Quique")
personas.remove("Paquico")

print(type(personas))
print(personas)