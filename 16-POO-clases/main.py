# Programacion orientada a objetos (POO o OOP)
# Lo primero que tendriamos seria el molde, que vendria a ser las clases, esto nos permitirá asignarle -
# atributos a nuestro objeto... 

# Definir una clase (molde para crear más objetos de ese tipo)
# Coche con caracteristicas similares


class Coche:
    # Lo siguientes son Atributos (En programación en general, se le conoce como variables)
    color = "Negro"
    marca = "Opel"
    modelo = "Vectra C GTS"
    velocidad = 220
    caballaje = 180
    plazas = 5
    año = 2002

    # Ahora vendrían los métodos, son acciones que realiza el objeto (coche). Son funciones.
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

# fin definición clase

# Ahora debemos crear el objeto / Instanciar la clase
print("---------- COCHE 1 ----------")
coche = Coche()


coche.setMarca("Opel")
coche.setModelo("Vectra C GTS")
coche.setColor("negro")
print(coche.getMarca(), coche.getModelo(), coche.getColor(), coche.año)


coche.setColor("amarillo")
coche.setModelo("El Coche Fantástico")
print(coche.getMarca(), coche.getModelo(), coche.getColor())

print("Velocidad actual: ", coche.getVelocidad())

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.frenar()

print("Velocidad actual: ", coche.getVelocidad())

print("\n---------- COCHE 2 ----------")
# Crear más objetos
coche2 = Coche()

print(coche2.getColor())

coche2.setModelo("Micra")
coche2.setColor("Negro")
coche2.setMarca("Nissan")
coche2.setAño("2010")

print(coche2.getMarca(), coche2.getModelo(), coche2.getColor(), coche2.getAño())

print(type(coche2))