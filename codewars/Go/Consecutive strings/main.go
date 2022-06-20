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
	for i := 0; i < len(strarr)-k+1; i++ {
		if len(strarr[i:i+k]) > max {
			max = len(strarr[i:i+k])
		}
	}
	return strings.Join(strarr[:max], "")
	
}

func main() {
	fmt.Println(LongestConsec([]string{"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"}, 2))
}