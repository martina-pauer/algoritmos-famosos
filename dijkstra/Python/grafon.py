class grafo():
    '''
        Define una simplificación para representar grafos:

            * grafo.vertice_origen, primer vertice del grafo

            * grafo.ponderado, ponderación del borde entre los vertices

            * grafo.vertice_destino, ultimo vertice del grafo
    '''
    def __init__(self, origen, peso, destino):

        self.vertice_origen = int(origen)

        self.ponderado = int(peso)

        self.vertice_destino = int(destino)