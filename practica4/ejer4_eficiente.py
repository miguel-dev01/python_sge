print("Introduce nombres. ENTER para terminar:")
nombres = []
escribir = input("Escribe nombre: ")

while escribir != "ENTER":
    nombres.append(escribir)
    escribir = input("Escribe nombre: ")

print("Se han introducido los siguientes nombres:")
nombres.sort()
for nombre in nombres:
    print(nombre)
