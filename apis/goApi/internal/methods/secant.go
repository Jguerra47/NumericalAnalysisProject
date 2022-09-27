package methods

import (
	"errors"
	"fmt"
	"math"

	"github.com/Jguerra47/NumericalAnalysisProject/apis/goApi/internal/domain"
	"github.com/Jguerra47/NumericalAnalysisProject/apis/goApi/utils"
	"github.com/Knetic/govaluate"
)

func Secant(f string, x0, x1, tol float64, n int) (domain.ResultLine, error) {
	exp, err := govaluate.NewEvaluableExpression(f)
	if err != nil {
		return domain.ResultLine{}, errors.New("Expression mal formed")
	}
	params := make(map[string]interface{})

	ans := domain.ResultLine{}

	params["x"] = x0
	aux, _ := exp.Evaluate(params)
	fx0, _ := aux.(float64)

	if fx0 == 0.0 {
		s := fmt.Sprintf("%v is a root.\n", utils.ConvF(fx0))
		ans.Ans = s
	} else {
		arr := make([]string, 0)
		arr = append(arr, "counter", "xn", "y1", "error")
		ans.Result = append(ans.Result, arr)

		params["x"] = x1
		aux, _ = exp.Evaluate(params)
		fx1, _ := aux.(float64)
		d := (fx1 - fx0)
		errAns := tol + 1
		counter := 1

		arr = make([]string, 0)
		arr = append(arr, fmt.Sprintf("%d", counter), utils.ConvF(x1), utils.ConvF(fx1), utils.ConvF(errAns))
		ans.Result = append(ans.Result, arr)

		for fx1 != 0.0 && errAns > tol && counter < n && d != 0 {
			x2 := x1 - ((fx1 * (x1 - x0)) / d)
			errAns = math.Abs(x2 - x1)
			x0 = x1
			fx0 = fx1

			params["x"] = x2
			aux, _ = exp.Evaluate(params)
			fx1, _ = aux.(float64)

			x1 = x2
			d = (fx1 - fx0)
			counter++

			arr = make([]string, 0)
			arr = append(arr, fmt.Sprintf("%d", counter), utils.ConvF(x1), utils.ConvF(fx1), utils.ConvF(errAns))
			ans.Result = append(ans.Result, arr)
		}

		if fx1 == 0.0 {
			s := fmt.Sprintf("%v is a root.\n", utils.ConvF(x1))
			ans.Ans = s
		} else if errAns < tol {
			s := fmt.Sprintf("%v is an approximation with tolerance %v.\n", utils.ConvF(x1), tol)
			ans.Ans = s
		} else if d == 0.0 {
			s := fmt.Sprintf("denominator is zero, fail.")
			ans.Ans = s
		} else {
			s := fmt.Sprintf("The method fails in iterarion %d.\n", counter)
			ans.Ans = s
		}
	}
	return ans, nil
}
