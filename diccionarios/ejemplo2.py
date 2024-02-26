# Métodos de diccionarios
# Crear un diccionario
mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder a un valor por clave
print("Nombre:", mi_diccionario["nombre"])

# Agregar un nuevo par clave-valor
mi_diccionario["profesion"] = "Ingeniero"
print("Diccionario después de agregar una nueva entrada:", mi_diccionario)

# Eliminar un par clave-valor
del mi_diccionario["edad"]
print("Diccionario después de eliminar la entrada 'edad':", mi_diccionario)

# Obtener todas las claves
print("Claves del diccionario:", mi_diccionario.keys())

# Obtener todos los valores
print("Valores del diccionario:", mi_diccionario.values())

# Comprobar si una clave existe en el diccionario
print("¿La clave 'ciudad' existe en el diccionario?", "ciudad" in mi_diccionario)

# Diccionarios en listas y viceversa
# Lista de diccionarios
lista_diccionarios = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Pedro", "edad": 35},
    {"nombre": "María", "edad": 28}
]

# Acceder a un elemento de la lista y luego a un valor específico dentro del diccionario
print("Edad de Pedro en la lista de diccionarios:", lista_diccionarios[1]["edad"])

# Lista de claves y valores de un diccionario
claves = ["nombre", "edad", "ciudad"]
valores = ["Carlos", 40, "Barcelona"]

# Construir un diccionario a partir de listas de claves y valores
nuevo_diccionario = dict(zip(claves, valores))
print("Nuevo diccionario construido a partir de listas:", nuevo_diccionario)
