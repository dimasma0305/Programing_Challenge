```go
package main

import (
	"fmt"
	"strings"
)

func solution(str, ending string) bool {
	//if part of ending in str return true
	if len(str) < len(ending) {
		return false
	}
	if strings.Contains(str, ending) {
		return true
	}
	return false
}

func main() {
	fmt.Println(solution("abcde", "cde"))
	fmt.Println(solution("abcde", "abc"))
	fmt.Println(solution("abcde", "abcd"))
	fmt.Println(solution("abcde", "abcde"))
	fmt.Println(solution("abcde", "abcdef"))
	fmt.Println(solution("abcde", "abcdefg"))
}

```