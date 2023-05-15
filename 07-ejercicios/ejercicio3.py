"""
EJERCICIO 3
- Hacer programa que muestre los cuadrados (un numero multiplciado por si mismo) de 
los 60 primeros numeros naturales. Resolver con FOR y con WHILE
"""

# BUCLE WHILE
contador = 0

while contador <= 60:
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")
    contador += 1



# BUCLE FOR
contador = 0

for contador in range(0,61):
    cuadrado = contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")
