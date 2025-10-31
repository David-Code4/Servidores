from iglesia import (Iglesia)
from servidor import (Servidor)


# ======== FUNCIONES DEL MENÚ PRINCIPAL =========
def menu():
    iglesia = Iglesia()
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Registrar nuevo servidor")
        print("2. Listar servidores")
        print("3. Asignar servidores a fecha")
        print("4. Ver asignaciones")
        print("5. salir")
        


        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            cont +=1
            iglesia.registrar_servidor()
        elif opcion == "2":
            iglesia.listar_servidores()
        elif opcion == "3":
            iglesia.asignar_servidores()
        elif opcion == "4":
            iglesia.ver_asignaciones()
        elif opcion == "5":
            print("\n👋 Saliendo del programa... ¡Dios te bendiga!")
            break
        else:
        
            print("Opción no válida. Intente de nuevo.")

# ======== EJECUCIÓN PRINCIPAL =========
if __name__ == "__main__":
    menu()
