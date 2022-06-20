package main

import (
	"fmt"
	"strconv"
)


func Thirt(n int) int {
	repSqnc := []int{1, 10, 9, 12, 3, 4}
	str_n := strconv.Itoa(n)
	sum := 0
	var a int
	for true {
		a = n
		for i:=0; i<len(str_n); i++ {
			sum = sum + repSqnc[i%len(repSqnc)] * int(str_n[len(str_n)-1-i]-'0')
		}
		str_n = strconv.Itoa(sum)
		n = sum
		if a == sum {
			break
		}
		sum = 0
	}
	return sum
}

func Thirt2(n int) int {
	var t = []int {1,10,9,12,3,4}
	var i,j,k int
	for ; n != k; n = j {
	  for k,i,j = n,0,0; n > 0; i++ {
		j += (n%10) * t[i%6]
		n /= 10
	  }
	}
	return n
  }

func main() {
	fmt.Println(Thirt2(1234567))
}