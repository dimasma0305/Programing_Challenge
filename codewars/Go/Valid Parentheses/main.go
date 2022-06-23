package main

import (
	"fmt"
	"regexp"
	"strings"
)

func ValidParentheses(parens string) bool {
	if len(parens)%2 != 0 {
		return false
	}
	dict := map[string]string{"(": ")"}
	var stack []string
	for _, i := range parens {

		if _, ok := dict[string(i)]; ok {
			stack = append(stack, string(i))
		} else {
			if len(stack) == 0 {
				return false
			}
			a := stack[len(stack)-1]
			stack = append(stack[:len(stack)-1], stack[len(stack)+1-1:]...)
			if string(i) != dict[a] {
				return false
			}
		}
	}

	return len(stack) == 0
}
func ValidParentheses(parens string) bool {
	b := 0
	for _, c := range parens {
		if c == '(' {
			b++
		} else {
			b--
			if b < 0 {
				return false
			}
		}
	}
	return b == 0
}
func ValidParentheses(parens string) bool {
	_, err := regexp.Compile(parens)
	return err == nil
}
func ValidParentheses(parens string) bool {
	for strings.Contains(parens, "()") {
		parens = strings.Replace(parens, "()", "", -1)
	}
	return len(parens) == 0
}

func main() {
	fmt.Println(ValidParentheses("(())((()((()))))"))
}
