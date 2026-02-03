''# Честно-чётное число

Дано n (n ≤ 1e9). Нужно вывести 1, если все цифры n чётные, иначе 0.

## Идея
Пробегаем цифры через n%10 и проверяем чётность.
Сложность: O(k), где k — число цифр (≤ 10).
''
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var n int
	fmt.Fscan(in, &n)

	ok := 1
	for n > 0 {
		d := n % 10
		if d%2 != 0 {
			ok = 0
			break
		}
		n /= 10
	}

	fmt.Fprintln(out, ok)
}