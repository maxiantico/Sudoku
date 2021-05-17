from mapas import MAPAS
import random
from sudoku import obtener_origen_region

juego = random.choice(MAPAS)
juego = """903020600
000305001
001806400
008102900
700000008
006708200
002609500
800203009
005010309"""
juego = juego.split("\n")


def armar_tablero(juego):
    tablero = []
    for i in juego:
        fila=[]
        for valor in i:
            valor_fila=int(valor)
            fila.append(valor_fila)
        tablero.append(fila)
    return tablero


def hay_valor_en_region(sudoku, fila, columna, valor):
    '''
    Devuelve True si hay hay algún casillero con el valor `valor`
    en la región de 3x3 a la que corresponde la posición (fila, columna).

    Ver como se agrupan las regiones en la documentación de la función
    obtener_origen_region.
    
    Por ejemplo, para la posición (fila = 0, columna = 1) deberán revisar 
    si está `valor` en todas las siguientes celdas:
    (0, 0), (0, 1) (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2).
    '''
    
    
    region_1 = ((0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2))
    region_2 = ((0,3), (0,4), (0,5), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5))
    region_3 = ((0,6), (0,7), (0,8), (1,6), (1,7), (1,8), (2,6), (2,7), (2,8))
    region_4 = ((3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2))
    region_5 = ((3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5))
    region_6 = ((3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8))
    region_7 = ((6,0), (6,1), (6,2), (7,0), (7,1), (7,2), (8,0), (8,1), (8,2))
    region_8 = ((6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5))
    region_9 = ((6,6), (6,7), (6,8), (7,6), (7,7), (7,8), (8,6), (8,7), (8,8))
    
    all_regions = (region_1, region_2, region_3, region_4, region_5, region_6, 
                   region_7, region_8, region_9)
    
    #Obtengo la region donde debo verificar si se encuentra el valor ingresado
    for regions in all_regions:
        if regions[0] == obtener_origen_region(fila, columna):
            region_valor = regions         
    
    
    for region in region_valor:
        if sudoku[(region[0])][(region[1])] == valor and sudoku[(region[0])][(region[1])] != 0:
            return True




sudoku = armar_tablero(juego)
print(hay_valor_en_region(sudoku, 8, 7, 9))
