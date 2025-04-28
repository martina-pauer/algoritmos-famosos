package main

import "fmt"

// representacion simplificada de 4 Grafos: Vertice_Origen, Ponderacion, Vertice_Destino
var grafos [4][3]uint8 = [4][3]uint8{{1, 13, 2}, {1, 7, 2}, {1, 60, 2}, {1, 10, 2}}

func main() {
	var menor uint8 = grafos[0][1]

	var indice uint32

	for grafo_seleccionado := 0; grafo_seleccionado < len(grafos); grafo_seleccionado++ {
		if grafo_seleccionado == len(grafos)-1 {
			break
		} else if menor >= grafos[grafo_seleccionado+1][1] {
			// Compara ponderacion, la guarda junto a la fila donde está el grafo
			menor = grafos[grafo_seleccionado+1][1]
			indice = uint32(grafo_seleccionado)
		}
	}

	fmt.Println("La fila de menor ponderacion es ", grafos[indice][0], ", ", menor, ", ", grafos[indice][2])
}
