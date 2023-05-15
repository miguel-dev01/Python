"""
SET --> Es una coleccion de datos o valores pero no tienen ningun index ni orden...
"""

personas = {
    "Miguel",
    "Francisco",
    "Elon Musk"
}

personas.add("Paquico")
personas.remove("Francisco")

print(type(personas))
print(personas)