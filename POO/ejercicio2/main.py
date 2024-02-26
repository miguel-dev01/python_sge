from empleado import Empleado
from programador import Programador

def main():
    print("1 - Dar de alta empleados\n"
          "2 - Ver empleados\n"
          "3 - Aumentar su sueldo\n")
    opcion = int(input("Seleccione opción (0 para salir): "))
    empleados = []
    while opcion != 0:
        if opcion == 1:
            empleados = [
                Empleado(),
                Programador("Maria", 50, 2500, 120, "Python"),
                Programador("Angel", 21, 3400, 90, "Java"),
                Programador("Quique", 15, 900, 50, "C#")
            ]
            print("Empleados creados correctamente")
        elif opcion == 2:
            if empleados:
                print("\nLista de empleados:")
                for empleado in empleados:
                    print(empleado)
            else:
                print("No hay empleados dados de alta")
        elif opcion == 3:
            if not empleados:
                print("No hay empleados dados de alta")
            else:
                for programador in empleados:
                    programador.aumentar_salario(50)
                print("El salario de los empleados ha sido aumentado exitosamente")
        else:
            print("Comando no reconocido")
        opcion = int(input("Seleccione opción (0 para salir): "))


if __name__ == main():
    main()