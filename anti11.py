from sys import stdin,stdout

MOD = 10**9 + 7
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    fib = [2,3]
    for i in range(n-2):
        fib.append((fib[-1] + fib[-2])%(MOD))
    stdout.write(f"{fib[n-1]}\n")
