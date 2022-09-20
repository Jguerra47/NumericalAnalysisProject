package utils

import "strconv"

func ConvF(f float64) string {
	return strconv.FormatFloat(f, 'g', -1, 32)
}
