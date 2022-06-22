package main

import (
	"fmt"
)

func reverseInts(input []uint64) []uint64 {
	if len(input) == 0 {
		return input
	}
	return append(reverseInts(input[1:]), input[0])
}

func PartsSums(ls []uint64) []uint64 {
	sum := make([]uint64, len(ls)+1)
	for i, e := 0, reverseInts(ls); i < len(ls); i++ {
		sum[len(ls)-i-1] += sum[len(ls)-i] + e[i]
	}
	return sum
}

func PartsSums2(ls []uint64) []uint64 {
	v := make([]uint64, len(ls)+1)
	for i := len(ls) - 1; i >= 0; i-- {
		v[i] = v[i+1] + ls[i]
	}
	return v
}

func main() {
	a := []uint64{1, 2, 3, 4}
	fmt.Println(PartsSums(a))
}
