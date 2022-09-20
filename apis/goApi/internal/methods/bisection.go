package methods

import (
	"errors"
	"fmt"
	"math"

	"github.com/Jguerra47/NumericalAnalysisProject/apis/goApi/internal/domain"
	"github.com/Jguerra47/NumericalAnalysisProject/apis/goApi/utils"
	"github.com/Knetic/govaluate"
)

func Bisection(f string, l, r, tol float64, n int) (domain.ResultLine, error) {
	exp, err := govaluate.NewEvaluableExpression(f)
	if err != nil {
		return domain.ResultLine{}, errors.New("Expression mal formed")
	}
	params := make(map[string]interface{})

	params["x"] = l
	aux, _ := exp.Evaluate(params)
	fL := aux.(float64)

	params["x"] = r
	aux, _ = exp.Evaluate(params)
	fR := aux.(float64)

	ans := domain.ResultLine{}

	if fL == 0.0 {
		s := fmt.Sprintf("%v is a root.\n", utils.ConvF(fL))
		ans.Ans = s
		return domain.ResultLine{}, nil
	}
	if fR == 0.0 {
		s := fmt.Sprintf("%v is a root.\n", utils.ConvF(fR))
		ans.Ans = s
		return domain.ResultLine{}, nil
	}

	if fL*fR < 0 {
		mid := (l + r) / 2
		params["x"] = mid
		aux, _ = exp.Evaluate(params)
		fmid := aux.(float64)
		counter := 1
		errAns := tol + 1
		arr := make([]string, 0)
		arr = append(arr, "counter", "left", "right", "xmid", "fmid", "error")
		ans.Result = append(ans.Result, arr)
		for errAns > tol && fmid != 0.0 && counter < n {
			arr = make([]string, 0)
			arr = append(arr, fmt.Sprintf("%d", counter), utils.ConvF(l), utils.ConvF(r), utils.ConvF(mid), utils.ConvF(fmid), utils.ConvF(errAns))
			ans.Result = append(ans.Result, arr)
			if fL*fmid < 0 {
				r = mid
				fR = fmid
			} else {
				l = mid
				fL = fmid
			}
			auxM := mid
			mid = (r + l) / 2
			params["x"] = mid
			aux, _ = exp.Evaluate(params)
			fmid = aux.(float64)
			errAns = math.Abs(mid - auxM)
			counter = counter + 1
		}

		arr = make([]string, 0)
		arr = append(arr, fmt.Sprintf("%d", counter), utils.ConvF(l), utils.ConvF(r), utils.ConvF(mid), utils.ConvF(fmid), utils.ConvF(errAns))
		ans.Result = append(ans.Result, arr)
		if mid == 0.0 {
			s := fmt.Sprintf("%v is a root.\n", utils.ConvF(mid))
			ans.Ans = s
		} else if errAns < tol {
			s := fmt.Sprintf("%v is an approximation with tolerance %v.\n", utils.ConvF(fR), tol)
			ans.Ans = s
		} else {
			s := fmt.Sprintf("The method fails in iterarion %d.\n", counter)
			ans.Ans = s
		}
		return ans, nil
	}

	return domain.ResultLine{}, nil
}
