def recorrer_filas(recorrida : list, posicion : list) -> list:
    '''
        Recorre filas hasta una posicion de una
        matriz, luego recorre por filas hasta estar en 
        la posicion devolviendo camino realizado
    '''
    camino = []

    columna, fila = 0, 0

    for filas in recorrida:
        
        camino.append(filas[columna])

        if ((fila == posicion[0]) and (fila < len(filas))):
            columna += 1
        elif ((fila == posicion[0]) and (columna == posicion[1])):
            break

        fila += 1   

    return camino    