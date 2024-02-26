a = (0, [1, 2], "hola", {3: 5, 7: (6, 7), 8: [9, 10]})


# a[2] = "Pepe" -> Es inmutable, no cambia
# a[1] = 0 --> No se puede cambiar
# a[1][1] = 5 --> si
# a[3][3] = [3, 7] --> si
# a[3][7] = "hola"
# a[3][7][0] = 5 --> No se puede cambiar, por que el nivel al que se ha accedido es tupla
# a[3][8][0] = 5 -> Si se puede cambiar
