"""
- Para ver muchos de los módulos, en la página oficial de Python, escribir: **Python Module Index**

Son funcionalidades ya hechas para reutilizar código. Se les denominan también librerías.

Podemos conseguir modulos creados por la comunidad, incluso nosotros crearnos nuestro propio módulo.
"""

# Importar el modulo. Se debe llamar igual que el archivo donde se encuentran las funciones
from random import random
import modulo

print(modulo.holaMundo("Miguel"))
print(modulo.calculadora(2,2))

# Importar una función concreta del módulo
from modulo import holaMundo
print(holaMundo("Miguel"))

# Llamar a la funcion normal sin objeto delante
from modulo import *

# Modulo de fechas
import datetime
print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y")
print("Mi fecha personalizada es: " ,fecha_personalizada)

# Módulo de matemáticas
import math

print("Raiz cuadrada de 10:", math.sqrt(10))

print("Número pi: ", float(math.pi))

print("Redondear: ", math.ceil(6.56525625))

# Módulo random (números aleatorios)
import random

print("Número aleatorio entre 15 y 67: ", random.randint(15, 67))