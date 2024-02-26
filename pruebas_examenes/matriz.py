# # NOMBRE: JESUS CANOVAS FERNANDEZ


# #Ejercicio 1: Transposición de Matriz
# def transponer_matriz(matriz):
#     return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
# matriz_original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matriz_transpuesta = transponer_matriz(matriz_original)
# print(matriz_transpuesta)


# Ejercicio 2: Producto de Matrices
def multiplicar_matrices(matriz1, matriz2):
    result = [[sum(a * b for a, b in zip(matriz1_fila, matriz2_columna)) for matriz2_columna in zip(*matriz2)] for
              matriz1_fila in matriz1]
    return result


matriz_a = [[1, 2, 3], [4, 5, 6]]
matriz_b = [[7, 8], [9, 10], [11, 12]]
matriz_resultado = multiplicar_matrices(matriz_a, matriz_b)
print(matriz_resultado)


# #Ejercicio 3: Rotación de Matriz
# def rotar_matriz(matriz):
#     return [list(reversed(col)) for col in zip(*matriz)]
# matriz_original = [[1, 2, 3],
#                    [4, 5, 6],
#                    [7, 8, 9]]
# matriz_rotada = rotar_matriz(matriz_original)
# print(matriz_rotada)


# #Ejercicio 4: Suma de Matrices
# def sumar_matrices(matriz1, matriz2):
#     return [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
# matriz_a = [[1, 2], [3, 4]]
# matriz_b = [[5, 6], [7, 8]]
# matriz_suma = sumar_matrices(matriz_a, matriz_b)
# print(matriz_suma)


# #Ejercicio 5: Suma de Filas, Columnas y Diagonales
# def suma_filas_columnas_diagonales(matriz):
#     n = len(matriz)
#     sumas = {'Filas': [sum(fila) for fila in matriz],
#              'Columnas': [sum(col) for col in zip(*matriz)],
#              'Diagonal Principal': [matriz[i][i] for i in range(n)],
#              'Diagonal Secundaria': [matriz[i][n-i-1] for i in range(n)]}
#     return sumas
# matriz_ejemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# resultados = suma_filas_columnas_diagonales(matriz_ejemplo)
# print(resultados)


# #Ejercicio 6: Verificar Matriz Identidad
# def es_matriz_identidad(matriz):
#     n = len(matriz)
#     return all(matriz[i][i] == 1 and all(matriz[i][j] == 0 for j in range(n) if j != i) for i in range(n))
# matriz_identidad = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# matriz_no_identidad = [[1, 0, 0], [0, 1, 0], [0, 1, 1]]
# print(es_matriz_identidad(matriz_identidad))  # True
# print(es_matriz_identidad(matriz_no_identidad))  # False


# #Ejercicio 7: Suma de Elementos por Columna
# def columna_maxima(matriz):
#     sumas_columnas = [sum(col) for col in zip(*matriz)]
#     maxima_columna = sumas_columnas.index(max(sumas_columnas))
#     return maxima_columna, sumas_columnas[maxima_columna]
# matriz_ejemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# columna_max, suma_maxima = columna_maxima(matriz_ejemplo)
# print(f"La columna con la mayor suma es {columna_max}, con suma total de {suma_maxima}")


# #Ejercicio 8: Zigzag en Matriz
# def imprimir_zigzag(matriz):
#     for i in range(len(matriz)):
#         if i % 2 == 0:
#             for j in range(len(matriz[i])):
#                 print(matriz[i][j], end=" ")
#         else:
#             for j in range(len(matriz[i]) - 1, -1, -1):
#                 print(matriz[i][j], end=" ")
# matriz_ejemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# imprimir_zigzag(matriz_ejemplo)


# #Ejercicio 9: Imprimir Elementos en Diagonal
# print()
# def imprimir_diagonal(matriz):
#     for k in range(len(matriz) + len(matriz[0]) - 1):
#         for i in range(len(matriz)):
#             for j in range(len(matriz[i])):
#                 if i + j == k:
#                     print(matriz[i][j], end=" ")
# matriz_ejemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# imprimir_diagonal(matriz_ejemplo)


