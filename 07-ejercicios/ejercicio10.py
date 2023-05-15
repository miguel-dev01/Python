"""
Ejercicio 10
-  Un programa que pida la nota de 15 alumnos y extraer por 
pantalla cuantos han aprobado y cuantos han suspendido.
"""

"""
# bucle WHILE
contador = 0 
aprobados = 0
suspensos = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input("¿Que nota quieres ponerle al alumno?: "))

    if nota >= 5:
        aprobados += 1

    else:
        suspensos += 1

    contador += 1

print(f"Alumnos aprobados {aprobados}")
print(f"Alumnos suspensos {suspensos}")
"""

# bucle FOR

contador = 0
aprobados = 0
suspensos = 0

numeroalumno = 15

for numeroalumno in range(0, 15):
    nota = int(input(f"Que nota quieres darle al alumno: "))

    if nota >= 5:
        aprobados += 1

    else:
        suspensos += 1

    contador += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspensos: {suspensos}")