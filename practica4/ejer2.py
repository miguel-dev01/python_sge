femple = [
    {"num_empleado": 1, "nombre": "Juan", "cat": "A", "pais": "Francia"},
    {"num_empleado": 2, "nombre": "Maria", "cat": "B", "pais": "España"},
    {"num_empleado": 3, "nombre": "Carlos", "cat": "A", "pais": "Alemania"},
    {"num_empleado": 4, "nombre": "Luisa", "cat": "D", "pais": "Italia"},
    {"num_empleado": 5, "nombre": "Miguel", "cat": "D", "pais": "España"},
]

suma_empleados_categoria = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
suma_empleados_pais = {
    "Francia": 0,
    "España": 0,
    "Portugal": 0,
    "Alemania": 0,
    "Italia": 0,
    "Noruega": 0,
    "China": 0,
}

for e in femple:
    suma_empleados_categoria[e["cat"]] += 1
    suma_empleados_pais[e["pais"]] += 1

# Obtener numero total de empleados por categoría
print("Total de empleados por categoria", suma_empleados_categoria)

# Número total de empleados por país
print("Total de empleados por pais", suma_empleados_pais)

# País con máximo número de empleados (se supone que no hay
# dos países coincidentes en ello)
for pais in suma_empleados_pais:
    if suma_empleados_pais[pais] == max(suma_empleados_pais.values()):
        print("Pais con mas empleados", pais)
