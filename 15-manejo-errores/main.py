# Capturar excepciones y manejar errores en código susceptible a fallos.

# ¿Como funcionan?
try:
    nombre = input("¿Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_usuario = "El nombre es" + nombre 

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduce bien el nombre")
else:
    print("Todo ha funcionado correctamente")


# Multiples excepciones
try:
    numero = int(input("Número para elevarlo al cuadrado: "))

    print("El cuadrado es " + str(numero*numero))

except TypeError:
    print("Debes convertir tus cadenas a integeer (enteros)")

except ValueError:
    print("Introduce números, no cadenas de texto.")

# Se puede hacer un EXCEPT, error más amigable, es decir que nos muestre automaticamente el error.
except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__)


# Excepciones personalizadas o lanzar excepciones

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real o atribuible a un ser humano")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido al maravilloso mundo de Python, {nombre}")
except ValueError:
    print("Introduce los datos de forma correcta, por favor")
# Ya hemos implementado el tipo de error: ValueError, pero si saltara otro tipo de error, hariamos lo siguente:
except Exception as e:
    print("Existe un error", e)




