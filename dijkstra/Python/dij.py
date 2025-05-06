#!/usr/bin/python3
from grafon import grafo

def contiene(grafos : list, valor_1 : str, valor_2 : str) -> bool:
    '''
        Dice si entre todos los vertices de los
        grafos hay dos caracters
    '''
    por_ahora = False

    for graf in grafos:
        por_ahora = ((chr(graf.vertice_destino) == valor_1) or (chr(graf.vertice_origen) == valor_1))

        if por_ahora:
            break

    for graf in grafos:
        por_ahora = por_ahora and ((chr(graf.vertice_destino) == valor_2) or (chr(graf.vertice_origen) == valor_2))

        if por_ahora:
            break

    return por_ahora

def representar(grafos : list):
    '''
        Genera una salida para saber contenido de
        un grafo en formato legible
    '''
    salida = ''

    for objeto in grafos:
        salida += f'({chr(objeto.vertice_origen)} - {objeto.ponderado} - {chr(objeto.vertice_destino)})'

        if objeto != grafos[len(grafos) - 1]:
            salida += ' - '

    return salida

primera_parte = grafo(97, 1, 98)

segunda_parte = grafo(98, 3, 99)
# Si lleva solo a un vertice el peso es 1 sino por cada nuevo vertice sube 1
tercera_parte = grafo(100, primera_parte.ponderado + 1, 99)

cuarta_parte = grafo(100, 1, 102)

quinta_parte = grafo(99, tercera_parte.ponderado + 1, 97)

partes = [primera_parte, segunda_parte, tercera_parte, cuarta_parte, quinta_parte]

print(f'El grafo es: {representar(partes)}\n')

inicio = input('\tIngrese caracter de inicio: ')

fin = input('\tIngrese caracter a donde ir: ')

recorrido = []

menor_ponderacion = partes[0].ponderado

mayor_ponderacion = partes[1].ponderado

for recorrer in partes:
    if (recorrer.ponderado < menor_ponderacion):
        menor_ponderacion = recorrer.ponderado
    elif (recorrer.ponderado >= mayor_ponderacion):
        mayor_ponderacion = recorrer.ponderado

for recorriendo in partes:
    if contiene(recorrido, inicio, fin):
        break
    elif ((chr(recorriendo.vertice_origen) == inicio) or (chr(recorriendo.vertice_destino) == fin)) and (recorriendo.ponderado >= menor_ponderacion) and (recorriendo.ponderado < mayor_ponderacion):
        recorrido.append(recorriendo)   
    elif ((chr(recorriendo.vertice_origen) == inicio) or (chr(recorriendo.vertice_destino) == fin)) and (recorriendo.ponderado >= menor_ponderacion) and (recorriendo.ponderado <= mayor_ponderacion):
        recorrido.append(recorriendo)
        break
print(f'\nEl recorrido de Dijkstra encontrado es {representar(recorrido).__str__()}')