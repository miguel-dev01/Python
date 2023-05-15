# El constructor es un método (poner definicion)

from coche import Coche

carro = Coche("Blanco", "Tesla", "Model X", 220, 250, 6)
carro2 = Coche("Verde", "Seat", "Ibiza", 200, 110, 4)
carro3 = Coche("Azul", "Citroen", "Xsara", 205, 115, 5)
carro4 = Coche("Rojo", "Nissan", "Leaf", 210, 120, 5)

print(carro.getMarca(), carro.getModelo(), carro.getColor())
print(carro2.getMarca(), carro2.getModelo(), carro2.getColor())



print("\n ----------")
print(carro.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())


# Detectar tipado
if type(carro3) == Coche:
    print("Es un objeto que nos interesa, es correcto")
else:
    print("Es un objeto incorrecto, no nos interesa")
        # Sin embargo, si carro3, lo dejamos como variable suelta, sin hacer referencia a la clase, no se cumpliría la condición.

# VISIBILIDAD
# Nos puede servir si algunas de las funciones de un objeto sean publicadas o denegadas a que sean
# vistas por todo el mundo.

# Público
print(carro.soy_publico)

# print(carro.__soy_privado)

# Para que no dé error, un elemento privado debe mostrarse de la siguiente forma:
print(carro.getPrivado())