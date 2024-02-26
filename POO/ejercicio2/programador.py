from empleado import Empleado

class Programador(Empleado):
    def __init__(self, nombre: str = "Miguel", edad: int = 10, salario: float = 2000.0,
                 lineas_hora: int = None, lenguaje: str = None):
        super().__init__(nombre, edad, salario)
        self.lineas_hora = lineas_hora
        self.lenguaje = lenguaje

    def __str__(self):
        return (f"{super().__str__()}, "
                f"Lineas por hora: {self.lineas_hora}, "
                f"Lenguaje: {self.lenguaje}")