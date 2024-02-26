from asignatura import Asignatura

class Alumno:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        self.asignaturas = []

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_edad(self, edad):
        self._edad = edad

    def get_edad(self):
        return self._edad

    nombre = property(get_nombre, set_nombre)
    edad = property(get_edad, set_edad)

    def promedio_alumno(self):
        suma_notas = float()
        cant = 0
        for asig in self.asignaturas:
            suma_notas += asig.nota
            cant += 1
        if cant > 0:
            return suma_notas / cant
        else:
            # Por si no hay notas o asignaturas
            return 0.0

    def introducir_asignatura(self, nombre_asignatura: Asignatura):
        if nombre_asignatura not in self.asignaturas:
            self.asignaturas.append(nombre_asignatura)
        else:
            print(f"La asignatura nueva {nombre_asignatura} ya existe en el "
                  f"plan de estudios del alumno")
    
    def __str__(self):
        asignaturas = ", ".join([i.nombre for i in self.asignaturas])
        return (f"Nombre: {self.nombre}\nEdad: {self._edad}\nAsignaturas: {asignaturas}\n"
                f"Promedio: {self.promedio_alumno()}\n")