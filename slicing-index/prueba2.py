dominio = "www.google.es"
print("Subdominios de", dominio + ":")

for parte in dominio.split('.'):
    print(parte)
print()

print("*" * 100)

x = None
if x is not None:
    print("No esta vacio")
else:
    print("Esta vacio")