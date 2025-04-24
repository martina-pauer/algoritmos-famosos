package main

import "fmt"

func contar_unos(numero_binario []uint8) uint64 {

	var unos uint64 = 0

	for bit := 0; bit < len(numero_binario); bit += 1 {
		if numero_binario[bit] == 1 {
			unos += 1
		}
	}

	return unos
}

func main() {

	numero := make([]uint8, 3, 64)

	numero[0] = 0

	numero[1] = 1

	numero[2] = 0

	if (contar_unos(numero) % 2) == 0 {

		numero = append(numero, 0)

		fmt.Println("Agrego cero: ", numero)

	} else {

		numero = append(numero, 1)

		fmt.Println("Agrego uno: ", numero)
	}
}
