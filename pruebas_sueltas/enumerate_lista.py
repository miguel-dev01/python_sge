import random

nombres = ["Juan", "María", "Pedro", "Ana"]
random.shuffle(nombres)

for indice, nombre in enumerate(nombres):
    print(f"El nombre en la posición {indice} es: {nombre}")