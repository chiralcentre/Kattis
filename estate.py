from sys import stdin,stdout
from math import sqrt

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    ans = 0
    #let number of terms in AP be i
    #i(2a + i - 1)/2 = n
    #i(2a + i - 1) = 2n
    #a = ((2n/i) - i + 1)/2
    #iterate through all factors of 2*n and for every factor i, check if 2n/i - i + 1 is divisible by 2 and >= 4
    #time complexity O(sqrt(n))
    for i in range(1,int(sqrt(2 * n)) + 1):
        if not (2 * n) % i:
            t = (2 * n) // i - i + 1
            if t >= 4 and not t % 2:
                ans += 1
    stdout.write(f"{ans}\n")
