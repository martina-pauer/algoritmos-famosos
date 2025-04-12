#!/usr/bin/python3

# Prueba de implementación de algoritmo Paridad De Turing para equiparar ceros y unos
from paridad import corregir, paridad_turing
# Uso un bucle que recorre listas bidimensionales para hacer demostración
print('\n\tEntrada\t\tSalida\n')
for entrada in [[1, 0, 1], [1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0, 1], [0], [1]]:
    print(f'\t{corregir(entrada)}\t\t{corregir(paridad_turing(entrada))}')