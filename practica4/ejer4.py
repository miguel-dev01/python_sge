print("Introduce nombres. ENTER para terminar:")
nombres = {}
escribir = ""
i = 1

while escribir != "ENTER":
    try:
        escribir = input("Escribe nombre: ")
        if escribir != "ENTER":
            nombres["persona " + str(i)] = escribir
            i += 1
            continue
        print("PULSAMOS --ENTER--")
    except ValueError:
        print("Error: Introduce un nombre válido.")

print("Se han introducido los siguientes nombres:")
sorted_names = sorted(nombres.items(), key=lambda x: x[1])
for nombre in sorted_names:
    print(nombre[1])