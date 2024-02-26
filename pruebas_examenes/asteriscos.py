# Figura 1: Triángulo
def dibujar_triangulo(filas):
    for i in range(1, filas + 1):
        print('* ' * i)

# Figura 2: Cuadrado
def dibujar_cuadrado(lado):
    for i in range(lado):
        print('* ' * lado)

# Figura 3: Pirámide invertida
def dibujar_piramide_invertida(filas):
    for i in range(filas, 0, -1):
        print('  ' * (filas - i) + '* ' * i)

# Figura 4: Rombo
def dibujar_rombo(filas):
    for i in range(1, filas + 1):
        print(' ' * (filas - i) + '* ' * i)
    for i in range(filas - 1, 0, -1):
        print(' ' * (filas - i) + '* ' * i)

if __name__ == "__main__":
    # Puedes ajustar los parámetros según tus preferencias
    dibujar_triangulo(5)

    print("\n")

    dibujar_cuadrado(4)

    print("\n")

    dibujar_piramide_invertida(4)

    print("\n")

    dibujar_rombo(4)
