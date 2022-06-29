package main

import (
	"fmt"
	"strings"
)

func Rot13(msg string) string {
	var enc []string
	for _, i := range msg {
		if i >= 'a' && i <= 'z' {
			i += 13
			if i > 'z' {
				i -= 26
			}
		}
		
		if i >= 'A' && i <= 'Z' {
			i += 13
			if i > 'Z' {
				i -= 26
			}
		}
		enc = append(enc, string(i))
	}
	return strings.Join(enc, "")
}
func main() {
	fmt.Println(Rot13("dimas"))
}
