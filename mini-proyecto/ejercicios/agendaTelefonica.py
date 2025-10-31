'''Descripción:
Crea una función agregar_contacto(diccionario) que permita agregar nombres y números de teléfono a una agenda (diccionario).

Requisitos:

Cada nombre es una clave y el número telefónico es el valor.'''


def agregar_contacto(diccionario):
    while True:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")

        diccionario[nombre] = telefono

        print(f"Contacto '{nombre}' agregado correctamente.")
        validar = input("¿Desea seguir o finalizar? Escriba 'fin' para salir, o presione '1' para continuar: ")
        if validar.lower() == "fin":
            break
    return diccionario

agenda = {}
print("Agenda final:", agregar_contacto(agenda))