# #Ejercicio 10: Recorrido en Espiral
# print()
# def imprimir_espiral(matriz):
#     m, n = len(matriz), len(matriz[0])
#     inicio_fila, inicio_col = 0, 0

#     while inicio_fila < m and inicio_col < n:
#         for i in range(inicio_col, n):
#             print(matriz[inicio_fila][i], end=" ")

#         inicio_fila += 1

#         for i in range(inicio_fila, m):
#             print(matriz[i][n - 1], end=" ")

#         n -= 1

#         if inicio_fila < m:
#             for i in range(n - 1, inicio_col - 1, -1):
#                 print(matriz[m - 1][i], end=" ")

#             m -= 1

#         if inicio_col < n:
#             for i in range(m - 1, inicio_fila - 1, -1):
#                 print(matriz[i][inicio_col], end=" ")

#             inicio_col += 1
# matriz_ejemplo = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# imprimir_espiral(matriz_ejemplo)


# #Ejercicio 11: Suma de Filas y Columnas
# print()
# def suma_filas_columnas(matriz):
#     filas = len(matriz)
#     columnas = len(matriz[0])

#     for i in range(filas):
#         suma_fila = sum(matriz[i])
#         print(f"Suma de la fila {i + 1}: {suma_fila}")

#     for j in range(columnas):
#         suma_columna = sum(matriz[i][j] for i in range(filas))
#         print(f"Suma de la columna {j + 1}: {suma_columna}")
# matriz_ejemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# suma_filas_columnas(matriz_ejemplo)


# #Ejercicio 13: Operaciones en Bloques
# def operaciones_en_bloques(matriz, bloques):
#     for bloque in bloques:
#         fila_inicio, fila_fin, col_inicio, col_fin = bloque

#         numeros_en_bloque = [matriz[i][j] for i in range(fila_inicio, fila_fin + 1) for j in range(col_inicio, col_fin + 1)]

#         if any(numero % 2 == 0 for numero in numeros_en_bloque):
#             for i in range(fila_inicio, fila_fin + 1):
#                 for j in range(col_inicio, col_fin + 1):
#                     matriz[i][j] += 1
#         else:
#             for i in range(fila_inicio, fila_fin + 1):
#                 for j in range(col_inicio, col_fin + 1):
#                     matriz[i][j] -= 1
# matriz_ejemplo = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# bloques_ejemplo = [(0, 1, 0, 1), (2, 3, 2, 3)]  # Bloques representados como (fila_inicio, fila_fin, col_inicio, col_fin)

# def MostrarMatriz(matriz):
#     for fila in range(len(matriz)):
#         for columna in range(len(matriz[fila])):
#             print(matriz[fila][columna], end="\t")
#         print()

# print("Matriz Original:")
# MostrarMatriz(matriz_ejemplo)
# print("\nBloques:")
# for bloque in bloques_ejemplo:
#     print(f"Fila: {bloque[0]}-{bloque[1]}, Columna: {bloque[2]}-{bloque[3]}")
# print("\nAplicando Operaciones en Bloques:")
# operaciones_en_bloques(matriz_ejemplo, bloques_ejemplo)
# MostrarMatriz(matriz_ejemplo)


# #Ejercicio 12: Relleno en Espiral
# print()
# def rellenar_espiral(matriz):
#     n = len(matriz)
#     valor = 1
#     fila_inicio, fila_fin, col_inicio, col_fin = 0, n - 1, 0, n - 1

#     while valor <= n * n:
#         for i in range(col_inicio, col_fin + 1):
#             matriz[fila_inicio][i] = valor
#             valor += 1
#         fila_inicio += 1

#         for i in range(fila_inicio, fila_fin + 1):
#             matriz[i][col_fin] = valor
#             valor += 1
#         col_fin -= 1

#         for i in range(col_fin, col_inicio - 1, -1):
#             matriz[fila_fin][i] = valor
#             valor += 1
#         fila_fin -= 1

