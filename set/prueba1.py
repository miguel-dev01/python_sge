curso1 = set(["Miguel", "Maria", "Marcos"])
curso2 = set(["Pedro", "Pablo", "Mario"])
curso3 = set(["Carlos", "Alejandro", "Claudia"])

instituto = [curso1, curso2, curso3]

equipo = set(["Miguel", "Claudia"])
pertenece = False

for curso in instituto:
    if equipo.issubset(curso):
        print("El equipo es de un curso")
        pertenece = True
        break

if not pertenece:
    print("No pertenece a ningun curso")

# Son similares a las listas pero con la diferencia de que no se pueden repetir elementos
conjunto = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
conjunto2 = set([1, 1, 2])

print(conjunto)
print(conjunto2)