class Asignatura:
    def __init__(self, nombre, nota: float):
        self.nombre = nombre
        self.nota = nota

    @property
    def get_nota(self):
        return self.nota

    def set_nota(self, nota):
        self.nota = nota

    def saber_calificacion(self):
        if self.nota >= 60:
            return "Aprobado :)"
        else:
            return "Reprobado :("

    def consultar_nombre_asig(self):
        return self.nombre

    def __str__(self):
        return f"Asignatura: {self.nombre}\nNota: {self.nota}\nCalificación: {self.saber_calificacion()}"