#         for i in range(fila_fin, fila_inicio - 1, -1):
#             matriz[i][col_inicio] = valor
#             valor += 1
#         col_inicio += 1
# def visualizarmatriz(matriz):
#     for fila in matriz:
#         for elemento in fila:
#             print(elemento, end="\t")
#         print()

# matriz_ejemplo = [[0] * 5 for _ in range(5)]  # Matriz 5x5 inicializada con ceros
# rellenar_espiral(matriz_ejemplo)
# visualizarmatriz(matriz_ejemplo)


# print()  # Agregar una nueva línea después de cada fila


# def imprimir_matriz(matriz):
#     for fila in matriz:
#         for elemento in fila:
#             print(elemento, end="\t")
#         print()  # Agregar una nueva línea después de cada fila

# # Ejemplo de uso
# mi_matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# imprimir_matriz(mi_matriz)


# # Multiplicación de Matrices
# matriz1 = []
# matriz2 = []
# resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# # Ingresar valores para la primera matriz
# print("Ingrese los valores para la primera matriz:")
# for i in range(3):
#     fila = [int(input(f"Elemento {i+1}{j+1}: ")) for j in range(3)]
#     matriz1.append(fila)

# # Ingresar valores para la segunda matriz
# print("Ingrese los valores para la segunda matriz:")
# for i in range(3):
#     fila = [int(input(f"Elemento {i+1}{j+1}: ")) for j in range(3)]
#     matriz2.append(fila)

# # Calcular la multiplicación de matrices
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             resultado[i][j] += matriz1[i][k] * matriz2[k][j]

# # Mostrar la matriz resultante
# print("Matriz Resultante:")
# for fila in resultado:
#     print(fila)

# #Ejercicio 14: Contar Vocales en una Matriz
def contar_vocales(matriz):
    total_vocales = sum(fila.count(vocal) for fila in matriz for vocal in 'aeiouAEIOU')
    return total_vocales


matriz_texto = [
    ['H', 'o', 'l', 'a'],
    ['E', 's', 't', 'e'],
    ['e', 'j', 'e', 'm', 'p', 'l', 'o']
]

cantidad_vocales = contar_vocales(matriz_texto)
print(f"La matriz contiene {cantidad_vocales} vocales.")


# #Ejercicio 15: Buscar Palabra en una Matriz de Texto
def buscar_palabra(matriz, palabra):
    palabra_encontrada = any(palabra in ''.join(fila) for fila in matriz)
    return palabra_encontrada


matriz_texto = [
    ['H', 'o', 'l', 'a'],
    ['E', 's', 't', 'e'],
    ['e', 'j', 'e', 'm', 'p', 'l', 'o']
]

palabra_a_buscar = 'Hola'
resultado = buscar_palabra(matriz_texto, palabra_a_buscar)

if resultado:
    print(f"La palabra '{palabra_a_buscar}' se encuentra en la matriz.")
else:
    print(f"La palabra '{palabra_a_buscar}' no se encuentra en la matriz.")


# #Ejercicio 16: Copiar Matriz
def copiar_matriz(matriz):
    return [fila.copy() for fila in matriz]


matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_copia = copiar_matriz(matriz_original)
print("Matriz Original:")
print(matriz_original)
print("\nMatriz Copia:")
print(matriz_copia)


# #Ejercicio 17: Contar Números Pares e Impares en una Matriz
def contar_pares_impares(matriz):
    total_pares = sum(1 for fila in matriz for num in fila if num % 2 == 0)
    total_impares = sum(1 for fila in matriz for num in fila if num % 2 != 0)
    return total_pares, total_impares


matriz_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

pares, impares = contar_pares_impares(matriz_numeros)
print(f"La matriz tiene {pares} números pares y {impares} números impares.")


# #Ejercicio 18: Buscar Mínimo y Máximo en una Matriz
def encontrar_minimo_maximo(matriz):
    minimo = min(min(fila) for fila in matriz)
    maximo = max(max(fila) for fila in matriz)
    return minimo, maximo


