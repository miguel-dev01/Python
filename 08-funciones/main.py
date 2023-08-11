"""
Las funciones son un grupo de instrucciones agrupadas bajo un nombre concreto y que se puede usar
tantas veces como sea preciso, "invocando" el nombre de dicha función

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)

"""

# EJEMPLO 1

print("####### EJEMPLO 1 #######")

# Definir funcion
def muestranombres():
    print("Miguel")
    print("Victor")
    print("Elon Musk")
    print("Maria")
    print("Alejandro")
    print("Angel")
    print("\n")

# Invocar a la funcion
muestranombres()
muestranombres()



# EJEMPLO 2: parametros
print("####### EJEMPLO 2 #######")

def mostrartunombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")

nombre = input("Introduce tu nombre: ")

mostrartunombre(nombre, 18)



# EJEMPLO 3: 
print("####### EJEMPLO 3 #######")

def tabla(numero):
    print(f"Tabla de multiplicar del {numero}")

    for tabla in range(11):
        operacion = numero * tabla
        print(f"{numero} * {tabla} = {operacion}")

tabla(5)
tabla(7)




# EJEMPLO 4 : Parametros opcionales, se le puede poner FALSE, o bien un numero o texto por defecto
print("####### EJEMPLO 4 #######")

def getEmpleado(nombre, dni = None):
    print("Informacion del EMPLEADO")
    print(f"Nombre: {nombre}")
    print(f"DNI: {dni}")

    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Miguel Sanchez")



# EJEMPLO 5: Mas sobre parametros opciones y RETURN
print("####### EJEMPLO 5 #######")

def saludame(nombre):
    saludo = f"Hola saludos, {nombre}"

    return saludo

print(saludame("Miguel Sanchez"))


#EJEMPLO 6
print("####### EJEMPLO 6 #######")

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    cadena += "Suma: " + str(suma)
    cadena += "Resta: " + str(resta)
    cadena += "Multiplicacion: " + str(multiplicacion)
    cadena += "division: " + str(division)
    """
    # print() sirve para mostrar un mensaje en la pantalla de una aplicación de consola, 
    # mientras que RETURN se utiliza para establecer el resultado (o valor de retorno) de una función. 
    # Así, return es una operación mucho más genérica que print()
    """
    return cadena

print(calculadora(1, 1))


#EJEMPLO 7
print("####### EJEMPLO 7 #######")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"

    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"

    return texto

def devuelvetodo():
    texto = getNombre + "/n" + getApellidos
    return texto

print(devuelvetodo())

#EJEMPLO 8: Funcion Lambda (Funcion anonima, es decir, que no tiene nombre, sirve para 
# tarear muy muy pequeñas y concretas)
print("####### EJEMPLO 8 #######")

dime_el_año = lambda year: f"El año es {year}"

print(dime_el_año(2050))