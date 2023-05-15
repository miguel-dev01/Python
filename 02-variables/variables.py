"""
Una variable es un contenedor de informacion que dentro guardará un dato,
se pueden crear muchas variables y que cada una tenga un dato distinto.
"""

# VARIABLES

texto = "master en Python"
texto2 = "segunda frase"
numero = 45

print(texto)
print(texto2)
print(numero)

# CONCATENACION

nombre = "Miguelico"
apellidos = "Sanchez"
web = "blogmart.es"

    #1º forma para concatenar

print(nombre + " " + web)

    #2º forma para concatenar

print(f"{nombre} {apellidos} {web}")

    #3º forma para concatenar

print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))