matriz_numeros = [
    [3, 7, 2],
    [8, 1, 9],
    [4, 6, 5]
]

minimo, maximo = encontrar_minimo_maximo(matriz_numeros)
print(f"El valor mínimo en la matriz es {minimo} y el valor máximo es {maximo}.")


# #Ejercicio 19: Multiplicar Elementos Diagonales de una Matriz Cuadrada
def multiplicar_diagonales(matriz):
    diagonal_principal = 1
    diagonal_secundaria = 1
    n = len(matriz)

    for i in range(n):
        diagonal_principal *= matriz[i][i]
        diagonal_secundaria *= matriz[i][n - i - 1]

    return diagonal_principal, diagonal_secundaria


matriz_cuadrada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_principal, diagonal_secundaria = multiplicar_diagonales(matriz_cuadrada)
print(
    f"El producto de la diagonal principal es {diagonal_principal}, y el de la diagonal secundaria es {diagonal_secundaria}.")


# #Ejercicio 20: Validar Si una Matriz es Simétrica
def es_matriz_simetrica(matriz):
    return all(matriz[i][j] == matriz[j][i] for i in range(len(matriz)) for j in range(len(matriz[0])))


matriz_simetrica = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matriz_no_simetrica = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"¿La matriz es simétrica? {es_matriz_simetrica(matriz_simetrica)}")  # True
print(f"¿La matriz es simétrica? {es_matriz_simetrica(matriz_no_simetrica)}")  # False


# #Ejercicio 21: Obtener Promedio de Filas y Columnas
def promedio_filas_columnas(matriz):
    promedios_filas = [sum(fila) / len(fila) for fila in matriz]
    promedios_columnas = [sum(col) / len(col) for col in zip(*matriz)]
    return promedios_filas, promedios_columnas


matriz_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

promedios_filas, promedios_columnas = promedio_filas_columnas(matriz_numeros)
print(f"Promedios de filas: {promedios_filas}")
print(f"Promedios de columnas: {promedios_columnas}")


# #Ejercicio 22: Transposición de Matriz de Texto
def transponer_matriz_texto(matriz_texto):
    matriz_transpuesta = [''.join(col) for col in zip(*matriz_texto)]
    return matriz_transpuesta


matriz_texto_original = [
    ['H', 'o', 'l', 'a'],
    ['E', 's', 't', 'e'],
    ['e', 'j', 'e', 'm', 'p', 'l', 'o']
]

matriz_texto_transpuesta = transponer_matriz_texto(matriz_texto_original)
for fila in matriz_texto_transpuesta:
    print(fila)


# #Ejercicio 23: Encontrar Submatriz Cuadrada de Mayor Suma
def encontrar_submatriz_maxima(matriz):
    max_suma = float('-inf')
    max_submatriz = None

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            for k in range(i, len(matriz)):
                for l in range(j, len(matriz[0])):
                    suma_submatriz = sum(sum(fila[j:l + 1]) for fila in matriz[i:k + 1])
                    if suma_submatriz > max_suma:
                        max_suma = suma_submatriz
                        max_submatriz = (i, j, k, l)

    return max_suma, max_submatriz


matriz_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma_maxima, submatriz_maxima = encontrar_submatriz_maxima(matriz_numeros)
print(f"La suma máxima es {suma_maxima} y la submatriz cuadrada de mayor suma es {submatriz_maxima}")


# #Ejercicio 24: Desplazar Elementos en una Matriz
def desplazar_matriz(matriz, k):
    n = len(matriz)
    m = len(matriz[0])

    desplazada = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            nueva_fila = (i + k) % n
            desplazada[nueva_fila][j] = matriz[i][j]

    return desplazada


matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

k_desplazamiento = 1
matriz_desplazada = desplazar_matriz(matriz_original, k_desplazamiento)
print(f"Matriz Original:")
for fila in matriz_original:
    print(fila)
