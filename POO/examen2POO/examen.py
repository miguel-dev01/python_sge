class Examen:
    def __init__(self, modulo: str):
        self.modulo = modulo
        self.preguntas = {}

    def __str__(self):
        cadena = ""
        for unidad in self.preguntas:
            cadena += "Tema o unidad: " + unidad + "\n\t"
            for elemento in self.preguntas[unidad]:
                cadena += "Pregunta: " + elemento[0] + "\n\t"
                cadena += "Respuesta: " + elemento[1] + "\n\t"
                cadena += "Puntuación: " + str(elemento[2]) + "\n\t"
            cadena += "\n"
        return cadena

    def insertar_pregunta(self, pregunta, respuesta, puntuacion, unidad="Python"):
        if puntuacion < 0:
            puntuacion = 1
        elif puntuacion > 10:
            puntuacion = 10
        tupla = (pregunta, respuesta, puntuacion)
        if unidad not in self.preguntas.keys():
            self.preguntas[unidad] = [tupla]
        else:
            self.preguntas[unidad].append(tupla)

    def generar_examen(self, unidad, num_preguntas):
        if unidad not in self.preguntas.keys():
            print("La unidad sobre la que quieres generar el examen no existe.")
            return None
        elif num_preguntas > len(self.preguntas[unidad]):
            print("No hay suficientes preguntas en esa unidad.")
            return None
        suma_nota = 0.0
        puntuacion_maxima = sum(suma_nota[2] for suma_nota in self.preguntas[unidad])
        for pregunta in self.preguntas[unidad]:
            usuario_respuesta = input(pregunta[0] + " ")
            if usuario_respuesta == pregunta[1]:
                suma_nota += pregunta[2]

        print("Total preguntas:", len(self.preguntas[unidad]))
        print("Puntuacion maxima posible:", puntuacion_maxima)
        print("Puntuacion obtenida:", suma_nota)


examen1 = Examen("SGE")
examen1.insertar_pregunta("¿De que color es el cielo?:",
                          "Azul", 1.0, "Geologia")
examen1.insertar_pregunta("¿Java o Python?:",
                          "Python", -1.5, "Lenguajes")
examen1.insertar_pregunta("¿Python es compilado o interpretado?:",
                          "interpretado", 2.5, "Lenguajes")
examen1.generar_examen("Geologia", 1)