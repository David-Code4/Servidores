'''Descripción:
Crea una función calcular_promedios() que pida ingresar varias materias y las notas de cada una.

Requisitos:

Guarda los datos en un diccionario con formato:
{ "Matemáticas": [4.0, 3.5, 5.0], "Historia": [3.0, 4.5] }

Calcula el promedio de cada materia.

Maneja excepciones si el usuario ingresa una nota inválida.'''

notas= []
def calcular_promedios(dic):
    i=0
    while True:
        materia = input("ingresa la materia ")
        cant = input("cantidad de notas por esta materia")
        for i in range (cant):
            nota = input (f"ingresa el {i} valor de esta materia, solo se admite este formato 0.0 ")
            if nota > 5.0 or nota < 1.0:
                print("error")
            else:
                notas[i] = nota
            
        dic[materia] = notas
        