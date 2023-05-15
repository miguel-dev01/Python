"""
Variable local es aquella que se define dentro de la funcion y no fuera. Solo estan disponibles dentro,
a no ser que hagamos RETURN.

Variables globales son las que se declaran fueran de la funcion y estan disponibles dentro 
y fuera de ellas.

"""

# Variable global

frase = "Visteme despacio que tengo prisa"

print(frase)


def holamundo():
    #frase = "Hola mundo a todos!!"
    print(frase)

    global website
    website = "mi variable global llamada website, de forma que ahora lo puedo poner dentro y fuera"


    year = 2021
    print(year)


holamundo()
print(website)
# Si yo a continuacion hago print de YEAR, va a dar error porque no existe. Dado que donde
# si existe es dentro de la funcion "holamundo", por tanto es variable local