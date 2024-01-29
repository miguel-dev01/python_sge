numero = int(input("Introduzca un numero: "))
primos = []

for i in range(2, numero + 1):
    es_primo = True
    for j in range(2, i):
        if i % j == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(i)


print(f"Numeros primos [2-{numero}]:", primos)
