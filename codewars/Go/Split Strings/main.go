package main

import "fmt"

func Solution(str string) []string {
	var result []string
	for i := 0; i < len(str); i += 2 {
		if i+1 < len(str) {
			result = append(result, str[i:i+2])
		} else {
			result = append(result, str[i:]+"_")
		}
	}
	return result
}

func main() {
	fmt.Println(Solution("abcdefg"))
}
