package main

import (
	"fmt"
	"math"
)
func intToInt64(nums []int) []int64 {
	res := make([]int64, len(nums))
	for i, v := range nums {
		res[i] = int64(v)
	}
	return res
}
func sort(nums []int) []int {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i] > nums[j] {
				nums[i], nums[j] = nums[j], nums[i]
			}
		}
	}
	return nums
}
func Decompose(n int64) []int64 {
	var goal int
	var current int
	result := []int{int(n)}
	for len(result) > 0 {
		// fmt.Println("result", result)
		// fmt.Println("current:", (current))
		current = int(result[len(result)-1])
		result = append(result[0:len(result)-1])
		goal += int(math.Pow(float64(current), 2))
		// fmt.Println("goal:",goal)
		
		for i := (current - 1); i > 0; i = i-1 {
			// fmt.Println("i:", i)
			if (goal - int(math.Pow(float64(i), 2))) >= 0 {
				goal -= int(math.Pow(float64(i), 2))
				// fmt.Println("goal", goal)
				result = append(result, int(i))
				if goal == 0 {
					result = sort(result)
					return intToInt64(result)
				}
			} else {
				// print("too large ")
			}
		}
	}
	return nil
}

func main() {
	fmt.Println(Decompose(2))
}
