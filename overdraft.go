package main

import "fmt"

func main() {
	var n, b int
	fmt.Scan(&n)
	var start, lowest = 0, 0
	for i := 0; i < n; i++ {
		fmt.Scan(&b)
		start += b
		if start < lowest {
			lowest = start
		}
	}
	fmt.Println(-lowest)
}
