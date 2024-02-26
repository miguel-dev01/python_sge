from alumno import Alumno
from asignatura import Asignatura

def main():
    asignatura1 = Asignatura("Programación", 50)
    asignatura2 = Asignatura("Bases de datos", 40)
    asignatura3 = Asignatura("Sistemas operativos", 70)
    asignatura4 = Asignatura("Montaje y mantenimiento de equipos", 90)

    alumno1 = Alumno("Miguel", 20)
    alumno1.introducir_asignatura(asignatura1)
    alumno1.introducir_asignatura(asignatura2)
    alumno1.introducir_asignatura(asignatura4)

    alumno2 = Alumno("Maria", 19)
    alumno2.introducir_asignatura(asignatura2)
    alumno2.introducir_asignatura(asignatura4)

    alumno3 = Alumno("Juan", 21)
    alumno3.introducir_asignatura(asignatura3)
    alumno3.introducir_asignatura(asignatura4)

    alumnos = [alumno1, alumno2, alumno3]
    for alumno in alumnos:
        print(alumno)


if __name__ == "__main__":
    main()