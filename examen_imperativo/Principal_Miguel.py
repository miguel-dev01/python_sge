from Examen_Utilidades import *
from random import randint


def introducirJugadores():
    par = False
    numero_jugadores = 0
    while par != True:
        numero_jugadores = int(input("Introduce numero de jugadores: "))
        if numero_jugadores % 2 == 0:
            par = True

    Equipos = []
    equipo1 = {}
    equipo2 = {}
    jugador = ""
    while len(equipo1) != numero_jugadores:
        aleatorio = randint(1, numero_jugadores)
        jugador = str(input("Introduce nombre de jugador: "))
        equipo1[aleatorio] = jugador

    for i in range(int(len(equipo1) / 2), len(equipo1)):
        equipo2[i] = equipo1[i]
        equipo1.pop(i)

    Equipos.append(equipo1)
    Equipos.append(equipo2)

    return Equipos

# print(introducirJugadores())

def mostrarEquipos(lista_jugadores):
    print("Equipos participantes")
    print("-" * 20)

    contador = 0
    for i in lista_jugadores:
        print("Equipo", contador, ":", i)
        contador += 1


def jugadoresTablero(matriz, lista):
    # aleatorio_fila = randint(len(matriz))
    # aleatorio_columna = randint(len(matriz))
    pass




lista = introducirJugadores()
# lista = [{2: "Maria", 4: "Juan"}, {1: "Jose", 3: "Lola"}]
matriz = crearmatriz(5, 5)

jugadoresTablero(matriz, lista)
mostrarEquipos(lista)