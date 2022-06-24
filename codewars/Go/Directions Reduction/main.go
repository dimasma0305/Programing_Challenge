package main

import (
	"fmt"
)

func DirReduc(arr []string) []string {
	dict := map[string]string{
		"NORTH": "SOUTH",
		"EAST":  "WEST",
		"SOUTH": "NORTH",
		"WEST":  "EAST",
	}
	res := []string{}
	for _, i := range arr {
		if len(res) != 0 && dict[i] == res[len(res)-1] {
			res = res[:len(res)-1]
		} else {
			res = append(res, i)
		}

	}
	return res
}

func main() {
	fmt.Println(DirReduc([]string{"NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"}))
}
