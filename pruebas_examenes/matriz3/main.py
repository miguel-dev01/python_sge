from recorte import recortes

matriz = [[1, 2, 3], [4, 5], [6, 7], [8, 9, 10]]
# matriz = [[1, 2, 3], [4, 5, 6], [8, 9, 10]]
# matriz = [[1, 2, 3], [4, 5], [6], [8], [9, 10]]

def mostrarMatriz(matriz_arreglada):
    for fila in matriz_arreglada:
        for columna in fila:
            for subcolumna in columna:
                print(subcolumna, end="\t")


matrices_tupla = recortes(matriz)
mostrarMatriz(matrices_tupla)