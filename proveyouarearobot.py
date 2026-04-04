from sys import stdin,stdout

MAX = pow(10,9)
#use Miller Rabin's test to check if the number is prime
def isPrime(n):
    if n < 5 or n & 1 == 0 or not n % 3:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or not a % n:
            continue
        #for else construct: if p != n - 1 for i in range(s), return false
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True

n,m = map(int,stdin.readline().split())
grid = [list(map(int,stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        stdout.write("1") if isPrime(grid[i][j]) else stdout.write("0")
    stdout.write("\n")
            
