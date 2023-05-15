# La herencia es la posibilidad de compartir atributos y métodos entre clases. Y que difirentes
# clases hereden de otras.

# Clase padre o molde
class Persona:
    """
    nombre = "Miguel"
    apellidos = "Sanchez Garcia"
    edad = 20
    profesion = "Informatico / Administrador de sistemas / Programador"
    """

    def getNombre(self):
        return self.nombre

    def getApellidos(self):
        return self.apellidos

    def getEdad(self):
        return self.edad

    def getProfesion(self):
        return self.profesion

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def setEdad(self, edad):
        self.edad = edad

    def setProfesion(self, profesion):
        self.profesion = profesion

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"
    
    def dormir(self):
        return "Estoy sobando"

# Aunque clase informatico es una diferente, un informático no deja de ser una persona.
# Por tanto, se hereda de la siguiente manera:
class Informatico(Persona):
    """
    lenguajes = ""
    experiencia =
    """

    def __init__(self):
        self.lenguajes = "HTML, CSS, PHP, JavaScript y Python"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def repararPC(self):
        return "He reparado tu ordenador"

class TecnicoRedes(Informatico):
    
    def __init__(self):
        super().__init__()
        self.auditarRedes = "experto"
        self.experiencia = 15

    def auditoria(self):
        return "Estoy diseñando y auditando una red local (LAN)"
