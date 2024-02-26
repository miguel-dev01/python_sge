class Diccionario:
    def __init__(self, nombre="miguel", editorial="DAM", nivel="FP"):
        self.nombre = nombre
        self.editorial = editorial
        self.nivel = nivel
        self.diccionario = {}

    def introducir_palabra(self, palabra):
        if palabra in self.diccionario:
            return "Ya existe"
        else:
            self.diccionario[palabra] = []
            return "Introducido correctamente"

    def introducir_acepciones(self, palabra, acepcion):
        if palabra in self.diccionario:
            self.diccionario[palabra].append(acepcion)
            return "Acepción añadida"
        else:
            return "No existe la palabra"

    def consulta(self):
        pass

    def palabras(self):
        pass

    def __str__(self):
        cadena = f"Diccionario: {self.nombre}\n\n"
        palabras = sorted(self.diccionario.keys())
        for p in palabras:
            cadena += p + ":\n"
            for a in self.dic[p]:
                cadena += f"\t{a}\n"
        return cadena

opcion = int(input("Teclee una opcion (0 Salir): "))
while opcion != 0:
    if opcion == 1:
        dicc = Diccionario()
    elif opcion == 2:
        palabra = input("Palabra: ")
        print(dicc.introducir_palabra(palabra))
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    opcion = int(input("Teclee una opcion: "))