package main

import (
	"fmt"
	"strings"
)

var (
	// make a morse dict
	morseDict = map[string]string{
		"A": ".-", "B": "-...",
		"C": "-.-.", "D": "-..", "E": ".",
		"F": "..-.", "G": "--.", "H": "....",
		"I": "..", "J": ".---", "K": "-.-",
		"L": ".-..", "M": "--", "N": "-.",
		"O": "---", "P": ".--.", "Q": "--.-",
		"R": ".-.", "S": "...", "T": "-",
		"U": "..-", "V": "...-", "W": ".--",
		"X": "-..-", "Y": "-.--", "Z": "--..",
		"1": ".----", "2": "..---", "3": "...--",
		"4": "....-", "5": ".....", "6": "-....",
		"7": "--...", "8": "---..", "9": "----.",
		"0": "-----", ", ": "--..--", ".": ".-.-.-",
		"?": "..--..", "/": "-..-.", "-": "-....-",
		"(": "-.--.", ")": "-.--.-"}
)

func DecodeMorse(morseCode string) string {
	var result string
	var citext string // store morse code, singgle character
	var cntspc int    // count space

	// split string by space
	arr := strings.Split(morseCode, " ")
	for _, val := range arr {
		// if space, add space to result
		if val == "" {
			result += " "
			cntspc++
		} else {
			// search through morse dict
			citext = search(val, morseDict)
			if citext != "" {
				result += citext
			}
		}
	}
	return strings.TrimSpace(result)
}
func search(byt string, dic map[string]string) string {
	// search through key and val
	for key, val := range dic {
		if val == byt {
			return key
		}
	}
	return ""
}
func main() {
	fmt.Println(DecodeMorse(".... . -.--   .--- ..- -.. ."))
}
