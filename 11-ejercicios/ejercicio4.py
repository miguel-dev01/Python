"""
Ejercicio 4.
Crear un script que tenga cuatro variables: Una lista, un string, un entero y un booleano. Y que
imprima un mensaje según el tipo de dato.
"""
# Hecho sin función
"""
lista = ["Hola mundo", 10]
string = "Miguel"
entero = 10
booleano = True

if lista != list:
    print(f"Es de tipo {type(lista)}")
elif string != str:
    print(f"Es de tipo {type(string)}")
elif entero != int:
    print(f"Es de tipo {type(entero)}")
elif booleano != bool:
    print(f"Es de tipo {type(booleano)}")
else:
    print("Mierda todo")
"""

# Hecho con una función


def comprobarTipado(dato, tipo):
    test = isinstance(dato, tipo)
    result = ""

    if test:
        result = f"Este dato es del tipo {type(dato)}"
    else:
        result = None
    
    return result

lista = ["Hola mundo", 10]
string = "Miguel"
entero = 10
booleano = True

print(comprobarTipado(lista, list))
