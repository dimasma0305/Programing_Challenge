package main

import "fmt"

func PartsSums(ls []uint64) []uint64 {
	var sum []uint64
	var sum2 uint64
	lenLs := len(ls)
	for j := 0; j < lenLs; j++ {
		sum2 += ls[j:]
		sum = append(sum, sum2)
		sum2 = 0
	}
	sum = append(sum, 0)
	return sum
}

func main() {
	a := []uint64{1, 2, 3, 4, 5, 6}
	fmt.Println(PartsSums(a))
}
