class Diccionario:
    def __init__(self, Nombre="Ingeniero", Editorial="RAE", Nivel="FP"):
        self.Nombre = Nombre
        self.Editorial = Editorial
        self.Nivel = Nivel
        self.dic = dict()

    def IntroducirPalabra(self, Palabra):
        if Palabra in self.dic:
            return "Ya existe"
        else:
            self.dic[Palabra] = list()
            return "Introducida"

    def IntroducirAcepciones(self, Palabra, Acepcion):
        if Palabra in self.dic:
            self.dic[Palabra].append(Acepcion)
            return "Acepción añadida"
        else:
            return "La palabra no existe"

    def __str__(self):
        cadena = f"Diccionario {self.Nombre}\n\n\n"
        palabras = sorted(self.dic.keys())
        for p in palabras:
            cadena += p + ":\n"
            for a in self.dic[p]:
                cadena += f"\t{a}\n"
        return cadena

    def Palabras(self, inicial):
        palabras = sorted(self.dic.keys())
        i = 0
        while i < len(palabras) and not palabras[i].startswith(inicial):
            i += 1
        if i < len(palabras):
            while i < len(palabras) and palabras[i].startswith(inicial):
                print(palabras[i])
                i += 1
        else:
            print("No hay ninguna palabra con esa inicial.")

        """ for palabra in palabras:
            if palabra[0] == inicial:
                print(palabra) """


print(
    "1. Crear diccionario."
    "\n2. Introducir palabra."
    "\n3. Introducir acepción."
    "\n4. Consultar palabras."
    "\n5. Palabras por letra."
)

opcion = int(input("Teclee opción (0 Salir): "))
while opcion != 0:
    if opcion == 1:
        D = Diccionario()
    elif opcion == 2:
        P = input("Palabra: ")
        print(D.IntroducirPalabra(P))
        print(D.dic)
    elif opcion == 3:
        P = input("Palabra: ")
        A = input("Acepción: ")
        print(D.IntroducirAcepciones(P, A))
        print(D.dic)
    elif opcion == 4:
        print(D)
    elif opcion == 5:
        I = input("Letra: ")
        print(D.Palabras(I))
        print(D.dic)
    opcion = int(input("Teclee opción (0 Salir): "))
