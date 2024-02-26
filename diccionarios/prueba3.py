def lista_dentro_de_direcciones(lista_direcciones):
    resultado = ""
    for direccion in lista_direcciones:
        for elemento in direccion:
            resultado += str(elemento) + " "
        resultado += "\n"
    return resultado.strip()

def direcciones_dentro_de_lista(direcciones):
    resultado = []
    for direccion in direcciones:
        resultado.append(" ".join(map(str, direccion)))
    return "\n".join(resultado)

# Ejemplo de uso:


direcciones = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado_lista_a_direcciones = lista_dentro_de_direcciones(direcciones)
print("Lista dentro de direcciones:")
print(resultado_lista_a_direcciones)

lista = ["1 2 3", "4 5 6", "7 8 9"]
resultado_direcciones_a_lista = direcciones_dentro_de_lista(lista)
print("\nDirecciones dentro de lista:")
print(resultado_direcciones_a_lista)
