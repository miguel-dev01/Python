"""
EJERCICIO 7
- Hacer un programa que muestre todos los numeros impares entre dos numeros que indique el usuario.
"""

numero1 = int(input("Indique el primer número: "))
numero2 = int(input("Indique el último número: "))

if numero1 < numero2:

    for contador in range(numero1, (numero2 + 1)):
        if contador%2 == 0: 
            print(f"{contador} es PAR")
        else:
            print(f"{contador} es IMPAR")
else:
    print("ESTA COMBINACION ES INCORRECTA")
