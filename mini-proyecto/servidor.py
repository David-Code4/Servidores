import json
#from datetime import datetime

# ======== CLASE SERVIDOR =========
class Servidor:
    def __init__(self, nombre, edad, area, disponibilidad):
        self.nombre = nombre
        self.edad = edad
        self.area = area
        self.disponibilidad = disponibilidad

    def to_dict(self):
        """Convierte el objeto a un diccionario para guardarlo."""
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "area": self.area,
            "disponibilidad": self.disponibilidad
        }