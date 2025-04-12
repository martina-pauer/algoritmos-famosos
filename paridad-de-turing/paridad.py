#!/usr/bin/python3

def paridad_turing(digitos : list) -> list:
    '''
        Cuenta cuantos digitos '1' hay en la lista de digitos,
        si es una cantidad par agrega digito '0' como último digito
        sino agrega 1
    '''
    # Para respetar principio de inmutabilidad de parametros
    resultado = []
    # Hago así para que sean listas independientes (como en una maquina de Turing)
    for digito in digitos:
        # Agrego así para evitar que pueda sincronizarse con el parametro
        resultado.append(digito)
    # Agrego digito que falta    
    if ((digitos.count(1) % 2) == 0):
        # Agrego cero ante paridad de unos para equilibrar
        resultado.append(0)
    else:
        # Agrego uno ante la paridad de ceros para evitar desproporcion
        resultado.append(1)

    return resultado

def corregir(digitos : list) -> str:
    '''
        Reconvierte digitos en un texto para salida
        mas bonita
    '''
    texto = ''
    
    for digito in digitos:
        texto += digito.__str__()
        
    return texto    

# Uso un bucle que recorre listas bidimensionales para hacer demostración
print('\n\tEntrada\t\tSalida\n')
for entrada in [[1, 0, 1], [1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0, 1], [0], [1]]:
    print(f'\t{corregir(entrada)}\t\t{corregir(paridad_turing(entrada))}')