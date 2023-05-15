class Coche:

    color = "Negro"
    marca = "Opel"
    modelo = "Vectra C GTS"
    velocidad = 220
    caballaje = 180
    plazas = 5
    año = 2002

    soy_publico = "Hola, soy un atributo público"
    __soy_privado = "Hola, soy un atributo privado"

    def getPrivado(self):
        return self.__soy_privado


    def __init__(self, color, marca, modelo, caballaje, velocidad, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas


    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setAño(self, año):
        self.año = año

    def getAño(self):
        return self.año

    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad

    def getInfo(self):
        info = "------ Información del coche ------"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Con una velocidad máxima de: " + str(self.getVelocidad()) + " km/h"

        return info