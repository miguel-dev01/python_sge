# Hacer con listas y con diccionarios

cadena = input("Introduce una frase: ")
cadena = cadena.lower()

# Con lista
# resultado = [0, 0, 0, 0, 0]

resultado = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for letra in cadena:
    if letra == "a":
        resultado["a"] += 1
    elif letra == "e":
        resultado["e"] += 1
    elif letra == "i":
        resultado["i"] += 1
    elif letra == "o":
        resultado["o"] += 1
    elif letra == "u":
        resultado["u"] += 1

print(resultado)