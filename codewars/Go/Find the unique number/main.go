package main

import "fmt"

func FindUniq(arr []float32) float32 {
	count_same := make(map[float32]int)
	for _, v := range arr {
		count_same[v]++
	}
	for k, v := range count_same {
		if v == 1 {
			return k
		}
	}
	return 0
}

func main() {
	fmt.Println(FindUniq([]float32{1, 1, 1, 2, 1, 1}))
}
