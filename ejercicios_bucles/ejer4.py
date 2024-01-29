numero = int(input("Introduce un numero: "))
suma = 0

# for i in range(0, int(numero)):
#     if i % 2 == 0:
#         suma += i

print("La suma es:", sum(i for i in range(0, numero + 1, 2)))
