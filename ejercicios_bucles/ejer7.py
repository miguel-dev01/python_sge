numero = None
result = 0.0

while numero != 0:
    numero = float(input("Introduce un numero (0 para salir): "))

    if numero > result:
        result = numero

print("Mayor: ", result)
