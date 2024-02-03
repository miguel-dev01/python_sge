matriz = [[2, 5, 3, 4, 5],
          [2, 6, 8, 4, 5],
          [9, 8, 3, 5, 2],
          [5, 3, 8, 5, 6],
          [0, 1, 4, 3, 4]]
total_filas = list()
total_columnas = [0] * len(matriz)

# En un solo bucle
for fila in matriz:
    suma_fila = 0
    for columna, element in enumerate(fila):
        suma_fila += element
        total_columnas[columna] += element
    total_filas.append(suma_fila)

# Con dos bucles separados
# for fila in matriz:
#     suma = 0
#     for j in fila:
#         suma += j
#     total_filas.append(suma)
#
# for fila in matriz:
#     for columna, elemento in enumerate(fila):
#         total_columnas[columna] += elemento

print("Total filas: ")
for i in total_filas:
    print(i, end=" ")

print("\n\nTotal columnas: ")
for i in total_columnas:
    print(i, end=" ")