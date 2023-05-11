from sys import stdin,stdout
from math import ceil

INF = pow(10,9)
while True:
    n = int(stdin.readline())
    if n == 0:
        break
    L,H,D = 0,INF,1
    for _ in range(n):
        p = stdin.readline().split()
        if p[0] == "greater":
            L = max(L,int(p[2]))
        elif p[0] == "less":
            H = min(H,int(p[2]))
        else: #divisible
            d = int(p[2])
            if D % d:
                D *= d
    if H == INF:
        stdout.write("infinite\n")
    else:
        first = ceil((L + 1)/ D) * D
        ans = [str(i) for i in range(first,H,D)]
        if ans:
            stdout.write(" ".join(str(a) for a in ans))
            stdout.write("\n")
        else:
            stdout.write("none\n")
