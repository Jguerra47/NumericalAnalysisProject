package main

import (
	"fmt"

	"github.com/Jguerra47/NumericalAnalysisProject/apis/goApi/internal/methods"
	"github.com/Jguerra47/NumericalAnalysisProject/apis/goApi/utils"
)

func main() {
	// // Bisection
	// // function - left - rigth - tolerance - iterations
	// res, err := methods.Bisection("x**3", -3, 6, 0.0001, 20)
	// if err != nil {
	// 	fmt.Println(err)
	// } else {
	// 	utils.PrintMatrix(res.Result)
	// 	fmt.Println(res.Ans)
	// }

	// Newton
	// function - x0 - fx - dfc - error
	res, err := methods.Secant("x**3", -3, 6, 0.0001, 20)
	if err != nil {
		fmt.Println(err)
	} else {
		utils.PrintMatrix(res.Result)
		fmt.Println(res.Ans)
	}
}
