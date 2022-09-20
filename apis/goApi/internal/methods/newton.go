package methods

import (
	"errors"
	"fmt"
	"math"

	"github.com/Jguerra47/NumericalAnalysisProject/apis/goApi/internal/domain"
	"github.com/Jguerra47/NumericalAnalysisProject/apis/goApi/utils"
	"github.com/Knetic/govaluate"
)

func Newton(f, fdx string, tol, x0 float64, n int) (domain.ResultLine, error) {
	expF, err := govaluate.NewEvaluableExpression(f)
	if err != nil {
		return domain.ResultLine{}, errors.New("Expression mal formed")
	}
	paramsF := make(map[string]interface{})

	expFdx, err := govaluate.NewEvaluableExpression(fdx)
	if err != nil {
		return domain.ResultLine{}, errors.New("Expression mal formed")
	}
	paramsFdx := make(map[string]interface{})

	ans := domain.ResultLine{}

	paramsF["x"] = x0
	aux, _ := expF.Evaluate(paramsF)
	fx, _ := aux.(float64)

	paramsFdx["x"] = x0
	aux, _ = expFdx.Evaluate(paramsFdx)
	dfx := aux.(float64)

	arr := make([]string, 0)
	arr = append(arr, "counter", "xn", "f(xn)", "f'(xn)", "error")
	ans.Result = append(ans.Result, arr)

	counter := 1
	errAns := tol + 1
	x1 := 0.0

	arr = make([]string, 0)
	arr = append(arr, fmt.Sprintf("%d", counter), utils.ConvF(x0), utils.ConvF(fx), utils.ConvF(dfx), utils.ConvF(errAns))
	ans.Result = append(ans.Result, arr)

	for errAns > tol && fx != 0.0 && dfx != 0.0 && counter < n {
		x1 = x0 - (fx / dfx)
		fmt.Println((fx / dfx))
		paramsF["x"] = x1
		aux, _ = expF.Evaluate(paramsF)
		fx = aux.(float64)

		paramsFdx["x"] = x1
		aux, _ = expFdx.Evaluate(paramsFdx)
		dfx = aux.(float64)

		errAns = math.Abs(x1 - x0)
		x0 = x1
		counter++

		arr = make([]string, 0)
		arr = append(arr, fmt.Sprintf("%d", counter), utils.ConvF(x0), utils.ConvF(fx), utils.ConvF(dfx), utils.ConvF(errAns))
		ans.Result = append(ans.Result, arr)
	}
	if fx == 0.0 {
		s := fmt.Sprintf("%v is a root.\n", utils.ConvF(x0))
		ans.Ans = s
	} else if errAns < tol {
		s := fmt.Sprintf("%v is an approximation with tolerance %v.\n", utils.ConvF(x1), tol)
		ans.Ans = s
	} else if dfx == 0.0 {
		s := fmt.Sprintf("%v is a posible multiple root.\n", utils.ConvF(x1))
		ans.Ans = s
	} else {
		s := fmt.Sprintf("The method fails in iterarion %d.\n", counter)
		ans.Ans = s
	}
	return ans, nil
}
