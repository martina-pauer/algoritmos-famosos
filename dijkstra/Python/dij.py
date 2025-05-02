#!/usr/bin/python3
from grafon import grafo

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

for recorrer in partes:
   if ((chr(recorrer.vertice_origen) == inicio) or (chr(recorrer.vertice_destino) == inicio) or (chr(recorrer.vertice_origen) == fin) or (chr(recorrer.vertice_destino) == fin)):
      if recorrer.ponderado < 2:
         continue
      else:
          recorrido.append(recorrer)


print(f'\nEl recorrido de Dijkstra encontrado es {representar(recorrido).__str__()}')   