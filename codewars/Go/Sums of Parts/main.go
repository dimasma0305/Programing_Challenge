package main

import "fmt"

func PartsSums(ls []uint64) []uint64 {
	var sum2 uint64
	for _, v := range ls {
		sum2 += v
	}
	return sum2
}

func main() {
	a := []uint64{1, 2, 3, 4, 5, 6}
	fmt.Println(PartsSums(a))
}
