#!/usr/bin/python3

from grafon import grafo

ponderados = []

print('Implementación simple de algoritmo de bor\u016fvka\n')

for ingresado in range(1, 5):
    ponderados.append(grafo(input('\n\tIngrese vertice origen: '), input('\n\tIngrese ponderación: '), input('\n\tIngrese vertice destino: ')))
    print(f'\n\t\t[ Grafo {ingresado.__str__()} ingresado ]\n')

menor = ponderados[0]

for comparar in ponderados:
    if menor.ponderado >= comparar.ponderado:
        menor = comparar

print(f'\n\nEl grafo(origen, ponderado, destino) con menor ponderación es ({menor.vertice_origen.__str__()}, {menor.ponderado.__str__()}, {menor.vertice_destino.__str__()})\n')