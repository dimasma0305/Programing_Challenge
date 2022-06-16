package main

import (
	"fmt"
)

func Xor(a, b bool) bool {
  return a != b
}

func main() {
  fmt.Println(Xor(true, true))
}