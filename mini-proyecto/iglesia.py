import json
from servidor import (Servidor)
#from datetime import datetime



# ======== CLASE IGLESIA =========
class Iglesia:
    def __init__(self):
        self.servidores = []
        self.asignaciones = []
        self.cargar_datos()

    # ---------- REGISTRAR SERVIDOR ----------
    def registrar_servidor(self):
        print("\n--- Registrar nuevo servidor ---")
        nombre = input("Nombre: ").strip()
        edad = input("Edad: ").strip()
        area = input("Área de servicio (Seguridad, Comunicaciones, Consolidación, Ujieres, Alabanza, Kids, Intercesión): ").capitalize()
        disponibilidad = input("Disponibilidad (Ej: domingos, miércoles): ").strip()

        nuevo = Servidor(nombre, edad, area, disponibilidad)
        self.servidores.append(nuevo)
        print(f"\n✅ Servidor {nombre} agregado correctamente.")
        self.guardar_datos()

    # ---------- LISTAR SERVIDORES ----------
    def listar_servidores(self):
        print("\n--- Lista de servidores registrados ---")
        if not self.servidores:
            print("No hay servidores registrados.")
            return

        area = input("¿Deseas filtrar por área? (Sí/No): ").lower()
        if area == "sí" or area == "si":
            filtro = input("Ingresa el área: ").capitalize()
            filtrados = [s for s in self.servidores if s.area == filtro]
            if not filtrados:
                print(f"No hay servidores registrados en el área de {filtro}.")
                return
            for s in filtrados:
                print(f"- {s.nombre} ({s.edad} años) - {s.area} - Disponibilidad: {s.disponibilidad}")
        else:
            for s in self.servidores:
                print(f"- {s.nombre} ({s.edad} años) - {s.area} - Disponibilidad: {s.disponibilidad}")

    # ---------- ASIGNAR SERVIDORES ----------
    def asignar_servidores(self):
        print("\n--- Asignar servidores a una fecha ---")
        area = input("Área a asignar: ").capitalize()
        fecha = input("Fecha (DD/MM/AAAA): ")

        disponibles = [s for s in self.servidores if s.area == area]
        if not disponibles:
            print(f"No hay servidores en el área de {area}.")
            return

        print(f"\nServidores disponibles en {area}:")
        for i, s in enumerate(disponibles):
            print(f"{i + 1}. {s.nombre} ({s.disponibilidad})")

        seleccion = input("Ingresa los números de los servidores separados por coma (Ej: 1,3,4): ")
        indices = [int(i.strip()) - 1 for i in seleccion.split(",") if i.strip().isdigit()]
        elegidos = [disponibles[i].nombre for i in indices if 0 <= i < len(disponibles)]

        if not elegidos:
            print("No se seleccionaron servidores válidos.")
            return

        asignacion = {
            "fecha": fecha,
            "area": area,
            "servidores": elegidos
        }
        self.asignaciones.append(asignacion)
        print(f"\n✅ Servidores asignados correctamente al área {area} para el {fecha}.")
        self.guardar_datos()

    # ---------- VER ASIGNACIONES ---------------
    def ver_asignaciones(self):
        print("\n--- Asignaciones registradas ---")
        if not self.asignaciones:
            print("No hay asignaciones guardadas.")
            return

        for a in self.asignaciones:
            print(f"\n📅 {a['fecha']} - Área: {a['area']}")
            for s in a['servidores']:
                print(f"   - {s}")

    # ---------- GUARDAR Y CARGAR DATOS ----------
    def guardar_datos(self):
        """Guarda los datos en un archivo JSON."""
        data = {
            "servidores": [s.to_dict() for s in self.servidores],
            "asignaciones": self.asignaciones
        }
        with open("iglesia_datos.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        """Carga los datos del archivo JSON si existe."""
        try:
            with open("iglesia_datos.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.servidores = [Servidor(**s) for s in data.get("servidores", [])]
                self.asignaciones = data.get("asignaciones", [])
        except FileNotFoundError:
            pass

