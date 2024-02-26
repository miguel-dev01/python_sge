from Examen_Utilidades import crearmatriz, visualizarmatriz, mover
import random


def IntroducirJugadores():
    numJugadores = int(input("Introduce el número de jugadores (debe ser par): "))
    Equipos = [{}, {}]
    fin = False
    i = 0
    while i < numJugadores:
        i += 1
        jugador = input("Introduce el nombre del jugador: ")
        equipo = random.randint(0, 1)
        if len(Equipos[equipo]) == (numJugadores / 2):
            if equipo == 0:
                equipo = 1
            else:
                equipo = 0
        Equipos[equipo][i] = jugador
    return Equipos


# equipos = [{2: "María", 4: "Juan"}, {1: "José", 3: "Lola"}]


def MostrarEquipos(equipos):
    print("Equipos participantes")
    print("----------\n\n")
    i = 0
    for equipo in equipos:
        print(f"Equipo {i}: ", end=" ")
        for numero, jugador in equipo.items():
            print(f"{numero}. {jugador}", end=" - ")
        print()
        i += 1


def JugadoresTablero(tablero, equipos):
    filasColumnas = len(tablero)
    posiciones = {}
    for equipo in equipos:
        for jugador in equipo:
            x = random.randint(0, filasColumnas - 1)
            y = random.randint(0, filasColumnas - 1)

            while [x, y] in posiciones.values():
                x = random.randint(0, filasColumnas)
                y = random.randint(0, filasColumnas)
            posiciones[jugador] = [x, y]
            if x < len(tablero) and y < len(tablero):
                tablero[x][y] = jugador
    return posiciones


def Jugar(equipos, tablero, posicionesActuales):
    nJugadores = len(posicionesActuales)
    while nJugadores > 0:
        i = 1
        while i < len(posicionesActuales) + 1:
            jugador = posicionesActuales[i]
            if not posicionesActuales[i]:
                i += 1
            print(i)
            print(jugador)
            modoMovimiento = input(
                "¿Deseas moverte por filas (F) o por columnas (C)?: "
            )
            salto = random.randint(1, nJugadores * 2)
            nuevaPosicion = mover(tablero, jugador, modoMovimiento, salto)
            if tablero[nuevaPosicion[0]][nuevaPosicion[1]] == "-":
                tablero[jugador[0]][jugador[1]] = "-"
                jugador = nuevaPosicion
                tablero[nuevaPosicion[0]][nuevaPosicion[1]] = i
            elif tablero[nuevaPosicion[0]][nuevaPosicion[1]] == i:
                tablero[jugador[0]][jugador[1]] = i
            else:
                jEliminar = tablero[nuevaPosicion[0]][nuevaPosicion[1]]
                posicionesActuales.pop(jEliminar)
                tablero[jugador[0]][jugador[1]] = "-"
                jugador = nuevaPosicion
                tablero[nuevaPosicion[0]][nuevaPosicion[1]] = i
                nJugadores -= 1
            visualizarmatriz(tablero)
            i += 1
    jugadorEnPie = posicionesActuales
    if jugadorEnPie:
        i = 0
        for equipo in equipos:
            while not jugadorEnPie in equipo:
                i += 1
        print(f"Ha ganado el equipo {i}.")
    else:
        print("Empate.")


equipos = IntroducirJugadores()
MostrarEquipos(equipos)
tablero = crearmatriz(len(equipos[0]) * 2, len(equipos[0]) * 2)
posicionesActuales = JugadoresTablero(tablero, equipos)
visualizarmatriz(tablero)
Jugar(equipos, tablero, posicionesActuales)