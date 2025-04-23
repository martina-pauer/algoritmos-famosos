def recorrer_filas(recorrida : list, posicion : list) -> list:
    '''
        Recorre filas hasta una posicion de una
        matriz, luego recorre por filas hasta estar en 
        la posicion devolviendo camino realizado
    '''
    camino = []

    columna, fila = 0, 0

    while (fila != posicion[0]):
        camino.append(recorrida[fila][columna])
        fila += 1

    camino.append(recorrida[0][1])

    while (columna != posicion[1]):
        camino.append(recorrida[fila][columna])
        columna += 1
    
    camino.append(recorrida[fila][columna])

    return camino