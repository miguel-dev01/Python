from io import open
import pathlib
import shutil


# Abrir archivos
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)

archivo = open(ruta, "a+")

# Escribir
archivo.write("****** VIVA LA INTELIGENCIA ARTIFICIAL ******")

# Cerrar archivo
archivo.close()

# Abrir archivos 2
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
contenido = archivo_lectura.read()
print(contenido)

# Leer contenido y guardar en línea
lista = archivo_lectura.readlines()
archivo_lectura.close()

print(lista)

for frase in lista:
    lista_frase = frase.split()
    print("- " + frase.upper())


# Copiar
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_alternativa = "../07"
shutil.copyfile(ruta_original, ruta_nueva)

# Mover archivos
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"

shutil.move(ruta_original, ruta_nueva)

# Eliminar archivos
import os

ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
os.remove(ruta_nueva)

# Comprobar si existe
import os.path
print(os.path.abspath("./"))


# print(os.path.abspath("../"))

ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
ruta_comprobar = "./fichero_texto.txt"


if os.path.isfile(ruta_comprobar):
    print("El archivo no existe")
else:
    print("El archivo no existe")