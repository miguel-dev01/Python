"""
Un diccionario almacena un conjuntos de datos, 
pero en vez de tener index o indices numericos, como en las listas, va a tener indices alfanumericos.
En formato clave , valor.
Es parecido a un array asociativo o un objeto json.
"""

ejemplo = {
    #CLAVE : VALOR
    "nombre":"Miguel",
    "apellidos":"Sanchez Garcia",
    "python":"AprendePython"
}

print(ejemplo)

# Si quiero acceder a un solo indice
print(ejemplo["apellidos"])


# Diccionarios dentro de listas

contactos = [
    {
        'nombre':'Maria',
        'E-mail':'maria@python.com'
    },
    {
        'nombre':'Luis',
        'E-mail':'luis@python.com'
    },
    {
        'nombre':'Miguel',
        'E-mail':'miguel@python.com'
    }

]

print(contactos)

# Acceder a un indice concreto de diccionario dentro de lista
# tendremos que indicar:  numero del diccionario + clave, posteriormente te devolverá su valor
print(contactos[2]['E-mail'])


# Tambien se puede modificar su valor.
contactos[2]['E-mail'] = "michael@python.com"
print(contactos[2]['E-mail'])


for contacto in contactos:
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"E-mail del contanto: {contacto['E-mail']}")
    print("-------")