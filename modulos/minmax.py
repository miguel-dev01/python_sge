def min(a, b):
    if a < b:
        return a
    else:
        return b


def max(a, b):
    if a > b:
        return a
    else:
        return b

# Este código se ejecutará solo si el script es ejecutado directamente
if __name__ == "__main__":
    print("hola")
    print(min(3, 4))
    print(max(3, 4))
    print(id(min)) # Enlace a la función min
