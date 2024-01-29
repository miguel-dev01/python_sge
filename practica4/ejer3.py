notas = []
numero_alumno = 1
print("Introduce notas de alumnos, ENTER para terminar:")
nota = input(f"Nota del alumno {numero_alumno}: ")
while nota != "ENTER":
    try:
        notas.append(float(nota))
        numero_alumno += 1
        nota = input(f"Nota del alumno {numero_alumno}: ")
    except ValueError:
        print("Error: Introduce un número válido.")

print("Se han introducido las siguientes notas:")
numero_alumno = 1
for nota in notas:
    print(f"Alumno {numero_alumno}: " + str(nota))
    numero_alumno += 1

print("Resumen de notas:")
print("Numero de alumnos: " + str(len(notas)))
print("Aprobados: " + str(len([nota for nota in notas if nota >= 5])))
print("Suspensos: " + str(len([nota for nota in notas if nota < 5])))
print(f"Media: {sum(notas) / len(notas)}")

################################################################################

# while True:
#     nota = input(f"Nota del alumno {numero_alumno}: ")
#     if nota == "ENTER":
#         break
#     try:
#         notas.append(float(nota))
#         numero_alumno += 1
#     except ValueError:
#         print("Error: Introduce un número válido.")

# print("Se han introducido las siguientes notas:")
# for i, nota in enumerate(notas, start=1):
#     print(f"Alumno {i}: {nota}")

# print("Resumen de notas:")
# num_alumnos = len(notas)
# aprobados = sum(nota >= 5 for nota in notas)
# suspensos = num_alumnos - aprobados
# media = sum(notas) / num_alumnos

# print("Numero de alumnos:", num_alumnos)
# print("Aprobados:", aprobados)
# print("Suspensos:", suspensos)
# print("Media:", media)
