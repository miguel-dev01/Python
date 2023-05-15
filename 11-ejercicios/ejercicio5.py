"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:
Videojuegos de -->
ACCION      AVENTURA            DEPORTES
GTA         ASSASSINS           FIFA
COD         CRASH               PRO
PUGB        PRINCE OF PERSIA    MOTOGP

Mostrar esta información ordenada en un diccionario.
"""
"""
diccionario = [
    {
        'Nombre categoria': 'Accion',
        'nombre videojuego': 'GTA',
        'nombre videojuego': 'COD',
        'nombre videojuego': 'PUGB',
    },
    {
        'Nombre categoria': 'Accion',
        'nombre videojuego': 'Assassins',
        'nombre videojuego': 'Crash',
        'nombre videojuego': 'Prince of persia',
    },
    {
        'Nombre categoria': 'Deportes',
        'nombre videojuego': 'FIFA',
        'nombre videojuego': 'MotoGP',
        'nombre videojuego': 'PRO',
    }
]
"""

# Solucion
tabla = [
    {
        "categoria":"accion",
        "juegos": ["gta","cod","pugb"]
    },
    {
        "categoria":"aventuras",
        "juegos": ["prince of persia","assassins","crash"]
    },
    {
        "categoria":"deportes",
        "juegos": ["fifa","pro","motogp"]
    }
]

for categoria in tabla:
    print(f"-----------{categoria['categoria']}-----------")
    print(f"Nombre del videojuego {categoria['juegos']}")

for categoria in tabla:
    print(f"-----------{categoria['categoria']}-----------")
    for juego in categoria['juegos']:
        print(juego)