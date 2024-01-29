class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def iniciales(self):
        cadena = ''
        for caracter in self.nombre:
            if caracter >= 'A' and caracter <= 'Z':
                cadena = cadena + caracter + '.'
        return cadena

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'

persona1 = Persona('Miguel Sanchez', 20)
print(persona1.iniciales())