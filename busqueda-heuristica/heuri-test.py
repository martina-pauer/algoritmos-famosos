#!/usr/bin/python3

import heuri, random

matriz = []

print('Busqueda heuristica en A estrella\n')

filas = int(input('\tIngrese cantidad de filas: '))

columnas = int(input('\tIngrese cantidad de columnas: '))

fila_agregada = []

for fila in range(0, filas):

    for columna in range(0, columnas):
        fila_agregada.append(input(f'\nIngrese componente ({fila}, {columna}): '))

    matriz.append(fila_agregada)    

    fila_agregada = []

recorriendo = 'El recorrido aleatorio es: '

for elemento in heuri.recorrer_filas(matriz, [random.randint(0, filas - 1), random.randint(0, columnas - 1)]):
    recorriendo += f'\n\n\t"{elemento}"'

print(recorriendo)