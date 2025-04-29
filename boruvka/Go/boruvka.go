package main

import "fmt"

// representacion simplificada de 4 Grafos: Vertice_Origen, Ponderacion, Vertice_Destino
var grafos [4][3]uint8

func main() {

	fmt.Println("\nCarga de 4 grafos\n")

	for fila := 0; fila < len(grafos); fila++ {
		fmt.Println("\tIngrese origen, ponderacion, destino: ")
		for columna := 0; columna < len(grafos[fila]); columna++ {
			fmt.Print("\t\t")
			fmt.Scanln(&grafos[fila][columna])
		}
	}

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

	fmt.Println("\nEl grafo de menor ponderacion es ", grafos[indice][0], ", ", menor, ", ", grafos[indice][2])
}
