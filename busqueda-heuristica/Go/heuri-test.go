package main

import (
	"fmt"
)

func recorrido(recorrer [3][2]string, ultima_fila int, ultima_columna int) []string {

	resultado := make([]string, 4, 20)

	resultado[0] = recorrer[0][0]

	for fila := 1; fila < len(recorrer); fila++ {
		if fila != ultima_fila {
			resultado[fila] = recorrer[fila][0]
		} else {
			break
		}
	}

	for columnas := 1; columnas < len(recorrer[0]); columnas++ {
		if columnas == ultima_columna {
			resultado[columnas+1] = recorrer[0][columnas]
		} else {
			break
		}
	}

	resultado[ultima_fila+1] = recorrer[ultima_fila][ultima_columna]

	return resultado
}

func main() {
	var matriz [3][2]string = [3][2]string{{"a", "1"}, {"x", "d"}, {"y", "b"}}

	camino := recorrido(matriz, 2, 1)

	fmt.Print("\nEl recorrido de (0, 0) encontrado hasta posicion (2, 1) es:\n\n")

	for indice := 0; indice < len(camino); indice++ {
		fmt.Println("\tElemento ", indice+1, "\t->\t", camino[indice])
	}
	
	fmt.Println("")

}
