"""
 Bucle WHILE
 Es una estructura de control que itera o repite la ejecución de una serie de instrucciones 
 tantas veces como sea necesario hasta que deje de cumplirse la condicion.

While condicion:
    bloque de instrucciones
    actualizacion de contador

"""
contador = 1

while contador <= 100:
    print(f"Estoy en el número: {contador}")
    contador += 1

print("------------------------------")
contador = 1
muestrame = str(0)
while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)

# Ejemplo

print("######## EJEMPLO #########")
numero_usuario = int(input("¿De que numero quieres la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla de multiplicar {numero_usuario}")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador}")
    contador += 1
else:
    print("TABLA FINALIZADA CON BUCLE WHILE")