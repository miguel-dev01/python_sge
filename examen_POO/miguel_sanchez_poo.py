# Miguel Sanchez 2DAM - python
class Vagon:
    def __init__(self, numero_v: int, capacidad: int = 4):
        self.numero_v = numero_v
        self.capacidad = capacidad
        self.pasajeros = {}

    def asientos_libres_vagon(self):
        contador_asientos = 0
        for clave, valor in self.pasajeros.items():
            contador_asientos += valor
            if contador_asientos == self.capacidad:
                return 0
        return self.capacidad - contador_asientos

    def asignar_asientos_vagon(self, dni_cliente, num_asientos):
        asientos_disponibles = self.asientos_libres_vagon()
        if num_asientos > asientos_disponibles:
            return False

        dnis = self.pasajeros.keys()
        if dni_cliente in dnis:
            self.pasajeros[dni_cliente] += num_asientos
        else:
            self.pasajeros[dni_cliente] = num_asientos
        return True

    def pasajeros_vagon(self):
        cadena = ""
        cadena += f"Vagon numero: {self.numero_v} - Capacidad: {self.capacidad} - Libres: {self.asientos_libres_vagon()}\n"
        cadena += "Pasajeros: "
        for clave, valor in self.pasajeros.items():
            cadena += f"\n\t\t{clave}: Asientos {valor}"
        return cadena


# Datos demo
# vagon = Vagon(1)
# print(vagon.asientos_libres_vagon())

# vagon.asignar_asientos_vagon("1234456A", 0)
# vagon.asignar_asientos_vagon("1111111X", 0)

# print(vagon.pasajeros_vagon())


class Tren:
    def __init__(self, nombre: str, n_vagones: int = 2):
        self.nombre = nombre
        self.n_vagones = n_vagones
        self.vagones = [Vagon(i+1) for i, vagon in enumerate(range(n_vagones))]

    def comprar_billetes(self, dni_cliente, numero_asientos):
        i = 0
        while i < len(self.vagones) and numero_asientos > self.vagones[i].asientos_libres_vagon():
            i += 1
        if i < len(self.vagones):
            self.vagones[i].asignar_asientos_vagon(dni_cliente, numero_asientos)
            return f"Tren: {self.nombre}. Vagon: {self.vagones[i].numero_v}. Asientos: {numero_asientos}"
        else:
            return "No hay billetes en el mismo vagon"

    def __str__(self):
        cadena = ""
        cadena += "Tren: " + self.nombre + "\n"
        for vagon in self.vagones:
            cadena += vagon.pasajeros_vagon() + "\n"
        return cadena


print("1 - Crear tren\n"
      "2 - Comprar billetes\n"
      "3 - Visualizar tren\n"
      "4 - Salir\n")
opcion = 0
tren = None
while opcion != 4:
    try:
        opcion = int(input("Teclee una opcion (4 Salir): "))
    except ValueError:
        print("Solo se permiten valores numericos")
    if opcion == 1:
        nombre_tren = input("Introduce nombre del tren: ")
        tren = Tren(nombre_tren)
        print(f"Tren {tren.nombre} creado correctamente")
    elif opcion == 2:
        dni_cliente = input("Teclee el dni: ")
        cantidad_billetes = int(input("Teclee cantidad de billetes: "))
        print(tren.comprar_billetes(dni_cliente, cantidad_billetes))
    elif opcion == 3:
        if tren is not None:
            print(tren)
        else:
            print("No hay tren creado todavia")
    elif opcion == 4:
        print("Saliendo...")
    else:
        print("Comando no reconocido")
