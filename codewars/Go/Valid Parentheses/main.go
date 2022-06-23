package main

func ValidParentheses(parens string) bool {
	if len(parens) % 2 != 0 {
		return false
	}
	dict := map[string]string{"(":")"}
	var stack []string
	for _, i := range parens {
		i = string(i)
		if i == dict["("] {

		}
	}

}

func main() {

}