# Realizado por Miguel Sanchez
from random import randint

def generarCiudad(filas, columnas):
    matriz = []
    for i in range(filas):
        actual = []
        for j in range(columnas):
            actual.append("sano")
        matriz.append(actual)
    aleatorio_fila = randint(0, filas - 1)
    aleatorio_column = randint(0, columnas - 1)
    matriz[aleatorio_fila][aleatorio_column] = "I-0" + "\t"

    return matriz

def mostrarCiudad(matriz, dia):
    print()
    print("Dia:", dia, "\n")
    for fila in matriz:
        for j in fila:
            print(j, end="\t")
        print()

def contagiar(matriz):
    filas = len(matriz)
    dia_actual = 0
    global total_elem
    while total_elem > 0:
        for i in range(filas):
            # si filas tiene valor entonces ... sino 0
            columnas = len(matriz[i]) if filas > 0 else 0
            for j in range(columnas):
                # derecha
                if j < columnas - 1 and matriz[i][j + 1] == "sano":
                    matriz[i][j + 1] = "I-" + str(dia_actual) + "\t"
                    total_elem -= 1
                # izqui
                if j > 0 and matriz[i][j - 1] == "sano":
                    matriz[i][j - 1] = "I-" + str(dia_actual) + "\t"
                    total_elem -= 1
                # arriba
                if i > 0 and matriz[i - 1][j] == "sano":
                    matriz[i - 1][j] = "I-" + str(dia_actual) + "\t"
                    total_elem -= 1
                # abajo
                if i < filas - 1 and matriz[i + 1][j] == "sano":
                    matriz[i + 1][j] = "I-" + str(dia_actual) + "\t"
                    total_elem -= 1
            dia_actual += 1
            mostrarCiudad(matriz, dia_actual)


try:
    filas = int(input("Introduce numero de filas: "))
    columnas = int(input("Introduce numero de columnas: "))

    total_elem = filas * columnas - 1
    matrizCiudad = generarCiudad(filas, columnas)
    contagiar(matrizCiudad)
except ValueError:
    print("Solo se pueden introducir numeros. Intentalo de nuevo")