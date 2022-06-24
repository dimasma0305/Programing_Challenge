package main

import (
	"fmt"
)

func DirReduc(arr []string) []string {
	var (
		n int
		e int
		s int
		w int
	)
	for i := 0; i < len(arr); i++ {
		switch arr[i] {
		case "NORTH":
			n += 1
		case "EAST":
			e += 1
		case "SOUTH":
			s += 1
		case "WEST":
			w += 1
		}
	}
	NminS := n - s
	EminW := e - w
	newArr := []string{}
	if NminS < 0 {
		newArr = arrAppend(newArr, "SOUTH", NminS*NminS)
	}
	if NminS > 0 {
		newArr = arrAppend(newArr, "NORTH", NminS)
	}
	if EminW < 0 {
		newArr = arrAppend(newArr, "WEST", EminW*EminW)
	}
	if EminW > 0 {
		newArr = arrAppend(newArr, "EAST", NminS)
	}
	return newArr

}
func arrAppend(arr []string, txt string, dup int) []string {
	var n []string
	for i := 0; i < dup; i++ {
		n = append(n, txt)
	}
	return n
}

func main() {
	fmt.Println(DirReduc([]string{}))
}
