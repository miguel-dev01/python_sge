from POO.examen1POO.alumno import Alumno


class Aula:
    def __init__(self, ciclo="DAM", curso=1):
        self.ciclo = ciclo
        if curso not in [1, 2]:
            self.curso = 1
        else:
            self.curso = curso
        self.alumnos = []

    def __str__(self):
        alumnos_str = ", ".join([f"{alumno.nombre}" for alumno in self.alumnos])
        return (f"Ciclo: {self.ciclo}\n"
                f"Curso: {self.curso}\n"
                f"Alumnos: {alumnos_str}")

    def insertar_alumno(self, alumno):
        if len(self.alumnos) <= 30:
            self.alumnos.append(alumno)
            return "Aniadido correctamente"
        else:
            return "Aula llena"

    def existe_alumno(self, alumno):
        # Con while
        i = 0
        while i < len(self.alumnos) and self.alumnos[i].nombre != alumno:
            i += 1
        return i < len(self.alumnos)

        # for alumno_i in self.alumnos:
        #     if alumno_i == alumno:
        #         return True
        # return False

    def alumnos_menores(self):
        diccionario = {"menores": []}
        for alumno in self.alumnos:
            edad = alumno.edad
            if edad < 20:
                diccionario["menores"].append(alumno.nombre)
            else:
                rango = edad // 10
                if rango in diccionario:
                    diccionario[rango].append(alumno.nombre)
                else:
                    diccionario[rango] = [alumno.nombre]
        return diccionario


"""
alumno1 = Alumno("Miguel", 15)
alumno2 = Alumno("Maria", 20)
alumno3 = Alumno("Quique", 30)
alumno4 = Alumno("Alex", 47)
alumno5 = Alumno("Angel", 29)

aula = Aula("ASIR", 1)
aula.insertar_alumno(alumno1)
aula.insertar_alumno(alumno2)
aula.insertar_alumno(alumno3)
aula.insertar_alumno(alumno4)
aula.insertar_alumno(alumno5)
print(aula)

print("Existe alumno?", aula.existe_alumno("Diego"))
print("Diccionario:", aula.alumnos_menores())
"""

def main():
    print("Aqui las opciones...")
    aula = None
    alumnos_creados = False
    alumnos = []
    opcion = 0
    while opcion != 8:
        try:
            opcion = int(input("Teclee una opcion (8 Salir): "))
        except ValueError:
            print("Solo valores numericos")
        if opcion == 1:
            alumnos = [
                Alumno("Miguel", 15),
                Alumno("Maria", 20),
                Alumno("Quique", 30),
                Alumno("Alex", 47),
                Alumno("Angel", 29)
            ]
            alumnos_creados = True
            print("Alumnos creados correctamente")
        elif opcion == 2:
            aula = Aula("ASIR")
            print("Aula creada correctamente")
        elif opcion == 3:
            if not alumnos_creados or aula is None:
                print("Primero debes crear los alumnos y el aula.")
            else:
                for alumno in alumnos:
                    aula.insertar_alumno(alumno)
                print("Alumnos insertados en el aula correctamente")
        elif opcion == 4:
            if aula is not None:
                print(aula)
            else:
                print("Debe crear el aula primero")
        elif opcion == 5:
            if aula is not None and alumnos_creados is not False:
                nombre_alumno = input("Introduce el nombre del alumno a buscar: ")
                print("Existe alumno?", aula.existe_alumno(nombre_alumno))
            else:
                print("Debe tener creados los alumnos y las aulas")
        elif opcion == 6:
            if aula is not None and alumnos_creados is not False:
                nombre_alumno = input("Introduce el nombre del alumno: ")
                if aula.existe_alumno(nombre_alumno):
                    print(f"El alumno {nombre_alumno} ya existe")
                    break
                edad_alumno = int(input("Introduce la edad del alumno: "))
                nuevo_alumno = Alumno(nombre_alumno, edad_alumno)
                mensaje = aula.insertar_alumno(nuevo_alumno)
                print(mensaje)
            else:
                print("Aula y alumnos no creados aún.")
        elif opcion == 7:
            if aula is not None:
                print("Alumnos menores:", aula.alumnos_menores())
            else:
                print("Aula no creada todavía.")
        else:
            print("Opcion no reconocida")
        # try:
        #     opcion = int(input("Teclee una opcion (8 Salir): "))
        # except ValueError:
        #     print("Solo valores numericos")
    print("Saliendo...")


if __name__ == "__main__":
    main()