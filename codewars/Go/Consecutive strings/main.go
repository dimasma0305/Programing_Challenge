package main

import (
	"fmt"
	"strings"
)

func LongestConsec(strarr []string, k int) string {
	if len(strarr) == 0 || k > len(strarr) || k <= 0 {
		return ""
	}
	max := 0
	var Mystr string
	for i := 0; i < len(strarr)-k+1; i++ {
		if len(strings.Join(strarr[i:i+k], "")) > max {
			max = len(strings.Join(strarr[i:i+k], ""))
			Mystr = strings.Join(strarr[i:i+k], "")
		}
	}
	// fmt.Println(len(strings.Join(strarr[0:2], "")))
	return Mystr
}

func main() {
	fmt.Println(LongestConsec([]string{"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"}, 2))
}