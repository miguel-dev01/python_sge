numero = int(input("Introduce un numero: "))
multiplos = ""

for i in range(1, numero):
    if i % 11 == 0:
        if multiplos:
            multiplos += ", "
        multiplos += str(i)

print(f"Los multiplos de {numero} son: {multiplos}")
