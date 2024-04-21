from sys import stdin,stdout

N = int(stdin.readline())
T = list(map(int,stdin.readline().split()))
for i in range(N - 2, -1, -1):
    T[i] = min(T[i], T[i + 1])
stdout.write(f"{sum(T)}\n")
