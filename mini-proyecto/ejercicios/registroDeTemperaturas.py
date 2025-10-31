'''Descripción:
--Crea una función llamada registrar_temperaturas() que pida al usuario ingresar 
temperaturas diarias (en °C) y las almacene en una lista.
--El ingreso termina cuando el usuario escriba "fin".
Requisitos:
Al final, muestra:
La lista completa de temperaturas.
El promedio de las temperaturas.'''

almacen = [] 

def temperaturas():
    
    while True:
        tem = float(input("Ingresa la temperatura diaria en °C: "))
        almacen.append(tem)  
        validar = input("¿Desea seguir o finalizar? Escriba 'fin' para salir, o presione '1' para continuar: ")
        if validar.lower() == "fin":
            break

    return almacen  


print("Temperaturas registradas:", temperaturas())

if len(almacen) > 0:
    prom = 0
    for valor in almacen:
        prom += valor

    promedio = prom / len(almacen)
    print(f"El promedio de temperaturas es: {promedio:.2f} °C")
else:
    print("No se ingresaron temperaturas.")


