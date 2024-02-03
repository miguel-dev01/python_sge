# Devolvera una tupla, con dos listas dentro -> matriz_recorte y matriz_sobrante
def recortes(matriz):
    recorte = int()
    n_filas = len(matriz)
    longitud_columnas = float('inf')
    for fila in matriz:
        n_columnas = len(fila)
        if n_columnas < longitud_columnas:
            longitud_columnas = n_columnas

    if n_filas < longitud_columnas:
        recorte = n_filas
    else:
        recorte = longitud_columnas

    matriz_recorte = []
    matriz_sobrante = []
    for fila in matriz[:recorte]:
        matriz_ = []
        for columna in fila[:recorte]:
            matriz_.append(columna)
            if columna in fila:
                fila.remove(columna)
        matriz_recorte.append(matriz_)

    matriz_sobrante = [fila for fila in matriz if fila]
    return tuple([matriz_recorte]) + tuple([matriz_sobrante])