def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"


def calculadora(numero1, numero2):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    cadena += "Suma es: " + str(suma)
    cadena += "Resta es: " + str(resta)
    cadena += "Multiplicación es: " + str(multi)
    cadena += "Division es: " + str(division)

    return cadena

print(calculadora(1, 1))
