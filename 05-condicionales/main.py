# Si un dato cumple una condicion se van a ejecutar un grupo de instrucciones 
# y si no, se ejecutaran otro grupo de instrucciones.
"""
#CONDICIONAL IF

SI se cumple esta condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutan otro grupo de instrucciones

if conficion:
    instrucciones
else:
    otras instrucciones


#OPERADORES DE COMPARACION
== igual
!= diferente
<  menor que
>  mayor que
<= menor o igual que
>= mayor o igual que

#OPERADORES LOGICOS
and --> Y
or --> O
! --> negacion
not --> NO
"""

#Ejemplo1
print("\n##################### EJEMPLO 1 #########################")

#color = "rojo"
color = input("Adivina cual es mi color favorito:")

if color == "negro":
    print("Enhorabuena!!!")
    print("Has acertado cual es mi color favorito")
else:
    print("Lo siento mucho, has fallado")
    print("Mi color favorito es el negro")


"""
#Ejemplo 2
print("\n##################### EJEMPLO 2 #########################")

#year = 2020
year = int(input("¿En que año estamos?"))

if year >= 2021:
    print("Estamos de 2021 en adelante !!")
else:
    print("Es un año anterior a 2021")
"""


#Ejemplo 3
print("\n##################### EJEMPLO 3 #########################")

nombre = "Miguel Sanchez"
ciudad = "Murcia"
continente = "Europa"
edad = int(input("Indique su edad:"))
mayoria_edad = 18

if edad > mayoria_edad:
    print(f"{nombre} con residencia en {ciudad}, es mayor de edad")

    if continente != "Europa":
        print("El usuario NO es europeo")
    else:
        print(f"Es europeo y de {ciudad}")
else:
    print(f"{nombre} NO es mayor de edad")

#Ejemplo 4
print("\n##################### EJEMPLO 4 #########################")

dia = int(input("introduce el numero del dia de la semana:"))
"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
      print("Es martes")
    else:
        if dia == 3:
          print("Es miercoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es Viernes")
                else:
                    print("es fin de semana")
"""

# ELIF (Es una estructura de control que permite hacerlo mas sencillo y legible, reduciendo lineas de codigo)
if dia == 1:
    print("Hoy es lunes")
elif dia == 2:
    print("Hoy es martes")
elif dia == 3:
    print("Hoy es miercoles")
elif dia == 4:
    print("Hoy es jueves")
elif dia == 5:
    print("Hoy es viernes")
else:
    print("Es fin de semana")

#Ejemplo 5
print("\n##################### EJEMPLO 5 #########################")

edad_minima = 18
edad_maxima = 65
edad_real = int(input("¿Tienes edad para trabajar? Introduzca su edad:"))

if edad_real >= 18 and edad_real <=  65:
    print("Está en edad de trabajar")
else:
    print("No está en edad de trabajar")

#Ejemplo 6
print("\n##################### EJEMPLO 6 #########################")

pais = input("Introduzca el pais:")

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")