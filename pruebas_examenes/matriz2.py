# Realizado por Miguel Sanchez
from random import randint

aleatorio_fila = int()
aleatorio_column = int()

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

def contagiar(matriz):
    filas = len(matriz)
    dia_actual = 0
    i = aleatorio_fila
    while i < filas:
        columnas = len(matriz[i])
        j = 0
        while j < columnas:
            # derecha
            if j < columnas - 1 and matriz[i][j + 1] == 'sano':
                matriz[i][j + 1] = "I-" + str(dia_actual) + "\t"
            # izquierda
            if j > 0 and matriz[i][j - 1] == 'sano':
                matriz[i][j - 1] = "I-" + str(dia_actual) + "\t"
            # arriba
            if i > 0 and matriz[i - 1][j] == 'sano':
                matriz[i - 1][j] = "I-" + str(dia_actual) + "\t"
            # abajo
            if i < filas - 1 and matriz[i + 1][j] == 'sano':
                matriz[i + 1][j] = "I-" + str(dia_actual) + "\t"
            j += 1
        i += 1
        dia_actual += 1
        mostrarCiudad(matriz, dia_actual)

def mostrarCiudad(matriz, dia):
    print()
    print("Dia:", dia, "\n")
    for fila in matriz:
        for j in fila:
            print(j, end='\t')
        print()

# def main():
try:
    filas = int(input("Introduce numero de filas: "))
    columnas = int(input("Introduce numero de columnas: "))

    total_elementos = filas * columnas
    matrizCiudad = generarCiudad(filas, columnas)
    contagiar(matrizCiudad)
except ValueError:
    print("Solo se pueden introducir numeros. Intentalo de nuevo")
    # main()

# main()