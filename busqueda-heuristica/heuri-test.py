#!/usr/bin/python3

import heuri

matriz = []

filas = 3

columnas = 2

fila_agregada = []

for fila in range(0, filas):

    for columna in range(0, columnas):
        fila_agregada.append(input(f'Ingrese componente ({fila}, {columna}): '))

    matriz.append(fila_agregada)    

    fila_agregada = []

print(heuri.recorrer_filas(matriz, [1, 1]))