print(f"\nMatriz Desplazada (k={k_desplazamiento}):")
for fila in matriz_desplazada:
    print(fila)


# #Ejercicio 25: Encontrar Coordenadas de Elemento en Matriz
def encontrar_coordenadas(matriz, elemento):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == elemento:
                return i, j
    return None


matriz_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

elemento_a_buscar = 5
coordenadas = encontrar_coordenadas(matriz_numeros, elemento_a_buscar)
print(f"Las coordenadas del elemento {elemento_a_buscar} son: {coordenadas}")


# #Ejercicio 26: Eliminar Fila y Columna en una Matriz
def eliminar_fila_columna(matriz, fila, columna):
    nueva_matriz = [fila_matriz[:columna] + fila_matriz[columna + 1:] for fila_matriz in
                    (matriz[:fila] + matriz[fila + 1:])]
    return nueva_matriz


matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

fila_eliminar = 1
columna_eliminar = 2
matriz_modificada = eliminar_fila_columna(matriz_original, fila_eliminar, columna_eliminar)
print(f"Matriz Original:")
for fila in matriz_original:
    print(fila)
print(f"\nMatriz Modificada (eliminando fila {fila_eliminar} y columna {columna_eliminar}):")
for fila in matriz_modificada:
    print(fila)


# #Ejercicio 30: Sumar Todos los Elementos de una Matriz
def suma_matriz(matriz):
    return sum(sum(fila) for fila in matriz)


matriz_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

resultado_suma = suma_matriz(matriz_numeros)
print(f"La suma de todos los elementos de la matriz es: {resultado_suma}")


# #Ejercicio 31: Encontrar el Máximo en una Matriz
def encontrar_maximo(matriz):
    return max(max(fila) for fila in matriz)


matriz_numeros = [
    [1, 2, 3],
    [4, 9, 6],
    [7, 8, 5]
]

maximo_encontrado = encontrar_maximo(matriz_numeros)
print(f"El valor máximo en la matriz es: {maximo_encontrado}")


# #Ejercicio 32: Contar Elementos en una Matriz
def contar_elementos(matriz, elemento):
    return sum(fila.count(elemento) for fila in matriz)


matriz_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

elemento_a_contar = 5
cantidad_elementos = contar_elementos(matriz_numeros, elemento_a_contar)
print(f"El elemento {elemento_a_contar} aparece {cantidad_elementos} veces en la matriz.")


# #Ejercicio 33: Multiplicar Todos los Elementos de una Matriz por un Escalar
def multiplicar_matriz_por_escalar(matriz, escalar):
    return [[elemento * escalar for elemento in fila] for fila in matriz]


matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

escalar = 2
matriz_resultado = multiplicar_matriz_por_escalar(matriz_original, escalar)
print(f"Matriz Original:")
for fila in matriz_original:
    print(fila)
print(f"\nMatriz Resultado (multiplicada por {escalar}):")
for fila in matriz_resultado:
    print(fila)


# #Ejercicio 34: Pintar un Rombo
def pintar_rombo(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


altura_rombo = 5
print(f"Rombo de altura {altura_rombo}:\n")
pintar_rombo(altura_rombo)


# #Ejercicio 35: Pintar una Pirámide
def pintar_piramide(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))


altura_piramide = 4
print(f"Pirámide de altura {altura_piramide}:\n")
pintar_piramide(altura_piramide)


# #Ejercicio 36: Pintar un Triángulo
def pintar_triangulo(n):
    for i in range(n):
        print("*" * (i + 1))


altura_triangulo = 5
print(f"Triángulo de altura {altura_triangulo}:\n")
pintar_triangulo(altura_triangulo)


# #Ejercicio 37: Pintar una Escalera
def pintar_escalera(n):
    for i in range(n):
        print("*" * (i + 1))


escalones_escalera = 6
print(f"Escalera con {escalones_escalera} escalones:\n")
pintar_escalera(escalones_escalera)


# #Ejercicio 38: Pintar un Cuadrado
def pintar_cuadrado(n):
    for i in range(n):
        print("*" * n)


