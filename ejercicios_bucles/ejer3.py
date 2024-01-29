import statistics as stats

print("Miguel Sanchez, 2DAM")
print("Introduzca las notas, ENTER para terminar:")

id_alumno = 1
cant_aprobados = 0
cant_suspensos = 0
nota = 0.0
notas = []
comando = ""
# Buscar una mejor solucion al While True
while True:
    comando = input(f"Nota del alumno {str(id_alumno)}: ")
    if comando == "ENTER":
        break
    try:
        nota = float(comando)
    except ValueError:
        print("Error: Debes introducir un valor")
        continue
    notas.append(nota)
    if nota >= 5.0:
        cant_aprobados += 1
    else:
        cant_suspensos += 1
    id_alumno += 1

print("Numero de alumnos:", id_alumno)
print("Aprobados:", cant_aprobados)
print("Suspensos:", cant_suspensos)
print("Nota media:", round(stats.mean(notas), ndigits=2))

# Otra manera de mostrar la media
#print("Nota media:", round(sum(notas) / len(notas), ndigits=2))
