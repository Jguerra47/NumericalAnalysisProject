package utils

import (
	"fmt"
	"math"
)

func PrintMatrix(m [][]string) {
	s := 0
	for i := 0; i < len(m); i++ {
		for j := 0; j < len(m[i]); j++ {
			s = int(math.Max(float64(s), float64(len(m[i][j]))))
		}
	}
	for i := 0; i < len(m); i++ {
		for j := 0; j < len(m[i]); j++ {
			fmt.Printf(" %20s |", m[i][j])
		}
		fmt.Println()
	}
}
