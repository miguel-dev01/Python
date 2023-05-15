"""
EJERCICIO 6
- Mostrar todas las tablas de multiplicar del 1 al 10. Mostrando el titulo de la tabla y
luego las multiplicaciones.
"""
# EJERCICIO HECHO POR MI
"""
tabla = 1
contador = 4

print(f"######## TABLA DEL {contador} ##########")

if tabla <= 1:
    for contador in range (0,11):
    print(f"{tabla} x {contador} = {tabla*contador}")

else:
    print("tabla finalizada")
"""

# PRUEBA 2, REALIZADA POR MI
"""
for nombre in range (1, 11):
    print(f"TABLA DEL {nombre}")
    print("################")

    for numero in range (0, 16):
         print(f"{nombre} x {numero} = {nombre*numero}")
"""

# PRUEBA 3, UN EJERCICIO QUE HAGO POR MI CUENTA, RELACIONADO TAMBIEN CON ESTE EJERCICIO
    #MOSTRAR TABLA DE MULTIPLICAR SEGUN EL USUARIO

numero_usuario = int(input("Indique la tabla de multiplicar que desea consultar: "))


for numero_tabla in range(0, 11):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")

print("TABLA FINALIZADA")
