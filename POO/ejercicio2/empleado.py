class Empleado:
    def __init__(self, nombre: str = "Miguel", edad: int = 10, salario: float = 2000.0):
        self.nombre = nombre
        if edad >= 18 and edad <= 45:
            self.edad = edad
        else:
            self.edad = 18
        self.salario = salario

    def mostrar_clasificacion(edad):
        result = ""
        if edad <= 21:
            result = "Principiante"
        elif edad >= 22 and edad <= 35:
            result = "Senior"
        return result

    def aumentar_salario(self, porcentaje):
        aumento = self.salario * porcentaje / 100
        self.salario += aumento

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}"