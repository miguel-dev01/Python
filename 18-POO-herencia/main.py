import clases

persona = clases.Persona()
persona.setNombre("Michael")
persona.setApellidos("Sanchez Garcia")
persona.setEdad("19 años")
persona.setProfesion("Ingeniero eléctrico")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

"""
humano = persona()

print(humano.getNombre(), humano.getApellidos)
"""

informatico = clases.Informatico()
informatico.setNombre("Carlos")
informatico.setApellidos("Martinez")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()} y sabe {informatico.getLenguajes()}")

print(informatico.caminar())
print(informatico.experiencia)

tecnico = clases.TecnicoRedes()
# El constructor es exclusivo de cada clase, no se hereda
# Por tanto, lenguajes solo lo sabe informatico porque esta en dicha clase, no en la clase de tecnico
print(tecnico.auditarRedes, tecnico.getLenguajes())


# Para acceder a los elementos y funciones de la clase padre debemos hacer **super().__init__()**