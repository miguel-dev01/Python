"""
EJERCICIO 5.
Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario
"""

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 < numero2:
    for contador in range(numero1, numero2):
        print(contador)

else:
    print("Estos numeros no se pueden dividir porque el numero1 tiene que ser menor al numero2")