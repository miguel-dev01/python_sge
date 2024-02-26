def modifica(a, b):
    for elemento in b:
        a.append(elemento)  # a -> [1,2,3,1,2,3]
    b = b + [4]  # Pierde la referencia -> Ya lista2 no se va a modificar, se queda en [1, 2, 3]
    a[-1] = 100  # a -> [1,2,3,1,2,3,100]
    del b[0]  # borra en esa posicion
    return b[:]  # Esto que retorna seria la lista 3


lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

lista3 = modifica(lista1, lista2)

print(lista1)
print(lista2)
print(lista3)