# Creamos un objeto lista
lista_original = [1, 2, 3]

# Creamos una nueva variable y la asignamos a la lista original
nueva_lista = lista_original

# Modificamos la nueva lista
nueva_lista.append(4)

# La lista original también se ha modificado,
# ya que ambas variables apuntan al mismo objeto en memoria.
# Tienen el mismo puntero.
print("Lista original:", lista_original)  # Salida: Lista original: [1, 2, 3, 4]
print("Lista nueva:", nueva_lista)

# Ejemplo con un tipo de dato inmutable
# Creamos una variable entera
x = 5

# Creamos una nueva variable y la asignamos a x
y = x

# Modificamos el valor de y
y = 10

# Imprimimos x y y para ver sus valores
print("x:", x)  # Salida: x: 5
print("y:", y)  # Salida: y: 10
