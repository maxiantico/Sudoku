#para pruebas de codigo sudoku#
from mapas import MAPAS
import random

def crear_juego(juego = random.choice(MAPAS)):
    juego = juego('\n'.join)
    print(juego)
    
    '''
    Dada una representación en cadena de un juego de Sudoku,
    devuelve un juego de Sudoku.

    El juego de Sudoku se representa como una matriz de 9x9
    donde cada elemento es un número entero o la constante
    VACIO para indicar que no se escribió ningún número en 
    esa posición.

    La representación es una cadena con el siguiente formato:

    003020600
    900305001
    001806400
    008102900
    700000008
    006708200
    002609500
    800203009
    005010300

    Donde un 0 significa que la casilla está vacía.
    '''
    print(len(juego))
    tablero = []
    for i in range(juego):
        fila = []
        for j in range(9):
            if j <= 9:
                fila.append(i)
            else:
                fila.append(0)
        tablero.append(fila)
    return tablero
    print (tablero)


crear_juego(game = random.choice(MAPAS))