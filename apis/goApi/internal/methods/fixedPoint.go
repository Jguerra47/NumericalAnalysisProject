package methods

import (
	"errors"
	"fmt"
	. "math"

	"github.com/Jguerra47/NumericalAnalysisProject/apis/goApi/internal/domain"
	"github.com/Jguerra47/NumericalAnalysisProject/apis/goApi/utils"
	"github.com/Knetic/govaluate"
)

func FixedPoint(f, g string, x0, tol float64, n int) (domain.ResultLine, error) {
	exp, err := govaluate.NewEvaluableExpression(g)
	if err != nil {
		fmt.Println(err)
		return domain.ResultLine{}, errors.New("Expression mal formed")
	}
	params := make(map[string]interface{})

	expF, err := govaluate.NewEvaluableExpression(f)
	if err != nil {
		return domain.ResultLine{}, errors.New("Expression mal formed")
	}
	paramsF := make(map[string]interface{})

	ans := domain.ResultLine{}
	errAns := tol + 1
	counter := 1

	arr := make([]string, 0)
	arr = append(arr, "counter", "x", "error")
	ans.Result = append(ans.Result, arr)

	for counter < n && errAns < tol {
		params["x"] = x0
		aux, _ := exp.Evaluate(params)
		fx, _ := aux.(float64)

		errAns = Abs(fx - x0)

		arr = make([]string, 0)
		arr = append(arr, fmt.Sprintf("%d", counter), utils.ConvF(x0), utils.ConvF(errAns))
		ans.Result = append(ans.Result, arr)

		x0 = fx
	}
	paramsF["x"] = x0
	aux, _ := expF.Evaluate(paramsF)
	fx, _ := aux.(float64)
	if fx == 0.0 {
		s := fmt.Sprintf("%v is a root.\n", utils.ConvF(x0))
		ans.Ans = s
	} else if errAns < tol {
		s := fmt.Sprintf("%v is an approximation with tolerance %v.\n", utils.ConvF(x0), tol)
		ans.Ans = s
	} else {
		s := fmt.Sprintf("The method fails in iterarion %d.\n", counter)
		ans.Ans = s
	}
	return ans, nil
}
