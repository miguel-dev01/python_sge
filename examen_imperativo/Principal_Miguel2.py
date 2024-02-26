import random

from Examen_Utilidades import *
from random import randint


def introducirJugadores():
    numero_jugadores = int(input("Introduce numero de jugadores: "))
    while numero_jugadores % 2 != 0:
        numero_jugadores = int(input("Introduce numero de jugadores: "))

    equipos = []
    jugadores = []
    for i in range(numero_jugadores):
        jugador = input(f"Introduce nombre del jugador {i + 1}: ")
        jugadores.append(jugador)
    random.shuffle(jugadores)
    mitad = numero_jugadores // 2
    equipo1 = {i + 1: jugadores[i] for i in range(mitad)}
    equipo2 = {i + 1: jugadores[i] for i in range(mitad, numero_jugadores)}

    equipos.append(equipo1)
    equipos.append(equipo2)

    return equipos

# print(introducirJugadores())

def mostrarEquipos(lista_jugadores):
    print("Equipos participantes")
    print("-" * 20)
    contador = 0
    for equipo in lista_jugadores:
        print(f"Equipo {contador}: ", end=" ")
        for clave, valor in list(equipo.items())[:-1]:
            print(f"{clave}. {valor}", end=" - ")
        clave, valor = list(equipo.items())[-1]
        print(f"{clave}. {valor}", end=" ")
        print()
        contador += 1


def jugadoresTablero(matriz, lista):
    for equipo in lista:
        for clave, valor in equipo.items():
            aleatorio_fila = randint(1, len(matriz) - 1)
            aleatorio_columna = randint(1, len(matriz[0]) - 1)
            if matriz[aleatorio_fila][aleatorio_columna] != "-":
                aleatorio_fila = randint(1, len(matriz) - 1)
                aleatorio_columna = randint(1, len(matriz[0]) - 1)
                matriz[aleatorio_fila][aleatorio_columna] = clave
            else:
                matriz[aleatorio_fila][aleatorio_columna] = clave

    for fila in matriz:
        for columna in fila:
            print(columna, end="\t")
        print()


lista = introducirJugadores()
# lista = [{2: "Maria", 4: "Juan"}, {1: "Jose", 3: "Lola"}]
matriz = crearmatriz(5, 5)

mostrarEquipos(lista)
jugadoresTablero(matriz, lista)