lado_cuadrado = 4
print(f"Cuadrado de lado {lado_cuadrado}:\n")
pintar_cuadrado(lado_cuadrado)


# #Ejercicio 39: Pintar un Triángulo Invertido
def pintar_triangulo_invertido(n):
    for i in range(n, 0, -1):
        print("*" * i)


altura_triangulo_invertido = 5
print(f"Triángulo invertido de altura {altura_triangulo_invertido}:\n")
pintar_triangulo_invertido(altura_triangulo_invertido)


# #Ejercicio 40: Pintar un Rombo con una Matriz Cuadrada
def pintar_rombo_matriz(n):
    matriz_rombo = [[' ' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        matriz_rombo[i][n // 2] = '*'
        matriz_rombo[n // 2][i] = '*'
        matriz_rombo[i][n - i - 1] = '*'
        matriz_rombo[n - i - 1][n // 2] = '*'

    for fila in matriz_rombo:
        print(''.join(fila))


tamano_rombo_matriz = 5
print(f"Rombo con matriz cuadrada de tamaño {tamano_rombo_matriz}:\n")
pintar_rombo_matriz(tamano_rombo_matriz)


# #Ejercicio 41: Pintar una Pirámide con una Matriz Cuadrada
def pintar_piramide_matriz(n):
    matriz_piramide = [[' ' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        matriz_piramide[i][n // 2 - i:n // 2 + i + 1] = '*' * (2 * i + 1)

    for fila in matriz_piramide:
        print(''.join(fila))


altura_piramide_matriz = 5
print(f"Pirámide con matriz cuadrada de altura {altura_piramide_matriz}:\n")
pintar_piramide_matriz(altura_piramide_matriz)


# #Ejercicio 42: Pintar un Triángulo con una Matriz Cuadrada
def pintar_triangulo_matriz(n):
    matriz_triangulo = [[' ' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        matriz_triangulo[i][:i + 1] = '*' * (i + 1)

    for fila in matriz_triangulo:
        print(''.join(fila))


altura_triangulo_matriz = 5
print(f"Triángulo con matriz cuadrada de altura {altura_triangulo_matriz}:\n")
pintar_triangulo_matriz(altura_triangulo_matriz)


# #Ejercicio 43: Pintar una Escalera con una Matriz Cuadrada
def pintar_escalera_matriz(n):
    matriz_escalera = [[' ' for _ in range(n)] for _ in range(n)]

    for i in range(n):
        matriz_escalera[i][:i + 1] = '*' * (i + 1)

    for fila in matriz_escalera:
        print(''.join(fila))


escalones_escalera_matriz = 6
print(f"Escalera con matriz cuadrada de {escalones_escalera_matriz} escalones:\n")
pintar_escalera_matriz(escalones_escalera_matriz)


# #Ejercicio 44: Pintar un Cuadrado con una Matriz Cuadrada
def pintar_cuadrado_matriz(n):
    matriz_cuadrado = [['*' for _ in range(n)] for _ in range(n)]

    for fila in matriz_cuadrado:
        print(''.join(fila))


lado_cuadrado_matriz = 4
print(f"Cuadrado con matriz cuadrada de lado {lado_cuadrado_matriz}:\n")
pintar_cuadrado_matriz(lado_cuadrado_matriz)


# #Ejercicio 45: Pintar un Triángulo Invertido con una Matriz Cuadrada
def pintar_triangulo_invertido_matriz(n):
    matriz_triangulo_invertido = [[' ' for _ in range(n)] for _ in range(n)]

    for i in range(n, 0, -1):
        matriz_triangulo_invertido[n - i][:i] = '*' * i

    for fila in matriz_triangulo_invertido:
        print(''.join(fila))


altura_triangulo_invertido_matriz = 5
print(f"Triángulo invertido con matriz cuadrada de altura {altura_triangulo_invertido_matriz}:\n")
pintar_triangulo_invertido_matriz(altura_triangulo_invertido_matriz)
